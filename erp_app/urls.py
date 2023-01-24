from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register('product',views.ProductViewSet)

from .views import *


urlpatterns = [
    path('', views.index, name="erp_app"),
    ###################################################################################################
    path('view_api/<int:pk>', views.pro_det, name="pro_det"),  # ek data
    path('view_api/', views.pro_det1, name="pro_det1"),    # malti data
    ###################################################################################################
    # path('add_api/', views.create_data, name="create_data"),  # add data
    path('ab_api/', include(router.urls),name='ab_api'),    # add data
    ###################################################################################################
    # RegisterUser
    path('RegisterUser/', RegisterUser.as_view()),


    ###################################################################################################

    path('student-view/<str:pk>/', views.studentView, name="studentview"),
    path('add-student/', views.studentAdd, name="studentadd"),
    path('update-student/<str:pk>/', views.studentUpdate, name="studentupdate"),
    path('delete-student/<str:pk>/', views.studentdelete, name="studentdelete"),




    

]




