from django.shortcuts import render
from .models import home_form,event,activity,notice,registration,inaugration,assembly,function,Pt
from .models import contact as Cont
import datetime
# Create your views here.
current_time = datetime.datetime.now()
today_date=datetime.date.today()
current_year=current_time.year  

context={
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
    stud=event.objects.all()
    acti=activity.objects.all()
    note=notice.objects.all()
    s={'stu':stud,'act':acti,'note':note}
    # s.update()
    # a.update()
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
   
    return render(request,('admission.html'),context)
def admission2(request):
    return render(request,('admission2.html'),context)

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
    return render(request,('service.html'),context)

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
