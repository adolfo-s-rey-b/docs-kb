[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Concatenate#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.Concatenate Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/merging/concatenate.py#L8-L163)

Concatenates a list of inputs.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.Concatenate(
        axis=-1, **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate \`tf.feature\_column\`s to Keras preprocessing layers](https://www.tensorflow.org/guide/migrate/migrating_feature_columns)<br>    <br>*   [Migrate from TPU embedding\_columns to TPUEmbedding layer](https://www.tensorflow.org/guide/migrate/tpu_embedding) | *   [Load a pandas DataFrame](https://www.tensorflow.org/tutorials/load_data/pandas_dataframe)<br>    <br>*   [Load CSV data](https://www.tensorflow.org/tutorials/load_data/csv)<br>    <br>*   [pix2pix: Image-to-image translation with a conditional GAN](https://www.tensorflow.org/tutorials/generative/pix2pix)<br>    <br>*   [Image segmentation](https://www.tensorflow.org/tutorials/images/segmentation)<br>    <br>*   [Networks](https://www.tensorflow.org/agents/tutorials/8_networks_tutorial) |

It takes as input a list of tensors, all of the same shape except for the concatenation axis, and returns a single tensor that is the concatenation of all inputs.

#### Examples:

    x = np.arange(20).reshape(2, 2, 5)

Usage in a Keras model:

    x1 = keras.layers.Dense(8)(np.arange(10).reshape(5, 2))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `axis` | Axis along which to concatenate. |
| `**kwargs` | Standard layer keyword arguments. |

|     |
| --- |
| Returns<br>------- |     |
| A tensor, the concatenation of the inputs alongside axis `axis`. |     |

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