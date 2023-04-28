from django.shortcuts import render
import json
import urllib.request

def home(request):
    if request.method=='POST':
        city=request.POST.get('data')
        res=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=06efd6bdaaf07088da04bf9eb4272205').read()
        json_data=json.loads(res)
        data={
            "country_code":str(json_data['sys']['country']),
            "coordinate":str(json_data['coord']['lon'])+ ' Lon'+'  '+ str(json_data['coord']['lat'])+ ' lat',
            "temp":str(json_data['main']['temp']) + 'k',
            "pressure":str(json_data['main']['pressure']),
            "humidity":str(json_data['main']['humidity']),
            "city":city,
            }
    else:
        data={}    

        
        
        
    
    return render(request,'index.html',data)

# Create your views here.
