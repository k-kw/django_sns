from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from userprofile.models import Userprofile
from .models import Follow
from django.db.models import Q

# follow(create Follow-record)
@login_required(login_url='login')
def follow(request, id):
    lgprf=Userprofile.objects.filter(user=request.user)[0]
    follower_prf=Userprofile.objects.filter(id=id)[0]
    #自分のフォロー禁止
    if(lgprf==follower_prf):
        return redirect('yourprofile')
    
    flw=Follow(flwee_prf=lgprf, flwer_prf=follower_prf)
    flw.save()
    return redirect('publicprofile', id)

# ログインユーザが対象をすでにフォローしているのか確認
def cf_follow(loginuser_prf, objuser_prf):
    if Follow.objects.filter(flwee_prf=loginuser_prf, flwer_prf=objuser_prf).exists():
        return True
    else:
        return False


# unfollow(create Follow-record)
@login_required(login_url='login')
def unfollow(request, id):
    lgprf=Userprofile.objects.filter(user=request.user)[0]
    follower_prf=Userprofile.objects.filter(id=id)[0]
    flw=Follow.objects.filter(flwee_prf=lgprf,flwer_prf=follower_prf)[0]
    flw.delete()
    return redirect('publicprofile', id)

# ユーザがフォロー中の人数
def count_followee(userprf):
    return Follow.objects.filter(flwee_prf=userprf).count()

# ユーザのフォロワー数
def count_follower(userprf):
    return Follow.objects.filter(flwer_prf=userprf).count()

# フォロー一覧
@login_required(login_url='login')
def follow_list(request, id, which):
    objprf=Userprofile.objects.filter(id=id)[0]
    params={
        'objprf': objprf
    }
    if(which=='wee'):
        params['title']='Followee list'
        params['head']=objprf.user.username+'がフォロー中のユーザー'
        flw_list=Follow.objects.filter(flwee_prf=objprf).order_by('-ctime')
        flw_prf_list=[]
        for flw in flw_list:
            flw_prf_list.append(flw.flwer_prf)

        params['flw_prf_list']=flw_prf_list

    elif(which=='wer'):
        params['title']='Follower list'
        params['head']=objprf.user.username+'のフォロワー'
        flw_list=Follow.objects.filter(flwer_prf=objprf).order_by('-ctime')
        flw_prf_list=[]
        for flw in flw_list:
            flw_prf_list.append(flw.flwee_prf)

        params['flw_prf_list']=flw_prf_list

    else:
        return redirect('yourprofile')
    
    
    return render(request, 'follow_list.html', params)
