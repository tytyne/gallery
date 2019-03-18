

import datetime as dt
from django.shortcuts import render
from .models import Article
from django.http import HttpResponse,Http404

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune')

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day
 
def photos_today(request):
    date = dt.date.today()
    photos = Article.todays_photos()
    return render(request, 'all-photos/article.html', {"date": date,"photos":photos})
def past_days_photos(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photos_today)

    photos = Article.days_photos(date)
    return render(request, 'all-photos/past-photos.html',{"date": date,"photos":photos})    


def search_category(request):
    locations = Location.objects.all()
    if 'category' in request.GET and request.GET['category']:
        search_term = (request.GET.get('category')).title()
        searched_images = Article.search_by_category(search_term)
        message = f'{search_term}'
        return render(request,'search.html',{'message':message,'images':searched_images,'locations':locations})

    else:
        message = "You haven't searched for any category"
        return render(request,'search.html',{'message':message,'locations':locations})

        return render(request, 'all-photos/search.html',{"message":message})
 
def article(request):
  
    article = Article.objects.all()
    print(article)
    
    return render(request,"all-photos/article.html", {"article":article})        
