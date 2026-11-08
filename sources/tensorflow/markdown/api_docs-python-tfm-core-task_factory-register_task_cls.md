[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/task_factory/register_task_cls#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/task_factory/register_task_cls)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/task_factory/register_task_cls?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/task_factory/register_task_cls#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/core/task_factory/register_task_cls#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.task\_factory.register\_task\_cls Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/task_factory/register_task_cls#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tfm/core/task_factory/register_task_cls#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/task_factory.py#L23-L55)

Decorates a factory of Tasks for lookup by a subclass of TaskConfig.

tfm.core.task_factory.register_task_cls(
        task_config_cls
    )

This decorator supports registration of tasks as follows:

@dataclasses.dataclass
    class MyTaskConfig(TaskConfig):
      # Add fields here.
      pass
    
    @register_task_cls(MyTaskConfig)
    class MyTask(Task):
      # Inherits def __init__(self, task_config).
      pass
    
    my_task_config = MyTaskConfig()
    my_task = get_task(my_task_config)  # Returns MyTask(my_task_config).

Besisdes a class itself, other callables that create a Task from a TaskConfig can be decorated by the result of this function, as long as there is at most one registration for each config class.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `task_config_cls` | a subclass of TaskConfig (_not_ an instance of TaskConfig). Each task\_config\_cls can only be used for a single registration. |

|     |
| --- |
| Returns<br>------- |     |
| A callable for use as class decorator that registers the decorated class for creation from an instance of task\_config\_cls. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.