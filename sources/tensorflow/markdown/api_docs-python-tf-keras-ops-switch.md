[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/ops/switch#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/ops/switch)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/ops/switch?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Fops%2Fswitch&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/switch#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/switch#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.ops.switch Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/ops/switch#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/ops/switch#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/core.py#L552-L590)

Apply exactly one of the `branches` given by `index`.

tf.keras.ops.switch(
        index, branches, *operands
    )

If `index` is out of bounds, it is clamped to within bounds.

The semantics of `switch` are given roughly by this Python implementation:

def switch(index, branches, *operands):
        index = clamp(0, index, len(branches) - 1)
        return branches[index](*operands)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `index` | An integer scalar indicating which branch function to apply. |
| `branches` | A sequence of functions to be applied based on `index`. |
| `operands` | Inputs to whichever branch is applied. |

|     |
| --- |
| Returns<br>------- |     |
| The outputs of `branch(*operands)` for the branch that was selected based on `index`. |     |

#### Examples:

    add_fn = lambda x, y: x + y

    keras.ops.switch(1, branches, x, y)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.