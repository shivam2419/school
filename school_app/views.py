from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .models import contact as Cont
import datetime

# Create your views here.
current_time = datetime.datetime.now()
today_date=datetime.date.today()
current_year=current_time.year  

session_context={
    "year":current_year,
    "next_year":current_year+1,
    "over_year":current_year+2,
    "date":today_date
}

def index(request):
    if request.method=="POST":
        fname=request.POST.get('f_name')
        lname=request.POST.get('l_name')
        email=request.POST.get('email')
        pnum=request.POST.get('pnum')

        submit=home_form(f_name=fname,l_name=lname,email=email,pnum=pnum)
        submit.save()
    stud =event.objects.order_by('-created_at')
    acti=activity.objects.all()
    note=notice.objects.order_by('-created_at')
    s={'stu':stud,'act':acti,'note':note}
    return render(request,('index.html'),s)

def about(request):
    return render(request,('about.html'))

def gallery(request):
    inaug=inaugration.objects.all()
    assem=assembly.objects.all()
    func=function.objects.all()
    pt=Pt.objects.all()
    context={'inaug':inaug,'assem':assem,'func':func,'pt':pt}
    return render(request,('Gallery.html'),context)

def admission(request):
    # todaydate=date.today()
    return render(request,('admission.html'),session_context)

def admission2(request):
    return render(request,('admission2.html'),session_context)

