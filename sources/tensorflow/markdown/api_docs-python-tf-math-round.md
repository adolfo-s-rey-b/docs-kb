[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/round?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/round)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/round?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/round?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/round?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/round?version=stable#returns_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.round Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/round?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/round?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/round?version=stable#returns_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L942-L968)

Rounds the values of a tensor to the nearest integer, element-wise.

#### View aliases

**Main aliases**

[`tf.round`](https://www.tensorflow.org/api_docs/python/tf/math/round)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.round`](https://www.tensorflow.org/api_docs/python/tf/math/round)

tf.math.round(
        x, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Learned data compression](https://www.tensorflow.org/tutorials/generative/data_compression)<br>    <br>*   [Substantial Undocumented Infection Facilitates the Rapid Dissemination of Novel Coronavirus (SARS-CoV2)](https://www.tensorflow.org/probability/examples/Undocumented_Infection_and_the_Dissemination_of_SARS-CoV2)<br>    <br>*   [Research tools](https://www.tensorflow.org/quantum/tutorials/research_tools)<br>    <br>*   [Super resolution with TensorFlow Lite](https://www.tensorflow.org/lite/examples/super_resolution/overview)<br>    <br>*   [Graph-based Neural Structured Learning in TFX](https://www.tensorflow.org/tfx/tutorials/tfx/neural_structured_learning) |

Rounds half to even. Also known as bankers rounding. If you want to round according to the current system rounding mode use tf::cint. For example:

x = tf.constant([0.9, 2.5, 2.3, 1.5, -4.5])
    tf.round(x)  # [ 1.0, 2.0, 2.0, 2.0, -4.0 ]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor` of type `float16`, `float32`, `float64`, `int32`, or `int64`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of same shape and type as `x`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.