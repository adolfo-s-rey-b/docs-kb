[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/types/experimental/ConcreteFunction#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/types/experimental/ConcreteFunction)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/types/experimental/ConcreteFunction?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/types/experimental/ConcreteFunction#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/types/experimental/ConcreteFunction#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/types/experimental/ConcreteFunction#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.types.experimental.ConcreteFunction Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/types/experimental/ConcreteFunction#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/types/experimental/ConcreteFunction#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/types/experimental/ConcreteFunction#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/core.py#L169-L182)

Base class for differentiable graph functions.

Inherits From: [`Callable`](https://www.tensorflow.org/api_docs/python/tf/types/experimental/Callable)

A `ConcreteFunction` encapsulates the original graph function definition with support for differentiability under [`tf.GradientTape`](https://www.tensorflow.org/api_docs/python/tf/GradientTape)
 contexts. In the process, it may generate new graph functions (using the original) to efficiently perform forwards and backwards passes.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `function_type` | Returns a FunctionType describing this callable. |
| `inference_fn` | Returns the original `AtomicFunction` owned by this ConcreteFunction. |

Methods
-------

### `__call__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/core.py#L124-L139)

__call__(
        *args, **kwargs
    )

Executes this callable.

This behaves like a regular op - in eager mode, it immediately starts execution, returning results. In graph mode, it creates ops which return symbolic TensorFlow values (like [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
, etc.). For example, [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 callables typically generate a [`tf.raw_ops.PartitionedCall`](https://www.tensorflow.org/api_docs/python/tf/raw_ops/PartitionedCall)
 op, but not always - the exact operations being generated are an internal implementation detail.

|     |     |
| --- | --- |
| Args |     |
| `*args` | positional argument for this call |
| `**kwargs` | keyword arguments for this call |

|     |
| --- |
| Returns |     |
| The execution results. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.