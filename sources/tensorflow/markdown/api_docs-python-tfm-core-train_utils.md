[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftfm%2Fcore%2Ftrain_utils&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils#other-members)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: tfm.core.train\_utils Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils#classes)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils#functions)
    
*   [Other Members](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils#other-members)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/train_utils.py)

Training utils.

Classes
-------

[`class BestCheckpointExporter`](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/BestCheckpointExporter)
: Keeps track of the best result, and saves its checkpoint.

[`class ExperimentParser`](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/ExperimentParser)
: Constructs the Experiment config from Flags or equivalent object.

[`class ParseConfigOptions`](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/ParseConfigOptions)
: Use this dataclass instead of FLAGS to customize parse\_configuration().

Functions
---------

[`cast_leaf_nested_dict(...)`](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/cast_leaf_nested_dict)
: Cast the leaves of a dictionary with arbitrary depth in place.

[`convert_variables_to_constants_v2_as_graph(...)`](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/convert_variables_to_constants_v2_as_graph)
: Replaces all the variables in a graph with constants of the same values.

[`create_optimizer(...)`](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/create_optimizer)
: A create optimizer util to be backward compatability with new args.

[`create_trainer(...)`](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/create_trainer)
: Create trainer.

[`get_leaf_nested_dict(...)`](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/get_leaf_nested_dict)
: Get leaf from a dictionary with arbitrary depth with a list of keys.

[`maybe_create_best_ckpt_exporter(...)`](https://www.tensorflow.org/api_docs/python/tfm/core/train_lib/maybe_create_best_ckpt_exporter)
: Maybe create a BestCheckpointExporter object, according to the config.

[`parse_configuration(...)`](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/parse_configuration)
: Parses ExperimentConfig from flags.

[`read_global_step_from_checkpoint(...)`](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/read_global_step_from_checkpoint)
: Read global step from checkpoint, or get global step from its filename.

[`remove_ckpts(...)`](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/remove_ckpts)
: Remove model checkpoints, so we can restart.

[`save_gin_config(...)`](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/save_gin_config)
: Serializes and saves the experiment config.

[`serialize_config(...)`](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/serialize_config)
: Serializes and saves the experiment config.

[`try_count_flops(...)`](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/try_count_flops)
: Counts and returns model FLOPs.

[`try_count_params(...)`](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/try_count_params)
: Count the number of parameters if model is possible.

[`write_json_summary(...)`](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/write_json_summary)
: Dump evaluation metrics to json file.

[`write_model_params(...)`](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/write_model_params)
: Writes the model parameters and shapes to a file.

[`write_summary(...)`](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/write_summary)
: Write evaluation metrics to TF summary.

|     |     |
| --- | --- |
| Other Members<br>------------- |     |
| BEST\_CHECKPOINT\_NAME | `'best_ckpt'` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.