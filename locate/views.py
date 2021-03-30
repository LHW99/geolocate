from django.shortcuts import render
try:
  from geolocate.settings.private_settings import API_KEY
except:
  print('ok')
import requests

def home(request):
  if request.method == 'GET':
    response = requests.get(f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&key={API_KEY}&callback=initMap')
    data = response.json()
    print(data)

  return render(request, 'home.html')