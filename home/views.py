from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from home.models import myuser
from django.db.models import Q
from pick_courses.views import *
from django.http import HttpResponseServerError, HttpResponseNotFound


def get_user_object(user_id):
    return myuser.objects.get(Q(user_id=user_id))


'''
    Home 
    Renders the homepage only when user is logged in else redirects user to login page
'''
def home(request): 
    if(not request.user.is_authenticated):
        return redirect('/signin')
    if(request.user.username=='admin'):
        return render(request,'admin.html')

    name=get_user_object(request.user.username).name

    data={'user_name':name}
    try:
        user_id=request.user.username
        course_ids=user_registered_courses(user_id)
        registered_courses_objects=get_course_objects(course_ids)
        courses=[]
        
        data['number_registered_courses']=len(registered_courses_objects)
        
        days_of_week={'M':'monday','T':'tuesday','W':'wednesday','Th':'thursday','F':'friday',"Sa":'saturday',"S":"saturday","Su":'sunday'}
        for i in registered_courses_objects:
            if(i.days):
                courses.append({'name':i.name,'start':i.start_time,'end':i.end_time,'days':[days_of_week[j] for j in i.days.split(',')],'course_id':i.course_id,'prof_name':i.prof_name})
            else:
                courses.append({'name':i.name,'start':i.start_time,'end':i.end_time,'days':None,'course_id':i.course_id,'prof_name':i.prof_name})

        data['registered_course']=courses

    except:
        pass

    
    
    return render(request,'index.html',data)


    

'''
    Sign in method using django auth
    Once signed in ,user redirected to homepage
'''
def signin_user(request):
    if(request.method=="POST"):
        user_id=request.POST.get('user_id')
        password=request.POST.get('password')
        user_exists = authenticate(username=user_id, password=password)
        if(user_exists is not None):
            login(request,user_exists)
            print("login successful")
            return redirect('home')
        else:
            return render(request,'signin.html',{"message":"Login Failed, Please Retry"})
    
    return render(request,"signin.html")


'''
    Used to create a new user
    Django inbuilt table user used to authenticate
    myuser table used to store all details of the user
'''

def signup_user(request):
    if(request.method == 'POST'):
        name=request.POST.get('name')
        user_id=request.POST.get('user_id')
        email=request.POST.get('email')
        password=request.POST.get('password')
        # print("User details----",name,email,password)

        # check if user_id exists
        try:
            get_user_object(user_id)
            print("already exists")
            return render(request,'signup.html',{"message":"User Id already taken"})
        except:
            pass
        
        user_created = User.objects.create_user(username=user_id,
                                 password=password)
        if(user_created):

            reg = myuser(name=name, email=email, password=password,user_id=user_id)
            reg.save()

            
        
            return render(request,'signup.html',{"message":"Signed Up successfully! Please Login To continue","signedup":1})            

        

    return render(request,'signup.html')

    
'''
    Simple sign out using django auth 
'''
def signout_user(request):
    logout(request)
    return redirect('signin')


def handle_not_found404(request,exceptions=None):
    return render(request,'not_found.html',{"Error":404,"Message":"Page Not Found"})


def handle_not_found400(request,exceptions=None):
    return render(request,'not_found.html',{"Error":400,"Message":"Error! 400"})


def handle_not_found500(request):
    return render(request,'not_found.html',{"Error":500,"Message":"Error! 500"})
