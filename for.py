"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

dict1 = {'school_class': '4a', 'scores': [3,5,4,5,2]}
dict2 = {'school_class': '2Б', 'scores': [2,1,4,5,5]}
dict3 = {'school_class': '2В', 'scores': [3,2,2,4,4]}
dict4 = {'school_class': '3Б', 'scores': [5,5,4,5,5]}
list_of_dicts = [dict1, dict2, dict3, dict4]

def school_avg_score():
    sum_score = 0
    count_pupils = 0
    for item in list_of_dicts:
        sum_score += sum(item['scores'])
        count_pupils += len(item['scores'])
    avg_score = sum_score/count_pupils
    print(f'средний балл по школе: {avg_score }')

def class_avg_score():
    for item in list_of_dicts:
        print(item['school_class'] + ' ' + str(sum(item['scores']) / len(item['scores'])))

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school_avg_score()
    class_avg_score()
    
if __name__ == "__main__":
    main()
