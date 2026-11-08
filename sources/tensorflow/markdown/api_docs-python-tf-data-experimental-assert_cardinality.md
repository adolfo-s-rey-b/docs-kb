[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/assert_cardinality#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/assert_cardinality)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/assert_cardinality?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/data/experimental/assert_cardinality#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/assert_cardinality#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/assert_cardinality#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/assert_cardinality#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.assert\_cardinality Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/data/experimental/assert_cardinality#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/assert_cardinality#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/assert_cardinality#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/assert_cardinality#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/cardinality.py#L67-L96)

Asserts the cardinality of the input dataset.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.assert_cardinality`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/assert_cardinality)

tf.data.experimental.assert_cardinality(
        expected_cardinality
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Fine tuning models for plant disease detection](https://www.tensorflow.org/hub/tutorials/cropnet_on_device) |

    dataset = tf.data.TFRecordDataset("examples.tfrecord")

|     |     |
| --- | --- |
| Args<br>---- |     |
| `expected_cardinality` | The expected cardinality of the input dataset. |

|     |
| --- |
| Returns<br>------- |     |
| A `Dataset` transformation function, which can be passed to [`tf.data.Dataset.apply`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#apply)<br>. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `FailedPreconditionError` | The assertion is checked at runtime (when iterating the dataset) and an error is raised if the actual and expected cardinality differ. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.