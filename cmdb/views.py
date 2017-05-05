from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    # request包含用户(浏览器)提交过来的所有信息
    error_msg = ""
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        if username == "hongyu_951@163.com" and password == "123456":
            return redirect('/index/')
        else:
            error_msg = "用户名或密码错误！"
    return render(request,
                  'login.html',
                  {"error_msg": error_msg})


def index(request):
    return render(request,
                  'index.html')
