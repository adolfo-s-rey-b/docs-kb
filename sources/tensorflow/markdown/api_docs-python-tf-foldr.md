[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/foldr#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/foldr)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/foldr?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/foldr#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/foldr#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/foldr#raises)
    
*   [Example](https://www.tensorflow.org/api_docs/python/tf/foldr#example)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.foldr Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/foldr#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/foldr#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/foldr#raises)
    
*   [Example](https://www.tensorflow.org/api_docs/python/tf/foldr#example)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/functional_ops.py#L358-L432)

foldr on the list of tensors unpacked from `elems` on dimension 0. (deprecated argument values)

tf.foldr(
        fn,
        elems,
        initializer=None,
        parallel_iterations=10,
        back_prop=True,
        swap_memory=False,
        name=None
    )

This foldr operator repeatedly applies the callable `fn` to a sequence of elements from last to first. The elements are made of the tensors unpacked from `elems`. The callable fn takes two tensors as arguments. The first argument is the accumulated value computed from the preceding invocation of fn, and the second is the value at the current position of `elems`. If `initializer` is None, `elems` must contain at least one element, and its first element is used as the initializer.

Suppose that `elems` is unpacked into `values`, a list of tensors. The shape of the result tensor is `fn(initializer, values[0]).shape`.

This method also allows multi-arity `elems` and output of `fn`. If `elems` is a (possibly nested) list or tuple of tensors, then each of these tensors must have a matching first (unpack) dimension. The signature of `fn` may match the structure of `elems`. That is, if `elems` is `(t1, [t2, t3, [t4, t5]])`, then an appropriate signature for `fn` is: `fn = lambda (t1, [t2, t3, [t4, t5]]):`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `fn` | The callable to be performed. |
| `elems` | A tensor or (possibly nested) sequence of tensors, each of which will be unpacked along their first dimension. The nested sequence of the resulting slices will be the first argument to `fn`. |
| `initializer` | (optional) A tensor or (possibly nested) sequence of tensors, as the initial value for the accumulator. |
| `parallel_iterations` | (optional) The number of iterations allowed to run in parallel. |
| `back_prop` | (optional) Deprecated. False disables support for back propagation. Prefer using [`tf.stop_gradient`](https://www.tensorflow.org/api_docs/python/tf/stop_gradient)<br> instead. |
| `swap_memory` | (optional) True enables GPU-CPU memory swapping. |
| `name` | (optional) Name prefix for the returned tensors. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor or (possibly nested) sequence of tensors, resulting from applying `fn` consecutively to the list of tensors unpacked from `elems`, from last to first. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | if `fn` is not callable. |

|     |
| --- |
| Example<br>------- |     |
| elems = [1, 2, 3, 4, 5, 6]<br>    sum = tf.foldr(lambda a, x: a + x, elems)<br>    # sum == 21 |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.