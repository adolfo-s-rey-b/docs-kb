[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/expand_dims#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/expand_dims)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/expand_dims?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fexpand_dims&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/expand_dims#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/expand_dims#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/expand_dims#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/expand_dims#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.expand\_dims Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/expand_dims#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/expand_dims#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/expand_dims#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/expand_dims#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L318-L389)

Returns a tensor with a length 1 axis inserted at index `axis`. (deprecated arguments)

tf.compat.v1.expand_dims(
        input, axis=None, name=None, dim=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Fitting Dirichlet Process Mixture Model Using Preconditioned Stochastic Gradient Langevin Dynamics](https://www.tensorflow.org/probability/examples/Fitting_DPMM_Using_pSGLD)<br>    <br>*   [Wiki40B Language Models](https://www.tensorflow.org/hub/tutorials/wiki40b_lm) |

Given a tensor `input`, this operation inserts a dimension of length 1 at the dimension index `axis` of the `input`'s shape. The dimension index follows Python indexing rules: It's zero-based, a negative index that is counted backward from the end.

This operation is useful to:

*   Add an outer "batch" dimension to a single element.
*   Align axes for broadcasting.
*   To add an inner vector length axis to a tensor of scalars.

#### For example:

If you have a single image of shape `[height, width, channels]`:

    image = tf.zeros([10,10,3])

You can add an outer `batch` axis by passing `axis=0`:

    tf.expand_dims(image, axis=0).shape.as_list()

The new axis location matches Python `list.insert(axis, 1)`:

    tf.expand_dims(image, axis=1).shape.as_list()

Following standard Python indexing rules, a negative `axis` counts from the end so `axis=-1` adds an innermost dimension:

    tf.expand_dims(image, -1).shape.as_list()

This operation requires that `axis` is a valid index for `input.shape`, following Python indexing rules:

-1-tf.rank(input) <= axis <= tf.rank(input)

This operation is related to:

*   [`tf.squeeze`](https://www.tensorflow.org/api_docs/python/tf/squeeze)
    , which removes dimensions of size 1.
*   [`tf.reshape`](https://www.tensorflow.org/api_docs/python/tf/reshape)
    , which provides a more flexible reshaping capability.
*   [`tf.sparse.expand_dims`](https://www.tensorflow.org/api_docs/python/tf/sparse/expand_dims)
    , which provides this functionality for [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)
    

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. |
| `axis` | 0-D (scalar). Specifies the dimension index at which to expand the shape of `input`. Must be in the range `[-rank(input) - 1, rank(input)]`. |
| `name` | The name of the output is `Tensor` (optional). |
| `dim` | 0-D (scalar). Equivalent to `axis`, to be deprecated. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` with the same data as `input`, but its shape has an additional dimension of size 1 added. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if either both or neither of `dim` and `axis` are specified. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.