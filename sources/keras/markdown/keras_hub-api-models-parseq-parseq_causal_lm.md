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
 / [PARSeq](https://keras.io/keras_hub/api/models/parseq/)
 / PARSeqCausalLM model

PARSeqCausalLM model
====================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/parseq/parseq_causal_lm.py#L16)

### `PARSeqCausalLM` class

Copied!

`keras_hub.models.PARSeqCausalLM(     preprocessor,     backbone,     num_perms=6,     add_forward_perms=True,     add_mirrored_perms=True,     seed=None,     end_token_id=0,     **kwargs )`

Scene Text Recognition with PARSeq. Performs OCR in natural scenes using the PARSeq model described in [Scene Text Recognition with Permuted Autoregressive Sequence Models](https://arxiv.org/abs/2207.06966)
. PARSeq is a ViT-based model that allows iterative decoding by performing an autoregressive decoding phase, followed by a refinement phase. **Arguments**

*   **preprocessor**: A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
     instance or a [`keras.Layer`](https://keras.io/api/layers/base_layer#layer-class)
     instance. The preprocessor to use for the model.
*   **backbone**: A [`keras_hub.models.PARSeqBackbone`](https://keras.io/keras_hub/api/models/parseq/parseq_backbone#parseqbackbone-class)
     instance or a [`keras.Model`](https://keras.io/api/models/model#model-class)
    . The backbone model to use for the model.
*   **num\_perms**: int. The number of permutations to generate for training. Defaults to 6.
*   **add\_forward\_perms**: bool. Whether to add forward permutations to the generated permutations. Defaults to `True`.
*   **add\_mirrored\_perms**: bool. Whether to add mirrored permutations to the generated permutations. Defaults to `True`.
*   **seed**: int. The random seed to use for generating permutations. Defaults to `None`, which means no seed is set.
*   **\*\*kwargs**: Additional keyword arguments passed to the base [`keras_hub.models.CausalLM`](https://keras.io/keras_hub/api/base_classes/causal_lm#causallm-class)
     constructor.

**Examples**

Call `predict()` to run inference.

Copied!

``# Load preset and run inference images = np.random.randint(0, 256, size=(2, 32, 128, 3)) parseq = keras_hub.models.PARSeqCausalLM.from_preset(     "parseq_vit" ) parseq.generate(images)  # Call `fit()` on a single batch. images = np.random.randint(0, 256, size=(2, 32, 128, 3)) token_ids = np.array([[1, 2, 3, 4], [1, 2, 3, 0]]) padding_mask = np.array([[1, 1, 1, 1], [1, 1, 1, 0]]) parseq = keras_hub.models.PARSeqCausalLM.from_preset(     "parseq_vit" ) parseq.fit(     x={         "images": images,         "token_ids": token_ids,         "padding_mask": padding_mask     },     batch_size=2, )``

**Call `fit()` with custom loss, optimizer and image encoder**

.

Copied!

`# Initialize the image encoder, preprocessor and tokenizer mean, std = 0.5, 0.5 image_converter = PARSeqImageConverter(     image_size=(32, 128),     offset=-mean / std,     scale=1.0 / 255.0 / std,     interpolation="bicubic", ) tokenizer = PARSeqTokenizer(max_label_length=25) preprocessor = keras_hub.models.PARSeqCausalLMPreprocessor(     image_converter=image_converter,     tokenizer=tokenizer, )  # Create the backbone image_encoder = ViTBackbone(     image_shape=(32, 128, 3),     patch_size=(4, 8),     num_layers=12,     num_heads=6,     hidden_dim=384,     mlp_dim=384 * 4,     use_class_token=False,     name="encoder", ) backbone = PARSeqBackbone(     vocabulary_size=97,     max_label_length=25,     image_encoder=image_encoder,     num_decoder_heads=12,     num_decoder_layers=1,     decoder_hidden_dim=384,     decoder_mlp_dim=4 * 384, ) # Create the PARSeq model parseq = keras_hub.models.PARSeqCausalLM(     backbone=backbone,     preprocessor=preprocessor, ) parseq.compile(     loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),     optimizer=keras.optimizers.Adam(5e-5), ) parseq.fit(     x={         "images": images,         "token_ids": token_ids,         "padding_mask": padding_mask     },     batch_size=2, )`

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)

### `from_preset` method

Copied!

`PARSeqCausalLM.from_preset(preset, load_weights=True, **kwargs)`

Instantiate a [`keras_hub.models.Task`](https://keras.io/keras_hub/api/base_classes/task#task-class)
 from a model preset.

A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:

1.  a built-in preset identifier like `'bert_base_en'`
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`
3.  a Hugging Face handle like `'hf://user/bert_base_en'`
4.  a path to a local preset directory like `'./bert_base_en'`

For any `Task` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.

This constructor can be called in one of two ways. Either from a task specific base class like `keras_hub.models.CausalLM.from_preset()`, or from a model class like `keras_hub.models.BertTextClassifier.from_preset()`. If calling from the a base class, the subclass of the returning object will be inferred from the config in the preset directory.

**Arguments**

*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.
*   **load\_weights**: bool. If `True`, saved weights will be loaded into the model architecture. If `False`, all weights will be randomly initialized.

**Examples**

Copied!

`# Load a Gemma generative task. causal_lm = keras_hub.models.CausalLM.from_preset(     "gemma_2b_en", )  # Load a Bert classification task. model = keras_hub.models.TextClassifier.from_preset(     "bert_base_en",     num_classes=2, )`

| Preset | Parameters | Description |
| --- | --- | --- |
| [parseq](https://www.kaggle.com/models/keras/parseq/keras/parseq/1) | 23.83M | Permuted autoregressive sequence (PARSeq) base model for scene text recognition |

* * *

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/causal_lm.py#L284)

### `generate` method

Copied!

`PARSeqCausalLM.generate(     inputs, max_length=None, stop_token_ids="auto", strip_prompt=False )`

Generate text given prompt `inputs`.

This method generates text based on given `inputs`. The sampling method used for generation can be set via the `compile()` method.

If `inputs` are a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
, outputs will be generated "batch-by-batch" and concatenated. Otherwise, all inputs will be handled as a single batch.

If a `preprocessor` is attached to the model, `inputs` will be preprocessed inside the `generate()` function and should match the structure expected by the `preprocessor` layer (usually raw strings). If a `preprocessor` is not attached, inputs should match the structure expected by the `backbone`. See the example usage above for a demonstration of each.

**Arguments**

*   **inputs**: python data, tensor data, or a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
    . If a `preprocessor` is attached to the model, `inputs` should match the structure expected by the `preprocessor` layer. If a `preprocessor` is not attached, `inputs` should match the structure expected the `backbone` model.
*   **max\_length**: Optional. int. The max length of the generated sequence. Will default to the max configured `sequence_length` of the `preprocessor`. If `preprocessor` is `None`, `inputs` should be should be padded to the desired maximum length and this argument will be ignored.
*   **stop\_token\_ids**: Optional. `None`, "auto", or tuple of token ids. Defaults to "auto" which uses the `preprocessor.tokenizer.end_token_id`. Not specifying a processor will produce an error. None stops generation after generating `max_length` tokens. You may also specify a list of token id's the model should stop on. Note that sequences of tokens will each be interpreted as a stop token, multi-token stop sequences are not supported.
*   **strip\_prompt**: Optional. By default, generate() returns the full prompt followed by its completion generated by the model. If this option is set to True, only the newly generated text is returned.

* * *

### `backbone` property

Copied!

`keras_hub.models.PARSeqCausalLM.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.PARSeqCausalLM.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[PARSeqCausalLM model](https://keras.io/keras_hub/api/models/parseq/parseq_causal_lm/#parseqcausallm-model)

[`PARSeqCausalLM` class](https://keras.io/keras_hub/api/models/parseq/parseq_causal_lm/#parseqcausallm-class)

[`from_preset` method](https://keras.io/keras_hub/api/models/parseq/parseq_causal_lm/#frompreset-method)

[`generate` method](https://keras.io/keras_hub/api/models/parseq/parseq_causal_lm/#generate-method)

[`backbone` property](https://keras.io/keras_hub/api/models/parseq/parseq_causal_lm/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/parseq/parseq_causal_lm/#preprocessor-property)