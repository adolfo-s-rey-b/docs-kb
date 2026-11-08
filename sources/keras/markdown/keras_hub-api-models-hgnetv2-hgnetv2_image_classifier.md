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
 / [HGNetV2](https://keras.io/keras_hub/api/models/hgnetv2/)
 / HGNetV2ImageClassifier model

HGNetV2ImageClassifier model
============================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/hgnetv2/hgnetv2_image_classifier.py#L13)

### `HGNetV2ImageClassifier` class

Copied!

`keras_hub.models.HGNetV2ImageClassifier(     backbone,     preprocessor,     num_classes,     head_filters=None,     pooling="avg",     activation=None,     dropout=0.0,     head_dtype=None,     **kwargs )`

HGNetV2 image classification model.

`HGNetV2ImageClassifier` wraps a `HGNetV2Backbone` and a `HGNetV2ImageClassifierPreprocessor` to create a model that can be used for image classification tasks. This model implements the HGNetV2 architecture with an additional classification head including a 1x1 convolution layer, global pooling, and a dense output layer.

The model takes an additional `num_classes` argument, controlling the number of predicted output classes, and optionally, a `head_filters` argument to specify the number of filters in the classification head's convolution layer. To fine-tune with `fit()`, pass a dataset containing tuples of `(x, y)` labels where `x` is an image tensor and `y` is an integer from `[0, num_classes)`.\
\
**Arguments**\
\
*   **backbone**: A `HGNetV2Backbone` instance.\
*   **preprocessor**: A `HGNetV2ImageClassifierPreprocessor` instance, a [`keras.Layer`](https://keras.io/api/layers/base_layer#layer-class)\
     instance, or a callable. If `None` no preprocessing will be applied to the inputs.\
*   **num\_classes**: int. The number of classes to predict.\
*   **head\_filters**: int, optional. The number of filters in the classification head's 1x1 convolution layer. If `None`, it defaults to the last value of `hidden_sizes` from the backbone.\
*   **pooling**: `"avg"` or `"max"`. The type of global pooling to apply after the head convolution. Defaults to `"avg"`.\
*   **activation**: `None`, str, or callable. The activation function to use on the final `Dense` layer. Set `activation=None` to return the output logits. Defaults to `None`.\
*   **dropout**: float. Dropout rate applied before the final dense layer. Defaults to 0.0.\
*   **head\_dtype**: `None`, str, or `keras.mixed_precision.DTypePolicy`. The dtype to use for the classification head's computations and weights.\
\
**Examples**\
\
Call `predict()` to run inference.\
\
Copied!\
\
`# Load preset and predict. images = np.random.randint(0, 256, size=(2, 224, 224, 3)) classifier = keras_hub.models.HGNetV2ImageClassifier.from_preset(     "hgnetv2_b5_ssld_stage2_ft_in1k" ) classifier.predict(images)`\
\
Call `fit()` on a single batch.\
\
Copied!\
\
`# Load preset and train. images = np.random.randint(0, 256, size=(2, 224, 224, 3)) labels = [0, 3] classifier = keras_hub.models.HGNetV2ImageClassifier.from_preset(     "hgnetv2_b5_ssld_stage2_ft_in1k" ) classifier.fit(x=images, y=labels, batch_size=2)`\
\
Call `fit()` with custom loss, optimizer and frozen backbone.\
\
Copied!\
\
`classifier = keras_hub.models.HGNetV2ImageClassifier.from_preset(     "hgnetv2_b5_ssld_stage2_ft_in1k" ) classifier.compile(     loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),     optimizer=keras.optimizers.Adam(5e-5), ) classifier.backbone.trainable = False classifier.fit(x=images, y=labels, batch_size=2)`\
\
Create a custom HGNetV2 classifier with specific head configuration.\
\
Copied!\
\
`backbone = keras_hub.models.HGNetV2Backbone.from_preset(     "hgnetv2_b5_ssld_stage2_ft_in1k" ) preproc = keras_hub.models.HGNetV2ImageClassifierPreprocessor.from_preset(     "hgnetv2_b5_ssld_stage2_ft_in1k" ) classifier = keras_hub.models.HGNetV2ImageClassifier(     backbone=backbone,     preprocessor=preproc,     num_classes=10,     pooling="avg",     dropout=0.2, )`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)\
\
### `from_preset` method\
\
Copied!\
\
`HGNetV2ImageClassifier.from_preset(preset, load_weights=True, **kwargs)`\
\
Instantiate a [`keras_hub.models.Task`](https://keras.io/keras_hub/api/base_classes/task#task-class)\
 from a model preset.\
\
A preset is a directory of configs, weights and other file assets used to save and load a pre-trained model. The `preset` can be passed as one of:\
\
1.  a built-in preset identifier like `'bert_base_en'`\
2.  a Kaggle Models handle like `'kaggle://user/bert/keras/bert_base_en'`\
3.  a Hugging Face handle like `'hf://user/bert_base_en'`\
4.  a path to a local preset directory like `'./bert_base_en'`\
\
For any `Task` subclass, you can run `cls.presets.keys()` to list all built-in presets available on the class.\
\
This constructor can be called in one of two ways. Either from a task specific base class like `keras_hub.models.CausalLM.from_preset()`, or from a model class like `keras_hub.models.BertTextClassifier.from_preset()`. If calling from the a base class, the subclass of the returning object will be inferred from the config in the preset directory.\
\
**Arguments**\
\
*   **preset**: string. A built-in preset identifier, a Kaggle Models handle, a Hugging Face handle, or a path to a local directory.\
*   **load\_weights**: bool. If `True`, saved weights will be loaded into the model architecture. If `False`, all weights will be randomly initialized.\
\
**Examples**\
\
Copied!\
\
`# Load a Gemma generative task. causal_lm = keras_hub.models.CausalLM.from_preset(     "gemma_2b_en", )  # Load a Bert classification task. model = keras_hub.models.TextClassifier.from_preset(     "bert_base_en",     num_classes=2, )`\
\
| Preset | Parameters | Description |\
| --- | --- | --- |\
| [hgnetv2\_b4\_ssld\_stage2\_ft\_in1k](https://www.kaggle.com/models/keras/hgnetv2/keras/hgnetv2_b4_ssld_stage2_ft_in1k/1) | 13.60M | HGNetV2 B4 model with 2-stage SSLD training, fine-tuned on ImageNet-1K. |\
| [hgnetv2\_b5\_ssld\_stage1\_in22k\_in1k](https://www.kaggle.com/models/keras/hgnetv2/keras/hgnetv2_b5_ssld_stage1_in22k_in1k/1) | 33.42M | HGNetV2 B5 model with 1-stage SSLD training, pre-trained on ImageNet-22K and fine-tuned on ImageNet-1K. |\
| [hgnetv2\_b5\_ssld\_stage2\_ft\_in1k](https://www.kaggle.com/models/keras/hgnetv2/keras/hgnetv2_b5_ssld_stage2_ft_in1k/1) | 33.42M | HGNetV2 B5 model with 2-stage SSLD training, fine-tuned on ImageNet-1K. |\
| [hgnetv2\_b6\_ssld\_stage1\_in22k\_in1k](https://www.kaggle.com/models/keras/hgnetv2/keras/hgnetv2_b6_ssld_stage1_in22k_in1k/1) | 69.18M | HGNetV2 B6 model with 1-stage SSLD training, pre-trained on ImageNet-22K and fine-tuned on ImageNet-1K. |\
| [hgnetv2\_b6\_ssld\_stage2\_ft\_in1k](https://www.kaggle.com/models/keras/hgnetv2/keras/hgnetv2_b6_ssld_stage2_ft_in1k/1) | 69.18M | HGNetV2 B6 model with 2-stage SSLD training, fine-tuned on ImageNet-1K. |\
\
* * *\
\
### `backbone` property\
\
Copied!\
\
`keras_hub.models.HGNetV2ImageClassifier.backbone`\
\
A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)\
 model with the core architecture.\
\
* * *\
\
### `preprocessor` property\
\
Copied!\
\
`keras_hub.models.HGNetV2ImageClassifier.preprocessor`\
\
A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)\
 layer used to preprocess input.\
\
* * *\
\
[HGNetV2ImageClassifier model](https://keras.io/keras_hub/api/models/hgnetv2/hgnetv2_image_classifier/#hgnetv2imageclassifier-model)\
\
[`HGNetV2ImageClassifier` class](https://keras.io/keras_hub/api/models/hgnetv2/hgnetv2_image_classifier/#hgnetv2imageclassifier-class)\
\
[`from_preset` method](https://keras.io/keras_hub/api/models/hgnetv2/hgnetv2_image_classifier/#frompreset-method)\
\
[`backbone` property](https://keras.io/keras_hub/api/models/hgnetv2/hgnetv2_image_classifier/#backbone-property)\
\
[`preprocessor` property](https://keras.io/keras_hub/api/models/hgnetv2/hgnetv2_image_classifier/#preprocessor-property)