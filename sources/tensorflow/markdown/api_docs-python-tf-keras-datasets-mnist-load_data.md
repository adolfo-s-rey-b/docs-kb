[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/mnist/load_data#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/mnist/load_data)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/mnist/load_data?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/mnist/load_data#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/mnist/load_data#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/mnist/load_data#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.datasets.mnist.load\_data Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/mnist/load_data#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/mnist/load_data#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/mnist/load_data#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/datasets/mnist.py#L9-L71)

Loads the MNIST dataset.

tf.keras.datasets.mnist.load_data(
        path='mnist.npz'
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Import a JAX model using JAX2TF](https://www.tensorflow.org/guide/jax2tf)<br>    <br>*   [Mixed precision](https://www.tensorflow.org/guide/mixed_precision)<br>    <br>*   [Multi-GPU and distributed training](https://www.tensorflow.org/guide/keras/distributed_training)<br>    <br>*   [Weight clustering in Keras example](https://www.tensorflow.org/model_optimization/guide/clustering/clustering_example)<br>    <br>*   [Pruning in Keras example](https://www.tensorflow.org/model_optimization/guide/pruning/pruning_with_keras) | *   [Custom training loop with Keras and MultiWorkerMirroredStrategy](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_ctl)<br>    <br>*   [Multi-worker training with Keras](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras)<br>    <br>*   [Convolutional Variational Autoencoder](https://www.tensorflow.org/tutorials/generative/cvae)<br>    <br>*   [Deep Convolutional Generative Adversarial Network](https://www.tensorflow.org/tutorials/generative/dcgan)<br>    <br>*   [Save and load models](https://www.tensorflow.org/tutorials/keras/save_and_load) |

This is a dataset of 60,000 28x28 grayscale images of the 10 digits, along with a test set of 10,000 images. More info can be found at the [MNIST homepage](http://yann.lecun.com/exdb/mnist/)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `path` | path where to cache the dataset locally (relative to `~/.keras/datasets`). |

|     |
| --- |
| Returns<br>------- |     |
| Tuple of NumPy arrays: `(x_train, y_train), (x_test, y_test)`. |     |

**`x_train`**: `uint8` NumPy array of grayscale image data with shapes `(60000, 28, 28)`, containing the training data. Pixel values range from 0 to 255.

**`y_train`**: `uint8` NumPy array of digit labels (integers in range 0-9) with shape `(60000,)` for the training data.

**`x_test`**: `uint8` NumPy array of grayscale image data with shapes `(10000, 28, 28)`, containing the test data. Pixel values range from 0 to 255.

**`y_test`**: `uint8` NumPy array of digit labels (integers in range 0-9) with shape `(10000,)` for the test data.

#### Example:

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    assert x_train.shape == (60000, 28, 28)
    assert x_test.shape == (10000, 28, 28)
    assert y_train.shape == (60000,)
    assert y_test.shape == (10000,)

#### License:

Yann LeCun and Corinna Cortes hold the copyright of MNIST dataset, which is a derivative work from original NIST datasets. MNIST dataset is made available under the terms of the [Creative Commons Attribution-Share Alike 3.0 license.](https://creativecommons.org/licenses/by-sa/3.0/)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.