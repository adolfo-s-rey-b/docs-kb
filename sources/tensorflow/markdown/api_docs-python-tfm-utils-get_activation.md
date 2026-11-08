[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/utils/get_activation#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/utils/get_activation)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/utils/get_activation?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/utils/get_activation#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/utils/get_activation#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.utils.get\_activation Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/utils/get_activation#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/utils/get_activation#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/tf_utils.py#L87-L137)

Maps an identifier to a Python function, e.g., "relu" => [`tf.nn.relu`](https://www.tensorflow.org/api_docs/python/tf/nn/relu)
.

tfm.utils.get_activation(
        identifier, use_keras_layer=False, **kwargs
    )

It checks string first and if it is one of customized activation not in TF, the corresponding activation will be returned. For non-customized activation names and callable identifiers, always fallback to tf\_keras.activations.get.

Prefers using keras layers when use\_keras\_layer=True. Now it only supports 'relu', 'linear', 'identity', 'swish', 'mish', 'leaky\_relu', and 'gelu'.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `identifier` | String name of the activation function or callable. |
| `use_keras_layer` | If True, use keras layer if identifier is allow-listed. |
| `**kwargs` | Keyword arguments to use to instantiate an activation function. Available only for 'leaky\_relu' and 'gelu' when using keras layers. For example: get\_activation('leaky\_relu', use\_keras\_layer=True, alpha=0.1) |

|     |
| --- |
| Returns<br>------- |     |
| A Python function corresponding to the activation function or a keras activation layer when use\_keras\_layer=True. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.