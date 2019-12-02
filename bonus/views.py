from django.shortcuts import render
from .models import *
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.contrib.auth import models
import json
from django.core import serializers
from django.db.models import Avg, Count, Sum, FloatField, Case, When, F, Value
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework.parsers import JSONParser
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view


def testrequest(request):
    return render(request, "bonus/requestin.html")


@api_view()
def GetDiagramValues(request):
    sums = BonusTransaction.objects.filter(user=request.user).aggregate(
        balance=Sum("value", output_field=FloatField()),
        total_earned=Sum(
            Case(
                When(value__gt=0, then=F("value")), default=0, output_field=FloatField()
            )
        ),
    )
    sums["total_spent"] = sums["balance"] - sums["total_earned"]
    return JsonResponse(sums, safe=False)

class UserBonusTransactionList(ListAPIView):
    serializer_class = BonusTransactionSerializer

    def get_queryset(self):
        return BonusTransaction.objects.filter(user=self.request.user)
