[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SaverDef#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SaverDef)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SaverDef?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Ftrain%2FSaverDef&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SaverDef#attributes)
    
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SaverDef#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.SaverDef Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SaverDef#attributes)
    
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/SaverDef#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/core/protobuf/saver.proto)

A ProtocolMessage

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `filename_tensor_name` | `string filename_tensor_name` |
| `keep_checkpoint_every_n_hours` | `float keep_checkpoint_every_n_hours` |
| `max_to_keep` | `int32 max_to_keep` |
| `restore_op_name` | `string restore_op_name` |
| `save_tensor_name` | `string save_tensor_name` |
| `sharded` | `bool sharded` |
| `version` | `CheckpointFormatVersion version` |

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| V2  | `2` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.