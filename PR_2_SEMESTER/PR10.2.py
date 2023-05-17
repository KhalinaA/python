import os
import time
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image

# Определение пути к исходному изображению
input_path = "input_image.jpg"

# Определение пути к папке для сохранения сжатых изображений
output_dir = "K-means Compressor"
os.makedirs(output_dir, exist_ok=True)

# Определение возможных значений количества итераций
max_iter_values = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Загрузка исходного изображения
image = np.array(Image.open(input_path))

# Подбор оптимального количества итераций
best_iter = None
best_time = float("inf")
best_quality = float("inf")
for max_iter in max_iter_values:
    # Сжатие изображения методом K-means
    start_time = time.time()
    kmeans = KMeans(n_clusters=16, max_iter=max_iter, n_init=1).fit(image.reshape(-1, 3))
    compressed_image = kmeans.cluster_centers_[kmeans.labels_].reshape(image.shape).astype("uint8")
    end_time = time.time()
    
    # Вычисление времени выполнения и качества сжатия
    execution_time = end_time - start_time
    mse = np.mean((image - compressed_image) ** 2)
    quality = 10 * np.log10(255 ** 2 / mse)
    
    # Сохранение сжатого изображения
    output_path = os.path.join(output_dir, f"compressed_{max_iter}_iters.jpg")
    Image.fromarray(compressed_image).save(output_path)
    
    # Обновление лучшего значения
    if execution_time < best_time or (execution_time == best_time and quality < best_quality):
        best_iter = max_iter
        best_time = execution_time
        best_quality = quality

# Вывод результата подбора оптимального количества итераций
print(f"Best number of iterations: {best_iter}")
print(f"Execution time: {best_time:.3f} seconds")
print(f"Compression quality: {best_quality:.3f} dB")
