[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/registry/register#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/registry/register)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/registry/register?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/registry/register#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/core/registry/register#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/core/registry/register#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.registry.register Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/registry/register#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/core/registry/register#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/core/registry/register#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/registry.py#L18-L62)

Register decorated function or class to collection.

tfm.core.registry.register(
        registered_collection, reg_key
    )

Register decorated function or class into registered\_collection, in a hierarchical order. For example, when reg\_key="my\_model/my\_exp/my\_config\_0" the decorated function or class is stored under registered\_collection\["my\_model"\]\["my\_exp"\]\["my\_config\_0"\]. This decorator is supposed to be used together with the lookup() function in this file.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `registered_collection` | a dictionary. The decorated function or class will be put into this collection. |
| `reg_key` | The key for retrieving the registered function or class. If reg\_key is a string, it can be hierarchical like my\_model/my\_exp/my\_config\_0 |

|     |
| --- |
| Returns<br>------- |     |
| A decorator function |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `KeyError` | when function or class to register already exists. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.