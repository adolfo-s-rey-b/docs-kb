[Skip to main content](https://www.tensorflow.org/api_docs/python/orbit/actions/JSONPersistedValue#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/orbit/actions/JSONPersistedValue)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/orbit/actions/JSONPersistedValue?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/actions/JSONPersistedValue#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/actions/JSONPersistedValue#methods)
    *   [read](https://www.tensorflow.org/api_docs/python/orbit/actions/JSONPersistedValue#read)
        
    *   [write](https://www.tensorflow.org/api_docs/python/orbit/actions/JSONPersistedValue#write)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

orbit.actions.JSONPersistedValue Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/actions/JSONPersistedValue#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/actions/JSONPersistedValue#methods)
    *   [read](https://www.tensorflow.org/api_docs/python/orbit/actions/JSONPersistedValue#read)
        
    *   [write](https://www.tensorflow.org/api_docs/python/orbit/actions/JSONPersistedValue#write)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/orbit/actions/new_best_metric.py#L167-L222)

Represents a value that is persisted via a file-based backing store.

orbit.actions.JSONPersistedValue(
        initial_value: Any, filename: str, write_value: bool = True
    )

The value must be JSON-serializable. Each time the value is updated, it will be written to the backing file. It is only read from the file at initialization.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `initial_value` | The initial value to use if no backing file exists or was given. This must be a JSON-serializable value (possibly nested combination of lists, dicts, and primitive values). |
| `filename` | The path to use for persistent storage of the value. This may be `None`, in which case the value is not stable across preemptions. |
| `write_value` | If `True`, new values will be written to `filename` on calls to `write()`. If `False`, `filename` is only read once to restore any persisted value, and new values will not be written to it. This can be useful in certain multi-client settings to avoid race conditions or excessive file writes. If `filename` is `None`, this parameter has no effect. |

Methods
-------

### `read`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/actions/new_best_metric.py#L209-L211)

read()

Returns the value.

### `write`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/actions/new_best_metric.py#L213-L222)

write(
        value
    )

Writes the value, updating the backing store if one was provided.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-02-13 UTC.