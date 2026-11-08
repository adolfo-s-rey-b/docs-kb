[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/cond#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/cond)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/cond?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/cond#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/cond#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/cond#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.cond Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/cond#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/cond#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/cond#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/cond.py#L39-L240)

Return `true_fn()` if the predicate `pred` is true else `false_fn()`. (deprecated arguments)

tf.compat.v1.cond(
        pred,
        true_fn=None,
        false_fn=None,
        strict=False,
        name=None,
        fn1=None,
        fn2=None
    )

`true_fn` and `false_fn` both return lists of output tensors. `true_fn` and `false_fn` must have the same non-zero number and type of outputs.

Although this behavior is consistent with the dataflow model of TensorFlow, it has frequently surprised users who expected a lazier semantics. Consider the following simple program:

z = tf.multiply(a, b)
    result = tf.cond(x < y, lambda: tf.add(x, z), lambda: tf.square(y))

If `x < y`, the `tf.add` operation will be executed and `tf.square` operation will not be executed. Since `z` is needed for at least one branch of the `cond`, the [`tf.multiply`](https://www.tensorflow.org/api_docs/python/tf/math/multiply)
 operation is always executed, unconditionally.

Note that `cond` calls `true_fn` and `false_fn` _exactly once_ (inside the call to `cond`, and not at all during `Session.run()`). `cond` stitches together the graph fragments created during the `true_fn` and `false_fn` calls with some additional graph nodes to ensure that the right branch gets executed depending on the value of `pred`.

[`tf.cond`](https://www.tensorflow.org/api_docs/python/tf/cond)
 supports nested structures as implemented in `tensorflow.python.util.nest`. Both `true_fn` and `false_fn` must return the same (possibly nested) value structure of lists, tuples, and/or named tuples. Singleton lists and tuples form the only exceptions to this: when returned by `true_fn` and/or `false_fn`, they are implicitly unpacked to single values. This behavior is disabled by passing `strict=True`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `pred` | A scalar determining whether to return the result of `true_fn` or `false_fn`. |
| `true_fn` | The callable to be performed if pred is true. |
| `false_fn` | The callable to be performed if pred is false. |
| `strict` | A boolean that enables/disables 'strict' mode; see above. |
| `name` | Optional name prefix for the returned tensors. |

|     |
| --- |
| Returns<br>------- |     |
| Tensors returned by the call to either `true_fn` or `false_fn`. If the callables return a singleton list, the element is extracted from the list. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | if `true_fn` or `false_fn` is not callable. |
| `ValueError` | if `true_fn` and `false_fn` do not return the same number of tensors, or return tensors of different types. |

#### Example:

x = tf.constant(2)
    y = tf.constant(5)
    def f1(): return tf.multiply(x, 17)
    def f2(): return tf.add(y, 23)
    r = tf.cond(tf.less(x, y), f1, f2)
    # r is set to f1().
    # Operations in f2 (e.g., tf.add) are not executed.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.