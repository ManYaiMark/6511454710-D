from django.views.generic import DeleteView,UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render
from search.models import *

# Create your views here.
def course_idsearch(request):
  search = request.GET.get('id', '')
  courses = Course.objects.filter(Course_id__icontains=search)
  return render(request,'search/search.html',{'courses':courses})


def courses(request):
  courses = Course.objects.all()
  return render(request,'search/courses.html',{'courses':courses})

def course_namesearch(request):
  search = request.GET.get('id','')
  courses = Course.objects.filter(Course_name__icontains=search)
  return render(request,'search/search.html',{'courses':courses})

class edit(UpdateView):
  model = Course
  fields = ['Course_name','Teacher_name']
  template_name = 'search/edit.html'
  success_url = reverse_lazy('courses')

class delete(DeleteView):
  model = Course
  template_name = 'search/delete.html'
  success_url = reverse_lazy('courses')