[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/view_as_complex#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/view_as_complex)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/view_as_complex?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/view_as_complex#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/view_as_complex#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.view\_as\_complex Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/view_as_complex#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/view_as_complex#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L1265-L1303)

Converts a real tensor with shape `(..., 2)` to a complex tensor, where the last dimension represents the real and imaginary components of a complex tensor.

tf.keras.ops.view_as_complex(
        x
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `x` | A real tensor with last dimension of size 2. |

|     |
| --- |
| Returns<br>------- |     |
| A complex tensor with shape `x.shape[:-1]`. |     |

#### Example:

> > > import numpy as np from keras import ops

<pre class="devsite-click-to-copy prettyprint lang-py">
    <code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">real_imag = np.array([[1.0, 2.0], [3.0, 4.0]])</code>
    <code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">complex_tensor = ops.view_as_complex(real_imag)</code>
    <code class="devsite-terminal" data-terminal-prefix="&gt;&gt;&gt;">complex_tensor</code>
    <code class="no-select nocode">array([1.+2.j, 3.+4.j])</code>
    </pre>

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.