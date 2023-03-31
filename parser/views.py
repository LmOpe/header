from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def get_header(request):
    user_ip = request.META.get("HTTP_X_FORWARDED_FOR")
    language = request.META.get('HTTP_ACCEPT_LANGUAGE')
    software = request.META.get('HTTP_USER_AGENT')
    ip = 0
    if user_ip:
        ip = user_ip.split(','[0])
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    return JsonResponse({'ipaddress': ip, 'language': language, 'software': software})