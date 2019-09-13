"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
"""    
dict1 = {
    "Как дела": "Хорошо!",
    "Что делаешь?": "Программирую",
    "Что смотришь?": "Сериальчики",
    "Что читаешь?": "Хабр"
     }


def ask_user():
    while True:
        try:
            key = input('Спрашивай! ')
            if key in dict1:
                    print(dict1[key])
        except KeyboardInterrupt:
            print('Пока!')
            break   
            
                

if __name__ == "__main__":
    ask_user()
