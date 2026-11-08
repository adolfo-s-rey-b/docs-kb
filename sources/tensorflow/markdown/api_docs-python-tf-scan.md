[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/scan#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/scan)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/scan?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/scan#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/scan#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/scan#raises)
    
*   [Examples](https://www.tensorflow.org/api_docs/python/tf/scan#examples)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.scan Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/scan#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/scan#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/scan#raises)
    
*   [Examples](https://www.tensorflow.org/api_docs/python/tf/scan#examples)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/functional_ops.py#L691-L812)

scan on the list of tensors unpacked from `elems` on dimension 0. (deprecated argument values)

tf.scan(
        fn,
        elems,
        initializer=None,
        parallel_iterations=10,
        back_prop=True,
        swap_memory=False,
        infer_shape=True,
        reverse=False,
        name=None
    )

The simplest version of `scan` repeatedly applies the callable `fn` to a sequence of elements from first to last. The elements are made of the tensors unpacked from `elems` on dimension 0. The callable fn takes two tensors as arguments. The first argument is the accumulated value computed from the preceding invocation of fn, and the second is the value at the current position of `elems`. If `initializer` is None, `elems` must contain at least one element, and its first element is used as the initializer.

Suppose that `elems` is unpacked into `values`, a list of tensors. The shape of the result tensor is `[len(values)] + fn(initializer, values[0]).shape`. If reverse=True, it's fn(initializer, values\[-1\]).shape.

This method also allows multi-arity `elems` and accumulator. If `elems` is a (possibly nested) list or tuple of tensors, then each of these tensors must have a matching first (unpack) dimension. The second argument of `fn` must match the structure of `elems`.

If no `initializer` is provided, the output structure and dtypes of `fn` are assumed to be the same as its input; and in this case, the first argument of `fn` must match the structure of `elems`.

If an `initializer` is provided, then the output of `fn` must have the same structure as `initializer`; and the first argument of `fn` must match this structure.

For example, if `elems` is `(t1, [t2, t3])` and `initializer` is `[i1, i2]` then an appropriate signature for `fn` in `python2` is: `fn = lambda (acc_p1, acc_p2), (t1, [t2, t3]):` and `fn` must return a list, `[acc_n1, acc_n2]`. An alternative correct signature for `fn`, and the one that works in `python3`, is: `fn = lambda a, t:`, where `a` and `t` correspond to the input tuples.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `fn` | The callable to be performed. It accepts two arguments. The first will have the same structure as `initializer` if one is provided, otherwise it will have the same structure as `elems`. The second will have the same (possibly nested) structure as `elems`. Its output must have the same structure as `initializer` if one is provided, otherwise it must have the same structure as `elems`. |
| `elems` | A tensor or (possibly nested) sequence of tensors, each of which will be unpacked along their first dimension. The nested sequence of the resulting slices will be the first argument to `fn`. |
| `initializer` | (optional) A tensor or (possibly nested) sequence of tensors, initial value for the accumulator, and the expected output type of `fn`. |
| `parallel_iterations` | (optional) The number of iterations allowed to run in parallel. |
| `back_prop` | (optional) Deprecated. False disables support for back propagation. Prefer using [`tf.stop_gradient`](https://www.tensorflow.org/api_docs/python/tf/stop_gradient)<br> instead. |
| `swap_memory` | (optional) True enables GPU-CPU memory swapping. |
| `infer_shape` | (optional) False disables tests for consistent output shapes. |
| `reverse` | (optional) True scans the tensor last to first (instead of first to last). |
| `name` | (optional) Name prefix for the returned tensors. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor or (possibly nested) sequence of tensors. Each tensor packs the results of applying `fn` to tensors unpacked from `elems` along the first dimension, and the previous accumulator value(s), from first to last (or last to first, if `reverse=True`). |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | if `fn` is not callable or the structure of the output of `fn` and `initializer` do not match. |
| `ValueError` | if the lengths of the output of `fn` and `initializer` do not match. |

|     |
| --- |
| Examples<br>-------- |     |
| elems = np.array([1, 2, 3, 4, 5, 6])<br>    sum = scan(lambda a, x: a + x, elems)<br>    # sum == [1, 3, 6, 10, 15, 21]<br>    sum = scan(lambda a, x: a + x, elems, reverse=True)<br>    # sum == [21, 20, 18, 15, 11, 6]<br><br>elems = np.array([1, 2, 3, 4, 5, 6])<br>    initializer = np.array(0)<br>    sum_one = scan(<br>        lambda a, x: x[0] - x[1] + a, (elems + 1, elems), initializer)<br>    # sum_one == [1, 2, 3, 4, 5, 6]<br><br>elems = np.array([1, 0, 0, 0, 0, 0])<br>    initializer = (np.array(0), np.array(1))<br>    fibonaccis = scan(lambda a, _: (a[1], a[0] + a[1]), elems, initializer)<br>    # fibonaccis == ([1, 1, 2, 3, 5, 8], [1, 2, 3, 5, 8, 13]) |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.