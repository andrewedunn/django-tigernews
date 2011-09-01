from django.contrib import admin
from news.models import Entry
from news.models import Feed 

class EntryAdmin(admin.ModelAdmin):
	list_display = ('feed', 'published', 'title')

admin.site.register(Entry, EntryAdmin)
admin.site.register(Feed)

