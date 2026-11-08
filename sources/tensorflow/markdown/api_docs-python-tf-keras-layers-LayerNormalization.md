[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LayerNormalization#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LayerNormalization)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LayerNormalization?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FLayerNormalization&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LayerNormalization#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LayerNormalization#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LayerNormalization#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LayerNormalization#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LayerNormalization#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.LayerNormalization Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LayerNormalization#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LayerNormalization#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LayerNormalization#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LayerNormalization#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LayerNormalization#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/normalization/layer_normalization.py#L11-L227)

Layer normalization layer (Ba et al., 2016).

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.LayerNormalization(
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

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Image captioning with visual attention](https://www.tensorflow.org/text/tutorials/image_captioning)<br>    <br>*   [Neural machine translation with a Transformer and Keras](https://www.tensorflow.org/text/tutorials/transformer)<br>    <br>*   [Neural machine translation with attention](https://www.tensorflow.org/text/tutorials/nmt_with_attention) |

Normalize the activations of the previous layer for each given example in a batch independently, rather than across a batch like Batch Normalization. i.e. applies a transformation that maintains the mean activation within each example close to 0 and the activation standard deviation close to 1.

If `scale` or `center` are enabled, the layer will scale the normalized outputs by broadcasting them with a trainable variable `gamma`, and center the outputs by broadcasting with a trainable variable `beta`. `gamma` will default to a ones tensor and `beta` will default to a zeros tensor, so that centering and scaling are no-ops before training has begun.

So, with scaling and centering enabled the normalization equations are as follows:

Let the intermediate activations for a mini-batch to be the `inputs`.

For each sample `x_i` in `inputs` with `k` features, we compute the mean and variance of the sample:

mean_i = sum(x_i[j] for j in range(k)) / k
    var_i = sum((x_i[j] - mean_i) ** 2 for j in range(k)) / k

and then compute a normalized `x_i_normalized`, including a small factor `epsilon` for numerical stability.

x_i_normalized = (x_i - mean_i) / sqrt(var_i + epsilon)

And finally `x_i_normalized` is linearly transformed by `gamma` and `beta`, which are learned parameters:

output_i = x_i_normalized * gamma + beta

`gamma` and `beta` will span the axes of `inputs` specified in `axis`, and this part of the inputs' shape must be fully defined.

#### For example:

    layer = keras.layers.LayerNormalization(axis=[1, 2, 3])

Note that other implementations of layer normalization may choose to define `gamma` and `beta` over a separate set of axes from the axes being normalized across. For example, Group Normalization ([Wu et al. 2018](https://arxiv.org/abs/1803.08494)
) with group size of 1 corresponds to a Layer Normalization that normalizes across height, width, and channel and has `gamma` and `beta` span only the channel dimension. So, this Layer Normalization implementation will not match a Group Normalization layer with group size set to 1.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `axis` | Integer or List/Tuple. The axis or axes to normalize across. Typically, this is the features axis/axes. The left-out axes are typically the batch axis/axes. `-1` is the last dimension in the input. Defaults to `-1`. |
| `epsilon` | Small float added to variance to avoid dividing by zero. Defaults to 1e-3. |
| `center` | If True, add offset of `beta` to normalized tensor. If False, `beta` is ignored. Defaults to `True`. |
| `scale` | If True, multiply by `gamma`. If False, `gamma` is not used. When the next layer is linear (also e.g. [`nn.relu`](https://www.tensorflow.org/api_docs/python/tf/keras/ops/relu)<br>), this can be disabled since the scaling will be done by the next layer. Defaults to `True`. |
| `beta_initializer` | Initializer for the beta weight. Defaults to zeros. |
| `gamma_initializer` | Initializer for the gamma weight. Defaults to ones. |
| `beta_regularizer` | Optional regularizer for the beta weight. None by default. |
| `gamma_regularizer` | Optional regularizer for the gamma weight. None by default. |
| `beta_constraint` | Optional constraint for the beta weight. None by default. |
| `gamma_constraint` | Optional constraint for the gamma weight. None by default. |
| `**kwargs` | Base layer keyword arguments (e.g. `name` and `dtype`). |

#### Reference:

*   [Lei Ba et al., 2016](https://arxiv.org/abs/1607.06450)
    .

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