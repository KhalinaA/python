import re
import urllib.request

url = 'https://quke.ru/shop/smartfony/apple?page-size=72'

# получаем HTML-код страницы
html = urllib.request.urlopen(url).read().decode('utf-8')

# извлекаем название и цену смартфона с помощью регулярных выражений
phones = re.findall(r'\"name\": \"(.*)\"[\s\S]*?(?=\"price)\"price\": (\d+)', html)

# проверяем, что список phones не пустой
if phones:
    # выводим данные о самом дорогом и самом дешевом смартфоне, а также среднюю цену всех смартфонов
    prices = [float(phone[1].replace('.', '').replace(',', '.')) for phone in phones]
    max_price = max(prices)
    min_price = min(prices)
    avg_price = sum(prices) / len(prices)
    print(f'Самый дорогой смартфон: {phones[prices.index(max_price)][0]}, цена: {max_price:.2f} руб.')
    print(f'Самый дешевый смартфон: {phones[prices.index(min_price)][0]}, цена: {min_price:.2f} руб.')
    print(f'Средняя цена смартфонов: {avg_price:.2f} руб.')
    
    # записываем данные в файл
    with open('catalog.txt', 'w', encoding='utf-8') as file:
        for phone in phones:
            name = phone[0]
            price = phone[1]
            file.write(f'{name} | {price}\n')
else:
    print('На странице не найдено ни одного смартфона.')
