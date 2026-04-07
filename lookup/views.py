from django.shortcuts import render
import requests
import json

AQI_DESCRIPTIONS = {
  "Good": "(0 -50) Air quality is considered satisfactory, and air pollution poses little or no risk.",
  "Moderate": "(51-100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.",
  "Unhealthy for Sensitive Groups": "(101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air.",
  "Unhealthy": "(151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.",
  "Very Unhealthy": "(201 - 300) Health alert: everyone may experience more serious health effects.",
  "Hazardous": "(301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected.",
}

AQI_COLOR_CLASSES = {
  "Good": "good",
  "Moderate": "moderate",
  "Unhealthy for Sensitive Groups": "usg",
  "Unhealthy": "unhealthy",
  "Very Unhealthy": "veryunhealthy",
  "Hazardous": "hazardous",
}

DEFAULT_ZIPCODE = "10001"

def home(request):
  if request.method == "POST":
    zipcode = request.POST.get("zipcode")
    return renderAirNow(request, zipcode)
  else: 
    return renderAirNow(request, DEFAULT_ZIPCODE)

def renderAirNow(request, zipcode):
  api_request = requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=25&API_KEY=CB5551AE-93A9-4FE6-8A67-C9589BB2FA9D")
  
  try:
    api = json.loads(api_request.content)
  except Exception as e:
    api = "Error..."

  category_description = ""
  category_color = ""

  if api != "Error..." and api:
    category_name = api[0]['Category']['Name']
    category_description = AQI_DESCRIPTIONS.get(category_name, "")
    category_color = AQI_COLOR_CLASSES.get(category_name, "")

  return render(request, 'home.html', {
    'api': api,
    'category_description': category_description,
    'category_color': category_color,
  })

def about(request):
  return render(request, 'about.html', {})