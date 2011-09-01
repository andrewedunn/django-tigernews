from django.shortcuts import render_to_response
from news.models import Entry
import datetime

def home(request):
	enddate = datetime.datetime.now()
	enddate = enddate + datetime.timedelta(days=1)
	startdate = enddate + datetime.timedelta(days=-3)
	latest_entries = Entry.objects.filter(published__range=[startdate, enddate]).order_by('-published')
	return render_to_response('home.html', {'latest_entries': latest_entries})

