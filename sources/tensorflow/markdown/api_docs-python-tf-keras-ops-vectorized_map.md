[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/vectorized_map#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/vectorized_map)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/vectorized_map?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.vectorized\_map Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L1171-L1203)

Parallel map of `function` on axis 0 of tensor(s) `elements`.

tf.keras.ops.vectorized_map(
        function, elements
    )

Schematically, `vectorized_map` implements the following, in the case of a single tensor input `elements`:

def vectorized_map(function, elements):
        outputs = []
        for e in elements:
            outputs.append(function(e))
        return np.stack(outputs)

In the case of an iterable of tensors `elements`, it implements the following:

def vectorized_map(function, elements):
        batch_size = elements[0].shape[0]
        outputs = []
        for index in range(batch_size):
            outputs.append(function([e[index] for e in elements]))
        return np.stack(outputs)

In this case, `function` is expected to take as input a single list of tensor arguments.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.