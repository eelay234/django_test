from django.shortcuts import render, redirect
from datetime import datetime
import random

# Create your views here.
def index(request):
  return render(request, "app_test/index.html")
