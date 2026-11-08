[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/XLNetSpanLabeler#main-content)

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
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.models.XLNetSpanLabeler Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/xlnet.py#L247-L344)

Span labeler model based on XLNet.

tfm.nlp.models.XLNetSpanLabeler(
        network: Union[tf_keras.layers.Layer, tf_keras.Model],
        start_n_top: int = 5,
        end_n_top: int = 5,
        dropout_rate: float = 0.1,
        span_labeling_activation: tf_keras.initializers.Initializer = 'tanh',
        initializer: tf_keras.initializers.Initializer = 'glorot_uniform',
        **kwargs
    )

This is an implementation of the network structure surrounding a Transformer-XL encoder as described in "XLNet: Generalized Autoregressive Pretraining for Language Understanding" ([https://arxiv.org/abs/1906.08237](https://arxiv.org/abs/1906.08237)
).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `network` | A transformer network. This network should output a sequence output and a classification output. Furthermore, it should expose its embedding table via a "get\_embedding\_table" method. |
| `start_n_top` | Beam size for span start. |
| `end_n_top` | Beam size for span end. |
| `dropout_rate` | The dropout rate for the span labeling layer. |
| `span_labeling_activation` | The activation for the span labeling head. |
| `initializer` | The initializer (if any) to use in the span labeling network. Defaults to a Glorot uniform initializer. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `checkpoint_items` |     |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/xlnet.py#L308-L333)

call(
        inputs: Mapping[str, Any]
    )

Calls the model on new inputs and returns the outputs as tensors.

In this case `call()` just reapplies all ops in the graph to the new inputs (e.g. build a new computational graph from the provided inputs).

|     |     |
| --- | --- |
| Args |     |
| `inputs` | Input tensor, or dict/list/tuple of input tensors. |
| `training` | Boolean or boolean scalar tensor, indicating whether to run the `Network` in training mode or inference mode. |
| `mask` | A mask or list of masks. A mask can be either a boolean tensor or None (no mask). For more details, check the guide [here](https://www.tensorflow.org/guide/keras/masking_and_padding)<br>. |

|     |
| --- |
| Returns |     |
| A tensor if there is a single output, or a list of tensors if there are more than one outputs. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.