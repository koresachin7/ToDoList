"""
* @Author: Sachin kore
* @Date: 2023-6-16
* @Title: To Do list user registration
"""
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from users.models import User


@csrf_exempt
def user_registration(request):
    """
    Description:
        This Function is creating for user registrations
    :param request:
    :return: JsonResponse
    """
    try:
        if request.method == "POST":

            data = json.loads(request.body)
            user_name = data.get("user_name")

            if User.objects.filter(user_name=user_name).exists():
                return JsonResponse({"message": "Username is already Take", "data": {"username": user_name}})
            else:
                user = User(user_name=user_name, first_name=data.get("first_name"), last_name=data.get("last_name"),
                            password=data.get("password"))
                user.save()
                return JsonResponse({"message": "User data Successfully Sava", "data": data})

    except Exception as e:
        return HttpResponse("Data is invalid", e)


@csrf_exempt
def login(request):
    """
    Description: Creating API to Login User
    :param request:
    :return:
    """
    if request.method == "POST":
        data = json.loads(request.body)
        user_name = data.get("user_name")
        password = data.get("password")

        if User.objects.filter(user_name=user_name, password=password):
            return HttpResponse("User is valid")
        else:
            return HttpResponse("User is invalid")
