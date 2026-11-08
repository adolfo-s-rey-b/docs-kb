[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/train/FeatureLists#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/train/FeatureLists)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/train/FeatureLists?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ftrain%2FFeatureLists&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/train/FeatureLists#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/train/FeatureLists#child_classes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.train.FeatureLists Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/train/FeatureLists#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/train/FeatureLists#child_classes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/core/example/feature.proto)

Mainly used as part of a [`tf.train.SequenceExample`](https://www.tensorflow.org/api_docs/python/tf/train/SequenceExample)
.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.FeatureLists`](https://www.tensorflow.org/api_docs/python/tf/train/FeatureLists)

Contains a list of [`tf.train.Feature`](https://www.tensorflow.org/api_docs/python/tf/train/Feature)
s.

The [`tf.train.SequenceExample`](https://www.tensorflow.org/api_docs/python/tf/train/SequenceExample)
 proto can be thought of as a proto implementation of the following python type:

# tf.train.Feature
    Feature = Union[List[bytes],\
                    List[int64],\
                    List[float]]
    
    # tf.train.FeatureList
    FeatureList = List[Feature]
    
    # tf.train.FeatureLists
    FeatureLists = Dict[str, FeatureList]
    
    class SequenceExample(typing.NamedTuple):
      context: Dict[str, Feature]
      feature_lists: FeatureLists

This proto implements the `Dict[str, FeatureList]` portion.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `feature_list` | `repeated FeatureListEntry feature_list` |

Child Classes
-------------

[`class FeatureListEntry`](https://www.tensorflow.org/api_docs/python/tf/train/FeatureLists/FeatureListEntry)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.