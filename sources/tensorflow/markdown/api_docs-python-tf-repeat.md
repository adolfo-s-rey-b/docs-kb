[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/repeat#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/repeat)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/repeat?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Frepeat&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/repeat#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/repeat#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/repeat#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.repeat Stay organized with collections Save and categorize content based on your preferences.
================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/repeat#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/repeat#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/repeat#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L6700-L6750)

Repeat elements of `input`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.repeat`](https://www.tensorflow.org/api_docs/python/tf/repeat)

tf.repeat(
        input, repeats, axis=None, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Transfer learning with YAMNet for environmental sound classification](https://www.tensorflow.org/tutorials/audio/transfer_learning_audio)<br>    <br>*   [Parametrized Quantum Circuits for Reinforcement Learning](https://www.tensorflow.org/quantum/tutorials/quantum_reinforcement_learning)<br>    <br>*   [Recommend movies for users with TensorFlow Ranking](https://www.tensorflow.org/ranking/tutorials/quickstart)<br>    <br>*   [Listwise ranking](https://www.tensorflow.org/recommenders/examples/listwise_ranking) |

See also [`tf.concat`](https://www.tensorflow.org/api_docs/python/tf/concat)
, [`tf.stack`](https://www.tensorflow.org/api_docs/python/tf/stack)
, [`tf.tile`](https://www.tensorflow.org/api_docs/python/tf/tile)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | An `N`\-dimensional Tensor. |
| `repeats` | An 1-D `int` Tensor. The number of repetitions for each element. repeats is broadcasted to fit the shape of the given axis. `len(repeats)` must equal `input.shape[axis]` if axis is not None. |
| `axis` | An int. The axis along which to repeat values. By default, (axis=None),use the flattened input array, and return a flat output array. |
| `name` | A name for the operation. |

|     |
| --- |
| Returns<br>------- |     |
| A Tensor which has the same shape as `input`, except along the given axis. If axis is None then the output array is flattened to match the flattened input array. |     |

#### Example usage:

    repeat(['a', 'b', 'c'], repeats=[3, 0, 2], axis=0)

    repeat([[1, 2], [3, 4]], repeats=[2, 3], axis=0)

    repeat([[1, 2], [3, 4]], repeats=[2, 3], axis=1)

    repeat(3, repeats=4)

    repeat([[1,2], [3,4]], repeats=2)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.