import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image

# Имя исходного изображения
image_name = 'image.jpg'

# Загружаем изображение и преобразуем в массив NumPy
image = np.array(Image.open(image_name))

# Создаем папку для сохранения сжатых изображений
if not os.path.exists('Scikit Compressor'):
    os.makedirs('Scikit Compressor')

# Задаем варианты количества цветов
n_colors = [2, 3, 4, 8, 16, 32, 64, 128, 256]

# Проходим по всем вариантам количества цветов
for n in n_colors:
    # Создаем объект KMeans с количеством кластеров, равным n
    kmeans = KMeans(n_clusters=n)
    
    # Преобразуем изображение в двумерный массив
    image_2d = image.reshape(-1, 3)
    
    # Обучаем модель KMeans
    kmeans.fit(image_2d)
    
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
    Image.fromarray(compressed_image).save(f'Scikit Compressor/image_{n}.jpg')
    
    # Выводим получившееся изображение на экран
    plt.imshow(compressed_image)
    plt.show()
