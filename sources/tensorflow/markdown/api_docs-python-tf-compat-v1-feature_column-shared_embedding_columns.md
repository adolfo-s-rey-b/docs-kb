[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/shared_embedding_columns#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/shared_embedding_columns)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/shared_embedding_columns?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/shared_embedding_columns#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/shared_embedding_columns#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/shared_embedding_columns#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.feature\_column.shared\_embedding\_columns Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/shared_embedding_columns#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/shared_embedding_columns#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/feature_column/shared_embedding_columns#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/feature_column/feature_column_v2.py#L518-L672)

List of dense columns that convert from sparse, categorical input. (deprecated)

tf.compat.v1.feature_column.shared_embedding_columns(
        categorical_columns,
        dimension,
        combiner='mean',
        initializer=None,
        shared_embedding_collection_name=None,
        ckpt_to_load_from=None,
        tensor_name_in_ckpt=None,
        max_norm=None,
        trainable=True,
        use_safe_embedding_lookup=True
    )

This is similar to `embedding_column`, except that it produces a list of embedding columns that share the same embedding weights.

Use this when your inputs are sparse and of the same type (e.g. watched and impression video IDs that share the same vocabulary), and you want to convert them to a dense representation (e.g., to feed to a DNN).

Inputs must be a list of categorical columns created by any of the `categorical_column_*` function. They must all be of the same type and have the same arguments except `key`. E.g. they can be categorical\_column\_with\_vocabulary\_file with the same vocabulary\_file. Some or all columns could also be weighted\_categorical\_column.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `categorical_columns` | List of categorical columns created by a `categorical_column_with_*` function. These columns produce the sparse IDs that are inputs to the embedding lookup. All columns must be of the same type and have the same arguments except `key`. E.g. they can be categorical\_column\_with\_vocabulary\_file with the same vocabulary\_file. Some or all columns could also be weighted\_categorical\_column. |
| `dimension` | An integer specifying dimension of the embedding, must be > 0. |
| `combiner` | A string specifying how to reduce if there are multiple entries in a single row. Currently 'mean', 'sqrtn' and 'sum' are supported, with 'mean' the default. 'sqrtn' often achieves good accuracy, in particular with bag-of-words columns. Each of this can be thought as example level normalizations on the column. For more information, see `tf.embedding_lookup_sparse`. |
| `initializer` | A variable initializer function to be used in embedding variable initialization. If not specified, defaults to `truncated_normal_initializer` with mean `0.0` and standard deviation `1/sqrt(dimension)`. |
| `shared_embedding_collection_name` | Optional name of the collection where shared embedding weights are added. If not given, a reasonable name will be chosen based on the names of `categorical_columns`. This is also used in `variable_scope` when creating shared embedding weights. |
| `ckpt_to_load_from` | String representing checkpoint name/pattern from which to restore column weights. Required if `tensor_name_in_ckpt` is not `None`. |
| `tensor_name_in_ckpt` | Name of the `Tensor` in `ckpt_to_load_from` from which to restore the column weights. Required if `ckpt_to_load_from` is not `None`. |
| `max_norm` | If not `None`, each embedding is clipped if its l2-norm is larger than this value, before combining. |
| `trainable` | Whether or not the embedding is trainable. Default is True. |
| `use_safe_embedding_lookup` | If true, uses safe\_embedding\_lookup\_sparse instead of embedding\_lookup\_sparse. safe\_embedding\_lookup\_sparse ensures there are no empty rows and all weights and ids are positive at the expense of extra compute cost. This only applies to rank 2 (NxM) shaped input tensors. Defaults to true, consider turning off if the above checks are not needed. Note that having empty rows will not trigger any error though the output result might be 0 or omitted. |

|     |
| --- |
| Returns<br>------- |     |
| A list of dense columns that converts from sparse input. The order of results follows the ordering of `categorical_columns`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if `dimension` not > 0. |
| `ValueError` | if any of the given `categorical_columns` is of different type or has different arguments than the others. |
| `ValueError` | if exactly one of `ckpt_to_load_from` and `tensor_name_in_ckpt` is specified. |
| `ValueError` | if `initializer` is specified and is not callable. |
| `RuntimeError` | if eager execution is enabled. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.