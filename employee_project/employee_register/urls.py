from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.employee_form,name='employe_insert'),
    path('<int:id>/',views.employee_form,name='employe_update'),
    path('delete/<int:id>/',views.employee_delet,name='employee_delete'),
    path('list/',views.employee_list,name='employee_list'),
]
