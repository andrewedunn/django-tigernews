from django.db import models

# TODO
# - Entry: Display Entry?
# - Entry: Display Feed? (foreign key to Feed)
# - Entry: # of clicks
# - Feed: Display feed?
# - Feed: Update feed?
# - UpdateHistory: (new class) record every update

class Entry(models.Model):
	title = models.CharField(max_length=255)
	link = models.URLField()
	published = models.DateTimeField()
	summary = models.TextField(null=True,blank=True)
	source = models.CharField(max_length=255,null=True,blank=True)
	entryid = models.CharField(max_length=255,null=True,blank=True)
	feed = models.ForeignKey('Feed') 
	created_date = models.DateTimeField(auto_now_add=True)
	last_modified_date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title

class Feed(models.Model):
	title = models.CharField(max_length=255)
	link = models.URLField()
	created_date = models.DateTimeField(auto_now_add=True)
	last_modified_date = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.title
