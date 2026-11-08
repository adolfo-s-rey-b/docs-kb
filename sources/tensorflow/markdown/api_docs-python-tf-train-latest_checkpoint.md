[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/train/latest_checkpoint#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/train/latest_checkpoint)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/train/latest_checkpoint?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/train/latest_checkpoint#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/latest_checkpoint#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/train/latest_checkpoint#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.train.latest\_checkpoint Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/train/latest_checkpoint#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/train/latest_checkpoint#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/train/latest_checkpoint#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/checkpoint/checkpoint_management.py#L328-L365)

Finds the filename of latest saved checkpoint file.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.latest_checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/latest_checkpoint)

tf.train.latest_checkpoint(
        checkpoint_dir, latest_filename=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrating model checkpoints](https://www.tensorflow.org/guide/migrate/migrating_checkpoints)<br>    <br>*   [Training checkpoints](https://www.tensorflow.org/guide/checkpoint)<br>    <br>*   [Estimators](https://www.tensorflow.org/guide/estimator) | *   [Custom training with tf.distribute.Strategy](https://www.tensorflow.org/tutorials/distribute/custom_training)<br>    <br>*   [Custom training loop with Keras and MultiWorkerMirroredStrategy](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_ctl)<br>    <br>*   [Multi-worker training with Keras](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras)<br>    <br>*   [Deep Convolutional Generative Adversarial Network](https://www.tensorflow.org/tutorials/generative/dcgan)<br>    <br>*   [pix2pix: Image-to-image translation with a conditional GAN](https://www.tensorflow.org/tutorials/generative/pix2pix) |

Gets the checkpoint state given the provided checkpoint\_dir and looks for a corresponding TensorFlow 2 (preferred) or TensorFlow 1.x checkpoint path. The latest\_filename argument is only applicable if you are saving checkpoint using [`v1.train.Saver.save`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#save)

See the [Training Checkpoints Guide](https://www.tensorflow.org/guide/checkpoint)
 for more details and examples.\`

|     |     |
| --- | --- |
| Args<br>---- |     |
| `checkpoint_dir` | Directory where the variables were saved. |
| `latest_filename` | Optional name for the protocol buffer file that contains the list of most recent checkpoint filenames. See the corresponding argument to [`v1.train.Saver.save`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/Saver#save)<br>. |

|     |
| --- |
| Returns<br>------- |     |
| The full path to the latest checkpoint or `None` if no checkpoint was found. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-05 UTC.