[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/Input#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/Input)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/Input?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/Input#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/Input#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/Input#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.Input Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/Input#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/Input#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/Input#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/input_layer.py#L145-L221)

Used to instantiate a Keras tensor.

#### View aliases

**Main aliases**

[`tf.keras.layers.Input`](https://www.tensorflow.org/api_docs/python/tf/keras/Input)

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.keras.Input`](https://www.tensorflow.org/api_docs/python/tf/keras/Input)

tf.keras.Input(
        shape=None,
        batch_size=None,
        dtype=None,
        sparse=None,
        ragged=None,
        batch_shape=None,
        name=None,
        tensor=None,
        optional=False
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate \`tf.feature\_column\`s to Keras preprocessing layers](https://www.tensorflow.org/guide/migrate/migrating_feature_columns)<br>    <br>*   [Use TF1.x models in TF2 workflows](https://www.tensorflow.org/guide/migrate/model_mapping)<br>    <br>*   [Extension types](https://www.tensorflow.org/guide/extension_type)<br>    <br>*   [Debug a TensorFlow 2 migrated training pipeline](https://www.tensorflow.org/guide/migrate/migration_debugging)<br>    <br>*   [Migrate from TPU embedding\_columns to TPUEmbedding layer](https://www.tensorflow.org/guide/migrate/tpu_embedding) | *   [Parameter server training with ParameterServerStrategy](https://www.tensorflow.org/tutorials/distribute/parameter_server_training)<br>    <br>*   [pix2pix: Image-to-image translation with a conditional GAN](https://www.tensorflow.org/tutorials/generative/pix2pix)<br>    <br>*   [Classify structured data using Keras preprocessing layers](https://www.tensorflow.org/tutorials/structured_data/preprocessing_layers)<br>    <br>*   [Transfer learning with YAMNet for environmental sound classification](https://www.tensorflow.org/tutorials/audio/transfer_learning_audio)<br>    <br>*   [Load CSV data](https://www.tensorflow.org/tutorials/load_data/csv) |

A Keras tensor is a symbolic tensor-like object, which we augment with certain attributes that allow us to build a Keras model just by knowing the inputs and outputs of the model.

For instance, if `a`, `b` and `c` are Keras tensors, it becomes possible to do: `model = Model(input=[a, b], output=c)`

|     |     |
| --- | --- |
| Args<br>---- |     |
| `shape` | A shape tuple (tuple of integers or `None` objects), not including the batch size. For instance, `shape=(32,)` indicates that the expected input will be batches of 32-dimensional vectors. Elements of this tuple can be `None`; `None` elements represent dimensions where the shape is not known and may vary (e.g. sequence length). |
| `batch_size` | Optional static batch size (integer). |
| `dtype` | The data type expected by the input, as a string (e.g. `"float32"`, `"int32"`...) |
| `sparse` | A boolean specifying whether the expected input will be sparse tensors. Note that, if `sparse` is `False`, sparse tensors can still be passed into the input - they will be densified with a default value of 0. This feature is only supported with the TensorFlow and the JAX backends. Defaults to `False`. |
| `ragged` | A boolean specifying whether the expected input will be ragged tensors. Note that, if `ragged` is `False`, ragged tensors can still be passed into the input - they will be densified with a default value of 0. This feature is only supported with the TensorFlow backend. Defaults to `False`. |
| `batch_shape` | Optional shape tuple (tuple of integers or `None` objects), including the batch size. |
| `name` | Optional name string for the layer. Should be unique in a model (do not reuse the same name twice). It will be autogenerated if it isn't provided. |
| `tensor` | Optional existing tensor to wrap into the `Input` layer. If set, the layer will use this tensor rather than creating a new placeholder tensor. |
| `optional` | Boolean, whether the input is optional or not. An optional input can accept `None` values. |

|     |
| --- |
| Returns<br>------- |     |
| A Keras tensor. |     |

#### Example:

# This is a logistic regression in Keras
    x = Input(shape=(32,))
    y = Dense(16, activation='softmax')(x)
    model = Model(x, y)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.