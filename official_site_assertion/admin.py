from django.contrib import admin
from .models import Assertion
from .models import Objective


class AssertionAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'url_pattern', 'created_time', 'updated_time')


admin.site.register(Assertion, AssertionAdmin)


class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'url_pattern', 'created_time', 'updated_time')

admin.site.register(Objective, ObjectiveAdmin)