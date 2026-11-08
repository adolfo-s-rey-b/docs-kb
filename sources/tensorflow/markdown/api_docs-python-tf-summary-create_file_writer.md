[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/summary/create_file_writer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/summary/create_file_writer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/summary/create_file_writer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fsummary%2Fcreate_file_writer&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/summary/create_file_writer#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/summary/create_file_writer#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/summary/create_file_writer#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Was this helpful?

tf.summary.create\_file\_writer Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/summary/create_file_writer#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/summary/create_file_writer#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/summary/create_file_writer#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/summary_ops_v2.py#L520-L594)

Creates a summary file writer for the given log directory.

tf.summary.create_file_writer(
        logdir,
        max_queue=None,
        flush_millis=None,
        filename_suffix=None,
        name=None,
        experimental_trackable=False,
        experimental_mesh=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Introduction to modules, layers, and models](https://www.tensorflow.org/guide/intro_to_modules) | *   [pix2pix: Image-to-image translation with a conditional GAN](https://www.tensorflow.org/tutorials/generative/pix2pix)<br>    <br>*   [Migrating tf.summary usage to TF 2.x](https://www.tensorflow.org/tensorboard/migrate)<br>    <br>*   [Displaying image data in TensorBoard](https://www.tensorflow.org/tensorboard/image_summaries)<br>    <br>*   [TensorBoard Scalars: Logging training metrics in Keras](https://www.tensorflow.org/tensorboard/scalars_and_keras)<br>    <br>*   [Displaying text data in TensorBoard](https://www.tensorflow.org/tensorboard/text_summaries) |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `logdir` | a string specifying the directory in which to write an event file. |
| `max_queue` | the largest number of summaries to keep in a queue; will flush once the queue gets bigger than this. Defaults to 10. |
| `flush_millis` | the largest interval between flushes. Defaults to 120,000. |
| `filename_suffix` | optional suffix for the event file name. Defaults to `.v2`. |
| `name` | a name for the op that creates the writer. |
| `experimental_trackable` | a boolean that controls whether the returned writer will be a `TrackableResource`, which makes it compatible with SavedModel when used as a [`tf.Module`](https://www.tensorflow.org/api_docs/python/tf/Module)<br> property. |
| `experimental_mesh` | a [`tf.experimental.dtensor.Mesh`](https://www.tensorflow.org/api_docs/python/tf/experimental/dtensor/Mesh)<br> instance. When running with DTensor, the mesh (experimental\_mesh.host\_mesh()) will be used for bringing all the DTensor logging from accelerator to CPU mesh. |

|     |
| --- |
| Returns<br>------- |     |
| A SummaryWriter object. |     |

Was this helpful?

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.