[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/utils/cross_replica_concat#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/utils/cross_replica_concat)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/utils/cross_replica_concat?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Futils%2Fcross_replica_concat&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/utils/cross_replica_concat#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/utils/cross_replica_concat#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/utils/cross_replica_concat#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.utils.cross\_replica\_concat Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/utils/cross_replica_concat#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/utils/cross_replica_concat#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/utils/cross_replica_concat#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/tf_utils.py#L225-L283)

Concatenates the given `value` across (GPU/TPU) cores, along `axis`.

tfm.utils.cross_replica_concat(
        value, axis, name='cross_replica_concat'
    )

In general, each core ("replica") will pass a replica-specific value as `value` (corresponding to some element of a data-parallel computation taking place across replicas).

The resulting concatenated `Tensor` will have the same shape as `value` for all dimensions except `axis`, where it will be larger by a factor of the number of replicas. It will also have the same `dtype` as `value`.

The position of a given replica's `value` within the resulting concatenation is determined by that replica's replica ID. For example:

With `value` for replica 0 given as

0 0 0
    0 0 0

and `value` for replica 1 given as

1 1 1
    1 1 1

the resulting concatenation along axis 0 will be

0 0 0
    0 0 0
    1 1 1
    1 1 1

and this result will be identical across all replicas.

Note that this API only works in TF2 with [`tf.distribute`](https://www.tensorflow.org/api_docs/python/tf/distribute)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `value` | The `Tensor` to concatenate across replicas. Each replica will have a different value for this `Tensor`, and these replica-specific values will be concatenated. |
| `axis` | The axis along which to perform the concatenation as a Python integer (not a `Tensor`). E.g., `axis=0` to concatenate along the batch dimension. |
| `name` | A name for the operation (used to create a name scope). |

|     |
| --- |
| Returns<br>------- |     |
| The result of concatenating `value` along `axis` across replicas. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | when the batch (0-th) dimension is None. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.