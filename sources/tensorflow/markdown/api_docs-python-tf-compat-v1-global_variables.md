[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.global\_variables Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L1772-L1804)

Returns global variables.

tf.compat.v1.global_variables(
        scope=None
    )

Migrate to TF2
--------------

Not compatible with eager execution and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. In particular, Graph collections are deprecated in TF2. Instead please create a [tf.Module](https://www.tensorflow.org/guide/intro_to_modules)
 container for all your model state, including variables. You can then list all the variables in your [`tf.Module`](https://www.tensorflow.org/api_docs/python/tf/Module)
 through the `variables` attribute.

Description
-----------

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Validating correctness & numerical equivalence](https://www.tensorflow.org/guide/migrate/validate_correctness)<br>    <br>*   [Migrating model checkpoints](https://www.tensorflow.org/guide/migrate/migrating_checkpoints) |

Global variables are variables that are shared across machines in a distributed environment. The `Variable()` constructor or `get_variable()` automatically adds new variables to the graph collection `GraphKeys.GLOBAL_VARIABLES`. This convenience function returns the contents of that collection.

An alternative to global variables are local variables. See [`tf.compat.v1.local_variables`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/local_variables)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `scope` | (Optional.) A string. If supplied, the resulting list is filtered to include only items whose `name` attribute matches `scope` using `re.match`. Items without a `name` attribute are never returned if a scope is supplied. The choice of `re.match` means that a `scope` without special tokens filters by prefix. |

|     |
| --- |
| Returns<br>------- |     |
| A list of `Variable` objects. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.