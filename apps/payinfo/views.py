#encoding: utf-8

from django.shortcuts import render


def payinfo(request):
    return render(request,'payinfo/payinfo.html')