

from django.contrib import admin
from django.urls import path,include
from api.views import Bankviewset,Employeeviewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'bankapi', Bankviewset)
router.register(r'employee',Employeeviewset)


urlpatterns = [

    path('',include(router.urls))
    
]
