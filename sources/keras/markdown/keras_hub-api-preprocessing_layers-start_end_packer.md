None

[KerasHub: Pretrained Models](https://keras.io/keras_hub/)

[Getting started](https://keras.io/keras_hub/getting_started/)
 [Developer guides](https://keras.io/keras_hub/guides/)
 [API documentation](https://keras.io/keras_hub/api/)
 [Modeling API](https://keras.io/keras_hub/api/base_classes/)
 [Model Architectures](https://keras.io/keras_hub/api/models/)
 [Tokenizers](https://keras.io/keras_hub/api/tokenizers/)
 [Preprocessing Layers](https://keras.io/keras_hub/api/preprocessing_layers/)
 [Modeling Layers](https://keras.io/keras_hub/api/modeling_layers/)
 [Samplers](https://keras.io/keras_hub/api/samplers/)
 [Metrics](https://keras.io/keras_hub/api/metrics/)
 [Pretrained models list](https://keras.io/keras_hub/presets/)

► [KerasHub: Pretrained Models](https://keras.io/keras_hub/)
 / [API documentation](https://keras.io/keras_hub/api/)
 / [Preprocessing Layers](https://keras.io/keras_hub/api/preprocessing_layers/)
 / StartEndPacker layer

StartEndPacker layer
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/preprocessing/start_end_packer.py#L18)

### `StartEndPacker` class

Copied!

`keras_hub.layers.StartEndPacker(     sequence_length,     start_value=None,     end_value=None,     pad_value=None,     return_padding_mask=False,     name=None,     padding_side="right",     **kwargs )`

Adds start and end tokens to a sequence and pads to a fixed length.

This layer is useful when tokenizing inputs for tasks like translation, where each sequence should include a start and end marker. It should be called after tokenization. The layer will first trim inputs to fit, then add start/end tokens, and finally pad, if necessary, to `sequence_length`.

Input data should be passed as tensors, [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
s, or lists. For batched input, inputs should be a list of lists or a rank two tensor. For unbatched inputs, each element should be a list or a rank one tensor.

**Arguments**

*   **sequence\_length**: int. The desired output length.
*   **start\_value**: int/str/list/tuple. The ID(s) or token(s) that are to be placed at the start of each sequence. The dtype must match the dtype of the input tensors to the layer. If `None`, no start value will be added.
*   **end\_value**: int/str/list/tuple. The ID(s) or token(s) that are to be placed at the end of each input segment. The dtype must match the dtype of the input tensors to the layer. If `None`, no end value will be added.
*   **pad\_value**: int/str. The ID or token that is to be placed into the unused positions after the last segment in the sequence. If `None`, 0 or "" will be added depending on the dtype of the input tensor.
*   **return\_padding\_mask**: bool. Whether to return a boolean padding mask of all locations that are filled in with the `pad_value`.
*   **padding\_side**: str. Whether to pad the input on the "left" or "right". Defaults to "right".

**Call arguments**

*   **inputs**: A [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
    , [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
    , or list of python strings.
*   **sequence\_length**: Pass to override the configured `sequence_length` of the layer.
*   **add\_start\_value**: Pass `False` to not append a start value for this input.
*   **add\_end\_value**: Pass `False` to not append an end value for this input.

**Examples**

Unbatched input (int).

Copied!

`>>> inputs = [5, 6, 7] >>> start_end_packer = keras_hub.layers.StartEndPacker( ...     sequence_length=7, start_value=1, end_value=2, ... ) >>> outputs = start_end_packer(inputs) >>> np.array(outputs) array([1, 5, 6, 7, 2, 0, 0], dtype=int32)`

Batched input (int).

Copied!

`>>> inputs = [[5, 6, 7], [8, 9, 10, 11, 12, 13, 14]] >>> start_end_packer = keras_hub.layers.StartEndPacker( ...     sequence_length=6, start_value=1, end_value=2, ... ) >>> outputs = start_end_packer(inputs) >>> np.array(outputs) array([[ 1,  5,  6,  7,  2,  0],        [ 1,  8,  9, 10, 11,  2]], dtype=int32)`

Unbatched input (str).

Copied!

`>>> inputs = ["this", "is", "fun"] >>> start_end_packer = keras_hub.layers.StartEndPacker( ...     sequence_length=6, start_value="<s>", end_value="</s>", ...     pad_value="<pad>" ... ) >>> outputs = start_end_packer(inputs) >>> np.array(outputs).astype("U") array(['<s>', 'this', 'is', 'fun', '</s>', '<pad>'], dtype='<U5')`

Batched input (str).

Copied!

`>>> inputs = [["this", "is", "fun"], ["awesome"]] >>> start_end_packer = keras_hub.layers.StartEndPacker( ...     sequence_length=6, start_value="<s>", end_value="</s>", ...     pad_value="<pad>" ... ) >>> outputs = start_end_packer(inputs) >>> np.array(outputs).astype("U") array([['<s>', 'this', 'is', 'fun', '</s>', '<pad>'],        ['<s>', 'awesome', '</s>', '<pad>', '<pad>', '<pad>']], dtype='<U7')`

Multiple start tokens.

Copied!

`>>> inputs = [["this", "is", "fun"], ["awesome"]] >>> start_end_packer = keras_hub.layers.StartEndPacker( ...     sequence_length=6, start_value=["</s>", "<s>"], end_value="</s>", ...     pad_value="<pad>" ... ) >>> outputs = start_end_packer(inputs) >>> np.array(outputs).astype("U") array([['</s>', '<s>', 'this', 'is', 'fun', '</s>'],        ['</s>', '<s>', 'awesome', '</s>', '<pad>', '<pad>']], dtype='<U7')`

* * *

[StartEndPacker layer](https://keras.io/keras_hub/api/preprocessing_layers/start_end_packer/#startendpacker-layer)

[`StartEndPacker` class](https://keras.io/keras_hub/api/preprocessing_layers/start_end_packer/#startendpacker-class)