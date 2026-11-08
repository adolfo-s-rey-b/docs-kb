[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/SparseConditionalAccumulator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/SparseConditionalAccumulator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/SparseConditionalAccumulator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2FSparseConditionalAccumulator&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/SparseConditionalAccumulator#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/SparseConditionalAccumulator#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/SparseConditionalAccumulator#methods)
    *   [apply\_grad](https://www.tensorflow.org/api_docs/python/tf/compat/v1/SparseConditionalAccumulator#apply_grad)
        
    *   [apply\_indexed\_slices\_grad](https://www.tensorflow.org/api_docs/python/tf/compat/v1/SparseConditionalAccumulator#apply_indexed_slices_grad)
        
    *   [num\_accumulated](https://www.tensorflow.org/api_docs/python/tf/compat/v1/SparseConditionalAccumulator#num_accumulated)
        
    *   [set\_global\_step](https://www.tensorflow.org/api_docs/python/tf/compat/v1/SparseConditionalAccumulator#set_global_step)
        
    *   [take\_grad](https://www.tensorflow.org/api_docs/python/tf/compat/v1/SparseConditionalAccumulator#take_grad)
        
    *   [take\_indexed\_slices\_grad](https://www.tensorflow.org/api_docs/python/tf/compat/v1/SparseConditionalAccumulator#take_indexed_slices_grad)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Was this helpful?

tf.compat.v1.SparseConditionalAccumulator Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/SparseConditionalAccumulator#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/SparseConditionalAccumulator#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/SparseConditionalAccumulator#methods)
    *   [apply\_grad](https://www.tensorflow.org/api_docs/python/tf/compat/v1/SparseConditionalAccumulator#apply_grad)
        
    *   [apply\_indexed\_slices\_grad](https://www.tensorflow.org/api_docs/python/tf/compat/v1/SparseConditionalAccumulator#apply_indexed_slices_grad)
        
    *   [num\_accumulated](https://www.tensorflow.org/api_docs/python/tf/compat/v1/SparseConditionalAccumulator#num_accumulated)
        
    *   [set\_global\_step](https://www.tensorflow.org/api_docs/python/tf/compat/v1/SparseConditionalAccumulator#set_global_step)
        
    *   [take\_grad](https://www.tensorflow.org/api_docs/python/tf/compat/v1/SparseConditionalAccumulator#take_grad)
        
    *   [take\_indexed\_slices\_grad](https://www.tensorflow.org/api_docs/python/tf/compat/v1/SparseConditionalAccumulator#take_indexed_slices_grad)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/data_flow_ops.py#L1476-L1669)

A conditional accumulator for aggregating sparse gradients.

Inherits From: [`ConditionalAccumulatorBase`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/ConditionalAccumulatorBase)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sparse.SparseConditionalAccumulator`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/SparseConditionalAccumulator)

tf.compat.v1.SparseConditionalAccumulator(
        dtype,
        shape=None,
        shared_name=None,
        name='sparse_conditional_accumulator',
        reduction_type='MEAN'
    )

Sparse gradients are represented by `IndexedSlices`.

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/data_flow_ops.py#L1537-L1583)

apply_grad(
        grad_indices, grad_values, grad_shape=None, local_step=0, name=None
    )

Attempts to apply a sparse gradient to the accumulator.

The attempt is silently dropped if the gradient is stale, i.e., `local_step` is less than the accumulator's global time step.

A sparse gradient is represented by its indices, values and possibly empty or None shape. Indices must be a vector representing the locations of non-zero entries in the tensor. Values are the non-zero slices of the gradient, and must have the same first dimension as indices, i.e., the nnz represented by indices and values must be consistent. Shape, if not empty or None, must be consistent with the accumulator's shape (if also provided).

|     |
| --- |
| Example |     |
| A tensor \[\[0, 0\], \[0, 1\], \[2, 3\]\] can be represented indices: \[1,2\] values: \[\[0,1\],\[2,3\]\] shape: \[3, 2\] |     |

|     |     |
| --- | --- |
| Args |     |
| `grad_indices` | Indices of the sparse gradient to be applied. |
| `grad_values` | Values of the sparse gradient to be applied. |
| `grad_shape` | Shape of the sparse gradient to be applied. |
| `local_step` | Time step at which the gradient was computed. |
| `name` | Optional name for the operation. |

|     |
| --- |
| Returns |     |
| The operation that (conditionally) applies a gradient to the accumulator. |     |

|     |     |
| --- | --- |
| Raises |     |
| `InvalidArgumentError` | If grad is of the wrong shape |

### `apply_indexed_slices_grad`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/data_flow_ops.py#L1513-L1535)

apply_indexed_slices_grad(
        grad, local_step=0, name=None
    )

Attempts to apply a gradient to the accumulator.

The attempt is silently dropped if the gradient is stale, i.e., `local_step` is less than the accumulator's global time step.

|     |     |
| --- | --- |
| Args |     |
| `grad` | The gradient `IndexedSlices` to be applied. |
| `local_step` | Time step at which the gradient was computed. |
| `name` | Optional name for the operation. |

|     |
| --- |
| Returns |     |
| The operation that (conditionally) applies a gradient to the accumulator. |     |

|     |     |
| --- | --- |
| Raises |     |
| `InvalidArgumentError` | If grad is of the wrong shape |

### `num_accumulated`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/data_flow_ops.py#L1638-L1651)

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/data_flow_ops.py#L1653-L1669)

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

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/data_flow_ops.py#L1585-L1607)

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
| A tuple of indices, values, and shape representing the average gradient. |     |

|     |     |
| --- | --- |
| Raises |     |
| `InvalidArgumentError` | If `num_required` < 1 |

### `take_indexed_slices_grad`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/data_flow_ops.py#L1609-L1635)

take_indexed_slices_grad(
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
| An `IndexedSlices` holding the value of the average gradient. |     |

|     |     |
| --- | --- |
| Raises |     |
| `InvalidArgumentError` | If `num_required` < 1 |

Was this helpful?

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.