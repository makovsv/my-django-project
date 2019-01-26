from django.contrib import admin
from .models import *

class LifeProfileAdmin (admin.ModelAdmin):
    #list_display = [field.name for field in Subscriber._meta.fields]
    # list_filter = ('name',)
    # search_fields = ['name', 'email']
    fields = ["myusername"]
    # exclude = ["email"]

    class Meta:
        model = LifeProfile

admin.site.register(LifeProfile)
