[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertPretrainerV2#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertPretrainerV2)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertPretrainerV2?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fnlp%2Fmodels%2FBertPretrainerV2&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertPretrainerV2#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertPretrainerV2#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertPretrainerV2#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertPretrainerV2#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.models.BertPretrainerV2 Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertPretrainerV2#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertPretrainerV2#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertPretrainerV2#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/BertPretrainerV2#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/bert_pretrainer.py#L161-L281)

BERT pretraining model V2.

tfm.nlp.models.BertPretrainerV2(
        encoder_network: tf_keras.Model,
        mlm_activation=None,
        mlm_initializer='glorot_uniform',
        classification_heads: Optional[List[tf_keras.layers.Layer]] = None,
        customized_masked_lm: Optional[tf_keras.layers.Layer] = None,
        name: str = 'bert',
        **kwargs
    )

Adds the masked language model head and optional classification heads upon the transformer encoder.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `encoder_network` | A transformer network. This network should output a sequence output and a classification output. |
| `mlm_activation` | The activation (if any) to use in the masked LM network. If None, no activation will be used. |
| `mlm_initializer` | The initializer (if any) to use in the masked LM. Default to a Glorot uniform initializer. |
| `classification_heads` | A list of optional head layers to transform on encoder sequence outputs. |
| `customized_masked_lm` | A customized masked\_lm layer. If None, will create a standard layer from [`layers.MaskedLM`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/MaskedLM)<br>; if not None, will use the specified masked\_lm layer. Above arguments `mlm_activation` and `mlm_initializer` will be ignored. |
| `name` | The name of the model. |

Inputs: Inputs defined by the encoder network, plus `masked_lm_positions` as a dictionary. Outputs: A dictionary of `lm_output`, classification head outputs keyed by head names, and also outputs from `encoder_network`, keyed by `sequence_output` and `encoder_outputs` (if any).

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `checkpoint_items` | Returns a dictionary of items to be additionally checkpointed. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/bert_pretrainer.py#L229-L265)

call(
        inputs
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