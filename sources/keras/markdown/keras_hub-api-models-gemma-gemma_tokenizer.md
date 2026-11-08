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
 / [Gemma](https://keras.io/keras_hub/api/models/gemma/)
 / GemmaTokenizer

GemmaTokenizer
==============

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/gemma/gemma_tokenizer.py#L8)

### `GemmaTokenizer` class

Copied!

`keras_hub.tokenizers.GemmaTokenizer(proto, **kwargs)`

Gemma tokenizer layer based on SentencePiece.

This tokenizer class will tokenize raw strings into integer sequences and is based on [`keras_hub.tokenizers.SentencePieceTokenizer`](https://keras.io/keras_hub/api/tokenizers/sentence_piece_tokenizer#sentencepiecetokenizer-class)
. Unlike the underlying tokenizer, it will check for all special tokens needed by Gemma models and provides a `from_preset()` method to automatically download a matching vocabulary for a Gemma preset.

If input is a batch of strings (rank > 0), the layer will output a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 where the last dimension of the output is ragged.

If input is a scalar string (rank == 0), the layer will output a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 with static shape `[None]`.

**Arguments**

*   **proto**: Either a `string` path to a SentencePiece proto file, or a `bytes` object with a serialized SentencePiece proto. See the [SentencePiece repository](https://github.com/google/sentencepiece)
     for more details on the format.

**Examples**

Copied!

`# Unbatched input. tokenizer = keras_hub.models.GemmaTokenizer.from_preset("gemma_2b_en") tokenizer("The quick brown fox jumped.")  # Batched input. tokenizer(["The quick brown fox jumped.", "The fox slept."])  # Detokenization. tokenizer.detokenize(tokenizer("The quick brown fox jumped."))  # Custom vocabulary. bytes_io = io.BytesIO() ds = tf.data.Dataset.from_tensor_slices(["The quick brown fox jumped."]) sentencepiece.SentencePieceTrainer.train(     sentence_iterator=ds.as_numpy_iterator(),     model_writer=bytes_io,     vocab_size=8,     model_type="WORD",     pad_id=0,     bos_id=1,     eos_id=2,     unk_id=3,     pad_piece="<pad>",     bos_piece="<bos>",     eos_piece="<eos>",     unk_piece="<unk>", ) tokenizer = keras_hub.models.GemmaTokenizer(     proto=bytes_io.getvalue(), ) tokenizer("The quick brown fox jumped.")`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/tokenizers/tokenizer.py#L213)

### `from_preset` method

Copied!

`GemmaTokenizer.from_preset(preset, config_file="tokenizer.json", **kwargs)`

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
| [vault\_gemma\_1b\_en](https://www.kaggle.com/models/keras/vaultgemma/keras/vault_gemma_1b_en/2) | 1.04B | 1 billion parameter, 26-layer, VaultGemma model. |
| [gemma\_2b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_2b_en/3) | 2.51B | 2 billion parameter, 18-layer, base Gemma model. |
| [gemma\_instruct\_2b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_instruct_2b_en/3) | 2.51B | 2 billion parameter, 18-layer, instruction tuned Gemma model. |
| [gemma\_1.1\_instruct\_2b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_1.1_instruct_2b_en/4) | 2.51B | 2 billion parameter, 18-layer, instruction tuned Gemma model. The 1.1 update improves model quality. |
| [code\_gemma\_1.1\_2b\_en](https://www.kaggle.com/models/keras/codegemma/keras/code_gemma_1.1_2b_en/2) | 2.51B | 2 billion parameter, 18-layer, CodeGemma model. This model has been trained on a fill-in-the-middle (FIM) task for code completion. The 1.1 update improves model quality. |
| [code\_gemma\_2b\_en](https://www.kaggle.com/models/keras/codegemma/keras/code_gemma_2b_en/2) | 2.51B | 2 billion parameter, 18-layer, CodeGemma model. This model has been trained on a fill-in-the-middle (FIM) task for code completion. |
| [gemma2\_2b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_2b_en/2) | 2.61B | 2 billion parameter, 26-layer, base Gemma model. |
| [gemma2\_instruct\_2b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_instruct_2b_en/2) | 2.61B | 2 billion parameter, 26-layer, instruction tuned Gemma model. |
| [shieldgemma\_2b\_en](https://www.kaggle.com/models/google/shieldgemma/keras/shieldgemma_2b_en/2) | 2.61B | 2 billion parameter, 26-layer, ShieldGemma model. |
| [c2s\_scale\_gemma\_2\_2b\_en](https://www.kaggle.com/models/keras/cell2sentence/keras/c2s_scale_gemma_2_2b_en/1) | 2.61B | A 2 billion parameter, single-cell biology-aware model built on the Gemma-2 architecture. |
| [gemma\_7b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_7b_en/4) | 8.54B | 7 billion parameter, 28-layer, base Gemma model. |
| [gemma\_instruct\_7b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_instruct_7b_en/4) | 8.54B | 7 billion parameter, 28-layer, instruction tuned Gemma model. |
| [gemma\_1.1\_instruct\_7b\_en](https://www.kaggle.com/models/keras/gemma/keras/gemma_1.1_instruct_7b_en/5) | 8.54B | 7 billion parameter, 28-layer, instruction tuned Gemma model. The 1.1 update improves model quality. |
| [code\_gemma\_7b\_en](https://www.kaggle.com/models/keras/codegemma/keras/code_gemma_7b_en/3) | 8.54B | 7 billion parameter, 28-layer, CodeGemma model. This model has been trained on a fill-in-the-middle (FIM) task for code completion. |
| [code\_gemma\_instruct\_7b\_en](https://www.kaggle.com/models/keras/codegemma/keras/code_gemma_instruct_7b_en/3) | 8.54B | 7 billion parameter, 28-layer, instruction tuned CodeGemma model. This model has been trained for chat use cases related to code. |
| [code\_gemma\_1.1\_instruct\_7b\_en](https://www.kaggle.com/models/keras/codegemma/keras/code_gemma_1.1_instruct_7b_en/3) | 8.54B | 7 billion parameter, 28-layer, instruction tuned CodeGemma model. This model has been trained for chat use cases related to code. The 1.1 update improves model quality. |
| [gemma2\_9b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_9b_en/4) | 9.24B | 9 billion parameter, 42-layer, base Gemma model. |
| [gemma2\_instruct\_9b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_instruct_9b_en/4) | 9.24B | 9 billion parameter, 42-layer, instruction tuned Gemma model. |
| [shieldgemma\_9b\_en](https://www.kaggle.com/models/google/shieldgemma/keras/shieldgemma_9b_en/2) | 9.24B | 9 billion parameter, 42-layer, ShieldGemma model. |
| [gemma2\_27b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_27b_en/3) | 27.23B | 27 billion parameter, 42-layer, base Gemma model. |
| [gemma2\_instruct\_27b\_en](https://www.kaggle.com/models/keras/gemma2/keras/gemma2_instruct_27b_en/3) | 27.23B | 27 billion parameter, 42-layer, instruction tuned Gemma model. |
| [shieldgemma\_27b\_en](https://www.kaggle.com/models/google/shieldgemma/keras/shieldgemma_27b_en/2) | 27.23B | 27 billion parameter, 42-layer, ShieldGemma model. |
| [c2s\_scale\_gemma\_2\_27b\_en](https://www.kaggle.com/models/keras/cell2sentence/keras/c2s_scale_gemma_2_27b_en/1) | 27.23B | A 27 billion parameter, single-cell biology-aware model built on the Gemma-2 architecture. |
| [pali\_gemma\_3b\_mix\_224](https://www.kaggle.com/models/keras/paligemma/keras/pali_gemma_3b_mix_224/4) | 2.92B | image size 224, mix fine tuned, text sequence length is 256 |
| [pali\_gemma\_3b\_224](https://www.kaggle.com/models/keras/paligemma/keras/pali_gemma_3b_224/4) | 2.92B | image size 224, pre trained, text sequence length is 128 |
| [pali\_gemma\_3b\_mix\_448](https://www.kaggle.com/models/keras/paligemma/keras/pali_gemma_3b_mix_448/4) | 2.92B | image size 448, mix fine tuned, text sequence length is 512 |
| [pali\_gemma\_3b\_448](https://www.kaggle.com/models/keras/paligemma/keras/pali_gemma_3b_448/4) | 2.92B | image size 448, pre trained, text sequence length is 512 |
| [pali\_gemma\_3b\_896](https://www.kaggle.com/models/keras/paligemma/keras/pali_gemma_3b_896/4) | 2.93B | image size 896, pre trained, text sequence length is 512 |
| [pali\_gemma2\_mix\_3b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_mix_3b_224/2) | 3.03B | 3 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_pt\_3b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_3b_224/2) | 3.03B | 3 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma\_2\_ft\_docci\_3b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma_2_ft_docci_3b_448/2) | 3.03B | 3 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been fine-tuned on the DOCCI dataset for improved descriptions with fine-grained details. |
| [pali\_gemma2\_mix\_3b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_mix_3b_448/2) | 3.03B | 3 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_pt\_3b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_3b_448/2) | 3.03B | 3 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_pt\_3b\_896](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_3b_896/2) | 3.04B | 3 billion parameter, image size 896, 27-layer for SigLIP-So400m vision encoder and 26-layer Gemma2 2B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_mix\_10b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_mix_10b_224/3) | 9.66B | 10 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_pt\_10b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_10b_224/3) | 9.66B | 10 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_ft\_docci\_10b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_ft_docci_10b_448/3) | 9.66B | 10 billion parameter, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been fine-tuned on the DOCCI dataset for improved descriptions with fine-grained details. |
| [pali\_gemma2\_mix\_10b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_mix_10b_448/3) | 9.66B | 10 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_pt\_10b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_10b_448/3) | 9.66B | 10 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_pt\_10b\_896](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_10b_896/3) | 9.67B | 10 billion parameter, image size 896, 27-layer for SigLIP-So400m vision encoder and 42-layer Gemma2 9B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_mix\_28b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_28b_mix_224/3) | 27.65B | 28 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 46-layer Gemma2 27B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_mix\_28b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_28b_mix_448/3) | 27.65B | 28 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 46-layer Gemma2 27B lanuage model. This model has been fine-tuned on a wide range of vision-language tasks and domains. |
| [pali\_gemma2\_pt\_28b\_224](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_28b_224/4) | 27.65B | 28 billion parameter, image size 224, 27-layer for SigLIP-So400m vision encoder and 46-layer Gemma2 27B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_pt\_28b\_448](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_28b_448/3) | 27.65B | 28 billion parameter, image size 448, 27-layer for SigLIP-So400m vision encoder and 46-layer Gemma2 27B lanuage model. This model has been pre-trained on a mixture of datasets. |
| [pali\_gemma2\_pt\_28b\_896](https://www.kaggle.com/models/keras/paligemma2/keras/pali_gemma2_pt_28b_896/3) | 27.65B | 28 billion parameter, image size 896, 27-layer for SigLIP-So400m vision encoder and 46-layer Gemma2 27B lanuage model. This model has been pre-trained on a mixture of datasets. |

* * *

[GemmaTokenizer](https://keras.io/keras_hub/api/models/gemma/gemma_tokenizer/#gemmatokenizer)

[`GemmaTokenizer` class](https://keras.io/keras_hub/api/models/gemma/gemma_tokenizer/#gemmatokenizer-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/gemma/gemma_tokenizer/#frompreset-method)