from django.contrib import admin
from feeds.models import Feed, Tags

#class TagsAdmin(admin.ModelAdmin):
#    list_display=('name')

class FeedAdmin(admin.ModelAdmin):
    list_display=('published', 'title', 'body')

admin.site.register(Tags)
admin.site.register(Feed, FeedAdmin)
