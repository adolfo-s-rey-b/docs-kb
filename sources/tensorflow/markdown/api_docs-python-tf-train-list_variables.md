[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/train/list_variables#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/train/list_variables)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/train/list_variables?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/train/list_variables#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/list_variables#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/train/list_variables#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.train.list\_variables Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/train/list_variables#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/list_variables#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/train/list_variables#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/checkpoint_utils.py#L117-L147)

Lists the checkpoint keys and shapes of variables in a checkpoint.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.list_variables`](https://www.tensorflow.org/api_docs/python/tf/train/list_variables)

tf.train.list_variables(
        ckpt_dir_or_file
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Introduction to modules, layers, and models](https://www.tensorflow.org/guide/intro_to_modules) | *   [TensorFlow 2 TPUEmbeddingLayer: Quick Start](https://www.tensorflow.org/recommenders/examples/tpu_embedding_layer) |

Checkpoint keys are paths in a checkpoint graph.

#### Example usage:

import tensorflow as tf
    import os
    ckpt_directory = "/tmp/training_checkpoints/ckpt"
    ckpt = tf.train.Checkpoint(optimizer=optimizer, model=model)
    manager = tf.train.CheckpointManager(ckpt, ckpt_directory, max_to_keep=3)
    train_and_checkpoint(model, manager)
    tf.train.list_variables(manager.latest_checkpoint)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `ckpt_dir_or_file` | Directory with checkpoints file or path to checkpoint. |

|     |
| --- |
| Returns<br>------- |     |
| List of tuples `(key, shape)`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.