from django.shortcuts import render

# Create your views here.
def entries_list(request):
  return render(request, 'entries/entries_list.html')