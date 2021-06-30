from typing import NamedTuple
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Member
from django.utils import timezone

def join(request):
    if request.method == 'GET':
        return render(request, 'member/join.html', {})
    else:
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user_name = request.POST['user_name']

        member = Member(user_id=user_id, user_pw=user_pw, user_name=user_name)
        member.c_date = timezone.now()
        member.save()

        return HttpResponse('가입 완료' + user_id + user_pw + user_name)

def login2(request):
    if request.method == 'GET':
        # form = LoginForm()
        return render(request, 'member/login.html', {})
    else:
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        
        try:
            member = Member.objects.get(user_id=user_id, user_pw=user_pw)
        except:
            return HttpResponse('로그인 실패')
        else:
            # 세션에 로그인 관련 정보 저장
            request.session['user.id'] = user_id
            a = request.session
            return HttpResponse('로그인 성공')
            
def logout2(request):
    del request.session['user_id']
    return redirect('/login2/') # url 'name' or path

import glob
def upload1(request):
    if request.method == 'POST':
        upload_file = request.FILES.get('my_file')

        f_list = glob.glob('*')
        print(f_list)
        if upload_file in f_list:
            print('존재하고 있음')

        name = upload_file.name
        size = upload_file.size

        with open('static/files/%s' % name, 'wb') as file:
            for chunk in upload_file.chunks():
                file.write(chunk)
        return HttpResponse('%s<br>%s' % (name, size))
    return render(request, 'upload1.html', {})

import os
from config import settings
def download(request):
    # c:/dev/django/tutorial/db.sqlite3
    filepath = os.path.join(
        settings.BASE_DIR, 'db.sqlite3')

    filename = filepath.split('/')[-1]
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        response = HttpResponse(
        f, content_type='application/octet-stream')
        response['Content-Disposition'] = \
        'attachment; filename="{}"'.format(filename)
        return response