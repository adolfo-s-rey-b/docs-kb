[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Attention#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Attention)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Attention?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FAttention&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Attention#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Attention#call-arguments)
    
*   [Output](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Attention#output)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Attention#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Attention#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Attention#from_config)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.Attention Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Attention#args)
    
*   [Call arguments](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Attention#call-arguments)
    
*   [Output](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Attention#output)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Attention#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Attention#methods)
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Attention#from_config)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/attention/attention.py#L8-L319)

Dot-product attention layer, a.k.a. Luong-style attention.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.Attention(
        use_scale=False,
        score_mode='dot',
        dropout=0.0,
        seed=None,
        **kwargs
    )

Inputs are a list with 2 or 3 elements:

1.  A `query` tensor of shape `(batch_size, Tq, dim)`.
2.  A `value` tensor of shape `(batch_size, Tv, dim)`.
3.  A optional `key` tensor of shape `(batch_size, Tv, dim)`. If none supplied, `value` will be used as a `key`.

The calculation follows the steps:

1.  Calculate attention scores using `query` and `key` with shape `(batch_size, Tq, Tv)`.
2.  Use scores to calculate a softmax distribution with shape `(batch_size, Tq, Tv)`.
3.  Use the softmax distribution to create a linear combination of `value` with shape `(batch_size, Tq, dim)`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `use_scale` | If `True`, will create a scalar variable to scale the attention scores. |
| `dropout` | Float between 0 and 1. Fraction of the units to drop for the attention scores. Defaults to `0.0`. |
| `seed` | A Python integer to use as random seed in case of `dropout`. |
| `score_mode` | Function to use to compute attention scores, one of `{"dot", "concat"}`. `"dot"` refers to the dot product between the query and key vectors. `"concat"` refers to the hyperbolic tangent of the concatenation of the `query` and `key` vectors. |

|     |     |
| --- | --- |
| Call arguments<br>-------------- |     |
| `inputs` | List of the following tensors:<br><br>*   `query`: Query tensor of shape `(batch_size, Tq, dim)`.<br>*   `value`: Value tensor of shape `(batch_size, Tv, dim)`.<br>*   `key`: Optional key tensor of shape `(batch_size, Tv, dim)`. If not given, will use `value` for both `key` and `value`, which is the most common case. |
| `mask` | List of the following tensors:*   `query_mask`: A boolean mask tensor of shape `(batch_size, Tq)`. If given, the output will be zero at the positions where `mask==False`.<br>*   `value_mask`: A boolean mask tensor of shape `(batch_size, Tv)`. If given, will apply the mask such that values at positions where `mask==False` do not contribute to the result. |
| `return_attention_scores` | bool, it `True`, returns the attention scores (after masking and softmax) as an additional output argument. |
| `training` | Python boolean indicating whether the layer should behave in training mode (adding dropout) or in inference mode (no dropout). |
| `use_causal_mask` | Boolean. Set to `True` for decoder self-attention. Adds a mask such that position `i` cannot attend to positions `j > i`. This prevents the flow of information from the future towards the past. Defaults to `False`. |

|     |
| --- |
| Output<br>------ |     |
| Attention outputs of shape `(batch_size, Tq, dim)`. (Optional) Attention scores after masking and softmax with shape `(batch_size, Tq, Tv)`. |     |

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