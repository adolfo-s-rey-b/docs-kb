[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/sigmoid#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/sigmoid)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/sigmoid?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/sigmoid#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/sigmoid#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/sigmoid#returns)
    
*   [scipy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/sigmoid#scipy-compatibility)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.sigmoid Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/sigmoid#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/sigmoid#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/sigmoid#returns)
    
*   [scipy compatibility](https://www.tensorflow.org/api_docs/python/tf/math/sigmoid#scipy-compatibility)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L4150-L4200)

Computes sigmoid of `x` element-wise.

#### View aliases

**Main aliases**

[`tf.nn.sigmoid`](https://www.tensorflow.org/api_docs/python/tf/math/sigmoid)
, [`tf.sigmoid`](https://www.tensorflow.org/api_docs/python/tf/math/sigmoid)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sigmoid`](https://www.tensorflow.org/api_docs/python/tf/math/sigmoid)

tf.math.sigmoid(
        x, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Logistic regression for binary classification with Core APIs](https://www.tensorflow.org/guide/core/logistic_regression_core)<br>    <br>*   [Advanced automatic differentiation](https://www.tensorflow.org/guide/advanced_autodiff)<br>    <br>*   [Introduction to gradients and automatic differentiation](https://www.tensorflow.org/guide/autodiff) | *   [Convolutional Variational Autoencoder](https://www.tensorflow.org/tutorials/generative/cvae)<br>    <br>*   [Classify structured data using Keras preprocessing layers](https://www.tensorflow.org/tutorials/structured_data/preprocessing_layers)<br>    <br>*   [Classify text with BERT](https://www.tensorflow.org/text/tutorials/classify_text_with_bert)<br>    <br>*   [Shape Constraints for Ethics with Tensorflow Lattice](https://www.tensorflow.org/lattice/tutorials/shape_constraints_for_ethics)<br>    <br>*   [Shape Constraints with Tensorflow Lattice](https://www.tensorflow.org/lattice/tutorials/shape_constraints) |

Formula for calculating sigmoid(x)\=y\=1/(1+exp(−x)).

For x∈(−∞,∞), sigmoid(x)∈(0,1).

#### Example Usage:

If a positive number is large, then its sigmoid will approach to 1 since the formula will be `y = <large_num> / (1 + <large_num>)`

    x = tf.constant([0.0, 1.0, 50.0, 100.0])

If a negative number is large, its sigmoid will approach to 0 since the formula will be `y = 1 / (1 + <large_num>)`

    x = tf.constant([-100.0, -50.0, -1.0, 0.0])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A Tensor with type `float16`, `float32`, `float64`, `complex64`, or `complex128`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A Tensor with the same type as `x`. |     |

#### Usage Example:

    x = tf.constant([-128.0, 0.0, 128.0], dtype=tf.float32)

scipy compatibility
-------------------

Equivalent to scipy.special.expit

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.