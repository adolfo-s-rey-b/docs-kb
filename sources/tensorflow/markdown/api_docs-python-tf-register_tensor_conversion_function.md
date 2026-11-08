[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/register_tensor_conversion_function#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/register_tensor_conversion_function)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/register_tensor_conversion_function?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/register_tensor_conversion_function#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/register_tensor_conversion_function#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.register\_tensor\_conversion\_function Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/register_tensor_conversion_function#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/register_tensor_conversion_function#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_conversion_registry.py#L80-L131)

Registers a function for converting objects of `base_type` to `Tensor`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.register_tensor_conversion_function`](https://www.tensorflow.org/api_docs/python/tf/register_tensor_conversion_function)

tf.register_tensor_conversion_function(
        base_type, conversion_func, priority=100
    )

The conversion function must have the following signature:

    def conversion_func(value, dtype=None, name=None, as_ref=False):
          # ...

It must return a `Tensor` with the given `dtype` if specified. If the conversion function creates a new `Tensor`, it should use the given `name` if specified. All exceptions will be propagated to the caller.

The conversion function may return `NotImplemented` for some inputs. In this case, the conversion process will continue to try subsequent conversion functions.

If `as_ref` is true, the function must return a `Tensor` reference, such as a `Variable`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `base_type` | The base type or tuple of base types for all objects that `conversion_func` accepts. |
| `conversion_func` | A function that converts instances of `base_type` to `Tensor`. |
| `priority` | Optional integer that indicates the priority for applying this conversion function. Conversion functions with smaller priority values run earlier than conversion functions with larger priority values. Defaults to 100. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If the arguments do not have the appropriate type. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.