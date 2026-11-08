[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/hyperparams#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/hyperparams)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/hyperparams?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tfm/hyperparams#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/hyperparams#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/hyperparams#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.hyperparams Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tfm/hyperparams#modules)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/hyperparams#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/hyperparams#functions)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/modeling/hyperparams/__init__.py)

Hyperparams package definition.

Modules
-------

[`base_config`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/base_config)
 module: Base configurations to standardize experiments.

[`oneof`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/oneof)
 module: Config class that supports oneof functionality.

[`params_dict`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/params_dict)
 module: A parameter dictionary class which supports the nest structure.

Classes
-------

[`class Config`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/Config)
: The base configuration class that supports YAML/JSON based overrides.

[`class OneOfConfig`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/OneOfConfig)
: Configuration for configs with one of feature.

[`class ParamsDict`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/ParamsDict)
: A hyperparameter container class.

Functions
---------

[`bind(...)`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/bind)
: Bind a class to config cls.

[`nested_csv_str_to_json_str(...)`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/nested_csv_str_to_json_str)
: Converts a nested (using '.') comma-separated k=v string to a JSON string.

[`override_params_dict(...)`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/override_params_dict)
: Override a given ParamsDict using a dict, JSON/YAML/CSV string or YAML file.

[`read_yaml_to_params_dict(...)`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/read_yaml_to_params_dict)
: Reads a YAML file to a ParamsDict.

[`save_params_dict_to_yaml(...)`](https://www.tensorflow.org/api_docs/python/tfm/hyperparams/save_params_dict_to_yaml)
: Saves the input ParamsDict to a YAML file.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.