[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertPretrainer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertPretrainer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertPretrainer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertPretrainer#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertPretrainer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertPretrainer#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.models.BertPretrainer Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertPretrainer#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertPretrainer#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertPretrainer#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/bert_pretrainer.py#L30-L158)

BERT pretraining model.

tfm.nlp.models.BertPretrainer(
        network,
        num_classes,
        num_token_predictions,
        embedding_table=None,
        activation=None,
        initializer='glorot_uniform',
        output='logits',
        **kwargs
    )

\[Note\] Please use the new `BertPretrainerV2` for your projects.

The BertPretrainer allows a user to pass in a transformer stack, and instantiates the masked language model and classification networks that are used to create the training objectives.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `network` | A transformer network. This network should output a sequence output and a classification output. |
| `num_classes` | Number of classes to predict from the classification network. |
| `num_token_predictions` | Number of tokens to predict from the masked LM. |
| `embedding_table` | Embedding table of a network. If None, the "network.get\_embedding\_table()" is used. |
| `activation` | The activation (if any) to use in the masked LM network. If None, no activation will be used. |
| `initializer` | The initializer (if any) to use in the masked LM and classification networks. Defaults to a Glorot uniform initializer. |
| `output` | The output style for this network. Can be either `logits` or `predictions`. |

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