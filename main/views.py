from django.shortcuts import render
#import json to load json data into python dictionary
import json
#urllib.request to make a request api
import urllib.request


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
    
    #source contains JSON data from API
        source = urllib.request.urlopen(
    'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=afcd952a09ac2e0735a7a4412f5d5234'
         ).read()
  
        
    
    #converting JSON data to dictionary
        list_of_data = json.loads(source)

    #data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
            + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data = {}
    return render(request, "main/index.html", data)