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
 / [MetaCLIP 2](https://keras.io/keras_hub/api/models/metaclip_2/)
 / MetaCLIP2Tokenizer

MetaCLIP2Tokenizer
==================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/metaclip_2/metaclip_2_tokenizer.py#L18)

### `MetaCLIP2Tokenizer` class

Copied!

`keras_hub.tokenizers.MetaCLIP2Tokenizer(proto, **kwargs)`

MetaCLIP 2 tokenizer using SentencePiece subword segmentation.

This tokenizer class tokenizes raw strings into integer sequences and is based on [`keras_hub.tokenizers.SentencePieceTokenizer`](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer#sentencepiecetokenizer-class)
. MetaCLIP 2 uses the XLM-V tokenizer (`facebook/xlm-v-base`) which is a multilingual SentencePiece BPE tokenizer with ~901K vocabulary supporting 100+ languages.

Unlike the underlying tokenizer, it will check for all special tokens needed by MetaCLIP 2 models and provides a `from_preset()` method to automatically download a matching vocabulary for a MetaCLIP 2 preset.

Note: The XLM-V tokenizer uses a remapping of special token indices similar to XLM-RoBERTa. The special tokens are mapped as follows: - `<s>` (BOS): 0 - `<pad>`: 1 - `</s>` (EOS): 2 - `<unk>`: 3

If input is a batch of strings (rank > 0), the layer will output a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 where the last dimension of the output is ragged.

If input is a scalar string (rank == 0), the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 with static shape `[None]`.

**Arguments**

*   **proto**: Either a `string` path to a SentencePiece proto file or a `bytes` object with a serialized SentencePiece proto. See the [SentencePiece repository](https://github.com/google/sentencepiece)
     for more details on the format.

**Examples**

Copied!

`# Unbatched input. tokenizer = keras_hub.models.MetaCLIP2Tokenizer.from_preset(     "metaclip_2_vit_huge_patch14_224" ) tokenizer("The quick brown fox jumped.")  # Batched input. tokenizer(["The quick brown fox jumped.", "The fox slept."])  # Detokenization. tokenizer.detokenize(tokenizer("The quick brown fox jumped."))  # Multilingual support (XLM-V supports 100+ languages) tokenizer("这是一个测试")  # Chinese tokenizer("これはテストです")  # Japanese`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`MetaCLIP2Tokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

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
| [metaclip\_2\_vit\_huge\_patch14\_224](https://www.kaggle.com/models/keras/metaclip2/keras/metaclip_2_vit_huge_patch14_224/1) | 1.86B | 2 billion parameter, 32-layer for vision and 24-layer for text, patch size of 14, image resolution 224x224. MetaCLIP 2 worldwide huge model (ViT-H-14-quickgelu-worldwide) trained on 29B seen pairs with QuickGELU activation. |
| [metaclip\_2\_vit\_huge\_patch14\_378](https://www.kaggle.com/models/keras/metaclip2/keras/metaclip_2_vit_huge_patch14_378/1) | 1.86B | 2 billion parameter, 32-layer for vision and 24-layer for text, patch size of 14, image resolution 378x378. MetaCLIP 2 worldwide huge model (ViT-H-14-378-worldwide) trained on 29B seen pairs. |
| [metaclip\_2\_vit\_giant\_patch14\_224](https://www.kaggle.com/models/keras/metaclip2/keras/metaclip_2_vit_giant_patch14_224/1) | 3.63B | 4 billion parameter, 40-layer for vision and 24-layer for text, patch size of 14, image resolution 224x224. MetaCLIP 2 worldwide giant model (ViT-bigG-14-worldwide) trained on 29B seen pairs. |
| [metaclip\_2\_vit\_giant\_patch14\_378](https://www.kaggle.com/models/keras/metaclip2/keras/metaclip_2_vit_giant_patch14_378/1) | 3.63B | 4 billion parameter, 40-layer for vision and 24-layer for text, patch size of 14, image resolution 378x378. MetaCLIP 2 worldwide giant model (ViT-bigG-14-378-worldwide) trained on 29B seen pairs. |

* * *

[MetaCLIP2Tokenizer](https://keras.io/keras_hub/api/models/metaclip_2/metaclip_2_tokenizer/#metaclip2tokenizer)

[`MetaCLIP2Tokenizer` class](https://keras.io/keras_hub/api/models/metaclip_2/metaclip_2_tokenizer/#metaclip2tokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/metaclip_2/metaclip_2_tokenizer/#frompreset-method)