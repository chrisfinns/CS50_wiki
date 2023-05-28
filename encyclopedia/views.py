from django.shortcuts import render
from django.http import HttpResponse

from . import util


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

