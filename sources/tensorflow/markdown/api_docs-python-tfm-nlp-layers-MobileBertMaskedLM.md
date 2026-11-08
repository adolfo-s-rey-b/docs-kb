[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertMaskedLM#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertMaskedLM)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertMaskedLM?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertMaskedLM#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertMaskedLM#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertMaskedLM#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.MobileBertMaskedLM Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertMaskedLM#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertMaskedLM#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MobileBertMaskedLM#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/mobile_bert_layers.py#L434-L575)

Masked language model network head for BERT modeling.

tfm.nlp.layers.MobileBertMaskedLM(
        embedding_table,
        activation=None,
        initializer='glorot_uniform',
        output='logits',
        output_weights_use_proj=False,
        **kwargs
    )

This layer implements a masked language model based on the provided transformer based encoder. It assumes that the encoder network being passed has a "get\_embedding\_table()" method. Different from canonical BERT's masked LM layer, when the embedding width is smaller than hidden\_size, it adds an extra output weights in shape \[vocab\_size, (hidden\_size - embedding\_width)\].

|     |     |
| --- | --- |
| Args<br>---- |     |
| `embedding_table` | The embedding table from encoder network. |
| `activation` | The activation, if any, for the dense layer. |
| `initializer` | The initializer for the dense layer. Defaults to a Glorot uniform initializer. |
| `output` | The output style for this layer. Can be either `logits` or `predictions`. |
| `output_weights_use_proj` | Use projection instead of concating extra output weights, this may reduce the MLM task accuracy but will reduce the model params as well. |
| `**kwargs` | keyword arguments. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/mobile_bert_layers.py#L517-L542)

call(
        sequence_data, masked_positions
    )

This is where the layer's logic lives.

The `call()` method may not create state (except in its first invocation, wrapping the creation of variables or other resources in [`tf.init_scope()`](https://www.tensorflow.org/api_docs/python/tf/init_scope)
). It is recommended to create state, including [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
 instances and nested `Layer` instances, in `__init__()`, or in the `build()` method that is called automatically before `call()` executes for the first time.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | Input tensor, or dict/list/tuple of input tensors. The first positional `inputs` argument is subject to special rules:<br><br>*   `inputs` must be explicitly passed. A layer cannot have zero arguments, and `inputs` cannot be provided via the default value of a keyword argument.<br>*   NumPy array or Python scalar values in `inputs` get cast as tensors.<br>*   TF-Keras mask metadata is only collected from `inputs`.<br>*   Layers are built (`build(input_shape)` method) using shape info from `inputs` only.<br>*   `input_spec` compatibility is only checked against `inputs`.<br>*   Mixed precision input casting is only applied to `inputs`. If a layer has tensor arguments in `*args` or `**kwargs`, their casting behavior in mixed precision should be handled manually.<br>*   The SavedModel input specification is generated using `inputs` only.<br>*   Integration with various ecosystem packages like TFMOT, TFLite, TF.js, etc is only supported for `inputs` and not for tensors in positional and keyword arguments. |
| `*args` | Additional positional arguments. May contain tensors, although this is not recommended, for the reasons above. |
| `**kwargs` | Additional keyword arguments. May contain tensors, although this is not recommended, for the reasons above. The following optional keyword arguments are reserved:*   `training`: Boolean scalar tensor of Python boolean indicating whether the `call` is meant for training or inference.<br>*   `mask`: Boolean input mask. If the layer's `call()` method takes a `mask` argument, its default value will be set to the mask generated for `inputs` by the previous layer (if `input` did come from a layer that generated a corresponding mask, i.e. if it came from a TF-Keras layer with masking support). |

|     |
| --- |
| Returns |     |
| A tensor or list/tuple of tensors. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.