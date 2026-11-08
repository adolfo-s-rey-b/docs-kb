None

[Keras 3 API documentation](https://keras.io/api/)
 [Keras 2 API documentation](https://keras.io/2/api/)

[Models API](https://keras.io/2/api/models/)
 [Layers API](https://keras.io/2/api/layers/)
 [Callbacks API](https://keras.io/2/api/callbacks/)
 [Optimizers](https://keras.io/2/api/optimizers/)
 [Metrics](https://keras.io/2/api/metrics/)
 [Losses](https://keras.io/2/api/losses/)
 [Data loading](https://keras.io/2/api/data_loading/)
 [Built-in small datasets](https://keras.io/2/api/datasets/)
 [MNIST digits classification dataset](https://keras.io/2/api/datasets/mnist/)
 [CIFAR10 small images classification dataset](https://keras.io/2/api/datasets/cifar10/)
 [CIFAR100 small images classification dataset](https://keras.io/2/api/datasets/cifar100/)
 [IMDB movie review sentiment classification dataset](https://keras.io/2/api/datasets/imdb/)
 [Reuters newswire classification dataset](https://keras.io/2/api/datasets/reuters/)
 [Fashion MNIST dataset, an alternative to MNIST](https://keras.io/2/api/datasets/fashion_mnist/)
 [Boston Housing price regression dataset](https://keras.io/2/api/datasets/boston_housing/)
 [Keras Applications](https://keras.io/2/api/applications/)
 [Mixed precision](https://keras.io/2/api/mixed_precision/)
 [Utilities](https://keras.io/2/api/utils/)

► [Keras 2 API documentation](https://keras.io/2/api/)
 / [Built-in small datasets](https://keras.io/2/api/datasets/)
 / CIFAR100 small images classification dataset

CIFAR100 small images classification dataset
============================================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/datasets/cifar100.py#L29)

### `load_data` function

Copied!

`tf_keras.datasets.cifar100.load_data(label_mode="fine", cache_dir=None)`

Loads the CIFAR100 dataset.

This is a dataset of 50,000 32x32 color training images and 10,000 test images, labeled over 100 fine-grained classes that are grouped into 20 coarse-grained classes. See more info at the [CIFAR homepage](https://www.cs.toronto.edu/~kriz/cifar.html)
.

**Arguments**

*   **label\_mode**: one of "fine", "coarse". If it is "fine" the category labels are the fine-grained labels, if it is "coarse" the output labels are the coarse-grained superclasses.
*   **cache\_dir**: directory where to cache the dataset locally. When None, defaults to `~/.keras/datasets`.

**Returns**

*   **Tuple of NumPy arrays**: `(x_train, y_train), (x_test, y_test)`.

**x\_train**: uint8 NumPy array of image data with shapes `(50000, 32, 32, 3)`, containing the training data. Pixel values range from 0 to 255.

**y\_train**: uint8 NumPy array of labels (integers in range 0-99) with shape `(50000, 1)` for the training data.

**x\_test**: uint8 NumPy array of image data with shapes `(10000, 32, 32, 3)`, containing the test data. Pixel values range from 0 to 255.

**y\_test**: uint8 NumPy array of labels (integers in range 0-99) with shape `(10000, 1)` for the test data.

**Example**

Copied!

`(x_train, y_train), (x_test, y_test) = keras.datasets.cifar100.load_data() assert x_train.shape == (50000, 32, 32, 3) assert x_test.shape == (10000, 32, 32, 3) assert y_train.shape == (50000, 1) assert y_test.shape == (10000, 1)`

* * *

[CIFAR100 small images classification dataset](https://keras.io/2/api/datasets/cifar100/#cifar100-small-images-classification-dataset)

[`load_data` function](https://keras.io/2/api/datasets/cifar100/#loaddata-function)