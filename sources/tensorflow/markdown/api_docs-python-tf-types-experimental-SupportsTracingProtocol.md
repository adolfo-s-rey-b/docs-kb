[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/types/experimental/SupportsTracingProtocol#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/types/experimental/SupportsTracingProtocol)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/types/experimental/SupportsTracingProtocol?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ftypes%2Fexperimental%2FSupportsTracingProtocol&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/types/experimental/SupportsTracingProtocol#methods)
    *   [\_\_tf\_tracing\_type\_\_](https://www.tensorflow.org/api_docs/python/tf/types/experimental/SupportsTracingProtocol#__tf_tracing_type__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Was this helpful?

tf.types.experimental.SupportsTracingProtocol Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/types/experimental/SupportsTracingProtocol#methods)
    *   [\_\_tf\_tracing\_type\_\_](https://www.tensorflow.org/api_docs/python/tf/types/experimental/SupportsTracingProtocol#__tf_tracing_type__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/trace.py#L281-L302)

A protocol allowing custom classes to control tf.function retracing.

tf.types.experimental.SupportsTracingProtocol(
        *args, **kwargs
    )

Methods
-------

### `__tf_tracing_type__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/trace.py#L285-L302)

@abc.abstractmethod

Returns the tracing type of this object.

The tracing type is used to build the signature of a tf.function when traced, and to match arguments with existing signatures. When a Function object is called, tf.function looks at the tracing type of the call arguments. If an existing signature of matching type exists, it will be used. Otherwise, a new function is traced, and its signature will use the tracing type of the call arguments.

|     |     |
| --- | --- |
| Args |     |
| `context` | a context reserved for internal/future usage. |

|     |
| --- |
| Returns |     |
| The tracing type of this object. |     |

Was this helpful?

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.