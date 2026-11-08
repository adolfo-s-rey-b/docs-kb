[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#migrate-to-tf2)
    *   [How to Rewrite Checkpoints](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#how_to_rewrite_checkpoints)
        
    *   [Checkpoint Management in TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#checkpoint_management_in_tf2)
        
    *   [Writing MetaGraphDefs in TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#writing_metagraphdefs_in_tf2)
        
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#methods)
    *   [as\_saver\_def](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#as_saver_def)
        
    *   [build](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#build)
        
    *   [export\_meta\_graph](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#export_meta_graph)
        
    *   [from\_proto](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#from_proto)
        
    *   [recover\_last\_checkpoints](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#recover_last_checkpoints)
        
    *   [restore](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#restore)
        
    *   [save](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#save)
        
    *   [set\_last\_checkpoints](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#set_last_checkpoints)
        
    *   [set\_last\_checkpoints\_with\_time](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#set_last_checkpoints_with_time)
        
    *   [to\_proto](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#to_proto)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.Saver Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#migrate-to-tf2)
    *   [How to Rewrite Checkpoints](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#how_to_rewrite_checkpoints)
        
    *   [Checkpoint Management in TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#checkpoint_management_in_tf2)
        
    *   [Writing MetaGraphDefs in TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#writing_metagraphdefs_in_tf2)
        
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#methods)
    *   [as\_saver\_def](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#as_saver_def)
        
    *   [build](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#build)
        
    *   [export\_meta\_graph](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#export_meta_graph)
        
    *   [from\_proto](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#from_proto)
        
    *   [recover\_last\_checkpoints](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#recover_last_checkpoints)
        
    *   [restore](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#restore)
        
    *   [save](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#save)
        
    *   [set\_last\_checkpoints](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#set_last_checkpoints)
        
    *   [set\_last\_checkpoints\_with\_time](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#set_last_checkpoints_with_time)
        
    *   [to\_proto](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#to_proto)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/saver.py#L641-L1474)

Saves and restores variables.

tf.compat.v1.train.Saver(
        var_list=None,
        reshape=False,
        sharded=False,
        max_to_keep=5,
        keep_checkpoint_every_n_hours=10000.0,
        name=None,
        restore_sequentially=False,
        saver_def=None,
        builder=None,
        defer_build=False,
        allow_empty=False,
        write_version=saver_pb2.SaverDef.V2,
        pad_step_number=False,
        save_relative_paths=False,
        filename=None
    )

Migrate to TF2
--------------

[`tf.compat.v1.train.Saver`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver)
 is not supported for saving and restoring checkpoints in TF2. Please switch to [`tf.train.Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)
 or [`tf.keras.Model.save_weights`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#save_weights)
, which perform a more robust [object-based saving](https://www.tensorflow.org/guide/checkpoint#loading_mechanics)
.

### How to Rewrite Checkpoints

Please rewrite your checkpoints immediately using the object-based checkpoint APIs.

You can load a name-based checkpoint written by [`tf.compat.v1.train.Saver`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver)
 using [`tf.train.Checkpoint.restore`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#restore)
 or [`tf.keras.Model.load_weights`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#load_weights)
. However, you may have to change the names of the variables in your model to match the variable names in the name-based checkpoint, which can be viewed with [`tf.train.list_variables(path)`](https://www.tensorflow.org/api_docs/python/tf/train/list_variables)
.

Another option is to create an `assignment_map` that maps the name of the variables in the name-based checkpoint to the variables in your model, eg:

{
        'sequential/dense/bias': model.variables[0],
        'sequential/dense/kernel': model.variables[1]
    }

and use [`tf.compat.v1.train.init_from_checkpoint(path, assignment_map)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/init_from_checkpoint)
 to restore the name-based checkpoint.

After restoring, re-encode your checkpoint using [`tf.train.Checkpoint.save`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#save)
 or [`tf.keras.Model.save_weights`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#save_weights)
.

See the [Checkpoint compatibility](https://www.tensorflow.org/guide/migrate#checkpoint_compatibility)
 section of the migration guide for more details.

### Checkpoint Management in TF2

Use [`tf.train.CheckpointManager`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager)
 to manage checkpoints in TF2. [`tf.train.CheckpointManager`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager)
 offers equivalent `keep_checkpoint_every_n_hours` and `max_to_keep` parameters.

To recover the latest checkpoint,

checkpoint = tf.train.Checkpoint(model)
    manager = tf.train.CheckpointManager(checkpoint)
    status = checkpoint.restore(manager.latest_checkpoint)

[`tf.train.CheckpointManager`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager)
 also writes a [`CheckpointState` proto](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/training/checkpoint_state.proto)
 which contains the timestamp when each checkpoint was created.

### Writing `MetaGraphDef`s in TF2

To replace, [`tf.compat.v1.train.Saver.save(write_meta_graph=True)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#save)
, use [`tf.saved_model.save`](https://www.tensorflow.org/api_docs/python/tf/saved_model/save)
 to write the `MetaGraphDef` (which is contained in `saved_model.pb`).

Description
-----------

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Migrating model checkpoints](https://www.tensorflow.org/guide/migrate/migrating_checkpoints)<br>    <br>*   [Migrate the SavedModel workflow](https://www.tensorflow.org/guide/migrate/saved_model) |

See [Variables](https://tensorflow.org/guide/variables)
 for an overview of variables, saving and restoring.

The `Saver` class adds ops to save and restore variables to and from _checkpoints_. It also provides convenience methods to run these ops.

Checkpoints are binary files in a proprietary format which map variable names to tensor values. The best way to examine the contents of a checkpoint is to load it using a `Saver`.

Savers can automatically number checkpoint filenames with a provided counter. This lets you keep multiple checkpoints at different steps while training a model. For example you can number the checkpoint filenames with the training step number. To avoid filling up disks, savers manage checkpoint files automatically. For example, they can keep only the N most recent files, or one checkpoint for every N hours of training.

You number checkpoint filenames by passing a value to the optional `global_step` argument to `save()`:

saver.save(sess, 'my-model', global_step=0) ==> filename: 'my-model-0'
    ...
    saver.save(sess, 'my-model', global_step=1000) ==> filename: 'my-model-1000'

Additionally, optional arguments to the `Saver()` constructor let you control the proliferation of checkpoint files on disk:

*   `max_to_keep` indicates the maximum number of recent checkpoint files to keep. As new files are created, older files are deleted. If None or 0, no checkpoints are deleted from the filesystem but only the last one is kept in the `checkpoint` file. Defaults to 5 (that is, the 5 most recent checkpoint files are kept.)
    
*   `keep_checkpoint_every_n_hours`: In addition to keeping the most recent `max_to_keep` checkpoint files, you might want to keep one checkpoint file for every N hours of training. This can be useful if you want to later analyze how a model progressed during a long training session. For example, passing `keep_checkpoint_every_n_hours=2` ensures that you keep one checkpoint file for every 2 hours of training. The default value of 10,000 hours effectively disables the feature.
    

Note that you still have to call the `save()` method to save the model. Passing these arguments to the constructor will not save variables automatically for you.

A training program that saves regularly looks like:

...
    # Create a saver.
    saver = tf.compat.v1.train.Saver(...variables...)
    # Launch the graph and train, saving the model every 1,000 steps.
    sess = tf.compat.v1.Session()
    for step in range(1000000):
        sess.run(..training_op..)
        if step % 1000 == 0:
            # Append the step number to the checkpoint name:
            saver.save(sess, 'my-model', global_step=step)

In addition to checkpoint files, savers keep a protocol buffer on disk with the list of recent checkpoints. This is used to manage numbered checkpoint files and by `latest_checkpoint()`, which makes it easy to discover the path to the most recent checkpoint. That protocol buffer is stored in a file named 'checkpoint' next to the checkpoint files.

If you create several savers, you can specify a different filename for the protocol buffer file in the call to `save()`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `var_list` | A list of `Variable`/`SaveableObject`, or a dictionary mapping names to `SaveableObject`s. If `None`, defaults to the list of all saveable objects. |
| `reshape` | If `True`, allows restoring parameters from a checkpoint where the variables have a different shape. |
| `sharded` | If `True`, shard the checkpoints, one per device. |
| `max_to_keep` | Maximum number of recent checkpoints to keep. Defaults to 5. |
| `keep_checkpoint_every_n_hours` | How often to keep checkpoints. Defaults to 10,000 hours. |
| `name` | String. Optional name to use as a prefix when adding operations. |
| `restore_sequentially` | A `Bool`, which if true, causes restore of different variables to happen sequentially within each device. This can lower memory usage when restoring very large models. |
| `saver_def` | Optional `SaverDef` proto to use instead of running the builder. This is only useful for specialty code that wants to recreate a `Saver` object for a previously built `Graph` that had a `Saver`. The `saver_def` proto should be the one returned by the `as_saver_def()` call of the `Saver` that was created for that `Graph`. |
| `builder` | Optional `SaverBuilder` to use if a `saver_def` was not provided. Defaults to `BulkSaverBuilder()`. |
| `defer_build` | If `True`, defer adding the save and restore ops to the `build()` call. In that case `build()` should be called before finalizing the graph or using the saver. |
| `allow_empty` | If `False` (default) raise an error if there are no variables in the graph. Otherwise, construct the saver anyway and make it a no-op. |
| `write_version` | controls what format to use when saving checkpoints. It also affects certain filepath matching logic. The V2 format is the recommended choice: it is much more optimized than V1 in terms of memory required and latency incurred during restore. Regardless of this flag, the Saver is able to restore from both V2 and V1 checkpoints. |
| `pad_step_number` | if True, pads the global step number in the checkpoint filepaths to some fixed width (8 by default). This is turned off by default. |
| `save_relative_paths` | If `True`, will write relative paths to the checkpoint state file. This is needed if the user wants to copy the checkpoint directory and reload from the copied directory. |
| `filename` | If known at graph construction time, filename used for variable loading/saving. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If `var_list` is invalid. |
| `ValueError` | If any of the keys or values in `var_list` are not unique. |
| `RuntimeError` | If eager execution is enabled and`var_list` does not specify a list of variables to save. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `last_checkpoints` | List of not-yet-deleted checkpoint filenames.<br><br>You can pass any of the returned values to `restore()`. |

Methods
-------

### `as_saver_def`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/saver.py#L1074-L1080)

as_saver_def()

Generates a `SaverDef` representation of this saver.

|     |
| --- |
| Returns |     |
| A `SaverDef` proto. |     |

### `build`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/saver.py#L943-L946)

build()

### `export_meta_graph`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/saver.py#L1339-L1386)

export_meta_graph(
        filename=None,
        collection_list=None,
        as_text=False,
        export_scope=None,
        clear_devices=False,
        clear_extraneous_savers=False,
        strip_default_attrs=False,
        save_debug_info=False
    )

Writes `MetaGraphDef` to save\_path/filename.

|     |     |
| --- | --- |
| Args |     |
| `filename` | Optional meta\_graph filename including the path. |
| `collection_list` | List of string keys to collect. |
| `as_text` | If `True`, writes the meta\_graph as an ASCII proto. |
| `export_scope` | Optional `string`. Name scope to remove. |
| `clear_devices` | Whether or not to clear the device field for an `Operation` or `Tensor` during export. |
| `clear_extraneous_savers` | Remove any Saver-related information from the graph (both Save/Restore ops and SaverDefs) that are not associated with this Saver. |
| `strip_default_attrs` | Boolean. If `True`, default-valued attributes will be removed from the NodeDefs. For a detailed guide, see [Stripping Default-Valued Attributes](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes)<br>. |
| `save_debug_info` | If `True`, save the GraphDebugInfo to a separate file, which in the same directory of filename and with `_debug` added before the file extension. |

|     |
| --- |
| Returns |     |
| A `MetaGraphDef` proto. |     |

### `from_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/saver.py#L1109-L1120)

@staticmethod

Returns a `Saver` object created from `saver_def`.

|     |     |
| --- | --- |
| Args |     |
| `saver_def` | a `SaverDef` protocol buffer. |
| `import_scope` | Optional `string`. Name scope to use. |

|     |
| --- |
| Returns |     |
| A `Saver` built from saver\_def. |     |

### `recover_last_checkpoints`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/saver.py#L1163-L1184)

recover_last_checkpoints(
        checkpoint_paths
    )

Recovers the internal saver state after a crash.

This method is useful for recovering the "self.\_last\_checkpoints" state.

Globs for the checkpoints pointed to by `checkpoint_paths`. If the files exist, use their mtime as the checkpoint timestamp.

|     |     |
| --- | --- |
| Args |     |
| `checkpoint_paths` | a list of checkpoint paths. |

### `restore`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/saver.py#L1388-L1462)

restore(
        sess, save_path
    )

Restores previously saved variables.

This method runs the ops added by the constructor for restoring variables. It requires a session in which the graph was launched. The variables to restore do not have to have been initialized, as restoring is itself a way to initialize variables.

The `save_path` argument is typically a value previously returned from a `save()` call, or a call to `latest_checkpoint()`.

|     |     |
| --- | --- |
| Args |     |
| `sess` | A `Session` to use to restore the parameters. None in eager mode. |
| `save_path` | Path where parameters were previously saved. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If save\_path is None or not a valid checkpoint. |

### `save`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/saver.py#L1186-L1337)

save(
        sess,
        save_path,
        global_step=None,
        latest_filename=None,
        meta_graph_suffix='meta',
        write_meta_graph=True,
        write_state=True,
        strip_default_attrs=False,
        save_debug_info=False
    )

Saves variables.

This method runs the ops added by the constructor for saving variables. It requires a session in which the graph was launched. The variables to save must also have been initialized.

The method returns the path prefix of the newly created checkpoint files. This string can be passed directly to a call to `restore()`.

|     |     |
| --- | --- |
| Args |     |
| `sess` | A Session to use to save the variables. |
| `save_path` | String. Prefix of filenames created for the checkpoint. |
| `global_step` | If provided the global step number is appended to `save_path` to create the checkpoint filenames. The optional argument can be a `Tensor`, a `Tensor` name or an integer. |
| `latest_filename` | Optional name for the protocol buffer file that will contains the list of most recent checkpoints. That file, kept in the same directory as the checkpoint files, is automatically managed by the saver to keep track of recent checkpoints. Defaults to 'checkpoint'. |
| `meta_graph_suffix` | Suffix for `MetaGraphDef` file. Defaults to 'meta'. |
| `write_meta_graph` | `Boolean` indicating whether or not to write the meta graph file. |
| `write_state` | `Boolean` indicating whether or not to write the `CheckpointStateProto`. |
| `strip_default_attrs` | Boolean. If `True`, default-valued attributes will be removed from the NodeDefs. For a detailed guide, see [Stripping Default-Valued Attributes](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes)<br>. |
| `save_debug_info` | If `True`, save the GraphDebugInfo to a separate file, which in the same directory of save\_path and with `_debug` added before the file extension. This is only enabled when `write_meta_graph` is `True` |

|     |
| --- |
| Returns |     |
| A string: path prefix used for the checkpoint files. If the saver is sharded, this string ends with: '-?????-of-nnnnn' where 'nnnnn' is the number of shards created. If the saver is empty, returns None. |     |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | If `sess` is not a `Session`. |
| `ValueError` | If `latest_filename` contains path components, or if it collides with `save_path`. |
| `RuntimeError` | If save and restore ops weren't built. |

### `set_last_checkpoints`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/saver.py#L1133-L1148)

set_last_checkpoints(
        last_checkpoints
    )

Sets the list of old checkpoint filenames.

|     |     |
| --- | --- |
| Args |     |
| `last_checkpoints` | A list of checkpoint filenames. |

|     |     |
| --- | --- |
| Raises |     |
| `AssertionError` | If last\_checkpoints is not a list. |

### `set_last_checkpoints_with_time`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/saver.py#L1150-L1161)

set_last_checkpoints_with_time(
        last_checkpoints_with_time
    )

Sets the list of old checkpoint filenames and timestamps.

|     |     |
| --- | --- |
| Args |     |
| `last_checkpoints_with_time` | A list of tuples of checkpoint filenames and timestamps. |

|     |     |
| --- | --- |
| Raises |     |
| `AssertionError` | If last\_checkpoints\_with\_time is not a list. |

### `to_proto`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/saver.py#L1082-L1107)

to_proto(
        export_scope=None
    )

Converts this `Saver` to a `SaverDef` protocol buffer.

|     |     |
| --- | --- |
| Args |     |
| `export_scope` | Optional `string`. Name scope to remove. |

|     |
| --- |
| Returns |     |
| A `SaverDef` protocol buffer. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.