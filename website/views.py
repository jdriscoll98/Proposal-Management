from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
import json
import datetime
from datetime import timedelta
from django.utils import timezone

#-------------------------------------------------------------------------------
# Page Views
#-------------------------------------------------------------------------------
