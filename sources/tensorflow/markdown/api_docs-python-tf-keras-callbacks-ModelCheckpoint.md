[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#methods)
    *   [on\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_batch_begin)
        
    *   [on\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_batch_end)
        
    *   [on\_epoch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_epoch_begin)
        
    *   [on\_epoch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_epoch_end)
        
    *   [on\_predict\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_predict_batch_begin)
        
    *   [on\_predict\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_predict_batch_end)
        
    *   [on\_predict\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_predict_begin)
        
    *   [on\_predict\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_predict_end)
        
    *   [on\_test\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_test_batch_begin)
        
    *   [on\_test\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_test_batch_end)
        
    *   [on\_test\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_test_begin)
        
    *   [on\_test\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_test_end)
        
    *   [on\_train\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_train_batch_begin)
        
    *   [on\_train\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_train_batch_end)
        
    *   [on\_train\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_train_begin)
        
    *   [on\_train\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_train_end)
        
    *   [set\_model](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#set_model)
        
    *   [set\_params](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#set_params)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.callbacks.ModelCheckpoint Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#methods)
    *   [on\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_batch_begin)
        
    *   [on\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_batch_end)
        
    *   [on\_epoch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_epoch_begin)
        
    *   [on\_epoch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_epoch_end)
        
    *   [on\_predict\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_predict_batch_begin)
        
    *   [on\_predict\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_predict_batch_end)
        
    *   [on\_predict\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_predict_begin)
        
    *   [on\_predict\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_predict_end)
        
    *   [on\_test\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_test_batch_begin)
        
    *   [on\_test\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_test_batch_end)
        
    *   [on\_test\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_test_begin)
        
    *   [on\_test\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_test_end)
        
    *   [on\_train\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_train_batch_begin)
        
    *   [on\_train\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_train_batch_end)
        
    *   [on\_train\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_train_begin)
        
    *   [on\_train\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#on_train_end)
        
    *   [set\_model](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#set_model)
        
    *   [set\_params](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint#set_params)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/model_checkpoint.py#L14-L470)

Callback to save the Keras model or model weights at some frequency.

Inherits From: [`Callback`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/Callback)

tf.keras.callbacks.ModelCheckpoint(
        filepath,
        monitor='val_loss',
        verbose=0,
        save_best_only=False,
        save_weights_only=False,
        mode='auto',
        save_freq='epoch',
        initial_value_threshold=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate checkpoint saving](https://www.tensorflow.org/guide/migrate/checkpoint_saver)<br>    <br>*   [Migrate evaluation](https://www.tensorflow.org/guide/migrate/evaluator)<br>    <br>*   [Multi-GPU and distributed training](https://www.tensorflow.org/guide/keras/distributed_training) | *   [Save and load models](https://www.tensorflow.org/tutorials/keras/save_and_load)<br>    <br>*   [Generate music with an RNN](https://www.tensorflow.org/tutorials/audio/music_generation)<br>    <br>*   [Distributed training with Keras](https://www.tensorflow.org/tutorials/distribute/keras)<br>    <br>*   [Parameter server training with ParameterServerStrategy](https://www.tensorflow.org/tutorials/distribute/parameter_server_training)<br>    <br>*   [Human Pose Classification with MoveNet and TensorFlow Lite](https://www.tensorflow.org/lite/tutorials/pose_classification) |

`ModelCheckpoint` callback is used in conjunction with training using `model.fit()` to save a model or weights (in a checkpoint file) at some interval, so the model or weights can be loaded later to continue the training from the state saved.

A few options this callback provides include:

*   Whether to only keep the model that has achieved the "best performance" so far, or whether to save the model at the end of every epoch regardless of performance.
*   Definition of "best"; which quantity to monitor and whether it should be maximized or minimized.
*   The frequency it should save at. Currently, the callback supports saving at the end of every epoch, or after a fixed number of training batches.
*   Whether only weights are saved, or the whole model is saved.

#### Example:

# Define a learning rate schedule
    initial_learning_rate = 0.1
    lr_schedule = keras.optimizers.schedules.ExponentialDecay(
        initial_learning_rate,
        decay_steps=100000,
        decay_rate=0.96,
        staircase=True,
    )
    
    model.compile(
        optimizer=keras.optimizers.RMSprop(learning_rate=lr_schedule),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    
    checkpoint_filepath = '/tmp/ckpt/checkpoint.model.keras'
    model_checkpoint_callback = keras.callbacks.ModelCheckpoint(
        filepath=checkpoint_filepath,
        monitor='val_accuracy',
        mode='max',
        save_best_only=True)
    
    # Model is saved at the end of every epoch, if it's the best seen so far.
    model.fit(
        x_train, y_train, epochs=10, callbacks=[model_checkpoint_callback]
    )
    
    # The model (that are considered the best) can be loaded as -
    keras.models.load_model(checkpoint_filepath)
    
    # Alternatively, one could checkpoint just the model weights as -
    checkpoint_filepath = '/tmp/ckpt/checkpoint.weights.h5'
    model_checkpoint_callback = keras.callbacks.ModelCheckpoint(
        filepath=checkpoint_filepath,
        save_weights_only=True,
        monitor='val_accuracy',
        mode='max',
        save_best_only=True)
    
    # Model weights are saved at the end of every epoch, if it's the best seen
    # so far.
    model.fit(
        x_train, y_train, epochs=10, callbacks=[model_checkpoint_callback]
    )
    
    # The model weights (that are considered the best) can be loaded as -
    model.load_weights(checkpoint_filepath)

Resuming training from weight-only checkpoints:

When using `save_weights_only=True`, the weights file includes the state of the optimizer (including iteration count and learning rate state) if the model is compiled at the time of saving.

To correctly resume training and restore the optimizer state (e.g., to continue a learning rate schedule without resetting it), you must **compile the model before loading the weights**.

# Define a learning rate schedule
    initial_learning_rate = 0.1
    lr_schedule = keras.optimizers.schedules.ExponentialDecay(
        initial_learning_rate,
        decay_steps=100000,
        decay_rate=0.96,
        staircase=True,
    )
    
    # 1. Create a fresh model instance
    model = get_model()
    
    # 2. Compile the model *before* loading weights
    model.compile(
        optimizer=keras.optimizers.RMSprop(learning_rate=lr_schedule),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    
    # 3. Load weights (optimizer state is restored automatically)
    model.load_weights(checkpoint_filepath)
    
    # 4. Continue training
    model.fit(x_train, y_train, epochs=10)

|     |     |     |
| --- | --- | --- |
| Args<br>---- |     |
| `filepath` | string or `PathLike`, path to save the model file. `filepath` can contain named formatting options, which will be filled the value of `epoch` and keys in `logs` (passed in `on_epoch_end`). The `filepath` name needs to end with `".weights.h5"` when `save_weights_only=True` or should end with `".keras"` or `".h5"` when checkpoint saving the whole model (default). For example: if `filepath` is `"{epoch:02d}-{val_loss:.2f}.keras"` or "{epoch:02d}-{val\_loss:.2f}.weights.h5"`, then the model checkpoints will be saved with the epoch number and the validation loss in the filename. The directory of the filepath should not be reused by any other callbacks to avoid conflicts. </td> </tr><tr> <td>`monitor\` | The metric name to monitor. Typically the metrics are set by the [`Model.compile`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#compile)<br> method. Note:<br><br>*   Prefix the name with `"val_"` to monitor validation metrics.<br>*   Use `"loss"` or `"val_loss"` to monitor the model's total loss.<br>*   If you specify metrics as strings, like `"accuracy"`, pass the same string (with or without the `"val_"` prefix).<br>*   If you pass [`metrics.Metric`](https://www.tensorflow.org/api_docs/python/tf/keras/Metric)<br>     objects, `monitor` should be set to `metric.name`<br>*   If you're not sure about the metric names you can check the contents of the `history.history` dictionary returned by `history = model.fit()`<br>*   Multi-output models set additional prefixes on the metric names. |
| `verbose` | Verbosity mode, 0 or 1. Mode 0 is silent, and mode 1 displays messages when the callback takes an action. |
| `save_best_only` | if `save_best_only=True`, it only saves when the model is considered the "best" and the latest best model according to the quantity monitored will not be overwritten. If `filepath` doesn't contain formatting options like `{epoch}` then `filepath` will be overwritten by each new better model. |
| `mode` | one of {`"auto"`, `"min"`, `"max"`}. If `save_best_only=True`, the decision to overwrite the current save file is made based on either the maximization or the minimization of the monitored quantity. For `val_acc`, this should be `"max"`, for `val_loss` this should be `"min"`, etc. In `"auto"` mode, the direction is automatically inferred from the name of the monitored quantity. |
| `save_weights_only` | if `True`, then only the model's weights will be saved (`model.save_weights(filepath)`), else the full model is saved (`model.save(filepath)`). |
| `save_freq` | `"epoch"` or integer. When using `"epoch"`, the callback saves the model after each epoch. When using integer, the callback saves the model at end of this many batches. If the `Model` is compiled with `steps_per_execution=N`, then the saving criteria will be checked every Nth batch. Note that if the saving isn't aligned to epochs, the monitored metric may potentially be less reliable (it could reflect as little as 1 batch, since the metrics get reset every epoch). Defaults to `"epoch"`. |
| `initial_value_threshold` | Floating point initial "best" value of the metric to be monitored. Only applies if `save_best_value=True`. Only overwrites the model weights already saved if the performance of current model is better than this value. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `model` |     |

Methods
-------

### `on_batch_begin`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L102-L104)

on_batch_begin(
        batch, logs=None
    )

A backwards compatibility alias for `on_train_batch_begin`.

### `on_batch_end`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L106-L108)

on_batch_end(
        batch, logs=None
    )

A backwards compatibility alias for `on_train_batch_end`.

### `on_epoch_begin`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/model_checkpoint.py#L227-L228)

on_epoch_begin(
        epoch, logs=None
    )

Called at the start of an epoch.

Subclasses should override for any actions to run. This function should only be called during TRAIN mode.

|     |     |
| --- | --- |
| Args |     |
| `epoch` | Integer, index of epoch. |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_epoch_end`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/model_checkpoint.py#L230-L236)

on_epoch_end(
        epoch, logs=None
    )

Called at the end of an epoch.

Subclasses should override for any actions to run. This function should only be called during TRAIN mode.

|     |     |
| --- | --- |
| Args |     |
| `epoch` | Integer, index of epoch. |
| `logs` | Dict, metric results for this training epoch, and for the validation epoch if validation is performed. Validation result keys are prefixed with `val_`. For training epoch, the values of the `Model`'s metrics are returned. Example: `{'loss': 0.2, 'accuracy': 0.7}`. |

### `on_predict_batch_begin`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L211-L225)

on_predict_batch_begin(
        batch, logs=None
    )

Called at the beginning of a batch in `predict` methods.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in `Model` is set to `N`, this method will only be called every `N` batches.

|     |     |
| --- | --- |
| Args |     |
| `batch` | Integer, index of batch within the current epoch. |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_predict_batch_end`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L227-L240)

on_predict_batch_end(
        batch, logs=None
    )

Called at the end of a batch in `predict` methods.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in `Model` is set to `N`, this method will only be called every `N` batches.

|     |     |
| --- | --- |
| Args |     |
| `batch` | Integer, index of batch within the current epoch. |
| `logs` | Dict. Aggregated metric results up until this batch. |

### `on_predict_begin`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L288-L297)

on_predict_begin(
        logs=None
    )

Called at the beginning of prediction.

Subclasses should override for any actions to run.

|     |     |
| --- | --- |
| Args |     |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_predict_end`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L299-L308)

on_predict_end(
        logs=None
    )

Called at the end of prediction.

Subclasses should override for any actions to run.

|     |     |
| --- | --- |
| Args |     |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_test_batch_begin`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L174-L191)

on_test_batch_begin(
        batch, logs=None
    )

Called at the beginning of a batch in `evaluate` methods.

Also called at the beginning of a validation batch in the `fit` methods, if validation data is provided.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in `Model` is set to `N`, this method will only be called every `N` batches.

|     |     |
| --- | --- |
| Args |     |
| `batch` | Integer, index of batch within the current epoch. |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_test_batch_end`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L193-L209)

on_test_batch_end(
        batch, logs=None
    )

Called at the end of a batch in `evaluate` methods.

Also called at the end of a validation batch in the `fit` methods, if validation data is provided.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in `Model` is set to `N`, this method will only be called every `N` batches.

|     |     |
| --- | --- |
| Args |     |
| `batch` | Integer, index of batch within the current epoch. |
| `logs` | Dict. Aggregated metric results up until this batch. |

### `on_test_begin`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L265-L274)

on_test_begin(
        logs=None
    )

Called at the beginning of evaluation or validation.

Subclasses should override for any actions to run.

|     |     |
| --- | --- |
| Args |     |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_test_end`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L276-L286)

on_test_end(
        logs=None
    )

Called at the end of evaluation or validation.

Subclasses should override for any actions to run.

|     |     |
| --- | --- |
| Args |     |
| `logs` | Dict. Currently the output of the last call to `on_test_batch_end()` is passed to this argument for this method but that may change in the future. |

### `on_train_batch_begin`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L139-L155)

on_train_batch_begin(
        batch, logs=None
    )

Called at the beginning of a training batch in `fit` methods.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in `Model` is set to `N`, this method will only be called every `N` batches.

|     |     |
| --- | --- |
| Args |     |
| `batch` | Integer, index of batch within the current epoch. |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_train_batch_end`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/model_checkpoint.py#L223-L225)

on_train_batch_end(
        batch, logs=None
    )

Called at the end of a training batch in `fit` methods.

Subclasses should override for any actions to run.

Note that if the `steps_per_execution` argument to `compile` in `Model` is set to `N`, this method will only be called every `N` batches.

|     |     |
| --- | --- |
| Args |     |
| `batch` | Integer, index of batch within the current epoch. |
| `logs` | Dict. Aggregated metric results up until this batch. |

### `on_train_begin`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L242-L251)

on_train_begin(
        logs=None
    )

Called at the beginning of training.

Subclasses should override for any actions to run.

|     |     |
| --- | --- |
| Args |     |
| `logs` | Dict. Currently no data is passed to this argument for this method but that may change in the future. |

### `on_train_end`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L253-L263)

on_train_end(
        logs=None
    )

Called at the end of training.

Subclasses should override for any actions to run.

|     |     |
| --- | --- |
| Args |     |
| `logs` | Dict. Currently the output of the last call to `on_epoch_end()` is passed to this argument for this method but that may change in the future. |

### `set_model`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L74-L75)

set_model(
        model
    )

### `set_params`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L71-L72)

set_params(
        params
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.