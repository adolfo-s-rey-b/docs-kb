[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sparse/bincount#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sparse/bincount)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sparse/bincount?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsparse%2Fbincount&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/bincount#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/bincount#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sparse/bincount#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sparse.bincount Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sparse/bincount#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sparse/bincount#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sparse/bincount#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/sparse_ops.py#L3205-L3412)

Count the number of times an integer value appears in a tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sparse.bincount`](https://www.tensorflow.org/api_docs/python/tf/sparse/bincount)

tf.sparse.bincount(
        values,
        weights=None,
        axis=0,
        minlength=None,
        maxlength=None,
        binary_output=False,
        name=None
    )

This op takes an N-dimensional `Tensor`, `RaggedTensor`, or `SparseTensor`, and returns an N-dimensional int64 SparseTensor where element `[i0...i[axis], j]` contains the number of times the value `j` appears in slice `[i0...i[axis], :]` of the input tensor. Currently, only N=0 and N=-1 are supported.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `values` | A Tensor, RaggedTensor, or SparseTensor whose values should be counted. These tensors must have a rank of 2 if `axis=-1`. |
| `weights` | If non-None, must be the same shape as `arr`. If `arr` is a SparseTensor, `weights` must be a SparseTensor with the same dense shape and same indices as `arr`. For each value in `value`, the bin will be incremented by the corresponding weight instead of 1. |
| `axis` | The axis to slice over. Axes at and below `axis` will be flattened before bin counting. Currently, only `0`, and `-1` are supported. If None, all axes will be flattened (identical to passing `0`). |
| `minlength` | If given, ensures the output has length at least `minlength`, padding with zeros at the end if necessary. |
| `maxlength` | If given, skips values in `values` that are equal or greater than `maxlength`, ensuring that the output has length at most `maxlength`. |
| `binary_output` | If True, this op will output 1 instead of the number of times a token appears (equivalent to one\_hot + reduce\_any instead of one\_hot + reduce\_add). Defaults to False. |
| `name` | A name for this op. |

|     |
| --- |
| Returns<br>------- |     |
| A SparseTensor with `output.shape = values.shape[:axis] + [N]`, where `N` is<br><br>*   `maxlength` (if set);<br>*   `minlength` (if set, and `minlength > reduce_max(values)`);<br>*   `0` (if `values` is empty);<br>*   `reduce_max(values) + 1` otherwise. |     |

|     |
| --- |
| Raises<br>------ |     |
| `InvalidArgumentError` if negative values are provided as an input. |     |

#### Examples:

**Bin-counting every item in individual batches**

This example takes an input (which could be a Tensor, RaggedTensor, or SparseTensor) and returns a SparseTensor where the value of (i,j) is the number of times value j appears in batch i.

    data = np.array([[10, 20, 30, 20], [11, 101, 11, 10001]], dtype=np.int64)

This example shows a sparse tensor input. Missing zeros are not counted.

    data = tf.sparse.SparseTensor(

**Bin-counting with defined output shape**

This example takes an input (which could be a Tensor, RaggedTensor, or SparseTensor) and returns a SparseTensor where the value of (i,j) is the number of times value j appears in batch i. However, all values of j above 'maxlength' are ignored. The dense\_shape of the output sparse tensor is set to 'minlength'. Note that, while the input is identical to the example above, the value '10001' in batch item 2 is dropped, and the dense shape is \[2, 500\] instead of \[2,10002\] or \[2, 102\].

    minlength = maxlength = 500

**Binary bin-counting**

This example takes an input (which could be a Tensor, RaggedTensor, or SparseTensor) and returns a SparseTensor where (i,j) is 1 if the value j appears in batch i at least once and is 0 otherwise. Note that, even though some values (like 20 in batch 1 and 11 in batch 2) appear more than once, the 'values' tensor is all 1s.

    data = np.array([[10, 20, 30, 20], [11, 101, 11, 10001]], dtype=np.int64)

**Weighted bin-counting**

This example takes two inputs - a values tensor and a weights tensor. These tensors must be identically shaped, and have the same row splits or indices in the case of RaggedTensors or SparseTensors. When performing a weighted count, the op will output a SparseTensor where the value of (i, j) is the sum of the values in the weight tensor's batch i in the locations where the values tensor has the value j. In this case, the output dtype is the same as the dtype of the weights tensor.

    data = np.array([[10, 20, 30, 20], [11, 101, 11, 10001]], dtype=np.int64)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.