from django.shortcuts import render, redirect
from .models import Entry
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

def entries_list(request):
  entries = Entry.objects.all().order_by('date')
  return render(request, 'entries/entries_list.html', {'entries': entries})

def entry_details(request, slug):
  entry = Entry.objects.get(slug=slug)
  return render(request, 'entries/entry_info.html', { 'entry': entry })

@login_required(login_url="/accounts/login")
def entry_new(request):
  if request.method == 'POST':
    form = forms.CreateEntry(request.POST, request.FILES)
    if form.is_valid():
      new_entry = form.save(commit=False)
      new_entry.author = request.user
      new_entry.save()
      return redirect('entries:list')
  else:
    form = forms.CreateEntry()
  return render(request, 'entries/new_entry.html', {'form': form})
