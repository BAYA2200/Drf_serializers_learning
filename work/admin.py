from django.contrib import admin

# Register your models here.
from work.models import Position, Employee

admin.site.register(Position)
admin.site.register(Employee)
