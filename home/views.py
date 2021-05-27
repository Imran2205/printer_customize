from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserPhoneNumberForm, AccountCompleteForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from .models import BestOffers, ProfileInfo, ABL, BedSize, Covered, Display, FilamentChamber, FilamentQuantity, Height, MotorDriver, Nozzle, UPSModule, WiFi, Orders, LatestProduct, OurOwnProduct
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import datetime
import shortuuid

PRINT_ORDER_STR = 'print'
PRINTER_ORDER_STR = 'printer'

def home(request):
    best_offers = BestOffers.objects.all()
    abls = ABL.objects.all()
    bed_size = BedSize.objects.all()
    cover = Covered.objects.all()
    display = Display.objects.all()
    filament_chamber = FilamentChamber.objects.all()
    filament_quantity = FilamentQuantity.objects.all()
    height = Height.objects.all()
    motor_driver = MotorDriver.objects.all()
    nozzle = Nozzle.objects.all()
    ups_module = UPSModule.objects.all()
    wifi = WiFi.objects.all()
    latest_products = LatestProduct.objects.all()
    own_products = OurOwnProduct.objects.all()
    context = {
        'best_offers': best_offers,
        'abls': abls,
        'bed_size': bed_size,
        'cover': cover,
        'display': display,
        'filament_chamber': filament_chamber,
        'filament_quantity': filament_quantity,
        'height': height,
        'motor_driver': motor_driver,
        'nozzle': nozzle,
        'ups_module': ups_module,
        'wifi': wifi,
        'title': 'Machronics Geo|Customize your 3d printer',
        'latest_products': latest_products,
        'own_products': own_products
    }
    return render(request, 'home/home.html', context)


def complete_profile(request):
    context = {

    }
    return render(request, 'home/complete_profile.html', context)

def file_upload(request):
    context = {

    }
    return render(request, 'home/file_upload.html', context)

def link_upload(request):
    context = {

    }
    return render(request, 'home/link_upload.html', context)

def print_order(request):
    context = {

    }
    return render(request, 'home/print_order.html', context)

def login_register(request, log_or_reg='login'):
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST)
        phone_form = User_phone_number_form(request.POST)
        login_form = AuthenticationForm(request, request.POST)
        if user_form.is_valid() and phone_form.is_valid():
            user = user_form.save(commit = False)
            user.is_active = False
            user.save()
            phone = phone_form.save(commit = False)
            phone.user = user
            phone.user_id_no = shortuuid.uuid(name = user.username)
            phone.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account'
            message = render_to_string('home/acc_active_email.html',{
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = user_form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to = [to_email]
            )
            email.send()
            messages.success(request, f'Registration complete! Please verify your email before trying to login!')
            return redirect('login_register', log_or_reg='login')
        elif login_form.is_valid():
            #username = request.POST.get('username')
            #password = request.POST.get('password')
            """username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user:
   
             if user.is_active:
                    login(request, user)
                    messages.success(request, f'Login successful.')
                    return redirect('home')
                else:
                    messages.error(request, f'Your account is inactive.')
                    return redirect('login_register')
            else:
                messages.error(request, f'Username or password is incorrect')
                return redirect('login_register')"""
            login(request, login_form.get_user())
            return redirect('home')
        else:
            if 'first_name' in request.POST:
                messages.error(request, f'register')
            else:
                messages.error(request, f'login')

    else:
        user_form = UserRegisterForm()
        phone_form = User_phone_number_form()
        login_form = AuthenticationForm(request)
        if log_or_reg == 'register':
            messages.error(request, f'register')
        else:
            messages.error(request, f'login')

    context = {
        'user_form': user_form,
        'phone_form': phone_form,
        'login_form': login_form
    }

    return render(request, 'home/login.html', context=context)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, f'Verification done! You may now login.')
        return redirect('login_register', log_or_reg='login')
    else:
        messages.success(request, f'Verification Failed! Please try again or contact us for verifying your account.')
        return redirect('login_register', log_or_reg='login')

@login_required
def dashboard(request):
    orders = Orders.objects.filter(user = request.user)
    profiles = ProfileInfo.objects.filter(user = request.user)
    context = {
        'orders': orders,
        'profiles': profiles,
        'title': 'User Dashboard'
    }
    return render(request, 'home/dashboard.html', context)

def ajax_form_save(request):
    current_user = request.user
    if request.method == "GET" and request.is_ajax():
        price = request.GET.get('price', None)
        abls = request.GET.get('abls', None)
        bed_size = request.GET.get('bed_size', None)
        cover = request.GET.get('cover', None)
        display = request.GET.get('display', None)
        filament_chamber = request.GET.get('filament_chamber', None)
        filament_quantity = request.GET.get('filament_quantity', None)
        height = request.GET.get('height', None)
        motor_driver = request.GET.get('motor_driver', None)
        nozzle = request.GET.get('nozzle', None)
        ups_module = request.GET.get('ups_module', None)
        wifi = request.GET.get('wifi', None)
        try:
            instance = Orders()
            instance.user = current_user
            instance.title = current_user.username + '@' + str(datetime.datetime.now())
            instance.price = price
            instance.wifi = wifi
            instance.ups_module = ups_module
            instance.nozzle = nozzle
            instance.height = height
            instance.filament_chamber = filament_chamber
            instance.filament = filament_quantity
            instance.bed_size = bed_size
            instance.cover = cover
            instance.abl = abls
            instance.display = display
            instance.motor_driver_type = motor_driver
            instance.save()
            instance.order_id_no = shortuuid.uuid(name = PRINTER_ORDER_STR+str(instance.id))
            instance.save(update_fields=['order_id_no'])
        except Exception as e:
            return JsonResponse({"success": False}, status=400)
        return JsonResponse({}, status=200)
    return JsonResponse({"success": False}, status=400)