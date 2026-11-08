[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/map_fn#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/map_fn)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/map_fn?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/map_fn#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/map_fn#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/map_fn#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/map_fn#raises)
    
*   [Examples](https://www.tensorflow.org/api_docs/python/tf/map_fn#examples)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.map\_fn Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/map_fn#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/map_fn#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/map_fn#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/map_fn#raises)
    
*   [Examples](https://www.tensorflow.org/api_docs/python/tf/map_fn#examples)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/map_fn.py#L613-L644)

Transforms `elems` by applying `fn` to each element unstacked on axis 0. (deprecated arguments)

tf.map_fn(
        fn,
        elems,
        dtype=None,
        parallel_iterations=None,
        back_prop=True,
        swap_memory=False,
        infer_shape=True,
        name=None,
        fn_output_signature=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Matrix approximation with Core APIs](https://www.tensorflow.org/guide/core/matrix_core)<br>    <br>*   [Extension types](https://www.tensorflow.org/guide/extension_type)<br>    <br>*   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor)<br>    <br>*   [NumPy API on TensorFlow](https://www.tensorflow.org/guide/tf_numpy) | *   [Federated Learning for Text Generation](https://www.tensorflow.org/federated/tutorials/federated_learning_for_text_generation)<br>    <br>*   [Classify Flowers with Transfer Learning](https://www.tensorflow.org/hub/tutorials/image_feature_vector)<br>    <br>*   [Quantum Convolutional Neural Network](https://www.tensorflow.org/quantum/tutorials/qcnn) |

See also [`tf.scan`](https://www.tensorflow.org/api_docs/python/tf/scan)
.

`map_fn` unstacks `elems` on axis 0 to obtain a sequence of elements; calls `fn` to transform each element; and then stacks the transformed values back together.

#### Mapping functions with single-Tensor inputs and outputs

If `elems` is a single tensor and `fn`'s signature is `tf.Tensor->tf.Tensor`, then `map_fn(fn, elems)` is equivalent to `tf.stack([fn(elem) for elem in tf.unstack(elems)])`. E.g.:

    tf.map_fn(fn=lambda t: tf.range(t, t + 3), elems=tf.constant([3, 5, 2]))

`map_fn(fn, elems).shape = [elems.shape[0]] + fn(elems[0]).shape`.

#### Mapping functions with multi-arity inputs and outputs

`map_fn` also supports functions with multi-arity inputs and outputs:

*   If `elems` is a tuple (or nested structure) of tensors, then those tensors must all have the same outer-dimension size (`num_elems`); and `fn` is used to transform each tuple (or structure) of corresponding slices from `elems`. E.g., if `elems` is a tuple `(t1, t2, t3)`, then `fn` is used to transform each tuple of slices `(t1[i], t2[i], t3[i])` (where `0 <= i < num_elems`).
    
*   If `fn` returns a tuple (or nested structure) of tensors, then the result is formed by stacking corresponding elements from those structures.
    

#### Specifying `fn`'s output signature

If `fn`'s input and output signatures differ (their structures, dtypes or tensor types do not match), then the output signature must be specified using `fn_output_signature`. For example:

    tf.map_fn(fn=tf.strings.length,  # input & output have different dtypes

`fn_output_signature` can be specified using any of the following:

*   A [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)
     or [`tf.TensorSpec`](https://www.tensorflow.org/api_docs/python/tf/TensorSpec)
     (to describe a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
    )
*   A [`tf.RaggedTensorSpec`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensorSpec)
     (to describe a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
    )
*   A [`tf.SparseTensorSpec`](https://www.tensorflow.org/api_docs/python/tf/SparseTensorSpec)
     (to describe a [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)
    )
*   A (possibly nested) tuple, list, or dict containing the above types.

#### RaggedTensors

`map_fn` supports [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 inputs and outputs. In particular:

*   If `elems` is a `RaggedTensor`, then `fn` will be called with each row of that ragged tensor.
    
    *   If `elems` has only one ragged dimension, then the values passed to `fn` will be [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
        s.
    *   If `elems` has multiple ragged dimensions, then the values passed to `fn` will be [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
        s with one fewer ragged dimension.
*   If the result of `map_fn` should be a `RaggedTensor`, then use a [`tf.RaggedTensorSpec`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensorSpec)
     to specify `fn_output_signature`.
    
    *   If `fn` returns [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
        s with varying sizes, then use a [`tf.RaggedTensorSpec`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensorSpec)
         with `ragged_rank=0` to combine them into a single ragged tensor (which will have ragged\_rank=1).
    *   If `fn` returns [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
        s, then use a [`tf.RaggedTensorSpec`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensorSpec)
         with the same `ragged_rank`.

    # Example: RaggedTensor input

    # Example: RaggedTensor output

*   [`tf.ragged.map_flat_values(fn, rt)`](https://www.tensorflow.org/api_docs/python/tf/ragged/map_flat_values)
     (if fn is expressible as TensorFlow ops)
*   `rt.with_flat_values(map_fn(fn, rt.flat_values))` (otherwise)

E.g.:

    rt = tf.ragged.constant([[1, 2, 3], [], [4, 5], [6]])

#### SparseTensors

`map_fn` supports [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)
 inputs and outputs. In particular:

*   If `elems` is a `SparseTensor`, then `fn` will be called with each row of that sparse tensor. In particular, the value passed to `fn` will be a [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)
     with one fewer dimension than `elems`.
    
*   If the result of `map_fn` should be a `SparseTensor`, then use a [`tf.SparseTensorSpec`](https://www.tensorflow.org/api_docs/python/tf/SparseTensorSpec)
     to specify `fn_output_signature`. The individual `SparseTensor`s returned by `fn` will be stacked into a single `SparseTensor` with one more dimension.
    

    # Example: SparseTensor input

    # Example: SparseTensor output

*   If the function is expressible as TensorFlow ops, use:
    
    tf.sparse.SparseTensor(st.indices, fn(st.values), st.dense_shape)
    
*   Otherwise, use:
    
    tf.sparse.SparseTensor(st.indices, tf.map_fn(fn, st.values),
                               st.dense_shape)
    

#### `map_fn` vs. vectorized operations

`map_fn` will apply the operations used by `fn` to each element of `elems`, resulting in `O(elems.shape[0])` total operations. This is somewhat mitigated by the fact that `map_fn` can process elements in parallel. However, a transform expressed using `map_fn` is still typically less efficient than an equivalent transform expressed using vectorized operations.

`map_fn` should typically only be used if one of the following is true:

*   It is difficult or expensive to express the desired transform with vectorized operations.
*   `fn` creates large intermediate values, so an equivalent vectorized transform would take too much memory.
*   Processing elements in parallel is more efficient than an equivalent vectorized transform.
*   Efficiency of the transform is not critical, and using `map_fn` is more readable.

E.g., the example given above that maps `fn=lambda t: tf.range(t, t + 3)` across `elems` could be rewritten more efficiently using vectorized ops:

    elems = tf.constant([3, 5, 2])

In some cases, [`tf.vectorized_map`](https://www.tensorflow.org/api_docs/python/tf/vectorized_map)
 can be used to automatically convert a function to a vectorized equivalent.

#### Eager execution

When executing eagerly, `map_fn` does not execute in parallel even if `parallel_iterations` is set to a value > 1. You can still get the performance benefits of running a function in parallel by using the [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 decorator:

    fn=lambda t: tf.range(t, t + 3)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `fn` | The callable to be performed. It accepts one argument, which will have the same (possibly nested) structure as `elems`. Its output must have the same structure as `fn_output_signature` if one is provided; otherwise it must have the same structure as `elems`. |
| `elems` | A tensor or (possibly nested) sequence of tensors, each of which will be unstacked along their first dimension. `fn` will be applied to the nested sequence of the resulting slices. `elems` may include ragged and sparse tensors. `elems` must consist of at least one tensor. |
| `dtype` | Deprecated: Equivalent to `fn_output_signature`. |
| `parallel_iterations` | (optional) The number of iterations allowed to run in parallel. When graph building, the default value is 10. While executing eagerly, the default value is set to 1. |
| `back_prop` | (optional) Deprecated: prefer using [`tf.stop_gradient`](https://www.tensorflow.org/api_docs/python/tf/stop_gradient)<br> instead. False disables support for back propagation. |
| `swap_memory` | (optional) True enables GPU-CPU memory swapping. |
| `infer_shape` | (optional) False disables tests for consistent output shapes. |
| `name` | (optional) Name prefix for the returned tensors. |
| `fn_output_signature` | The output signature of `fn`. Must be specified if `fn`'s input and output signatures are different (i.e., if their structures, dtypes, or tensor types do not match). `fn_output_signature` can be specified using any of the following:<br><br>*   A [`tf.DType`](https://www.tensorflow.org/api_docs/python/tf/dtypes/DType)<br>     or [`tf.TensorSpec`](https://www.tensorflow.org/api_docs/python/tf/TensorSpec)<br>     (to describe a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>    )<br>*   A [`tf.RaggedTensorSpec`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensorSpec)<br>     (to describe a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)<br>    )<br>*   A [`tf.SparseTensorSpec`](https://www.tensorflow.org/api_docs/python/tf/SparseTensorSpec)<br>     (to describe a [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)<br>    )<br>*   A (possibly nested) tuple, list, or dict containing the above types. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor or (possibly nested) sequence of tensors. Each tensor stacks the results of applying `fn` to tensors unstacked from `elems` along the first dimension, from first to last. The result may include ragged and sparse tensors. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | if `fn` is not callable or the structure of the output of `fn` and `fn_output_signature` do not match. |
| `ValueError` | if the lengths of the output of `fn` and `fn_output_signature` do not match, or if the `elems` does not contain any tensor. |

|     |
| --- |
| Examples<br>-------- |     |
| >>> elems = np.array([1, 2, 3, 4, 5, 6])<br>    >>> tf.map_fn(lambda x: x * x, elems)<br>    <tf.Tensor: shape=(6,), dtype=int64, numpy=array([ 1,  4,  9, 16, 25, 36])><br><br>    elems = (np.array([1, 2, 3]), np.array([-1, 1, -1]))<br><br>    elems = np.array([1, 2, 3]) |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.