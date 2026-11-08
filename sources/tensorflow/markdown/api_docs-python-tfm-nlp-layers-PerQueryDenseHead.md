[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/PerQueryDenseHead#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/PerQueryDenseHead)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/PerQueryDenseHead?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/PerQueryDenseHead#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/PerQueryDenseHead#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/PerQueryDenseHead#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.PerQueryDenseHead Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/PerQueryDenseHead#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/PerQueryDenseHead#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/PerQueryDenseHead#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/cls_head.py#L369-L460)

Pooling head used for EncT5 style models.

tfm.nlp.layers.PerQueryDenseHead(
        num_queries: int,
        features: int,
        use_bias: bool = False,
        kernel_initializer: str = 'glorot_uniform',
        **kwargs
    )

This module projects each query to use a different projection.

For a input shape= \[bs, num\_queries, hidden\_size\], it projects each query to (features). Ending up with shape= \[bs, num\_queries, features\].

For example, for classification with a few classes, one may use num\_queries as 1 and features as number of classes. For multilabel classification, one may use num\_queries as number of classes and features as 2. So each query represents a binary classification of one label.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `num_queries` | number of queries (the learnable embeddings in the input sequences) from the decoder. |
| `features` | int with numbers of output features. Each query with be projected to this number with a different projection. |
| `use_bias` | whether to add a bias to the output. |
| `kernel_initializer` | Initializer for dense layer kernels. |
| `**kwargs` | Keyword arguments. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/cls_head.py#L431-L444)

call(
        inputs: tf.Tensor
    ) -> tf.Tensor

Implements call().

|     |     |
| --- | --- |
| Args |     |
| `inputs` | a rank-3 Tensor of shape= \[bs, num\_queries, hidden\_size\]. |

|     |
| --- |
| Returns |     |
| A Tensor, shape= \[batch size, num\_queries, features\]. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.