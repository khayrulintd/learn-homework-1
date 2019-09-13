"""
Перепишите функцию discounted(price, discount, max_discount=20)из урока 
про функции так, чтобы она перехватывала исключения, когда переданы 
некорректные аргументы (например, строки вместо чисел).
    
"""

product = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 30000, 'discount': 10}
price = product['price']
discount = product['discount']


def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            print('скидка больше максимальной')
            return price
            
        else:
            return price - (price * discount / 100)
            print(price - (price * discount / 100))                  

    except (ValueError, TypeError):
        print('Введены некорректные значения цены или скидки')

     
    
if __name__ == "__main__":
    print(discounted(product['price'], product['discount']))
    