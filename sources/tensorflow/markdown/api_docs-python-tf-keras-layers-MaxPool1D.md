[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool1D#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool1D)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool1D?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FMaxPool1D&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool1D#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool1D#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool1D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool1D#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool1D#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.MaxPool1D Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool1D#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool1D#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool1D#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool1D#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool1D#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/pooling/max_pooling1d.py#L5-L93)

Max pooling operation for 1D temporal data.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

#### View aliases

**Main aliases**

[`tf.keras.layers.MaxPooling1D`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPool1D)

tf.keras.layers.MaxPool1D(
        pool_size=2,
        strides=None,
        padding='valid',
        data_format=None,
        name=None,
        **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Using Counterfactual Logit Pairing with Keras](https://www.tensorflow.org/responsible_ai/model_remediation/counterfactual/guide/counterfactual_keras) | *   [Wiki Talk Comments Toxicity Prediction](https://www.tensorflow.org/responsible_ai/fairness_indicators/tutorials/Fairness_Indicators_TFCO_Wiki_Case_Study) |

Downsamples the input representation by taking the maximum value over a spatial window of size `pool_size`. The window is shifted by `strides`.

The resulting output when using the `"valid"` padding option has a shape of: `output_shape = (input_shape - pool_size + 1) / strides)`.

The resulting output shape when using the `"same"` padding option is: `output_shape = input_shape / strides`

|     |     |
| --- | --- |
| Args<br>---- |     |
| `pool_size` | int, size of the max pooling window. |
| `strides` | int or None. Specifies how much the pooling window moves for each pooling step. If None, it will default to `pool_size`. |
| `padding` | string, either `"valid"` or `"same"` (case-insensitive). `"valid"` means no padding. `"same"` results in padding evenly to the left/right or up/down of the input such that output has the same height/width dimension as the input. |
| `data_format` | string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, steps, features)` while `"channels_first"` corresponds to inputs with shape `(batch, features, steps)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`. |

#### Input shape:

*   If `data_format="channels_last"`: 3D tensor with shape `(batch_size, steps, features)`.
*   If `data_format="channels_first"`: 3D tensor with shape `(batch_size, features, steps)`.

#### Output shape:

*   If `data_format="channels_last"`: 3D tensor with shape `(batch_size, downsampled_steps, features)`.
*   If `data_format="channels_first"`: 3D tensor with shape `(batch_size, features, downsampled_steps)`.

#### Examples:

`strides=1` and `padding="valid"`:

    x = np.array([1., 2., 3., 4., 5.])

`strides=2` and `padding="valid"`:

    x = np.array([1., 2., 3., 4., 5.])

`strides=1` and `padding="same"`:

    x = np.array([1., 2., 3., 4., 5.])

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