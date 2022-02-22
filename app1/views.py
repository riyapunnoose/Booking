from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Booking
from .models import admins, user_det
from .models import Event
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.db.models import Count


# Create your views here.
@login_required()
def first(request):
    return render(request, "third.html")




@login_required()
def pay(request):
    return render(request, "payment.html")


def login(request):
    return render(request, "first.html")


@login_required()
def adminpage(request):
    return render(request, "admin.html")


@login_required()
def Fourth(request, id):
    event = Event.objects.filter(id=id)
    return render(request, "fourth.html", {'event': event})


def register(request):
    a = request.POST['username']
    b = request.POST['password']
    f = request.POST['cpassword']
    c = request.POST['firstname']
    e = request.POST['Lastname']
    d = request.POST['email']
    phone = request.POST['phonnum']
    if User.objects.filter(username=a).exists():
        messages.error(request, ("Username or Password Already exists..."))
        return render(request, 'first.html')
    elif b != f:
        messages.error(request, "password and confirm password must be same")
        return render(request, 'first.html')
    else:
        data = User.objects.create_user(username=a, password=b, first_name=c, email=d, last_name=e)
        data.save()
        usd = User.objects.get(username=a)
        usp = user_det.objects.create(user_ids=usd.id, phoneno=phone)
        usp.save()
        return render(request, "third.html")


def log(request):
    if request.method == "POST":
        uname = request.POST['username']
        if admins.objects.filter(username=uname).exists():
            m = admins.objects.get(username=request.POST['username'])
            if m.password == request.POST['password']:
                request.session['user_id'] = m.id
                return render(request, 'admin.html')
            else:
                messages.error(request, "Username or Password Incorrect")
                return render(request, 'third.html')
        elif User.objects.filter(username=uname).exists():
            password = request.POST['password']
            user = auth.authenticate(username=uname, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('second')
            else:
                messages.error(request, "Username or Password Incorrect")
                return render(request, 'third.html')
        else:
            return render(request, 'third.html')
    else:
        return render(request, 'third.html')


def adminside(request):
    a = request.POST['event']
    b = request.POST['about']
    c = request.POST['category']
    f = request.POST['place']
    d = request.POST['price']
    e = request.POST['date']
    data = Event.objects.create(eventid=a, aboutid=b, categoryid=c, EntryFeeid=d, date=e, placeid=f)
    data.save()
    return render(request, 'admin.html')


@login_required()
def SearchEvent(request):
    a1 = request.POST['cls']
    b = Event.objects.filter(categoryid=a1)
    return render(request, 'mainevent.html', {"ue": b})

@login_required()
def bookhistory(request):
    if request.method == "POST":
        ses = request.user.id
        bookings = Booking.objects.filter(uuser_id=ses)
        return render(request, 'history.html', {'books': bookings})


def bookhistoryad(request):
    h = Booking.objects.all()
    return render(request, 'adhistory.html', {'h': h})


def bookhistoryEV(request):
    h = Event.objects.all()
    return render(request, 'eventhistory.html', {'h': h})



def logout_view(request):
    logout(request)
    return redirect(log)


def deleteing(request):
    u = request.POST['Catid']
    Event.objects.filter(eventid=u).delete()
    return redirect(bookhistoryEV)


@login_required()
def booking(request, id):
    if request.method == "POST":
        name = request.POST['Name']
        nos = request.POST['NoOFTick']
        if nos == "0":
            messages.error(request, "Please select your ticket")
            return redirect('Fourth', id)
        else:
            ses = request.user.id
            fee = Event.objects.get(id=id)
            total = fee.EntryFeeid * int(nos)
            Booking.objects.create(name=name, nos=nos, Evnt_id=fee.placeid, total=total, uuser_id=ses).save()
            temp = Booking.objects.filter(uuser_id=ses).latest('date_now')
            one = Booking.objects.filter(date_now=temp.date_now)
            return render(request, 'confirm.html', {'temp': one})
    else:
        return redirect('Fourth', id)

@login_required()
def second(request):
    return render(request, 'Home.html')
def main(request):
    return render(request, 'mainevent.html')

@login_required()
def paymentop(request):
    return render(request, 'success.html')


@login_required()
def pp(request):
    return render(request, 'payment.html')


@login_required()
def ss(request):
    return render(request, 'success.html')


def Forgotpass(request):
    if request.method == 'POST':
        mail = request.POST.get('email')
        if User.objects.filter(email=mail).exists():
            message = ('http://127.0.0.1:8000/log')
            email = EmailMessage('Reset Password Link', 'http://127.0.0.1:8000/change', to=[mail])
            email.send()
            print(email)
            return redirect(log)
        else:
            messages.error(request, 'Invalid Mail ID')
            return redirect(log)
    else:
        return redirect(log)


def change(request):
    if request.method == 'POST':
        a = request.POST['emaill']
        b = request.POST['newpassword']
        c = request.POST['confirmpass']
        if b == c:
            temp = User.objects.get(email=a)
            temp.set_password(b)
            temp.save()
            return render(request, 'third.html')
        else:
            pass
    else:
        return render(request, 'Changepassword.html')


def changepass(request):
    return render(request, 'Changepassword.html')


def ME(request):
    return render(request, 'admin.html')


def Registered_user(request):
    user_list = User.objects.all()
    return render(request, 'user.html', {"ue": user_list})
