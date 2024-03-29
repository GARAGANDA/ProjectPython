from django.http import JsonResponse
from django.shortcuts import render
import requests

from vacancy.models import TopSkills, MainPage, GeographySalary


# Create your views here.
def hhru_api(request):
    api_url = "https://api.hh.ru/vacancies?text=backend&period=1"
    response = requests.get(api_url)
    response_json = response.json()
    result = []
    value = ''
    date_time = []
    for i in response_json['items'][:10]:
        value = ''
        if i.get('salary') is None:
            value = 'Не указана'
        elif i['salary']['from'] is not None or i['salary']['to'] is not None:
            if i['salary']['from'] is not None:
                value = value + ' от ' + str(i['salary']['from'])
            if i['salary']['to'] is not None:
                value = value + ' до ' + str(i['salary']['to'])
            if i['salary']['currency'] is not None:
                value += ' ' + i['salary']['currency']
        date,time=i['published_at'].split('T')
        time=time[:-5]

        #if value is not '':
        #    value+=i['salary']['currency']
        result.append(
            {'name': i['name'], 'salary': value,
             'area': i['area']['name'], 'employer': i['employer']['name'],
             'date': date+' '+time})
        value=''
    # return JsonResponse(result)
    return render(request, 'hh_api.html', {'vacancies': result})

def top_skills(request):
    res = {}
    res_profession = {}
    years = TopSkills.objects.all().order_by('year').values("year").distinct()
    for ls in years:
        year=ls['year']
        res[year] = TopSkills.objects.filter(year=year, is_profession=False)
        res_profession[year] = TopSkills.objects.filter(year=year, is_profession=True)
    return render(request, 'topskills.html', {'years':years,'res':res,'res_profession':res_profession})

def geography_salary(request):
    res = {}
    res_profession = {}
    areas = GeographySalary.objects.all().order_by('area_name').values("area_name").distinct()
    for ls in areas:
        area = ls['area_name']
        obgs = GeographySalary.objects.filter(area_name=area, is_profession=False)
        if obgs:
            res[area] = obgs
        objs = GeographySalary.objects.filter(area_name=area, is_profession=True)
        if objs:
            res_profession[area] = objs
    return render(request, 'geographysalary.html', {'area_name':areas,'res':res,'res_profession':res_profession})

def relevancy_salary(request):
    res = {}
    res_profession = {}
    years = TopSkills.objects.all().order_by('year').values("year").distinct()
    for ls in years:
        year = ls['year']
        res[year] = TopSkills.objects.filter(year=year, is_profession=False)
        res_profession[year] = TopSkills.objects.filter(year=year, is_profession=True)
    return render(request, 'relevancesalary.html', {'years':years,'res':res,'res_profession':res_profession})

def index(request):
    mainpage = MainPage.objects.filter(is_set=True)[0]
    return render(request,'index.html',{'mainpage':mainpage})


