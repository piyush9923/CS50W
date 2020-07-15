from django.shortcuts import render

from . import util
import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def info(request, title):
    if title in util.list_entries():
        raw_html = markdown2.markdown(util.get_entry(title))
        return render(request, "encyclopedia/main.html", {
            "title": title,
            "text": raw_html
        })
    else:
        return render(request, "encyclopedia/error.html")
