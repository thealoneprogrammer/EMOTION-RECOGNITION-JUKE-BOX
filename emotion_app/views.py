from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Auth
from django.http import JsonResponse, HttpResponse
import uuid
from emotion_app import Testing_Final_Webcam, Testing_Final
from shutil import copyfile
import os
import glob

@csrf_exempt
def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        happy_songs = []
        angry_songs = []
        disgust_songs = []
        fear_songs = []
        neutral_songs = []
        sad_songs = []
        surprise_songs = []

        arr = os.listdir(os.path.dirname(__file__) + '/../static/assets/js/songs/happy')
        happy_songs.append(arr)

        arr = os.listdir(os.path.dirname(__file__) + '/../static/assets/js/songs/angry')
        angry_songs.append(arr)

        arr = os.listdir(os.path.dirname(__file__) + '/../static/assets/js/songs/disgust')
        disgust_songs.append(arr)

        arr = os.listdir(os.path.dirname(__file__) + '/../static/assets/js/songs/fear')
        fear_songs.append(arr)

        arr = os.listdir(os.path.dirname(__file__) + '/../static/assets/js/songs/neutral')
        neutral_songs.append(arr)

        arr = os.listdir(os.path.dirname(__file__) + '/../static/assets/js/songs/sad')
        sad_songs.append(arr)

        arr = os.listdir(os.path.dirname(__file__) + '/../static/assets/js/songs/surprise')
        surprise_songs.append(arr)

        try:
            Auth.objects.get(user_name=username, password=password)
            return render(request, 'main.html', {"happy_songs": happy_songs, "angry_songs": angry_songs, "disgust_songs": disgust_songs, "fear_songs": fear_songs, "neutral_songs": neutral_songs, "sad_songs": sad_songs, "surprise_songs": surprise_songs})

        except:
            return render(request, 'home.html', {"error_msg": "Username and password does not match!!..."})


@csrf_exempt
def dashboard(request):
    if request.method == 'GET':
        return render(request, 'main.html')


@csrf_exempt
def logout(request):
    if request.method == 'GET':
        return render(request, 'home.html')


@csrf_exempt
def open_camera(request):
    if request.method == 'POST':
        print("inside open camera")
        Testing_Final_Webcam.load_webcam()
        return render(request, 'home.html')


@csrf_exempt
def process_image(request):
    if request.method == 'POST':
        img = request.POST.get('image')
        response = Testing_Final.getImagePath(img)
        # print(type(response[0]))
        return HttpResponse(response[0], status=200)


@csrf_exempt
def upload_new_song(request):
    if request.method == 'POST':
        song = request.POST.get('song')
        folder = request.POST.get('folder')
        copyfile(os.path.dirname(__file__) + '/test_songs/' + song, os.path.dirname(__file__) + '/../static/assets/js/songs/' + folder + '/' + song)
        return HttpResponse("response[0]", status=200)


@csrf_exempt
def reset(request):
    if request.method == 'POST':
        username = request.POST['reset-username']
        new_password = request.POST['reset-password']

        try:
            info = Auth.objects.get(user_name=username)
            info.password = new_password
            info.save()

            return render(request, 'home.html', {"reset_success_msg": "Password Updated"})
        except:
            return render(request, 'home.html', {"reset_error_msg": "User does not exists!!..."})



