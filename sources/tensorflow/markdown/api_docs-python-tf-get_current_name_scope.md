[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/get_current_name_scope#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/get_current_name_scope)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/get_current_name_scope?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fget_current_name_scope&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.get\_current\_name\_scope Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/ops.py#L5710-L5742)

Returns current full name scope specified by [`tf.name_scope(...)`](https://www.tensorflow.org/api_docs/python/tf/name_scope)
s.

tf.get_current_name_scope() -> str

For example,

with tf.name_scope("outer"):
      tf.get_current_name_scope()  # "outer"
    
      with tf.name_scope("inner"):
        tf.get_current_name_scope()  # "outer/inner"

In other words, [`tf.get_current_name_scope()`](https://www.tensorflow.org/api_docs/python/tf/get_current_name_scope)
 returns the op name prefix that will be prepended to, if an op is created at that place.

Note that [`@tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 resets the name scope stack as shown below.

with tf.name_scope("outer"):
    
      @tf.function
      def foo(x):
        with tf.name_scope("inner"):
          return tf.add(x * x)  # Op name is "inner/Add", not "outer/inner/Add"

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.