[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/train/load_checkpoint#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/train/load_checkpoint)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/train/load_checkpoint?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ftrain%2Fload_checkpoint&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/train/load_checkpoint#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/load_checkpoint#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/train/load_checkpoint#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/train/load_checkpoint#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.train.load\_checkpoint Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/train/load_checkpoint#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/load_checkpoint#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/train/load_checkpoint#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/train/load_checkpoint#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/checkpoint_utils.py#L46-L80)

Returns `CheckpointReader` for checkpoint found in `ckpt_dir_or_file`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.load_checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/load_checkpoint)

tf.train.load_checkpoint(
        ckpt_dir_or_file
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Migrating model checkpoints](https://www.tensorflow.org/guide/migrate/migrating_checkpoints)<br>    <br>*   [Training checkpoints](https://www.tensorflow.org/guide/checkpoint)<br>    <br>*   [Migrate the fault tolerance mechanism](https://www.tensorflow.org/guide/migrate/fault_tolerance) |

If `ckpt_dir_or_file` resolves to a directory with multiple checkpoints, reader for the latest checkpoint is returned.

#### Example usage:

import tensorflow as tf
    a = tf.Variable(1.0)
    b = tf.Variable(2.0)
    ckpt = tf.train.Checkpoint(var_list={'a': a, 'b': b})
    ckpt_path = ckpt.save('tmp-ckpt')
    reader= tf.train.load_checkpoint(ckpt_path)
    print(reader.get_tensor('var_list/a/.ATTRIBUTES/VARIABLE_VALUE'))  # 1.0

|     |     |
| --- | --- |
| Args<br>---- |     |
| `ckpt_dir_or_file` | Directory with checkpoints file or path to checkpoint file. |

|     |
| --- |
| Returns<br>------- |     |
| `CheckpointReader` object. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `ckpt_dir_or_file` resolves to a directory with no checkpoints. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.