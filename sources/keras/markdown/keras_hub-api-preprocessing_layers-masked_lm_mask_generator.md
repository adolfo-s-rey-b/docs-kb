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
 / MaskedLMMaskGenerator layer

MaskedLMMaskGenerator layer
===========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/preprocessing/masked_lm_mask_generator.py#L27)

### `MaskedLMMaskGenerator` class

Copied!

`keras_hub.layers.MaskedLMMaskGenerator(     vocabulary_size,     mask_selection_rate,     mask_token_id,     mask_selection_length=None,     unselectable_token_ids=[0],     mask_token_rate=0.8,     random_token_rate=0.1,     **kwargs )`

Layer that applies language model masking.

This layer is useful for preparing inputs for masked language modeling (MaskedLM) tasks. It follows the masking strategy described in the [original BERT paper](https://arxiv.org/abs/1810.04805)
. Given tokenized text, it randomly selects certain number of tokens for masking. Then for each selected token, it has a chance (configurable) to be replaced by "mask token" or random token, or stay unchanged.

Input data should be passed as tensors, [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
s, or lists. For batched input, inputs should be a list of lists or a rank two tensor. For unbatched inputs, each element should be a list or a rank one tensor.

This layer can be used with [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
 to generate dynamic masks on the fly during training.

**Arguments**

*   **vocabulary\_size**: int, the size of the vocabulary.
*   **mask\_selection\_rate**: float, the probability of a token is selected for masking.
*   **mask\_token\_id**: int. The id of mask token.
*   **mask\_selection\_length**: int. Maximum number of tokens selected for masking in each sequence. If set, the output `mask_positions`, `mask_ids` and `mask_weights` will be padded to dense tensors of length `mask_selection_length`, otherwise the output will be a RaggedTensor. Defaults to `None`.
*   **unselectable\_token\_ids**: A list of tokens id that should not be considered eligible for masking. By default, we assume `0` corresponds to a padding token and ignore it. Defaults to `[0]`.
*   **mask\_token\_rate**: float. `mask_token_rate` must be between 0 and 1 which indicates how often the mask\_token is substituted for tokens selected for masking. Defaults to `0.8`.
*   **random\_token\_rate**: float. `random_token_rate` must be between 0 and 1 which indicates how often a random token is substituted for tokens selected for masking. Note: mask\_token\_rate + random\_token\_rate <= 1, and for (1 - mask\_token\_rate - random\_token\_rate), the token will not be changed. Defaults to `0.1`.

**Returns**

*   **A Dict with 4 keys**: token\_ids: Tensor or RaggedTensor, has the same type and shape of input. Sequence after getting masked. mask\_positions: Tensor, or RaggedTensor if `mask_selection_length` is None. The positions of token\_ids getting masked. mask\_ids: Tensor, or RaggedTensor if `mask_selection_length` is None. The original token ids at masked positions. mask\_weights: Tensor, or RaggedTensor if `mask_selection_length` is None. `mask_weights` has the same shape as `mask_positions` and `mask_ids`. Each element in `mask_weights` should be 0 or 1, 1 means the corresponding position in `mask_positions` is an actual mask, 0 means it is a pad.

**Examples**

Basic usage.

Copied!

`masker = keras_hub.layers.MaskedLMMaskGenerator(     vocabulary_size=10,     mask_selection_rate=0.2,     mask_token_id=0,     mask_selection_length=5 ) # Dense input. masker([1, 2, 3, 4, 5])  # Ragged input. masker([[1, 2], [1, 2, 3, 4]])`

Masking a batch that contains special tokens.

Copied!

`pad_id, cls_id, sep_id, mask_id = 0, 1, 2, 3 batch = [     [cls_id,   4,    5,      6, sep_id,    7,    8, sep_id, pad_id, pad_id],     [cls_id,   4,    5, sep_id,      6,    7,    8,      9, sep_id, pad_id], ]  masker = keras_hub.layers.MaskedLMMaskGenerator(     vocabulary_size = 10,     mask_selection_rate = 0.2,     mask_selection_length = 5,     mask_token_id = mask_id,     unselectable_token_ids = [         cls_id,         sep_id,         pad_id,     ] ) masker(batch)`

* * *

[MaskedLMMaskGenerator layer](https://keras.io/keras_hub/api/preprocessing_layers/masked_lm_mask_generator/#maskedlmmaskgenerator-layer)

[`MaskedLMMaskGenerator` class](https://keras.io/keras_hub/api/preprocessing_layers/masked_lm_mask_generator/#maskedlmmaskgenerator-class)