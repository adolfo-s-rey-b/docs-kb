[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/BatchableExtensionType#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/BatchableExtensionType)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/BatchableExtensionType?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fexperimental%2FBatchableExtensionType&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/BatchableExtensionType#used-in-the-notebooks)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/experimental/BatchableExtensionType#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/BatchableExtensionType#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/BatchableExtensionType#__ne__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.BatchableExtensionType Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/experimental/BatchableExtensionType#used-in-the-notebooks)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/experimental/BatchableExtensionType#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/BatchableExtensionType#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/experimental/BatchableExtensionType#__ne__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/extension_type.py#L831-L857)

An ExtensionType that can be batched and unbatched.

Inherits From: [`ExtensionType`](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionType)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.experimental.BatchableExtensionType`](https://www.tensorflow.org/api_docs/python/tf/experimental/BatchableExtensionType)

tf.experimental.BatchableExtensionType(
        *args, **kwargs
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Extension types](https://www.tensorflow.org/guide/extension_type) |

`BatchableExtensionType`s can be used with APIs that require batching or unbatching, including `Keras`, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
, and [`tf.map_fn`](https://www.tensorflow.org/api_docs/python/tf/map_fn)
. E.g.:

    class Vehicle(tf.experimental.BatchableExtensionType):

An `ExtensionTypeBatchEncoder` is used by these APIs to encode `ExtensionType` values. The default encoder assumes that values can be stacked, unstacked, or concatenated by simply stacking, unstacking, or concatenating every nested `Tensor`, `ExtensionType`, `CompositeTensor`, or `TensorShape` field. Extension types where this is not the case will need to override `__batch_encoder__` with a custom `ExtensionTypeBatchEncoder`. See [`tf.experimental.ExtensionTypeBatchEncoder`](https://www.tensorflow.org/api_docs/python/tf/experimental/ExtensionTypeBatchEncoder)
 for more details.

Methods
-------

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/extension_type.py#L276-L305)

__eq__(
        other
    )

Return self==value.

### `__ne__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/extension_type.py#L307-L312)

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