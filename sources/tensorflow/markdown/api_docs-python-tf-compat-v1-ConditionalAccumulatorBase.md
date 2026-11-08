[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulatorBase#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulatorBase)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulatorBase?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulatorBase#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulatorBase#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulatorBase#methods)
    *   [num\_accumulated](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulatorBase#num_accumulated)
        
    *   [set\_global\_step](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulatorBase#set_global_step)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.ConditionalAccumulatorBase Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulatorBase#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulatorBase#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulatorBase#methods)
    *   [num\_accumulated](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulatorBase#num_accumulated)
        
    *   [set\_global\_step](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulatorBase#set_global_step)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/data_flow_ops.py#L1305-L1382)

A conditional accumulator for aggregating gradients.

tf.compat.v1.ConditionalAccumulatorBase(
        dtype, shape, accumulator_ref
    )

Up-to-date gradients (i.e., time step at which gradient was computed is equal to the accumulator's time step) are added to the accumulator.

Extraction of the average gradient is blocked until the required number of gradients has been accumulated.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dtype` | Datatype of the accumulated gradients. |
| `shape` | Shape of the accumulated gradients. |
| `accumulator_ref` | A handle to the conditional accumulator, created by sub- classes |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `accumulator_ref` | The underlying accumulator reference. |
| `dtype` | The datatype of the gradients accumulated by this accumulator. |
| `name` | The name of the underlying accumulator. |

Methods
-------

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

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.