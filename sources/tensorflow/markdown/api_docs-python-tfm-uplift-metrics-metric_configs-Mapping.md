[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs/Mapping#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs/Mapping)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs/Mapping?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs/Mapping#methods)
    *   [get](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs/Mapping#get)
        
    *   [items](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs/Mapping#items)
        
    *   [keys](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs/Mapping#keys)
        
    *   [values](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs/Mapping#values)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs/Mapping#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs/Mapping#__eq__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs/Mapping#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs/Mapping#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs/Mapping#__len__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.uplift.metrics.metric\_configs.Mapping Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs/Mapping#methods)
    *   [get](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs/Mapping#get)
        
    *   [items](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs/Mapping#items)
        
    *   [keys](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs/Mapping#keys)
        
    *   [values](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs/Mapping#values)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs/Mapping#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs/Mapping#__eq__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs/Mapping#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs/Mapping#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tfm/uplift/metrics/metric_configs/Mapping#__len__)
        

A Mapping is a generic container for associating key/value pairs.

This class provides concrete generic implementations of all methods except for **getitem**, **iter**, and **len**.

Methods
-------

### `get`

get(
        key, default=None
    )

Retrieve the corresponding layout by the string key.

When there isn't an exact match, all the existing keys in the layout map will be treated as a regex and map against the input key again. The first match will be returned, based on the key insertion order. Return None if there isn't any match found.

|     |     |
| --- | --- |
| Args |     |
| `key` | the string key as the query for the layout. |

|     |
| --- |
| Returns |     |
| Corresponding layout based on the query. |     |

### `items`

items()

D.items() -> a set-like object providing a view on D's items

### `keys`

keys()

D.keys() -> a set-like object providing a view on D's keys

### `values`

values()

D.values() -> an object providing a view on D's values

### `__contains__`

__contains__(
        key
    )

### `__eq__`

__eq__(
        other
    )

Return self==value.

### `__getitem__`

__getitem__(
        key
    )

### `__iter__`

__iter__()

### `__len__`

__len__()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.