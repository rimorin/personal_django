from django.shortcuts import render
from .models import User
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the user index.")

def get_users(request):
    latest_user_list = User.objects.order_by('-created_date')
    print(latest_user_list)
    serialize_data = UserSerializer(latest_user_list, many=True)
    print(serialize_data.data)
    return JsonResponse(serialize_data.data, safe=False)

@csrf_exempt
def set_user(request):

    if request.method == 'POST':
        data = request.POST
        form = User(user_id=data['user_id'], name=data['name'], password=data['password'], created_date=timezone.now())
        form.save()
        print('user created with id -', form.id)

        serialize_data = UserSerializer(form)
        print(serialize_data.data)

        return JsonResponse(serialize_data.data)

    else:
        form = User()

    return HttpResponse("Invalid req")

@csrf_exempt
def update_user(request):

    if request.method == 'POST':
        data = request.POST
        
        user = User.objects.get(user_id=data['user_id'])
        user.name = data['name']
        user.save()
        # print()
        return JsonResponse(UserSerializer(user).data)
    else:
        return HttpResponse("Invalid req")

@csrf_exempt
def delete_user(request):

    if request.method == 'POST':
        data = request.POST
        user_id_value = data['user_id']
        user = User.objects.get(user_id=user_id_value)
        user.delete()
        msg = "Deleted user id:" + user_id_value
        return HttpResponse(msg)
    else:
        return HttpResponse("Invalid req")
    
