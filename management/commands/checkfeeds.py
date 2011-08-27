from django.core.management.base import NoArgsCommand 
from news.models import Entry, Feed
import feedparser
import time
import logging

logging.basicConfig(filename='checkfeeds.log',level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.info('Running check feeds')
logging.debug('Test')

class Command(NoArgsCommand):
	requires_model_validation = True 
	can_import_settings = True

	def	handle_noargs(self, **options):
		# Check for feeds
		#print Feed.objects.all()
		for f in Feed.objects.all():
			e = feedparser.parse(f.link)
			for i in range(len(e.entries)):
					print e.entries[i].title,
					print e.entries[i].link,
					print e.entries[i].updated_parsed,
					print e.entries[i].summary,
					print e.entries[i].id,
					print f
				#	g = Entry(
				#		title = e.entries[i].title,
				#		link = e.entries[i].link,
				#		published = e.entries[i].updated_parsed,
				#		summary = e.entries[i].summary,
				#		entryid = e.entries[i].id,
				#		feed = f
				#)	
		#for i in range(len(d.entries)):
			#if Entry.objects.filter(link__exact=d.entries[i].link):
				#print "Link exists"
			#else:
				#print "Link does not exist"
			#e = Entry(
			#	title=d.entries[i].title,
			#	link=d.entries[i].link,
			#	published=time.strftime("%Y-%m-%d %H:%M",d.entries[i].updated_parsed),
			#	source="LSUSports.net"
			#	)
			#e.save()
			#print d.entries[i].title
			#print d.entries[i].link
			#print time.strftime("%Y-%m-%d %H:%M",d.entries[i].updated_parsed)
			#print "LSUSports.net"
