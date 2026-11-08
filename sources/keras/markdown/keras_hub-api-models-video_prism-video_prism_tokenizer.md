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
 / [Model Architectures](https://keras.io/keras_hub/api/models/)
 / [VideoPrism](https://keras.io/keras_hub/api/models/video_prism/)
 / VideoPrismTokenizer

VideoPrismTokenizer
===================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/video_prism/video_prism_tokenizer.py#L10)

### `VideoPrismTokenizer` class

Copied!

`keras_hub.tokenizers.VideoPrismTokenizer(proto, **kwargs)`

VideoPrism tokenizer layer based on SentencePiece.

This tokenizer class will tokenize raw strings into integer sequences and is based on [`keras_hub.tokenizers.SentencePieceTokenizer`](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer#sentencepiecetokenizer-class)
.

If input is a batch of strings (rank > 0), the layer will output a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 where the last dimension of the output is ragged.

If input is a scalar string (rank == 0), the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 with static shape `[None]`.

**Arguments**

*   **proto**: Either a `string` path to a SentencePiece proto file, or a `bytes` object with a serialized SentencePiece proto. See the [SentencePiece repository](https://github.com/google/sentencepiece)
     for more details on the format.

**Examples**

Copied!

`# Unbatched input. tokenizer = keras_hub.models.VideoPrismTokenizer.from_preset(     "videoprism_lvt_public_v1_base" ) tokenizer("The quick brown fox jumped.")  # Batched input. tokenizer(["The quick brown fox jumped.", "The fox slept."])  # Detokenization. tokenizer.detokenize(tokenizer("The quick brown fox jumped."))`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`VideoPrismTokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

Instantiate a `keras_hub.models.Tokenizer` from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a path to a local preset directory like `'./bert_base_en'`

For any `Tokenizer` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

This constructor can be called in one of two ways. Either from the base class like `keras_hub.models.Tokenizer.from_preset()`, or from a model class like `keras_hub.models.GemmaTokenizer.from_preset()`. If calling from the base class, the subclass of the returning object will be inferred from the config in the preset directory.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, the weights will be loaded into the model architecture. If `False`, the weights will be randomly initialized.

**Examples**

Copied!

`# Load a preset tokenizer. tokenizer = keras_hub.tokenizer.Tokenizer.from_preset("bert_base_en")  # Tokenize some input. tokenizer("The quick brown fox tripped.")  # Detokenize some input. tokenizer.detokenize([5, 6, 7, 8, 9])`

| Preset | Parameters | Description |
| --- | --- | --- |
| [videoprism\_public\_v1\_base](https://www.kaggle.com/models/keras/videoprism/keras/videoprism_public_v1_base/1) | 114.00M | 114 million parameter, 12-layer ViT-B, 16-frame, 288x288 resolution, video-only encoder for spatiotemporal representation. |
| [videoprism\_lvt\_public\_v1\_base](https://www.kaggle.com/models/keras/videoprism/keras/videoprism_lvt_public_v1_base/1) | 248.00M | 248 million parameter, 12-layer ViT-B video encoder + text encoder, 16-frame, 288x288 resolution, for multimodal video-language tasks. |
| [videoprism\_public\_v1\_large](https://www.kaggle.com/models/keras/videoprism/keras/videoprism_public_v1_large/1) | 354.00M | 354 million parameter, 24-layer ViT-L, 16-frame, 288x288 resolution, video-only encoder for spatiotemporal representation. |
| [videoprism\_lvt\_public\_v1\_large](https://www.kaggle.com/models/keras/videoprism/keras/videoprism_lvt_public_v1_large/1) | 580.00M | 580 million parameter, 24-layer ViT-L video encoder + text encoder, 16-frame, 288x288 resolution, for multimodal video-language tasks. |

* * *

[VideoPrismTokenizer](https://keras.io/keras_hub/api/models/video_prism/video_prism_tokenizer/#videoprismtokenizer)

[`VideoPrismTokenizer` class](https://keras.io/keras_hub/api/models/video_prism/video_prism_tokenizer/#videoprismtokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/video_prism/video_prism_tokenizer/#frompreset-method)