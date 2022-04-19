import imp
from logging.config import valid_ident
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from temp.serializers import EmployeesSerializers
from .models import Employees, Companies
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from .serializers import EmployeesSerializers
# Create your views here.


@api_view(['GET'])
def api_all_Employeess(request):
    all_Employeess = Employees.objects.all()
    ep_ser = EmployeesSerializers(all_Employeess, many=True)
    return Response(ep_ser.data)


@api_view(['GET'])
def api_one_Employeess(request, ep_id):
    ep = Employees.objects.get(id=ep_id)
    ep_ser = EmployeesSerializers(ep, many=False)
    return Response(ep_ser.data)


@api_view(['POST'])
def api_add_Employeess(request):
    ep_ser = EmployeesSerializers(data=request.data)
    if ep_ser.is_valid():
        ep_ser.save()
        return redirect('api-all')


@api_view(['POST'])
def api_edit_Employeess(request, ep_id):
    ep = Employees.objects.get(id=ep_id)
    ep_ser = EmployeesSerializers(data=request.data, instance=ep)
    if ep_ser.is_valid():
        ep_ser.save()
        return redirect('api-all')


@api_view(['DELETE'])
def api_del_Employeess(request, ep_id):
    ep = Employees.objects.get(id=ep_id)
    ep.delete()
    return Response('Employees Deleted Success')


def home(request):
    ep = Employees.objects.all()
    context = {'students': ep}
    return render(request, 'temp/index.html', context)
