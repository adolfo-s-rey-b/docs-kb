[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulator#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulator#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulator#methods)
    *   [apply\_grad](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulator#apply_grad)
        
    *   [num\_accumulated](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulator#num_accumulated)
        
    *   [set\_global\_step](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulator#set_global_step)
        
    *   [take\_grad](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulator#take_grad)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.ConditionalAccumulator Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulator#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulator#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulator#methods)
    *   [apply\_grad](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulator#apply_grad)
        
    *   [num\_accumulated](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulator#num_accumulated)
        
    *   [set\_global\_step](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulator#set_global_step)
        
    *   [take\_grad](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulator#take_grad)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/data_flow_ops.py#L1385-L1473)

A conditional accumulator for aggregating gradients.

Inherits From: [`ConditionalAccumulatorBase`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulatorBase)

tf.compat.v1.ConditionalAccumulator(
        dtype,
        shape=None,
        shared_name=None,
        name='conditional_accumulator',
        reduction_type='MEAN'
    )

Up-to-date gradients (i.e., time step at which gradient was computed is equal to the accumulator's time step) are added to the accumulator.

Extraction of the average gradient is blocked until the required number of gradients has been accumulated.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dtype` | Datatype of the accumulated gradients. |
| `shape` | Shape of the accumulated gradients. |
| `shared_name` | Optional. If non-empty, this accumulator will be shared under the given name across multiple sessions. |
| `name` | Optional name for the accumulator. |
| `reduction_type` | Reduction type to use when taking the gradient. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `accumulator_ref` | The underlying accumulator reference. |
| `dtype` | The datatype of the gradients accumulated by this accumulator. |
| `name` | The name of the underlying accumulator. |

Methods
-------

### `apply_grad`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/data_flow_ops.py#L1424-L1446)

apply_grad(
        grad, local_step=0, name=None
    )

Attempts to apply a gradient to the accumulator.

The attempt is silently dropped if the gradient is stale, i.e., local\_step is less than the accumulator's global time step.

|     |     |
| --- | --- |
| Args |     |
| `grad` | The gradient tensor to be applied. |
| `local_step` | Time step at which the gradient was computed. |
| `name` | Optional name for the operation. |

|     |
| --- |
| Returns |     |
| The operation that (conditionally) applies a gradient to the accumulator. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If grad is of the wrong shape |

### `num_accumulated`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/data_flow_ops.py#L1351-L1364)

num_accumulated(
        name=None
    )

Number of gradients that have currently been aggregated in accumulator.

|     |     |
| --- | --- |
| Args |     |
| `name` | Optional name for the operation. |

|     |
| --- |
| Returns |     |
| Number of accumulated gradients currently in accumulator. |     |

### `set_global_step`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/data_flow_ops.py#L1366-L1382)

set_global_step(
        new_global_step, name=None
    )

Sets the global time step of the accumulator.

The operation logs a warning if we attempt to set to a time step that is lower than the accumulator's own time step.

|     |     |
| --- | --- |
| Args |     |
| `new_global_step` | Value of new time step. Can be a variable or a constant |
| `name` | Optional name for the operation. |

|     |
| --- |
| Returns |     |
| Operation that sets the accumulator's time step. |     |

### `take_grad`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/data_flow_ops.py#L1448-L1473)

take_grad(
        num_required, name=None
    )

Attempts to extract the average gradient from the accumulator.

The operation blocks until sufficient number of gradients have been successfully applied to the accumulator.

Once successful, the following actions are also triggered:

*   Counter of accumulated gradients is reset to 0.
*   Aggregated gradient is reset to 0 tensor.
*   Accumulator's internal time step is incremented by 1.

|     |     |
| --- | --- |
| Args |     |
| `num_required` | Number of gradients that needs to have been aggregated |
| `name` | Optional name for the operation |

|     |
| --- |
| Returns |     |
| A tensor holding the value of the average gradient. |     |

|     |     |
| --- | --- |
| Raises |     |
| `InvalidArgumentError` | If num\_required < 1 |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.