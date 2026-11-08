[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/HashedCrossing#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/HashedCrossing)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/HashedCrossing?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/HashedCrossing#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/HashedCrossing#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/HashedCrossing#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/HashedCrossing#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.HashedCrossing Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/HashedCrossing#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/HashedCrossing#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/HashedCrossing#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/HashedCrossing#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/hashed_crossing.py#L11-L229)

A preprocessing layer which crosses features using the "hashing trick".

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.HashedCrossing(
        num_bins,
        output_mode='int',
        sparse=False,
        name=None,
        dtype=None,
        **kwargs
    )

This layer performs crosses of categorical features using the "hashing trick". Conceptually, the transformation can be thought of as: `hash(concatenate(features)) % num_bins`.

This layer currently only performs crosses of scalar inputs and batches of scalar inputs. Valid input shapes are `(batch_size, 1)`, `(batch_size,)` and `()`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_bins` | Number of hash bins. |
| `output_mode` | Specification for the output of the layer. Values can be `"int"`, or `"one_hot"` configuring the layer as follows:<br><br>*   `"int"`: Return the integer bin indices directly.<br>*   `"one_hot"`: Encodes each individual element in the input into an array the same size as `num_bins`, containing a 1 at the input's bin index. Defaults to `"int"`. |
| `sparse` | Boolean. Only applicable to `"one_hot"` mode and only valid when using the TensorFlow backend. If `True`, returns a `SparseTensor` instead of a dense `Tensor`. Defaults to `False`. |
| `**kwargs` | Keyword arguments to construct a layer. |

#### Examples:

**Crossing two scalar features.**

    layer = keras.layers.HashedCrossing(

**Crossing and one-hotting two scalar features.**

    layer = keras.layers.HashedCrossing(

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