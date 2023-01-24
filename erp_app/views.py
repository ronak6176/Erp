from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Product,User
import json
from .serializers import ProductSerializer,UserSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
########################################################################################################
from rest_framework.decorators import api_view
from rest_framework.response import Response


from django.shortcuts import get_object_or_404
from rest_framework import status



# from rest_framework import serializers,viewsets

# from .serializers import PersonSerializer,SpeciesSerializer,RoSerializer,MRSerializer
# from rest_framework import status
#######################################################################################################
# from snippets.models import Snippet
# from .serializers import SnippetSerializer
# from rest_framework.renderers import JSONRenderer
# from rest_framework.renderers import JSONRenderer






# Create your views here.

def index(request):
    return HttpResponse("hi ron")

#########################################################################################################

# ek data get................................





def pro_det(request,pk):
    print('++++++')
    pro=Product.objects.get(id=pk)
    # pro=Product.objects.get.all()
    print(pro,'==================')
    serializer =ProductSerializer(pro)
    # print(serializer,'+++++++++++++++++++++++++')
    data= JSONRenderer().render(serializer.data)
    print(data,'-------')
    return HttpResponse(data,content_type='application/json')
#########################################################################################################



#  all data get

def pro_det1(request):
    print('++++++')
    pro=Product.objects.all()
    # pro=Product.objects.get.all()
    print(pro,'==================')
    serializer =ProductSerializer(pro,many=True)
    # print(serializer,'+++++++++++++++++++++++++')
    data= JSONRenderer().render(serializer.data)
    print(data,'-------')
    return HttpResponse(data,content_type='application/json')



#########################################################################################################



# create data (registration)
# @csrf_exempt 
# def create_data(request):
#     print('-------------')
#     if request.method == 'POST':
#         j_data=request.body
#         stream=io.BytesIO(j_data)
#         print(stream,'77777777777777777777777')
#         # print(p_data=JSONParser.parse(stream))
#         p_data=JSONParser.parse(stream)
#         print(p_data,'555555555555555555555555')
#         serializer=ProductSerializer(data=p_data)
#         print('555555')

#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'done data'}
#             json_data= JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#             # return JsonResponse({'Result': f'Product {json_data} Added...'}, safe=False)
#     json_data=JSONRenderer().render(serializer.errors)
#     return HttpResponse(json_data,content_type ='application/json')
#     # return JsonResponse({'Result': f'Product {json_data} Added...'}, safe=False)



#########################################################################################################

#  simpel add data



# @csrf_exempt 
class ProductViewSet(viewsets.ModelViewSet):
    print('-------------')
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


#########################################################################################################

# ragister user using token

class RegisterUser(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)

        if not serializer.is_valid():
            print(serializer.errors)

            return Response({'status':403 , 'errors': serializer.errors , 'messge': 'not valid'})
        
        serializer.save()
        
        user=User.objects.get(username=serializer.data['username'])
        token_obj , _ =Token.objects.get_or_create(user=user)


        return Response({'status':200 , 'errors': serializer.data ,'token' : str(token_obj) , 'messge': 'valid'})





#########################################################################################################


   
# ****** crude ******


@api_view(['GET'])
def studentView(request, pk):
    try :
        student = Product.objects.get(id=pk)
        serialstudent = ProductSerializer(student, many=False)
        return Response({
            'status':200,
            'students':serialstudent.data,
        })
    except :
        return Response({'status':400})


@api_view(['POST'])
def studentAdd(request):
    try:
            
        serialdata = ProductSerializer(data=request.data)
        if serialdata.is_valid():
            serialdata.save()
        
        return Response({
            'status':200,
            'student':serialdata.data,
            'message':'Student added successfully'
        })

    except:
        return Response({'status':400})

@api_view(['POST'])
def studentUpdate(request, pk):
    try :
        student = Product.objects.get(id=pk)
        serialstudent = ProductSerializer(instance=student, data=request.data)

        if serialstudent.is_valid():
            serialstudent.save()
            
        return Response({
            'status':200,
            'student':serialstudent.data,
            'message':'Updated successfully'
        })

    except :
        return Response({'status':400})


@api_view(['DELETE'])
def studentdelete(request, pk):
    try:

        student = Product.objects.get(id=pk)
        student.delete()
        
        students = Product.objects.all()
        serialstudents = ProductSerializer(students, many=True)
        
        return Response({
            'status':200,
            'student':serialstudents.data,
            'message':'Student Deleted successfully'
        })

    except:
        return Response({'status':400})


#########################################################################################################