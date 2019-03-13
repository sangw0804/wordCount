from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    if request.method == 'POST':
        text = request.POST.get('content')
        splitted_text = text.strip().split(' ')
        word_counted = {
            word: splitted_text.count(word)
            for word in splitted_text
        }
        return render(request, 'index.html', {'word_counted': word_counted})
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')
