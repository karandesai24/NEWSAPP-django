from django.shortcuts import render
import requests
from django.http import HttpResponse

def my_view(request):
    # ...

    # Return a "created" (201) response code.
    return HttpResponse(status=201)

# Create your views here.
def index(request):
    r=requests.get('http://api.mediastack.com/v1/news?access_key=API_KEY&categories =entertainment,-sports & languages = en,&countries=in')
    res=r.json()
    data=res['data']
    title=[]
    description=[]
    image=[]
    url=[]
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['image'])
        url.append(i['url'])

    news=zip(title,description,image,url)
    return render(request,'newsapp/index.html',{'news':news})
