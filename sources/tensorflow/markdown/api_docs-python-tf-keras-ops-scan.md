[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/scan#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/scan)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/scan?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fscan&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/scan#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/scan#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.scan Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/scan#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/scan#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L116-L192)

Scan a function over leading array axes while carrying along state.

tf.keras.ops.scan(
        f, init, xs=None, length=None, reverse=False, unroll=1
    )

When the type of `xs` is an array type or `None`, and the type of `ys` is an array type, the semantics of `scan()` are given roughly by this Python implementation:

def scan(f, init, xs, length=None):
        if xs is None:
            xs = [None] * length
        carry = init
        ys = []
        for x in xs:
            carry, y = f(carry, x)
            ys.append(y)
        return carry, np.stack(ys)

The loop-carried value `carry` (`init`) must hold a fixed shape and dtype across all iterations.

In TensorFlow, `y` must match `carry` in shape and dtype. This is not required in other backends.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `f` | Callable defines the logic for each loop iteration. This accepts two arguments where the first is a value of the loop carry and the second is a slice of `xs` along its leading axis. This callable returns a pair where the first represents a new value for the loop carry and the second represents a slice of the output. |
| `init` | The initial loop carry value. This can be a scalar, tensor, or any nested structure. It must match the structure of the first element returned by `f`. |
| `xs` | Optional value to scan along its leading axis. This can be a tensor or any nested structure. If `xs` is not provided, you must specify `length` to define the number of loop iterations. Defaults to `None`. |
| `length` | Optional integer specifying the number of loop iterations. If `length` is not provided, it defaults to the sizes of leading axis of the arrays in `xs`. Defaults to `None`. |
| `reverse` | Optional boolean specifying whether to run the scan iteration forward or in reverse, equivalent to reversing the leading axes of the arrays in both `xs` and in `ys`. |
| `unroll` | Optional positive integer or boolean specifying how many scan iterations to unroll within a single iteration of a loop. If an integer is provided, it determines how many unrolled loop iterations to run within a single rolled iteration of the loop. If a boolean is provided, it will determine if the loop is completely unrolled (`unroll=True`) or left completely unrolled (`unroll=False`). Note that unrolling is only supported by JAX and TensorFlow backends. |

|     |
| --- |
| Returns<br>------- |     |
| A pair where the first element represents the final loop carry value and the second element represents the stacked outputs of `f` when scanned over the leading axis of the inputs. |     |

#### Examples:

    sum_fn = lambda c, x: (c + x, c + x)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.