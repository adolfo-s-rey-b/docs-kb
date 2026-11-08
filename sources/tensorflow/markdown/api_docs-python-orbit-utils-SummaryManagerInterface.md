[Skip to main content](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManagerInterface#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManagerInterface)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManagerInterface?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManagerInterface#methods)
    *   [flush](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManagerInterface#flush)
        
    *   [summary\_writer](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManagerInterface#summary_writer)
        
    *   [write\_summaries](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManagerInterface#write_summaries)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

orbit.utils.SummaryManagerInterface Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManagerInterface#methods)
    *   [flush](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManagerInterface#flush)
        
    *   [summary\_writer](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManagerInterface#summary_writer)
        
    *   [write\_summaries](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManagerInterface#write_summaries)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/orbit/utils/summary_manager_interface.py#L20-L64)

A utility interface for managing summary writing.

Methods
-------

### `flush`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/utils/summary_manager_interface.py#L23-L26)

@abc.abstractmethod

Flushes the the recorded summaries.

### `summary_writer`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/utils/summary_manager_interface.py#L28-L31)

@abc.abstractmethod

Returns the underlying summary writer for scoped writers.

### `write_summaries`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/utils/summary_manager_interface.py#L33-L64)

@abc.abstractmethod

Writes summaries for the given dictionary of values.

The summary\_dict can be any nested dict. The SummaryManager should recursively creates summaries, yielding a hierarchy of summaries which will then be reflected in the corresponding UIs.

For example, users may evaluate on multiple datasets and return `summary_dict` as a nested dictionary:

{
        "dataset1": {
            "loss": loss1,
            "accuracy": accuracy1
        },
        "dataset2": {
            "loss": loss2,
            "accuracy": accuracy2
        },
    }

This will create two set of summaries, "dataset1" and "dataset2". Each summary dict will contain summaries including both "loss" and "accuracy".

|     |     |
| --- | --- |
| Args |     |
| `summary_dict` | A dictionary of values. If any value in `summary_dict` is itself a dictionary, then the function will create a new summary\_dict with name given by the corresponding key. This is performed recursively. Leaf values are then summarized using the parent relative path. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-02-13 UTC.