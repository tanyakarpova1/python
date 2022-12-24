import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from pyowm import OWM
from pyowm.utils.config import get_default_config


bot = Bot(token='5948642193:AAHz4mb_AG9xPX9jYlajWEwcZYiPkXEbB5g')
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши название города и я пришлю прогноз погоды")


@dp.message_handler()
async def get_weather(message: types.Message):
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    owm = OWM('c1afae166690c0e89087d73758e4ef27')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    state = w.detailed_status
    w.wind()
    humidity = w.humidity
    temperature = w.temperature('celsius')['temp']

    def weather():
        print("В городе " + str(message.text) + " сегодня " + str(state) +
              "\nТемпература " + str(
            round(temperature)) + " градусов по цельсию" +
              "\nВлажность составляет " + str(humidity) + "%" +
              "\nСкорость ветра " + str(w.wind()['speed']) + " метров в секунду")

    weather()

    await message.reply("В городе " + str(message.text) + " сегодня " + str(state) +
              "\nТемпература " + str(
            round(temperature)) + " градусов по цельсию" +
              "\nВлажность составляет " + str(humidity) + "%" +
              "\nСкорость ветра " + str(w.wind()['speed']) + " метров в секунду")

    if (temperature < -10):
        await message.reply("Рекомендация по одежде: Свитер; зимняя шапка; зимняя куртка с капющоном; перчатки; утепленные штаны; шарф")
    elif (temperature < 0 and temperature > -10):
        await message.reply("Рекомендация по одежде: Зимняя куртка, зимняя шапка, шарф, утепленные штаны")
    elif (temperature > 0 and temperature < 5):
        await message.reply("Рекормендация по одежде: Дубленка или пуховик; осенние ботинки или кроссовки; джинсы; осенняя шапка и шарф")
    elif (temperature > 5 and temperature < 10):
        await message.reply("Рекомендация по одежде: Джинсы или брюки, осенние ботинки, сапоги или кроссовки; куртка")
    elif (temperature > 10 and temperature < 15):
        await message.reply("Рекомендация по одежде: Брюки или спортивные штаны, джинсы; ветровка или толстовка; кроссовки")
    elif (temperature > 15 and temperature < 20):
        await message.reply("Рекомендация по одежде: Футболка; легкая куртка; кроссовки;Брюки или спортивные штаны, джинсы ")
    elif (temperature > 20):
        await message.reply("Рекомендация по одежде: Легкие штаны или шорты, футболка; летние кроссовки, сандалии или босоножки")


if __name__ == "__main__":
    executor.start_polling(dp)
