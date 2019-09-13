"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

print(ephem.constellation(m))
('Sgr', 'Sagittarius')

    The constellation() function returns a tuple containing the abbreviated name and full name of the constellation in which its argument lies.
    You can either pass a Body whose position is computed, or a tuple (ra, dec) of coordinates — in which case epoch 2000 is assumed unless you also pass an epoch= keyword argument specifying another value.

"""
import logging
import ephem
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def get_planet_name(bot, update):    
    planet_list = ['Mars', 'Mercury', 'Saturn', 'Venus', 'Uranus', 'Jupiter', 'Sun', 'Neptune', 'Pluto', 'Moon'] 
    t = update.message.text
    logging.info(f'вызван get_planet_name + {update.message.text}')
    tlist = t.split()
    planet = list(set(planet_list) & set(tlist))
    today = date.today().strftime('%Y/%m/%d')
       
    if len(planet) == 1:
        if 'Mars' in planet:
            planet_today = ephem.Mars(today)    
            const = ephem.constellation(planet_today)                       
        elif 'Mercury' in planet:
            planet_today = ephem.Mercury(today)    
            const = ephem.constellation(planet_today)            
        elif 'Saturn' in planet:
            planet_today = ephem.Saturn(today)    
            const = ephem.constellation(planet_today)           
        elif "Venus" in planet:
            planet_today = ephem.Venus(today)    
            const = ephem.constellation(planet_today)            
        elif 'Uranus' in planet:
            planet_today = ephem.Uranus(today)    
            const = ephem.constellation(planet_today)                    
        elif 'Jupiter'in planet:
            planet_today = ephem.Jupiter(today)    
            const = ephem.constellation(planet_today)            
        elif 'Sun' in planet:
            planet_today = ephem.Sun(today)    
            const = ephem.constellation(planet_today)            
        elif 'Neptune' in planet:
            planet_today = ephem.Neptune(today)    
            const = ephem.constellation(planet_today)            
        elif 'Pluto' in planet:
            planet_today = ephem.Pluto(today)    
            const = ephem.constellation(planet_today)            
        elif 'Moon' in planet:
            planet_today = ephem.Moon(today)    
            const = ephem.constellation(planet_today)
    elif len(planet) > 1:
        const ='Введите не больше 1 планеты'    
    else:
        const ='Вы не ввели название планеты, либо я не знаю таких планет'    
    text = const
        
    update.message.reply_text(text)
    logging.info(f'определено созвездие: {text}')  

def main():
    mybot = Updater("727575069:AAEbR3kPXvJNOMsCAV9E4TUCIZokCDPy-pc", request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user)) 
    dp.add_handler(CommandHandler("Planet",  get_planet_name))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
