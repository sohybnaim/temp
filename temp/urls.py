
from . import views
from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('api-all', views.api_all_Employeess, name='api-all'),
    path('api-one/<ep_id>', views.api_one_Employeess, name='api-one'),
    path('api-add', views.api_add_Employeess, name='api-add'),
    path('api-edit/<ep_id>', views.api_edit_Employeess, name='api-edit'),
    path('api-del/<ep_id>', views.api_del_Employeess, name='api-del'),

]
