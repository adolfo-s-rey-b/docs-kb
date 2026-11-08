[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linspace#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linspace)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linspace?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/linspace#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linspace#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linspace#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/linspace#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linspace Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/linspace#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linspace#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linspace#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/linspace#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L113-L230)

Generates evenly-spaced values in an interval along a given axis.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.lin_space`](https://www.tensorflow.org/api_docs/python/tf/linspace)
, [`tf.compat.v1.linspace`](https://www.tensorflow.org/api_docs/python/tf/linspace)

tf.linspace(
        start, stop, num, name=None, axis=0
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Multilayer perceptrons for digit recognition with Core APIs](https://www.tensorflow.org/guide/core/mlp_core)<br>    <br>*   [Advanced automatic differentiation](https://www.tensorflow.org/guide/advanced_autodiff)<br>    <br>*   [Introduction to gradients and automatic differentiation](https://www.tensorflow.org/guide/autodiff)<br>    <br>*   [Basic training loops](https://www.tensorflow.org/guide/basic_training_loops)<br>    <br>*   [TensorFlow basics](https://www.tensorflow.org/guide/basics) | *   [Integrated gradients](https://www.tensorflow.org/tutorials/interpretability/integrated_gradients)<br>    <br>*   [Learned data compression](https://www.tensorflow.org/tutorials/generative/data_compression)<br>    <br>*   [Basic regression: Predict fuel efficiency](https://www.tensorflow.org/tutorials/keras/regression)<br>    <br>*   [Scalable model compression](https://www.tensorflow.org/tutorials/optimization/compression)<br>    <br>*   [TFP Release Notes notebook (0.12.1)](https://www.tensorflow.org/probability/examples/TFP_Release_Notebook_0_12_1) |

A sequence of `num` evenly-spaced values are generated beginning at `start` along a given `axis`. If `num > 1`, the values in the sequence increase by `(stop - start) / (num - 1)`, so that the last one is exactly `stop`. If `num <= 0`, `ValueError` is raised.

Matches [np.linspace](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html)
's behaviour except when `num == 0`.

#### For example:

tf.linspace(10.0, 12.0, 3, name="linspace") => [ 10.0  11.0  12.0]

`Start` and `stop` can be tensors of arbitrary size:

    tf.linspace([0., 5.], [10., 40.], 5, axis=0)

`Axis` is where the values will be generated (the dimension in the returned tensor which corresponds to the axis will be equal to `num`)

    tf.linspace([0., 5.], [10., 40.], 5, axis=-1)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `start` | A `Tensor`. Must be one of the following types: `bfloat16`, `float32`, `float64`. N-D tensor. First entry in the range. |
| `stop` | A `Tensor`. Must have the same type and shape as `start`. N-D tensor. Last entry in the range. |
| `num` | A `Tensor`. Must be one of the following types: `int32`, `int64`. 0-D tensor. Number of values to generate. |
| `name` | A name for the operation (optional). |
| `axis` | Axis along which the operation is performed (can be specified to non-zero only when N-D tensors are provided). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `start`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `InvalidArgumentError` | If `axis` is specified to non-zero when 1-D tensor is provided. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.