from django.http import HttpResponse
from django.shortcuts import render

from .models import Answer


def index(request):
    latest_answers = Answer.objects.order_by("-pub_date")[:5]
    context = {"latest_answers": latest_answers}
    return render(request, "tomdle_app/index.html", context)

def play(request, date):
    return HttpResponse(f"This page lets you play the game for date {date}.")
