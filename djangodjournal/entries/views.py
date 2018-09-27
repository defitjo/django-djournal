from django.shortcuts import render
from .models import Entry
from django.http import HttpResponse

def entries_list(request):
  entries = Entry.objects.all().order_by('date')
  return render(request, 'entries/entries_list.html', {'entries': entries})

def entry_details(request, slug):
  entry = Entry.objects.get(slug=slug)
  return render(request, 'entries/entry_info.html', { 'entry': entry })