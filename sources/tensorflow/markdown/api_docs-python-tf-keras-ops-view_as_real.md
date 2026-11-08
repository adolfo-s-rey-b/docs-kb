[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/view_as_real#main-content)

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
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.view\_as\_real Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L1306-L1336)

Converts a complex tensor to a real tensor with shape `(..., 2)`, where the last dimension represents the real and imaginary components.

tf.keras.ops.view_as_real(
        x
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A complex tensor. |

|     |
| --- |
| Returns<br>------- |     |
| A real tensor where the last dimension contains the real and imaginary parts. |     |

#### Example:

> > > import numpy as np from keras import ops

<pre class="devsite-click-to-copy prettyprint lang-py">
    <code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">complex_tensor = np.array([1 + 2j, 3 + 4j])</code>
    <code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">real = ops.view_as_real(complex_tensor)</code>
    <code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">real</code>
    <code class="no-select nocode">array([[1., 2.],</code>\
    <code class="no-select nocode">       [3., 4.]])</code>
    </pre>

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.