from aiogram import Bot, Dispatcher, executor, types
import python_weather

bot = Bot(token="TOKEN")
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather.IMPERIAL)

@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.get(message.text)
    celsius = (weather.current.temperature - 32) / 1.8

    resp_msg = str(weather.nearest_area) + "\n"
    resp_msg += f"Текущая температура: {round(celsius)}\n"
    resp_msg += f"Влажность: {weather.current.humidity}\n"
    resp_msg += f"Скорость ветра: {weather.current.wind_speed}"

    await message.answer(resp_msg)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

