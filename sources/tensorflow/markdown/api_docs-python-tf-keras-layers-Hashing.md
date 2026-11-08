[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Hashing#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Hashing)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Hashing?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Hashing#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Hashing#args)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Hashing#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Hashing#output-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Hashing#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Hashing#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Hashing#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.Hashing Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Hashing#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Hashing#args)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Hashing#input-shape)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Hashing#output-shape)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Hashing#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Hashing#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Hashing#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/hashing.py#L10-L299)

A preprocessing layer which hashes and bins categorical features.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.Hashing(
        num_bins,
        mask_value=None,
        salt=None,
        output_mode='int',
        sparse=False,
        **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Working with preprocessing layers](https://www.tensorflow.org/guide/keras/preprocessing_layers) | *   [Using side features: feature preprocessing](https://www.tensorflow.org/recommenders/examples/featurization)<br>    <br>*   [Unified Embedding Tables (UET)](https://www.tensorflow.org/recommenders/examples/uet) |

This layer transforms categorical inputs to hashed output. It element-wise converts a ints or strings to ints in a fixed range. The stable hash function uses `tensorflow::ops::Fingerprint` to produce the same output consistently across all platforms.

This layer uses [FarmHash64](https://github.com/google/farmhash)
 by default, which provides a consistent hashed output across different platforms and is stable across invocations, regardless of device and context, by mixing the input bits thoroughly.

If you want to obfuscate the hashed output, you can also pass a random `salt` argument in the constructor. In that case, the layer will use the [SipHash64](https://github.com/google/highwayhash)
 hash function, with the `salt` value serving as additional input to the hash function.

**Example (FarmHash64)**

    layer = keras.layers.Hashing(num_bins=3)

**Example (FarmHash64) with a mask value**

    layer = keras.layers.Hashing(num_bins=3, mask_value='')

**Example (SipHash64)**

    layer = keras.layers.Hashing(num_bins=3, salt=[133, 137])

**Example (Siphash64 with a single integer, same as `salt=[133, 133]`)**

    layer = keras.layers.Hashing(num_bins=3, salt=133)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_bins` | Number of hash bins. Note that this includes the `mask_value` bin, so the effective number of bins is `(num_bins - 1)` if `mask_value` is set. |
| `mask_value` | A value that represents masked inputs, which are mapped to index 0. `None` means no mask term will be added and the hashing will start at index 0. Defaults to `None`. |
| `salt` | A single unsigned integer or None. If passed, the hash function used will be SipHash64, with these values used as an additional input (known as a "salt" in cryptography). These should be non-zero. If `None`, uses the FarmHash64 hash function. It also supports tuple/list of 2 unsigned integer numbers, see reference paper for details. Defaults to `None`. |
| `output_mode` | Specification for the output of the layer. Values can be `"int"`, `"one_hot"`, `"multi_hot"`, or `"count"` configuring the layer as follows:<br><br>*   `"int"`: Return the integer bin indices directly.<br>*   `"one_hot"`: Encodes each individual element in the input into an array the same size as `num_bins`, containing a 1 at the input's bin index. If the last dimension is size 1, will encode on that dimension. If the last dimension is not size 1, will append a new dimension for the encoded output.<br>*   `"multi_hot"`: Encodes each sample in the input into a single array the same size as `num_bins`, containing a 1 for each bin index index present in the sample. Treats the last dimension as the sample dimension, if input shape is `(..., sample_length)`, output shape will be `(..., num_tokens)`.<br>*   `"count"`: As `"multi_hot"`, but the int array contains a count of the number of times the bin index appeared in the sample. Defaults to `"int"`. |
| `sparse` | Boolean. Only applicable to `"one_hot"`, `"multi_hot"`, and `"count"` output modes. Only supported with TensorFlow backend. If `True`, returns a `SparseTensor` instead of a dense `Tensor`. Defaults to `False`. |
| `**kwargs` | Keyword arguments to construct a layer. |

|     |
| --- |
| Input shape<br>----------- |     |
| A single string, a list of strings, or an `int32` or `int64` tensor of shape `(batch_size, ...,)`. |     |

|     |
| --- |
| Output shape<br>------------ |     |
| An `int32` tensor of shape `(batch_size, ...)`. |     |

#### Reference:

*   [SipHash with salt](https://www.131002.net/siphash/siphash.pdf)
    

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

Last updated 2026-11-05 UTC.