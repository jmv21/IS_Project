from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
