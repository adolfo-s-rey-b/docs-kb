[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/argmax#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/argmax)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/argmax?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fmath%2Fargmax&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/argmax#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/argmax#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/argmax#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.argmax Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/argmax#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/argmax#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/argmax#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/math_ops.py#L271-L323)

Returns the index with the largest value across axes of a tensor.

#### View aliases

**Main aliases**

[`tf.argmax`](https://www.tensorflow.org/api_docs/python/tf/math/argmax)

tf.math.argmax(
        input,
        axis=None,
        output_type=tf.dtypes.int64,
        name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Multilayer perceptrons for digit recognition with Core APIs](https://www.tensorflow.org/guide/core/mlp_core)<br>    <br>*   [Migrate metrics and optimizers](https://www.tensorflow.org/guide/migrate/metrics_optimizers)<br>    <br>*   [Distributed training with Core APIs and DTensor](https://www.tensorflow.org/guide/core/distribution)<br>    <br>*   [Introduction to Tensors](https://www.tensorflow.org/guide/tensor)<br>    <br>*   [Introduction to Variables](https://www.tensorflow.org/guide/variable) | *   [Transfer learning with YAMNet for environmental sound classification](https://www.tensorflow.org/tutorials/audio/transfer_learning_audio)<br>    <br>*   [Transfer learning with TensorFlow Hub](https://www.tensorflow.org/tutorials/images/transfer_learning_with_hub)<br>    <br>*   [Custom training: walkthrough](https://www.tensorflow.org/tutorials/customization/custom_training_walkthrough)<br>    <br>*   [Simple audio recognition: Recognizing keywords](https://www.tensorflow.org/tutorials/audio/simple_audio)<br>    <br>*   [Distributed training with DTensors](https://www.tensorflow.org/tutorials/distribute/dtensor_ml_tutorial) |

In case of identity returns the smallest index.

#### For example:

    A = tf.constant([2, 20, 30, 3, 6])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. |
| `axis` | An integer, the axis to reduce across. Default to 0. |
| `output_type` | An optional output dtype ([`tf.int32`](https://www.tensorflow.org/api_docs/python/tf#int32)<br> or [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br>). Defaults to [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br>. |
| `name` | An optional name for the operation. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `output_type`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.