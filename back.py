# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 18:02:39 2020

@author: MSI
"""



def weather():
  import pyowm
  import geocoder
  from datetime import date
  import json


  with open('data.json') as f:
    categories = json.load(f)

  


  #Key from OpenWeather
  Api_Key = 'd9658ab3ed06a8f71622777e5ed08e8e'

  #Get actual date
  year = date.today().year
  day = date.today().day
  name_day = date.today().strftime("%A")
  name_month = date.today().strftime("%B")

  #Get actiual country and city using ip adress
  g = geocoder.ip('me')
  city = g.city
  country = g.country


  location = city + ', ' + country




  #Current weather a givwn city 
  owm = pyowm.OWM(Api_Key)
  mgr = owm.weather_manager()

  observation = mgr.weather_at_place(location)

  w = observation.weather
  detailed_status = w.detailed_status
  temperature = int(round( w.temp['temp'] - 273.1, 0))
#Asign 1 of 5 weather categories
  for i in categories:
    status = categories[i]['status']
      
    for ii in status:
          
      if detailed_status == ii:
        Categorie = i
        break


  fecha = name_day + ', ' + name_month + ' '  + str(day) + ', ' + str(year) 



  activities = categories[Categorie]['activities']
  temperature = str(temperature ) + ' °C'

  return fecha, location, Categorie, activities, temperature


















