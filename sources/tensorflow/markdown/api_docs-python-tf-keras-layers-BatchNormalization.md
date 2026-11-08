[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/BatchNormalization#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/BatchNormalization)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/BatchNormalization?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FBatchNormalization&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/BatchNormalization#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/BatchNormalization#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/BatchNormalization#call-arguments)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/BatchNormalization#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/BatchNormalization#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/BatchNormalization#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.BatchNormalization Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/BatchNormalization#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/BatchNormalization#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/BatchNormalization#call-arguments)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/BatchNormalization#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/BatchNormalization#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/BatchNormalization#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/normalization/batch_normalization.py#L31-L586)

Layer that normalizes its inputs.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.BatchNormalization(
        axis=-1,
        momentum=0.99,
        epsilon=0.001,
        center=True,
        scale=True,
        beta_initializer='zeros',
        gamma_initializer='ones',
        moving_mean_initializer='zeros',
        moving_variance_initializer='ones',
        beta_regularizer=None,
        gamma_regularizer=None,
        beta_constraint=None,
        gamma_constraint=None,
        renorm=False,
        renorm_clipping=None,
        renorm_momentum=0.99,
        synchronized=False,
        **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Effective Tensorflow 2](https://www.tensorflow.org/guide/effective_tf2)<br>    <br>*   [Advanced automatic differentiation](https://www.tensorflow.org/guide/advanced_autodiff)<br>    <br>*   [Pruning for on-device inference w/ XNNPACK](https://www.tensorflow.org/model_optimization/guide/pruning/pruning_for_on_device_inference)<br>    <br>*   [Sparse weights using structural pruning](https://www.tensorflow.org/model_optimization/guide/pruning/pruning_with_sparsity_2_by_4) | *   [Custom layers](https://www.tensorflow.org/tutorials/customization/custom_layers)<br>    <br>*   [Deep Convolutional Generative Adversarial Network](https://www.tensorflow.org/tutorials/generative/dcgan)<br>    <br>*   [pix2pix: Image-to-image translation with a conditional GAN](https://www.tensorflow.org/tutorials/generative/pix2pix)<br>    <br>*   [Distributed training with DTensors](https://www.tensorflow.org/tutorials/distribute/dtensor_ml_tutorial) |

Batch normalization applies a transformation that maintains the mean output close to 0 and the output standard deviation close to 1.

Importantly, batch normalization works differently during training and during inference.

**During training** (i.e. when using `fit()` or when calling the layer/model with the argument `training=True`), the layer normalizes its output using the mean and standard deviation of the current batch of inputs. That is to say, for each channel being normalized, the layer returns `gamma * (batch - mean(batch)) / sqrt(var(batch) + epsilon) + beta`, where:

*   `epsilon` is small constant (configurable as part of the constructor arguments)
*   `gamma` is a learned scaling factor (initialized as 1), which can be disabled by passing `scale=False` to the constructor.
*   `beta` is a learned offset factor (initialized as 0), which can be disabled by passing `center=False` to the constructor.

**During inference** (i.e. when using `evaluate()` or `predict()` or when calling the layer/model with the argument `training=False` (which is the default), the layer normalizes its output using a moving average of the mean and standard deviation of the batches it has seen during training. That is to say, it returns `gamma * (batch - self.moving_mean) / sqrt(self.moving_var+epsilon) + beta`.

`self.moving_mean` and `self.moving_var` are non-trainable variables that are updated each time the layer in called in training mode, as such:

*   `moving_mean = moving_mean * momentum + mean(batch) * (1 - momentum)`
*   `moving_var = moving_var * momentum + var(batch) * (1 - momentum)`

As such, the layer will only normalize its inputs during inference _after having been trained on data that has similar statistics as the inference data_.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `axis` | Integer, the axis that should be normalized (typically the features axis). For instance, after a `Conv2D` layer with `data_format="channels_first"`, use `axis=1`. |
| `momentum` | Momentum for the moving average. |
| `epsilon` | Small float added to variance to avoid dividing by zero. |
| `center` | If `True`, add offset of `beta` to normalized tensor. If `False`, `beta` is ignored. |
| `scale` | If `True`, multiply by `gamma`. If `False`, `gamma` is not used. When the next layer is linear this can be disabled since the scaling will be done by the next layer. |
| `beta_initializer` | Initializer for the beta weight. |
| `gamma_initializer` | Initializer for the gamma weight. |
| `moving_mean_initializer` | Initializer for the moving mean. |
| `moving_variance_initializer` | Initializer for the moving variance. |
| `beta_regularizer` | Optional regularizer for the beta weight. |
| `gamma_regularizer` | Optional regularizer for the gamma weight. |
| `beta_constraint` | Optional constraint for the beta weight. |
| `gamma_constraint` | Optional constraint for the gamma weight. |
| `synchronized` | Only applicable with the TensorFlow backend. If `True`, synchronizes the global batch statistics (mean and variance) for the layer across all devices at each training step in a distributed training strategy. If `False`, each replica uses its own local batch statistics. |
| `renorm` | Whether to use [Batch Renormalization](https://arxiv.org/abs/1702.03275)<br>. This adds extra variables during training. The inference is the same for either value of this parameter. |
| `renorm_clipping` | Dictionary, valid only if `renorm = True`. Maps optional keys `"rmax"`, `"rmin"`, `"dmax"` to floats used to clip the renorm correction. The correction `(r, d)` is used as `corrected_value = normalized_value * r + d`, with `r` clipped to `[rmin, rmax]`, and `d` to `[-dmax, dmax]`. Missing `rmax`, `rmin`, `dmax` are set to `inf`, `0`, `inf`, respectively. |
| `renorm_momentum` | Momentum used to update the moving means and standard deviations with renorm. Valid only if `renorm= True`. Unlike `momentum`, this affects training and should be neither too small (which would add noise) nor too large (which would give stale estimates). Note that `momentum` is still applied to get the means and variances for inference. |
| `**kwargs` | Base layer keyword arguments (e.g. `name` and `dtype`). |

|     |     |
| --- | --- |
| Call arguments<br>-------------- |     |
| `inputs` | Input tensor (of any rank). |
| `training` | Python boolean indicating whether the layer should behave in training mode or in inference mode.<br><br>*   `training=True`: The layer will normalize its inputs using the mean and variance of the current batch of inputs.<br>*   `training=False`: The layer will normalize its inputs using the mean and variance of its moving statistics, learned during training. |
| `mask` | Binary tensor of shape broadcastable to `inputs` tensor, with `True` values indicating the positions for which mean and variance should be computed. Masked elements of the current inputs are not taken into account for mean and variance computation during training. Any prior unmasked element values will be taken into account until their momentum expires. |

#### Reference:

*   [Ioffe and Szegedy, 2015](https://arxiv.org/abs/1502.03167)
    .

**About setting `layer.trainable = False` on a `BatchNormalization` layer:**

The meaning of setting `layer.trainable = False` is to freeze the layer, i.e. its internal state will not change during training: its trainable weights will not be updated during `fit()` or `train_on_batch()`, and its state updates will not be run.

Usually, this does not necessarily mean that the layer is run in inference mode (which is normally controlled by the `training` argument that can be passed when calling a layer). "Frozen state" and "inference mode" are two separate concepts.

However, in the case of the `BatchNormalization` layer, **setting `trainable = False` on the layer means that the layer will be subsequently run in inference mode** (meaning that it will use the moving mean and the moving variance to normalize the current batch, rather than using the mean and variance of the current batch).

#### Note that:

*   Setting `trainable` on an model containing other layers will recursively set the `trainable` value of all inner layers.
*   If the value of the `trainable` attribute is changed after calling `compile()` on a model, the new value doesn't take effect for this model until `compile()` is called again.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/operation.py#L322-L362)

@classmethod

Creates an operation from its config.

This method is the reverse of `get_config`, capable of instantiating the same operation from the config dictionary.

if "dtype" in config and isinstance(config["dtype"], dict):
        policy = dtype_policies.deserialize(config["dtype"])

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary, typically the output of `get_config`. |

|     |
| --- |
| Returns |     |
| An operation instance. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.