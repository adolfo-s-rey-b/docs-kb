[Skip to main content](https://www.tensorflow.org/api_docs/python/orbit#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/orbit)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/orbit?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/orbit#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/orbit#classes)
    
*   [Type Aliases](https://www.tensorflow.org/api_docs/python/orbit#type_aliases)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: orbit Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/orbit#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/orbit#classes)
    
*   [Type Aliases](https://www.tensorflow.org/api_docs/python/orbit#type_aliases)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/orbit/__init__.py)

Defines exported symbols for the [`orbit`](https://www.tensorflow.org/api_docs/python/orbit)
 package.

Modules
-------

[`actions`](https://www.tensorflow.org/api_docs/python/orbit/actions)
 module: Defines an "action" abstraction for use with [`orbit.Controller`](https://www.tensorflow.org/api_docs/python/orbit/Controller)
.

[`utils`](https://www.tensorflow.org/api_docs/python/orbit/utils)
 module: Defines exported symbols for the [`orbit.utils`](https://www.tensorflow.org/api_docs/python/orbit/utils)
 package.

Classes
-------

[`class AbstractEvaluator`](https://www.tensorflow.org/api_docs/python/orbit/AbstractEvaluator)
: An abstract class defining the API required for evaluation.

[`class AbstractTrainer`](https://www.tensorflow.org/api_docs/python/orbit/AbstractTrainer)
: An abstract class defining the API required for training.

[`class Controller`](https://www.tensorflow.org/api_docs/python/orbit/Controller)
: Class that controls the outer loop of model training and evaluation.

[`class StandardEvaluator`](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator)
: Implements the standard functionality of AbstractEvaluator APIs.

[`class StandardEvaluatorOptions`](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluatorOptions)
: Advanced options for the [`orbit.StandardEvaluator`](https://www.tensorflow.org/api_docs/python/orbit/StandardEvaluator)
.

[`class StandardTrainer`](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer)
: Implements standard functionality on top of the AbstractTrainer API.

[`class StandardTrainerOptions`](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainerOptions)
: Advanced options for [`orbit.StandardTrainer`](https://www.tensorflow.org/api_docs/python/orbit/StandardTrainer)
.

Type Aliases
------------

[`Action`](https://www.tensorflow.org/api_docs/python/orbit/Action)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-02-13 UTC.