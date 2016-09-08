from django.shortcuts import render
from django.http import HttpResponse, Http404

# importing models
from models import *

# Create your views here.

# Django REST framework
from django.utils import timezone
from django.contrib.auth.models import User, Group

from django import forms

import hashlib
import base64

def make_digest(value):
    return base64.urlsafe_b64encode(hashlib.md5(value).digest())

class TinyurlForm(forms.ModelForm):

    class Meta:
        model = Tinyurl
        fields = ('url',)

def post_new(request):
    url = None
    tinyurl = None
    if request.method == "POST":
        form = TinyurlForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            idx = post.url.find('://')
            post.tiny = make_digest(post.url[idx+3:])
            post.save()
            url = post.url
            tinyurl = post.tiny
    else:
        form = TinyurlForm()
    return render(request, 'tinyurl.html', {'form': form, 'url': url, 'tinyurl': tinyurl})
