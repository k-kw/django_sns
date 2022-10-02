from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from follow.views import count_follower,count_followee
from bbs.views import postmsg_owner
from .forms import UserprofileForm
from .models import Userprofile
import sns.settings as settings

# Create your views here.

#display your profile not template
@login_required(login_url='login')
def yourprofile(request):
    loginuser=request.user
    if Userprofile.objects.filter(user=loginuser).exists():
        lgprf=Userprofile.objects.filter(user=loginuser)[0]
        params={
            'head':"profile",
            'name':loginuser.username,
            'profile':lgprf,
            'cnt_followee': count_followee(lgprf),
            'cnt_follower': count_follower(lgprf),
            'postmsgs': postmsg_owner(lgprf),
        }
        return render(request, 'userprofile/userprofile.html', params)
    else:
        return redirect(to='upprofile')

# 未登録時, プロフィールを新規作成
@login_required(login_url='login')
def upprofile(request):
    loginuser=request.user
    if request.method=="POST":
        userprofile=Userprofile(user=loginuser)
        userprofileform=UserprofileForm(request.POST, request.FILES, instance=userprofile)
        userprofileform.save()
        print(f'Create_{loginuser.username}_profile\n',)
        return redirect(to='yourprofile')
    else:
        loginuser=request.user    
        params={
            'head':"Upload profile",
            'msg':"メッセージを編集、画像をアップロードしましょう。",
            'user':loginuser,
            'form':UserprofileForm,
        }
        return render(request, 'userprofile/upprofile.html', params)

# 未登録時, デフォルトをセット
@login_required(login_url='login')
def set_default(request):
    loginuser=request.user
    print(settings.MEDIA_ROOT+'/prfimgs/'+'default.png')
    print(settings.DEBUG)
    
    userprofile=Userprofile(user=loginuser, msg='未設定', prfimg='default.png')
    userprofile.save()
    print(f'Set_default_{loginuser.username}_profile\n')

    return redirect(to='yourprofile')




# プロフィールを編集
@login_required(login_url='login')
def editprofile(request):
    loginuser=request.user
    if request.method=="POST":
        userprofile=Userprofile.objects.filter(user=loginuser)[0]
        userprofileform=UserprofileForm(request.POST, request.FILES, instance=userprofile)
        
        userprofileform.save()
        print(f'Edit_{loginuser.username}_profile\n')
        return redirect(to='yourprofile')

    else:
        loginuser=request.user
        nowprf=Userprofile.objects.filter(user=loginuser)[0]
        nowform=UserprofileForm(instance=nowprf)
        params={
            'head':"Edit profile",
            'msg':"メッセージを編集、画像をアップロードしましょう。",
            'user':loginuser,
            'form':nowform,
        }
    return render(request, 'userprofile/editprofile.html', params)
