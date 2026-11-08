[Skip to main content](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManager#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManager)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManager?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManager#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManager#methods)
    *   [flush](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManager#flush)
        
    *   [summary\_writer](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManager#summary_writer)
        
    *   [write\_summaries](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManager#write_summaries)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

orbit.utils.SummaryManager Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManager#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManager#methods)
    *   [flush](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManager#flush)
        
    *   [summary\_writer](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManager#summary_writer)
        
    *   [write\_summaries](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManager#write_summaries)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/orbit/utils/summary_manager.py#L24-L112)

A utility class for managing summary writing.

Inherits From: [`SummaryManagerInterface`](https://www.tensorflow.org/api_docs/python/orbit/utils/SummaryManagerInterface)

orbit.utils.SummaryManager(
        summary_dir, summary_fn, global_step=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `summary_dir` | The directory in which to write summaries. If `None`, all summary writing operations provided by this class are no-ops. |
| `summary_fn` | A callable defined accepting `name`, `value`, and `step` parameters, making calls to [`tf.summary`](https://www.tensorflow.org/api_docs/python/tf/summary)<br> functions to write summaries. |
| `global_step` | A [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)<br> containing the global step value. |

Methods
-------

### `flush`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/utils/summary_manager.py#L64-L67)

flush()

Flushes the underlying summary writers.

### `summary_writer`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/utils/summary_manager.py#L47-L62)

summary_writer(
        relative_path=''
    )

Returns the underlying summary writer for a specific subdirectory.

|     |     |
| --- | --- |
| Args |     |
| `relative_path` | The current path in which to write summaries, relative to the summary directory. By default it is empty, which corresponds to the root directory. |

### `write_summaries`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/utils/summary_manager.py#L69-L103)

write_summaries(
        summary_dict
    )

Writes summaries for the given dictionary of values.

This recursively creates subdirectories for any nested dictionaries provided in `summary_dict`, yielding a hierarchy of directories which will then be reflected in the TensorBoard UI as different colored curves.

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

This will create two subdirectories, "dataset1" and "dataset2", inside the summary root directory. Each directory will contain event files including both "loss" and "accuracy" summaries.

|     |     |
| --- | --- |
| Args |     |
| `summary_dict` | A dictionary of values. If any value in `summary_dict` is itself a dictionary, then the function will create a subdirectory with name given by the corresponding key. This is performed recursively. Leaf values are then summarized using the summary writer instance specific to the parent relative path. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-02-13 UTC.