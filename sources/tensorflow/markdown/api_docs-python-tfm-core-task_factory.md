[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/task_factory#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/task_factory)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/task_factory?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/core/task_factory#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.core.task\_factory Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/core/task_factory#functions)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/task_factory.py)

A global factory to register and access all registered tasks.

Functions
---------

[`get_task(...)`](https://www.tensorflow.org/api_docs/python/tfm/core/task_factory/get_task)
: Creates a Task (of suitable subclass type) from task\_config.

[`get_task_cls(...)`](https://www.tensorflow.org/api_docs/python/tfm/core/task_factory/get_task_cls)

[`register_task_cls(...)`](https://www.tensorflow.org/api_docs/python/tfm/core/task_factory/register_task_cls)
: Decorates a factory of Tasks for lookup by a subclass of TaskConfig.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.