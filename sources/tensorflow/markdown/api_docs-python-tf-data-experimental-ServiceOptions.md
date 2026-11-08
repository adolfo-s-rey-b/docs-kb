[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ServiceOptions#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ServiceOptions)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ServiceOptions?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ServiceOptions#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ServiceOptions#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ServiceOptions#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ServiceOptions#__ne__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.ServiceOptions Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ServiceOptions#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ServiceOptions#methods)
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ServiceOptions#__eq__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ServiceOptions#__ne__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/options.py#L496-L531)

Represents options for tf.data service.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.ServiceOptions`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ServiceOptions)

tf.data.experimental.ServiceOptions()

You can set the service options of a dataset through the `experimental_service` property of [`tf.data.Options`](https://www.tensorflow.org/api_docs/python/tf/data/Options)
; the property is an instance of [`tf.data.experimental.ServiceOptions`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/ServiceOptions)
.

options = tf.data.Options()
    options.experimental_service.pinned = True
    dataset = dataset.with_options(options)

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `pinned` | If true, the tf.data service client allocates data to pinned memory, which facilitates more efficient copying from host memory to GPU memory downstream. For gRPC, compression must be disabled for this to take effect. For alternative data transfer protocols, this may or may not take effect, depending on the implementation. |

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