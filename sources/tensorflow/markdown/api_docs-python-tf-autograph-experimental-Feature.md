[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/autograph/experimental/Feature#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/autograph/experimental/Feature)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/autograph/experimental/Feature?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/autograph/experimental/Feature#attributes)
    
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/autograph/experimental/Feature#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.autograph.experimental.Feature Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/autograph/experimental/Feature#attributes)
    
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/autograph/experimental/Feature#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/autograph/core/converter.py#L78-L127)

This enumeration represents optional conversion options.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.autograph.experimental.Feature`](https://www.tensorflow.org/api_docs/python/tf/autograph/experimental/Feature)

These conversion options are experimental. They are subject to change without notice and offer no guarantees.

_Example Usage_

optionals= tf.autograph.experimental.Feature.EQUALITY_OPERATORS
    @tf.function(experimental_autograph_options=optionals)
    def f(i):
      if i == 0:  # EQUALITY_OPERATORS allows the use of == here.
        tf.print('i is zero')

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `ALL` | Enable all features. |
| `AUTO_CONTROL_DEPS` | Insert of control dependencies in the generated code. |
| `ASSERT_STATEMENTS` | Convert Tensor-dependent assert statements to tf.Assert. |
| `BUILTIN_FUNCTIONS` | Convert builtin functions applied to Tensors to their TF counterparts. |
| `EQUALITY_OPERATORS` | Whether to convert the equality operator ('==') to tf.math.equal. |
| `LISTS` | Convert list idioms, like initializers, slices, append, etc. |
| `NAME_SCOPES` | Insert name scopes that name ops according to context, like the function they were defined in. |

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| ALL | `<Feature.ALL: 'ALL'>` |
| ASSERT\_STATEMENTS | `<Feature.ASSERT_STATEMENTS: 'ASSERT_STATEMENTS'>` |
| AUTO\_CONTROL\_DEPS | `<Feature.AUTO_CONTROL_DEPS: 'AUTO_CONTROL_DEPS'>` |
| BUILTIN\_FUNCTIONS | `<Feature.BUILTIN_FUNCTIONS: 'BUILTIN_FUNCTIONS'>` |
| EQUALITY\_OPERATORS | `<Feature.EQUALITY_OPERATORS: 'EQUALITY_OPERATORS'>` |
| LISTS | `<Feature.LISTS: 'LISTS'>` |
| NAME\_SCOPES | `<Feature.NAME_SCOPES: 'NAME_SCOPES'>` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.