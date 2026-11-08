[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/convert_to_tensor#main-content)

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
    

tf.compat.v1.convert\_to\_tensor Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_conversion.py#L33-L93)

Converts the given `value` to a `Tensor`.

tf.compat.v1.convert_to_tensor(
        value, dtype=None, name=None, preferred_dtype=None, dtype_hint=None
    ) -> tf.Tensor

This function converts Python objects of various types to `Tensor` objects. It accepts `Tensor` objects, numpy arrays, Python lists, and Python scalars. For example:

import numpy as np
    
    def my_func(arg):
      arg = tf.convert_to_tensor(arg, dtype=tf.float32)
      return tf.matmul(arg, arg) + arg
    
    # The following calls are equivalent.
    value_1 = my_func(tf.constant([[1.0, 2.0], [3.0, 4.0]]))
    value_2 = my_func([[1.0, 2.0], [3.0, 4.0]])
    value_3 = my_func(np.array([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32))

This function can be useful when composing a new operation in Python (such as `my_func` in the example above). All standard Python op constructors apply this function to each of their Tensor-valued inputs, which allows those ops to accept numpy arrays, Python lists, and scalars in addition to `Tensor` objects.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | An object whose type has a registered `Tensor` conversion function. |
| `dtype` | Optional element type for the returned tensor. If missing, the type is inferred from the type of `value`. |
| `name` | Optional name to use if a new `Tensor` is created. |
| `preferred_dtype` | Optional element type for the returned tensor, used when dtype is None. In some cases, a caller may not have a dtype in mind when converting to a tensor, so preferred\_dtype can be used as a soft preference. If the conversion to `preferred_dtype` is not possible, this argument has no effect. |
| `dtype_hint` | same meaning as preferred\_dtype, and overrides it. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` based on `value`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If no conversion function is registered for `value` to `dtype`. |
| `RuntimeError` | If a registered conversion function returns an invalid value. |
| `ValueError` | If the `value` is a tensor not of given `dtype` in graph mode. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.