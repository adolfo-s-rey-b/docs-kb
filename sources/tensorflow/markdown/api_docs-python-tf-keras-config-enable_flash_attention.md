[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/config/enable_flash_attention#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/config/enable_flash_attention)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/config/enable_flash_attention?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.config.enable\_flash\_attention Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/backend/config.py#L177-L195)

Enable flash attention.

tf.keras.config.enable_flash_attention()

Flash attention offers performance optimization for attention layers, making it especially useful for large language models (LLMs) that benefit from faster and more memory-efficient attention computations.

Once enabled, supported layers like `MultiHeadAttention` will **attempt** to use flash attention for faster computations. By default, this feature is enabled.

Note that enabling flash attention does not guarantee it will always be used. Typically, the inputs must be in `float16` or `bfloat16` dtype, and input layout requirements may vary depending on the backend.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.