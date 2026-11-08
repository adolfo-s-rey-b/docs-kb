[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointOptions#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointOptions)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointOptions?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointOptions#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointOptions#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.train.CheckpointOptions Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointOptions#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointOptions#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/checkpoint_options.py#L25-L128)

Options for constructing a Checkpoint.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.CheckpointOptions`](https://www.tensorflow.org/api_docs/python/tf/train/CheckpointOptions)

tf.train.CheckpointOptions(
        experimental_io_device=None,
        experimental_enable_async_checkpoint=False,
        experimental_write_callbacks=None,
        enable_async=False,
        experimental_skip_slot_variables=False,
        experimental_sharding_callback=None
    )

Used as the `options` argument to either [`tf.train.Checkpoint.save()`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#save)
 or [`tf.train.Checkpoint.restore()`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#restore)
 methods to adjust how variables are saved/restored.

Example: Run IO ops on "localhost" while saving a checkpoint:

step = tf.Variable(0, name="step")
    checkpoint = tf.train.Checkpoint(step=step)
    options = tf.train.CheckpointOptions(experimental_io_device="/job:localhost")
    checkpoint.save("/tmp/ckpt", options=options)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `experimental_io_device` | string. Applies in a distributed setting. Tensorflow device to use to access the filesystem. If `None` (default) then for each variable the filesystem is accessed from the CPU:0 device of the host where that variable is assigned. If specified, the filesystem is instead accessed from that device for all variables. This is for example useful if you want to save to a local directory, such as "/tmp" when running in a distributed setting. In that case pass a device for the host where the "/tmp" directory is accessible. |
| `experimental_enable_async_checkpoint` | bool Type. Deprecated, please use the enable\_async option. |
| `experimental_write_callbacks` | List\[Callable\]. A list of callback functions that will be executed after each saving event finishes (i.e. after `save()` or `write()`). For async checkpoint, the callbacks will be executed only after the async thread finishes saving. The return values of the callback(s) will be ignored. The callback(s) can optionally take the `save_path` (the result of `save()` or `write()`) as an argument. The callbacks will be executed in the same order of this list after the checkpoint has been written. |
| `enable_async` | bool Type. Indicates whether async checkpointing is enabled. Default is False, i.e., no async checkpoint. Async checkpoint moves the checkpoint file writing off the main thread, so that the model can continue to train while the checkpoint file writing runs in the background. Async checkpoint reduces TPU device idle cycles and speeds up model training process, while memory consumption may increase. |
| `experimental_skip_slot_variables` | bool Type. If true, ignores slot variables during restore. Context: TPU Embedding layers for Serving do not properly restore slot variables. This option is a way to omit restoring slot variables which are not required for Serving usecase anyways.(b/315912101) |
| `experimental_sharding_callback` | [`tf.train.experimental.ShardingCallback`](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardingCallback)<br>. A pre-made or custom callback that determines how checkpoints are sharded on disk. Pre-made callback options are `tf.train.experimental.ShardByDevicePolicy` and [`tf.train.experimental.MaxShardSizePolicy`](https://www.tensorflow.org/api_docs/python/tf/train/experimental/MaxShardSizePolicy)<br>. You may also write a custom callback, see [`tf.train.experimental.ShardingCallback`](https://www.tensorflow.org/api_docs/python/tf/train/experimental/ShardingCallback)<br>. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `enable_async` |     |
| `experimental_enable_async_checkpoint` |     |
| `experimental_io_device` |     |
| `experimental_sharding_callback` |     |
| `experimental_skip_slot_variables` |     |
| `experimental_write_callbacks` |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.