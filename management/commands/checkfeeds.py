from django.core.management.base import NoArgsCommand 
from news.models import Entry
import feedparser
import time

class Command(NoArgsCommand):
	requires_model_validation = True 
	can_import_settings = True

	def	handle_noargs(self, **options):
		#print Entry.objects.all() 
		d = feedparser.parse('http://www.lsusports.net/rss.dbml?db_oem_id=5200&media=news')
		for i in range(len(d.entries)):
			e = Entry(title=d.entries[i].title, link=d.entries[i].link, published=time.strftime("%Y-%m-%d %H:%M",d.entries[i].updated_parsed), source="LSUSports.net")
			e.save()
			#print d.entries[i].title
			#print d.entries[i].link
			print time.strftime("%Y-%m-%d %H:%M",d.entries[i].updated_parsed)
			#print "LSUSports.net"
