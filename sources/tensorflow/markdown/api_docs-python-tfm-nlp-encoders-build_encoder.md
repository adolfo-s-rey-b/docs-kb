[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders/build_encoder#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders/build_encoder)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders/build_encoder?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fnlp%2Fencoders%2Fbuild_encoder&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders/build_encoder#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders/build_encoder#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.nlp.encoders.build\_encoder Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders/build_encoder#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders/build_encoder#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/configs/encoders.py#L364-L775)

Instantiate a Transformer encoder network from EncoderConfig.

tfm.nlp.encoders.build_encoder(
        config: tfm.nlp.encoders.EncoderConfig,
        embedding_layer: Optional[tf_keras.layers.Layer] = None,
        encoder_cls=None,
        bypass_config: bool = False
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `config` | the one-of encoder config, which provides encoder parameters of a chosen encoder. |
| `embedding_layer` | an external embedding layer passed to the encoder. |
| `encoder_cls` | an external encoder cls not included in the supported encoders, usually used by gin.configurable. |
| `bypass_config` | whether to ignore config instance to create the object with `encoder_cls`. |

|     |
| --- |
| Returns<br>------- |     |
| An encoder instance. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.