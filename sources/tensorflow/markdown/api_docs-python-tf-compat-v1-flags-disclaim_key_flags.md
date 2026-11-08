[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/flags/disclaim_key_flags#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.flags.disclaim\_key\_flags Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

Declares that the current module will not define any more key flags.

tf.compat.v1.flags.disclaim_key_flags() -> None

Normally, the module that calls the DEFINE\_xxx functions claims the flag to be its key flag. This is undesirable for modules that define additional DEFINE\_yyy functions with its own flag parsers and serializers, since that module will accidentally claim flags defined by DEFINE\_yyy as its key flags. After calling this function, the module disclaims flag definitions thereafter, so the key flags will be correctly attributed to the caller of DEFINE\_yyy.

After calling this function, the module will not be able to define any more flags. This function will affect all FlagValues objects.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.