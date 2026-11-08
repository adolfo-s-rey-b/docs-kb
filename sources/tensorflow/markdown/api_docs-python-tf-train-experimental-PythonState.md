[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/train/experimental/PythonState#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/train/experimental/PythonState)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/train/experimental/PythonState?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ftrain%2Fexperimental%2FPythonState&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/train/experimental/PythonState#methods)
    *   [deserialize](https://www.tensorflow.org/api_docs/python/tf/train/experimental/PythonState#deserialize)
        
    *   [serialize](https://www.tensorflow.org/api_docs/python/tf/train/experimental/PythonState#serialize)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.train.experimental.PythonState Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/train/experimental/PythonState#methods)
    *   [deserialize](https://www.tensorflow.org/api_docs/python/tf/train/experimental/PythonState#deserialize)
        
    *   [serialize](https://www.tensorflow.org/api_docs/python/tf/train/experimental/PythonState#serialize)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/trackable/python_state.py#L28-L87)

A mixin for putting Python state in an object-based checkpoint.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.train.experimental.PythonState`](https://www.tensorflow.org/api_docs/python/tf/train/experimental/PythonState)

This is an abstract class which allows extensions to TensorFlow's object-based checkpointing (see [`tf.train.Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint)
). For example a wrapper for NumPy arrays:

import io
    import numpy
    
    class NumpyWrapper(tf.train.experimental.PythonState):
    
      def __init__(self, array):
        self.array = array
    
      def serialize(self):
        string_file = io.BytesIO()
        try:
          numpy.save(string_file, self.array, allow_pickle=False)
          serialized = string_file.getvalue()
        finally:
          string_file.close()
        return serialized
    
      def deserialize(self, string_value):
        string_file = io.BytesIO(string_value)
        try:
          self.array = numpy.load(string_file, allow_pickle=False)
        finally:
          string_file.close()

Instances of `NumpyWrapper` are checkpointable objects, and will be saved and restored from checkpoints along with TensorFlow state like variables.

root = tf.train.Checkpoint(numpy=NumpyWrapper(numpy.array([1.])))
    save_path = root.save(prefix)
    root.numpy.array *= 2.
    assert [2.] == root.numpy.array
    root.restore(save_path)
    assert [1.] == root.numpy.array

Methods
-------

### `deserialize`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/trackable/python_state.py#L79-L81)

@abc.abstractmethod

Callback to deserialize the object.

### `serialize`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/trackable/python_state.py#L75-L77)

@abc.abstractmethod

Callback to serialize the object. Returns a string.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.