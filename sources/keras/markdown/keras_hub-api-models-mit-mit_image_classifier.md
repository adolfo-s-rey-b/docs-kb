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
 / [MiT](https://keras.io/keras_hub/api/models/mit/)
 / MiTImageClassifier model

MiTImageClassifier model
========================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/mit/mit_image_classifier.py#L9)

### `MiTImageClassifier` class

Copied!

`keras_hub.models.MiTImageClassifier(     backbone,     num_classes,     preprocessor=None,     pooling="avg",     activation=None,     dropout=0.0,     head_dtype=None,     **kwargs )`

Base class for all image classification tasks.

`ImageClassifier` tasks wrap a [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 and a [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 to create a model that can be used for image classification. `ImageClassifier` tasks take an additional `num_classes` argument, controlling the number of predicted output classes.

To fine-tune with `fit()`, pass a dataset containing tuples of `(x, y)` labels where `x` is a string and `y` is an integer from `[0, num_classes)`. All `ImageClassifier` tasks include a `from_preset()` constructor which can be used to load a pre-trained config and weights.\
\
**Arguments**\
\
*   **backbone**: A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)\
     instance or a [`keras.Model`](https://keras.io/api/models/model#model-class)\
    .\
*   **num\_classes**: int. The number of classes to predict.\
*   **preprocessor**: `None`, a [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)\
     instance, a [`keras.Layer`](https://keras.io/api/layers/base_layer#layer-class)\
     instance, or a callable. If `None` no preprocessing will be applied to the inputs.\
*   **pooling**: `"avg"` or `"max"`. The type of pooling to apply on backbone output. Defaults to average pooling.\
*   **activation**: `None`, str, or callable. The activation function to use on the `Dense` layer. Set `activation=None` to return the output logits. Defaults to `"softmax"`.\
*   **head\_dtype**: `None`, str, or `keras.mixed_precision.DTypePolicy`. The dtype to use for the classification head's computations and weights.\
\
**Examples**\
\
Call `predict()` to run inference.\
\
Copied!\
\
`# Load preset and train images = np.random.randint(0, 256, size=(2, 224, 224, 3)) classifier = keras_hub.models.ImageClassifier.from_preset(     "resnet_50_imagenet" ) classifier.predict(images)`\
\
Call `fit()` on a single batch.\
\
Copied!\
\
`# Load preset and train images = np.random.randint(0, 256, size=(2, 224, 224, 3)) labels = [0, 3] classifier = keras_hub.models.ImageClassifier.from_preset(     "resnet_50_imagenet" ) classifier.fit(x=images, y=labels, batch_size=2)`\
\
Call `fit()` with custom loss, optimizer and backbone.\
\
Copied!\
\
`classifier = keras_hub.models.ImageClassifier.from_preset(     "resnet_50_imagenet" ) classifier.compile(     loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),     optimizer=keras.optimizers.Adam(5e-5), ) classifier.backbone.trainable = False classifier.fit(x=images, y=labels, batch_size=2)`\
\
Custom backbone.\
\
Copied!\
\
`images = np.random.randint(0, 256, size=(2, 224, 224, 3)) labels = [0, 3] backbone = keras_hub.models.ResNetBackbone(     stackwise_num_filters=[64, 64, 64],     stackwise_num_blocks=[2, 2, 2],     stackwise_num_strides=[1, 2, 2],     block_type="basic_block",     use_pre_activation=True,     pooling="avg", ) classifier = keras_hub.models.ImageClassifier(     backbone=backbone,     num_classes=4, ) classifier.fit(x=images, y=labels, batch_size=2)`\
\
* * *\
\
[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/task.py#L161)\
\
### `from_preset` method\
\
Copied!\
\
`MiTImageClassifier.from_preset(preset, load_weights=True, **kwargs)`\
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
| [mit\_b0\_ade20k\_512](https://www.kaggle.com/models/keras/mit/keras/mit_b0_ade20k_512/4) | 3.32M | MiT (MixTransformer) model with 8 transformer blocks. |\
| [mit\_b0\_cityscapes\_1024](https://www.kaggle.com/models/keras/mit/keras/mit_b0_cityscapes_1024/3) | 3.32M | MiT (MixTransformer) model with 8 transformer blocks. |\
| [mit\_b1\_ade20k\_512](https://www.kaggle.com/models/keras/mit/keras/mit_b1_ade20k_512/4) | 13.16M | MiT (MixTransformer) model with 8 transformer blocks. |\
| [mit\_b1\_cityscapes\_1024](https://www.kaggle.com/models/keras/mit/keras/mit_b1_cityscapes_1024/3) | 13.16M | MiT (MixTransformer) model with 8 transformer blocks. |\
| [mit\_b2\_ade20k\_512](https://www.kaggle.com/models/keras/mit/keras/mit_b2_ade20k_512/4) | 24.20M | MiT (MixTransformer) model with 16 transformer blocks. |\
| [mit\_b2\_cityscapes\_1024](https://www.kaggle.com/models/keras/mit/keras/mit_b2_cityscapes_1024/3) | 24.20M | MiT (MixTransformer) model with 16 transformer blocks. |\
| [mit\_b3\_ade20k\_512](https://www.kaggle.com/models/keras/mit/keras/mit_b3_ade20k_512/3) | 44.08M | MiT (MixTransformer) model with 28 transformer blocks. |\
| [mit\_b3\_cityscapes\_1024](https://www.kaggle.com/models/keras/mit/keras/mit_b3_cityscapes_1024/3) | 44.08M | MiT (MixTransformer) model with 28 transformer blocks. |\
| [mit\_b4\_ade20k\_512](https://www.kaggle.com/models/keras/mit/keras/mit_b4_ade20k_512/3) | 60.85M | MiT (MixTransformer) model with 41 transformer blocks. |\
| [mit\_b4\_cityscapes\_1024](https://www.kaggle.com/models/keras/mit/keras/mit_b4_cityscapes_1024/3) | 60.85M | MiT (MixTransformer) model with 41 transformer blocks. |\
| [mit\_b5\_ade20k\_640](https://www.kaggle.com/models/keras/mit/keras/mit_b5_ade20k_640/3) | 81.45M | MiT (MixTransformer) model with 52 transformer blocks. |\
| [mit\_b5\_cityscapes\_1024](https://www.kaggle.com/models/keras/mit/keras/mit_b5_cityscapes_1024/3) | 81.45M | MiT (MixTransformer) model with 52 transformer blocks. |\
\
* * *\
\
### `backbone` property\
\
Copied!\
\
`keras_hub.models.MiTImageClassifier.backbone`\
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
`keras_hub.models.MiTImageClassifier.preprocessor`\
\
A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)\
 layer used to preprocess input.\
\
* * *\
\
[MiTImageClassifier model](https://keras.io/keras_hub/api/models/mit/mit_image_classifier/#mitimageclassifier-model)\
\
[`MiTImageClassifier` class](https://keras.io/keras_hub/api/models/mit/mit_image_classifier/#mitimageclassifier-class)\
\
[`from_preset` method](https://keras.io/keras_hub/api/models/mit/mit_image_classifier/#frompreset-method)\
\
[`backbone` property](https://keras.io/keras_hub/api/models/mit/mit_image_classifier/#backbone-property)\
\
[`preprocessor` property](https://keras.io/keras_hub/api/models/mit/mit_image_classifier/#preprocessor-property)