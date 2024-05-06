from django.shortcuts import render
from moviepy.editor import *
from sign.forms import textForm
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize

# Create your views here.
from django.http import HttpResponse



def home(request):
    form = textForm()
    return render(request, 'sign/home.html', {'form': form})

def translate(request):
    
    
    if request.method == 'POST':
        form = textForm(request.POST)
        stop_words = set(stopwords.words('english'))
        if form.is_valid():
            user_input = form.cleaned_data['name']
        word_tokens = wordpunct_tokenize(user_input)
        filtered_word_tokens = [word for word in word_tokens if not word.lower() in stop_words]
        sign_videos = []

        for word in filtered_word_tokens:
            sign_videos.append(VideoFileClip('sign/static/img/videos/'+word.upper()+'.mp4'))
        final = concatenate_videoclips(sign_videos)
        final.write_videofile('sign/static/img/videos/finalVideo.mp4')
        return render(request, 'sign/translation.html')
    else:
        return HttpResponse("not found")