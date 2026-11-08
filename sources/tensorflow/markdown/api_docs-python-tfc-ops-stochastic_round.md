[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/ops/stochastic_round#main-content)

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
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.ops.stochastic\_round Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

Rounds `inputs / step_size` stochastically.

#### View aliases

**Main aliases**

[`tfc.stochastic_round`](https://www.tensorflow.org/api_docs/python/tfc/ops/stochastic_round)

tfc.ops.stochastic_round(
        inputs, step_size, seed, name=None
    )

This op computes the elementwise function:

output = { floor(x) with prob. p = x - floor(x) floor(x) + 1 with prob. 1 - p } where x = input / step\_size.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`. Floating point tensor to be rounded. |
| `step_size` | A `Tensor` of type `float32`. Scalar tensor. Step size for rounding. |
| `seed` | A `Tensor` of type `int32`. Arbitrary shape tensor. Seed for random number generator. If it has no elements, seeding is attempted from system time. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `int32`. Integer tensor of same shape as `inputs`, containing rounded values. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.