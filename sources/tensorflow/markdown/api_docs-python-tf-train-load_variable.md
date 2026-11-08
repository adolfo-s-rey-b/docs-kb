[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/train/load_variable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/train/load_variable)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/train/load_variable?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/load_variable#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/train/load_variable#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.train.load\_variable Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/load_variable#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/train/load_variable#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/checkpoint_utils.py#L83-L114)

Returns the tensor value of the given variable in the checkpoint.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.load_variable`](https://www.tensorflow.org/api_docs/python/tf/train/load_variable)

tf.train.load_variable(
        ckpt_dir_or_file, name
    )

When the variable name is unknown, you can use [`tf.train.list_variables`](https://www.tensorflow.org/api_docs/python/tf/train/list_variables)
 to inspect all the variable names.

#### Example usage:

import tensorflow as tf
    a = tf.Variable(1.0)
    b = tf.Variable(2.0)
    ckpt = tf.train.Checkpoint(var_list={'a': a, 'b': b})
    ckpt_path = ckpt.save('tmp-ckpt')
    var= tf.train.load_variable(
        ckpt_path, 'var_list/a/.ATTRIBUTES/VARIABLE_VALUE')
    print(var)  # 1.0

|     |     |
| --- | --- |
| Args<br>---- |     |
| `ckpt_dir_or_file` | Directory with checkpoints file or path to checkpoint. |
| `name` | Name of the variable to return. |

|     |
| --- |
| Returns<br>------- |     |
| A numpy `ndarray` with a copy of the value of this variable. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.