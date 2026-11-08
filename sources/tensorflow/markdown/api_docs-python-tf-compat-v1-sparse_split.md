[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_split#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_split)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_split?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fsparse_split&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_split#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_split#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_split#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.sparse\_split Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_split#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_split#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_split#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sparse_ops.py#L991-L1064)

Split a `SparseTensor` into `num_split` tensors along `axis`. (deprecated arguments)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sparse.split`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/sparse_split)

tf.compat.v1.sparse_split(
        keyword_required=KeywordRequired(),
        sp_input=None,
        num_split=None,
        axis=None,
        name=None,
        split_dim=None
    )

If the `sp_input.dense_shape[axis]` is not an integer multiple of `num_split` each slice starting from 0:`shape[axis] % num_split` gets extra one dimension. For example, if `axis = 1` and `num_split = 2` and the input is:

input_tensor = shape = [2, 7]
    [    a   d e  ]
    [b c          ]

Graphically the output tensors are:

output_tensor[0] =
    [    a   ]
    [b c     ]
    
    output_tensor[1] =
    [ d e  ]
    [      ]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `keyword_required` | Python 2 standin for \* (temporary for argument reorder) |
| `sp_input` | The `SparseTensor` to split. |
| `num_split` | A Python integer. The number of ways to split. |
| `axis` | A 0-D `int32` `Tensor`. The dimension along which to split. Must be in range \[-rank, rank), where rank is the number of dimensions in the input `SparseTensor`. |\
| `name` | A name for the operation (optional). |\
| `split_dim` | Deprecated old name for axis. |\
\
|     |\
| --- |\
| Returns<br>------- |     |\
| `num_split` `SparseTensor` objects resulting from splitting `value`. |     |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `TypeError` | If `sp_input` is not a `SparseTensor`. |\
| `ValueError` | If the deprecated `split_dim` and `axis` are both non None. |\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.