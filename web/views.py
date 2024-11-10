from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from web import models


# Create your views here.


def create(request):
    # obj = models.UserInfo.objects.create(username="jack2", password="123456", age=18, tel=147258369)
    obj = models.UserInfo(username="jack3", password="123456", age=18, tel=147258369)
    obj.save()
    print(obj)
    return HttpResponse('11111')


def get(request):
    obj = models.UserInfo.objects.all()
    print(obj)
    data = []
    for i in obj:
        item = dict(id=i.id, username=i.username, age=i.age, tel=i.tel)
        data.append(item)
    return JsonResponse({"code": 200, "message": "ok", "data": data})

def update(request):
    obj=models.UserInfo.objects.filter(username='jack3').update(username='admin')
    return JsonResponse({"code": 200, "message": "ok", "data": '1'})
