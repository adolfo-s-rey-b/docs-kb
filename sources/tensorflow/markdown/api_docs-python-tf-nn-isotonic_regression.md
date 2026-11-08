[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/isotonic_regression#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.isotonic\_regression Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_ops.py#L6622-L6694)

Solves isotonic regression problems along the given axis.

tf.nn.isotonic_regression(
        inputs, decreasing=True, axis=-1
    )

For each vector x, the problem solved is

\\\[\\argmin\_{y\_1 >= y\_2 >= ... >= y\_n} \\sum\_i (x\_i - y\_i)^2.\\\]

As the solution is component-wise constant, a second tensor is returned that encodes the segments. The problems are solved over the given axis.

Consider the following example, where we solve a batch of two problems. The first input is \[3, 1, 2\], while the second [1, 3, 4](https://www.tensorflow.org/api_docs/python/tf/nn/as%20the%20axis%20is%201)
.

>>> x = tf.constant([[3, 1, 2], [1, 3, 4]], dtype=tf.float32)
    >>> y, segments = tf.nn.isotonic_regression(x, axis=1)
    >>> y  # The solution.
    <tf.Tensor: shape=(2, 3), dtype=float32, numpy=
    array([[3.       , 1.5      , 1.5      ],\
           [2.6666667, 2.6666667, 2.6666667]], dtype=float32)>

Note that the first solution has two blocks \[2\] and \[1.5, 1.5\]. The second solution is constant, and thus has a single segment. These segments are exactly what the second returned tensor encodes:

    segments

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | A tensor holding the inputs. |
| `decreasing` | If set to False, the inequalities in the optimizing constrained are flipped. |
| `axis` | The axis along which the problems should be solved. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `output` | The solutions, same shape as type as the input. |
| `segments` | An int32 tensor, same shape as the input indicating the segments that have the same value. Specifically, those positions that have the same value correspond to the same segment. These values start at zero, and are monotonously increasing for each solution. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.