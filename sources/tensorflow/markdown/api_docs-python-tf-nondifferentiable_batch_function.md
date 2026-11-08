[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nondifferentiable_batch_function#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nondifferentiable_batch_function)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nondifferentiable_batch_function?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nondifferentiable_batch_function#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nondifferentiable_batch_function#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nondifferentiable\_batch\_function Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nondifferentiable_batch_function#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nondifferentiable_batch_function#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/batch_ops.py#L28-L123)

Batches the computation done by the decorated function.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nondifferentiable_batch_function`](https://www.tensorflow.org/api_docs/python/tf/nondifferentiable_batch_function)

tf.nondifferentiable_batch_function(
        num_batch_threads,
        max_batch_size,
        batch_timeout_micros,
        allowed_batch_sizes=None,
        max_enqueued_batches=10,
        autograph=True,
        enable_large_batch_splitting=True
    )

So, for example, in the following code

@batch_function(1, 2, 3)
    def layer(a):
      return tf.matmul(a, a)
    
    b = layer(w)

if more than one session.run call is simultaneously trying to compute `b` the values of `w` will be gathered, non-deterministically concatenated along the first axis, and only one thread will run the computation. See the documentation of the `Batch` op for more details.

Assumes that all arguments of the decorated function are Tensors which will be batched along their first dimension.

SparseTensor is not supported. The return value of the decorated function must be a Tensor or a list/tuple of Tensors.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_batch_threads` | Number of scheduling threads for processing batches of work. Determines the number of batches processed in parallel. |
| `max_batch_size` | Batch sizes will never be bigger than this. |
| `batch_timeout_micros` | Maximum number of microseconds to wait before outputting an incomplete batch. |
| `allowed_batch_sizes` | Optional list of allowed batch sizes. If left empty, does nothing. Otherwise, supplies a list of batch sizes, causing the op to pad batches up to one of those sizes. The entries must increase monotonically, and the final entry must equal max\_batch\_size. |
| `max_enqueued_batches` | The maximum depth of the batch queue. Defaults to 10. |
| `autograph` | Whether to use autograph to compile python and eager style code for efficient graph-mode execution. |
| `enable_large_batch_splitting` | The value of this option doesn't affect processing output given the same input; it affects implementation details as stated below: 1. Improve batching efficiency by eliminating unnecessary adding. 2.`max_batch_size` specifies the limit of input and `allowed_batch_sizes` specifies the limit of a task to be processed. API user can give an input of size 128 when 'max\_execution\_batch\_size' is 32 -> implementation can split input of 128 into 4 x 32, schedule concurrent processing, and then return concatenated results corresponding to 128. |

|     |
| --- |
| Returns<br>------- |     |
| The decorated function will return the unbatched computation output Tensors. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.