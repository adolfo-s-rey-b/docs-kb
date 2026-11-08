None

[KerasTuner: Hyperparam Tuning](https://keras.io/keras_tuner/)

[Getting started](https://keras.io/keras_tuner/getting_started/)
 [Developer guides](https://keras.io/keras_tuner/guides/)
 [API documentation](https://keras.io/keras_tuner/api/)
 [HyperParameters](https://keras.io/keras_tuner/api/hyperparameters/)
 [Tuners](https://keras.io/keras_tuner/api/tuners/)
 [Oracles](https://keras.io/keras_tuner/api/oracles/)
 [HyperModels](https://keras.io/keras_tuner/api/hypermodels/)
 [Errors](https://keras.io/keras_tuner/api/errors/)

► [KerasTuner: Hyperparam Tuning](https://keras.io/keras_tuner/)
 / [API documentation](https://keras.io/keras_tuner/api/)
 / [HyperModels](https://keras.io/keras_tuner/api/hypermodels/)
 / HyperImageAugment

HyperImageAugment
=================

[\[source\]](https://github.com/keras-team/keras-tuner/tree/v1.4.8/keras_tuner/src/applications/augment.py#L69)

### `HyperImageAugment` class

Copied!

`keras_tuner.applications.HyperImageAugment(     input_shape=None,     input_tensor=None,     rotate=0.5,     translate_x=0.4,     translate_y=0.4,     contrast=0.3,     augment_layers=3,     **kwargs )`

A image augmentation hypermodel.

The `HyperImageAugment` class searches for the best combination of image augmentation operations in Keras preprocessing layers. The input shape of the model should be (height, width, channels). The output of the model is of the same shape as the input.

**Arguments**

*   **input\_shape**: Optional shape tuple, e.g. `(256, 256, 3)`.
*   **input\_tensor**: Optional Keras tensor (i.e. output of `layers.Input()`) to use as image input for the model.
*   **rotate**: A number between \[0, 1\], a list of two numbers between \[0, 1\] or None. Configures the search space of the factor of random rotation transform in the augmentation. A factor is chosen for each trial. It sets maximum of clockwise and counterclockwise rotation in terms of fraction of pi, among all samples in the trial. Default is 0.5. When `rotate` is a single number, the search range is \[0, `rotate`\]. The transform is off when set to None.
*   **translate\_x**: A number between \[0, 1\], a list of two numbers between \[0, 1\] or None. Configures the search space of the factor of random horizontal translation transform in the augmentation. A factor is chosen for each trial. It sets maximum of horizontal translation in terms of ratio over the width among all samples in the trial. Default is 0.4. When `translate_x` is a single number, the search range is \[0, `translate_x`\]. The transform is off when set to None.
*   **translate\_y**: A number between \[0, 1\], a list of two numbers between \[0, 1\] or None. Configures the search space of the factor of random vertical translation transform in the augmentation. A factor is chosen for each trial. It sets maximum of vertical translation in terms of ratio over the height among all samples in the trial. Default is 0.4. When `translate_y` is a single number ,the search range is \[0, `translate_y`\]. The transform is off when set to None.
*   **contrast**: A number between \[0, 1\], a list of two numbers between \[0, 1\] or None. Configures the search space of the factor of random contrast transform in the augmentation. A factor is chosen for each trial. It sets maximum ratio of contrast change among all samples in the trial. Default is 0.3. When `contrast` is a single number, the search rnage is \[0, `contrast`\]. The transform is off when set to None.
*   **augment\_layers**: None, int or list of two ints, controlling the number of augment applied. Default is 3. When `augment_layers` is 0, all transform are applied sequentially. When `augment_layers` is nonzero, or a list of two ints, a simple version of RandAugment(https://arxiv.org/abs/1909.13719) is used. A search space for 'augment\_layers' is created to search \[0, `augment_layers`\], or between the two ints if a `augment_layers` is a list. For each trial, the hyperparameter 'augment\_layers' determines number of layers of augment transforms are applied, each randomly picked from all available transform types with equal probability on each sample.
*   **\*\*kwargs**: Additional keyword arguments that apply to all hypermodels. See [`keras_tuner.HyperModel`](https://keras.io/keras_tuner/api/hypermodels/base_hypermodel#hypermodel-class)
    .

**Example**

Copied!

`hm_aug = HyperImageAugment(input_shape=(32, 32, 3),                            augment_layers=0,                            rotate=[0.2, 0.3],                            translate_x=0.1,                            translate_y=None,                            contrast=None)`

Then the hypermodel `hm_aug` will search 'factor\_rotate' between \[0.2, 0.3\] and 'factor\_translate\_x' between \[0, 0.1\]. These two augments are applied on all samples with factor picked per each trial.

Copied!

`hm_aug = HyperImageAugment(input_shape=(32, 32, 3),                            translate_x=0.5,                            translate_y=[0.2, 0.4]                            contrast=None)`

Then the hypermodel `hm_aug` will search 'factor\_rotate' between \[0, 0.2\], 'factor\_translate\_x' between \[0, 0.5\], 'factor\_translate\_y' between \[0.2, 0.4\]. It will use RandAugment, searching 'augment\_layers' between \[0, 3\]. Each layer on each sample will be chosen from rotate, translate\_x and translate\_y.

* * *

[HyperImageAugment](https://keras.io/keras_tuner/api/hypermodels/hyper_image_augment/#hyperimageaugment)

[`HyperImageAugment` class](https://keras.io/keras_tuner/api/hypermodels/hyper_image_augment/#hyperimageaugment-class)