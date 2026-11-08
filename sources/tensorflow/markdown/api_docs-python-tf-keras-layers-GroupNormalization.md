[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupNormalization#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupNormalization)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupNormalization?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupNormalization#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupNormalization#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupNormalization#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupNormalization#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.GroupNormalization Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupNormalization#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupNormalization#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupNormalization#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/GroupNormalization#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/normalization/group_normalization.py#L11-L250)

Group normalization layer.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.GroupNormalization(
        groups=32,
        axis=-1,
        epsilon=0.001,
        center=True,
        scale=True,
        beta_initializer='zeros',
        gamma_initializer='ones',
        beta_regularizer=None,
        gamma_regularizer=None,
        beta_constraint=None,
        gamma_constraint=None,
        **kwargs
    )

Group Normalization divides the channels into groups and computes within each group the mean and variance for normalization. Empirically, its accuracy is more stable than batch norm in a wide range of small batch sizes, if learning rate is adjusted linearly with batch sizes.

Relation to Layer Normalization: If the number of groups is set to 1, then this operation becomes nearly identical to Layer Normalization (see Layer Normalization docs for details).

Relation to Instance Normalization: If the number of groups is set to the input dimension (number of groups is equal to number of channels), then this operation becomes identical to Instance Normalization. You can achieve this via `groups=-1`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `groups` | Integer, the number of groups for Group Normalization. Can be in the range `[1, N]` where N is the input dimension. The input dimension must be divisible by the number of groups. Defaults to 32. |
| `axis` | Integer or List/Tuple. The axis or axes to normalize across. Typically, this is the features axis/axes. The left-out axes are typically the batch axis/axes. -1 is the last dimension in the input. Defaults to `-1`. |
| `epsilon` | Small float added to variance to avoid dividing by zero. Defaults to 1e-3. |
| `center` | If `True`, add offset of `beta` to normalized tensor. If `False`, `beta` is ignored. Defaults to `True`. |
| `scale` | If `True`, multiply by `gamma`. If `False`, `gamma` is not used. When the next layer is linear (also e.g. `relu`), this can be disabled since the scaling will be done by the next layer. Defaults to `True`. |
| `beta_initializer` | Initializer for the beta weight. Defaults to zeros. |
| `gamma_initializer` | Initializer for the gamma weight. Defaults to ones. |
| `beta_regularizer` | Optional regularizer for the beta weight. None by default. |
| `gamma_regularizer` | Optional regularizer for the gamma weight. None by default. |
| `beta_constraint` | Optional constraint for the beta weight. None by default. |
| `gamma_constraint` | Optional constraint for the gamma weight. None by default. Input shape: Arbitrary. Use the keyword argument `input_shape` (tuple of integers, does not include the samples axis) when using this layer as the first layer in a model. Output shape: Same shape as input. |
| `**kwargs` | Base layer keyword arguments (e.g. `name` and `dtype`). |

#### Reference:

*   [Yuxin Wu & Kaiming He, 2018](https://arxiv.org/abs/1803.08494)
    

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