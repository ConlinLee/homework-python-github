#!-_-coding=utf-8
import webob
from functools import wraps

def wsgify_bak(fun):
    @wraps(fun)
    def wrap(environ , start_response):
        request = webob.Request(environ)
        response = fun(request)
        return response(environ,start_response)
    return wrap

