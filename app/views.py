from django.shortcuts import render,HttpResponse
from app import models
from app.models import UserInfo


# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")

def user_list(request):
    return render(request,"user_list.html")

def user_add(request):
    return render(request,"user_add.html")

def tpl(request):
    name = "韩超"
    roles = ["管理员" , "ceo" , "baoan"]
    user_info = {"name":"guozhi" , "salary": 10000 , "role": "cto"}
    data_list = [
    ]

    return render(request,"tpl.html" , {"n1": name , "n2": roles , "n3": user_info})

def login(request):
    if request.method == "GET" :
        return render(request , "login.html")
    else:
        print(request.POST)
        username = request.POST.get("user")
        password = request.POST.get("pwd")
        if username == 'root' and password == '123' :
            return HttpResponse("登陆成功")
        else:
            return render(request , 'login.html' , {"error_msg" : "用户名错误"})

def orm(request):
    # models.UserInfo.objects.create(name="abc" , password="123" , age=20)
    # models.UserInfo.objects.create(name="wer", password="123", age=22)
    # models.UserInfo.objects.filter(id=2).delete()
    data_list = models.UserInfo.objects.all()
    for obj in data_list:
        print(obj.name , obj.password , obj.age)
    return HttpResponse("成功")

def info_list(request):
    data_list = UserInfo.objects.all()

    return render(request,"info_list.html",{"data_list": data_list})