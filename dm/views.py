from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from userprofile.models import Userprofile
from .forms import DmForm
from .models import Dm
from django.db.models import Q

# Create your views here.

# send DM
@login_required(login_url='login')
def senddm(request, id):
    lgprf=Userprofile.objects.filter(user=request.user)[0]
    rcvprf=Userprofile.objects.filter(id=id)[0]
    
    #prohibit the user from sending the same user DM
    if(lgprf==rcvprf):
        return redirect('yourprofile')

    if request.method=="POST":
        imgflg=True
        if 'img' not in request.FILES:
            imgflg=False
        dm=Dm(sdprf=lgprf, rcvprf=rcvprf, imgflg=imgflg)
        dmform=DmForm(request.POST, request.FILES, instance=dm)
        dmform.save()
        return redirect('alldm', id)
    else:
        params={
            'title':'send DM',
            'head':rcvprf.user.username,
            'rcvprf':rcvprf,
            'form':DmForm(),
        }
        return render(request, 'dm/send.html', params)


# view all DM
@login_required(login_url='login')
def alldm(request, id):
    lgprf=Userprofile.objects.filter(user=request.user)[0]
    rcvprf=Userprofile.objects.filter(id=id)[0]
    #prohibit the user from sending the same user DM
    if(lgprf==rcvprf):
        return redirect('yourprofile')

    dms=Dm.objects.filter(Q(sdprf=lgprf, rcvprf=rcvprf)|Q(sdprf=rcvprf, rcvprf=lgprf)).order_by('-sdtime')
    params={
        'title':str(rcvprf.user.username),
        'head':str(rcvprf.user.username),
        'rcvprf':rcvprf,
        'dms':dms,
    }
    return render(request, 'dm/alldm.html', params)