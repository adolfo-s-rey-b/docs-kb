[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/CategoryEncoding#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/CategoryEncoding)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/CategoryEncoding?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FCategoryEncoding&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/CategoryEncoding#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/CategoryEncoding#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/CategoryEncoding#call-arguments)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/CategoryEncoding#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/CategoryEncoding#methods)
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/CategoryEncoding#convert_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/CategoryEncoding#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.CategoryEncoding Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/CategoryEncoding#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/CategoryEncoding#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/CategoryEncoding#call-arguments)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/CategoryEncoding#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/CategoryEncoding#methods)
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/CategoryEncoding#convert_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/CategoryEncoding#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/category_encoding.py#L8-L166)

A preprocessing layer which encodes integer features.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.CategoryEncoding(
        num_tokens=None, output_mode='multi_hot', sparse=False, **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrate \`tf.feature\_column\`s to Keras preprocessing layers](https://www.tensorflow.org/guide/migrate/migrating_feature_columns)<br>    <br>*   [Working with preprocessing layers](https://www.tensorflow.org/guide/keras/preprocessing_layers) | *   [Load CSV data](https://www.tensorflow.org/tutorials/load_data/csv)<br>    <br>*   [Classify structured data using Keras preprocessing layers](https://www.tensorflow.org/tutorials/structured_data/preprocessing_layers) |

This layer provides options for condensing data into a categorical encoding when the total number of tokens are known in advance. It accepts integer values as inputs, and it outputs a dense or sparse representation of those inputs. For integer inputs where the total number of tokens is not known, use [`keras.layers.IntegerLookup`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/IntegerLookup)
 instead.

#### Examples:

**One-hot encoding data**

    layer = keras.layers.CategoryEncoding(

**Multi-hot encoding data**

    layer = keras.layers.CategoryEncoding(

**Using weighted inputs in `"count"` mode**

    layer = keras.layers.CategoryEncoding(

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_tokens` | The total number of tokens the layer should support. All inputs to the layer must integers in the range `0 <= value < num_tokens`, or an error will be thrown. |
| `output_mode` | Specification for the output of the layer. Values can be `"one_hot"`, `"multi_hot"` or `"count"`, configuring the layer as follows:<br><br>- `"one_hot"`: Encodes each individual element in the input<br>        into an array of `num_tokens` size, containing a 1 at the<br>        element index. If the last dimension is size 1, will encode<br>        on that dimension. If the last dimension is not size 1,<br>        will append a new dimension for the encoded output.<br>    - `"multi_hot"`: Encodes each sample in the input into a single<br>        array of `num_tokens` size, containing a 1 for each<br>        vocabulary term present in the sample. Treats the last<br>        dimension as the sample dimension, if input shape is<br>        `(..., sample_length)`, output shape will be<br>        `(..., num_tokens)`.<br>    - `"count"`: Like `"multi_hot"`, but the int array contains a<br>        count of the number of times the token at that index<br>        appeared in the sample.<br><br>For all output modes, currently only output up to rank 2 is supported. Defaults to `"multi_hot"`. |
| `sparse` | Whether to return a sparse tensor; for backends that support sparse tensors. |

|     |     |
| --- | --- |
| Call arguments<br>-------------- |     |
| `inputs` | A 1D or 2D tensor of integer inputs. |
| `count_weights` | A tensor in the same shape as `inputs` indicating the weight for each sample value when summing up in `count` mode. Not used in `"multi_hot"` or `"one_hot"` modes. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

### `convert_weight`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/data_layer.py#L153-L159)

convert_weight(
        weight
    )

Convert the weight if it is from the a different backend.

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