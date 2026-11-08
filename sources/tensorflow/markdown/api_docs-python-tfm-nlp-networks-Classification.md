[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/Classification#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/Classification)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/Classification?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/Classification#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/Classification#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/Classification#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.networks.Classification Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/Classification#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/Classification#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/networks/Classification#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/networks/classification.py#L22-L107)

Classification network head for BERT modeling.

tfm.nlp.networks.Classification(
        input_width,
        num_classes,
        initializer='glorot_uniform',
        output='logits',
        **kwargs
    )

This network implements a simple classifier head based on a dense layer. If num\_classes is one, it can be considered as a regression problem.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input_width` | The innermost dimension of the input tensor to this network. |
| `num_classes` | The number of classes that this network should classify to. If equal to 1, a regression problem is assumed. |
| `activation` | The activation, if any, for the dense layer in this network. |
| `initializer` | The initializer for the dense layer in this network. Defaults to a Glorot uniform initializer. |
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