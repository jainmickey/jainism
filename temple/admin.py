from django.contrib import admin
from temple.models import Temple, Tags, Address

#class TagsAdmin(admin.ModelAdmin):
#    list_display=('name',)
#    prepopulated_fields = {'slug': ['name',]}

class TempleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'estd', 'location')

admin.site.register(Tags)
admin.site.register(Address)
admin.site.register(Temple, TempleAdmin)
