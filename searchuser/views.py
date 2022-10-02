from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from userprofile.models import Userprofile
from django.contrib.auth.models import User
from .forms import Userfindform
from follow.views import cf_follow,count_followee,count_follower
from bbs.views import postmsg_owner
# Create your views here.

# User all list (userprofile)
class UserListView(ListView):
    template_name = 'User_list.html'
    model = Userprofile
    #ListView overwrite
    def get_context_data(self):
        ctx=super().get_context_data()
        ctx['page_title']='UserList'
        ctx['page_head']='ユーザ検索・一覧'
        ctx['form']=Userfindform()
        return ctx

@login_required(login_url='login')
def publicprofile(request, prfid):
    lgprf=Userprofile.objects.filter(user=request.user)[0]
    objprf=Userprofile.objects.filter(id=prfid)[0]
    if(lgprf==objprf):
        return redirect('yourprofile')
    
    params={
        'title':'User profile',
        'object': objprf,
        'cf_follow': False,
        'cnt_followee': count_followee(objprf),
        'cnt_follower': count_follower(objprf),
        'postmsgs': postmsg_owner(objprf),
    }
    if (cf_follow(lgprf,objprf)):
        params['cf_follow']=True
    return render(request, 'publicprofile.html', params)

def searchusers(request):
    if request.method=='POST':
        head='検索結果一覧'
        findstring=request.POST['findstring']
        userprofile=Userprofile.objects.filter(user__username__contains=findstring)
        form=Userfindform(request.POST)
        params={
            'title':'search user',
            'head':head,
            'form':form,
            'record':userprofile,
        }
        return render(request, 'searchuser/searchuser.html', params)
    else:
        return redirect(to='userlist')
    