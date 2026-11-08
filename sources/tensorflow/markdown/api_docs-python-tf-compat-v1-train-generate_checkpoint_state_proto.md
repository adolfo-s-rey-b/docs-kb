[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/generate_checkpoint_state_proto#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/generate_checkpoint_state_proto)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/generate_checkpoint_state_proto?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/generate_checkpoint_state_proto#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/generate_checkpoint_state_proto#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/generate_checkpoint_state_proto#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.generate\_checkpoint\_state\_proto Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/generate_checkpoint_state_proto#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/generate_checkpoint_state_proto#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/generate_checkpoint_state_proto#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/checkpoint_management.py#L64-L126)

Generates a checkpoint state proto.

tf.compat.v1.train.generate_checkpoint_state_proto(
        save_dir,
        model_checkpoint_path,
        all_model_checkpoint_paths=None,
        all_model_checkpoint_timestamps=None,
        last_preserved_timestamp=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `save_dir` | Directory where the model was saved. |
| `model_checkpoint_path` | The checkpoint file. |
| `all_model_checkpoint_paths` | List of strings. Paths to all not-yet-deleted checkpoints, sorted from oldest to newest. If this is a non-empty list, the last element must be equal to model\_checkpoint\_path. These paths are also saved in the CheckpointState proto. |
| `all_model_checkpoint_timestamps` | A list of floats, indicating the number of seconds since the Epoch when each checkpoint was generated. |
| `last_preserved_timestamp` | A float, indicating the number of seconds since the Epoch when the last preserved checkpoint was written, e.g. due to a `keep_checkpoint_every_n_hours` parameter (see [`tf.train.CheckpointManager`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager)<br> for an implementation). |

|     |
| --- |
| Returns<br>------- |     |
| CheckpointState proto with model\_checkpoint\_path and all\_model\_checkpoint\_paths updated to either absolute paths or relative paths to the current save\_dir. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `all_model_checkpoint_timestamps` was provided but its length does not match `all_model_checkpoint_paths`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.