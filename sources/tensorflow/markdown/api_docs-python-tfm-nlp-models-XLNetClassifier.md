[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/XLNetClassifier#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/XLNetClassifier)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/XLNetClassifier?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/XLNetClassifier#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/XLNetClassifier#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/XLNetClassifier#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/XLNetClassifier#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.models.XLNetClassifier Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/XLNetClassifier#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/XLNetClassifier#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/XLNetClassifier#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/models/XLNetClassifier#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/xlnet.py#L155-L244)

Classifier model based on XLNet.

tfm.nlp.models.XLNetClassifier(
        network: Union[tf_keras.layers.Layer, tf_keras.Model],
        num_classes: int,
        initializer: tf_keras.initializers.Initializer = 'random_normal',
        summary_type: str = 'last',
        dropout_rate: float = 0.1,
        head_name: str = 'sentence_prediction',
        **kwargs
    )

This is an implementation of the network structure surrounding a Transformer-XL encoder as described in "XLNet: Generalized Autoregressive Pretraining for Language Understanding" ([https://arxiv.org/abs/1906.08237](https://arxiv.org/abs/1906.08237)
).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `network` | An XLNet/Transformer-XL based network. This network should output a sequence output and list of `state` tensors. |
| `num_classes` | Number of classes to predict from the classification network. |
| `initializer` | The initializer (if any) to use in the classification networks. Defaults to a RandomNormal initializer. |
| `summary_type` | Method used to summarize a sequence into a compact vector. |
| `dropout_rate` | The dropout probability of the cls head. |
| `head_name` | Name of the classification head. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `checkpoint_items` |     |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/models/xlnet.py#L215-L229)

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