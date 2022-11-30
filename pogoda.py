from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
place = input("Введите ваш город: ")
owm = OWM('c1afae166690c0e89087d73758e4ef27')
mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather
state = w.detailed_status
w.wind()
humidity = w.humidity
temperature = w.temperature('celsius')['temp']
def weather():
    print("В городе " + str(place) + " сегодня " + str(state) +
          "\nТемпература " + str(
        round(temperature)) + " градусов по цельсию" +
          "\nВлажность составляет " + str(humidity) + "%" +
          "\nСкорость ветра " + str(w.wind()['speed']) + " метров в секунду")
weather()
