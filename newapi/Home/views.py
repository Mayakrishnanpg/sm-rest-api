from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .form import StudentForm
from .models import Student
from .serializers import StudentSerializer


@api_view(["GET"])
def check(request):
    x={
        "id":1,
        "name":"ami",
        "class":"python"
    }
    return Response(x)

def InsertData(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form .is_valid():
            form.save()
            return redirect('InsertData')
    context ={
            "form":form
        }
    return render (request,"form.html",context)

@api_view(["GET"])
def StudentAllData(request):
    stud = Student.objects.all()
    serializer = StudentSerializer(stud, many = True)
    return Response(serializer.data)

@api_view(["GET"])
def StudentView(request,pk):
    stud = Student.objects.get(id= pk)
    serializer = StudentSerializer(stud, many = False)
    return Response(serializer.data)

@api_view(["POST"])
def  CreateStudent(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
def UpdateStudent(request,pk):
    stud = Student.objects.get(id = pk)
    serializer = StudentSerializer(instance=stud,data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def DeleteStudent(request,pk):
    stud = Student.objects.get(id = pk).delete()
    return Response("student delete")


    
    