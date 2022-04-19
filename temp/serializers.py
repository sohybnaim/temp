from ast import ClassDef
from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Employees, Companies
from temp import models


class EmployeesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('__all__')
