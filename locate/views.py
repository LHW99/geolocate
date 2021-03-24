from django.shortcuts import render
try:
  from stock_portfolio.settings.private_settings import API_KEY
except:
  print('ok')

def home(request):
  return render(request, 'home.html')