[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#methods)
    *   [clear](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#clear)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#from_config)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#get)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#get_config)
        
    *   [items](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#items)
        
    *   [keys](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#keys)
        
    *   [pop](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#pop)
        
    *   [popitem](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#popitem)
        
    *   [setdefault](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#setdefault)
        
    *   [update](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#update)
        
    *   [values](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#values)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#__call__)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#__eq__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#__len__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.optimizers.OptimizerMap Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#methods)
    *   [clear](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#clear)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#from_config)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#get)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#get_config)
        
    *   [items](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#items)
        
    *   [keys](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#keys)
        
    *   [pop](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#pop)
        
    *   [popitem](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#popitem)
        
    *   [setdefault](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#setdefault)
        
    *   [update](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#update)
        
    *   [values](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#values)
        
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#__call__)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#__eq__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/OptimizerMap#__len__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/multi_optimizer.py#L10-L158)

A class mapping variables to optimizers.

tf.keras.optimizers.OptimizerMap(
        default_optimizer, optimizer_map=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `default_optimizer` | Default Keras `Optimizer` for any unmapped variables. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `default_optimizer` |     |

Methods
-------

### `clear`

clear()

D.clear() -> None. Remove all items from D.

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/multi_optimizer.py#L149-L158)

@classmethod

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

### `get_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/multi_optimizer.py#L139-L147)

get_config()

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

### `__call__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/multi_optimizer.py#L136-L137)

__call__(
        variable
    )

Call self as a function.

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/multi_optimizer.py#L36-L99)

__getitem__(
        key
    )

Retrieves the corresponding `Optimizer` by the string key.

This method first attempts an exact key match. If no exact match is found, it treats all keys in the map as regular expression patterns and uses `re.fullmatch` to find a policy.

For example, to apply a optimizer to all sublayers of an `encoder` block, the key should be explicitly set to `"encoder/.*"`. A key of `"encoder"` will only match the layer with that exact path.

|     |     |
| --- | --- |
| Args |     |
| `key` | str. The key to query for an `Optimizer`. |

|     |
| --- |
| Returns |     |
| The corresponding `Optimizer`. If no match is found, this method returns `self.default_optimizer`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If the `key` matches more than one regex pattern in the map. |

#### Example:

> > > from keras.src import optimizers from keras.src.optimizers.multi\_optimizer import OptimizerMap opt\_adam = optimizers.Adam() opt\_sgd = optimizers.SGD() opt\_rmsprop = optimizers.RMSprop() optimizer\_map = OptimizerMap(default\_optimizer=opt\_rmsprop) optimizer\_map\["encoder/layer\_0/dense"\] = opt\_adam optimizer\_map\["encoder/.\*"\] = opt\_sgd optimizer\_map\["decoder"\] = opt\_adam

<pre class="devsite-click-to-copy prettyprint lang-py">
    <code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">optimizer_map[&quot;decoder&quot;].name</code>
    <code class="no-select nocode">&#x27;adam&#x27;</code>
    </pre>
    
    
    <pre class="devsite-click-to-copy prettyprint lang-py">
    <code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">optimizer_map[&quot;encoder/layer_0/dense&quot;].name</code>
    <code class="no-select nocode">&#x27;adam&#x27;</code>
    </pre>
    
    
    <pre class="devsite-click-to-copy prettyprint lang-py">
    <code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">optimizer_map[&quot;encoder/layer_0/attention/query&quot;].name</code>
    <code class="no-select nocode">&#x27;sgd&#x27;</code>
    </pre>
    
    
    <pre class="devsite-click-to-copy prettyprint lang-py">
    <code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">optimizer_map[&quot;decoder/layer_0/dense&quot;].name</code>
    <code class="no-select nocode">&#x27;rmsprop&#x27;</code>
    </pre>

### `__iter__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/multi_optimizer.py#L133-L134)

__iter__()

### `__len__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/optimizers/multi_optimizer.py#L130-L131)

__len__()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.