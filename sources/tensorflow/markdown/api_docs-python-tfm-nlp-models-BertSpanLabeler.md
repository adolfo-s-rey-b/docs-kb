[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertSpanLabeler#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertSpanLabeler)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertSpanLabeler?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertSpanLabeler#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertSpanLabeler#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertSpanLabeler#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertSpanLabeler#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.models.BertSpanLabeler Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertSpanLabeler#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertSpanLabeler#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertSpanLabeler#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertSpanLabeler#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/bert_span_labeler.py#L23-L125)

Span labeler model based on a BERT-style transformer-based encoder.

tfm.nlp.models.BertSpanLabeler(
        network,
        initializer='glorot_uniform',
        output='logits',
        **kwargs
    )

This is an implementation of the network structure surrounding a transformer encoder as described in "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding" ([https://arxiv.org/abs/1810.04805](https://arxiv.org/abs/1810.04805)
).

The BertSpanLabeler allows a user to pass in a transformer encoder, and instantiates a span labeling network based on a single dense layer.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `network` | A transformer network. This network should output a sequence output and a classification output. Furthermore, it should expose its embedding table via a `get_embedding_table` method. |
| `initializer` | The initializer (if any) to use in the span labeling network. Defaults to a Glorot uniform initializer. |
| `output` | The output style for this network. Can be either `logit`' or `predictions`. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `checkpoint_items` |     |

Methods
-------

### `call`

call(
        inputs, training=None, mask=None
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