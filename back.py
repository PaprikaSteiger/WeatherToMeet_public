# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 18:02:39 2020

@author: MSI
"""











def weather():
  import pyowm
  import geocoder
  from datetime import date

  categories = {
      'Sun' : {
          'status':['clear sky'],
          
          'activities' :["It's sunny! Have a barbeque with your friends and roast some marshmellows.",
                         "The sun is out! Grab a book, go to the park and get a tan. ",
                         "It's sunny! Take your hiking boots and watch the sunset from the highest point nearby.",
                         "The sun is out! Message your friend with the nicest balcony, garden, or rooftop and invite yourself over.",
                         
              
              ],
          
          
          
          },
      
      'SunWithClouds' : {
          'status':['few clouds', 'scattered clouds'],
          
          'activities' :["No rain today! Let's play minigolf with your friends - the loser needs to pay the beer and pizza after.",
                         "It's windy! Go fly a kite!"
              
              ],
          
          
          },
      
      'Clouds' : {
          'status':['light thunderstorm', 'thunderstorm', 'ragged thunderstorm', 
                    'heavy thunderstorm', 'mist', 'Haze', 'fog', 'broken clouds',
                    'overcast clouds'],
          
          'activities' :["No rain today! Take some old bread with you and feed the ducks by the lake.",
                         "It's cloudy today! Gather your board games and battle your friends for a game night.",
                         "The sun is gone! Invite your friends with their favourite bottle of wine and have a wine tasting.",
                         "Be aware of cloudy thoughts! Invite your friends for a yoga and meditation session.",
              ],
          
          
          
          
          },
      
      'CloudsWithRain' : {
          'status':['thunderstorm with light rain', 'thunderstorm with rain', 
                    'thunderstorm with heavy rain', 'thunderstorm with light drizzle',
                    'thunderstorm with drizzle', 'thunderstorm with heavy drizzle',
                    'light intensity drizzle', 'drizzle', 'heavy intensity drizzle',
                    'light intensity drizzle rain', 'drizzle rain', 'heavy intensity drizzle rain',
                    'shower rain and drizzle', 'heavy shower rain and drizzle', 'shower drizzle',
                    'light rain', 'moderate rain', 'heavy intensity rain', 'very heavy rain',
                    'extreme rain', 'freezing rain', 'light intensity shower rain', 'shower rain',
                    'heavy intensity shower rain', 'ragged shower rain'],
          
          'activities' :["What a rainy day! Choose any country from another continent and have a themed dinner party with friends.",
                         "Keep the rain drops away from your mood! Pile up all the snacks you have and screen your favourite childhood movies.",
                         
              
              ],
          
          
          
          
          
          },
      
      'CloudsWithSnow' : {
          'status':['light snow', 'Snow', 'Heavy snow', 'Light shower snow', 'Shower snow', 
                    'Heavy shower snow', 'Sleet', 'Light shower sleet', 'Shower sleet',
                    'Light rain and snow', 'Rain and snow'],
          
          'activities' :['Snow is falling! Battle your friends in "Who can do the ugliest snow angel?"',
                         "Look at the snow! Take a sled (or plastic bag) and find the next hill to sled down.",
                         "Snow is falling - Christmas is nearby! Get active and start decorating your appartment.",
                         "It's cold and snow is falling! Meet your friends in the parc and enjoy the frosty evening with a large thermos pitcher of Gluehwein."
              
              ],
          
          
          
          
          
          },
      'Warning' : {
          'status':['volcanic ash', 'sand/ dust whirls', 'sand', 'dust', 'Smoke',
                    'squalls', 'tornado'],
          
          'activities' :["Take care, stay at home"
              
              ],
          
          
          
          
          
          },
      
      }


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

















