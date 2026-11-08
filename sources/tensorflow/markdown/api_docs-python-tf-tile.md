[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tile#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tile)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tile?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/tile#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tile#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/tile#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tile Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/tile#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tile#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/tile#returns)
    

Constructs a tensor by tiling a given tensor.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.manip.tile`](https://www.tensorflow.org/api_docs/python/tf/tile)
, [`tf.compat.v1.tile`](https://www.tensorflow.org/api_docs/python/tf/tile)

tf.tile(
        input: Annotated[Any, TV_Tile_T],
        multiples: Annotated[Any, TV_Tile_Tmultiples],
        name=None
    ) -> Annotated[Any, TV_Tile_T]

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Better performance with the tf.data API](https://www.tensorflow.org/guide/data_performance)<br>    <br>*   [Ragged tensors](https://www.tensorflow.org/guide/ragged_tensor)<br>    <br>*   [Understanding masking & padding](https://www.tensorflow.org/guide/keras/understanding_masking_and_padding) | *   [Time series forecasting](https://www.tensorflow.org/tutorials/structured_data/time_series)<br>    <br>*   [Calculate gradients](https://www.tensorflow.org/quantum/tutorials/gradients)<br>    <br>*   [Quantum data](https://www.tensorflow.org/quantum/tutorials/quantum_data)<br>    <br>*   [Parametrized Quantum Circuits for Reinforcement Learning](https://www.tensorflow.org/quantum/tutorials/quantum_reinforcement_learning)<br>    <br>*   [A Tutorial on Multi-Armed Bandits with Per-Arm Features](https://www.tensorflow.org/agents/tutorials/per_arm_bandits_tutorial) |

This operation creates a new tensor by replicating `input` `multiples` times. The output tensor's i'th dimension has `input.dims(i) * multiples[i]` elements, and the values of `input` are replicated `multiples[i]` times along the 'i'th dimension. For example, tiling `[a b c d]` by `[2]` produces `[a b c d a b c d]`.

    a = tf.constant([[1,2,3],[4,5,6]], tf.int32)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input` | A `Tensor`. Can be of any rank. |
| `multiples` | A `Tensor`. Must be one of the following types: `int32`, `int64`. 1-D. Length must be the same as the number of dimensions in `input` |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor`. Has the same type as `input`. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.