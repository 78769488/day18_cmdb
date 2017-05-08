from django.shortcuts import render, redirect
import pymysql


# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='test',
                       cursorclass=pymysql.cursors.DictCursor)
userinfo = {}


# Create your views here.
def login(request):
    # request包含用户(浏览器)提交过来的所有信息
    error_msg = ""
    if request.method == "POST":
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        # 从数据库获取用户信息
        # 创建游标
        try:
            cursor = conn.cursor()
            res = cursor.execute('SELECT * FROM cmdb_userinfo WHERE email="%s" AND pwd="%s"' % (email, password))
            if res:
                global userinfo
                userinfo.update(cursor.fetchone())
                return redirect('/index/')
            else:
                error_msg = "用户名或密码错误！"
        except Exception as e:
            print(e)
            error_msg = "系统错误, 请稍后再试！"
    return render(request,
                  'login.html',
                  {"error_msg": error_msg})


def index(request):
    user_id = userinfo.get("id", None)
    sql = ("SELECT	* FROM	cmdb_hostinfo WHERE user_id = %s" % user_id)
    cursor = conn.cursor()
    cursor.execute(sql)
    host_list = cursor.fetchall()
    print(host_list)
    return render(request,
                  'index.html',
                  {'host_list': host_list})


def insert(request):
    print("未实现")
    if request.method == "POST":
        cursor = conn.cursor()
        userid = userinfo.get("id", None)
        hostname = request.POST.get("hostname", None)
        hostip = request.POST.get("hostip", None)
        hostport = request.POST.get("hostport", None)
        department = request.POST.get("department", None)
        area = request.POST.get("area", None)
        status = request.POST.get("status", None)
        description = request.POST.get("description", None)
        sql = ("INSERT INTO cmdb_hostinfo ("
               "hostname,ip,`port`,`status`,department,area,onlin_time,update_time,description,userid )"
               "VALUES (%s, %s, %s, %s, %s, %s, NOW(), NOW(), %s, %s)" %
               (hostname, hostip, hostport, status, department, area, description, userid))
        try:
            cursor.execute(sql)
            msg = "添加成功"
            cursor.close()
        except Exception as e:
            print(e)
            msg = "系统错误"
            exit(1)
        return redirect('/index/',
                        {"msg": msg})


def home(request):
    return render(request,
                  'home.html')
