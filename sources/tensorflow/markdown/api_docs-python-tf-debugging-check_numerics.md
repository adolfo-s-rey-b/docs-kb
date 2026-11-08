[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/debugging/check_numerics?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/debugging/check_numerics)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/debugging/check_numerics?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/debugging/check_numerics?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/check_numerics?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/debugging/check_numerics?version=stable#returns_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.debugging.check\_numerics Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/debugging/check_numerics?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/debugging/check_numerics?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/debugging/check_numerics?version=stable#returns_1)
    

See Stable See Nightly

Checks a tensor for NaN and Inf values.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.check_numerics`](https://www.tensorflow.org/api_docs/python/tf/debugging/check_numerics)

tf.debugging.check_numerics(
        tensor: Annotated[Any, TV_CheckNumerics_T], message: str, name=None
    ) -> Annotated[Any, TV_CheckNumerics_T]

### Used in the notebooks

| Used in the guide |
| --- |
| *   [TensorFlow graph optimization with Grappler](https://www.tensorflow.org/guide/graph_optimization) |

When run, reports an `InvalidArgument` error if `tensor` has any values that are not a number (NaN) or infinity (Inf). Otherwise, returns the input tensor.

#### Example usage:

a = tf.Variable(1.0)
    tf.debugging.check_numerics(a, message='')
    
    b = tf.Variable(np.nan)
    try:
      tf.debugging.check_numerics(b, message='Checking b')
    except Exception as e:
      assert "Checking b : Tensor had NaN values" in e.message
    
    c = tf.Variable(np.inf)
    try:
      tf.debugging.check_numerics(c, message='Checking c')
    except Exception as e:
      assert "Checking c : Tensor had Inf values" in e.message

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor` | A `Tensor`. Must be one of the following types: `bfloat16`, `half`, `float32`, `float64`. |
| `message` | A `string`. Prefix of the error message. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `tensor`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.