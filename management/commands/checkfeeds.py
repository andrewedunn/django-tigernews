from django.core.management.base import NoArgsCommand 
from news.models import Entry, Feed
import feedparser
import time
import datetime
import logging

logging.basicConfig(filename='checkfeeds.log',level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

class Command(NoArgsCommand):
	requires_model_validation = True 
	can_import_settings = True

	def	handle_noargs(self, **options):
		for f in Feed.objects.all():
			
			duplicate_entries = 0
			new_entries = 0
			
			# Parse feed and add it to dictionary e
			e = feedparser.parse(f.link)
			
			# DEBUG level parsing information. Notes the feed and checks feed elements.
			# Useful for checking if the contents of a feed exist. At minimum, need 'title' and 'link'. 
			logging.debug('Parsing ... %s' % f)
			logging.debug(
					'Key check ... \
					title: %s, \
					link: %s, \
					updated: %s, \
					published: %s, \
					created: %s, \
					summary: %s, \
					id: %s'
					% 
					('title' in e.feed, 
					'link' in e.feed, 
					'updated' in e.feed, 
					'published' in e.feed, 
					'created' in e.feed, 
					'summary' in e.feed, 
					'id' in e.feed )
				)
			
			# Cycle through each entry and write to Entry class g
			for i in range(len(e.entries)):
				
				# Create blank Entry glass g
				g = Entry()
				
				# Check if title exists in feed and write to Entry
				if 'title' in e.feed:
					g.title = e.entries[i].title
					logging.debug('Title: %s' % e.entries[i].title)
				else:
					logging.warning("Feed %s does not contain 'title' element" % f)
					break

				# Check if link exists in feed and write to Entry
				if 'link' in e.feed:
					g.link = e.entries[i].link
					logging.debug('Link: %s' % e.entries[i].link)
				else:
					logging.warning("Feed %s does not contain 'link' element" % f)
					break
				
				# Check if the entry exists in the database
				if Entry.objects.filter(link__exact=e.entries[i].link):
					duplicate_entries += 1	
					continue

				# Figure out what to use as the date and time
				if 'published' in e.feed:
					g.published = time.strftime("%Y-%m-%d %H:%M",e.entries[i].published_parsed)
					logging.debug('Published: %s' % g.published)
				elif 'updated' in e.feed:
					g.published = time.strftime("%Y-%m-%d %H:%M",e.entries[i].updated_parsed)
					logging.debug('Published: %s' % g.published)
				elif 'created' in e.feed:
					g.published = time.strftime("%Y-%m-%d %H:%M",e.entries[i].created_parsed)
					logging.debug('Published: %s' % g.published)
				else:
					g.published = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
					logging.debug('Published: %s' % g.published)

				# Check for summary
				if 'summary' in e.feed:
					g.summary = e.entries[i].summary
					logging.debug('Title: %s' % e.entries[i].summary)

				# Check for entry id
				if 'id' in e.feed:
					g.entryid = e.entries[i].id
				else:
					g.entryid = e.entries[i].link
				logging.debug('Entry ID: %s' % g.entryid)
				
				g.feed = f 

				g.save()
				new_entries += 1
			
			logging.debug('%s: %s total entries, %s new, %s duplicate' % ( f, duplicate_entries + new_entries, new_entries, duplicate_entries ))

		#	for i in range(len(e.entries)):
		#			print e.entries[i].title,
		#			print e.entries[i].link,
		#			print e.entries[i].updated_parsed,
		#			print e.entries[i].summary,
		#			print e.entries[i].id,
		#			print f
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
