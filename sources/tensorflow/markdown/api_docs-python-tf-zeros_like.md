[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/zeros_like#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/zeros_like)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/zeros_like?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/zeros_like#used-in-the-notebooks)
    
*   [Examples](https://www.tensorflow.org/api_docs/python/tf/zeros_like#examples)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/zeros_like#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/zeros_like#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.zeros\_like Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/zeros_like#used-in-the-notebooks)
    
*   [Examples](https://www.tensorflow.org/api_docs/python/tf/zeros_like#examples)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/zeros_like#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/zeros_like#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L2701-L2753)

Creates a tensor with all elements set to zero.

tf.zeros_like(
        input, dtype=None, name=None, layout=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Automatically rewrite TF 1.x and compat.v1 API symbols](https://www.tensorflow.org/guide/migrate/upgrade) | *   [CycleGAN](https://www.tensorflow.org/tutorials/generative/cyclegan)<br>    <br>*   [Deep Convolutional Generative Adversarial Network](https://www.tensorflow.org/tutorials/generative/dcgan)<br>    <br>*   [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream)<br>    <br>*   [pix2pix: Image-to-image translation with a conditional GAN](https://www.tensorflow.org/tutorials/generative/pix2pix)<br>    <br>*   [Integrated gradients](https://www.tensorflow.org/tutorials/interpretability/integrated_gradients) |

See also [`tf.zeros`](https://www.tensorflow.org/api_docs/python/tf/zeros)
.

Given a single tensor or array-like object (`input`), this operation returns a tensor of the same type and shape as `input` with all elements set to zero. Optionally, you can use `dtype` to specify a new type for the returned tensor.

Note that the layout of the input tensor is not preserved if the op is used inside tf.function. To obtain a tensor with the same layout as the input, chain the returned value to a [`dtensor.relayout_like`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/relayout_like)
.

|     |
| --- |
| Examples<br>-------- |     |
| >>> tensor = tf.constant([[1, 2, 3], [4, 5, 6]])<br>    >>> tf.zeros_like(tensor)<br>    <tf.Tensor: shape=(2, 3), dtype=int32, numpy=<br>    array([[0, 0, 0],<br>           [0, 0, 0]], dtype=int32)><br><br>    tf.zeros_like(tensor, dtype=tf.float32)<br><br>    tf.zeros_like([[1, 2, 3], [4, 5, 6]]) |     |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor` or array-like object. |
| `dtype` | A type for the returned `Tensor`. Must be `float16`, `float32`, `float64`, `int8`, `uint8`, `int16`, `uint16`, `int32`, `int64`, `complex64`, `complex128`, `bool` or `string` (optional). |
| `name` | A name for the operation (optional). |
| `layout` | Optional, [`tf.experimental.dtensor.Layout`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Layout)<br>. If provided, the result is a [DTensor](https://www.tensorflow.org/guide/dtensor_overview)<br> with the provided layout. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` with all elements set to zero. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.