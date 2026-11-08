[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#methods)
    *   [on\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_batch_begin)
        
    *   [on\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_batch_end)
        
    *   [on\_epoch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_epoch_begin)
        
    *   [on\_epoch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_epoch_end)
        
    *   [on\_predict\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_predict_batch_begin)
        
    *   [on\_predict\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_predict_batch_end)
        
    *   [on\_predict\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_predict_begin)
        
    *   [on\_predict\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_predict_end)
        
    *   [on\_test\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_test_batch_begin)
        
    *   [on\_test\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_test_batch_end)
        
    *   [on\_test\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_test_begin)
        
    *   [on\_test\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_test_end)
        
    *   [on\_train\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_train_batch_begin)
        
    *   [on\_train\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_train_batch_end)
        
    *   [on\_train\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_train_begin)
        
    *   [on\_train\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_train_end)
        
    *   [set\_model](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#set_model)
        
    *   [set\_params](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#set_params)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.callbacks.TerminateOnNaN Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#methods)
    *   [on\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_batch_begin)
        
    *   [on\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_batch_end)
        
    *   [on\_epoch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_epoch_begin)
        
    *   [on\_epoch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_epoch_end)
        
    *   [on\_predict\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_predict_batch_begin)
        
    *   [on\_predict\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_predict_batch_end)
        
    *   [on\_predict\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_predict_begin)
        
    *   [on\_predict\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_predict_end)
        
    *   [on\_test\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_test_batch_begin)
        
    *   [on\_test\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_test_batch_end)
        
    *   [on\_test\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_test_begin)
        
    *   [on\_test\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_test_end)
        
    *   [on\_train\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_train_batch_begin)
        
    *   [on\_train\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_train_batch_end)
        
    *   [on\_train\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_train_begin)
        
    *   [on\_train\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#on_train_end)
        
    *   [set\_model](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#set_model)
        
    *   [set\_params](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TerminateOnNaN#set_params)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/terminate_on_nan.py#L8-L69)

Callback that terminates training when a NaN loss is encountered.

Inherits From: [`Callback`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/Callback)

tf.keras.callbacks.TerminateOnNaN(
        raise_error: bool = False
    )

This callback monitors the loss value during training and terminates training when a NaN or Inf loss is detected. By default, training is stopped gracefully by setting `model.stop_training = True`, which triggers all callback cleanup methods including `on_train_end()`.

Alternatively, you can use `raise_error=True` to immediately raise a RuntimeError when NaN/Inf is detected. This raise\_error termination prevents `on_train_end()` from being called on other callbacks, which is useful for preserving backup states or preventing unintended cleanup when training fails.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `raise_error` | Boolean, default False. If False, uses graceful stop via `model.stop_training = True`. If True, immediately raises RuntimeError on NaN/Inf loss, bypassing callback cleanup methods. |

#### Example:

# Graceful termination (default)
    callback = keras.callbacks.TerminateOnNaN()
    model.fit(x, y, callbacks=[callback])
    
    # raise_error termination (strict failure)
    callback = keras.callbacks.TerminateOnNaN(raise_error=True)
    model.fit(x, y, callbacks=[callback])

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/terminate_on_nan.py#L46-L69)

on_batch_end(
        batch, logs=None
    )

Check for NaN/Inf loss at the end of each batch.

|     |     |
| --- | --- |
| Args |     |
| `batch` | Integer, index of batch within the current epoch. |
| `logs` | Dict, contains the return value of `model.train_step()`. |

|     |     |
| --- | --- |
| Raises |     |
| `RuntimeError` | If loss is NaN/Inf and raise\_error=True. |

### `on_epoch_begin`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L110-L121)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L123-L137)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/callback.py#L157-L172)

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