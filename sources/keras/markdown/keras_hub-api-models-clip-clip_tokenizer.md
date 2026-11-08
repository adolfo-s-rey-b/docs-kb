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
 / [CLIP](https://keras.io/keras_hub/api/models/clip/)
 / CLIPTokenizer

CLIPTokenizer
=============

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/clip/clip_tokenizer.py#L20)

### `CLIPTokenizer` class

Copied!

`keras_hub.tokenizers.CLIPTokenizer(     vocabulary=None, merges=None, pad_with_end_token=False, **kwargs )`

A CLIP tokenizer using Byte-Pair Encoding subword segmentation.

This tokenizer class will tokenize raw strings into integer sequences and is based on [`keras_hub.tokenizers.BytePairTokenizer`](https://keras.io/keras_hub/api/tokenizers/byte_pair_tokenizer#bytepairtokenizer-class)
. Unlike the underlying tokenizer, it will check for all special tokens needed by CLIP models and provides a `from_preset()` method to automatically download a matching vocabulary for a CLIP preset.

If input is a batch of strings (rank > 0), the layer will output a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 where the last dimension of the output is ragged.

If input is a scalar string (rank == 0), the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 with static shape `[None]`.

**Arguments**

*   **vocabulary**: string or dict, maps token to integer ids. If it is a string, it should be the file path to a json file.
*   **merges**: string or list, contains the merge rule. If it is a string, it should be the file path to merge rules. The merge rule file should have one merge rule per line. Every merge rule contains merge entities separated by a space.
*   **pad\_with\_end\_token**: bool. Whether to pad the output with `end_token`.

**Examples**

Copied!

`# Unbatched input. tokenizer = keras_hub.models.CLIPTokenizer.from_preset(     "clip_vit_base_patch32" ) tokenizer("The quick brown fox jumped.")  # Batched input. tokenizer(["The quick brown fox jumped.", "The fox slept."])  # Detokenization. tokenizer.detokenize(tokenizer("The quick brown fox jumped."))`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`CLIPTokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

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
| [clip\_vit\_base\_patch16](https://www.kaggle.com/models/keras/clip/keras/clip_vit_base_patch16/3) | 149.62M | 150 million parameter, 12-layer for vision and 12-layer for text, patch size of 16, CLIP model. |
| [clip\_vit\_base\_patch32](https://www.kaggle.com/models/keras/clip/keras/clip_vit_base_patch32/3) | 151.28M | 151 million parameter, 12-layer for vision and 12-layer for text, patch size of 32, CLIP model. |
| [clip\_vit\_b\_32\_laion2b\_s34b\_b79k](https://www.kaggle.com/models/keras/clip/keras/clip_vit_b_32_laion2b_s34b_b79k/3) | 151.28M | 151 million parameter, 12-layer for vision and 12-layer for text, patch size of 32, Open CLIP model. |
| [clip\_vit\_large\_patch14](https://www.kaggle.com/models/keras/clip/keras/clip_vit_large_patch14/3) | 427.62M | 428 million parameter, 24-layer for vision and 12-layer for text, patch size of 14, CLIP model. |
| [clip\_vit\_large\_patch14\_336](https://www.kaggle.com/models/keras/clip/keras/clip_vit_large_patch14_336/3) | 427.94M | 428 million parameter, 24-layer for vision and 12-layer for text, patch size of 14, image size of 336, CLIP model. |
| [clip\_vit\_h\_14\_laion2b\_s32b\_b79k](https://www.kaggle.com/models/keras/clip/keras/clip_vit_h_14_laion2b_s32b_b79k/3) | 986.11M | 986 million parameter, 32-layer for vision and 24-layer for text, patch size of 14, Open CLIP model. |
| [clip\_vit\_g\_14\_laion2b\_s12b\_b42k](https://www.kaggle.com/models/keras/clip/keras/clip_vit_g_14_laion2b_s12b_b42k/3) | 1.37B | 1.4 billion parameter, 40-layer for vision and 24-layer for text, patch size of 14, Open CLIP model. |
| [clip\_vit\_bigg\_14\_laion2b\_39b\_b160k](https://www.kaggle.com/models/keras/clip/keras/clip_vit_bigg_14_laion2b_39b_b160k/3) | 2.54B | 2.5 billion parameter, 48-layer for vision and 32-layer for text, patch size of 14, Open CLIP model. |
| [sam3\_pcs](https://www.kaggle.com/models/keras/sam3/keras/sam3_pcs/1) | 30.00M | 30 million parameter Promptable Concept Segmentation (PCS) SAM model. |

* * *

[CLIPTokenizer](https://keras.io/keras_hub/api/models/clip/clip_tokenizer/#cliptokenizer)

[`CLIPTokenizer` class](https://keras.io/keras_hub/api/models/clip/clip_tokenizer/#cliptokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/clip/clip_tokenizer/#frompreset-method)