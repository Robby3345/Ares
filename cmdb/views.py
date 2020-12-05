from django.shortcuts import render
from common import sqlhelper
from django.shortcuts import HttpResponse


def index(request):
    return render(request, "index.html")


def login_index(request):
    return render(request, "login.html")


def login(request):
    mail = request.POST['email']
    password = request.POST['password']
    content = {'login_info': "*请输入正确的用户名密码*"}
    check_sql = 'select id from login where mail="' + mail + '" and password="' + password + '"'
    conn = sqlhelper.SqlHelper("cmdb")
    is_exist = conn.get_list(check_sql)
    conn.close()
    if (len(is_exist) == 0):
        return render(request, "login.html", content)
    else:
        return render(request, "index.html")
