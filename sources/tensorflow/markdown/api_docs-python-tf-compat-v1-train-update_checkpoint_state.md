[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/update_checkpoint_state#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/update_checkpoint_state)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/update_checkpoint_state?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/update_checkpoint_state#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/update_checkpoint_state#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.update\_checkpoint\_state Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/update_checkpoint_state#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/update_checkpoint_state#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/checkpoint_management.py#L129-L172)

Updates the content of the 'checkpoint' file. (deprecated)

tf.compat.v1.train.update_checkpoint_state(
        save_dir,
        model_checkpoint_path,
        all_model_checkpoint_paths=None,
        latest_filename=None,
        all_model_checkpoint_timestamps=None,
        last_preserved_timestamp=None
    )

This updates the checkpoint file containing a CheckpointState proto.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `save_dir` | Directory where the model was saved. |
| `model_checkpoint_path` | The checkpoint file. |
| `all_model_checkpoint_paths` | List of strings. Paths to all not-yet-deleted checkpoints, sorted from oldest to newest. If this is a non-empty list, the last element must be equal to model\_checkpoint\_path. These paths are also saved in the CheckpointState proto. |
| `latest_filename` | Optional name of the checkpoint file. Default to 'checkpoint'. |
| `all_model_checkpoint_timestamps` | Optional list of timestamps (floats, seconds since the Epoch) indicating when the checkpoints in `all_model_checkpoint_paths` were created. |
| `last_preserved_timestamp` | A float, indicating the number of seconds since the Epoch when the last preserved checkpoint was written, e.g. due to a `keep_checkpoint_every_n_hours` parameter (see [`tf.train.CheckpointManager`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager)<br> for an implementation). |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | If any of the model checkpoint paths conflict with the file containing CheckpointSate. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.