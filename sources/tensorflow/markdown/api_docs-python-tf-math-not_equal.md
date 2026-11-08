[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/not_equal#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/not_equal)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/not_equal?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/not_equal#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/not_equal#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/not_equal#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/math/not_equal#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.not\_equal Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/not_equal#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/not_equal#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/not_equal#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/math/not_equal#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L1897-L1931)

Returns the truth value of (x != y) element-wise.

#### View aliases

**Main aliases**

[`tf.not_equal`](https://www.tensorflow.org/api_docs/python/tf/math/not_equal)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.math.not_equal`](https://www.tensorflow.org/api_docs/python/tf/math/not_equal)
, [`tf.compat.v1.not_equal`](https://www.tensorflow.org/api_docs/python/tf/math/not_equal)

tf.math.not_equal(
        x, y, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)<br>    <br>*   [Understanding masking & padding](https://www.tensorflow.org/guide/keras/understanding_masking_and_padding)<br>    <br>*   [Unicode strings](https://www.tensorflow.org/text/guide/unicode) | *   [Tutorial on Multi Armed Bandits in TF-Agents](https://www.tensorflow.org/agents/tutorials/bandits_tutorial) |

Performs a [broadcast](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
 with the arguments and then an element-wise inequality comparison, returning a Tensor of boolean values.

#### For example:

    x = tf.constant([2, 4])

    x = tf.constant([2, 4])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. |
| `y` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of type bool with the same size as that of x or y. |     |

|     |
| --- |
| Raises<br>------ |     |
| [`tf.errors.InvalidArgumentError`](https://www.tensorflow.org/api_docs/python/tf/errors/InvalidArgumentError)<br>: If shapes of arguments are incompatible |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.