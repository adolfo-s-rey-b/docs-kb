[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/sharded_save#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/sharded_save)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/sharded_save?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/sharded_save#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/sharded_save#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.dtensor.sharded\_save Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/sharded_save#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/sharded_save#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/save_restore.py#L34-L80)

Saves given named tensor slices in a sharded, multi-client safe fashion.

tf.experimental.dtensor.sharded_save(
        mesh: tf.experimental.dtensor.Mesh,
        file_prefix: Union[str, tf.Tensor],
        tensor_names: Union[List[str], tf.Tensor],
        shape_and_slices: Union[List[str], tf.Tensor],
        tensors: List[Union[tensor_lib.Tensor, tf_variables.Variable]]
    )

The method makes sure the checkpoint directory state is correct in a sharded mutli-client saving. Namely, we place a barrier after SaveV2 to make sure every client has done writing the files. And another one after MergeV2Checkpoints to make sure all Metadata is properly merged.

Upon existing, the checkpoint is completed and the all directory operations are done.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `mesh` | The Mesh that contains the Tensors to save. |
| `file_prefix` | The prefix of checkpoint. |
| `tensor_names` | a list of tensor names used in save op. |
| `shape_and_slices` | a list of shape and slice specification used in save op. The only supported value is "" as we don't support distributed saving with slices yet. |
| `tensors` | a list of tensors used in save op. The order should match tensor\_names. |

|     |
| --- |
| Returns<br>------- |     |
| A MergeV2Checkpoints op that merged all Metadata. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.