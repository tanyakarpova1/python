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
if(temperature<-10):
    print("Рекомендация по одежде: Свитер; зимняя шапка; зимняя куртка с капющоном; перчатки; утепленные штаны; шарф")
elif(temperature<0 and temperature>-10):
    print("Рекомендация по одежде: Зимняя куртка, зимняя шапка, шарф, утепленные штаны")
elif(temperature>0 and temperature<5):
    print("Рекормендация по одежде: Дубленка или пуховик; осенние ботинки или кроссовки; джинсы; осенняя шапка и шарф")
elif(temperature>5 and temperature<10):
    print("Рекомендация по одежде: Джинсы или брюки, осенние ботинки, сапоги или кроссовки; куртка")
elif(temperature>10 and temperature<15):
    print("Рекомендация по одежде: Брюки или спортивные штаны, джинсы; ветровка или толстовка; кроссовки")
elif(temperature>15 and temperature<20):
    print("Рекомендация по одежде: Футболка; легкая куртка; кроссовки;Брюки или спортивные штаны, джинсы ")
elif(temperature>20):
    print("Рекомендация по одежде: Легкие штаны или шорты, футболка; летние кроссовки, сандалии или босоножки")
