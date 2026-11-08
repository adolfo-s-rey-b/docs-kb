[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/GaussianProcessClassificationHead#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/GaussianProcessClassificationHead)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/GaussianProcessClassificationHead?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fnlp%2Flayers%2FGaussianProcessClassificationHead&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/GaussianProcessClassificationHead#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/GaussianProcessClassificationHead#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/GaussianProcessClassificationHead#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/GaussianProcessClassificationHead#call)
        
    *   [reset\_covariance\_matrix](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/GaussianProcessClassificationHead#reset_covariance_matrix)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.layers.GaussianProcessClassificationHead Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/GaussianProcessClassificationHead#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/GaussianProcessClassificationHead#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/GaussianProcessClassificationHead#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/GaussianProcessClassificationHead#call)
        
    *   [reset\_covariance\_matrix](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/GaussianProcessClassificationHead#reset_covariance_matrix)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/cls_head.py#L213-L338)

Gaussian process-based pooling head for sentence classification.

Inherits From: [`ClassificationHead`](https://www.tensorflow.org/api_docs/python/tfm/nlp/layers/ClassificationHead)

tfm.nlp.layers.GaussianProcessClassificationHead(
        inner_dim,
        num_classes,
        cls_token_idx=0,
        activation='tanh',
        dropout_rate=0.0,
        initializer='glorot_uniform',
        use_spec_norm=True,
        use_gp_layer=True,
        temperature=None,
        **kwargs
    )

This class implements a classifier head for BERT encoder that is based on the spectral-normalized neural Gaussian process (SNGP) \[1\]. SNGP is a simple method to improve a neural network's uncertainty quantification ability without sacrificing accuracy or lantency. It applies spectral normalization to the hidden pooler layer, and then replaces the dense output layer with a Gaussian process.

\[1\]: Jeremiah Liu et al. Simple and Principled Uncertainty Estimation with Deterministic Deep Learning via Distance Awareness. In _Neural Information Processing Systems_, 2020. [https://arxiv.org/abs/2006.10108](https://arxiv.org/abs/2006.10108)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inner_dim` | The dimensionality of inner projection layer. If 0 or `None` then only the output projection layer is created. |
| `num_classes` | Number of output classes. |
| `cls_token_idx` | The index inside the sequence to pool. |
| `activation` | Dense layer activation. |
| `dropout_rate` | Dropout probability. |
| `initializer` | Initializer for dense layer kernels. |
| `use_spec_norm` | Whether to apply spectral normalization to pooler layer. |
| `use_gp_layer` | Whether to use Gaussian process as the output layer. |
| `temperature` | The temperature parameter to be used for mean-field approximation during inference. If None then no mean-field adjustment is applied. |
| `**kwargs` | Additional keyword arguments. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `checkpoint_items` |     |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/cls_head.py#L287-L322)

call(
        features, training=False, return_covmat=False
    )

Returns model output.

Dring training, the model returns raw logits. During evaluation, the model returns uncertainty adjusted logits, and (optionally) the covariance matrix.

|     |     |
| --- | --- |
| Arguments |     |
| `features` | A tensor of input features, shape (batch\_size, feature\_dim). |
| `training` | Whether the model is in training mode. |
| `return_covmat` | Whether the model should also return covariance matrix if `use_gp_layer=True`. During training, it is recommended to set `return_covmat=False` to be compatible with the standard Keras pipelines (e.g., `model.fit()`). |

|     |     |
| --- | --- |
| Returns |     |
| `logits` | Uncertainty-adjusted predictive logits, shape (batch\_size, num\_classes). |
| `covmat` | (Optional) Covariance matrix, shape (batch\_size, batch\_size). Returned only when return\_covmat=True. |

### `reset_covariance_matrix`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/modeling/layers/cls_head.py#L324-L327)

reset_covariance_matrix()

Resets covariance matrix of the Gaussian process layer.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.