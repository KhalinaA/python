import os
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image

# Имя исходного изображения
image_name = 'PR_2_SEMESTER\image.jpg'

# Загружаем изображение и преобразуем в массив NumPy
image = np.array(Image.open(image_name))

# Создаем папку для сохранения сжатых изображений
if not os.path.exists('Scikit Compressor'):
    os.makedirs('Scikit Compressor')

# Задаем варианты количества цветов
n_colors = [2, 3, 4, 8, 16, 32, 64, 128, 256]

# Создаем списки для хранения результатов
information_sizes = []
execution_times = []

# Проходим по всем вариантам количества цветов
for n in n_colors:
    # Создаем объект KMeans с количеством кластеров, равным n
    kmeans = KMeans(n_clusters=n)
    
    # Преобразуем изображение в двумерный массив
    image_2d = image.reshape(-1, 3)
    
    # Обучаем модель KMeans
    start_time = time.time()  # Засекаем время начала выполнения
    kmeans.fit(image_2d)
    end_time = time.time()  # Засекаем время окончания выполнения
    execution_time = end_time - start_time
    
    # Получаем метки кластеров для каждого пикселя
    labels = kmeans.predict(image_2d)
    
    # Получаем цвета для каждого кластера
    colors = kmeans.cluster_centers_.astype(int)
    
    # Создаем новое изображение, используя цвета кластеров
    compressed_image = np.zeros_like(image_2d)
    for i in range(len(colors)):
        compressed_image[labels == i] = colors[i]
    compressed_image = compressed_image.reshape(image.shape)
    
    # Сохраняем получившееся изображение в отдельную папку
    save_path = f'Scikit Compressor/image_{n}.jpg'
    Image.fromarray(compressed_image).save(save_path)
    
    # Вычисляем информационный объем (размер файла) сжатого изображения
    information_size = os.path.getsize(save_path)
    
    # Добавляем информационный объем и время выполнения в списки результатов
    information_sizes.append(information_size)
    execution_times.append(execution_time)
    
    # Выводим получившееся изображение на экран
    plt.imshow(compressed_image)
    plt.show()

# Выводим результаты для заполнения таблицы
for i in range(len(n_colors)):
    print(f'{n_colors[i]:<6} {information_sizes[i]:<10} {execution_times[i]:<20}')
