[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/convert_to_tensor#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/convert_to_tensor)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/convert_to_tensor?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fconvert_to_tensor&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/convert_to_tensor#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/convert_to_tensor#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/convert_to_tensor#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/convert_to_tensor#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.convert\_to\_tensor Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/convert_to_tensor#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/convert_to_tensor#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/convert_to_tensor#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/convert_to_tensor#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_conversion.py#L96-L163)

Converts the given `value` to a `Tensor`.

tf.convert_to_tensor(
        value, dtype=None, dtype_hint=None, name=None
    ) -> tf.Tensor

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Logistic regression for binary classification with Core APIs](https://www.tensorflow.org/guide/core/logistic_regression_core)<br>    <br>*   [Extension types](https://www.tensorflow.org/guide/extension_type)<br>    <br>*   [Matrix approximation with Core APIs](https://www.tensorflow.org/guide/core/matrix_core)<br>    <br>*   [TensorFlow basics](https://www.tensorflow.org/guide/basics)<br>    <br>*   [Distributed training with Core APIs and DTensor](https://www.tensorflow.org/guide/core/distribution) | *   [DeepDream](https://www.tensorflow.org/tutorials/generative/deepdream)<br>    <br>*   [Custom training: walkthrough](https://www.tensorflow.org/tutorials/customization/custom_training_walkthrough)<br>    <br>*   [Distributed training with DTensors](https://www.tensorflow.org/tutorials/distribute/dtensor_ml_tutorial)<br>    <br>*   [Load a pandas DataFrame](https://www.tensorflow.org/tutorials/load_data/pandas_dataframe)<br>    <br>*   [Scalable model compression](https://www.tensorflow.org/tutorials/optimization/compression) |

This function converts Python objects of various types to `Tensor` objects. It accepts `Tensor` objects, numpy arrays, Python lists, and Python scalars.

#### For example:

    import numpy as np

    # The following calls are equivalent.

This function can be useful when composing a new operation in Python (such as `my_func` in the example above). All standard Python op constructors apply this function to each of their Tensor-valued inputs, which allows those ops to accept numpy arrays, Python lists, and scalars in addition to `Tensor` objects.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | An object whose type has a registered `Tensor` conversion function. |
| `dtype` | Optional element type for the returned tensor. If missing, the type is inferred from the type of `value`. |
| `dtype_hint` | Optional element type for the returned tensor, used when dtype is None. In some cases, a caller may not have a dtype in mind when converting to a tensor, so dtype\_hint can be used as a soft preference. If the conversion to `dtype_hint` is not possible, this argument has no effect. |
| `name` | Optional name to use if a new `Tensor` is created. |

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