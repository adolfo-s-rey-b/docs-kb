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
 / [MobileNetV5](https://keras.io/keras_hub/api/models/mobilenetv5/)
 / MobileNetV5ImageClassifier model

MobileNetV5ImageClassifier model
================================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/models/mobilenetv5/mobilenetv5_image_classifier.py#L18)

### `MobileNetV5ImageClassifier` class

Copied!

`keras_hub.models.MobileNetV5ImageClassifier(     backbone,     num_classes,     preprocessor=None,     head_hidden_size=2048,     global_pool="avg",     drop_rate=0.0,     head_dtype=None,     **kwargs )`

An end-to-end MobileNetV5 model for image classification.

This model attaches a classification head to a `MobileNetV5Backbone`. The head consists of a global pooling layer, an optional convolutional head, a dropout layer, and a final dense classifier layer.

This model can optionally be configured with a `preprocessor` layer, in which case it will automatically apply preprocessing to image inputs during `fit()`, `predict()`, and `evaluate()`.

**Arguments**

*   **backbone**: A [`keras_hub.models.MobileNetV5Backbone`](https://keras.io/keras_hub/api/models/mobilenetv5/mobilenetv5_backbone#mobilenetv5backbone-class)
     instance.
*   **num\_classes**: int. The number of classes for the classification head.
*   **preprocessor**: A [`keras_hub.models.ImageClassifierPreprocessor`](https://keras.io/keras_hub/api/base_classes/image_classifier_preprocessor#imageclassifierpreprocessor-class)
     or `None`. If `None`, this model will not apply preprocessing.
*   **head\_hidden\_size**: int. The number of channels in the convolutional head.
*   **global\_pool**: str. The type of global pooling to use.
*   **drop\_rate**: float. The dropout rate for the head.
*   **head\_dtype**: string or `keras.mixed_precision.DTypePolicy`. The dtype to use for the head computations and weights.

**Example**

Copied!

`import keras from keras_hub.models import MobileNetV5Backbone from keras_hub.models import MobileNetV5ImageClassifier  # Randomly initialized task model with a custom config. model_args = {     "stackwise_block_types": [["er"], ["uir", "uir"]],     "stackwise_num_blocks": [1, 2],     "stackwise_num_filters": [[24], [48, 48]],     "stackwise_strides": [[2], [2, 1]],     "stackwise_act_layers": [["relu"], ["relu", "relu"]],     "stackwise_exp_ratios": [[4.0], [6.0, 6.0]],     "stackwise_se_ratios": [[0.0], [0.0, 0.0]],     "stackwise_dw_kernel_sizes": [[0], [5, 5]],     "stackwise_dw_start_kernel_sizes": [[0], [0, 0]],     "stackwise_dw_end_kernel_sizes": [[0], [0, 0]],     "stackwise_exp_kernel_sizes": [[3], [0, 0]],     "stackwise_pw_kernel_sizes": [[1], [0, 0]],     "stackwise_num_heads": [[0], [0, 0]],     "stackwise_key_dims": [[0], [0, 0]],     "stackwise_value_dims": [[0], [0, 0]],     "stackwise_kv_strides": [[0], [0, 0]],     "stackwise_use_cpe": [[False], [False, False]],     "use_msfa": False, } backbone = MobileNetV5Backbone(**model_args) model = MobileNetV5ImageClassifier(backbone, 1000) images = keras.ops.ones((1, 224, 224, 3)) output = model.predict(images)`

* * *

### `backbone` property

Copied!

`keras_hub.models.MobileNetV5ImageClassifier.backbone`

A [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 model with the core architecture.

* * *

### `preprocessor` property

Copied!

`keras_hub.models.MobileNetV5ImageClassifier.preprocessor`

A [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 layer used to preprocess input.

* * *

[MobileNetV5ImageClassifier model](https://keras.io/keras_hub/api/models/mobilenetv5/mobilenetv5_image_classifier/#mobilenetv5imageclassifier-model)

[`MobileNetV5ImageClassifier` class](https://keras.io/keras_hub/api/models/mobilenetv5/mobilenetv5_image_classifier/#mobilenetv5imageclassifier-class)

[`backbone` property](https://keras.io/keras_hub/api/models/mobilenetv5/mobilenetv5_image_classifier/#backbone-property)

[`preprocessor` property](https://keras.io/keras_hub/api/models/mobilenetv5/mobilenetv5_image_classifier/#preprocessor-property)