[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_to_dense#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_to_dense)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_to_dense?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_to_dense#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_to_dense#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.sparse\_to\_dense Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_to_dense#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_to_dense#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sparse_ops.py#L1186-L1243)

Converts a sparse representation into a dense tensor. (deprecated)

tf.compat.v1.sparse_to_dense(
        sparse_indices,
        output_shape,
        sparse_values,
        default_value=0,
        validate_indices=True,
        name=None
    )

Builds an array `dense` with shape `output_shape` such that

# If sparse_indices is scalar
    dense[i] = (i == sparse_indices ? sparse_values : default_value)
    
    # If sparse_indices is a vector, then for each i
    dense[sparse_indices[i]] = sparse_values[i]
    
    # If sparse_indices is an n by d matrix, then for each i in [0, n)\
    dense[sparse_indices[i][0], ..., sparse_indices[i][d-1]] = sparse_values[i]\
\
All other values in `dense` are set to `default_value`. If `sparse_values` is a scalar, all sparse indices are set to this single value.\
\
Indices should be sorted in lexicographic order, and indices must not contain any repeats. If `validate_indices` is True, these properties are checked during execution.\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `sparse_indices` | A 0-D, 1-D, or 2-D `Tensor` of type `int32` or `int64`. `sparse_indices[i]` contains the complete index where `sparse_values[i]` will be placed. |\
| `output_shape` | A 1-D `Tensor` of the same type as `sparse_indices`. Shape of the dense output tensor. |\
| `sparse_values` | A 0-D or 1-D `Tensor`. Values corresponding to each row of `sparse_indices`, or a scalar value to be used for all sparse indices. |\
| `default_value` | A 0-D `Tensor` of the same type as `sparse_values`. Value to set for indices not specified in `sparse_indices`. Defaults to zero. |\
| `validate_indices` | A boolean value. If True, indices are checked to make sure they are sorted in lexicographic order and that there are no repeats. |\
| `name` | A name for the operation (optional). |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| Dense `Tensor` of shape `output_shape`. Has the same type as `sparse_values`. |     |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.