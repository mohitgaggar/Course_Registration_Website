from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from home.models import myuser
from pick_courses.models import available_course
from django.db.models import Q
from django.http import JsonResponse
import json


def myhome(request):
    return render(request,'home.html')


def get_course_objects(course_id_list):
    courses_obj_list=[]
    for i in course_id_list:
        courses_obj_list.append(available_course.objects.get(Q(course_id=i)))
    return courses_obj_list


def user_registered_courses(user_id):
    user_obj=get_user_object(user_id)
    if(user_obj.registered_courses):
        return [i for i in user_obj.registered_courses.split(',')]
    return []

'''
    Function to query the db to get myuser object given user_id
'''
def get_user_object(user_id):
    return myuser.objects.get(Q(user_id=user_id))


'''
    Function to query the db to get course object given course_id
'''
def get_course_object(course_id):
    return available_course.objects.get(Q(course_id=course_id))



'''
    Function to query the db to get all courses stored in available_course table
'''
def get_all_courses():
    return available_course.objects.all()

'''
    Helper function to get all ids of courses the user has currently registered for
'''
def get_registered_course_ids(user_id):
    
    try:
        registered_courses=[]
        registered_courses=user_registered_courses(user_id)
        registered_courses_objects=get_course_objects(registered_courses)
        registered_course_ids=''
        for i in registered_courses_objects:
            registered_course_ids+=' '+str(i.course_id)

        return registered_course_ids
        
    except:
        pass


'''
    Controller function to handle /search
    all search requr
'''
def search(request):
    # if(request.method=="POST"):
    name=request.GET.get('course_name')
    if(name==''):
        return redirect('/pick_course')
    courses_matching=[]
    all_courses=get_all_courses()
    for i in all_courses:
        if(name in i.name):
            courses_matching.append(i)

    passing_obj={'courses' : courses_matching}

    passing_obj['registered_course']=get_registered_course_ids(request.user.username)

   

    return render(request,'courses.html',passing_obj)

    return redirect('/pick_course')

'''
    Function to unregister this course from all users
'''
def remove_course_from_all_users(course_id):
    users=myuser.objects.all()
    for i in users:
        untake_course(course_id,i.user_id)
    

def delete_course(request):
    if(request.user.username=='admin'):
        if(request.method == 'POST'):
            course_id=request.POST.get('course_id')
            try:
                course_obj=get_course_object(course_id)
            except:
                return redirect('/home')

            remove_course_from_all_users(course_id)
            
            course_obj.delete()
        return render(request,'delete_course.html')
    else:
        return redirect('/home')


def update_course(request):
    if(request.user.username=='admin'):
        if(request.method == 'POST'):
            

            name=request.POST.get('name')
            course_id=request.POST.get('course_id')
            prof_name=request.POST.get('prof_name')
            prof_id=request.POST.get('prof_id')
            seats_available=request.POST.get('seats_available')
            description=request.POST.get('description')
            prerequisites=request.POST.get('prerequisites')
            days=request.POST.get('days')
            start_time=request.POST.get('start_time')
            end_time=request.POST.get('end_time')

            try:
                course_obj=get_course_object(course_id)
            except:
                return redirect('/home')
            
            if(name):
                course_obj.name=name
       
            if(prof_name):
                course_obj.prof_name=prof_name
            
            if(prof_id):
                course_obj.prof_id=prof_id
            
            if(description):
                course_obj.description=description
            
            if(seats_available):
                course_obj.seats_available=seats_available
            
            if(prerequisites):
                course_obj.prerequisites=prerequisites
            
            if(days):
                course_obj.days=days
            
            if(start_time):
                course_obj.start_time=start_time
            
            if(end_time):
                course_obj.end_time=end_time    

            course_obj.save()
            remove_course_from_all_users(course_id)

        return render(request,'update_course.html')
    else:
        return redirect('/home')

'''
    Helper function to check for timing clashes when days of 2 course match
'''
def timing_clash(start1,start2,end1,end2):
    if(start1>start2):
        if(start1>=end2):
            return 0
        else:
            return 1
    else:
        if(start2>=end1):
            return 0
        else:
            return 1


'''
    Helper function to check if days and timings of a course the user is trying to register for 
    clashes with any of the other existing course he/she has registered for
'''

def day_and_timing_clash(course_objects,new_course_object):
    if(new_course_object.days):
        new_course_days=new_course_object.days.strip().split(',')
    else:
        return 0,[]
    clash_courses=[]
    for i in course_objects:
        try:
            days=i.days.strip().split(',')
        except:
            continue
        
        for j in new_course_days:
            if(j in days and timing_clash(i.start_time,new_course_object.start_time,i.end_time,new_course_object.end_time)):
                clash_courses.append(i)
                break

    if(len(clash_courses)==0):
        return 0,clash_courses
    return 1,clash_courses
    



