from django.shortcuts import render
from django.http import HttpResponse
from .models import PlayerINFO,TeamINFO,NewsINFO,ContactINFO,Account
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import HttpResponseRedirect 
import datetime
@csrf_exempt
# Create your views here.
# 传递数据库内容（球员球队信息，新闻）
def index(request):
    
    PIF_list = PlayerINFO.objects[:]
    TIF_list = TeamINFO.objects[:]
    NIF_list = NewsINFO.objects[:]
    context = {
        'PIF_list': PIF_list,
        'TIF_list': TIF_list,
        'NIF_list': NIF_list
    }
    return render(request, 'myfirstsite/index.html', context)
# 传递联系信息
def conINFO(request):
    if request.method == 'POST':
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        message1 = request.POST.get('message')
        if(name1!= "" and email1!="" and message1!=""):
            messageN = ContactINFO.objects.create(name= name1,email=email1,message= message1)
            messages.success(request,"感谢您的反馈，请等待我的回复")
        else:
            messages.success(request,"消息提交失败，请仔细核对")
    return render(request, 'myfirstsite/index.html')

# 注册
def SignUP(request):
    if request.method == 'POST':
        usrname = request.POST.get('UserNM')
        usrpwd = request.POST.get('UserPwd')
        currenttime= str(datetime.datetime.now())
        result =  Account.objects.filter(UserNM = usrname)
        if(len(result))>0:
            messages.success(request,"该账号已被注册，请重新输入")
        else:
            USERN = Account.objects.create(UserNM= usrname,UserPwd= usrpwd,UserStrartTime=currenttime,UserLV="塑料V")
            messages.success(request,'您已成功注册')
    else:
        messages.success(request,"消息提交失败，请仔细核对")
    return render(request, 'myfirstsite/index.html')

