# -*- coding: utf-8 -*-
from django.template import loader,Context
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    imagelist = range(6)
    t = loader.get_template('cantest/index.html')
    c = Context({
        'imagelist':imagelist,
        })
    return HttpResponse(t.render(c))
