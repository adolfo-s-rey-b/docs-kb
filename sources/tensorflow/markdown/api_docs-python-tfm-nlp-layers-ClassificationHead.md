[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ClassificationHead#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ClassificationHead)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ClassificationHead?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fnlp%2Flayers%2FClassificationHead&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ClassificationHead#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ClassificationHead#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ClassificationHead#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ClassificationHead#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.ClassificationHead Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ClassificationHead#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ClassificationHead#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ClassificationHead#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ClassificationHead#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/cls_head.py#L25-L112)

Pooling head for sentence-level classification tasks.

tfm.nlp.layers.ClassificationHead(
        inner_dim,
        num_classes,
        cls_token_idx=0,
        activation='tanh',
        dropout_rate=0.0,
        initializer='glorot_uniform',
        **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inner_dim` | The dimensionality of inner projection layer. If 0 or `None` then only the output projection layer is created. |
| `num_classes` | Number of output classes. |
| `cls_token_idx` | The index inside the sequence to pool. |
| `activation` | Dense layer activation. |
| `dropout_rate` | Dropout probability. |
| `initializer` | Initializer for dense layer kernels. |
| `**kwargs` | Keyword arguments. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `checkpoint_items` |     |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/cls_head.py#L69-L92)

call(
        features: tf.Tensor, only_project: bool = False
    )

Implements call().

|     |     |
| --- | --- |
| Args |     |
| `features` | a rank-3 Tensor when self.inner\_dim is specified, otherwise it is a rank-2 Tensor. |
| `only_project` | a boolean. If True, we return the intermediate Tensor before projecting to class logits. |

|     |
| --- |
| Returns |     |
| a Tensor, if only\_project is True, shape= \[batch size, hidden size\]. If only\_project is False, shape= \[batch size, num classes\]. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.