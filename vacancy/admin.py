from django.contrib import admin

from vacancy.models import TopSkills, GeographySalary, RelevanceSalary, MainPage

# Register your models here.
admin.site.register(TopSkills)
admin.site.register(GeographySalary)
admin.site.register(RelevanceSalary)
admin.site.register(MainPage)