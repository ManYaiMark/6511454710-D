from django.urls import path,include
from search.views import *

urlpatterns = [
  path('',course_idsearch,name='search'),
  path('courses/',courses,name='courses'),
  path('course_name/',course_namesearch,name='course_name'),
  path('edit/<str:pk>/',edit.as_view(),name='edit'),
  path('delete/<str:pk>',delete.as_view(),name='delete'),

]