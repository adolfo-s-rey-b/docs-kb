[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/get_static_value#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/get_static_value)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/get_static_value?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fget_static_value&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/get_static_value#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/get_static_value#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/get_static_value#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/get_static_value#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.get\_static\_value Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/get_static_value#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/get_static_value#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/get_static_value#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/get_static_value#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/tensor_util.py#L1024-L1099)

Returns the constant value of the given tensor, if efficiently calculable.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.get_static_value`](https://www.tensorflow.org/api_docs/python/tf/get_static_value)

tf.get_static_value(
        tensor, partial=False
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Bayesian Modeling with Joint Distribution](https://www.tensorflow.org/probability/examples/Modeling_with_JointDistribution) |

This function attempts to partially evaluate the given tensor, and returns its value as a numpy ndarray if this succeeds.

#### Example usage:

    a = tf.constant(10)

    # `tf.Variable` is not supported.

Using `partial` option is most relevant when calling `get_static_value` inside a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. Setting it to `True` will return the results but for the values that cannot be evaluated will be `None`. For example:

class Foo:
      def __init__(self):
        self.a = tf.Variable(1)
        self.b = tf.constant(2)
    
      @tf.function
      def bar(self, partial):
        packed = tf.raw_ops.Pack(values=[self.a, self.b])
        static_val = tf.get_static_value(packed, partial=partial)
        tf.print(static_val)
    
    f = Foo()
    f.bar(partial=True)  # `array([None, array(2, dtype=int32)], dtype=object)`
    f.bar(partial=False)  # `None`

Compatibility(V1): If `constant_value(tensor)` returns a non-`None` result, it will no longer be possible to feed a different value for `tensor`. This allows the result of this function to influence the graph that is constructed, and permits static shape optimizations.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `tensor` | The Tensor to be evaluated. |
| `partial` | If True, the returned numpy array is allowed to have partially evaluated values. Values that can't be evaluated will be None. |

|     |
| --- |
| Returns<br>------- |     |
| A numpy ndarray containing the constant value of the given `tensor`, or None if it cannot be calculated. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | if tensor is not an tensor.Tensor. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.