None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Data loading](https://keras.io/api/data_loading/)
 [Tree API](https://keras.io/api/tree/)
 [Built-in small datasets](https://keras.io/api/datasets/)
 [MNIST digits classification dataset](https://keras.io/api/datasets/mnist/)
 [CIFAR10 small images classification dataset](https://keras.io/api/datasets/cifar10/)
 [CIFAR100 small images classification dataset](https://keras.io/api/datasets/cifar100/)
 [IMDB movie review sentiment classification dataset](https://keras.io/api/datasets/imdb/)
 [Reuters newswire classification dataset](https://keras.io/api/datasets/reuters/)
 [Fashion MNIST dataset, an alternative to MNIST](https://keras.io/api/datasets/fashion_mnist/)
 [California Housing price regression dataset](https://keras.io/api/datasets/california_housing/)
 [Boston Housing price regression dataset](https://keras.io/api/datasets/boston_housing/)
 [Keras Applications](https://keras.io/api/applications/)
 [Mixed precision](https://keras.io/api/mixed_precision/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Built-in small datasets](https://keras.io/api/datasets/)
 / CIFAR10 small images classification dataset

CIFAR10 small images classification dataset
===========================================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/datasets/cifar10.py#L13)

### `load_data` function

Copied!

`keras.datasets.cifar10.load_data()`

Loads the CIFAR10 dataset.

This is a dataset of 50,000 32x32 color training images and 10,000 test images, labeled over 10 categories. See more info at the [CIFAR homepage](https://www.cs.toronto.edu/~kriz/cifar.html)
.

The classes are:

| Label | Description |
| --- | --- |
| 0   | airplane |
| 1   | automobile |
| 2   | bird |
| 3   | cat |
| 4   | deer |
| 5   | dog |
| 6   | frog |
| 7   | horse |
| 8   | ship |
| 9   | truck |

**Returns**

*   **Tuple of NumPy arrays**: `(x_train, y_train), (x_test, y_test)`.

**`x_train`**: `uint8` NumPy array of grayscale image data with shapes `(50000, 32, 32, 3)`, containing the training data. Pixel values range from 0 to 255.

**`y_train`**: `uint8` NumPy array of labels (integers in range 0-9) with shape `(50000, 1)` for the training data.

**`x_test`**: `uint8` NumPy array of grayscale image data with shapes `(10000, 32, 32, 3)`, containing the test data. Pixel values range from 0 to 255.

**`y_test`**: `uint8` NumPy array of labels (integers in range 0-9) with shape `(10000, 1)` for the test data.

**Example**

Copied!

`(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data() assert x_train.shape == (50000, 32, 32, 3) assert x_test.shape == (10000, 32, 32, 3) assert y_train.shape == (50000, 1) assert y_test.shape == (10000, 1)`

**Note**: The CIFAR-10 dataset is known to have a small percentage of mislabeled samples, which is inherent to the original dataset. This label noise may impact training and evaluation. For more details, refer to discussions in the research literature on CIFAR-10 label quality.

* * *

[CIFAR10 small images classification dataset](https://keras.io/api/datasets/cifar10/#cifar10-small-images-classification-dataset)

[`load_data` function](https://keras.io/api/datasets/cifar10/#loaddata-function)