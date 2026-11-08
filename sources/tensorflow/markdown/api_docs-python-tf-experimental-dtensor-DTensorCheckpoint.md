[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DTensorCheckpoint#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DTensorCheckpoint)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DTensorCheckpoint?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DTensorCheckpoint#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DTensorCheckpoint#methods)
    *   [read](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DTensorCheckpoint#read)
        
    *   [restore](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DTensorCheckpoint#restore)
        
    *   [save](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DTensorCheckpoint#save)
        
    *   [sync](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DTensorCheckpoint#sync)
        
    *   [write](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DTensorCheckpoint#write)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.dtensor.DTensorCheckpoint Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DTensorCheckpoint#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DTensorCheckpoint#methods)
    *   [read](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DTensorCheckpoint#read)
        
    *   [restore](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DTensorCheckpoint#restore)
        
    *   [save](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DTensorCheckpoint#save)
        
    *   [sync](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DTensorCheckpoint#sync)
        
    *   [write](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/DTensorCheckpoint#write)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/dtensor/python/d_checkpoint.py#L407-L463)

Manages saving/restoring trackable values to disk, for DTensor. (deprecated)

Inherits From: [`Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)

tf.experimental.dtensor.DTensorCheckpoint(
        mesh: tf.experimental.dtensor.Mesh,
        root=None,
        **kwargs
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `save_counter` | An integer variable which starts at zero and is incremented on save.<br><br>Used to number checkpoints. |

Methods
-------

### `read`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/checkpoint.py#L2537-L2599)

read(
        save_path, options=None
    )

Reads a training checkpoint written with `write`.

Reads this `Checkpoint` and any objects it depends on.

This method is just like `restore()` but does not expect the `save_counter` variable in the checkpoint. It only restores the objects that the checkpoint already depends on.

The method is primarily intended for use by higher level checkpoint management utilities that use `write()` instead of `save()` and have their own mechanisms to number and track checkpoints.

#### Example usage:

# Create a checkpoint with write()
    ckpt = tf.train.Checkpoint(v=tf.Variable(1.))
    path = ckpt.write('/tmp/my_checkpoint')
    
    # Later, load the checkpoint with read()
    # With restore() assert_consumed() would have failed.
    checkpoint.read(path).assert_consumed()
    
    # You can also pass options to read(). For example this
    # runs the IO ops on the localhost:
    options = tf.train.CheckpointOptions(
        experimental_io_device="/job:localhost")
    checkpoint.read(path, options=options)

|     |     |
| --- | --- |
| Args |     |
| `save_path` | The path to the checkpoint as returned by `write`. |
| `options` | Optional [`tf.train.CheckpointOptions`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointOptions)<br> object. |

|     |
| --- |
| Returns |     |
| A load status object, which can be used to make assertions about the status of a checkpoint restoration. See `restore` for details. |     |

### `restore`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/checkpoint.py#L2601-L2748)

restore(
        save_path, options=None
    )

Restores a training checkpoint.

Restores this `Checkpoint` and any objects it depends on.

This method is intended to be used to load checkpoints created by `save()`. For checkpoints created by `write()` use the `read()` method which does not expect the `save_counter` variable added by `save()`.

`restore()` either assigns values immediately if variables to restore have been created already, or defers restoration until the variables are created. Dependencies added after this call will be matched if they have a corresponding object in the checkpoint (the restore request will queue in any trackable object waiting for the expected dependency to be added).

checkpoint = tf.train.Checkpoint( ... )
    checkpoint.restore(path)
    
    # You can additionally pass options to restore():
    options = tf.CheckpointOptions(experimental_io_device="/job:localhost")
    checkpoint.restore(path, options=options)

To ensure that loading is complete and no more deferred restorations will take place, use the `assert_consumed()` method of the status object returned by `restore()`:

checkpoint.restore(path, options=options).assert_consumed()

The assert will raise an error if any Python objects in the dependency graph were not found in the checkpoint, or if any checkpointed values do not have a matching Python object.

Name-based [`tf.compat.v1.train.Saver`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver)
 checkpoints from TensorFlow 1.x can be loaded using this method. Names are used to match variables. Re-encode name-based checkpoints using [`tf.train.Checkpoint.save`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#save)
 as soon as possible.

**Loading from SavedModel checkpoints**

To load values from a SavedModel, just pass the SavedModel directory to checkpoint.restore:

model = tf.keras.Model(...)
    tf.saved_model.save(model, path)  # or model.save(path, save_format='tf')
    
    checkpoint = tf.train.Checkpoint(model)
    checkpoint.restore(path).expect_partial()

This example calls `expect_partial()` on the loaded status, since SavedModels saved from Keras often generates extra keys in the checkpoint. Otherwise, the program prints a lot of warnings about unused keys at exit time.

|     |     |
| --- | --- |
| Args |     |
| `save_path` | The path to the checkpoint, as returned by `save` or [`tf.train.latest_checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/latest_checkpoint)<br>. If the checkpoint was written by the name-based [`tf.compat.v1.train.Saver`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver)<br>, names are used to match variables. This path may also be a SavedModel directory. |
| `options` | Optional [`tf.train.CheckpointOptions`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointOptions)<br> object. |

|     |
| --- |
| Returns |     |
| A load status object, which can be used to make assertions about the status of a checkpoint restoration.<br><br>The returned status object has the following methods:<br><br>*   `assert_consumed()`: Raises an exception if any variables are unmatched: either checkpointed values which don't have a matching Python object or Python objects in the dependency graph with no values in the checkpoint. This method returns the status object, and so may be chained with other assertions.<br>    <br>*   `assert_existing_objects_matched()`: Raises an exception if any existing Python objects in the dependency graph are unmatched. Unlike `assert_consumed`, this assertion will pass if values in the checkpoint have no corresponding Python objects. For example a [`tf.keras.Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)<br>     object which has not yet been built, and so has not created any variables, will pass this assertion but fail `assert_consumed`. Useful when loading part of a larger checkpoint into a new Python program, e.g. a training checkpoint with a [`tf.compat.v1.train.Optimizer`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Optimizer)<br>     was saved but only the state required for inference is being loaded. This method returns the status object, and so may be chained with other assertions.<br>    <br>*   `assert_nontrivial_match()`: Asserts that something aside from the root object was matched. This is a very weak assertion, but is useful for sanity checking in library code where objects may exist in the checkpoint which haven't been created in Python and some Python objects may not have a checkpointed value.<br>    <br>*   `expect_partial()`: Silence warnings about incomplete checkpoint restores. Warnings are otherwise printed for unused parts of the checkpoint file or object when the `Checkpoint` object is deleted (often at program shutdown). |     |

|     |     |
| --- | --- |
| Raises |     |
| `NotFoundError` | if the a checkpoint or SavedModel cannot be found at `save_path`. |

### `save`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/checkpoint.py#L2428-L2535)

save(
        file_prefix, options=None
    )

Saves a training checkpoint and provides basic checkpoint management.

The saved checkpoint includes variables created by this object and any trackable objects it depends on at the time [`Checkpoint.save()`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#save)
 is called.

`save` is a basic convenience wrapper around the `write` method, sequentially numbering checkpoints using `save_counter` and updating the metadata used by [`tf.train.latest_checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/latest_checkpoint)
. More advanced checkpoint management, for example garbage collection and custom numbering, may be provided by other utilities which also wrap `write` and `read`. ([`tf.train.CheckpointManager`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointManager)
 for example).

step = tf.Variable(0, name="step")
    checkpoint = tf.train.Checkpoint(step=step)
    checkpoint.save("/tmp/ckpt")
    
    # Later, read the checkpoint with restore()
    checkpoint.restore("/tmp/ckpt-1")
    
    # You can also pass options to save() and restore(). For example this
    # runs the IO ops on the localhost:
    options = tf.train.CheckpointOptions(experimental_io_device="/job:localhost")
    checkpoint.save("/tmp/ckpt", options=options)
    
    # Later, read the checkpoint with restore()
    checkpoint.restore("/tmp/ckpt-1", options=options)

|     |     |
| --- | --- |
| Args |     |
| `file_prefix` | A prefix to use for the checkpoint filenames (/path/to/directory/and\_a\_prefix). Names are generated based on this prefix and [`Checkpoint.save_counter`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#save_counter)<br>. |
| `options` | Optional [`tf.train.CheckpointOptions`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointOptions)<br> object. |

|     |
| --- |
| Returns |     |
| The full path to the checkpoint. |     |

### `sync`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/checkpoint.py#L2421-L2426)

sync()

Wait for any outstanding save or restore operations.

### `write`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/checkpoint.py#L2277-L2320)

write(
        file_prefix, options=None
    )

Writes a training checkpoint.

The checkpoint includes variables created by this object and any trackable objects it depends on at the time [`Checkpoint.write()`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#write)
 is called.

`write` does not number checkpoints, increment `save_counter`, or update the metadata used by [`tf.train.latest_checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/latest_checkpoint)
. It is primarily intended for use by higher level checkpoint management utilities. `save` provides a very basic implementation of these features.

Checkpoints written with `write` must be read with `read`.

#### Example usage:

step = tf.Variable(0, name="step")
    checkpoint = tf.Checkpoint(step=step)
    checkpoint.write("/tmp/ckpt")
    
    # Later, read the checkpoint with read()
    checkpoint.read("/tmp/ckpt")
    
    # You can also pass options to write() and read(). For example this
    # runs the IO ops on the localhost:
    options = tf.CheckpointOptions(experimental_io_device="/job:localhost")
    checkpoint.write("/tmp/ckpt", options=options)
    
    # Later, read the checkpoint with read()
    checkpoint.read("/tmp/ckpt", options=options)

|     |     |
| --- | --- |
| Args |     |
| `file_prefix` | A prefix to use for the checkpoint filenames (/path/to/directory/and\_a\_prefix). |
| `options` | Optional [`tf.train.CheckpointOptions`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointOptions)<br> object. |

|     |
| --- |
| Returns |     |
| The full path to the checkpoint (i.e. `file_prefix`). |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.