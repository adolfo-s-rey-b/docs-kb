[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/train_utils/ExperimentParser#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.train\_utils.ExperimentParser Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/train_utils.py#L300-L374)

Constructs the Experiment config from Flags or equivalent object.

tfm.core.train_utils.ExperimentParser(
        flags_obj
    )

Most of the cases, users only need to call the `parse()` function:

builder = ExperimentParser(FLAGS)
    params = builder.parse()

The advanced users can modify the flow by calling the parse\_\*() functions separately.

Methods
-------

### `base_experiment`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/train_utils.py#L325-L329)

base_experiment()

Get the base experiment config from --experiment field.

### `parse`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/train_utils.py#L316-L323)

parse()

Overrall process of constructing Experiment config.

### `parse_config_file`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/train_utils.py#L331-L336)

parse_config_file(
        params
    )

Override the configs of params from the config\_file.

### `parse_data_service`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/train_utils.py#L348-L363)

parse_data_service(
        params
    )

Override the data service configs of params from flags.

### `parse_params_override`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/train_utils.py#L365-L374)

parse_params_override(
        params
    )

### `parse_runtime`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/train_utils.py#L338-L346)

parse_runtime(
        params
    )

Override the runtime configs of params from flags.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.