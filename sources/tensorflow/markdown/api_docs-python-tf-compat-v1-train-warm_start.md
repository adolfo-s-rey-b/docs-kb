[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/warm_start#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/warm_start)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/warm_start?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Ftrain%2Fwarm_start&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/warm_start#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/warm_start#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.warm\_start Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/warm_start#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/warm_start#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/warm_starting_util.py#L405-L561)

Warm-starts a model using the given settings.

tf.compat.v1.train.warm_start(
        ckpt_to_initialize_from,
        vars_to_warm_start='.*',
        var_name_to_vocab_info=None,
        var_name_to_prev_var_name=None
    )

If you are using a tf.estimator.Estimator, this will automatically be called during training.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `ckpt_to_initialize_from` | \[Required\] A string specifying the directory with checkpoint file(s) or path to checkpoint from which to warm-start the model parameters. |
| `vars_to_warm_start` | \[Optional\] One of the following:<br><br>*   A regular expression (string) that captures which variables to warm-start (see tf.compat.v1.get\_collection). This expression will only consider variables in the TRAINABLE\_VARIABLES collection -- if you need to warm-start non\_TRAINABLE vars (such as optimizer accumulators or batch norm statistics), please use the below option.<br>    <br>*   A list of strings, each a regex scope provided to tf.compat.v1.get\_collection with GLOBAL\_VARIABLES (please see tf.compat.v1.get\_collection). For backwards compatibility reasons, this is separate from the single-string argument type.<br>    <br>*   A list of Variables to warm-start. If you do not have access to the `Variable` objects at the call site, please use the above option.<br>    <br>*   `None`, in which case only TRAINABLE variables specified in `var_name_to_vocab_info` will be warm-started.<br>    <br><br>Defaults to `'.*'`, which warm-starts all variables in the TRAINABLE\_VARIABLES collection. Note that this excludes variables such as accumulators and moving statistics from batch norm. |
| `var_name_to_vocab_info` | \[Optional\] Dict of variable names (strings) to `tf.estimator.VocabInfo`. The variable names should be "full" variables, not the names of the partitions. If not explicitly provided, the variable is assumed to have no (changes to) vocabulary. |
| `var_name_to_prev_var_name` | \[Optional\] Dict of variable names (strings) to name of the previously-trained variable in `ckpt_to_initialize_from`. If not explicitly provided, the name of the variable is assumed to be same between previous checkpoint and current model. Note that this has no effect on the set of variables that is warm-started, and only controls name mapping (use `vars_to_warm_start` for controlling what variables to warm-start). |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the WarmStartSettings contains prev\_var\_name or VocabInfo configuration for variable names that are not used. This is to ensure a stronger check for variable configuration than relying on users to examine the logs. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.