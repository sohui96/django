from django.http.response import JsonResponse

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm

from django.http import HttpResponse
from .models import Curriculum
# from django.http improt JsonResponse
# JsonResponse{{'key':'value'}}
# Create your views here.
# HTML 문자열
# JSON
# Template

from django.contrib.auth.models import User
# 아이디 중복 검사를 위해서 만듬
def check(request):
    username = request.GET.get('username')
    try:
        u = User.objects.get(username=username)
        result = False
    except:
        result = True
    return JsonResponse({'result': result})


def home(request):
    # return HttpResponse('Home page')
    return render(request, 'firstapp/dashboard.html')


def products(request):
    # return HttpResponse('products page')
    return render(request, 'firstapp/products.html')


def customer(request):
    # return HttpResponse('customer page')
    return render(request, 'firstapp/customer.html')


def main(request):
    return JsonResponse({'name': 'park', 'age': 37})


def insert(request):
    # 1-linux 입력
    Curriculum.objects.create(name='linux')
    # 2-python 입력
    c = Curriculum(name='python')
    c.save()
    # 3-html/css/js 입력
    Curriculum(name='python').save()
    #  4-django 입력
    Curriculum(name='django').save()
    return HttpResponse('데이터 입력 완료')

def show(request):
    curriculum = Curriculum.objects.all()
    # result = ''
    # for c in curriculum:
    #     result += c.name + '<br>'
    # return HttpResponse(result)

    return render(
        request, 'firstapp/show.html', { 'data': curriculum })


def template(request):
    curri = Curriculum.objects.all()
    data = {
        'curri': curri,
        'str': 'text', 'num': 10,
        'list': [1, 2, 3],
        'dict': {'a': 'aaa', 'b': 'bbb'}
    }
    return render(
        request, 'firstapp/template.html', data)

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)
            login(request, user)

        return redirect('login')

    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})