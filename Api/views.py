from django.shortcuts import render
from . models import Student
from . serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.

# Model Object = Single Student Data
def student_detail(request,pk):
    stu = Student.objects.get(id = pk)  # complex data type
    # print(stu)
    serializer = StudentSerializer(stu) # convert python data type 
    # print(serializer)
    # print(serializer.data)
    json_data = JSONRenderer().render(serializer.data) # convert json e
    # print(json_data)
    return HttpResponse(json_data, content_type = 'application/json') # json ke client ke dicci
    
    # return JsonResponse(serializer.data)  # shortcut 


# Query set all student data
def student_list(request):
    stu = Student.objects.all()  # complex data type
    serializer = StudentSerializer(stu, many=True) # convert python data type 
    # print(serializer)
    # print(serializer.data)
    json_data = JSONRenderer().render(serializer.data) # convert json e
    # print(json_data)
    return HttpResponse(json_data, content_type = 'application/json') # json ke client ke dicci
    
    # return JsonResponse(serializer.data, safe=False)  # shortcut