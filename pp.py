from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from attendence.models.Employee import Employee
from attendence.models.EmployeeIP import EmployeeIP
from django.db.utils import IntegrityError
from attendence.decrator import valid_user
from secu.models import User

'''
创建一个应用, 使用view来控制输出
拿到所有的fields信息
使用模板
生成code到html页面上,使用pre
使用markdown的模板完成代码高亮
'''


def get_list(request):
    if request.method == 'GET':
        page_size = int(request.GET.get('pagesize', 10))
        start_index = (int(request.GET.get('currentpage', 1)) - 1) * page_size
        start_index = 0 if start_index < 0 else start_index
        end_index = start_index + page_size

        total_records = EmployeeIP.objects.all().count()
        employee_ips = EmployeeIP.objects.all()[start_index:end_index]
        data = [{"name": eip.employee.first_name + ' ' + eip.employee.last_name, "ip": eip.IP} for eip in employee_ips]

        context = {
            "totalrecords": total_records,
            "data": data
        }
        return JsonResponse(context, safe=False)

    return render(request, 'attendence/login.html', '')


def add(request):
    if request.method == 'POST':
        try:
            ip = request.POST.get('ip', None)
            EmployeeIP.objects.create(
                IP=ip,
                employee=Employee.objects.get(user=User.objects.get(user_name=request.POST.get('user_name', None))),
                entry_user=User.objects.get(user_name=request.session.get('user_name', None))
            )
        except IntegrityError as e:
            return HttpResponse(0)

        return HttpResponse(1)

    return render(request, 'attendence/login.html', '')


def delete(request):
    if request.method == 'POST':
        try:
            ip = request.POST.get('ip', None)
            EmployeeIP.objects.get(PK=ip).delete()
        except err:
            return HttpResponse(0)
        return HttpResponse(1)

    return render(request, 'attendence/login.html', '')
