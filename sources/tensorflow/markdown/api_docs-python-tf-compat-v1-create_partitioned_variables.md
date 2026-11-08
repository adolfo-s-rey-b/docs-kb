[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/create_partitioned_variables#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/create_partitioned_variables)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/create_partitioned_variables?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/create_partitioned_variables#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/create_partitioned_variables#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/create_partitioned_variables#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.create\_partitioned\_variables Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/create_partitioned_variables#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/create_partitioned_variables#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/create_partitioned_variables#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/partitioned_variables.py#L275-L347)

Create a list of partitioned variables according to the given `slicing`. (deprecated)

tf.compat.v1.create_partitioned_variables(
        shape,
        slicing,
        initializer,
        dtype=tf.dtypes.float32,
        trainable=True,
        collections=None,
        name=None,
        reuse=None
    )

Currently only one dimension of the full variable can be sliced, and the full variable can be reconstructed by the concatenation of the returned list along that dimension.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `shape` | List of integers. The shape of the full variable. |
| `slicing` | List of integers. How to partition the variable. Must be of the same length as `shape`. Each value indicate how many slices to create in the corresponding dimension. Presently only one of the values can be more than 1; that is, the variable can only be sliced along one dimension.<br><br>For convenience, The requested number of partitions does not have to divide the corresponding dimension evenly. If it does not, the shapes of the partitions are incremented by 1 starting from partition 0 until all slack is absorbed. The adjustment rules may change in the future, but as you can save/restore these variables with different slicing specifications this should not be a problem. |
| `initializer` | A `Tensor` of shape `shape` or a variable initializer function. If a function, it will be called once for each slice, passing the shape and data type of the slice as parameters. The function must return a tensor with the same shape as the slice. |
| `dtype` | Type of the variables. Ignored if `initializer` is a `Tensor`. |
| `trainable` | If True also add all the variables to the graph collection `GraphKeys.TRAINABLE_VARIABLES`. |
| `collections` | List of graph collections keys to add the variables to. Defaults to `[GraphKeys.GLOBAL_VARIABLES]`. |
| `name` | Optional name for the full variable. Defaults to `"PartitionedVariable"` and gets uniquified automatically. |
| `reuse` | Boolean or `None`; if `True` and name is set, it would reuse previously created variables. if `False` it will create new variables. if `None`, it would inherit the parent scope reuse. |

|     |
| --- |
| Returns<br>------- |     |
| A list of Variables corresponding to the slicing. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If any of the arguments is malformed. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.