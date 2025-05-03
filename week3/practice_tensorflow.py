import tensorflow as tf
import matplotlib.pyplot as plt

# 加载 CIFAR-10 数据集
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

# 类别标签
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# 显示第0张图片
plt.figure(figsize=(1.5, 1.5), dpi=100)  # 小图 + 高DPI
plt.imshow(x_train[0])
plt.title(class_names[y_train[0][0]])
plt.axis('off')
plt.tight_layout()
plt.show()