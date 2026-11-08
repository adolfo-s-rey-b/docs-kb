[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fcallbacks%2FRemoteMonitor&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#methods)
    *   [on\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_batch_begin)
        
    *   [on\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_batch_end)
        
    *   [on\_epoch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_epoch_begin)
        
    *   [on\_epoch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_epoch_end)
        
    *   [on\_predict\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_predict_batch_begin)
        
    *   [on\_predict\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_predict_batch_end)
        
    *   [on\_predict\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_predict_begin)
        
    *   [on\_predict\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_predict_end)
        
    *   [on\_test\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_test_batch_begin)
        
    *   [on\_test\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_test_batch_end)
        
    *   [on\_test\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_test_begin)
        
    *   [on\_test\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_test_end)
        
    *   [on\_train\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_train_batch_begin)
        
    *   [on\_train\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_train_batch_end)
        
    *   [on\_train\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_train_begin)
        
    *   [on\_train\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_train_end)
        
    *   [set\_model](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#set_model)
        
    *   [set\_params](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#set_params)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Was this helpful?

tf.keras.callbacks.RemoteMonitor Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#methods)
    *   [on\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_batch_begin)
        
    *   [on\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_batch_end)
        
    *   [on\_epoch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_epoch_begin)
        
    *   [on\_epoch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_epoch_end)
        
    *   [on\_predict\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_predict_batch_begin)
        
    *   [on\_predict\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_predict_batch_end)
        
    *   [on\_predict\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_predict_begin)
        
    *   [on\_predict\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_predict_end)
        
    *   [on\_test\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_test_batch_begin)
        
    *   [on\_test\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_test_batch_end)
        
    *   [on\_test\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_test_begin)
        
    *   [on\_test\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_test_end)
        
    *   [on\_train\_batch\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_train_batch_begin)
        
    *   [on\_train\_batch\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_train_batch_end)
        
    *   [on\_train\_begin](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_train_begin)
        
    *   [on\_train\_end](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#on_train_end)
        
    *   [set\_model](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#set_model)
        
    *   [set\_params](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/RemoteMonitor#set_params)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/remote_monitor.py#L15-L83)

Callback used to stream events to a server.

Inherits From: [`Callback`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/Callback)

tf.keras.callbacks.RemoteMonitor(
        root='http://localhost:9000',
        path='/publish/epoch/end/',
        field='data',
        headers=None,
        send_as_json=False
    )

Requires the `requests` library. Events are sent to `root + '/publish/epoch/end/'` by default. Calls are HTTP POST, with a `data` argument which is a JSON-encoded dictionary of event data. If `send_as_json=True`, the content type of the request will be `"application/json"`. Otherwise the serialized JSON will be sent within a form.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `root` | String; root url of the target server. |
| `path` | String; path relative to `root` to which the events will be sent. |
| `field` | String; JSON field under which the data will be stored. The field is used only if the payload is sent within a form (i.e. when `send_as_json=False`). |
| `headers` | Dictionary; optional custom HTTP headers. |
| `send_as_json` | Boolean; whether the request should be sent as `"application/json"`. |

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/callbacks/remote_monitor.py#L54-L83)

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

Was this helpful?

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.