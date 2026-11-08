[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/unregister_dispatch_for#main-content)

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
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.unregister\_dispatch\_for Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/util/dispatch.py#L553-L609)

Unregisters a function that was registered with `@dispatch_for_*`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.experimental.unregister_dispatch_for`](https://www.tensorflow.org/api_docs/python/tf/experimental/unregister_dispatch_for)

tf.experimental.unregister_dispatch_for(
        dispatch_target
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Extension types](https://www.tensorflow.org/guide/extension_type) |

This is primarily intended for testing purposes.

#### Example:

    # Define a type and register a dispatcher to override `tf.abs`:

    # Unregister the dispatcher, so `tf.abs` no longer calls `my_abs`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dispatch_target` | The function to unregister. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `dispatch_target` was not registered using `@dispatch_for`, `@dispatch_for_unary_elementwise_apis`, or `@dispatch_for_binary_elementwise_apis`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.