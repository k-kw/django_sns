from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from userprofile.models import Userprofile
from .forms import PostmsgForm, Postmsgfindform, Re_postmsgForm
from .models import Postmsg, Re_postmsg
from django.views.generic import ListView

# Create your views here.


@login_required(login_url='login')
def postmsgc(request):
    loginuser=request.user

    if request.method=="POST":
        imgflg=True
        if 'img' not in request.FILES:
            imgflg=False
        postmsg=Postmsg(userprf=Userprofile.objects.filter(user=loginuser)[0], imgflg=imgflg)
        postmsgform=PostmsgForm(request.POST, request.FILES, instance=postmsg)
        postmsgform.save()
        return redirect(to='bbsall')
    else:
        params={
            'title':'BBS post message',
            'head':'掲示板にメッセージや画像を投稿しましょう！！',
            'form':PostmsgForm(),
        }
        return render(request, 'bbs/postmsgc.html', params)


class PostmsgListView(ListView):
    template_name='bbsall.html'
    model=Postmsg
    #ListView overwrite
    def get_context_data(self):
        ctx=super().get_context_data()
        ctx['page_title']='BBS'
        ctx['page_head']='掲示板へようこそ'
        ctx['form']=Postmsgfindform()
        return ctx
    
    def get_queryset(self):
        return Postmsg.objects.order_by('-createtime')

def searchbbs(request):
    if request.method=='POST':
        head='検索結果一覧'
        findstring=request.POST['findstring']
        postmsg=Postmsg.objects.filter(msg__contains=findstring).order_by('-createtime')
        form=Postmsgfindform(request.POST)
        params={
                'title':'search BBS',
                'head':head,
                'form':form,
                'record':postmsg,
        }
        return render(request, 'bbs/searchbbs.html', params)
    else:
        return redirect(to='bbsall')

def postmsg_owner(owner_prf):
    return Postmsg.objects.filter(userprf=owner_prf)


# 返信
@login_required(login_url='login')
def postmsgre(request, id):
    loginuser=request.user
    targetmsg=Postmsg.objects.get(id=id)
    
    if request.method=="POST":
        imgflg=True
        if 'img' not in request.FILES:
            imgflg=False
        remsg=Re_postmsg(
            userprf=Userprofile.objects.filter(user=loginuser)[0],
            target_msg=targetmsg,
            imgflg=imgflg
        )
        remsgform=Re_postmsgForm(request.POST, request.FILES, instance=remsg)
        remsgform.save()
        return redirect('postmsgre', id)
    else:
        params={
            'title':'BBS response message',
            'head1':'返信フォーム',
            'targetmsg': targetmsg,
            'form':Re_postmsgForm(),
            'head2': '返信一覧', 
            'res': Re_postmsg.objects.filter(target_msg=targetmsg).order_by('-createtime')
        }
        return render(request, 'bbs/postmsgre.html', params)