[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/summary_iterator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/summary_iterator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/summary_iterator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/summary_iterator#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/summary_iterator#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.summary\_iterator Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/summary_iterator#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/summary_iterator#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/summary/summary_iterator.py#L39-L91)

Returns a iterator for reading `Event` protocol buffers from an event file.

tf.compat.v1.train.summary_iterator(
        path
    )

You can use this function to read events written to an event file. It returns a Python iterator that yields `Event` protocol buffers.

Example: Print the contents of an events file.

for e in tf.compat.v1.train.summary_iterator(path to events file):
        print(e)

Example: Print selected summary values.

# This example supposes that the events file contains summaries with a
    # summary value tag 'loss'.  These could have been added by calling
    # `add_summary()`, passing the output of a scalar summary op created with
    # with: `tf.compat.v1.summary.scalar('loss', loss_tensor)`.
    for e in tf.compat.v1.train.summary_iterator(path to events file):
        for v in e.summary.value:
            if v.tag == 'loss':
                print(tf.make_ndarray(v.tensor))

Example: Continuously check for new summary values.

summaries = tf.compat.v1.train.summary_iterator(path to events file)
    while True:
      for e in summaries:
          for v in e.summary.value:
              if v.tag == 'loss':
                  print(tf.make_ndarray(v.tensor))
      # Wait for a bit before checking the file for any new events
      time.sleep(wait time)

See the protocol buffer definitions of [Event](https://www.tensorflow.org/code/tensorflow/core/util/event.proto)
 and [Summary](https://www.tensorflow.org/code/tensorflow/core/framework/summary.proto)
 for more information about their attributes.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `path` | The path to an event file created by a `SummaryWriter`. |

|     |
| --- |
| Returns<br>------- |     |
| A iterator that yields `Event` protocol buffers |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.