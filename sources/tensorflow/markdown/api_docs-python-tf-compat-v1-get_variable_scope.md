[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable_scope#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable_scope)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable_scope?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable_scope#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable_scope#description)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.get\_variable\_scope Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable_scope#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable_scope#description)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variable_scope.py#L1415-L1445)

Returns the current variable scope.

tf.compat.v1.get_variable_scope()

Migrate to TF2
--------------

Although it is a legacy [`compat.v1`](https://www.tensorflow.org/api_docs/python/tf/compat/v1)
 api, [`tf.compat.v1.get_variable`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable)
 is compatible with eager execution and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)

However, to maintain variable-scope based variable reuse you will need to combine it with `tf.compat.v1.keras.utils.track_tf1_style_variables`. (Though it will behave as if reuse is always set to [`tf.compat.v1.AUTO_REUSE`](https://www.tensorflow.org/api_docs/python/tf/compat/v1#AUTO_REUSE)
.)

See the [migration guide](https://www.tensorflow.org/guide/migrate/model_mapping)
 for more info.

The TF2 equivalent, if you are just trying to track variable name prefixes and not control `get_variable`\-based variable reuse, would be to use [`tf.name_scope`](https://www.tensorflow.org/api_docs/python/tf/name_scope)
 and capture the output of opening the scope (which represents the current name prefix).

For example:

x = tf.name_scope('foo') as current_scope:
      ...

Description
-----------

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.