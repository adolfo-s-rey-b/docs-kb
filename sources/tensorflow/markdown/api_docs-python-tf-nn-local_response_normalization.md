[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/local_response_normalization#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/local_response_normalization)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/local_response_normalization?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/local_response_normalization#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/local_response_normalization#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.local\_response\_normalization Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/local_response_normalization#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/local_response_normalization#returns)
    

Local Response Normalization.

#### View aliases

**Main aliases**

[`tf.nn.lrn`](https://www.tensorflow.org/api_docs/python/tf/nn/local_response_normalization)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.local_response_normalization`](https://www.tensorflow.org/api_docs/python/tf/nn/local_response_normalization)
, [`tf.compat.v1.nn.lrn`](https://www.tensorflow.org/api_docs/python/tf/nn/local_response_normalization)

tf.nn.local_response_normalization(
        input: Annotated[Any, TV_LRN_T],
        depth_radius: int = 5,
        bias: float = 1,
        alpha: float = 1,
        beta: float = 0.5,
        name=None
    ) -> Annotated[Any, TV_LRN_T]

The 4-D `input` tensor is treated as a 3-D array of 1-D vectors (along the last dimension), and each vector is normalized independently. Within a given vector, each component is divided by the weighted, squared sum of inputs within `depth_radius`. In detail,

sqr_sum[a, b, c, d] =
        sum(input[a, b, c, d - depth_radius : d + depth_radius + 1] ** 2)
    output = input / (bias + alpha * sqr_sum) ** beta

For details, see [Krizhevsky et al., ImageNet classification with deep convolutional neural networks (NIPS 2012)](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Must be one of the following types: `half`, `bfloat16`, `float32`. 4-D. |
| `depth_radius` | An optional `int`. Defaults to `5`. 0-D. Half-width of the 1-D normalization window. |
| `bias` | An optional `float`. Defaults to `1`. An offset (usually positive to avoid dividing by 0). |
| `alpha` | An optional `float`. Defaults to `1`. A scale factor, usually positive. |
| `beta` | An optional `float`. Defaults to `0.5`. An exponent. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `input`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.