[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/math/logical_and#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/math/logical_and)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/math/logical_and?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/logical_and#used-in-the-notebooks)
    
*   [Usage](https://www.tensorflow.org/api_docs/python/tf/math/logical_and#usage)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/logical_and#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/logical_and#returns)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/logical_and#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/logical_and#returns_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.math.logical\_and Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/math/logical_and#used-in-the-notebooks)
    
*   [Usage](https://www.tensorflow.org/api_docs/python/tf/math/logical_and#usage)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/logical_and#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/logical_and#returns)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/math/logical_and#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/math/logical_and#returns_1)
    

Returns the truth value of x AND y element-wise.

#### View aliases

**Main aliases**

[`tf.logical_and`](https://www.tensorflow.org/api_docs/python/tf/math/logical_and)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.logical_and`](https://www.tensorflow.org/api_docs/python/tf/math/logical_and)
, [`tf.compat.v1.math.logical_and`](https://www.tensorflow.org/api_docs/python/tf/math/logical_and)

tf.math.logical_and(
        x: Annotated[Any, tf.raw_ops.Any],
        y: Annotated[Any, tf.raw_ops.Any],
        name=None
    ) -> Annotated[Any, tf.raw_ops.Any]

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Tutorial on Multi Armed Bandits in TF-Agents](https://www.tensorflow.org/agents/tutorials/bandits_tutorial) |

Logical AND function.

Requires that `x` and `y` have the same shape or have [broadcast-compatible](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
 shapes. For example, `x` and `y` can be:

*   Two single elements of type `bool`.
*   One [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
     of type `bool` and one single `bool`, where the result will be calculated by applying logical AND with the single element to each element in the larger Tensor.
*   Two [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
     objects of type `bool` of the same shape. In this case, the result will be the element-wise logical AND of the two input tensors.

You can also use the `&` operator instead.

|     |
| --- |
| Usage<br>----- |     |
| >>> a = tf.constant([True])<br>    >>> b = tf.constant([False])<br>    >>> tf.math.logical_and(a, b)<br>    <tf.Tensor: shape=(1,), dtype=bool, numpy=array([False])><br>    >>> a & b<br>    <tf.Tensor: shape=(1,), dtype=bool, numpy=array([False])><br><br>    c = tf.constant([True])<br><br>    y = tf.constant([False, False, True, True])<br><br>This op also supports broadcasting<br><br>    tf.logical_and([[True, False]], [[True], [False]]) |     |

The reduction version of this elementwise operation is [`tf.math.reduce_all`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_all)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of type bool. |
| `y` | A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of type bool. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> of type bool with the shape that `x` and `y` broadcast to. |     |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A `Tensor` of type `bool`. |
| `y` | A `Tensor` of type `bool`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` of type `bool`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.