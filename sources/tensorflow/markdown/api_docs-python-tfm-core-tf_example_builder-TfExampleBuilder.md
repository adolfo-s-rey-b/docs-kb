[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/tf_example_builder/TfExampleBuilder#main-content)

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
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.tf\_example\_builder.TfExampleBuilder Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/tf_example_builder.py#L32-L144)

Builder class for preparing tf.train.Example.

tfm.core.tf_example_builder.TfExampleBuilder() -> None

Read API doc at [https://www.tensorflow.org/api\_docs/python/tf/train/Example](https://www.tensorflow.org/api_docs/python/tf/train/Example)

|     |
| --- |
| Example usage<br>------------- |     |
| >>> example_builder = TfExampleBuilder()<br>    >>> example = (<br>            example_builder.add_bytes_feature('feature_a', 'foobarbaz')<br>            .add_ints_feature('feature_b', [1, 2, 3])<br>            .example) |     |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `example` | Returns a copy of the generated tf.train.Example proto. |
| `serialized_example` | Returns a serialized string of the generated tf.train.Example proto. |

Methods
-------

### `add_bytes_feature`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/tf_example_builder.py#L100-L114)

add_bytes_feature(
        key: str, value: BytesValueType
    ) -> TfExampleBuilder

Adds byte(s) or string(s) with `key` to the example.

|     |     |
| --- | --- |
| Args |     |
| `key` | String key of the feature. |
| `value` | The byte(s) or string(s) to be added to the example. |

|     |
| --- |
| Returns |     |
| The builder object for subsequent method calls. |     |

### `add_feature`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/tf_example_builder.py#L86-L98)

add_feature(
        key: str, feature: tf.train.Feature
    ) -> TfExampleBuilder

Adds predefined `feature` with `key` to the example.

|     |     |
| --- | --- |
| Args |     |
| `key` | String key of the feature. |
| `feature` | The feature to be added to the example. |

|     |
| --- |
| Returns |     |
| The builder object for subsequent method calls. |     |

### `add_feature_dict`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/tf_example_builder.py#L69-L84)

add_feature_dict(
        feature_dict: Mapping[str, tf.train.Feature]
    ) -> TfExampleBuilder

Adds the predefined `feature_dict` to the example.

|     |     |
| --- | --- |
| Args |     |
| `feature_dict` | A dictionary from tf.Example feature key to tf.train.Feature. |

|     |
| --- |
| Returns |     |
| The builder object for subsequent method calls. |     |

### `add_floats_feature`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/tf_example_builder.py#L131-L144)

add_floats_feature(
        key: str, value: Union[float, Sequence[float]]
    ) -> TfExampleBuilder

Adds float(s) with `key` to the example.

|     |     |
| --- | --- |
| Args |     |
| `key` | String key of the feature. |
| `value` | The float(s) to be added to the example. |

|     |
| --- |
| Returns |     |
| The builder object for subsequent method calls. |     |

### `add_ints_feature`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/tf_example_builder.py#L116-L129)

add_ints_feature(
        key: str, value: Union[int, Sequence[int]]
    ) -> TfExampleBuilder

Adds integer(s) with `key` to the example.

|     |     |
| --- | --- |
| Args |     |
| `key` | String key of the feature. |
| `value` | The integer(s) to be added to the example. |

|     |
| --- |
| Returns |     |
| The builder object for subsequent method calls. |     |

### `reset`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/tf_example_builder.py#L63-L66)

reset() -> TfExampleBuilder

Resets the example to an empty proto.

### `set`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/tf_example_builder.py#L58-L61)

set(
        example: tf.train.Example
    ) -> TfExampleBuilder

Sets the example.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.