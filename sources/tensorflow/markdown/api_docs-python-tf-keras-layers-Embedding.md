[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding#args)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding#output-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding#methods)
    *   [enable\_lora](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding#enable_lora)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.Embedding Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding#args)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding#output-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding#methods)
    *   [enable\_lora](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding#enable_lora)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/embedding.py#L20-L792)

Turns nonnegative integers (indexes) into dense vectors of fixed size.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.Embedding(
        input_dim,
        output_dim,
        embeddings_initializer='uniform',
        embeddings_regularizer=None,
        embeddings_constraint=None,
        mask_zero=False,
        weights=None,
        lora_rank=None,
        lora_alpha=None,
        quantization_config=None,
        **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate \`tf.feature\_column\`s to Keras preprocessing layers](https://www.tensorflow.org/guide/migrate/migrating_feature_columns)<br>    <br>*   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor)<br>    <br>*   [Working with preprocessing layers](https://www.tensorflow.org/guide/keras/preprocessing_layers) | *   [Parameter server training with ParameterServerStrategy](https://www.tensorflow.org/tutorials/distribute/parameter_server_training)<br>    <br>*   [Basic text classification](https://www.tensorflow.org/tutorials/keras/text_classification)<br>    <br>*   [Load text](https://www.tensorflow.org/tutorials/load_data/text)<br>    <br>*   [Using side features: feature preprocessing](https://www.tensorflow.org/recommenders/examples/featurization)<br>    <br>*   [Taking advantage of context features](https://www.tensorflow.org/recommenders/examples/context_features) |

e.g. `[[4], [20]] -> [[0.25, 0.1], [0.6, -0.2]]`

This layer can only be used on nonnegative integer inputs of a fixed range.

#### Example:

    model = keras.Sequential()

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input_dim` | Integer. Size of the vocabulary, i.e. maximum integer index + 1. |
| `output_dim` | Integer. Dimension of the dense embedding. |
| `embeddings_initializer` | Initializer for the `embeddings` matrix (see [`keras.initializers`](https://www.tensorflow.org/api_docs/python/tf/keras/initializers)<br>). |
| `embeddings_regularizer` | Regularizer function applied to the `embeddings` matrix (see [`keras.regularizers`](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers)<br>). |
| `embeddings_constraint` | Constraint function applied to the `embeddings` matrix (see [`keras.constraints`](https://www.tensorflow.org/api_docs/python/tf/keras/constraints)<br>). |
| `mask_zero` | Boolean, whether or not the input value 0 is a special "padding" value that should be masked out. This is useful when using recurrent layers which may take variable length input. If this is `True`, then all subsequent layers in the model need to support masking or an exception will be raised. If `mask_zero` is set to `True`, as a consequence, index 0 cannot be used in the vocabulary (`input_dim` should equal size of vocabulary + 1). |
| `weights` | Optional floating-point matrix of size `(input_dim, output_dim)`. The initial embeddings values to use. |
| `lora_rank` | Optional integer. If set, the layer's forward pass will implement LoRA (Low-Rank Adaptation) with the provided rank. LoRA sets the layer's embeddings matrix to non-trainable and replaces it with a delta over the original matrix, obtained via multiplying two lower-rank trainable matrices. This can be useful to reduce the computation cost of fine-tuning large embedding layers. You can also enable LoRA on an existing `Embedding` layer by calling `layer.enable_lora(rank)`. |
| `lora_alpha` | Optional integer. If set, this parameter scales the low-rank adaptation delta (computed as the product of two lower-rank trainable matrices) during the forward pass. The delta is scaled by `lora_alpha / lora_rank`, allowing you to fine-tune the strength of the LoRA adjustment independently of `lora_rank`. |

|     |
| --- |
| Input shape<br>----------- |     |
| 2D tensor with shape: `(batch_size, input_length)`. |     |

|     |
| --- |
| Output shape<br>------------ |     |
| 3D tensor with shape: `(batch_size, input_length, output_dim)`. |     |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `embeddings` |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `variable_serialization_spec` | Returns a dict mapping quantization modes to variable names in order.<br><br>This spec is used by `save_own_variables` and `load_own_variables` to determine the correct ordering of variables during serialization for each quantization mode. `None` means no quantization. |

Methods
-------

### `enable_lora`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/embedding.py#L214-L259)

enable_lora(
        rank,
        lora_alpha=None,
        a_initializer='he_uniform',
        b_initializer='zeros'
    )

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/core/embedding.py#L369-L377)

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