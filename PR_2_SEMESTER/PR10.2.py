import os
import time
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans

# Путь к исходному изображению
input_path = "PR_2_SEMESTER\image.jpg"

# Папка для сохранения сжатых изображений
output_folder = "K-means Compressor"

# Список возможных значений количества цветов (k)
k_values = [2, 3, 4, 8, 16, 32, 64, 128, 256]

# Словарь для хранения результатов
results = {}

# Загрузка исходного изображения
original_image = Image.open(input_path)
image_array = np.array(original_image)

# Проход по каждому значению k
for k in k_values:
    # Создание экземпляра KMeans с количеством кластеров равным k
    kmeans = KMeans(n_clusters=k)

    # Замер времени выполнения сжатия
    start_time = time.time()

    # Преобразование изображения в массив пикселей
    pixels = image_array.reshape(-1, 3)

    # Применение алгоритма K-means
    kmeans.fit(pixels)

    # Получение центров кластеров
    colors = kmeans.cluster_centers_

    # Замена пикселей на центры кластеров
    compressed_pixels = colors[kmeans.labels_]

    # Восстановление изображения
    compressed_image_array = compressed_pixels.reshape(image_array.shape)

    # Сохранение сжатого изображения
    output_path = os.path.join(output_folder, f"compressed_{k}.jpg")
    compressed_image = Image.fromarray(compressed_image_array.astype(np.uint8))
    compressed_image.save(output_path)

    # Вычисление информационного объема сжатого изображения
    compressed_size = os.path.getsize(output_path)

    # Замер времени выполнения сжатия
    end_time = time.time()
    runtime = end_time - start_time

    # Сохранение результатов в словарь
    results[k] = (compressed_size, runtime)

# Вывод результатов для заполнения таблицы
print("Количество цветов\tИнформационный объем (K-means)\tВремя выполнения (K-means)")
for k, (compressed_size, runtime) in results.items():
    print(f"{k}\t\t\t{compressed_size}\t\t\t{runtime}")
