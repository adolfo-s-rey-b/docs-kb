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
 / [SigLIP](https://keras.io/keras_hub/api/models/siglip/)
 / SigLIPTokenizer

SigLIPTokenizer
===============

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/siglip/siglip_tokenizer.py#L8)

### `SigLIPTokenizer` class

Copied!

`keras_hub.tokenizers.SigLIPTokenizer(proto, **kwargs)`

SigLIP tokenizer layer based on SentencePiece.

This tokenizer class will tokenize raw strings into integer sequences and is based on [`keras_hub.tokenizers.SentencePieceTokenizer`](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer#sentencepiecetokenizer-class)
. Unlike the underlying tokenizer, it will check for all special tokens needed by SigLIP models and provides a `from_preset()` method to automatically download a matching vocabulary for a SigLIP preset.

If input is a batch of strings (rank > 0), the layer will output a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 where the last dimension of the output is ragged.

If input is a scalar string (rank == 0), the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 with static shape `[None]`.

**Arguments**

*   **proto**: Either a `string` path to a SentencePiece proto file, or a `bytes` object with a serialized SentencePiece proto. See the [SentencePiece repository](https://github.com/google/sentencepiece)
     for more details on the format.

**Examples**

Copied!

`# Unbatched input. tokenizer = keras_hub.models.SigLIPTokenizer.from_preset(     "siglip_base_patch16_224" ) tokenizer("The quick brown fox jumped.")  # Batched input. tokenizer(["The quick brown fox jumped.", "The fox slept."])  # Detokenization. tokenizer.detokenize(tokenizer("The quick brown fox jumped."))  # Custom vocabulary. bytes_io = io.BytesIO() ds = tf.data.Dataset.from_tensor_slices(["The quick brown fox jumped."]) sentencepiece.SentencePieceTrainer.train(     sentence_iterator=ds.as_numpy_iterator(),     model_writer=bytes_io,     vocab_size=8,     model_type="WORD",     pad_id=0,     bos_id=1,     eos_id=2,     unk_id=3,     unk_piece="<unk>", ) tokenizer = keras_hub.models.SigLIPTokenizer(     proto=bytes_io.getvalue(), ) tokenizer("The quick brown fox jumped.")`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`SigLIPTokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

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
| [siglip\_base\_patch16\_224](https://www.kaggle.com/models/keras/siglip/keras/siglip_base_patch16_224/1) | 203.16M | 200 million parameter, image size 224, pre-trained on WebLi. |
| [siglip\_base\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip_base_patch16_256/1) | 203.20M | 200 million parameter, image size 256, pre-trained on WebLi. |
| [siglip\_base\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip_base_patch16_384/1) | 203.45M | 200 million parameter, image size 384, pre-trained on WebLi. |
| [siglip\_base\_patch16\_512](https://www.kaggle.com/models/keras/siglip/keras/siglip_base_patch16_512/1) | 203.79M | 200 million parameter, image size 512, pre-trained on WebLi. |
| [siglip\_base\_patch16\_256\_multilingual](https://www.kaggle.com/models/keras/siglip/keras/siglip_base_patch16_256_multilingual/1) | 370.63M | 370 million parameter, image size 256, pre-trained on WebLi. |
| [siglip2\_base\_patch16\_224](https://www.kaggle.com/models/keras/siglip/keras/siglip2_base_patch16_224/1) | 375.19M | 375 million parameter, patch size 16, image size 224, pre-trained on WebLi. |
| [siglip2\_base\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip2_base_patch16_256/1) | 375.23M | 375 million parameter, patch size 16, image size 256, pre-trained on WebLi. |
| [siglip2\_base\_patch32\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip2_base_patch32_256/1) | 376.86M | 376 million parameter, patch size 32, image size 256, pre-trained on WebLi. |
| [siglip2\_base\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip2_base_patch16_384/1) | 376.86M | 376 million parameter, patch size 16, image size 384, pre-trained on WebLi. |
| [siglip\_large\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip_large_patch16_256/1) | 652.15M | 652 million parameter, image size 256, pre-trained on WebLi. |
| [siglip\_large\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip_large_patch16_384/1) | 652.48M | 652 million parameter, image size 384, pre-trained on WebLi. |
| [siglip\_so400m\_patch14\_224](https://www.kaggle.com/models/keras/siglip/keras/siglip_so400m_patch14_224/1) | 877.36M | 877 million parameter, image size 224, shape-optimized version, pre-trained on WebLi. |
| [siglip\_so400m\_patch14\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip_so400m_patch14_384/1) | 877.96M | 877 million parameter, image size 384, shape-optimized version, pre-trained on WebLi. |
| [medsiglip\_900m\_448](https://www.kaggle.com/models/keras/medsiglip/keras/medsiglip_900m_448/1) | 878.30M | A 900 million parameter variant of SigLIP trained to encode medical images and text into a common embedding space. MedSigLIP contains a vision encoder and a text encoder, and supports 448x448 image resolution with up to 64 text tokens. |
| [siglip2\_large\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip2_large_patch16_256/1) | 881.53M | 881 million parameter, patch size 16, image size 256, pre-trained on WebLi. |
| [siglip2\_large\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip2_large_patch16_384/1) | 881.86M | 881 million parameter, patch size 16, image size 384, pre-trained on WebLi. |
| [siglip2\_large\_patch16\_512](https://www.kaggle.com/models/keras/siglip/keras/siglip2_large_patch16_512/1) | 882.31M | 882 million parameter, patch size 16, image size 512, pre-trained on WebLi. |
| [siglip\_so400m\_patch16\_256\_i18n](https://www.kaggle.com/models/keras/siglip/keras/siglip_so400m_patch16_256_i18n/1) | 1.13B | 1.1 billion parameter, image size 256, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_so400m\_patch14\_224](https://www.kaggle.com/models/keras/siglip/keras/siglip2_so400m_patch14_224/1) | 1.14B | 1.1 billion parameter, patch size 14, image size 224, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_so400m\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip2_so400m_patch16_256/1) | 1.14B | 1.1 billion parameter, patch size 16, image size 256, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_so400m\_patch14\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip2_so400m_patch14_384/1) | 1.14B | 1.1 billion parameter, patch size 14, image size 224, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_so400m\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip2_so400m_patch16_384/1) | 1.14B | 1.1 billion parameter, patch size 16, image size 384, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_so400m\_patch16\_512](https://www.kaggle.com/models/keras/siglip/keras/siglip2_so400m_patch16_512/1) | 1.14B | 1.1 billion parameter, patch size 16, image size 512, shape-optimized version, pre-trained on WebLi. |
| [siglip2\_giant\_opt\_patch16\_256](https://www.kaggle.com/models/keras/siglip/keras/siglip2_giant_opt_patch16_256/2) | 1.87B | 1.8 billion parameter, patch size 16, image size 256, pre-trained on WebLi. |
| [siglip2\_giant\_opt\_patch16\_384](https://www.kaggle.com/models/keras/siglip/keras/siglip2_giant_opt_patch16_384/1) | 1.87B | 1.8 billion parameter, patch size 16, image size 384, pre-trained on WebLi. |

* * *

[SigLIPTokenizer](https://keras.io/keras_hub/api/models/siglip/siglip_tokenizer/#sigliptokenizer)

[`SigLIPTokenizer` class](https://keras.io/keras_hub/api/models/siglip/siglip_tokenizer/#sigliptokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/siglip/siglip_tokenizer/#frompreset-method)