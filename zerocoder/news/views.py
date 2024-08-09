from django.shortcuts import render, redirect
from .models import News_post
from .forms import News_post_form

def home(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})

def create_news(request):
    error = ""
    if request.method == 'POST':
        form = News_post_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = "Форма заполнена некорректно"
            return render(request, 'news/news.html')
    form = News_post_form()
    return render(request, 'news/add_new_post.html', {'form': form, 'errors': error})