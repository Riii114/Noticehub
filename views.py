from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import Notice

# Create your views here.
def all_notices(request):
    allnotices = Notice.objects.all()
    context = {'result':allnotices}
    return render(request,'user/notice.html',context)

