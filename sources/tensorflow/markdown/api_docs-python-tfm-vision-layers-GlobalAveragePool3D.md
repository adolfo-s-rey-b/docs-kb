[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/GlobalAveragePool3D#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/GlobalAveragePool3D)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/GlobalAveragePool3D?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/GlobalAveragePool3D#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/GlobalAveragePool3D#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/GlobalAveragePool3D#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.layers.GlobalAveragePool3D Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/GlobalAveragePool3D#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/GlobalAveragePool3D#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/GlobalAveragePool3D#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/nn_layers.py#L650-L781)

Creates a global average pooling layer with causal mode.

tfm.vision.layers.GlobalAveragePool3D(
        keepdims: bool = False,
        causal: bool = False,
        state_prefix: Optional[str] = None,
        **kwargs
    )

Implements causal mode, which runs a cumulative sum (with [`tf.cumsum`](https://www.tensorflow.org/api_docs/python/tf/math/cumsum)
) across frames in the time dimension, allowing the use of a stream buffer. Sums any valid input state with the current input to allow state to accumulate over several iterations.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `keepdims` | A `bool`. If True, keep the averaged dimensions. |
| `causal` | A `bool` of whether to run in causal mode with a cumulative sum across frames. |
| `state_prefix` | a prefix string to identify states. |
| `**kwargs` | Additional keyword arguments to be passed to this layer. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/nn_layers.py#L697-L781)

call(
        inputs: tf.Tensor,
        states: Optional[States] = None,
        output_states: bool = False
    ) -> Union[tf.Tensor, Tuple[tf.Tensor, States]]

Calls the layer with the given inputs.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | An input [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>. |
| `states` | A `dict` of states such that, if any of the keys match for this layer, will overwrite the contents of the buffer(s). Expected keys include `state_prefix + '__pool_buffer'` and `state_prefix + '__pool_frame_count'`. |
| `output_states` | A `bool`. If True, returns the output tensor and output states. Returns just the output tensor otherwise. |

|     |
| --- |
| Returns |     |
| An output [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> (and optionally the states if `output_states=True`). If `causal=True`, the output tensor will have shape `[batch_size, num_frames, 1, 1, channels]` if `keepdims=True`. We keep the frame dimension in this case to simulate a cumulative global average as if we are inputting one frame at a time. If `causal=False`, the output is equivalent to `tf_keras.layers.GlobalAveragePooling3D` with shape `[batch_size, 1, 1, 1, channels]` if `keepdims=True` (plus the optional buffer stored in `states`). |     |

|     |     |
| --- | --- |
| Raises |     |
| `ValueError` | If using 'channels\_first' data format. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.