from django.shortcuts import render
from markdown2 import Markdown
from django.views.decorators.csrf import csrf_exempt
import random

from . import util


def convert(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)


def index(request):
    entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })


def entry(request, title):
    html_content = convert(title)
    if html_content == None:
        return render(request, 'encyclopedia/error.html', {
            "message": "This entry doesn't exist"
        })
    else:
        return render(request, 'encyclopedia/entry.html', {
            "title": title,
            "content": html_content
        })


@csrf_exempt
def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        html_content = convert(entry_search)
        if html_content is not None:
            return render(request, 'encyclopedia/entry.html', {
                "title": entry_search,
                "content": html_content
            })
        else:
            every_entry = util.list_entries()
            recommendation = []
            for entry in every_entry:
                if entry_search.lower() in entry.lower():
                    recommendation.append(entry)
            return render(request, 'encyclopedia/search.html', {
                'recommendation': recommendation
            })


@csrf_exempt
def new_page(request):
    if request.method == 'GET':
        return render(request, 'encyclopedia/new.html')
    else:
        title = request.POST['title']
        content = request.POST['content']
        titleExist = util.get_entry(title)
        if titleExist is not None:
            return render(request, 'encyclopedia/error.html', {
                'message': 'Entry page already exist'
            })
        else:
            util.save_entry(title, content)
            html_content = convert(title)
            return render(request, 'encyclopedia/entry.html', {
                'title': title,
                'content': html_content
            })


@csrf_exempt
def edit(request):
    if request.method == 'POST':
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, 'encyclopedia/edit.html', {
            'title': title,
            'content': content
        })


@csrf_exempt
def save_edit(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = convert(title)
        return render(request, 'encyclopedia/entry.html', {
            'title': title,
            'content': html_content
        })


def rand(request):
    every_entry = util.list_entries()
    rand_entry = random.choice(every_entry)
    html_content = convert(rand_entry)
    return render(request, 'encyclopedia/entry.html', {
            'title': rand_entry,
            'content': html_content
        })
