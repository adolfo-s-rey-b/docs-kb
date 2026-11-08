[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#methods_2)
    *   [clear](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#clear)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#get)
        
    *   [items](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#items)
        
    *   [keys](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#keys)
        
    *   [pop](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#pop)
        
    *   [popitem](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#popitem)
        
    *   [setdefault](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#setdefault)
        
    *   [update](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#update)
        
    *   [values](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#values)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#__eq__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#__len__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.distribution.LayoutMap Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#methods_2)
    *   [clear](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#clear)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#get)
        
    *   [items](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#items)
        
    *   [keys](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#keys)
        
    *   [pop](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#pop)
        
    *   [popitem](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#popitem)
        
    *   [setdefault](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#setdefault)
        
    *   [update](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#update)
        
    *   [values](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#values)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#__eq__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/LayoutMap?version=stable#__len__)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L774-L891)

A dict-like object that maps string to `TensorLayout` instances.

tf.keras.distribution.LayoutMap(
        device_mesh
    )

`LayoutMap` uses a string as key and a `TensorLayout` as value. There is a behavior difference between a normal Python dict and this class. The string key will be treated as a regex when retrieving the value. See the docstring of `get` for more details.

See below for a usage example. You can define the naming schema of the `TensorLayout`, and then retrieve the corresponding `TensorLayout` instance.

In the normal case, the key to query is usually the `variable.path`, which is the identifier of the variable.

As shortcut, tuple or list of axis names are also allowed when inserting as value, and will be converted to `TensorLayout`.

layout_map = LayoutMap(device_mesh)
    layout_map['.*dense.*kernel'] = (None, 'model')
    layout_map['.*dense.*bias'] = ('model',)
    layout_map['.*conv2d.*kernel'] = (None, None, None, 'model')
    layout_map['.*conv2d.*bias'] = ('model',)
    
    layout_1 = layout_map['dense_1.kernel']             # layout_1 == layout_2d
    layout_2 = layout_map['dense_1.bias']               # layout_2 == layout_1d
    layout_3 = layout_map['dense_2.kernel']             # layout_3 == layout_2d
    layout_4 = layout_map['dense_2.bias']               # layout_4 == layout_1d
    layout_5 = layout_map['my_model/conv2d_123/kernel'] # layout_5 == layout_4d
    layout_6 = layout_map['my_model/conv2d_123/bias']   # layout_6 == layout_1d
    layout_7 = layout_map['my_model/conv3d_1/kernel']   # layout_7 == None
    layout_8 = layout_map['my_model/conv3d_1/bias']     # layout_8 == None

|     |     |
| --- | --- |
| Args<br>---- |     |
| `device_mesh` | [`keras.distribution.DeviceMesh`](https://www.tensorflow.org/api_docs/python/tf/keras/distribution/DeviceMesh)<br> instance. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `device_mesh` |     |

Methods
-------

### `clear`

clear()

D.clear() -> None. Remove all items from D.

### `get`

get(
        key, default=None
    )

Retrieves the corresponding layout by the string key.

When there isn't an exact match, all the existing keys in the layout map will be treated as a regex and map against the input key again. When there are multiple matches for the regex, an `ValueError` will be raised. Returns `None` if there isn't any match found.

|     |     |
| --- | --- |
| Args |     |
| `key` | String key to query a layout. |

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

### `pop`

pop(
        key, default=<object object>
    )

D.pop(k\[,d\]) -> v, remove specified key and return the corresponding value. If key is not found, d is returned if given, otherwise KeyError is raised.

### `popitem`

popitem()

D.popitem() -> (k, v), remove and return some (key, value) pair as a 2-tuple; but raise KeyError if D is empty.

### `setdefault`

setdefault(
        key, default=None
    )

D.setdefault(k\[,d\]) -> D.get(k,d), also set D\[k\]=d if k not in D

### `update`

update(
        other, /, **kwds
    )

D.update(\[E, \]\*\*F) -> None. Update D from mapping/iterable E and F. If E present and has a .keys() method, does: for k in E: D\[k\] = E\[k\] If E present and lacks .keys() method, does: for (k, v) in E: D\[k\] = v In either case, this is followed by: for k, v in F.items(): D\[k\] = v

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L818-L849)

__getitem__(
        key
    )

Retrieves the corresponding layout by the string key.

When there isn't an exact match, all the existing keys in the layout map will be treated as a regex and map against the input key again. When there are multiple matches for the regex, an `ValueError` will be raised. Returns `None` if there isn't any match found.

|     |     |
| --- | --- |
| Args |     |
| `key` | String key to query a layout. |

|     |
| --- |
| Returns |     |
| Corresponding layout based on the query. |     |

### `__iter__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L882-L883)

__iter__()

### `__len__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/distribution/distribution_lib.py#L879-L880)

__len__()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.