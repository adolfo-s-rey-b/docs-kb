[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fdtype_policies%2FDTypePolicyMap&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#methods)
    *   [clear](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#clear)
        
    *   [convert\_input](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#convert_input)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#from_config)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#get)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#get_config)
        
    *   [items](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#items)
        
    *   [keys](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#keys)
        
    *   [pop](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#pop)
        
    *   [popitem](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#popitem)
        
    *   [setdefault](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#setdefault)
        
    *   [update](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#update)
        
    *   [values](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#values)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#__eq__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#__len__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.dtype\_policies.DTypePolicyMap Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#methods)
    *   [clear](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#clear)
        
    *   [convert\_input](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#convert_input)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#from_config)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#get)
        
    *   [get\_config](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#get_config)
        
    *   [items](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#items)
        
    *   [keys](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#keys)
        
    *   [pop](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#pop)
        
    *   [popitem](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#popitem)
        
    *   [setdefault](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#setdefault)
        
    *   [update](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#update)
        
    *   [values](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#values)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#__eq__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/dtype_policies/DTypePolicyMap#__len__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy_map.py#L9-L294)

Dict-like object mapping layer paths to `DTypePolicy` instances.

Inherits From: [`DTypePolicy`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy)

tf.keras.dtype_policies.DTypePolicyMap(
        default_policy=None, policy_map=None
    )

`DTypePolicyMap` can be used in `get_config` in layers and subclasses to support a complex configurations of dtype policies.

For example, we can modify `get_config` in [`layers.MultiHeadAttention`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/MultiHeadAttention)
 as follows to support the mixing of dtype policies, such as quantization.

@keras.saving.register_keras_serializable("MyPackage")
    class MyMultiHeadAttention(keras.layers.MultiHeadAttention):
        def get_config(self):
            config = super().get_config()
            dtype_policy_map = dtype_policies.DTypePolicyMap()
            for layer in self._flatten_layers():
                if layer.dtype_policy.quantization_mode is not None:
                    dtype_policy_map[layer.path] = layer.dtype_policy
            if len(dtype_policy_map) > 0:
                config.update({"dtype": dtype_policy_map})
            return config

Internally, `DTypePolicyMap` uses a string as a key and a `DTypePolicy` as the value. Typically, the key used for querying is the [`Layer.path`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer#path)
. However, it is also possible to set a regex as the key. See the docstring of `get` for more details.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `default_policy` | An optional `DTypePolicy` instance specifying the default dtype policy. If not specified, the value will default to [`keras.config.dtype_policy()`](https://www.tensorflow.org/api_docs/python/tf/keras/config/dtype_policy)<br>. |
| `policy_map` | An optional dict that maps string to `DTypePolicy` instances. Defaults to `None` |

#### Example:

> > > from keras.src import dtype\_policies bfloat16 = dtype\_policies.DTypePolicy("bfloat16") float16 = dtype\_policies.DTypePolicy("float16") float32 = dtype\_policies.DTypePolicy("float32") policy\_map = DTypePolicyMap(default\_policy=float32)

# Set policies using an exact path and a regex pattern.
    # Note: "decoder" will only match the exact path, not its children.

> > > policy\_map\["encoder/layer\_0/dense"\] = bfloat16 policy\_map\["encoder/.\*"\] = float16 policy\_map\["decoder"\] = bfloat16

# 1. An exact match is found and returned directly.

> > > policy\_map\["encoder/layer\_0/dense"\].name 'bfloat16'

# 2. A regex match is found for a child layer.
    # It matches the "encoder/.*" pattern.

> > > policy\_map\["encoder/attention/query"\].name 'float16'

# 3. No implicit prefix matching occurs.
    # "decoder/attention" does not match the key "decoder".
    # The default policy is returned.

> > > policy\_map\["decoder/attention"\].name 'float32'

# 4. A ValueError is raised if a path matches multiple patterns.

> > > policy\_map\["encoder/attention/.\*"\] = bfloat16
> > > 
> > > "encoder/attention/query" now matches two patterns:
> > > ===================================================
> > > 
> > > \- "encoder/.\*"
> > > ================
> > > 
> > > \- "encoder/attention/.\*"
> > > ==========================
> > > 
> > > try: ... policy\_map\["encoder/attention/query"\] ... except ValueError as e: ... print(e) Path 'encoder/attention/query' matches multiple dtype policy ..

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `compute_dtype` | The compute dtype of this policy.<br><br>This is the dtype layers will do their computations in. Typically layers output tensors with the compute dtype as well.<br><br>Note that even if the compute dtype is float16 or bfloat16, hardware devices may not do individual adds, multiplies, and other fundamental operations in float16 or bfloat16, but instead may do some of them in float32 for numeric stability. The compute dtype is the dtype of the inputs and outputs of the ops that the layer executes. Internally, many ops will do certain internal calculations in float32 or some other device-internal intermediate format with higher precision than float16/bfloat16, to increase numeric stability. |
| `default_policy` | The default dtype policy.<br><br>If `default_policy` is not specified in the constructor, this property will be [`keras.config.dtype_policy()`](https://www.tensorflow.org/api_docs/python/tf/keras/config/dtype_policy)<br>. |
| `name` | Returns the name of this policy. |
| `quantization_mode` | The quantization mode of this policy. |
| `variable_dtype` | The variable dtype of this policy.<br><br>This is the dtype layers will create their variables in, unless a layer explicitly chooses a different dtype. If this is different than [`DTypePolicy.compute_dtype`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy#compute_dtype)<br>, Layers will cast variables to the compute dtype to avoid type errors.<br><br>Variable regularizers are run in the variable dtype, not the compute dtype. |

Methods
-------

### `clear`

clear()

D.clear() -> None. Remove all items from D.

### `convert_input`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy.py#L150-L175)

convert_input(
        x, autocast, dtype
    )

Converts the input dtype based on `autocast` and `dtype`.

Note that `x` can be a tensor, symbolic tensor or numpy array, and this method will keep integer inputs untouched and only apply casting to floats.

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy_map.py#L265-L273)

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

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy_map.py#L244-L263)

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

### `__contains__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy_map.py#L241-L242)

__contains__(
        key
    )

### `__eq__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy.py#L190-L197)

__eq__(
        other
    )

Return self==value.

### `__getitem__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy_map.py#L125-L212)

__getitem__(
        key
    )

Retrieves the corresponding `DTypePolicy` by the string key.

This method first attempts an exact key match. If no exact match is found, it treats all keys in the map as regular expression patterns and uses `re.fullmatch` to find a policy.

For example, to apply a policy to all sublayers of an `encoder` block, the key should be explicitly set to `"encoder/.*"`. A key of `"encoder"` will only match the layer with that exact path.

|     |     |
| --- | --- |
| Args |     |
| `key` | str. The key to query for a `DTypePolicy`. |

|     |
| --- |
| Returns |     |
| The corresponding `DTypePolicy`. If no match is found, this method returns `self.default_policy`. |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If the `key` matches more than one regex pattern in the map. |

#### Example:

> > > from keras.src import dtype\_policies bfloat16 = dtype\_policies.DTypePolicy("bfloat16") float16 = dtype\_policies.DTypePolicy("float16") float32 = dtype\_policies.DTypePolicy("float32") policy\_map = DTypePolicyMap(default\_policy=float32)

# Set policies using an exact path and a regex pattern.
    # Note: "decoder" will only match the exact path, not its children.

> > > policy\_map\["encoder/layer\_0/dense"\] = bfloat16 policy\_map\["encoder/.\*"\] = float16 policy\_map\["decoder"\] = bfloat16

# 1. An exact match is found and returned directly.

> > > policy\_map\["encoder/layer\_0/dense"\].name 'bfloat16'

# 2. A regex match is found for a child layer.
    # It matches the "encoder/.*" pattern.

> > > policy\_map\["encoder/attention/query"\].name 'float16'

# 3. No implicit prefix matching occurs.
    # "decoder/attention" does not match the key "decoder".
    # The default policy is returned.

> > > policy\_map\["decoder/attention"\].name 'float32'

# 4. A ValueError is raised if a path matches multiple patterns.

> > > policy\_map\["encoder/attention/.\*"\] = bfloat16
> > > 
> > > "encoder/attention/query" now matches two patterns:
> > > ===================================================
> > > 
> > > \- "encoder/.\*"
> > > ================
> > > 
> > > \- "encoder/attention/.\*"
> > > ==========================
> > > 
> > > try: ... policy\_map\["encoder/attention/query"\] ... except ValueError as e: ... print(e) Path 'encoder/attention/query' matches multiple dtype policy ..

### `__iter__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy_map.py#L278-L279)

__iter__()

### `__len__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/dtype_policies/dtype_policy_map.py#L275-L276)

__len__()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.