'''
    Helper function to register for a course given user_id and course_id
    If the user has taken all necessary prereuisites, registration is successful
    else doesnt do anything

    returns appropriate message as AJAX reposonse to be displayed to the user
'''
def take_course(course_id,user_id):
    user_obj = get_user_object(user_id)
    course_obj=get_course_object(course_id)

    if(course_obj.seats_available==0):
        return {'message':'Sorry! No seats available for this course'}

    

    can_take_course=1
    if(user_obj.registered_courses):
        already_registered_courses=list(user_obj.registered_courses.split(','))
        if(course_id in already_registered_courses):
            return {'message':'Already registered for this course'}
        user_registered_courses_objects=[]
        for i in already_registered_courses:
            user_registered_courses_objects.append(get_course_object(i))

        clash,clash_courses=day_and_timing_clash(user_registered_courses_objects,course_obj)
        if(clash):
            msg='Failed! There is a timing clash with these courses -'
            for i in clash_courses:
                msg+=' '+i.name+' ,'
            msg=msg[:-1]
            return {'message':msg}
    else:
        pass

    if(not course_obj.prerequisites):
        pass
    
    else:
        
        prerequisites=list(course_obj.prerequisites.split(','))
        
        if(not user_obj.courses_taken):
            can_take_course=0
        else:
            prev_courses=list(user_obj.courses_taken.split(','))

            prev_courses_dict={}
            for i in prev_courses:
                prev_courses_dict[i]=1

            can_take_course=1
            for i in prerequisites:
                if(i not in prev_courses_dict):
                    can_take_course=0


    if(can_take_course):

        
        reduce_available_seats(course_obj)
        if(user_obj.registered_courses):
            user_obj.registered_courses+=','+course_id
            
        else:
            user_obj.registered_courses=course_id
        user_obj.save()

        return {'message':'Successfully registered for course'}
        
    else:

        return {'message':'Prerequistites not taken cannot take course!'}
        

def untake_course(course_id,user_id):
    user_obj = get_user_object(user_id)
    course_obj=get_course_object(course_id)
    
    if(user_obj.registered_courses):
        already_registered_courses=list(user_obj.registered_courses.split(','))
        if(course_id in already_registered_courses):
            already_registered_courses.remove(course_id)
            user_obj.registered_courses=''
            if(already_registered_courses):
                user_obj.registered_courses=already_registered_courses[0]
                for i in already_registered_courses[1:]:
                    user_obj.registered_courses+=','+i

            user_obj.save()
            increase_available_seats(course_obj)
            return {'message':'Successfully un-registered for this course'}
    
    return {'message':'Course Not registered '}
    
def reduce_available_seats(course_obj):
    course_obj.seats_available-=1
    course_obj.save()

def increase_available_seats(course_obj):
    course_obj.seats_available+=1
    course_obj.save()



'''
    Controller for /register_course
    post request made by AJAX to register for a course
    Return a JSON with a message to be displayed to the user
'''
def register_course(request):
    if(request.method=='POST'):

        data=take_course(request.POST.get('course_id'),request.user.username)
        
        return JsonResponse(json.dumps(data), status=201,safe=False)




'''
    Controller for /unregister_course
    post request made by AJAX to register for a course
    Return a JSON with a message to be displayed to the user
'''
def unregister_course(request):
    if(request.method=='POST'):
        
        data=untake_course(request.POST.get('course_id'),request.user.username)
        
        return JsonResponse(json.dumps(data), status=201,safe=False)        

'''
    Controller for /pick_course 
    Displays all available courses when get request made
    All rows of table queried and passed to html page
    html page adds all course data into a html table

'''
def display_courses(request):
    if(not request.user.is_authenticated):
        return redirect('signin')


    all_courses = get_all_courses()
    passing_obj={'courses' : all_courses}
    
    try:
        user_id=request.user.username
        registered_courses=[]
        registered_courses=user_registered_courses(user_id)

        registered_courses_objects=get_course_objects(registered_courses)

        registered_course_ids=''
        for i in registered_courses_objects:
            registered_course_ids+=' '+str(i.course_id)
        passing_obj['registered_course']=registered_course_ids

        user_obj=get_user_object(user_id)
        passing_obj['user_name']=user_obj.name
    except:
        pass

    return render(request,'courses.html',passing_obj)

'''
    Controller for /add_course
    to add a new course 
    Only admin can access
    if other user tries to access , redirection to home
'''
def add_courses(request):
    if(request.user.username=='admin'):
        if(request.method == 'POST'):
            name=request.POST.get('name')
            course_id=request.POST.get('course_id')
            prof_name=request.POST.get('prof_name')
            prof_id=request.POST.get('prof_id')
            seats_available=request.POST.get('seats_available')
            description=request.POST.get('description')
            prerequisites=request.POST.get('prerequisites')
            days=request.POST.get('days')
            start_time=request.POST.get('start_time')
            end_time=request.POST.get('end_time')
            reg = available_course(days=days,name=name, course_id=course_id, prof_name=prof_name,prof_id=prof_id,seats_available=seats_available,description=description,prerequisites=prerequisites,start_time=start_time,end_time=end_time)
            reg.save()


        return render(request,'add_courses.html')
    else:
        return redirect('/home')



def base(request):
    return render(request,"base.html")


def disp_nav(request):
    return render(request,'navbar.html')