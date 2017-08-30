import re
import logging
from django import http
from django.core.cache import cache
from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser


class HandleRequests(object):
    def process_view(self, request, *arg, **kwargs):
        if not re.match(SAFE_TO_REDIRECT_URI_REGEX, request.path):
            if not request.user.is_authenticated() or isinstance(request.user, AnonymousUser):
                return http.HttpResponseRedirect('/login?next=%s' % request.path)
            return None
SAFE_TO_REDIRECT_URI_REGEX = '(/accounts/login/)|(/admin/)|(/logout)'

