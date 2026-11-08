[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/name_based_restore#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/name_based_restore)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/name_based_restore?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fexperimental%2Fdtensor%2Fname_based_restore&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/name_based_restore#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/name_based_restore#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.dtensor.name\_based\_restore Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/name_based_restore#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/name_based_restore#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/save_restore.py#L100-L173)

Restores from checkpoint\_prefix to name based DTensors.

tf.experimental.dtensor.name_based_restore(
        mesh: tf.experimental.dtensor.Mesh,
        checkpoint_prefix: str,
        name_tensor_dict: Dict[str, Union[tensor_lib.Tensor, tf_variables.Variable]]
    )

It is required to have already-initialized DTensor variables that have same shape/dtype for the tensors being restored.

Also, we currently only support a named based restore on a single mesh.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `mesh` | The single mesh that all Tensors would be restored to. |
| `checkpoint_prefix` | The prefix of checkpoint to be restored. |
| `name_tensor_dict` | A ordered dictionary of tensor\_names to a DTensor. The DTensor shape/dtype must match the tensors being saved/restored for now. |

|     |
| --- |
| Returns<br>------- |     |
| A dictionary of name to its restored DTensor value. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.