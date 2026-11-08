[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#methods)
    *   [read](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#read)
        
    *   [restore](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#restore)
        
    *   [save](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#save)
        
    *   [sync](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#sync)
        
    *   [write](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#write)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.train.Checkpoint Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#methods)
    *   [read](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#read)
        
    *   [restore](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#restore)
        
    *   [save](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#save)
        
    *   [sync](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#sync)
        
    *   [write](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#write)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/checkpoint.py#L2060-L2748)

Manages saving/restoring trackable values to disk.

tf.train.Checkpoint(
        root=None, **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrating model checkpoints](https://www.tensorflow.org/guide/migrate/migrating_checkpoints)<br>    <br>*   [Training checkpoints](https://www.tensorflow.org/guide/checkpoint)<br>    <br>*   [Random number generation](https://www.tensorflow.org/guide/random_numbers)<br>    <br>*   [Estimators](https://www.tensorflow.org/guide/estimator)<br>    <br>*   [Introduction to modules, layers, and models](https://www.tensorflow.org/guide/intro_to_modules) | *   [Custom training with tf.distribute.Strategy](https://www.tensorflow.org/tutorials/distribute/custom_training)<br>    <br>*   [Distributed training with DTensors](https://www.tensorflow.org/tutorials/distribute/dtensor_ml_tutorial)<br>    <br>*   [Custom training loop with Keras and MultiWorkerMirroredStrategy](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_ctl)<br>    <br>*   [Multi-worker training with Keras](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras)<br>    <br>*   [CycleGAN](https://www.tensorflow.org/tutorials/generative/cyclegan) |

TensorFlow objects may contain trackable state, such as [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
s, [`tf.keras.optimizers.Optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer)
 implementations, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 iterators, [`tf.keras.Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
 implementations, or [`tf.keras.Model`](https://www.tensorflow.org/api_docs/python/tf/keras/Model)
 implementations. These are called **trackable objects**.

A `Checkpoint` object can be constructed to save either a single or group of trackable objects to a checkpoint file. It maintains a `save_counter` for numbering checkpoints.

#### Example:

model = tf.keras.Model(...)
    checkpoint = tf.train.Checkpoint(model)
    
    # Save a checkpoint to /tmp/training_checkpoints-{save_counter}. Every time
    # checkpoint.save is called, the save counter is increased.
    save_path = checkpoint.save('/tmp/training_checkpoints')
    
    # Restore the checkpointed values to the `model` object.
    checkpoint.restore(save_path)

#### Example 2:

import tensorflow as tf
    import os
    
    checkpoint_directory = "/tmp/training_checkpoints"
    checkpoint_prefix = os.path.join(checkpoint_directory, "ckpt")
    
    # Create a Checkpoint that will manage two objects with trackable state,
    # one we name "optimizer" and the other we name "model".
    checkpoint = tf.train.Checkpoint(optimizer=optimizer, model=model)
    status = checkpoint.restore(tf.train.latest_checkpoint(checkpoint_directory))
    for _ in range(num_training_steps):
      optimizer.minimize( ... )  # Variables will be restored on creation.
    status.assert_consumed()  # Optional sanity checks.
    checkpoint.save(file_prefix=checkpoint_prefix)

[`Checkpoint.save()`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#save)
 and [`Checkpoint.restore()`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#restore)
 write and read object-based checkpoints, in contrast to TensorFlow 1.x's [`tf.compat.v1.train.Saver`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver)
 which writes and reads `variable.name` based checkpoints. Object-based checkpointing saves a graph of dependencies between Python objects (`Layer`s, `Optimizer`s, `Variable`s, etc.) with named edges, and this graph is used to match variables when restoring a checkpoint. It can be more robust to changes in the Python program, and helps to support restore-on-create for variables.

`Checkpoint` objects have dependencies on the objects passed as keyword arguments to their constructors, and each dependency is given a name that is identical to the name of the keyword argument for which it was created. TensorFlow classes like `Layer`s and `Optimizer`s will automatically add dependencies on their own variables (e.g. "kernel" and "bias" for [`tf.keras.layers.Dense`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense)
). Inheriting from [`tf.keras.Model`](https://www.tensorflow.org/api_docs/python/tf/keras/Model)
 makes managing dependencies easy in user-defined classes, since `Model` hooks into attribute assignment. For example:

class Regress(tf.keras.Model):
    
      def __init__(self):
        super().__init__()
        self.input_transform = tf.keras.layers.Dense(10)
        # ...
    
      def call(self, inputs):
        x = self.input_transform(inputs)
        # ...

This `Model` has a dependency named "input\_transform" on its `Dense` layer, which in turn depends on its variables. As a result, saving an instance of `Regress` using [`tf.train.Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)
 will also save all the variables created by the `Dense` layer.

When variables are assigned to multiple workers, each worker writes its own section of the checkpoint. These sections are then merged/re-indexed to behave as a single checkpoint. This avoids copying all variables to one worker, but does require that all workers see a common filesystem.

This function differs slightly from the Keras Model `save_weights` function. [`tf.keras.Model.save_weights`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#save_weights)
 creates a checkpoint file with the name specified in `filepath`, while [`tf.train.Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)
 numbers the checkpoints, using `filepath` as the prefix for the checkpoint file names. Aside from this, `model.save_weights()` and `tf.train.Checkpoint(model).save()` are equivalent.

See the [guide to training checkpoints](https://www.tensorflow.org/guide/checkpoint)
 for details.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `root` | The root object to checkpoint. `root` may be a trackable object or `WeakRef` of a trackable object. |
| `**kwargs` | Keyword arguments are set as attributes of this object, and are saved with the checkpoint. All `kwargs` must be trackable objects, or a nested structure of trackable objects (`list`, `dict`, or `tuple`). |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `root` or the objects in `kwargs` are not trackable. A `ValueError` is also raised if the `root` object tracks different objects from the ones listed in attributes in kwargs (e.g. `root.child = A` and [`tf.train.Checkpoint(root, child=B)`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)<br> are incompatible). |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `save_counter` | Incremented when `save()` is called. Used to number checkpoints. |

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