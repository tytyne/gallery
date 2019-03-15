

import datetime as dt
from django.shortcuts import render
from .models import Article
from django.http import HttpResponse,Http404

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune')
# def photos_of_day(request):
#     date = dt.date.today()
#     html = f'''
#         <html>
#             <body>
#                 <h1> {date.day}-{date.month}-{date.year}</h1>
#             </body>
#         </html>
#             '''
#     # return HttpResponse(html)
#     return render(request, 'all-photos/today-photos.html', {"date": date,})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day
# def past_days_photos(request,past_date):
#     try:
#         # Converts data from the string Url
#         date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

#     except ValueError:
#         # Raise 404 error when ValueError is thrown
#         raise Http404()
#     day = convert_dates(date)
#     html = f'''
#         <html>
#             <body>
#                 <h1>photos for {day} {date.day}-{date.month}-{date.year}</h1>
#             </body>
#         </html>
#             '''
#     return HttpResponse(html)    
def photos_today(request):
    date = dt.date.today()
    photos = Article.todays_photos()
    return render(request, 'all-photos/today-photos.html', {"date": date,"photos":photos})
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
def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})   
def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/article.html", {"article":article})        
