from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from selenium import webdriver
import time
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
from home.models import Meet, Message, Buffer
import speech_recognition as sr
from django.http import JsonResponse

def Glogin(mail_address, password,driver):
	# Login Page
	driver.get(
		'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

	# input Gmail
	driver.find_element_by_id("identifierId").send_keys(mail_address)
	driver.find_element_by_id("identifierNext").click()
	driver.implicitly_wait(10)

	# input Password
	driver.find_element_by_xpath(
		'//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
	driver.implicitly_wait(10)
	driver.find_element_by_id("passwordNext").click()
	driver.implicitly_wait(10)

	# go to google home page
	driver.get('https://google.com/')
	driver.implicitly_wait(100)

#------------------------------------------------------------------------------------------------

def home(request): 
    return render(request, "home.html")

def handleSignUp(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('dashboard')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('dashboard')
    
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        login(request, myuser)
        messages.success(request, "Account successfully created")
        return redirect('dashboard')

    else:
        return HttpResponse("404 - Not found")


def handeLogin(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect('dashboard')

    return HttpResponse("404- Not found")
    return HttpResponse("login")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('dashboard')

def dashboard(request): 
    return render(request, "dashboard.html")

def meet(request): 
    if request.method=="POST":
        code=request.POST['code']
        meet_obj = Meet.objects.filter(code = code).first()

        if meet_obj:
            if meet_obj.status :
                context={'code':code}
                return render(request, "postMessage.html", context)

            messages.error(request, "The meeting code is not active")
            return render(request, "home.html")
        messages.error(request, "The meeting code is not active")
        return render(request, "home.html")


def meetMessage(request,slug):
    context={'code':slug}
    return render(request, "meetMessage.html", context)

@csrf_exempt
def postMessage(request,slug): 
    if request.method == "POST":
        content = request.POST.get('content')
        meet= Meet.objects.get(code=slug)
        context={'code':slug}
               
    return render(request, "postMessage.html", context)

def enter(request, slug): 

    code = slug

    opt = Options()
    opt.add_argument('--disable-blink-features=AutomationControlled')
    opt.add_argument('--start-maximized')
    opt.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 0,
        "profile.default_content_setting_values.notifications": 1
    })

    Glogin(mail_address, password, driver)

    driver.get('https://meet.google.com/'+code)
    
    messages = Message.objects.filter(code = slug)
    context={'code':slug, 'messages': messages}
    url = slug + "/newMessages"
    return redirect(url)


def newMessages(request, slug): 
    messages = Message.objects.filter(code = slug)
    context={'code':slug, 'messages': messages}
    return render(request, "newMessages.html", context)


def bufferMessages(request, slug): 
    messages = Buffer.objects.filter(code = slug)
    context={'code':slug, 'messages': messages}
    return render(request, "bufferMessages.html", context)

def deleteMessage(request, slug, id): 
    message = Message.objects.get(sno = id)
    message.delete()
    messages = Message.objects.filter(code = slug)
    context={'code':slug, 'messages': messages}
    return render(request, "newMessages.html", context)

def buffer(request, slug, id): 
    message = Message.objects.get(sno = id)
    buffer = Buffer(content=message.content, meet=message.meet, code=slug)
    buffer.save()
    message.delete()
    messages = Message.objects.filter(code = slug)
    context={'code':slug, 'messages': messages}
    return render(request, "newMessages.html", context)
