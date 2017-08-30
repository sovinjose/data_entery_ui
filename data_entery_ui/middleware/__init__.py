import re
import logging
from django import http
from django.core.cache import cache
from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser


class HandleRequests(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if not re.match(SAFE_TO_REDIRECT_URI_REGEX, request.path):
            if not request.user.is_authenticated() and not isinstance(request.user, AnonymousUser):
                return http.HttpResponseRedirect('/login?next=%s' % request.path)
            return None
SAFE_TO_REDIRECT_URI_REGEX = '(/accounts/login/)|(/admin/)|(/logout)'

