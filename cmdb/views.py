from django.shortcuts import render
from common import sqlhelper
from django.shortcuts import HttpResponse


def index(request):
    return render(request, "index.html")


def login_index(request):
    return render(request, "login.html")


def flot(request):
    return render(request, "flot.html")


def morris(request):
    return render(request, "morris.html")


def tables(request):
    return render(request, "tables.html")


def forms(request):
    return render(request, "forms.html")


def panels(request):
    return render(request, "panels-wells.html")


def buttons(request):
    return render(request, "buttons.html")


def notifications(request):
    return render(request, "notifications.html")


def typography(request):
    return render(request, "typography.html")


def icons(request):
    return render(request, "icons.html")


def grid(request):
    return render(request, "grid.html")


def login(request):
    try:
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
    except Exception as e:
        print(e)


def get_machine_list(request):

    html_str = ''
    sql = 'select id,hostname,inner_ip,outer_ip,cpu,memory,disk,network,bandwidth,area,os,product_flag,start_time,end_time from info where isdelete=0'
    conn = sqlhelper.SqlHelper('cmdb')
    data = conn.get_list(sql)
    conn.close()
    content = {'tablelist': data}
    return render(request, "tables.html", content)
