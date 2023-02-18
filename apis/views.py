from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import generics, permissions, serializers
from rest_framework.parsers import MultiPartParser, FormParser


from django.views.decorators.csrf import csrf_exempt, csrf_protect
import uuid
from rest_framework import serializers 
from .models import users,driver_detail
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password,check_password
from .serializers import usersSerializer,driver_detailSerializer
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.conf.urls.static import static

# Create your views here.
# to fetch all users


@api_view(['GET', 'POST', 'DELETE'])
def get_all_users(request):
    if request.method == 'GET':
        tutorials = users.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = usersSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    # elif request.method == 'POST':
        # tutorial_data = JSONParser().parse(request)
        # tutorial_serializer = usersSerializer(data=tutorial_data)
        # if tutorial_serializer.is_valid():
            # tutorial_serializer.save()
            # return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        # return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = users.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)








# class usersView(APIView):  
  
#     def get(self, request, *args, **kwargs):  
#         result = users.objects.all()  
#         serializers = usersSerializer(result, many=True)  
#         return Response({'status': 'success', "users":serializers.data}, status=200)  
#         class Meta:
#             model = users
  
#     def post(self, request):  
#        serializer = usersSerializer(data=request.data)  
#        if serializer.is_valid():  
#            serializer.save()  
#            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
#        else:  
#            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
# 
@csrf_exempt
def reg_user(request):
    userdata = request.GET
    user = users(
        name = userdata['name'],
        email = userdata['email'],
        phone = userdata['phone'],
        password = make_password(userdata['password']),
        age = userdata['age'],
        # Firebase_id = userdata['fire_id'],
        gender = userdata['gender'],
    ) 
    if users.objects.filter(email=userdata['email']).exists():

        return HttpResponse({False:"False"},content_type= 'application/json')
    else:
        user.save()
        return HttpResponse({True:"True"},content_type= 'application/json')
#///////////////////////////////////////////////////////////////////////////////

@csrf_exempt
def user_fetchone(request):
    requests = request.GET
    email = requests['email']

    user = users.objects.filter(email = email).values()
    useri = list(user)
    if useri:
        return JsonResponse(useri,safe=False)
    else:
        return JsonResponse({False:"notfound"})

def user_login(request):
    requests = request.GET
    email = requests['email']
    password = requests['password']

    
    user = users.objects.filter(email = email).values() and users.objects.filter(password=password).values()
    if user:
        return JsonResponse({True:"True"})
    else:
        return JsonResponse({False:"false"})
    

# ////////////////////////////////////////////////////////////////////////////////







@csrf_exempt
def detector(request):
    data = {"success": False}
    if request.method == "POST":
        print("oke0")
        if request.FILES.get("image", None) is not None:
            #So this would be the logic
            img = request.FILES["image"]
            img_extension = os.path.splitext(img.name)[1]

            # This will generate random folder for saving your image using UUID
            save_path = "static/" + str(uuid.uuid4())
            if not os.path.exists(save_path):
                # This will ensure that the path is created properly and will raise exception if the directory already exists
                os.makedirs(os.path.dirname(save_path), exist_ok=True)

            # Create image save path with title
            img_save_path = "%s/%s%s" % (save_path, "image", img_extension)
            with open(img_save_path, "wb+") as f:
                for chunk in img.chunks():
                    f.write(chunk)
            data = {"success": True}
        else:
            return JsonResponse(data)
    return JsonResponse(data)   

  

# def reg_driver(request):
#     userdata = request.GET
#     user = driver_detail(
#         d_name = userdata['fname'],
#         d_email = userdata['email'],
#         d_phone = userdata['phone'],
#         d_password = (userdata['password']),
#         d_age = userdata['age'],
#         # Firebase_id = userdata['fire_id'],
#         d_gender = userdata['gender'],
#         d_photo = userdata['photo']
#     ) 
def driver(self, request, *args, **kwargs):
    form = EmployeeForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('home', kwargs={'pk': pk}))
    context = self.get_context_data(form=form)
    return self.render_to_response(context)     
def get(self, request, *args, **kwargs):
    return self.post(request, *args, **kwargs)