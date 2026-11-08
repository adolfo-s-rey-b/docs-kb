[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fnlp%2Fencoders&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.nlp.encoders Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders#functions)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/nlp/configs/encoders.py)

Transformer Encoders.

Includes configurations and factory methods.

Classes
-------

[`class AlbertEncoderConfig`](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders/AlbertEncoderConfig)
: ALBERT encoder configuration.

[`class BertEncoderConfig`](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders/BertEncoderConfig)
: BERT encoder configuration.

[`class BigBirdEncoderConfig`](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders/BigBirdEncoderConfig)
: BigBird encoder configuration.

[`class EncoderConfig`](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders/EncoderConfig)
: Encoder configuration.

[`class FNetEncoderConfig`](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders/FNetEncoderConfig)
: FNet encoder configuration.

[`class FunnelEncoderConfig`](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders/FunnelEncoderConfig)
: Funnel encoder configuration.

[`class KernelEncoderConfig`](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders/KernelEncoderConfig)
: Linear encoder configuration.

[`class MobileBertEncoderConfig`](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders/MobileBertEncoderConfig)
: MobileBERT encoder configuration.

[`class QueryBertConfig`](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders/QueryBertConfig)
: Query BERT encoder configuration.

[`class ReuseEncoderConfig`](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders/ReuseEncoderConfig)
: Reuse encoder configuration.

[`class SparseMixerEncoderConfig`](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders/SparseMixerEncoderConfig)
: SparseMixer encoder configuration.

[`class XLNetEncoderConfig`](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders/XLNetEncoderConfig)
: XLNet encoder configuration.

Functions
---------

[`build_encoder(...)`](https://www.tensorflow.org/api_docs/python/tfm/nlp/encoders/build_encoder)
: Instantiate a Transformer encoder network from EncoderConfig.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.