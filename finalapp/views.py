from django.shortcuts import render
from finalapp.models import sample
from django.http import HttpResponse
from django.http import JsonResponse
from final.serializers import sample_data
def fill(request):
         if request.method=='POST':
                  new_name=request.POST['name']
                  new_age=request.POST['age']
                  new_gender=request.POST['gender']
                  new_post=sample(name=new_name,age=new_age,gender=new_gender)
                  new_post.save()
         
         
         return render(request,'forms.html',{})
def show(request):
         o=sample.objects.all()
         serializer=sample_data(o,many=True)
         return render(request,'show.html',{"data":serializer})