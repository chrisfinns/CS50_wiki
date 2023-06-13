from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from . import util
from django.contrib import messages
from django.urls import reverse
import random
import markdown2


class searchForm(forms.Form):
    query = forms.CharField(label="Search")


def search(request):
    query = request.GET.get('q', '')
    search_results = []
    entries = util.list_entries()
    
   
    for entry in entries:
        if query.lower() in entry.lower():
            search_results.append(entry)
            
            if query.lower() == entry.lower():
                entry_page = "wiki/" + str(query.lower())
                
                return redirect(entry_page)

    return render(request, "encyclopedia/search.html", {
        "results": search_results,
    })


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_details(request, title):
    entries = util.list_entries()
    entries = [x.lower() for x in entries]
    if title.lower() in entries:
        content = markdown2.markdown(util.get_entry(title))

        return render(request, 'encyclopedia/entry_detail.html', 
            {'title': title, 'content': content})
    
    else:
        messages.error(request, f"{title}: Entry Does Not Exist. See List of current entries:")

        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


class NewPageForm(forms.Form):
    title = forms.CharField(label="title")
    content = forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'rows':3,'cols':5}))

def new_page(request):
    filenames = util.list_entries()
    if request.method =="POST":    
        form = NewPageForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            filenames = [x.lower() for x in filenames]
            
            if title.lower() not in filenames:
                util.save_entry(title, content)
                entry_page = "wiki/" + str(title)
                
                return redirect(entry_page)
            
            else:
                messages.error(request, 'Entry Exists')

        else:
            return render(request,"encyclopedia/new_page.html", {
                "form": form
            })
    
    return render(request, "encyclopedia/new_page.html", {
        "form": NewPageForm()
    })


def random_page(request):
    entries = util.list_entries()
    randomPage = random.choice(entries)
    print(f"{randomPage}")


    entry_page = "wiki/" + str(randomPage.lower())
    return redirect(entry_page)

def edit(request, title):
    content = util.get_entry(title)

    if request.method == "POST":
        contentEdit = request.POST['content']
        
        util.save_entry(title, contentEdit)
        return HttpResponseRedirect(reverse("encyclopedia:wiki_entry", args=[title]))


    return render(request, "encyclopedia/edit.html", {
        'title': title, 'content': content
    })