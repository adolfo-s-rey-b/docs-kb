[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/types/experimental/AtomicFunction#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/types/experimental/AtomicFunction)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/types/experimental/AtomicFunction?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/types/experimental/AtomicFunction#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/types/experimental/AtomicFunction#methods)
    *   [call\_with\_captures](https://www.tensorflow.org/api_docs/python/tf/types/experimental/AtomicFunction#call_with_captures)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/types/experimental/AtomicFunction#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.types.experimental.AtomicFunction Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/types/experimental/AtomicFunction#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/types/experimental/AtomicFunction#methods)
    *   [call\_with\_captures](https://www.tensorflow.org/api_docs/python/tf/types/experimental/AtomicFunction#call_with_captures)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/types/experimental/AtomicFunction#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/core.py#L142-L166)

Base class for graph functions.

Inherits From: [`Callable`](https://www.tensorflow.org/api_docs/python/tf/types/experimental/Callable)

An `AtomicFunction` encapsulates a single graph function definition.

`AtomicFunction` can be called directly only if no captures are needed according to the `FunctionType`. If captures are present, please use `call_with_captures` instead.

`AtomicFunction` does not support gradients. Please use the parent `ConcreteFunction` if you need gradient support.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `function_type` | Returns a FunctionType describing this callable. |

Methods
-------

### `call_with_captures`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/core.py#L156-L166)

call_with_captures(
        args, kwargs, captures
    )

Calls this AtomicFunction with captures as defined by its FunctionType.

|     |     |
| --- | --- |
| Args |     |
| `args` | Tuple containing positional arguments |
| `kwargs` | Dict containing keyword arguments |
| `captures` | Tuple of tensors supplying captured tensor values. |

|     |
| --- |
| Returns |     |
| A structured output value based on the inputs. |     |

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