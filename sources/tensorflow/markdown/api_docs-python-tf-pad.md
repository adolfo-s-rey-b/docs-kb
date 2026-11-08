[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/pad#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/pad)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/pad?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fpad&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/pad#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/pad#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/pad#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/pad#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.pad Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/pad#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/pad#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/pad#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/pad#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L3197-L3253)

Pads a tensor.

tf.pad(
        tensor, paddings, mode='CONSTANT', constant_values=0, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Advanced automatic differentiation](https://www.tensorflow.org/guide/advanced_autodiff) | *   [A Tour of TensorFlow Probability](https://www.tensorflow.org/probability/examples/A_Tour_of_TensorFlow_Probability)<br>    <br>*   [Multiple changepoint detection and Bayesian model selection](https://www.tensorflow.org/probability/examples/Multiple_changepoint_detection_and_Bayesian_model_selection)<br>    <br>*   [Graph-based Neural Structured Learning in TFX](https://www.tensorflow.org/tfx/tutorials/tfx/neural_structured_learning) |

This operation pads a `tensor` according to the `paddings` you specify. `paddings` is an integer tensor with shape `[n, 2]`, where n is the rank of `tensor`. For each dimension D of `input`, `paddings[D, 0]` indicates how many values to add before the contents of `tensor` in that dimension, and `paddings[D, 1]` indicates how many values to add after the contents of `tensor` in that dimension. If `mode` is "REFLECT" then both `paddings[D, 0]` and `paddings[D, 1]` must be no greater than `tensor.dim_size(D) - 1`. If `mode` is "SYMMETRIC" then both `paddings[D, 0]` and `paddings[D, 1]` must be no greater than `tensor.dim_size(D)`.

The padded size of each dimension D of the output is:

`paddings[D, 0] + tensor.dim_size(D) + paddings[D, 1]`

#### For example:

t = tf.constant([[1, 2, 3], [4, 5, 6]])
    paddings = tf.constant([[1, 1,], [2, 2]])
    # 'constant_values' is 0.
    # rank of 't' is 2.
    tf.pad(t, paddings, "CONSTANT")  # [[0, 0, 0, 0, 0, 0, 0],\
                                     #  [0, 0, 1, 2, 3, 0, 0],\
                                     #  [0, 0, 4, 5, 6, 0, 0],\
                                     #  [0, 0, 0, 0, 0, 0, 0]]
    
    tf.pad(t, paddings, "REFLECT")  # [[6, 5, 4, 5, 6, 5, 4],\
                                    #  [3, 2, 1, 2, 3, 2, 1],\
                                    #  [6, 5, 4, 5, 6, 5, 4],\
                                    #  [3, 2, 1, 2, 3, 2, 1]]
    
    tf.pad(t, paddings, "SYMMETRIC")  # [[2, 1, 1, 2, 3, 3, 2],\
                                      #  [2, 1, 1, 2, 3, 3, 2],\
                                      #  [5, 4, 4, 5, 6, 6, 5],\
                                      #  [5, 4, 4, 5, 6, 6, 5]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor` | A `Tensor`. |
| `paddings` | A `Tensor` of type `int32`. |
| `mode` | One of "CONSTANT", "REFLECT", or "SYMMETRIC" (case-insensitive) |
| `constant_values` | In "CONSTANT" mode, the scalar pad value to use. Must be same type as `tensor`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `tensor`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | When mode is not one of "CONSTANT", "REFLECT", or "SYMMETRIC". |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.