from django.shortcuts import render
from .models import Customer, User, Tracking, University, Level, Subject
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.response import Response
from .forms import UniversitiesFilterForm, GuestCustomerForm
from django.db.models import Q


# Create your views here.
def trackingUser(user, path):
    tracking = Tracking.objects.create(userName=user.username, request=path)
    tracking.save()


def index(request):
    universities = University.objects.all()[:4]
    return render(request, 'main/index.html', context={'universities': universities})


def universitiesFilter(request):
    form = GuestCustomerForm()
    universities_filter = None
    if request.method == 'POST':
        form = GuestCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            ielts_overall = float(form.cleaned_data['ielts_overall'])
            ielts_min = float(form.cleaned_data['ielts_min'])
            universities_filter = University.objects.filter(subjects=form.cleaned_data['subject']).filter(
                Q(level__levelName=form.cleaned_data['level']) & Q(
                    level__ieltOverall__lte=ielts_overall) & Q(
                    level__ieltsMin__lte=ielts_min))
    return render(request, 'main/universitiesFilter.html',
                  context={'universities_filter': universities_filter, 'form': form})


def universities(request):
    universities = University.objects.all()
    return render(request, 'main/universities.html', context={'universities': universities})


def university_detail(request, university_id):
    university = University.objects.get(id=university_id)
    subjects = Subject.objects.filter(universities=university)
    return render(request, 'main/universityDetail.html', context={'university': university, 'subjects': subjects})


@login_required
def customers(request):
    # trackingUser(request.user, request.get_full_path())
    pageName = 'customers'
    customers = Customer.objects.all()
    tableHeader = ['ID', 'Full Name', 'Phone Number', 'Current Job', 'Status']
    return render(request, 'main/table.html',
                  context={'customers': customers, 'tableHeader': tableHeader, 'pageName': pageName})


@login_required
def customerDetail(request, customer_id):
    # trackingUser(request.user, request.get_full_path())
    customer = Customer.objects.get(id=customer_id)
    return render(request, 'main/customer.html', context={'customer': customer})


@login_required
def userDetail(request, userId):
    user = User.objects.get(id=userId)
    return render(request, 'main/user.html', context={'user': user})


@login_required
def tracking(request):
    pageName = 'tracking'
    tracks = Tracking.objects.order_by('-date')
    tableHeader = ['Tên người dùng', 'Trang', 'Thời gian']
    return render(request, 'main/table.html',
                  context={'tracks': tracks, 'tableHeader': tableHeader, 'pageName': pageName})
