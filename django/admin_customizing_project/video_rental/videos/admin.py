from django.contrib import admin
from . import models


class MovieAdmin(admin.ModelAdmin):

    fields = ['release_year','title','length']

    search_fields = ['title','length']

    list_filter = ['release_year','length']

    list_display = ['title','release_year','length']

    list_editable = ['length']

# Register your models here.
admin.site.register(models.Movie,MovieAdmin)
# admin.site.register(models.Movie)
admin.site.register(models.Customer)