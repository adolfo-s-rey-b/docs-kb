[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/nested_csv_str_to_json_str#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/nested_csv_str_to_json_str)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/nested_csv_str_to_json_str?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/nested_csv_str_to_json_str#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/nested_csv_str_to_json_str#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/nested_csv_str_to_json_str#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.hyperparams.nested\_csv\_str\_to\_json\_str Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/nested_csv_str_to_json_str#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/nested_csv_str_to_json_str#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/nested_csv_str_to_json_str#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/hyperparams/params_dict.py#L352-L452)

Converts a nested (using '.') comma-separated k=v string to a JSON string.

#### View aliases

**Main aliases**

[`tfm.hyperparams.params_dict.nested_csv_str_to_json_str`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/nested_csv_str_to_json_str)

tfm.hyperparams.nested_csv_str_to_json_str(
        csv_str
    )

Converts a comma-separated string of key/value pairs that supports nesting of keys to a JSON string. Nesting is implemented using '.' between levels for a given key.

Spacing between commas and = is supported (e.g. there is no difference between "a=1,b=2", "a = 1, b = 2", or "a=1, b=2") but there should be no spaces before keys or after values (e.g. " a=1,b=2" and "a=1,b=2 " are not supported).

Note that this will only support values supported by CSV, meaning values such as nested lists (e.g. "a=\[\[1,2,3\],\[4,5,6\]\]") are not supported. Strings are supported as well, e.g. "a='hello'".

An example conversion would be:

"a=1, b=2, c.a=2, c.b=3, d.a.a=5"

to

"{ a: 1, b : 2, c: {a : 2, b : 3}, d: {a: {a : 5} } }"

|     |     |
| --- | --- |
| Args<br>---- |     |
| `csv_str` | the comma separated string. |

|     |
| --- |
| Returns<br>------- |     |
| the converted JSON string. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If csv\_str is not in a comma separated string or if the string is formatted incorrectly. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.