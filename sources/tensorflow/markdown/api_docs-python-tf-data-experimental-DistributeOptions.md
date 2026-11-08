[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DistributeOptions#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DistributeOptions)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DistributeOptions?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdata%2Fexperimental%2FDistributeOptions&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DistributeOptions#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DistributeOptions#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DistributeOptions#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DistributeOptions#__ne__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.DistributeOptions Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DistributeOptions#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DistributeOptions#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DistributeOptions#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DistributeOptions#__ne__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/options.py#L292-L331)

Represents options for distributed data processing.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.DistributeOptions`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DistributeOptions)

tf.data.experimental.DistributeOptions()

You can set the distribution options of a dataset through the `experimental_distribute` property of [`tf.data.Options`](https://www.tensorflow.org/api_docs/python/tf/data/Options)
; the property is an instance of [`tf.data.experimental.DistributeOptions`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/DistributeOptions)
.

options = tf.data.Options()
    options.experimental_distribute.auto_shard_policy = tf.data.experimental.AutoShardPolicy.OFF
    dataset = dataset.with_options(options)

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `auto_shard_policy` | The type of sharding to use. See [`tf.data.experimental.AutoShardPolicy`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy)<br> for additional information. |
| `num_devices` | The number of devices attached to this input pipeline. This will be automatically set by `MultiDeviceIterator`. |

Methods
-------

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/util/options.py#L38-L44)

__eq__(
        other
    )

Return self==value.

### `__ne__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/util/options.py#L46-L50)

__ne__(
        other
    )

Return self!=value.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.