def contact(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        text=request.POST.get('txt')

        contact_submit=Cont(f_name=fname,l_name=lname,email=email,desc=text)
        contact_submit.save()
    return render(request,('contact.html'))

def service(request):
    return render(request,('service.html'),session_context)

def register(request):
    if request.method=="POST":
        sname=request.POST.get('txtFieldValue_0')
        fname=request.POST.get('txtFieldValue_1')
        mname=request.POST.get('txtFieldValue_2')
        Dob=request.POST.get('txtFieldValue_3')
        pnum=request.POST.get('txtFieldValue_4')
        email=request.POST.get('txtFieldValue_5')
        gender=request.POST.get('txtFieldValue_6')
        applied_for=request.POST.get('txtFieldValue_7')
        last_school=request.POST.get('txtFieldValue_8')
        address=request.POST.get('txtFieldValue_9')
        trans_require=request.POST.get('txtFieldValue_10')

        regis_submit=registration(student_name=sname,father_name=fname,mother_name=mname,dob=Dob,phone_number=pnum,email_id=email,gender=gender,class_for=applied_for,last_schl=last_school,address=address,trans_req=trans_require)

        regis_submit.save()
    
    return render(request,('admission.html'))

def EventInfo(request):
    data = event.objects.all()
    context = {
        'data' : data
    }
    return render(request, 'eventinfo.html', context)

# Admin section
def admin(request):
    return render(request, 'admin/index.html')
def enquiry_dashboard(request):
    data = registration.objects.all()
    context = {
        'items' : data
    }
    return render(request, 'admin/dashboard.html', context)

def EnquiryInfo(request, pk):
    try:
        data = registration.objects.get(id=pk)
    except registration.DoesNotExist:
        # Handle the case where the registration with the given id doesn't exist
        return render(request, 'admin/error.html', {'message': 'Registration does not exist'})

    context = {'item': data}
    if request.method == 'POST':
        try:
            Info = registration.objects.get(id=pk)
            Info.delete()
            print('done')
            return redirect('Dashboard')
        except registration.DoesNotExist:
            # Handle the case where the registration with the given id doesn't exist
            print('noe')
            return render(request, 'admin/error.html', {'message': 'Registration does not exist'})

    return render(request, 'admin/enquiry_info.html', context)

def Activities_images(request):
    if request.method == 'POST':
        # Get the uploaded file from the request
        files = request.FILES.getlist('file')
        for file in files:
            new_instance = activity(activity=file)
            new_instance.save()
    
    top_obj = activity.objects.order_by('-id').first()
    images = activity.objects.order_by('-created_at')

    context = {
        'images': images,
        'top' : top_obj.activity.url,
    }
    return render(request, 'admin/activities.html', context)
def deleteActivity(request, pk):
    if request.method == 'POST':
        data = activity.objects.get(id=pk)
        data.delete()
        return redirect('Activities')
    data = activity.objects.get(id=pk)
    return render(request, 'admin/delete_activities.html', {'data' : data})

# Event section

def Events(request):
    if request.method == 'POST':
        name = request.POST.get('event_name')
        desc = request.POST.get('event_desc')

        date_string = request.POST.get('event_date')
        date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        date = date_obj.day
        months_dict = {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December'
        }
        month = date_obj.month

        img = request.FILES['event_img']
        print(img)
        obj = event(event = name, event_desc = desc, event_img = img, date = date, month = months_dict[month])
        obj.save()

    data = event.objects.order_by('-created_at')
    context = {
        'data' : data
    }
    return render(request, 'admin/eventsdata.html', context)

def deleteEvent(request, pk):
    if request.method == 'POST':
        data = event.objects.get(id=pk)
        data.delete()
        return redirect('Events')
    data = event.objects.get(id=pk)
    return render(request, 'admin/eventdelete.html', {'data' : data})


# Notice section

def Notices(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        notices = request.POST.get('notice')
        
        obj = notice(date = date, notice = notices)
        obj.save()
    data = notice.objects.order_by('-created_at')
    context = {
        'data' : data
    }
    return render(request, 'admin/noticedata.html', context)

def deleteNotice(request, pk):
    if request.method == 'POST':
        data = notice.objects.get(id=pk)
        data.delete()
        return redirect('Notice')
    data = notice.objects.get(id=pk)
    return render(request, 'admin/deletenotice.html', {'data':data})

# School gallery section
def School_gallery(request):
    return render(request, 'admin/school_gallery.html')

def addInaugration(request):
    if request.method == 'POST':
        # Get the uploaded file from the request
        files = request.FILES.getlist('file')
        for file in files:
            new_instance = inaugration(inaugration=file)
            new_instance.save()
    
    top_obj = inaugration.objects.order_by('-id').first().inaugration.url
    images = inaugration.objects.order_by('-created_at')

    own_id = 1
    context = {'top' : top_obj,
               'images' : images,
               'id' : own_id
               }
    return render(request, 'admin/addinaugration.html',context)

def addAssembly(request):
    if request.method == 'POST':
        # Get the uploaded file from the request
        files = request.FILES.getlist('file')
        for file in files:
            new_instance = assembly(assembly=file)
            new_instance.save()
    
    top_obj = assembly.objects.order_by('-id').first()
    if top_obj : 
        top_obj = top_obj.assembly.url
    images = assembly.objects.order_by('-created_at')

    own_id = 2
    context = {'top' : top_obj,
               'images' : images,
               'id' : own_id
               }
    return render(request, 'admin/addassembly.html', context)

def addFunction(request):
    if request.method == 'POST':
        # Get the uploaded file from the request
        files = request.FILES.getlist('file')
        for file in files:
            new_instance = function(function=file)
            new_instance.save()
    
    top_obj = function.objects.order_by('-id').first()
    if top_obj :
        top_obj = top_obj.function.url
    images = function.objects.order_by('-created_at')

    own_id = 3
    context = {'top' : top_obj,
               'images' : images,
               'id' : own_id
               }
    return render(request, 'admin/addfunction.html', context)

def addPt(request):
    if request.method == 'POST':
        # Get the uploaded file from the request
        files = request.FILES.getlist('file')
        for file in files:
            new_instance = Pt(Pt=file)
            new_instance.save()
    
    top_obj = Pt.objects.order_by('-id').first()
    if top_obj :
        top_obj = top_obj.Pt.url
    images = Pt.objects.order_by('-created_at')

    own_id = 4
    context = {'top' : top_obj,
               'images' : images,
               'id' : own_id
               }
    return render(request, 'admin/addpt.html', context)

# Delete from gallery
def deleteGallery(request, pk, pk1):
    if pk == '1':
        obj = inaugration.objects.get(id = pk1)
        obj.delete()
        return redirect('addInaugration')
    elif pk == '2':
        obj = assembly.objects.get(id = pk1)
        obj.delete()
        return redirect('addAssembly')
    elif pk == '3':
        obj = function.objects.get(id = pk1)
        obj.delete()
        return redirect('addFunction')
    elif pk == '4':
        obj = Pt.objects.get(id = pk1)
        obj.delete()
        return redirect('addPt')
    return render(request, 'admin/deletegallery.html')