[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/equal#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/equal)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/equal?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/equal#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/equal#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/equal#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/math/equal#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.equal Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/equal#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/equal#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/equal#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/math/equal#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L1860-L1894)

Returns the truth value of (x == y) element-wise.

#### View aliases

**Main aliases**

[`tf.equal`](https://www.tensorflow.org/api_docs/python/tf/math/equal)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.equal`](https://www.tensorflow.org/api_docs/python/tf/math/equal)
, [`tf.compat.v1.math.equal`](https://www.tensorflow.org/api_docs/python/tf/math/equal)

tf.math.equal(
        x, y, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Multilayer perceptrons for digit recognition with Core APIs](https://www.tensorflow.org/guide/core/mlp_core)<br>    <br>*   [Distributed training with Core APIs and DTensor](https://www.tensorflow.org/guide/core/distribution)<br>    <br>*   [Extension types](https://www.tensorflow.org/guide/extension_type)<br>    <br>*   [MinDiff Data Preparation](https://www.tensorflow.org/responsible_ai/model_remediation/min_diff/guide/min_diff_data_preparation) | *   [Tutorial on Multi Armed Bandits in TF-Agents](https://www.tensorflow.org/agents/tutorials/bandits_tutorial)<br>    <br>*   [Classify Flowers with Transfer Learning](https://www.tensorflow.org/hub/tutorials/image_feature_vector)<br>    <br>*   [Federated Learning for Image Classification](https://www.tensorflow.org/federated/tutorials/federated_learning_for_image_classification)<br>    <br>*   [Sending Different Data To Particular Clients With federated\_language.federated\_select](https://www.tensorflow.org/federated/tutorials/federated_select)<br>    <br>*   [End to end example for BigQuery TensorFlow reader](https://www.tensorflow.org/io/tutorials/bigquery) |

Performs a [broadcast](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
 with the arguments and then an element-wise equality comparison, returning a Tensor of boolean values.

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