[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/associative_scan#main-content)

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
    

tf.keras.ops.associative\_scan Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L232-L290)

Performs a scan with an associative binary operation, in parallel.

tf.keras.ops.associative_scan(
        f, elems, reverse=False, axis=0
    )

This operation his similar to `scan`, with the key difference that `associative_scan` is a parallel implementation with potentially significant performance benefits, especially when jit compiled. The catch is that it can only be used when `f` is a binary associative operation (i.e. it must verify `f(a, f(b, c)) == f(f(a, b), c)`).

For an introduction to associative scans, refer to this paper: Blelloch, Guy E. 1990. [Prefix Sums and Their Applications](https://www.cs.cmu.edu/%7Eguyb/papers/Ble93.pdf)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `f` | A Python callable implementing an associative binary operation with signature `r = f(a, b)`. Function `f` must be associative, i.e., it must satisfy the equation `f(a, f(b, c)) == f(f(a, b), c)`. The inputs and result are (possibly nested Python tree structures of) array(s) matching `elems`. Each array has a dimension in place of the `axis` dimension. `f` should be applied elementwise over the `axis` dimension. The result `r` has the same shape (and structure) as the two inputs `a` and `b`. |
| `elems` | A (possibly nested Python tree structure of) array(s), each with an `axis` dimension of size `num_elems`. |
| `reverse` | A boolean stating if the scan should be reversed with respect to the `axis` dimension. |
| `axis` | an integer identifying the axis over which the scan should occur. |

|     |
| --- |
| Returns<br>------- |     |
| A (possibly nested Python tree structure of) array(s) of the same shape and structure as `elems`, in which the `k`'th element of `axis` is the result of recursively applying `f` to combine the first `k` elements of `elems` along `axis`. For example, given `elems = [a, b, c, ...]`, the result would be `[a, f(a, b), f(f(a, b), c), ...]`. |     |

#### Examples:

    sum_fn = lambda x, y: x + y

    sum_fn = lambda x, y: [x[0] + y[0], x[1] + y[1], x[2] + y[2]]

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.