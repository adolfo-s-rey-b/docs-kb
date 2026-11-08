[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fdistillation%2FDistiller%3Fversion%3Dstable&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#arguments_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#methods_2)
    *   [compile](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#compile)
        
    *   [compile\_from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#compile_from_config)
        
    *   [compiled\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#compiled_loss)
        
    *   [compute\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#compute_loss)
        
    *   [compute\_metrics](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#compute_metrics)
        
    *   [evaluate](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#evaluate)
        
    *   [export](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#export)
        
    *   [fit](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#fit)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#from_config)
        
    *   [get\_compile\_config](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#get_compile_config)
        
    *   [get\_layer](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#get_layer)
        
    *   [get\_metrics\_result](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#get_metrics_result)
        
    *   [get\_quantization\_layer\_structure](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#get_quantization_layer_structure)
        
    *   [get\_state\_tree](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#get_state_tree)
        
    *   [load\_weights](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#load_weights)
        
    *   [loss](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#loss)
        
    *   [make\_predict\_function](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#make_predict_function)
        
    *   [make\_test\_function](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#make_test_function)
        
    *   [make\_train\_function](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#make_train_function)
        
    *   [predict](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#predict)
        
    *   [predict\_on\_batch](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#predict_on_batch)
        
    *   [predict\_step](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#predict_step)
        
    *   [reset\_metrics](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#reset_metrics)
        
    *   [save](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#save)
        
    *   [save\_weights](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#save_weights)
        
    *   [set\_state\_tree](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#set_state_tree)
        
    *   [stateless\_compute\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#stateless_compute_loss)
        
    *   [summary](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#summary)
        
    *   [test\_on\_batch](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#test_on_batch)
        
    *   [test\_step](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#test_step)
        
    *   [to\_json](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#to_json)
        
    *   [train\_on\_batch](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#train_on_batch)
        
    *   [train\_step](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#train_step)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.distillation.Distiller Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#arguments_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#methods_2)
    *   [compile](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#compile)
        
    *   [compile\_from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#compile_from_config)
        
    *   [compiled\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#compiled_loss)
        
    *   [compute\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#compute_loss)
        
    *   [compute\_metrics](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#compute_metrics)
        
    *   [evaluate](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#evaluate)
        
    *   [export](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#export)
        
    *   [fit](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#fit)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#from_config)
        
    *   [get\_compile\_config](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#get_compile_config)
        
    *   [get\_layer](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#get_layer)
        
    *   [get\_metrics\_result](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#get_metrics_result)
        
    *   [get\_quantization\_layer\_structure](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#get_quantization_layer_structure)
        
    *   [get\_state\_tree](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#get_state_tree)
        
    *   [load\_weights](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#load_weights)
        
    *   [loss](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#loss)
        
    *   [make\_predict\_function](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#make_predict_function)
        
    *   [make\_test\_function](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#make_test_function)
        
    *   [make\_train\_function](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#make_train_function)
        
    *   [predict](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#predict)
        
    *   [predict\_on\_batch](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#predict_on_batch)
        
    *   [predict\_step](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#predict_step)
        
    *   [reset\_metrics](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#reset_metrics)
        
    *   [save](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#save)
        
    *   [save\_weights](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#save_weights)
        
    *   [set\_state\_tree](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#set_state_tree)
        
    *   [stateless\_compute\_loss](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#stateless_compute_loss)
        
    *   [summary](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#summary)
        
    *   [test\_on\_batch](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#test_on_batch)
        
    *   [test\_step](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#test_step)
        
    *   [to\_json](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#to_json)
        
    *   [train\_on\_batch](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#train_on_batch)
        
    *   [train\_step](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/Distiller?version=stable#train_step)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distillation/distiller.py#L9-L598)

Distillation model for transferring knowledge from teacher to student.

Inherits From: [`Model`](https://www.tensorflow.org/api_docs/python/tf/keras/Model)
, [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.distillation.Distiller(
        teacher,
        student,
        distillation_losses,
        distillation_loss_weights=None,
        student_loss_weight=0.5,
        name='distiller',
        **kwargs
    )

Knowledge distillation transfers knowledge from a large, complex model (teacher) to a smaller, simpler model (student). The student learns from both ground truth labels and the teacher's predictions, often achieving better performance than training on labels alone.

|     |     |
| --- | --- |
| Arguments<br>--------- |     |
| `teacher` | A trained [`keras.Model`](https://www.tensorflow.org/api_docs/python/tf/keras/Model)<br> that serves as the knowledge source. The teacher model is frozen during distillation. |
| `student` | A [`keras.Model`](https://www.tensorflow.org/api_docs/python/tf/keras/Model)<br> to be trained through distillation. |
| `distillation_losses` | List of distillation losses to apply. Can be a single distillation loss or a list of distillation losses like [`keras.distillation.LogitsDistillation`](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/LogitsDistillation)<br>, [`keras.distillation.FeatureDistillation`](https://www.tensorflow.org/api_docs/python/tf/keras/distillation/FeatureDistillation)<br>, or custom distillation losses. |
| `distillation_loss_weights` | List of weights for each distillation loss. Must have the same length as `distillation_losses`. If `None`, equal weights are used. |
| `student_loss_weight` | Weight for the student's supervised loss component. Must be between 0 and 1. Defaults to 0.5. |
| `name` | Name for the distiller model. Defaults to `"distiller"`. |
| `**kwargs` | Additional keyword arguments passed to the parent `Model` class. |

#### Examples:

# Basic distillation with KerasHub models
    import keras_hub as hub
    
    teacher = hub.models.CausalLM.from_preset("gemma_2b_en")
    student = hub.models.CausalLM.from_preset(
        "gemma_1.1_2b_en", load_weights=False
    )
    
    # Single distillation loss
    distiller = Distiller(
        teacher=teacher,
        student=student,
        distillation_losses=LogitsDistillation(temperature=3.0),
    )
    
    # Compile the distiller (like any Keras model)
    distiller.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # Train the distiller
    distiller.fit(x_train, y_train, epochs=10)
    
    # Access the trained student model
    trained_student = distiller.student
    
    # Multiple distillation losses
    distiller = Distiller(
        teacher=teacher,
        student=student,
        distillation_losses=[\
            LogitsDistillation(temperature=3.0),\
            FeatureDistillation(\
                teacher_layer_name="dense_1",\
                student_layer_name="dense_1"\
            )\
        ],
        distillation_loss_weights=[1.0, 0.5],
    )
    
    # Compile with custom settings
    distiller.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `student` | The student model being trained. Access this to get the trained student model for independent use after distillation training. |
| `teacher` | The teacher model providing knowledge. This model is frozen during training. |
| `compiled_metrics` |     |
| `distribute_reduction_method` |     |
| `distribute_strategy` |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `jit_compile` |     |
| `layers` |     |
| `metrics_names` |     |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `run_eagerly` |     |

Methods
-------

### `compile`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distillation/distiller.py#L386-L412)

compile(
        optimizer='adam', loss=None, metrics=None, **kwargs
    )

Compile the distiller with proper integration.

|     |     |
| --- | --- |
| Arguments |     |
| `optimizer` | Optimizer for training the student model. |
| `loss` | Student loss function for the student's supervised learning. Can be a string identifier or a loss function instance. |
| `metrics` | Additional metrics to track during training. |
| `**kwargs` | Additional arguments passed to parent compile. |

### `compile_from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/trainers/trainer.py#L994-L1020)

compile_from_config(
        config
    )

Compiles the model with the information given in config.

This method uses the information in the config (optimizer, loss, metrics, etc.) to compile the model.

|     |     |
| --- | --- |
| Args |     |
| `config` | Dict containing information for compiling the model. |

### `compiled_loss`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L693-L702)

compiled_loss(
        y, y_pred, sample_weight=None, regularization_losses=None
    )

### `compute_loss`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distillation/distiller.py#L418-L551)

compute_loss(
        x=None, y=None, y_pred=None, sample_weight=None, training=True
    )

Compute combined distillation loss.

|     |     |
| --- | --- |
| Arguments |     |
| `x` | Input data. |
| `y` | Target data. |
| `y_pred` | Model predictions. |
| `sample_weight` | Sample weights (currently unused). |
| `training` | Whether the model is in training mode. |

|     |
| --- |
| Returns |     |
| Combined loss tensor. |     |

### `compute_metrics`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/trainers/trainer.py#L483-L527)

compute_metrics(
        x, y, y_pred, sample_weight=None
    )

Update metric states and collect all metrics to be returned.

Subclasses can optionally override this method to provide custom metric updating and collection logic. Custom metrics are not passed in `compile()`, they can be created in `__init__` or `build`. They are automatically tracked and returned by `self.metrics`.

#### Example:

class MyModel(Sequential):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.custom_metric = MyMetric(name="custom_metric")
    
        def compute_metrics(self, x, y, y_pred, sample_weight):
            # This super call updates metrics from `compile` and returns
            # results for all metrics listed in `self.metrics`.
            metric_results = super().compute_metrics(
                x, y, y_pred, sample_weight)
    
            # `metric_results` contains the previous result for
            # `custom_metric`, this is where we update it.
            self.custom_metric.update_state(x, y, y_pred, sample_weight)
            metric_results['custom_metric'] = self.custom_metric.result()
            return metric_results

|     |     |
| --- | --- |
| Args |     |
| `x` | Input data. |
| `y` | Target data. |
| `y_pred` | Predictions returned by the model output of `model.call(x)`. |
| `sample_weight` | Sample weights for weighting the loss function. |

|     |     |
| --- | --- |
| Returns |     |
| A `dict` containing values that will be passed to [`keras.callbacks.CallbackList.on_train_batch_end()`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/CallbackList#on_train_batch_end)<br>. Typically, the values of the metrics listed in `self.metrics` are returned. |     |
| `Example` | `{'loss': 0.2, 'accuracy': 0.7}`. |

### `evaluate`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L455-L519)

evaluate(
        x=None,
        y=None,
        batch_size=None,
        verbose='auto',
        sample_weight=None,
        steps=None,
        callbacks=None,
        return_dict=False,
        **kwargs
    )

Returns the loss value & metrics values for the model in test mode.

Computation is done in batches (see the `batch_size` arg.)

|     |     |
| --- | --- |
| Args |     |
| `x` | Input data. It can be:<br><br>*   A NumPy array (or array-like), or a list of arrays (in case the model has multiple inputs).<br>*   A backend-native tensor, or a list of tensors (in case the model has multiple inputs).<br>*   A dict mapping input names to the corresponding array/tensors, if the model has named inputs.<br>*   A [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>     returning `(inputs, targets)` or `(inputs, targets, sample_weights)`.<br>*   A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>     yielding `(inputs, targets)` or `(inputs, targets, sample_weights)`.<br>*   A `torch.utils.data.DataLoader` yielding `(inputs, targets)` or `(inputs, targets, sample_weights)`.<br>*   A Python generator function yielding `(inputs, targets)` or `(inputs, targets, sample_weights)`. |
| `y` | Target data. Like the input data `x`, it can be either NumPy array(s) or backend-native tensor(s). If `x` is a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, `torch.utils.data.DataLoader` or a Python generator function, `y` should not be specified since targets will be obtained from `x`. |
| `batch_size` | Integer or `None`. Number of samples per batch of computation. If unspecified, `batch_size` will default to 32. Do not specify the `batch_size` if your input data `x` is a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, `torch.utils.data.DataLoader` or Python generator function since they generate batches. |
| `verbose` | `"auto"`, 0, 1, or 2. Verbosity mode. 0 = silent, 1 = progress bar, 2 = single line. `"auto"` becomes 1 for most cases. Note that the progress bar is not particularly useful when logged to a file, so `verbose=2` is recommended when not running interactively (e.g. in a production environment). Defaults to `"auto"`. |
| `sample_weight` | Optional NumPy array or tensor of weights for the training samples, used for weighting the loss function (during training only). You can either pass a flat (1D) NumPy array or tensor with the same length as the input samples (1:1 mapping between weights and samples), or in the case of temporal data, you can pass a 2D NumPy array or tensor with shape `(samples, sequence_length)` to apply a different weight to every timestep of every sample. This argument is not supported when `x` is a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, `torch.utils.data.DataLoader` or Python generator function. Instead, provide `sample_weights` as the third element of `x`. Note that sample weighting does not apply to metrics specified via the `metrics` argument in `compile()`. To apply sample weighting to your metrics, you can specify them via the `weighted_metrics` in `compile()` instead. |
| `steps` | Integer or `None`. Total number of steps (batches of samples) to draw before declaring the evaluation round finished. If `steps` is `None`, it will run until `x` is exhausted. In the case of an infinitely repeating dataset, it will run indefinitely. |
| `callbacks` | List of [`keras.callbacks.Callback`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/Callback)<br> instances. List of callbacks to apply during evaluation. |
| `return_dict` | If `True`, loss and metric results are returned as a dict, with each key being the name of the metric. If `False`, they are returned as a list. |

|     |
| --- |
| Returns |     |
| Scalar test loss (if the model has a single output and no metrics) or list of scalars (if the model has multiple outputs and/or metrics). |     |

### `export`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L654-L862)

export(
        filepath,
        format='tf_saved_model',
        verbose=None,
        input_signature=None,
        **kwargs
    )

Export the model as an artifact for inference.

|     |     |
| --- | --- |
| Args |     |
| `filepath` | `str` or `pathlib.Path` object. The path to save the artifact. |
| `format` | `str`. The export format. Supported values: `"tf_saved_model"`, `"onnx"`, `"openvino"`, `"litert"`, and `"torch"`. Defaults to `"tf_saved_model"`. |
| `verbose` | `bool`. Whether to print a message during export. Defaults to `None`, which uses the default value set by different backends and formats. |
| `input_signature` | Optional. Specifies the shape and dtype of the model inputs. Can be a structure of [`keras.InputSpec`](https://www.tensorflow.org/api_docs/python/tf/keras/InputSpec)<br>, [`tf.TensorSpec`](https://www.tensorflow.org/api_docs/python/tf/TensorSpec)<br>, `backend.KerasTensor`, or backend tensor. If not provided, it will be automatically computed. Defaults to `None`. Note: With `format="litert"` and the PyTorch backend, dynamic input shapes are not supported. Any dynamic dimensions (i.e., `None` in input shapes) will be automatically replaced with `1` during export, which may cause runtime failures for other shapes. You must explicitly pass a fixed static `input_signature` matching your maximum runtime shape. |
| `**kwargs` | Additional keyword arguments.<br><br>*   `is_static`: Optional `bool`. Specific to the JAX backend and `format="tf_saved_model"`. Indicates whether `fn` is static. Set to `False` if `fn` involves state updates (e.g., RNG seeds and counters).<br>*   `jax2tf_kwargs`: Optional `dict`. Specific to the JAX backend and `format="tf_saved_model"`. Arguments for `jax2tf.convert`. See the documentation for [`jax2tf.convert`](https://github.com/google/jax/blob/main/jax/experimental/jax2tf/README.md)<br>    . If `native_serialization` and `polymorphic_shapes` are not provided, they will be automatically computed.<br>*   `opset_version`: Optional `int`. Specific to `format="onnx"`. An integer value that specifies the ONNX opset version.<br>*   LiteRT-specific options: Optional keyword arguments specific to `format="litert"`. These are passed directly to the TensorFlow Lite converter on the TensorFlow backend and include options like `optimizations`, `representative_dataset`, `experimental_new_quantizer`, `allow_custom_ops`, `enable_select_tf_ops`, etc. On the PyTorch backend, LiteRT export accepts `optimizations` plus the installed `litert_torch.convert()` keyword arguments such as `strict_export`, `dynamic_shapes` (note that standard ops do not support dynamic shapes, as noted below), `lightweight_conversion`, `enable_x64`, `runtime_constant_folding`, and `quant_config`.<br>*   PyTorch export options: Optional keyword arguments specific to `format="torch"`. These are passed directly to `torch.export.export` and include `strict`, `dynamic_shapes`, `prefer_deferred_runtime_asserts_over_guards`, and `preserve_module_call_signature`. |

**Note on LiteRT (TFLite) Export with PyTorch Backend:** With the PyTorch backend, LiteRT export (`format="litert"`) does not support dynamic input shapes. If no static signature is provided, any dynamic dimensions (represented as `None`) are automatically replaced with `1` during export. This can lead to runtime failures for other shapes. You must explicitly specify a fixed static `input_signature` (matching your maximum runtime dimensions) and pad your inputs to this static shape at runtime.

#### Examples:

Here's how to export a TensorFlow SavedModel for inference.

# Export the model as a TensorFlow SavedModel artifact
    model.export("path/to/location", format="tf_saved_model")
    
    # Load the artifact in a different process/environment
    reloaded_artifact = tf.saved_model.load("path/to/location")
    predictions = reloaded_artifact.serve(input_data)

Here's how to export an ONNX for inference.

# Export the model as a ONNX artifact
    model.export("path/to/location", format="onnx")
    
    # Load the artifact in a different process/environment
    ort_session = onnxruntime.InferenceSession("path/to/location")
    ort_inputs = {
        k.name: v for k, v in zip(ort_session.get_inputs(), input_data)
    }
    predictions = ort_session.run(None, ort_inputs)

Here's how to export a LiteRT (TFLite) for inference.

# Export the model as a LiteRT artifact
    model.export("path/to/location", format="litert")
    
    # Load the artifact in a different process/environment
    interpreter = tf.lite.Interpreter(model_path="path/to/location")
    interpreter.allocate_tensors()
    interpreter.set_tensor(
        interpreter.get_input_details()[0]['index'], input_data
    )
    interpreter.invoke()
    output_data = interpreter.get_tensor(
        interpreter.get_output_details()[0]['index']
    )

Here's how to export a PyTorch ExportedProgram for inference.

# Export the model as a PyTorch ExportedProgram artifact
    model.export("path/to/model.pt2", format="torch")
    
    # Load the artifact in a different process/environment
    import torch
    loaded_program = torch.export.load("path/to/model.pt2")
    predictions = loaded_program.module()(input_tensor)

### `fit`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L314-L453)

fit(
        x=None,
        y=None,
        batch_size=None,
        epochs=1,
        verbose='auto',
        callbacks=None,
        validation_split=0.0,
        validation_data=None,
        shuffle=True,
        class_weight=None,
        sample_weight=None,
        initial_epoch=0,
        steps_per_epoch=None,
        validation_steps=None,
        validation_batch_size=None,
        validation_freq=1
    )

Trains the model for a fixed number of epochs (dataset iterations).

|     |     |
| --- | --- |
| Args |     |
| `x` | Input data. It can be:<br><br>*   A NumPy array (or array-like), or a list of arrays (in case the model has multiple inputs).<br>*   A backend-native tensor, or a list of tensors (in case the model has multiple inputs).<br>*   A dict mapping input names to the corresponding array/tensors, if the model has named inputs.<br>*   A [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>     returning `(inputs, targets)` or `(inputs, targets, sample_weights)`.<br>*   A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>     yielding `(inputs, targets)` or `(inputs, targets, sample_weights)`.<br>*   A `torch.utils.data.DataLoader` yielding `(inputs, targets)` or `(inputs, targets, sample_weights)`.<br>*   A Python generator function yielding `(inputs, targets)` or `(inputs, targets, sample_weights)`. |
| `y` | Target data. Like the input data `x`, it can be either NumPy array(s) or backend-native tensor(s). If `x` is a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, `torch.utils.data.DataLoader` or a Python generator function, `y` should not be specified since targets will be obtained from `x`. |
| `batch_size` | Integer or `None`. Number of samples per gradient update. If unspecified, `batch_size` will default to 32. Do not specify the `batch_size` if your input data `x` is a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, `torch.utils.data.DataLoader` or Python generator function since they generate batches. |
| `epochs` | Integer. Number of epochs to train the model. An epoch is an iteration over the entire `x` and `y` data provided (unless the `steps_per_epoch` flag is set to something other than None). Note that in conjunction with `initial_epoch`, `epochs` is to be understood as "final epoch". The model is not trained for a number of iterations given by `epochs`, but merely until the epoch of index `epochs` is reached. |
| `verbose` | `"auto"`, 0, 1, or 2. Verbosity mode. 0 = silent, 1 = progress bar, 2 = one line per epoch. "auto" becomes 1 for most cases. Note that the progress bar is not particularly useful when logged to a file, so `verbose=2` is recommended when not running interactively (e.g., in a production environment). Defaults to `"auto"`. |
| `callbacks` | List of [`keras.callbacks.Callback`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/Callback)<br> instances. List of callbacks to apply during training. See [`keras.callbacks`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks)<br>. Note [`keras.callbacks.ProgbarLogger`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ProgbarLogger)<br> and [`keras.callbacks.History`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/History)<br> callbacks are created automatically and need not be passed to `model.fit()`. [`keras.callbacks.ProgbarLogger`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ProgbarLogger)<br> is created or not based on the `verbose` argument in `model.fit()`. |
| `validation_split` | Float between 0 and 1. Fraction of the training data to be used as validation data. The model will set apart this fraction of the training data, will not train on it, and will evaluate the loss and any model metrics on this data at the end of each epoch. The validation data is selected from the last samples in the `x` and `y` data provided, before shuffling. This argument is only supported when `x` and `y` are made of NumPy arrays or tensors. If both `validation_data` and `validation_split` are provided, `validation_data` will override `validation_split`. |
| `validation_data` | Data on which to evaluate the loss and any model metrics at the end of each epoch. The model will not be trained on this data. Thus, note the fact that the validation loss of data provided using `validation_split` or `validation_data` is not affected by regularization layers like noise and dropout. `validation_data` will override `validation_split`. It can be:*   A tuple `(x_val, y_val)` of NumPy arrays or tensors.<br>*   A tuple `(x_val, y_val, val_sample_weights)` of NumPy arrays.<br>*   A [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>    , a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>    , a `torch.utils.data.DataLoader` yielding `(inputs, targets)` or a Python generator function yielding `(x_val, y_val)` or `(inputs, targets, sample_weights)`. |
| `shuffle` | Boolean, whether to shuffle the training data before each epoch. This argument is ignored when `x` is a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, `torch.utils.data.DataLoader` or Python generator function. |
| `class_weight` | Optional dictionary mapping class indices (integers) to a weight (float) value, used for weighting the loss function (during training only). This can be useful to tell the model to "pay more attention" to samples from an under-represented class. When `class_weight` is specified and targets have a rank of 2 or greater, either `y` must be one-hot encoded, or an explicit final dimension of `1` must be included for sparse class labels. |
| `sample_weight` | Optional NumPy array or tensor of weights for the training samples, used for weighting the loss function (during training only). You can either pass a flat (1D) NumPy array or tensor with the same length as the input samples (1:1 mapping between weights and samples), or in the case of temporal data, you can pass a 2D NumPy array or tensor with shape `(samples, sequence_length)` to apply a different weight to every timestep of every sample. This argument is not supported when `x` is a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, `torch.utils.data.DataLoader` or Python generator function. Instead, provide `sample_weights` as the third element of `x`. Note that sample weighting does not apply to metrics specified via the `metrics` argument in `compile()`. To apply sample weighting to your metrics, you can specify them via the `weighted_metrics` in `compile()` instead. |
| `initial_epoch` | Integer. Epoch at which to start training (useful for resuming a previous training run). |
| `steps_per_epoch` | Integer or `None`. Total number of steps (batches of samples) before declaring one epoch finished and starting the next epoch. When training with input tensors or NumPy arrays, the default `None` means that the value used is the number of samples in your dataset divided by the batch size, or 1 if that cannot be determined. If `x` is a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, `torch.utils.data.DataLoader` or Python generator function, the epoch will run until the input dataset is exhausted. When passing an infinitely repeating dataset, you must specify the `steps_per_epoch` argument, otherwise the training will run indefinitely. |
| `validation_steps` | Integer or `None`. Only relevant if `validation_data` is provided. Total number of steps (batches of samples) to draw before stopping when performing validation at the end of every epoch. If `validation_steps` is `None`, validation will run until the `validation_data` dataset is exhausted. In the case of an infinitely repeating dataset, it will run indefinitely. If `validation_steps` is specified and only part of the dataset is consumed, the evaluation will start from the beginning of the dataset at each epoch. This ensures that the same validation samples are used every time. |
| `validation_batch_size` | Integer or `None`. Number of samples per validation batch. If unspecified, will default to `batch_size`. Do not specify the `validation_batch_size` if your data is a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, `torch.utils.data.DataLoader` or Python generator function since they generate batches. |
| `validation_freq` | Only relevant if validation data is provided. Specifies how many training epochs to run before a new validation run is performed, e.g. `validation_freq=2` runs validation every 2 epochs. |

Unpacking behavior for iterator-like inputs: A common pattern is to pass an iterator like object such as a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 or a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)
 to `fit()`, which will in fact yield not only features (`x`) but optionally targets (`y`) and sample weights (`sample_weight`). Keras requires that the output of such iterator-likes be unambiguous. The iterator should return a tuple of length 1, 2, or 3, where the optional second and third elements will be used for `y` and `sample_weight` respectively. Any other type provided will be wrapped in a length-one tuple, effectively treating everything as `x`. When yielding dicts, they should still adhere to the top-level tuple structure, e.g. `({"x0": x0, "x1": x1}, y)`. Keras will not attempt to separate features, targets, and weights from the keys of a single dict. A notable unsupported data type is the `namedtuple`. The reason is that it behaves like both an ordered datatype (tuple) and a mapping datatype (dict). So given a namedtuple of the form: `namedtuple("example_tuple", ["y", "x"])` it is ambiguous whether to reverse the order of the elements when interpreting the value. Even worse is a tuple of the form: `namedtuple("other_tuple", ["x", "y", "z"])` where it is unclear if the tuple was intended to be unpacked into `x`, `y`, and `sample_weight` or passed through as a single element to `x`.

|     |
| --- |
| Returns |     |
| A `History` object. Its `History.history` attribute is a record of training loss values and metrics values at successive epochs, as well as validation loss values and validation metrics values (if applicable). |     |

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distillation/distiller.py#L581-L598)

@classmethod

Create instance from configuration.

### `get_compile_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/trainers/trainer.py#L981-L992)

get_compile_config()

Returns a serialized config with information for compiling the model.

This method returns a config dictionary containing all the information (optimizer, loss, metrics, etc.) with which the model was compiled.

|     |
| --- |
| Returns |     |
| A dict containing information for compiling the model. |     |

### `get_layer`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L181-L220)

get_layer(
        name=None, index=None
    )

Retrieves a layer based on either its name (unique) or index.

If `name` and `index` are both provided, `index` will take precedence. Indices are based on order of horizontal graph traversal (bottom-up).

|     |     |
| --- | --- |
| Args |     |
| `name` | String, name of layer. |
| `index` | Integer, index of layer. |

|     |
| --- |
| Returns |     |
| A layer instance. |     |

### `get_metrics_result`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/trainers/trainer.py#L529-L546)

get_metrics_result()

Returns the model's metrics values as a dict.

If any of the metric result is a dict (containing multiple metrics), each of them gets added to the top level returned dict of this method.

|     |     |
| --- | --- |
| Returns |     |
| A `dict` containing values of the metrics listed in `self.metrics`. |     |
| `Example` | `{'loss': 0.2, 'accuracy': 0.7}`. |

### `get_quantization_layer_structure`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L427-L448)

get_quantization_layer_structure(
        mode=None
    )

Returns the quantization structure for the model.

This method is intended to be overridden by model authors to provide topology information required for structure-aware quantization modes like 'gptq'.

|     |     |
| --- | --- |
| Args |     |
| `mode` | The quantization mode. |

|     |
| --- |
| Returns |     |
| A dictionary describing the topology, e.g.: `{'pre_block_layers': [list], 'sequential_blocks': [list]}` or `None` if the mode does not require structure or is not supported. `'pre_block_layers'` is a list of layers that the inputs should be passed through, before being passed to the sequential blocks. For example, inputs to an LLM must first be passed through an embedding layer, followed by the transformer. |     |

### `get_state_tree`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L924-L1002)

get_state_tree(
        value_format='backend_tensor'
    )

Retrieves tree-like structure of model variables.

This method allows retrieval of different model variables (trainable, non-trainable, optimizer, and metrics). The variables are returned in a nested dictionary format, where the keys correspond to the variable names and the values are the nested representations of the variables.

|     |     |
| --- | --- |
| Returns |     |
| `dict` | A dictionary containing the nested representations of the requested variables. The keys are the variable names, and the values are the corresponding nested dictionaries. |
| `value_format` | One of `"backend_tensor"`, `"numpy_array"`. The kind of array to return as the leaves of the nested state tree. |

#### Example:

model = keras.Sequential([\
        keras.Input(shape=(1,), name="my_input"),\
        keras.layers.Dense(1, activation="sigmoid", name="my_dense"),\
    ], name="my_sequential")
    model.compile(optimizer="adam", loss="mse", metrics=["mae"])
    model.fit(np.array([[1.0]]), np.array([[1.0]]))
    state_tree = model.get_state_tree()

The `state_tree` dictionary returned looks like:

{
        'metrics_variables': {
            'loss': {
                'count': ...,
                'total': ...,
            },
            'mean_absolute_error': {
                'count': ...,
                'total': ...,
            }
        },
        'trainable_variables': {
            'my_sequential': {
                'my_dense': {
                    'bias': ...,
                    'kernel': ...,
                }
            }
        },
        'non_trainable_variables': {},
        'optimizer_variables': {
            'adam': {
                    'iteration': ...,
                    'learning_rate': ...,
                    'my_sequential_my_dense_bias_momentum': ...,
                    'my_sequential_my_dense_bias_velocity': ...,
                    'my_sequential_my_dense_kernel_momentum': ...,
                    'my_sequential_my_dense_kernel_velocity': ...,
                }
            }
        }
    }

### `load_weights`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L377-L425)

load_weights(
        filepath, skip_mismatch=False, **kwargs
    )

Load the weights from a single file or sharded files.

Weights are loaded based on the network's topology. This means the architecture should be the same as when the weights were saved. Note that layers that don't have weights are not taken into account in the topological ordering, so adding or removing layers is fine as long as they don't have weights.

**Partial weight loading**

If you have modified your model, for instance by adding a new layer (with weights) or by changing the shape of the weights of a layer, you can choose to ignore errors and continue loading by setting `skip_mismatch=True`. In this case any layer with mismatching weights will be skipped. A warning will be displayed for each skipped layer.

**Sharding**

When loading sharded weights, it is important to specify `filepath` that ends with `*.weights.json` which is used as the configuration file. Additionally, the sharded files `*_xxxxx.weights.h5` must be in the same directory as the configuration file.

|     |     |
| --- | --- |
| Args |     |
| `filepath` | `str` or `pathlib.Path` object. Path where the weights will be saved. When sharding, the filepath must end in `.weights.json`. |
| `skip_mismatch` | Boolean, whether to skip loading of layers where there is a mismatch in the number of weights, or a mismatch in the shape of the weights. |

#### Example:

# Load the weights in a single file.
    model.load_weights("model.weights.h5")
    
    # Load the weights in sharded files.
    model.load_weights("model.weights.json")

### `loss`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L704-L711)

loss(
        y, y_pred, sample_weight=None
    )

### `make_predict_function`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L264-L312)

make_predict_function(
        force=False
    )

### `make_test_function`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L259-L262)

make_test_function(
        force=False
    )

### `make_train_function`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L254-L257)

make_train_function(
        force=False
    )

### `predict`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L521-L598)

predict(
        x, batch_size=None, verbose='auto', steps=None, callbacks=None
    )

Generates output predictions for the input samples.

Computation is done in batches. This method is designed for batch processing of large numbers of inputs. It is not intended for use inside of loops that iterate over your data and process small numbers of inputs at a time.

For small numbers of inputs that fit in one batch, directly use `__call__()` for faster execution, e.g., `model(x)`, or `model(x, training=False)` if you have layers such as `BatchNormalization` that behave differently during inference.

|     |     |
| --- | --- |
| Args |     |
| `x` | Input data. It can be:<br><br>*   A NumPy array (or array-like), or a list of arrays (in case the model has multiple inputs).<br>*   A backend-native tensor, or a list of tensors (in case the model has multiple inputs).<br>*   A dict mapping input names to the corresponding array/tensors, if the model has named inputs.<br>*   A [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>    .<br>*   A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>    .<br>*   A `torch.utils.data.DataLoader`.<br>*   A Python generator function. |
| `batch_size` | Integer or `None`. Number of samples per batch of computation. If unspecified, `batch_size` will default to 32. Do not specify the `batch_size` if your input data `x` is a [`keras.utils.PyDataset`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/PyDataset)<br>, [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>, `torch.utils.data.DataLoader` or Python generator function since they generate batches. |
| `verbose` | `"auto"`, 0, 1, or 2. Verbosity mode. 0 = silent, 1 = progress bar, 2 = single line. `"auto"` becomes 1 for most cases. Note that the progress bar is not particularly useful when logged to a file, so `verbose=2` is recommended when not running interactively (e.g. in a production environment). Defaults to `"auto"`. |
| `steps` | Total number of steps (batches of samples) to draw before declaring the prediction round finished. If `steps` is `None`, it will run until `x` is exhausted. In the case of an infinitely repeating dataset, it will run indefinitely. |
| `callbacks` | List of [`keras.callbacks.Callback`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/Callback)<br> instances. List of callbacks to apply during prediction. |

|     |
| --- |
| Returns |     |
| NumPy array(s) of predictions. |     |

### `predict_on_batch`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L658-L664)

predict_on_batch(
        x
    )

Returns predictions for a single batch of samples.

|     |     |
| --- | --- |
| Args |     |
| `x` | Input data. It must be array-like. |

|     |
| --- |
| Returns |     |
| NumPy array(s) of predictions. |     |

### `predict_step`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L107-L113)

predict_step(
        data
    )

### `reset_metrics`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distillation/distiller.py#L553-L558)

reset_metrics()

Reset all metrics.

### `save`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L273-L317)

save(
        filepath, overwrite=True, zipped=None, **kwargs
    )

Saves a model as a `.keras` file.

Note that `model.save()` is an alias for `keras.saving.save_model()`.

The saved `.keras` file contains:

*   The model's configuration (architecture)
*   The model's weights
*   The model's optimizer's state (if any)

Thus models can be reinstantiated in the exact same state.

|     |     |
| --- | --- |
| Args |     |
| `filepath` | `str` or `pathlib.Path` object. The path where to save the model. Must end in `.keras` (unless saving the model as an unzipped directory via `zipped=False`). |
| `overwrite` | Whether we should overwrite any existing model at the target location, or instead ask the user via an interactive prompt. |
| `zipped` | Whether to save the model as a zipped `.keras` archive (default when saving locally), or as an unzipped directory (default when saving on the Hugging Face Hub). |

#### Example:

model = keras.Sequential(
        [\
            keras.layers.Dense(5, input_shape=(3,)),\
            keras.layers.Softmax(),\
        ],
    )
    model.save("model.keras")
    loaded_model = keras.saving.load_model("model.keras")
    x = keras.random.uniform((10, 3))
    assert np.allclose(model.predict(x), loaded_model.predict(x))

### `save_weights`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L319-L375)

save_weights(
        filepath, overwrite=True, max_shard_size=None
    )

Saves all weights to a single file or sharded files.

By default, the weights will be saved in a single `.weights.h5` file. If sharding is enabled (`max_shard_size` is not `None`), the weights will be saved in multiple files, each with a size at most `max_shard_size` (in GB). Additionally, a configuration file `.weights.json` will contain the metadata for the sharded files.

The saved sharded files contain:

*   `*.weights.json`: The configuration file containing 'metadata' and 'weight\_map'.
*   `*_xxxxxx.weights.h5`: The sharded files containing only the weights.

|     |     |
| --- | --- |
| Args |     |
| `filepath` | `str` or `pathlib.Path` object. Path where the weights will be saved. When sharding, the filepath must end in `.weights.json`. If `.weights.h5` is provided, it will be overridden. |
| `overwrite` | Whether to overwrite any existing weights at the target location or instead ask the user via an interactive prompt. |
| `max_shard_size` | `int` or `float`. Maximum size in GB for each sharded file. If `None`, no sharding will be done. Defaults to `None`. |

#### Example:

# Instantiate a EfficientNetV2L model with about 454MB of weights.
    model = keras.applications.EfficientNetV2L(weights=None)
    
    # Save the weights in a single file.
    model.save_weights("model.weights.h5")
    
    # Save the weights in sharded files. Use `max_shard_size=0.25` means
    # each sharded file will be at most ~250MB.
    model.save_weights("model.weights.json", max_shard_size=0.25)
    
    # Load the weights in a new model with the same architecture.
    loaded_model = keras.applications.EfficientNetV2L(weights=None)
    loaded_model.load_weights("model.weights.h5")
    x = keras.random.uniform((1, 480, 480, 3))
    assert np.allclose(model.predict(x), loaded_model.predict(x))
    
    # Load the sharded weights in a new model with the same architecture.
    loaded_model = keras.applications.EfficientNetV2L(weights=None)
    loaded_model.load_weights("model.weights.json")
    x = keras.random.uniform((1, 480, 480, 3))
    assert np.allclose(model.predict(x), loaded_model.predict(x))

### `set_state_tree`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L1037-L1076)

set_state_tree(
        state_tree
    )

Assigns values to variables of the model.

This method takes a dictionary of nested variable values, which represents the state tree of the model, and assigns them to the corresponding variables of the model. The dictionary keys represent the variable names (e.g., `'trainable_variables'`, `'optimizer_variables'`), and the values are nested dictionaries containing the variable paths and their corresponding values.

|     |     |
| --- | --- |
| Args |     |
| `state_tree` | A dictionary representing the state tree of the model. The keys are the variable names, and the values are nested dictionaries representing the variable paths and their values. |

### `stateless_compute_loss`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/trainers/trainer.py#L439-L481)

stateless_compute_loss(
        trainable_variables,
        non_trainable_variables,
        metrics_variables,
        x=None,
        y=None,
        y_pred=None,
        sample_weight=None,
        training=True
    )

### `summary`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L222-L271)

summary(
        line_length=None,
        positions=None,
        print_fn=None,
        expand_nested=False,
        show_trainable=False,
        layer_range=None
    )

Prints a string summary of the network.

|     |     |
| --- | --- |
| Args |     |
| `line_length` | Total length of printed lines (e.g. set this to adapt the display to different terminal window sizes). |
| `positions` | Relative or absolute positions of log elements in each line. If not provided, becomes `[0.3, 0.6, 0.70, 1.]`. Defaults to `None`. |
| `print_fn` | Print function to use. By default, prints to `stdout`. If `stdout` doesn't work in your environment, change to `print`. It will be called on each line of the summary. You can set it to a custom function in order to capture the string summary. |
| `expand_nested` | Whether to expand the nested models. Defaults to `False`. |
| `show_trainable` | Whether to show if a layer is trainable. Defaults to `False`. |
| `layer_range` | a list or tuple of 2 strings, which is the starting layer name and ending layer name (both inclusive) indicating the range of layers to be printed in summary. It also accepts regex patterns instead of exact names. In this case, the start predicate will be the first element that matches `layer_range[0]` and the end predicate will be the last element that matches `layer_range[1]`. By default `None` considers all layers of the model. |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | if `summary()` is called before the model is built. |

### `test_on_batch`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L635-L656)

test_on_batch(
        x, y=None, sample_weight=None, return_dict=False
    )

Test the model on a single batch of samples.

|     |     |
| --- | --- |
| Args |     |
| `x` | Input data. Must be array-like. |
| `y` | Target data. Must be array-like. |
| `sample_weight` | Optional array of the same length as x, containing weights to apply to the model's loss for each sample. In the case of temporal data, you can pass a 2D array with shape `(samples, sequence_length)`, to apply a different weight to every timestep of every sample. |
| `return_dict` | If `True`, loss and metric results are returned as a dict, with each key being the name of the metric. If `False`, they are returned as a list. |

|     |
| --- |
| Returns |     |
| A scalar loss value (when no metrics and `return_dict=False`), a list of loss and metric values (if there are metrics and `return_dict=False`), or a dict of metric and loss values (if `return_dict=True`). |     |

### `test_step`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L90-L105)

test_step(
        data
    )

### `to_json`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/models/model.py#L636-L652)

to_json(
        **kwargs
    )

Returns a JSON string containing the network configuration.

To load a network from a JSON save file, use [`keras.models.model_from_json(json_string, custom_objects={...})`](https://www.tensorflow.org/api_docs/python/tf/keras/models/model_from_json)
.

|     |     |
| --- | --- |
| Args |     |
| `**kwargs` | Additional keyword arguments to be passed to `json.dumps()`. |

|     |
| --- |
| Returns |     |
| A JSON string. |     |

### `train_on_batch`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L600-L633)

train_on_batch(
        x, y=None, sample_weight=None, class_weight=None, return_dict=False
    )

Runs a single gradient update on a single batch of data.

|     |     |
| --- | --- |
| Args |     |
| `x` | Input data. Must be array-like. |
| `y` | Target data. Must be array-like. |
| `sample_weight` | Optional array of the same length as x, containing weights to apply to the model's loss for each sample. In the case of temporal data, you can pass a 2D array with shape `(samples, sequence_length)`, to apply a different weight to every timestep of every sample. |
| `class_weight` | Optional dictionary mapping class indices (integers) to a weight (float) to apply to the model's loss for the samples from this class during training. This can be useful to tell the model to "pay more attention" to samples from an under-represented class. When `class_weight` is specified and targets have a rank of 2 or greater, either `y` must be one-hot encoded, or an explicit final dimension of 1 must be included for sparse class labels. |
| `return_dict` | If `True`, loss and metric results are returned as a dict, with each key being the name of the metric. If `False`, they are returned as a list. |

|     |
| --- |
| Returns |     |
| A scalar loss value (when no metrics and `return_dict=False`), a list of loss and metric values (if there are metrics and `return_dict=False`), or a dict of metric and loss values (if `return_dict=True`). |     |

### `train_step`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/tensorflow/trainer.py#L53-L88)

train_step(
        data
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-04 UTC.