[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Futils%2FConfig&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#methods)
    *   [as\_dict](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#as_dict)
        
    *   [freeze](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#freeze)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#get)
        
    *   [items](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#items)
        
    *   [keys](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#keys)
        
    *   [pop](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#pop)
        
    *   [to\_json](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#to_json)
        
    *   [unfreeze](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#unfreeze)
        
    *   [update](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#update)
        
    *   [values](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#values)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#__contains__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#__len__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.Config Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#methods)
    *   [as\_dict](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#as_dict)
        
    *   [freeze](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#freeze)
        
    *   [get](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#get)
        
    *   [items](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#items)
        
    *   [keys](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#keys)
        
    *   [pop](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#pop)
        
    *   [to\_json](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#to_json)
        
    *   [unfreeze](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#unfreeze)
        
    *   [update](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#update)
        
    *   [values](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#values)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#__contains__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tf/keras/utils/Config#__len__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/config.py#L12-L182)

A Config is a dict-like container for named values.

tf.keras.utils.Config(
        **kwargs
    )

It offers a few advantages over a plain dict:

*   Setting and retrieving values via attribute setting / getting.
*   Ability to freeze the config to ensure no accidental config modifications occur past a certain point in your program.
*   Easy serialization of the whole config as JSON.

#### Examples:

# Create a config via constructor arguments
    config = Config("learning_rate"=0.1, "momentum"=0.9)
    
    # Then keep adding to it via attribute-style setting
    config.use_ema = True
    config.ema_overwrite_frequency = 100
    
    # You can also add attributes via dict-like access
    config["seed"] = 123
    
    # You can retrieve entries both via attribute-style
    # access and dict-style access
    assert config.seed == 100
    assert config["learning_rate"] == 0.1

A config behaves like a dict:

config = Config("learning_rate"=0.1, "momentum"=0.9)
    for k, v in config.items():
        print(f"{k}={v}")
    
    print(f"keys: {list(config.keys())}")
    print(f"values: {list(config.values())}")

In fact, it can be turned into one:

config = Config("learning_rate"=0.1, "momentum"=0.9)
    dict_config = config.as_dict()

You can easily serialize a config to JSON:

config = Config("learning_rate"=0.1, "momentum"=0.9)
    
    json_str = config.to_json()

You can also freeze a config to prevent further changes:

config = Config()
    config.optimizer = "adam"
    config.seed = 123
    
    # Freeze the config to prevent changes.
    config.freeze()
    assert config.frozen
    
    config.foo = "bar"  # This will raise an error.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `frozen` | Returns True if the config is frozen. |

Methods
-------

### `as_dict`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/config.py#L108-L109)

as_dict()

### `freeze`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/config.py#L95-L97)

freeze()

Marks the config as frozen, preventing any ulterior modification.

### `get`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/config.py#L131-L132)

get(
        keyname, value=None
    )

### `items`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/config.py#L120-L121)

items()

### `keys`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/config.py#L114-L115)

keys()

### `pop`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/config.py#L123-L125)

pop(
        *args
    )

### `to_json`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/config.py#L111-L112)

to_json()

### `unfreeze`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/config.py#L99-L100)

unfreeze()

### `update`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/config.py#L127-L129)

update(
        *args, **kwargs
    )

### `values`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/config.py#L117-L118)

values()

### `__contains__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/config.py#L181-L182)

__contains__(
        item
    )

### `__getitem__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/config.py#L163-L164)

__getitem__(
        key
    )

### `__iter__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/config.py#L169-L172)

__iter__()

### `__len__`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/config.py#L174-L175)

__len__()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.