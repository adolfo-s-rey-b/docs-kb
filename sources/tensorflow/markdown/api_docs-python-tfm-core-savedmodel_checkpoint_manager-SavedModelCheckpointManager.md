[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/savedmodel_checkpoint_manager/SavedModelCheckpointManager#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/savedmodel_checkpoint_manager/SavedModelCheckpointManager)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/savedmodel_checkpoint_manager/SavedModelCheckpointManager?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/core/savedmodel_checkpoint_manager/SavedModelCheckpointManager#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/savedmodel_checkpoint_manager/SavedModelCheckpointManager#methods)
    *   [get\_existing\_savedmodels](https://www.tensorflow.org/api_docs/python/tfm/core/savedmodel_checkpoint_manager/SavedModelCheckpointManager#get_existing_savedmodels)
        
    *   [get\_savedmodel\_number\_from\_path](https://www.tensorflow.org/api_docs/python/tfm/core/savedmodel_checkpoint_manager/SavedModelCheckpointManager#get_savedmodel_number_from_path)
        
    *   [restore\_or\_initialize](https://www.tensorflow.org/api_docs/python/tfm/core/savedmodel_checkpoint_manager/SavedModelCheckpointManager#restore_or_initialize)
        
    *   [save](https://www.tensorflow.org/api_docs/python/tfm/core/savedmodel_checkpoint_manager/SavedModelCheckpointManager#save)
        
    *   [savedmodels\_iterator](https://www.tensorflow.org/api_docs/python/tfm/core/savedmodel_checkpoint_manager/SavedModelCheckpointManager#savedmodels_iterator)
        
    *   [sync](https://www.tensorflow.org/api_docs/python/tfm/core/savedmodel_checkpoint_manager/SavedModelCheckpointManager#sync)
        
    *   [wait\_for\_new\_savedmodel](https://www.tensorflow.org/api_docs/python/tfm/core/savedmodel_checkpoint_manager/SavedModelCheckpointManager#wait_for_new_savedmodel)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.savedmodel\_checkpoint\_manager.SavedModelCheckpointManager Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/core/savedmodel_checkpoint_manager/SavedModelCheckpointManager#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/savedmodel_checkpoint_manager/SavedModelCheckpointManager#methods)
    *   [get\_existing\_savedmodels](https://www.tensorflow.org/api_docs/python/tfm/core/savedmodel_checkpoint_manager/SavedModelCheckpointManager#get_existing_savedmodels)
        
    *   [get\_savedmodel\_number\_from\_path](https://www.tensorflow.org/api_docs/python/tfm/core/savedmodel_checkpoint_manager/SavedModelCheckpointManager#get_savedmodel_number_from_path)
        
    *   [restore\_or\_initialize](https://www.tensorflow.org/api_docs/python/tfm/core/savedmodel_checkpoint_manager/SavedModelCheckpointManager#restore_or_initialize)
        
    *   [save](https://www.tensorflow.org/api_docs/python/tfm/core/savedmodel_checkpoint_manager/SavedModelCheckpointManager#save)
        
    *   [savedmodels\_iterator](https://www.tensorflow.org/api_docs/python/tfm/core/savedmodel_checkpoint_manager/SavedModelCheckpointManager#savedmodels_iterator)
        
    *   [sync](https://www.tensorflow.org/api_docs/python/tfm/core/savedmodel_checkpoint_manager/SavedModelCheckpointManager#sync)
        
    *   [wait\_for\_new\_savedmodel](https://www.tensorflow.org/api_docs/python/tfm/core/savedmodel_checkpoint_manager/SavedModelCheckpointManager#wait_for_new_savedmodel)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/savedmodel_checkpoint_manager.py#L32-L258)

A CheckpointManager that also exports `SavedModel`s.

tfm.core.savedmodel_checkpoint_manager.SavedModelCheckpointManager(
        checkpoint: tf.train.Checkpoint,
        directory: str,
        max_to_keep: int,
        modules_to_export: Optional[Mapping[str, tf.Module]] = None,
        keep_checkpoint_every_n_hours: Optional[int] = None,
        checkpoint_name: str = 'ckpt',
        step_counter: Optional[tf.Variable] = None,
        checkpoint_interval: Optional[int] = None,
        init_fn: Optional[Callable[[], None]] = None
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `checkpoint` | Returns the [`tf.train.Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)<br> object. |
| `checkpoint_interval` |     |
| `checkpoints` | A list of managed checkpoints.<br><br>Note that checkpoints saved due to `keep_checkpoint_every_n_hours` will not show up in this list (to avoid ever-growing filename lists). |
| `directory` |     |
| `latest_checkpoint` | The prefix of the most recent checkpoint in `directory`.<br><br>Equivalent to [`tf.train.latest_checkpoint(directory)`](https://www.tensorflow.org/api_docs/python/tf/train/latest_checkpoint)<br> where `directory` is the constructor argument to `CheckpointManager`.<br><br>Suitable for passing to [`tf.train.Checkpoint.restore`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#restore)<br> to resume training. |
| `latest_savedmodel` | The path of the most recent SavedModel in `directory`. |
| `modules_to_export` |     |
| `savedmodels` | A list of managed SavedModels. |

Methods
-------

### `get_existing_savedmodels`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/savedmodel_checkpoint_manager.py#L106-L121)

get_existing_savedmodels() -> List[str]

Gets a list of all existing SavedModel paths in `directory`.

|     |
| --- |
| Returns |     |
| A list of all existing SavedModel paths. |     |

### `get_savedmodel_number_from_path`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/savedmodel_checkpoint_manager.py#L147-L164)

get_savedmodel_number_from_path(
        savedmodel_path: str
    ) -> Union[int, None]

Gets the savedmodel\_number/checkpoint\_number from savedmodel filepath.

The savedmodel\_number is global step when using with orbit controller.

|     |     |
| --- | --- |
| Args |     |
| `savedmodel_path` | savedmodel directory path. |

|     |
| --- |
| Returns |     |
| Savedmodel number or None if no matched pattern found in savedmodel path. |     |

### `restore_or_initialize`

restore_or_initialize()

Restore items in `checkpoint` from the latest checkpoint file.

This method will first try to restore from the most recent checkpoint in `directory`. If no checkpoints exist in `directory`, and `init_fn` is specified, this method will call `init_fn` to do customized initialization. This can be used to support initialization from pretrained models.

Note that unlike [`tf.train.Checkpoint.restore()`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#restore)
, this method doesn't return a load status object that users can run assertions on (e.g. assert\_consumed()). Thus to run assertions, users should directly use [`tf.train.Checkpoint.restore()`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#restore)
 method.

|     |
| --- |
| Returns |     |
| The restored checkpoint path if the latest checkpoint is found and restored. Otherwise None. |     |

### `save`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/savedmodel_checkpoint_manager.py#L58-L104)

save(
        checkpoint_number: Optional[int] = None,
        check_interval: bool = True,
        options: Optional[tf.train.CheckpointOptions] = None
    )

See base class.

### `savedmodels_iterator`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/savedmodel_checkpoint_manager.py#L166-L207)

savedmodels_iterator(
        min_interval_secs: float = 0,
        timeout: Optional[float] = None,
        timeout_fn: Optional[Callable[[], bool]] = None
    )

Continuously yield new SavedModel files as they appear.

The iterator only checks for new savedmodels when control flow has been reverted to it. The logic is same to the [`train.checkpoints_iterator`](https://www.tensorflow.org/api_docs/python/tf/train/checkpoints_iterator)
.

|     |     |
| --- | --- |
| Args |     |
| `min_interval_secs` | The minimum number of seconds between yielding savedmodels. |
| `timeout` | The maximum number of seconds to wait between savedmodels. If left as `None`, then the process will wait indefinitely. |
| `timeout_fn` | Optional function to call after a timeout. If the function returns True, then it means that no new savedmodels will be generated and the iterator will exit. The function is called with no arguments. |

|     |
| --- |
| Yields |     |
| String paths to latest SavedModel files as they arrive. |     |

### `sync`

sync()

Wait for any outstanding save or restore operations.

### `wait_for_new_savedmodel`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/savedmodel_checkpoint_manager.py#L209-L258)

wait_for_new_savedmodel(
        last_savedmodel: Optional[str] = None,
        seconds_to_sleep: float = 1.0,
        timeout: Optional[float] = None
    ) -> Union[str, None]

Waits until a new savedmodel file is found.

|     |     |
| --- | --- |
| Args |     |
| `last_savedmodel` | The last savedmodel path used or `None` if we're expecting a savedmodel for the first time. |
| `seconds_to_sleep` | The number of seconds to sleep for before looking for a new savedmodel. |
| `timeout` | The maximum number of seconds to wait. If left as `None`, then the process will wait indefinitely. |

|     |
| --- |
| Returns |     |
| A new savedmodel path, or None if the timeout was reached. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.