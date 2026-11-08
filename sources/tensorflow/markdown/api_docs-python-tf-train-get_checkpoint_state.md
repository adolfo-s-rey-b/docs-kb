[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/train/get_checkpoint_state#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/train/get_checkpoint_state)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/train/get_checkpoint_state?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/get_checkpoint_state#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/train/get_checkpoint_state#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/train/get_checkpoint_state#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.train.get\_checkpoint\_state Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/get_checkpoint_state#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/train/get_checkpoint_state#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/train/get_checkpoint_state#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/checkpoint_management.py#L250-L306)

Returns CheckpointState proto from the "checkpoint" file.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.get_checkpoint_state`](https://www.tensorflow.org/api_docs/python/tf/train/get_checkpoint_state)

tf.train.get_checkpoint_state(
        checkpoint_dir, latest_filename=None
    )

If the "checkpoint" file contains a valid CheckpointState proto, returns it.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `checkpoint_dir` | The directory of checkpoints. |
| `latest_filename` | Optional name of the checkpoint file. Default to 'checkpoint'. |

|     |
| --- |
| Returns<br>------- |     |
| A CheckpointState if the state was available, None otherwise. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if the checkpoint read doesn't have model\_checkpoint\_path set. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.