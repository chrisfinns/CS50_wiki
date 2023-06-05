from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from . import util


class searchForm(forms.Form):
    query = forms.CharField(label="Search")


def search(request):
    query = request.GET.get('q', '')
    search_results = []
    entries = util.list_entries()
    
   
    for entry in entries:
        
        if query in entry.lower():
            search_results.append(entry)
        
    return render(request, "encyclopedia/search.html", {
        "results": search_results,
        
    })
 
def new_page(request):
    
    
    return render(request, "encyclopedia/new_page.html")
    



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_details(request, title):
    content = util.get_entry(title)
    
    return render(request, 'encyclopedia/entry_detail.html', 
        {'title': title, 'content': content})


#def search(request, searchText):
#  return none

