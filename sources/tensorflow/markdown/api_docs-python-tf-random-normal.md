[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/random/normal#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/random/normal)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/random/normal?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/random/normal#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/normal#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/normal#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.random.normal Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/random/normal#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/random/normal#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/random/normal#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/random_ops.py#L39-L95)

Outputs random values from a normal distribution.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.normal`](https://www.tensorflow.org/api_docs/python/tf/random/normal)
, [`tf.compat.v1.random_normal`](https://www.tensorflow.org/api_docs/python/tf/random/normal)

tf.random.normal(
        shape,
        mean=0.0,
        stddev=1.0,
        dtype=tf.dtypes.float32,
        seed=None,
        name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Use TF1.x models in TF2 workflows](https://www.tensorflow.org/guide/migrate/model_mapping)<br>    <br>*   [Advanced automatic differentiation](https://www.tensorflow.org/guide/advanced_autodiff)<br>    <br>*   [Introduction to modules, layers, and models](https://www.tensorflow.org/guide/intro_to_modules)<br>    <br>*   [Introduction to gradients and automatic differentiation](https://www.tensorflow.org/guide/autodiff)<br>    <br>*   [Basic training loops](https://www.tensorflow.org/guide/basic_training_loops) | *   [Convolutional Variational Autoencoder](https://www.tensorflow.org/tutorials/generative/cvae)<br>    <br>*   [Deep Convolutional Generative Adversarial Network](https://www.tensorflow.org/tutorials/generative/dcgan)<br>    <br>*   [Intro to Autoencoders](https://www.tensorflow.org/tutorials/generative/autoencoder)<br>    <br>*   [Uncertainty-aware Deep Learning with SNGP](https://www.tensorflow.org/tutorials/understanding/sngp)<br>    <br>*   [Transfer learning for video classification with MoViNet](https://www.tensorflow.org/tutorials/video/transfer_learning_with_movinet) |

Example that generates a new set of random values every time:

    tf.random.set_seed(5);

Example that outputs a reproducible result:

    tf.random.set_seed(5);

In this case, we are setting both the global and operation-level seed to ensure this result is reproducible. See [`tf.random.set_seed`](https://www.tensorflow.org/api_docs/python/tf/random/set_seed)
 for more information.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `shape` | A 1-D integer Tensor or Python array. The shape of the output tensor. |
| `mean` | A Tensor or Python value of type `dtype`, broadcastable with `stddev`. The mean of the normal distribution. |
| `stddev` | A Tensor or Python value of type `dtype`, broadcastable with `mean`. The standard deviation of the normal distribution. |
| `dtype` | The float type of the output: `float16`, `bfloat16`, `float32`, `float64`. Defaults to `float32`. |
| `seed` | A Python integer. Used to create a random seed for the distribution. See [`tf.random.set_seed`](https://www.tensorflow.org/api_docs/python/tf/random/set_seed)<br> for behavior. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A tensor of the specified shape filled with random normal values. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.