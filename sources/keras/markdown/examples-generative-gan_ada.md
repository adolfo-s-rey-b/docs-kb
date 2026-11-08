None

[Code examples](https://keras.io/examples/)

[Computer Vision](https://keras.io/examples/vision/)
 [Natural Language Processing](https://keras.io/examples/nlp/)
 [Structured Data](https://keras.io/examples/structured_data/)
 [Timeseries](https://keras.io/examples/timeseries/)
 [Generative Deep Learning](https://keras.io/examples/generative/)
 [Denoising Diffusion Implicit Models](https://keras.io/examples/generative/ddim/)
 [A walk through latent space with Stable Diffusion 3](https://keras.io/examples/generative/random_walks_with_stable_diffusion_3/)
 [DreamBooth](https://keras.io/examples/generative/dreambooth/)
 [Denoising Diffusion Probabilistic Models](https://keras.io/examples/generative/ddpm/)
 [Teach StableDiffusion new concepts via Textual Inversion](https://keras.io/examples/generative/fine_tune_via_textual_inversion/)
 [Fine-tuning Stable Diffusion](https://keras.io/examples/generative/finetune_stable_diffusion/)
 [Variational AutoEncoder](https://keras.io/examples/generative/vae/)
 [GAN overriding Model.train\_step](https://keras.io/examples/generative/dcgan_overriding_train_step/)
 [WGAN-GP overriding Model.train\_step](https://keras.io/examples/generative/wgan_gp/)
 [Conditional GAN](https://keras.io/examples/generative/conditional_gan/)
 [CycleGAN](https://keras.io/examples/generative/cyclegan/)
 [Data-efficient GANs with Adaptive Discriminator Augmentation](https://keras.io/examples/generative/gan_ada/)
 [Deep Dream](https://keras.io/examples/generative/deep_dream/)
 [GauGAN for conditional image generation](https://keras.io/examples/generative/gaugan/)
 [PixelCNN](https://keras.io/examples/generative/pixelcnn/)
 [Face image generation with StyleGAN](https://keras.io/examples/generative/stylegan/)
 [Vector-Quantized Variational Autoencoders](https://keras.io/examples/generative/vq_vae/)
 [A walk through latent space with Stable Diffusion](https://keras.io/examples/generative/random_walks_with_stable_diffusion/)
 [Neural style transfer](https://keras.io/examples/generative/neural_style_transfer/)
 [Neural Style Transfer with AdaIN](https://keras.io/examples/generative/adain/)
 [GPT2 Text Generation with KerasHub](https://keras.io/examples/generative/gpt2_text_generation_with_keras_hub/)
 [GPT text generation from scratch with KerasHub](https://keras.io/examples/generative/text_generation_gpt/)
 [Text generation with a miniature GPT](https://keras.io/examples/generative/text_generation_with_miniature_gpt/)
 [Character-level text generation with LSTM](https://keras.io/examples/generative/lstm_character_level_text_generation/)
 [Text Generation using FNet](https://keras.io/examples/generative/text_generation_fnet/)
 [Music Generation with Transformer Models](https://keras.io/examples/generative/midi_generation_with_transformer/)
 [Drug Molecule Generation with VAE](https://keras.io/examples/generative/molecule_generation/)
 [Density estimation using Real NVP](https://keras.io/examples/generative/real_nvp/)
 [WGAN-GP with R-GCN for the generation of small molecular graphs](https://keras.io/examples/generative/wgan-graphs/)
 [Audio Data](https://keras.io/examples/audio/)
 [Reinforcement Learning](https://keras.io/examples/rl/)
 [Graph Data](https://keras.io/examples/graph/)
 [Quick Keras Recipes](https://keras.io/examples/keras_recipes/)

► [Code examples](https://keras.io/examples/)
 / [Generative Deep Learning](https://keras.io/examples/generative/)
 / Data-efficient GANs with Adaptive Discriminator Augmentation

Data-efficient GANs with Adaptive Discriminator Augmentation
============================================================

**Author:** [András Béres](https://www.linkedin.com/in/andras-beres-789190210)
  
**Date created:** 2021/10/28  
**Last modified:** 2025/01/23  
**Description:** Generating images from limited data using the Caltech Birds dataset.

ⓘ This example uses Keras 3

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/generative/ipynb/gan_ada.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/examples/generative/gan_ada.py)

* * *

Introduction
------------

### GANs

[Generative Adversarial Networks (GANs)](https://arxiv.org/abs/1406.2661)
 are a popular class of generative deep learning models, commonly used for image generation. They consist of a pair of dueling neural networks, called the discriminator and the generator. The discriminator's task is to distinguish real images from generated (fake) ones, while the generator network tries to fool the discriminator by generating more and more realistic images. If the generator is however too easy or too hard to fool, it might fail to provide useful learning signal for the generator, therefore training GANs is usually considered a difficult task.

### Data augmentation for GANS

Data augmentation, a popular technique in deep learning, is the process of randomly applying semantics-preserving transformations to the input data to generate multiple realistic versions of it, thereby effectively multiplying the amount of training data available. The simplest example is left-right flipping an image, which preserves its contents while generating a second unique training sample. Data augmentation is commonly used in supervised learning to prevent overfitting and enhance generalization.

The authors of [StyleGAN2-ADA](https://arxiv.org/abs/2006.06676)
 show that discriminator overfitting can be an issue in GANs, especially when only low amounts of training data is available. They propose Adaptive Discriminator Augmentation to mitigate this issue.

Applying data augmentation to GANs however is not straightforward. Since the generator is updated using the discriminator's gradients, if the generated images are augmented, the augmentation pipeline has to be differentiable and also has to be GPU-compatible for computational efficiency. Luckily, the [Keras image augmentation layers](https://keras.io/api/layers/preprocessing_layers/image_augmentation/)
 fulfill both these requirements, and are therefore very well suited for this task.

### Invertible data augmentation

A possible difficulty when using data augmentation in generative models is the issue of ["leaky augmentations" (section 2.2)](https://arxiv.org/abs/2006.06676)
, namely when the model generates images that are already augmented. This would mean that it was not able to separate the augmentation from the underlying data distribution, which can be caused by using non-invertible data transformations. For example, if either 0, 90, 180 or 270 degree rotations are performed with equal probability, the original orientation of the images is impossible to infer, and this information is destroyed.

A simple trick to make data augmentations invertible is to only apply them with some probability. That way the original version of the images will be more common, and the data distribution can be inferred. By properly choosing this probability, one can effectively regularize the discriminator without making the augmentations leaky.

* * *

Setup
-----

Copied!

`import os  os.environ["KERAS_BACKEND"] = "tensorflow"  import matplotlib.pyplot as plt import tensorflow as tf import tensorflow_datasets as tfds  import keras from keras import ops from keras import layers`

`WARNING: All log messages before absl::InitializeLog() is called are written to STDERR E0000 00:00:1738798965.367584   17795 cuda_dnn.cc:8310] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered E0000 00:00:1738798965.374084   17795 cuda_blas.cc:1418] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered`

* * *

Hyperparameterers
-----------------

Copied!

`# data num_epochs = 10  # train for 400 epochs for good results image_size = 64 # resolution of Kernel Inception Distance measurement, see related section kid_image_size = 75 padding = 0.25 dataset_name = "caltech_birds2011"  # adaptive discriminator augmentation max_translation = 0.125 max_rotation = 0.125 max_zoom = 0.25 target_accuracy = 0.85 integration_steps = 1000  # architecture noise_size = 64 depth = 4 width = 128 leaky_relu_slope = 0.2 dropout_rate = 0.4  # optimization batch_size = 128 learning_rate = 2e-4 beta_1 = 0.5  # not using the default value of 0.9 is important ema = 0.99`

* * *

Data pipeline
-------------

In this example, we will use the [Caltech Birds (2011)](https://www.tensorflow.org/datasets/catalog/caltech_birds2011)
 dataset for generating images of birds, which is a diverse natural dataset containing less then 6000 images for training. When working with such low amounts of data, one has to take extra care to retain as high data quality as possible. In this example, we use the provided bounding boxes of the birds to cut them out with square crops while preserving their aspect ratios when possible.

Copied!

``def round_to_int(float_value):     return ops.cast(ops.round(float_value), "int32")  def preprocess_image(data):     # unnormalize bounding box coordinates     height = ops.cast(ops.shape(data["image"])[0], "float32")     width = ops.cast(ops.shape(data["image"])[1], "float32")     bounding_box = data["bbox"] * ops.stack([height, width, height, width])      # calculate center and length of longer side, add padding     target_center_y = 0.5 * (bounding_box[0] + bounding_box[2])     target_center_x = 0.5 * (bounding_box[1] + bounding_box[3])     target_size = ops.maximum(         (1.0 + padding) * (bounding_box[2] - bounding_box[0]),         (1.0 + padding) * (bounding_box[3] - bounding_box[1]),     )      # modify crop size to fit into image     target_height = ops.min(         [target_size, 2.0 * target_center_y, 2.0 * (height - target_center_y)]     )     target_width = ops.min(         [target_size, 2.0 * target_center_x, 2.0 * (width - target_center_x)]     )      # crop image, `ops.image.crop_images` only works with non-tensor croppings     image = ops.slice(         data["image"],         start_indices=(             round_to_int(target_center_y - 0.5 * target_height),             round_to_int(target_center_x - 0.5 * target_width),             0,         ),         shape=(round_to_int(target_height), round_to_int(target_width), 3),     )      # resize and clip     image = ops.cast(image, "float32")     image = ops.image.resize(image, [image_size, image_size])      return ops.clip(image / 255.0, 0.0, 1.0)  def prepare_dataset(split):     # the validation dataset is shuffled as well, because data order matters     # for the KID calculation     return (         tfds.load(dataset_name, split=split, shuffle_files=True)         .map(preprocess_image, num_parallel_calls=tf.data.AUTOTUNE)         .cache()         .shuffle(10 * batch_size)         .batch(batch_size, drop_remainder=True)         .prefetch(buffer_size=tf.data.AUTOTUNE)     )  train_dataset = prepare_dataset("train") val_dataset = prepare_dataset("test")``

`I0000 00:00:1738798971.054632   17795 gpu_device.cc:2022] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 13840 MB memory:  -> device: 0, name: Tesla T4, pci bus id: 0000:00:04.0, compute capability: 7.5`

After preprocessing the training images look like the following: ![birds dataset](https://i.imgur.com/Ru5HgBM.png)

* * *

Kernel inception distance
-------------------------

[Kernel Inception Distance (KID)](https://arxiv.org/abs/1801.01401)
 was proposed as a replacement for the popular [Frechet Inception Distance (FID)](https://arxiv.org/abs/1706.08500)
 metric for measuring image generation quality. Both metrics measure the difference in the generated and training distributions in the representation space of an [InceptionV3](https://keras.io/api/applications/inceptionv3/)
 network pretrained on [ImageNet](https://www.tensorflow.org/datasets/catalog/imagenet2012)
.

According to the paper, KID was proposed because FID has no unbiased estimator, its expected value is higher when it is measured on fewer images. KID is more suitable for small datasets because its expected value does not depend on the number of samples it is measured on. In my experience it is also computationally lighter, numerically more stable, and simpler to implement because it can be estimated in a per-batch manner.

In this example, the images are evaluated at the minimal possible resolution of the Inception network (75x75 instead of 299x299), and the metric is only measured on the validation set for computational efficiency.

Copied!

`class KID(keras.metrics.Metric):     def __init__(self, name="kid", **kwargs):         super().__init__(name=name, **kwargs)          # KID is estimated per batch and is averaged across batches         self.kid_tracker = keras.metrics.Mean()          # a pretrained InceptionV3 is used without its classification layer         # transform the pixel values to the 0-255 range, then use the same         # preprocessing as during pretraining         self.encoder = keras.Sequential(             [                 layers.InputLayer(input_shape=(image_size, image_size, 3)),                 layers.Rescaling(255.0),                 layers.Resizing(height=kid_image_size, width=kid_image_size),                 layers.Lambda(keras.applications.inception_v3.preprocess_input),                 keras.applications.InceptionV3(                     include_top=False,                     input_shape=(kid_image_size, kid_image_size, 3),                     weights="imagenet",                 ),                 layers.GlobalAveragePooling2D(),             ],             name="inception_encoder",         )      def polynomial_kernel(self, features_1, features_2):         feature_dimensions = ops.cast(ops.shape(features_1)[1], "float32")         return (             features_1 @ ops.transpose(features_2) / feature_dimensions + 1.0         ) ** 3.0      def update_state(self, real_images, generated_images, sample_weight=None):         real_features = self.encoder(real_images, training=False)         generated_features = self.encoder(generated_images, training=False)          # compute polynomial kernels using the two sets of features         kernel_real = self.polynomial_kernel(real_features, real_features)         kernel_generated = self.polynomial_kernel(             generated_features, generated_features         )         kernel_cross = self.polynomial_kernel(real_features, generated_features)          # estimate the squared maximum mean discrepancy using the average kernel values         batch_size = ops.shape(real_features)[0]         batch_size_f = ops.cast(batch_size, "float32")         mean_kernel_real = ops.sum(kernel_real * (1.0 - ops.eye(batch_size))) / (             batch_size_f * (batch_size_f - 1.0)         )         mean_kernel_generated = ops.sum(             kernel_generated * (1.0 - ops.eye(batch_size))         ) / (batch_size_f * (batch_size_f - 1.0))         mean_kernel_cross = ops.mean(kernel_cross)         kid = mean_kernel_real + mean_kernel_generated - 2.0 * mean_kernel_cross          # update the average KID estimate         self.kid_tracker.update_state(kid)      def result(self):         return self.kid_tracker.result()      def reset_state(self):         self.kid_tracker.reset_state()`

* * *

Adaptive discriminator augmentation
-----------------------------------

The authors of [StyleGAN2-ADA](https://arxiv.org/abs/2006.06676)
 propose to change the augmentation probability adaptively during training. Though it is explained differently in the paper, they use [integral control](https://en.wikipedia.org/wiki/PID_controller#Integral)
 on the augmentation probability to keep the discriminator's accuracy on real images close to a target value. Note, that their controlled variable is actually the average sign of the discriminator logits (r\_t in the paper), which corresponds to 2 \* accuracy - 1.

This method requires two hyperparameters:

1.  `target_accuracy`: the target value for the discriminator's accuracy on real images. I recommend selecting its value from the 80-90% range.
2.  [`integration_steps`](https://en.wikipedia.org/wiki/PID_controller#Mathematical_form)
    : the number of update steps required for an accuracy error of 100% to transform into an augmentation probability increase of 100%. To give an intuition, this defines how slowly the augmentation probability is changed. I recommend setting this to a relatively high value (1000 in this case) so that the augmentation strength is only adjusted slowly.

The main motivation for this procedure is that the optimal value of the target accuracy is similar across different dataset sizes (see [figure 4 and 5 in the paper](https://arxiv.org/abs/2006.06676)
), so it does not have to be re-tuned, because the process automatically applies stronger data augmentation when it is needed.

Copied!

`# "hard sigmoid", useful for binary accuracy calculation from logits def step(values):     # negative values -> 0.0, positive values -> 1.0     return 0.5 * (1.0 + ops.sign(values))  # augments images with a probability that is dynamically updated during training class AdaptiveAugmenter(keras.Model):     def __init__(self):         super().__init__()          # stores the current probability of an image being augmented         self.probability = keras.Variable(0.0)         self.seed_generator = keras.random.SeedGenerator(42)          # the corresponding augmentation names from the paper are shown above each layer         # the authors show (see figure 4), that the blitting and geometric augmentations         # are the most helpful in the low-data regime         self.augmenter = keras.Sequential(             [                 layers.InputLayer(input_shape=(image_size, image_size, 3)),                 # blitting/x-flip:                 layers.RandomFlip("horizontal"),                 # blitting/integer translation:                 layers.RandomTranslation(                     height_factor=max_translation,                     width_factor=max_translation,                     interpolation="nearest",                 ),                 # geometric/rotation:                 layers.RandomRotation(factor=max_rotation),                 # geometric/isotropic and anisotropic scaling:                 layers.RandomZoom(                     height_factor=(-max_zoom, 0.0), width_factor=(-max_zoom, 0.0)                 ),             ],             name="adaptive_augmenter",         )      def call(self, images, training):         if training:             augmented_images = self.augmenter(images, training=training)              # during training either the original or the augmented images are selected             # based on self.probability             augmentation_values = keras.random.uniform(                 shape=(batch_size, 1, 1, 1), seed=self.seed_generator             )             augmentation_bools = ops.less(augmentation_values, self.probability)              images = ops.where(augmentation_bools, augmented_images, images)         return images      def update(self, real_logits):         current_accuracy = ops.mean(step(real_logits))          # the augmentation probability is updated based on the discriminator's         # accuracy on real images         accuracy_error = current_accuracy - target_accuracy         self.probability.assign(             ops.clip(self.probability + accuracy_error / integration_steps, 0.0, 1.0)         )`

* * *

Network architecture
--------------------

Here we specify the architecture of the two networks:

*   generator: maps a random vector to an image, which should be as realistic as possible
*   discriminator: maps an image to a scalar score, which should be high for real and low for generated images

GANs tend to be sensitive to the network architecture, I implemented a DCGAN architecture in this example, because it is relatively stable during training while being simple to implement. We use a constant number of filters throughout the network, use a sigmoid instead of tanh in the last layer of the generator, and use default initialization instead of random normal as further simplifications.

As a good practice, we disable the learnable scale parameter in the batch normalization layers, because on one hand the following relu + convolutional layers make it redundant (as noted in the [documentation](https://keras.io/api/layers/normalization_layers/batch_normalization/)
). But also because it should be disabled based on theory when using [spectral normalization (section 4.1)](https://arxiv.org/abs/1802.05957)
, which is not used here, but is common in GANs. We also disable the bias in the fully connected and convolutional layers, because the following batch normalization makes it redundant.

Copied!

`# DCGAN generator def get_generator():     noise_input = keras.Input(shape=(noise_size,))     x = layers.Dense(4 * 4 * width, use_bias=False)(noise_input)     x = layers.BatchNormalization(scale=False)(x)     x = layers.ReLU()(x)     x = layers.Reshape(target_shape=(4, 4, width))(x)     for _ in range(depth - 1):         x = layers.Conv2DTranspose(             width,             kernel_size=4,             strides=2,             padding="same",             use_bias=False,         )(x)         x = layers.BatchNormalization(scale=False)(x)         x = layers.ReLU()(x)     image_output = layers.Conv2DTranspose(         3,         kernel_size=4,         strides=2,         padding="same",         activation="sigmoid",     )(x)      return keras.Model(noise_input, image_output, name="generator")  # DCGAN discriminator def get_discriminator():     image_input = keras.Input(shape=(image_size, image_size, 3))     x = image_input     for _ in range(depth):         x = layers.Conv2D(             width,             kernel_size=4,             strides=2,             padding="same",             use_bias=False,         )(x)         x = layers.BatchNormalization(scale=False)(x)         x = layers.LeakyReLU(alpha=leaky_relu_slope)(x)     x = layers.Flatten()(x)     x = layers.Dropout(dropout_rate)(x)     output_score = layers.Dense(1)(x)      return keras.Model(image_input, output_score, name="discriminator")`

* * *

GAN model
---------

Copied!

`class GAN_ADA(keras.Model):     def __init__(self):         super().__init__()          self.seed_generator = keras.random.SeedGenerator(seed=42)         self.augmenter = AdaptiveAugmenter()         self.generator = get_generator()         self.ema_generator = keras.models.clone_model(self.generator)         self.discriminator = get_discriminator()          self.generator.summary()         self.discriminator.summary()         # we have created all layers at this point, so we can mark the model         # as having been built         self.built = True      def compile(self, generator_optimizer, discriminator_optimizer, **kwargs):         super().compile(**kwargs)          # separate optimizers for the two networks         self.generator_optimizer = generator_optimizer         self.discriminator_optimizer = discriminator_optimizer          self.generator_loss_tracker = keras.metrics.Mean(name="g_loss")         self.discriminator_loss_tracker = keras.metrics.Mean(name="d_loss")         self.real_accuracy = keras.metrics.BinaryAccuracy(name="real_acc")         self.generated_accuracy = keras.metrics.BinaryAccuracy(name="gen_acc")         self.augmentation_probability_tracker = keras.metrics.Mean(name="aug_p")         self.kid = KID()      @property     def metrics(self):         return [             self.generator_loss_tracker,             self.discriminator_loss_tracker,             self.real_accuracy,             self.generated_accuracy,             self.augmentation_probability_tracker,             self.kid,         ]      def generate(self, batch_size, training):         latent_samples = keras.random.normal(             shape=(batch_size, noise_size), seed=self.seed_generator         )         # use ema_generator during inference         if training:             generated_images = self.generator(latent_samples, training=training)         else:             generated_images = self.ema_generator(latent_samples, training=training)         return generated_images      def adversarial_loss(self, real_logits, generated_logits):         # this is usually called the non-saturating GAN loss          real_labels = ops.ones(shape=(batch_size, 1))         generated_labels = ops.zeros(shape=(batch_size, 1))          # the generator tries to produce images that the discriminator considers as real         generator_loss = keras.losses.binary_crossentropy(             real_labels, generated_logits, from_logits=True         )         # the discriminator tries to determine if images are real or generated         discriminator_loss = keras.losses.binary_crossentropy(             ops.concatenate([real_labels, generated_labels], axis=0),             ops.concatenate([real_logits, generated_logits], axis=0),             from_logits=True,         )          return ops.mean(generator_loss), ops.mean(discriminator_loss)      def train_step(self, real_images):         real_images = self.augmenter(real_images, training=True)          # use persistent gradient tape because gradients will be calculated twice         with tf.GradientTape(persistent=True) as tape:             generated_images = self.generate(batch_size, training=True)             # gradient is calculated through the image augmentation             generated_images = self.augmenter(generated_images, training=True)              # separate forward passes for the real and generated images, meaning             # that batch normalization is applied separately             real_logits = self.discriminator(real_images, training=True)             generated_logits = self.discriminator(generated_images, training=True)              generator_loss, discriminator_loss = self.adversarial_loss(                 real_logits, generated_logits             )          # calculate gradients and update weights         generator_gradients = tape.gradient(             generator_loss, self.generator.trainable_weights         )         discriminator_gradients = tape.gradient(             discriminator_loss, self.discriminator.trainable_weights         )         self.generator_optimizer.apply_gradients(             zip(generator_gradients, self.generator.trainable_weights)         )         self.discriminator_optimizer.apply_gradients(             zip(discriminator_gradients, self.discriminator.trainable_weights)         )          # update the augmentation probability based on the discriminator's performance         self.augmenter.update(real_logits)          self.generator_loss_tracker.update_state(generator_loss)         self.discriminator_loss_tracker.update_state(discriminator_loss)         self.real_accuracy.update_state(1.0, step(real_logits))         self.generated_accuracy.update_state(0.0, step(generated_logits))         self.augmentation_probability_tracker.update_state(self.augmenter.probability)          # track the exponential moving average of the generator's weights to decrease         # variance in the generation quality         for weight, ema_weight in zip(             self.generator.weights, self.ema_generator.weights         ):             ema_weight.assign(ema * ema_weight + (1 - ema) * weight)          # KID is not measured during the training phase for computational efficiency         return {m.name: m.result() for m in self.metrics[:-1]}      def test_step(self, real_images):         generated_images = self.generate(batch_size, training=False)          self.kid.update_state(real_images, generated_images)          # only KID is measured during the evaluation phase for computational efficiency         return {self.kid.name: self.kid.result()}      def plot_images(self, epoch=None, logs=None, num_rows=3, num_cols=6, interval=5):         # plot random generated images for visual evaluation of generation quality         if epoch is None or (epoch + 1) % interval == 0:             num_images = num_rows * num_cols             generated_images = self.generate(num_images, training=False)              plt.figure(figsize=(num_cols * 2.0, num_rows * 2.0))             for row in range(num_rows):                 for col in range(num_cols):                     index = row * num_cols + col                     plt.subplot(num_rows, num_cols, index + 1)                     plt.imshow(generated_images[index])                     plt.axis("off")             plt.tight_layout()             plt.show()             plt.close()`

* * *

Training
--------

One can should see from the metrics during training, that if the real accuracy (discriminator's accuracy on real images) is below the target accuracy, the augmentation probability is increased, and vice versa. In my experience, during a healthy GAN training, the discriminator accuracy should stay in the 80-95% range. Below that, the discriminator is too weak, above that it is too strong.

Note that we track the exponential moving average of the generator's weights, and use that for image generation and KID evaluation.

Copied!

`# create and compile the model model = GAN_ADA() model.compile(     generator_optimizer=keras.optimizers.Adam(learning_rate, beta_1),     discriminator_optimizer=keras.optimizers.Adam(learning_rate, beta_1), )  # save the best model based on the validation KID metric checkpoint_path = "gan_model.weights.h5" checkpoint_callback = keras.callbacks.ModelCheckpoint(     filepath=checkpoint_path,     save_weights_only=True,     monitor="val_kid",     mode="min",     save_best_only=True, )  # run training and plot generated images periodically model.fit(     train_dataset,     epochs=num_epochs,     validation_data=val_dataset,     callbacks=[         keras.callbacks.LambdaCallback(on_epoch_end=model.plot_images),         checkpoint_callback,     ], )`

``/usr/local/lib/python3.11/dist-packages/keras/src/layers/core/input_layer.py:27: UserWarning: Argument `input_shape` is deprecated. Use `shape` instead.   warnings.warn(  /usr/local/lib/python3.11/dist-packages/keras/src/layers/activations/leaky_relu.py:41: UserWarning: Argument `alpha` is deprecated. Use `negative_slope` instead.   warnings.warn(``

Model: "generator"

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Layer (type)                    ┃ Output Shape           ┃       Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ input\_layer\_1 (InputLayer)      │ (None, 64)             │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense (Dense)                   │ (None, 2048)           │       131,072 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ batch\_normalization             │ (None, 2048)           │         6,144 │
│ (BatchNormalization)            │                        │               │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ re\_lu (ReLU)                    │ (None, 2048)           │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ reshape (Reshape)               │ (None, 4, 4, 128)      │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ conv2d\_transpose                │ (None, 8, 8, 128)      │       262,144 │
│ (Conv2DTranspose)               │                        │               │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ batch\_normalization\_1           │ (None, 8, 8, 128)      │           384 │
│ (BatchNormalization)            │                        │               │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ re\_lu\_1 (ReLU)                  │ (None, 8, 8, 128)      │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ conv2d\_transpose\_1              │ (None, 16, 16, 128)    │       262,144 │
│ (Conv2DTranspose)               │                        │               │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ batch\_normalization\_2           │ (None, 16, 16, 128)    │           384 │
│ (BatchNormalization)            │                        │               │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ re\_lu\_2 (ReLU)                  │ (None, 16, 16, 128)    │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ conv2d\_transpose\_2              │ (None, 32, 32, 128)    │       262,144 │
│ (Conv2DTranspose)               │                        │               │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ batch\_normalization\_3           │ (None, 32, 32, 128)    │           384 │
│ (BatchNormalization)            │                        │               │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ re\_lu\_3 (ReLU)                  │ (None, 32, 32, 128)    │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ conv2d\_transpose\_3              │ (None, 64, 64, 3)      │         6,147 │
│ (Conv2DTranspose)               │                        │               │
└─────────────────────────────────┴────────────────────────┴───────────────┘

 Total params: 930,947 (3.55 MB)

 Trainable params: 926,083 (3.53 MB)

 Non-trainable params: 4,864 (19.00 KB)

Model: "discriminator"

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Layer (type)                    ┃ Output Shape           ┃       Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ input\_layer\_2 (InputLayer)      │ (None, 64, 64, 3)      │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ conv2d (Conv2D)                 │ (None, 32, 32, 128)    │         6,144 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ batch\_normalization\_4           │ (None, 32, 32, 128)    │           384 │
│ (BatchNormalization)            │                        │               │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ leaky\_re\_lu (LeakyReLU)         │ (None, 32, 32, 128)    │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ conv2d\_1 (Conv2D)               │ (None, 16, 16, 128)    │       262,144 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ batch\_normalization\_5           │ (None, 16, 16, 128)    │           384 │
│ (BatchNormalization)            │                        │               │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ leaky\_re\_lu\_1 (LeakyReLU)       │ (None, 16, 16, 128)    │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ conv2d\_2 (Conv2D)               │ (None, 8, 8, 128)      │       262,144 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ batch\_normalization\_6           │ (None, 8, 8, 128)      │           384 │
│ (BatchNormalization)            │                        │               │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ leaky\_re\_lu\_2 (LeakyReLU)       │ (None, 8, 8, 128)      │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ conv2d\_3 (Conv2D)               │ (None, 4, 4, 128)      │       262,144 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ batch\_normalization\_7           │ (None, 4, 4, 128)      │           384 │
│ (BatchNormalization)            │                        │               │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ leaky\_re\_lu\_3 (LeakyReLU)       │ (None, 4, 4, 128)      │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ flatten (Flatten)               │ (None, 2048)           │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dropout (Dropout)               │ (None, 2048)           │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense\_1 (Dense)                 │ (None, 1)              │         2,049 │
└─────────────────────────────────┴────────────────────────┴───────────────┘

 Total params: 796,161 (3.04 MB)

 Trainable params: 795,137 (3.03 MB)

 Non-trainable params: 1,024 (4.00 KB)

`Downloading data from https://storage.googleapis.com/tensorflow/keras-applications/inception_v3/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5`

Copied!

    `0/87910968 [37m━━━━━━━━━━━━━━━━━━━━  0s 0s/step`\
\
``\
\
4202496/87910968 \[37m━━━━━━━━━━━━━━━━━━━━ 1s 0us/step\
\
``\
\
12304384/87910968 ━━\[37m━━━━━━━━━━━━━━━━━━ 0s 0us/step\
\
``\
\
21815296/87910968 ━━━━\[37m━━━━━━━━━━━━━━━━ 0s 0us/step\
\
``\
\
34373632/87910968 ━━━━━━━\[37m━━━━━━━━━━━━━ 0s 0us/step\
\
``\
\
47669248/87910968 ━━━━━━━━━━\[37m━━━━━━━━━━ 0s 0us/step\
\
``\
\
62324736/87910968 ━━━━━━━━━━━━━━\[37m━━━━━━ 0s 0us/step\
\
``\
\
72032256/87910968 ━━━━━━━━━━━━━━━━\[37m━━━━ 0s 0us/step\
\
``\
\
82083840/87910968 ━━━━━━━━━━━━━━━━━━\[37m━━ 0s 0us/step\
\
``\
\
87910968/87910968 ━━━━━━━━━━━━━━━━━━━━ 0s 0us/step\
\
`Epoch 1/10  E0000 00:00:1738798983.901596   17795 meta_optimizer.cc:966] layout failed: INVALID_ARGUMENT: Size of values 0 does not match size of permutation 4 @ fanin shape inStatefulPartitionedCall/gradient_tape/adaptive_augmenter_3/SelectV2_1-1-TransposeNHWCToNCHW-LayoutOptimizer  WARNING: All log messages before absl::InitializeLog() is called are written to STDERR I0000 00:00:1738798987.822990   17861 cuda_solvers.cc:178] Creating GpuSolver handles for stream 0x9f45670  I0000 00:00:1738798988.976919   17862 cuda_dnn.cc:529] Loaded cuDNN version 90300`\
\
1/46 \[37m━━━━━━━━━━━━━━━━━━━━ 13:22 18s/step - aug\_p: 0.0000e+00 - d\_loss: 0.8829 - g\_loss: 0.5585 - gen\_acc: 0.2812 - real\_acc: 0.7031\
\
``\
\
2/46 \[37m━━━━━━━━━━━━━━━━━━━━ 7s 173ms/step - aug\_p: 0.0000e+00 - d\_loss: 0.7985 - g\_loss: 0.8154 - gen\_acc: 0.4258 - real\_acc: 0.6777\
\
``\
\
3/46 ━\[37m━━━━━━━━━━━━━━━━━━━ 8s 201ms/step - aug\_p: 0.0000e+00 - d\_loss: 0.7488 - g\_loss: 0.9481 - gen\_acc: 0.5052 - real\_acc: 0.6680\
\
``\
\
4/46 ━\[37m━━━━━━━━━━━━━━━━━━━ 10s 249ms/step - aug\_p: 0.0000e+00 - d\_loss: 0.7106 - g\_loss: 1.0407 - gen\_acc: 0.5586 - real\_acc: 0.6680\
\
``\
\
5/46 ━━\[37m━━━━━━━━━━━━━━━━━━ 11s 269ms/step - aug\_p: 0.0000e+00 - d\_loss: 0.6782 - g\_loss: 1.1104 - gen\_acc: 0.5991 - real\_acc: 0.6744\
\
``\
\
6/46 ━━\[37m━━━━━━━━━━━━━━━━━━ 10s 273ms/step - aug\_p: 0.0000e+00 - d\_loss: 0.6506 - g\_loss: 1.1692 - gen\_acc: 0.6301 - real\_acc: 0.6818\
\
``\
\
7/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 10s 280ms/step - aug\_p: 5.1020e-07 - d\_loss: 0.6253 - g\_loss: 1.2302 - gen\_acc: 0.6558 - real\_acc: 0.6902\
\
``\
\
8/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 10s 289ms/step - aug\_p: 1.4962e-06 - d\_loss: 0.6030 - g\_loss: 1.2838 - gen\_acc: 0.6772 - real\_acc: 0.6986\
\
``\
\
9/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 10s 297ms/step - aug\_p: 3.8570e-06 - d\_loss: 0.5829 - g\_loss: 1.3313 - gen\_acc: 0.6952 - real\_acc: 0.7074\
\
``\
\
10/46 ━━━━\[37m━━━━━━━━━━━━━━━━ 10s 299ms/step - aug\_p: 7.9244e-06 - d\_loss: 0.5644 - g\_loss: 1.3805 - gen\_acc: 0.7109 - real\_acc: 0.7162\
\
``\
\
11/46 ━━━━\[37m━━━━━━━━━━━━━━━━ 11s 314ms/step - aug\_p: 1.3531e-05 - d\_loss: 0.5473 - g\_loss: 1.4301 - gen\_acc: 0.7249 - real\_acc: 0.7245\
\
``\
\
12/46 ━━━━━\[37m━━━━━━━━━━━━━━━ 11s 333ms/step - aug\_p: 2.0444e-05 - d\_loss: 0.5318 - g\_loss: 1.4743 - gen\_acc: 0.7373 - real\_acc: 0.7322\
\
``\
\
13/46 ━━━━━\[37m━━━━━━━━━━━━━━━ 11s 352ms/step - aug\_p: 2.8561e-05 - d\_loss: 0.5174 - g\_loss: 1.5181 - gen\_acc: 0.7485 - real\_acc: 0.7394\
\
``\
\
14/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 11s 365ms/step - aug\_p: 3.7929e-05 - d\_loss: 0.5040 - g\_loss: 1.5586 - gen\_acc: 0.7587 - real\_acc: 0.7464\
\
``\
\
15/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 11s 379ms/step - aug\_p: 4.8560e-05 - d\_loss: 0.4914 - g\_loss: 1.5977 - gen\_acc: 0.7680 - real\_acc: 0.7530\
\
``\
\
16/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 11s 387ms/step - aug\_p: 6.0448e-05 - d\_loss: 0.4795 - g\_loss: 1.6355 - gen\_acc: 0.7766 - real\_acc: 0.7593\
\
``\
\
17/46 ━━━━━━━\[37m━━━━━━━━━━━━━ 11s 399ms/step - aug\_p: 7.3577e-05 - d\_loss: 0.4683 - g\_loss: 1.6715 - gen\_acc: 0.7844 - real\_acc: 0.7654\
\
``\
\
18/46 ━━━━━━━\[37m━━━━━━━━━━━━━ 11s 414ms/step - aug\_p: 8.7805e-05 - d\_loss: 0.4578 - g\_loss: 1.7063 - gen\_acc: 0.7917 - real\_acc: 0.7711\
\
``\
\
19/46 ━━━━━━━━\[37m━━━━━━━━━━━━ 11s 422ms/step - aug\_p: 1.0308e-04 - d\_loss: 0.4480 - g\_loss: 1.7386 - gen\_acc: 0.7984 - real\_acc: 0.7765\
\
``\
\
20/46 ━━━━━━━━\[37m━━━━━━━━━━━━ 11s 433ms/step - aug\_p: 1.1933e-04 - d\_loss: 0.4386 - g\_loss: 1.7736 - gen\_acc: 0.8046 - real\_acc: 0.7817\
\
``\
\
21/46 ━━━━━━━━━\[37m━━━━━━━━━━━ 11s 444ms/step - aug\_p: 1.3652e-04 - d\_loss: 0.4297 - g\_loss: 1.8065 - gen\_acc: 0.8104 - real\_acc: 0.7866\
\
``\
\
22/46 ━━━━━━━━━\[37m━━━━━━━━━━━ 10s 440ms/step - aug\_p: 1.5459e-04 - d\_loss: 0.4213 - g\_loss: 1.8383 - gen\_acc: 0.8158 - real\_acc: 0.7913\
\
``\
\
23/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 9s 434ms/step - aug\_p: 1.7347e-04 - d\_loss: 0.4132 - g\_loss: 1.8694 - gen\_acc: 0.8209 - real\_acc: 0.7958\
\
``\
\
24/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 9s 429ms/step - aug\_p: 1.9312e-04 - d\_loss: 0.4056 - g\_loss: 1.8988 - gen\_acc: 0.8257 - real\_acc: 0.8000\
\
``\
\
25/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 8s 426ms/step - aug\_p: 2.1348e-04 - d\_loss: 0.3983 - g\_loss: 1.9278 - gen\_acc: 0.8302 - real\_acc: 0.8041\
\
``\
\
26/46 ━━━━━━━━━━━\[37m━━━━━━━━━ 8s 423ms/step - aug\_p: 2.3451e-04 - d\_loss: 0.3914 - g\_loss: 1.9548 - gen\_acc: 0.8345 - real\_acc: 0.8079\
\
``\
\
27/46 ━━━━━━━━━━━\[37m━━━━━━━━━ 8s 427ms/step - aug\_p: 2.5614e-04 - d\_loss: 0.3848 - g\_loss: 1.9828 - gen\_acc: 0.8385 - real\_acc: 0.8116\
\
``\
\
28/46 ━━━━━━━━━━━━\[37m━━━━━━━━ 7s 424ms/step - aug\_p: 2.7834e-04 - d\_loss: 0.3785 - g\_loss: 2.0093 - gen\_acc: 0.8423 - real\_acc: 0.8151\
\
``\
\
29/46 ━━━━━━━━━━━━\[37m━━━━━━━━ 7s 420ms/step - aug\_p: 3.0107e-04 - d\_loss: 0.3724 - g\_loss: 2.0347 - gen\_acc: 0.8459 - real\_acc: 0.8185\
\
``\
\
30/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 6s 416ms/step - aug\_p: 3.2432e-04 - d\_loss: 0.3666 - g\_loss: 2.0599 - gen\_acc: 0.8493 - real\_acc: 0.8218\
\
``\
\
31/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 6s 413ms/step - aug\_p: 3.4806e-04 - d\_loss: 0.3610 - g\_loss: 2.0840 - gen\_acc: 0.8526 - real\_acc: 0.8249\
\
``\
\
32/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 5s 409ms/step - aug\_p: 3.7225e-04 - d\_loss: 0.3556 - g\_loss: 2.1073 - gen\_acc: 0.8556 - real\_acc: 0.8279\
\
``\
\
33/46 ━━━━━━━━━━━━━━\[37m━━━━━━ 5s 406ms/step - aug\_p: 3.9686e-04 - d\_loss: 0.3505 - g\_loss: 2.1300 - gen\_acc: 0.8586 - real\_acc: 0.8307\
\
``\
\
34/46 ━━━━━━━━━━━━━━\[37m━━━━━━ 4s 402ms/step - aug\_p: 4.2187e-04 - d\_loss: 0.3455 - g\_loss: 2.1520 - gen\_acc: 0.8614 - real\_acc: 0.8335\
\
``\
\
35/46 ━━━━━━━━━━━━━━━\[37m━━━━━ 4s 400ms/step - aug\_p: 4.4725e-04 - d\_loss: 0.3407 - g\_loss: 2.1736 - gen\_acc: 0.8641 - real\_acc: 0.8361\
\
``\
\
36/46 ━━━━━━━━━━━━━━━\[37m━━━━━ 3s 397ms/step - aug\_p: 4.7297e-04 - d\_loss: 0.3361 - g\_loss: 2.1947 - gen\_acc: 0.8667 - real\_acc: 0.8387\
\
``\
\
37/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 3s 393ms/step - aug\_p: 4.9903e-04 - d\_loss: 0.3316 - g\_loss: 2.2152 - gen\_acc: 0.8691 - real\_acc: 0.8411\
\
``\
\
38/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 3s 387ms/step - aug\_p: 5.2539e-04 - d\_loss: 0.3273 - g\_loss: 2.2357 - gen\_acc: 0.8715 - real\_acc: 0.8435\
\
``\
\
39/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 2s 382ms/step - aug\_p: 5.5206e-04 - d\_loss: 0.3231 - g\_loss: 2.2554 - gen\_acc: 0.8738 - real\_acc: 0.8458\
\
``\
\
40/46 ━━━━━━━━━━━━━━━━━\[37m━━━ 2s 376ms/step - aug\_p: 5.7902e-04 - d\_loss: 0.3191 - g\_loss: 2.2756 - gen\_acc: 0.8759 - real\_acc: 0.8480\
\
``\
\
41/46 ━━━━━━━━━━━━━━━━━\[37m━━━ 1s 371ms/step - aug\_p: 6.0626e-04 - d\_loss: 0.3151 - g\_loss: 2.2954 - gen\_acc: 0.8780 - real\_acc: 0.8502\
\
``\
\
42/46 ━━━━━━━━━━━━━━━━━━\[37m━━ 1s 366ms/step - aug\_p: 6.3377e-04 - d\_loss: 0.3113 - g\_loss: 2.3147 - gen\_acc: 0.8800 - real\_acc: 0.8522\
\
``\
\
43/46 ━━━━━━━━━━━━━━━━━━\[37m━━ 1s 362ms/step - aug\_p: 6.6154e-04 - d\_loss: 0.3076 - g\_loss: 2.3339 - gen\_acc: 0.8820 - real\_acc: 0.8543\
\
``\
\
44/46 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 358ms/step - aug\_p: 6.8956e-04 - d\_loss: 0.3041 - g\_loss: 2.3524 - gen\_acc: 0.8839 - real\_acc: 0.8562\
\
``\
\
45/46 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 354ms/step - aug\_p: 7.1780e-04 - d\_loss: 0.3006 - g\_loss: 2.3703 - gen\_acc: 0.8857 - real\_acc: 0.8581\
\
``\
\
46/46 ━━━━━━━━━━━━━━━━━━━━ 0s 350ms/step - aug\_p: 7.4625e-04 - d\_loss: 0.2973 - g\_loss: 2.3871 - gen\_acc: 0.8874 - real\_acc: 0.8599\
\
``\
\
46/46 ━━━━━━━━━━━━━━━━━━━━ 61s 958ms/step - aug\_p: 7.7349e-04 - d\_loss: 0.2942 - g\_loss: 2.4032 - gen\_acc: 0.8890 - real\_acc: 0.8616 - val\_kid: 9.1841\
\
`Epoch 2/10`\
\
1/46 \[37m━━━━━━━━━━━━━━━━━━━━ 22:28 30s/step - aug\_p: 0.0051 - d\_loss: 0.1030 - g\_loss: 8.8928 - gen\_acc: 1.0000 - real\_acc: 0.9375\
\
``\
\
2/46 \[37m━━━━━━━━━━━━━━━━━━━━ 7s 176ms/step - aug\_p: 0.0051 - d\_loss: 0.1073 - g\_loss: 8.4938 - gen\_acc: 0.9980 - real\_acc: 0.9297\
\
``\
\
3/46 ━\[37m━━━━━━━━━━━━━━━━━━━ 7s 176ms/step - aug\_p: 0.0051 - d\_loss: 0.1074 - g\_loss: 7.7540 - gen\_acc: 0.9952 - real\_acc: 0.9340\
\
``\
\
4/46 ━\[37m━━━━━━━━━━━━━━━━━━━ 7s 176ms/step - aug\_p: 0.0052 - d\_loss: 0.1037 - g\_loss: 7.2815 - gen\_acc: 0.9945 - real\_acc: 0.9388\
\
``\
\
5/46 ━━\[37m━━━━━━━━━━━━━━━━━━ 7s 175ms/step - aug\_p: 0.0052 - d\_loss: 0.0997 - g\_loss: 6.9305 - gen\_acc: 0.9943 - real\_acc: 0.9432\
\
``\
\
6/46 ━━\[37m━━━━━━━━━━━━━━━━━━ 7s 175ms/step - aug\_p: 0.0052 - d\_loss: 0.0960 - g\_loss: 6.6418 - gen\_acc: 0.9942 - real\_acc: 0.9473\
\
``\
\
7/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 6s 175ms/step - aug\_p: 0.0052 - d\_loss: 0.0933 - g\_loss: 6.4224 - gen\_acc: 0.9939 - real\_acc: 0.9503\
\
``\
\
8/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 6s 175ms/step - aug\_p: 0.0053 - d\_loss: 0.0907 - g\_loss: 6.2473 - gen\_acc: 0.9937 - real\_acc: 0.9530\
\
``\
\
9/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 6s 175ms/step - aug\_p: 0.0053 - d\_loss: 0.0885 - g\_loss: 6.0970 - gen\_acc: 0.9936 - real\_acc: 0.9552\
\
``\
\
10/46 ━━━━\[37m━━━━━━━━━━━━━━━━ 6s 175ms/step - aug\_p: 0.0053 - d\_loss: 0.0868 - g\_loss: 5.9686 - gen\_acc: 0.9936 - real\_acc: 0.9571\
\
``\
\
11/46 ━━━━\[37m━━━━━━━━━━━━━━━━ 6s 175ms/step - aug\_p: 0.0054 - d\_loss: 0.0852 - g\_loss: 5.8546 - gen\_acc: 0.9936 - real\_acc: 0.9588\
\
``\
\
12/46 ━━━━━\[37m━━━━━━━━━━━━━━━ 5s 176ms/step - aug\_p: 0.0054 - d\_loss: 0.0837 - g\_loss: 5.7615 - gen\_acc: 0.9937 - real\_acc: 0.9602\
\
``\
\
13/46 ━━━━━\[37m━━━━━━━━━━━━━━━ 5s 175ms/step - aug\_p: 0.0054 - d\_loss: 0.0825 - g\_loss: 5.6750 - gen\_acc: 0.9937 - real\_acc: 0.9614\
\
``\
\
14/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 176ms/step - aug\_p: 0.0055 - d\_loss: 0.0813 - g\_loss: 5.5972 - gen\_acc: 0.9937 - real\_acc: 0.9626\
\
``\
\
15/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 176ms/step - aug\_p: 0.0055 - d\_loss: 0.0802 - g\_loss: 5.5273 - gen\_acc: 0.9938 - real\_acc: 0.9636\
\
``\
\
16/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 176ms/step - aug\_p: 0.0055 - d\_loss: 0.0792 - g\_loss: 5.4619 - gen\_acc: 0.9939 - real\_acc: 0.9645\
\
``\
\
17/46 ━━━━━━━\[37m━━━━━━━━━━━━━ 5s 176ms/step - aug\_p: 0.0056 - d\_loss: 0.0783 - g\_loss: 5.4012 - gen\_acc: 0.9940 - real\_acc: 0.9654\
\
``\
\
18/46 ━━━━━━━\[37m━━━━━━━━━━━━━ 4s 176ms/step - aug\_p: 0.0056 - d\_loss: 0.0775 - g\_loss: 5.3477 - gen\_acc: 0.9941 - real\_acc: 0.9661\
\
``\
\
19/46 ━━━━━━━━\[37m━━━━━━━━━━━━ 4s 176ms/step - aug\_p: 0.0056 - d\_loss: 0.0768 - g\_loss: 5.2979 - gen\_acc: 0.9941 - real\_acc: 0.9667\
\
``\
\
20/46 ━━━━━━━━\[37m━━━━━━━━━━━━ 4s 176ms/step - aug\_p: 0.0057 - d\_loss: 0.0762 - g\_loss: 5.2495 - gen\_acc: 0.9941 - real\_acc: 0.9673\
\
``\
\
21/46 ━━━━━━━━━\[37m━━━━━━━━━━━ 4s 176ms/step - aug\_p: 0.0057 - d\_loss: 0.0758 - g\_loss: 5.2113 - gen\_acc: 0.9940 - real\_acc: 0.9677\
\
``\
\
22/46 ━━━━━━━━━\[37m━━━━━━━━━━━ 4s 176ms/step - aug\_p: 0.0057 - d\_loss: 0.0754 - g\_loss: 5.1753 - gen\_acc: 0.9940 - real\_acc: 0.9681\
\
``\
\
23/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 4s 176ms/step - aug\_p: 0.0058 - d\_loss: 0.0752 - g\_loss: 5.1387 - gen\_acc: 0.9940 - real\_acc: 0.9684\
\
``\
\
24/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 3s 176ms/step - aug\_p: 0.0058 - d\_loss: 0.0749 - g\_loss: 5.1112 - gen\_acc: 0.9939 - real\_acc: 0.9688\
\
``\
\
25/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 3s 176ms/step - aug\_p: 0.0058 - d\_loss: 0.0746 - g\_loss: 5.0899 - gen\_acc: 0.9939 - real\_acc: 0.9691\
\
``\
\
26/46 ━━━━━━━━━━━\[37m━━━━━━━━━ 3s 177ms/step - aug\_p: 0.0059 - d\_loss: 0.0744 - g\_loss: 5.0691 - gen\_acc: 0.9939 - real\_acc: 0.9693\
\
``\
\
27/46 ━━━━━━━━━━━\[37m━━━━━━━━━ 3s 177ms/step - aug\_p: 0.0059 - d\_loss: 0.0743 - g\_loss: 5.0465 - gen\_acc: 0.9937 - real\_acc: 0.9696\
\
``\
\
28/46 ━━━━━━━━━━━━\[37m━━━━━━━━ 3s 177ms/step - aug\_p: 0.0059 - d\_loss: 0.0742 - g\_loss: 5.0296 - gen\_acc: 0.9935 - real\_acc: 0.9698\
\
``\
\
29/46 ━━━━━━━━━━━━\[37m━━━━━━━━ 3s 177ms/step - aug\_p: 0.0060 - d\_loss: 0.0741 - g\_loss: 5.0163 - gen\_acc: 0.9934 - real\_acc: 0.9701\
\
``\
\
30/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 177ms/step - aug\_p: 0.0060 - d\_loss: 0.0740 - g\_loss: 5.0018 - gen\_acc: 0.9932 - real\_acc: 0.9703\
\
``\
\
31/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 177ms/step - aug\_p: 0.0060 - d\_loss: 0.0739 - g\_loss: 4.9862 - gen\_acc: 0.9931 - real\_acc: 0.9705\
\
``\
\
32/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 177ms/step - aug\_p: 0.0061 - d\_loss: 0.0739 - g\_loss: 4.9725 - gen\_acc: 0.9929 - real\_acc: 0.9707\
\
``\
\
33/46 ━━━━━━━━━━━━━━\[37m━━━━━━ 2s 177ms/step - aug\_p: 0.0061 - d\_loss: 0.0739 - g\_loss: 4.9583 - gen\_acc: 0.9928 - real\_acc: 0.9709\
\
``\
\
34/46 ━━━━━━━━━━━━━━\[37m━━━━━━ 2s 178ms/step - aug\_p: 0.0061 - d\_loss: 0.0739 - g\_loss: 4.9439 - gen\_acc: 0.9927 - real\_acc: 0.9711\
\
``\
\
35/46 ━━━━━━━━━━━━━━━\[37m━━━━━ 1s 178ms/step - aug\_p: 0.0062 - d\_loss: 0.0739 - g\_loss: 4.9297 - gen\_acc: 0.9926 - real\_acc: 0.9712\
\
``\
\
36/46 ━━━━━━━━━━━━━━━\[37m━━━━━ 1s 178ms/step - aug\_p: 0.0062 - d\_loss: 0.0740 - g\_loss: 4.9151 - gen\_acc: 0.9925 - real\_acc: 0.9714\
\
``\
\
37/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 178ms/step - aug\_p: 0.0062 - d\_loss: 0.0741 - g\_loss: 4.9027 - gen\_acc: 0.9924 - real\_acc: 0.9714\
\
``\
\
38/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 178ms/step - aug\_p: 0.0063 - d\_loss: 0.0743 - g\_loss: 4.8890 - gen\_acc: 0.9921 - real\_acc: 0.9715\
\
``\
\
39/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 178ms/step - aug\_p: 0.0063 - d\_loss: 0.0748 - g\_loss: 4.8802 - gen\_acc: 0.9918 - real\_acc: 0.9713\
\
``\
\
40/46 ━━━━━━━━━━━━━━━━━\[37m━━━ 1s 178ms/step - aug\_p: 0.0063 - d\_loss: 0.0752 - g\_loss: 4.8742 - gen\_acc: 0.9916 - real\_acc: 0.9712\
\
``\
\
41/46 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 178ms/step - aug\_p: 0.0064 - d\_loss: 0.0756 - g\_loss: 4.8685 - gen\_acc: 0.9914 - real\_acc: 0.9710\
\
``\
\
42/46 ━━━━━━━━━━━━━━━━━━\[37m━━ 0s 178ms/step - aug\_p: 0.0064 - d\_loss: 0.0759 - g\_loss: 4.8620 - gen\_acc: 0.9911 - real\_acc: 0.9709\
\
``\
\
43/46 ━━━━━━━━━━━━━━━━━━\[37m━━ 0s 178ms/step - aug\_p: 0.0064 - d\_loss: 0.0762 - g\_loss: 4.8555 - gen\_acc: 0.9909 - real\_acc: 0.9708\
\
``\
\
44/46 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 178ms/step - aug\_p: 0.0064 - d\_loss: 0.0765 - g\_loss: 4.8492 - gen\_acc: 0.9907 - real\_acc: 0.9707\
\
``\
\
45/46 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 178ms/step - aug\_p: 0.0065 - d\_loss: 0.0768 - g\_loss: 4.8424 - gen\_acc: 0.9905 - real\_acc: 0.9707\
\
``\
\
46/46 ━━━━━━━━━━━━━━━━━━━━ 0s 178ms/step - aug\_p: 0.0065 - d\_loss: 0.0771 - g\_loss: 4.8357 - gen\_acc: 0.9902 - real\_acc: 0.9706\
\
``\
\
46/46 ━━━━━━━━━━━━━━━━━━━━ 43s 280ms/step - aug\_p: 0.0065 - d\_loss: 0.0774 - g\_loss: 4.8293 - gen\_acc: 0.9900 - real\_acc: 0.9705 - val\_kid: 8.8293\
\
`Epoch 3/10`\
\
1/46 \[37m━━━━━━━━━━━━━━━━━━━━ 5:54 8s/step - aug\_p: 0.0105 - d\_loss: 0.0941 - g\_loss: 3.4148 - gen\_acc: 0.9766 - real\_acc: 0.9609\
\
``\
\
2/46 \[37m━━━━━━━━━━━━━━━━━━━━ 8s 196ms/step - aug\_p: 0.0105 - d\_loss: 0.0925 - g\_loss: 3.3668 - gen\_acc: 0.9805 - real\_acc: 0.9668\
\
``\
\
3/46 ━\[37m━━━━━━━━━━━━━━━━━━━ 8s 187ms/step - aug\_p: 0.0106 - d\_loss: 0.0918 - g\_loss: 3.3820 - gen\_acc: 0.9835 - real\_acc: 0.9666\
\
``\
\
4/46 ━\[37m━━━━━━━━━━━━━━━━━━━ 7s 183ms/step - aug\_p: 0.0106 - d\_loss: 0.0932 - g\_loss: 3.3732 - gen\_acc: 0.9847 - real\_acc: 0.9661\
\
``\
\
5/46 ━━\[37m━━━━━━━━━━━━━━━━━━ 7s 182ms/step - aug\_p: 0.0106 - d\_loss: 0.0941 - g\_loss: 3.3531 - gen\_acc: 0.9859 - real\_acc: 0.9670\
\
``\
\
6/46 ━━\[37m━━━━━━━━━━━━━━━━━━ 7s 181ms/step - aug\_p: 0.0107 - d\_loss: 0.0942 - g\_loss: 3.3519 - gen\_acc: 0.9869 - real\_acc: 0.9679\
\
``\
\
7/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 7s 180ms/step - aug\_p: 0.0107 - d\_loss: 0.0941 - g\_loss: 3.3467 - gen\_acc: 0.9877 - real\_acc: 0.9690\
\
``\
\
8/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 6s 179ms/step - aug\_p: 0.0107 - d\_loss: 0.0944 - g\_loss: 3.3438 - gen\_acc: 0.9882 - real\_acc: 0.9693\
\
``\
\
9/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 6s 179ms/step - aug\_p: 0.0107 - d\_loss: 0.0947 - g\_loss: 3.3384 - gen\_acc: 0.9886 - real\_acc: 0.9696\
\
``\
\
10/46 ━━━━\[37m━━━━━━━━━━━━━━━━ 6s 180ms/step - aug\_p: 0.0108 - d\_loss: 0.0948 - g\_loss: 3.3468 - gen\_acc: 0.9889 - real\_acc: 0.9694\
\
``\
\
11/46 ━━━━\[37m━━━━━━━━━━━━━━━━ 6s 180ms/step - aug\_p: 0.0108 - d\_loss: 0.0952 - g\_loss: 3.3443 - gen\_acc: 0.9888 - real\_acc: 0.9695\
\
``\
\
12/46 ━━━━━\[37m━━━━━━━━━━━━━━━ 6s 180ms/step - aug\_p: 0.0108 - d\_loss: 0.0955 - g\_loss: 3.3676 - gen\_acc: 0.9887 - real\_acc: 0.9693\
\
``\
\
13/46 ━━━━━\[37m━━━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0109 - d\_loss: 0.0954 - g\_loss: 3.3959 - gen\_acc: 0.9888 - real\_acc: 0.9693\
\
``\
\
14/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0109 - d\_loss: 0.0957 - g\_loss: 3.4125 - gen\_acc: 0.9883 - real\_acc: 0.9694\
\
``\
\
15/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0109 - d\_loss: 0.0963 - g\_loss: 3.4419 - gen\_acc: 0.9880 - real\_acc: 0.9688\
\
``\
\
16/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0110 - d\_loss: 0.0969 - g\_loss: 3.4641 - gen\_acc: 0.9876 - real\_acc: 0.9684\
\
``\
\
17/46 ━━━━━━━\[37m━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0110 - d\_loss: 0.0972 - g\_loss: 3.4867 - gen\_acc: 0.9873 - real\_acc: 0.9681\
\
``\
\
18/46 ━━━━━━━\[37m━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0110 - d\_loss: 0.0975 - g\_loss: 3.5046 - gen\_acc: 0.9869 - real\_acc: 0.9679\
\
``\
\
19/46 ━━━━━━━━\[37m━━━━━━━━━━━━ 4s 180ms/step - aug\_p: 0.0110 - d\_loss: 0.0977 - g\_loss: 3.5235 - gen\_acc: 0.9866 - real\_acc: 0.9678\
\
``\
\
20/46 ━━━━━━━━\[37m━━━━━━━━━━━━ 4s 180ms/step - aug\_p: 0.0111 - d\_loss: 0.0978 - g\_loss: 3.5387 - gen\_acc: 0.9863 - real\_acc: 0.9677\
\
``\
\
21/46 ━━━━━━━━━\[37m━━━━━━━━━━━ 4s 180ms/step - aug\_p: 0.0111 - d\_loss: 0.0980 - g\_loss: 3.5544 - gen\_acc: 0.9861 - real\_acc: 0.9676\
\
``\
\
22/46 ━━━━━━━━━\[37m━━━━━━━━━━━ 4s 179ms/step - aug\_p: 0.0111 - d\_loss: 0.0983 - g\_loss: 3.5646 - gen\_acc: 0.9857 - real\_acc: 0.9675\
\
``\
\
23/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 4s 179ms/step - aug\_p: 0.0112 - d\_loss: 0.0990 - g\_loss: 3.5834 - gen\_acc: 0.9853 - real\_acc: 0.9670\
\
``\
\
24/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 3s 179ms/step - aug\_p: 0.0112 - d\_loss: 0.0995 - g\_loss: 3.6027 - gen\_acc: 0.9850 - real\_acc: 0.9665\
\
``\
\
25/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 3s 179ms/step - aug\_p: 0.0112 - d\_loss: 0.1001 - g\_loss: 3.6171 - gen\_acc: 0.9845 - real\_acc: 0.9662\
\
``\
\
26/46 ━━━━━━━━━━━\[37m━━━━━━━━━ 3s 179ms/step - aug\_p: 0.0112 - d\_loss: 0.1006 - g\_loss: 3.6374 - gen\_acc: 0.9840 - real\_acc: 0.9659\
\
``\
\
27/46 ━━━━━━━━━━━\[37m━━━━━━━━━ 3s 179ms/step - aug\_p: 0.0113 - d\_loss: 0.1009 - g\_loss: 3.6630 - gen\_acc: 0.9836 - real\_acc: 0.9656\
\
``\
\
28/46 ━━━━━━━━━━━━\[37m━━━━━━━━ 3s 179ms/step - aug\_p: 0.0113 - d\_loss: 0.1012 - g\_loss: 3.6907 - gen\_acc: 0.9833 - real\_acc: 0.9654\
\
``\
\
29/46 ━━━━━━━━━━━━\[37m━━━━━━━━ 3s 179ms/step - aug\_p: 0.0113 - d\_loss: 0.1014 - g\_loss: 3.7165 - gen\_acc: 0.9830 - real\_acc: 0.9652\
\
``\
\
30/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 179ms/step - aug\_p: 0.0114 - d\_loss: 0.1016 - g\_loss: 3.7387 - gen\_acc: 0.9827 - real\_acc: 0.9651\
\
``\
\
31/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 179ms/step - aug\_p: 0.0114 - d\_loss: 0.1016 - g\_loss: 3.7601 - gen\_acc: 0.9824 - real\_acc: 0.9650\
\
``\
\
32/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 179ms/step - aug\_p: 0.0114 - d\_loss: 0.1017 - g\_loss: 3.7799 - gen\_acc: 0.9822 - real\_acc: 0.9649\
\
``\
\
33/46 ━━━━━━━━━━━━━━\[37m━━━━━━ 2s 179ms/step - aug\_p: 0.0114 - d\_loss: 0.1017 - g\_loss: 3.7963 - gen\_acc: 0.9820 - real\_acc: 0.9649\
\
``\
\
34/46 ━━━━━━━━━━━━━━\[37m━━━━━━ 2s 179ms/step - aug\_p: 0.0115 - d\_loss: 0.1019 - g\_loss: 3.8154 - gen\_acc: 0.9818 - real\_acc: 0.9647\
\
``\
\
35/46 ━━━━━━━━━━━━━━━\[37m━━━━━ 1s 179ms/step - aug\_p: 0.0115 - d\_loss: 0.1020 - g\_loss: 3.8348 - gen\_acc: 0.9816 - real\_acc: 0.9645\
\
``\
\
36/46 ━━━━━━━━━━━━━━━\[37m━━━━━ 1s 179ms/step - aug\_p: 0.0115 - d\_loss: 0.1022 - g\_loss: 3.8515 - gen\_acc: 0.9813 - real\_acc: 0.9644\
\
``\
\
37/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 179ms/step - aug\_p: 0.0115 - d\_loss: 0.1025 - g\_loss: 3.8702 - gen\_acc: 0.9810 - real\_acc: 0.9642\
\
``\
\
38/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 179ms/step - aug\_p: 0.0116 - d\_loss: 0.1027 - g\_loss: 3.8891 - gen\_acc: 0.9807 - real\_acc: 0.9640\
\
``\
\
39/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 179ms/step - aug\_p: 0.0116 - d\_loss: 0.1032 - g\_loss: 3.9048 - gen\_acc: 0.9803 - real\_acc: 0.9638\
\
``\
\
40/46 ━━━━━━━━━━━━━━━━━\[37m━━━ 1s 179ms/step - aug\_p: 0.0116 - d\_loss: 0.1036 - g\_loss: 3.9227 - gen\_acc: 0.9799 - real\_acc: 0.9636\
\
``\
\
41/46 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 179ms/step - aug\_p: 0.0117 - d\_loss: 0.1040 - g\_loss: 3.9415 - gen\_acc: 0.9796 - real\_acc: 0.9633\
\
``\
\
42/46 ━━━━━━━━━━━━━━━━━━\[37m━━ 0s 179ms/step - aug\_p: 0.0117 - d\_loss: 0.1044 - g\_loss: 3.9588 - gen\_acc: 0.9792 - real\_acc: 0.9631\
\
``\
\
43/46 ━━━━━━━━━━━━━━━━━━\[37m━━ 0s 179ms/step - aug\_p: 0.0117 - d\_loss: 0.1048 - g\_loss: 3.9748 - gen\_acc: 0.9789 - real\_acc: 0.9629\
\
``\
\
44/46 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 179ms/step - aug\_p: 0.0117 - d\_loss: 0.1052 - g\_loss: 3.9895 - gen\_acc: 0.9785 - real\_acc: 0.9627\
\
``\
\
45/46 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 179ms/step - aug\_p: 0.0118 - d\_loss: 0.1055 - g\_loss: 4.0041 - gen\_acc: 0.9782 - real\_acc: 0.9626\
\
``\
\
46/46 ━━━━━━━━━━━━━━━━━━━━ 0s 179ms/step - aug\_p: 0.0118 - d\_loss: 0.1058 - g\_loss: 4.0177 - gen\_acc: 0.9779 - real\_acc: 0.9624\
\
``\
\
46/46 ━━━━━━━━━━━━━━━━━━━━ 22s 315ms/step - aug\_p: 0.0118 - d\_loss: 0.1061 - g\_loss: 4.0306 - gen\_acc: 0.9776 - real\_acc: 0.9623 - val\_kid: 8.4585\
\
`Epoch 4/10`\
\
1/46 \[37m━━━━━━━━━━━━━━━━━━━━ 11s 263ms/step - aug\_p: 0.0154 - d\_loss: 0.1223 - g\_loss: 2.5203 - gen\_acc: 0.9688 - real\_acc: 1.0000\
\
``\
\
2/46 \[37m━━━━━━━━━━━━━━━━━━━━ 7s 180ms/step - aug\_p: 0.0154 - d\_loss: 0.1018 - g\_loss: 3.6445 - gen\_acc: 0.9766 - real\_acc: 0.9980\
\
``\
\
3/46 ━\[37m━━━━━━━━━━━━━━━━━━━ 7s 180ms/step - aug\_p: 0.0155 - d\_loss: 0.0925 - g\_loss: 4.2071 - gen\_acc: 0.9809 - real\_acc: 0.9926\
\
``\
\
4/46 ━\[37m━━━━━━━━━━━━━━━━━━━ 7s 180ms/step - aug\_p: 0.0155 - d\_loss: 0.0875 - g\_loss: 4.3535 - gen\_acc: 0.9827 - real\_acc: 0.9910\
\
``\
\
5/46 ━━\[37m━━━━━━━━━━━━━━━━━━ 7s 180ms/step - aug\_p: 0.0155 - d\_loss: 0.0850 - g\_loss: 4.3580 - gen\_acc: 0.9843 - real\_acc: 0.9900\
\
``\
\
6/46 ━━\[37m━━━━━━━━━━━━━━━━━━ 7s 180ms/step - aug\_p: 0.0156 - d\_loss: 0.0830 - g\_loss: 4.3789 - gen\_acc: 0.9856 - real\_acc: 0.9889\
\
``\
\
7/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 7s 180ms/step - aug\_p: 0.0156 - d\_loss: 0.0821 - g\_loss: 4.3592 - gen\_acc: 0.9864 - real\_acc: 0.9879\
\
``\
\
8/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 6s 180ms/step - aug\_p: 0.0156 - d\_loss: 0.0814 - g\_loss: 4.3377 - gen\_acc: 0.9871 - real\_acc: 0.9870\
\
``\
\
9/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 6s 180ms/step - aug\_p: 0.0156 - d\_loss: 0.0811 - g\_loss: 4.3049 - gen\_acc: 0.9876 - real\_acc: 0.9864\
\
``\
\
10/46 ━━━━\[37m━━━━━━━━━━━━━━━━ 6s 180ms/step - aug\_p: 0.0157 - d\_loss: 0.0807 - g\_loss: 4.2813 - gen\_acc: 0.9881 - real\_acc: 0.9859\
\
``\
\
11/46 ━━━━\[37m━━━━━━━━━━━━━━━━ 6s 180ms/step - aug\_p: 0.0157 - d\_loss: 0.0804 - g\_loss: 4.2560 - gen\_acc: 0.9884 - real\_acc: 0.9855\
\
``\
\
12/46 ━━━━━\[37m━━━━━━━━━━━━━━━ 6s 180ms/step - aug\_p: 0.0157 - d\_loss: 0.0804 - g\_loss: 4.2284 - gen\_acc: 0.9886 - real\_acc: 0.9851\
\
``\
\
13/46 ━━━━━\[37m━━━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0158 - d\_loss: 0.0806 - g\_loss: 4.2117 - gen\_acc: 0.9888 - real\_acc: 0.9847\
\
``\
\
14/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0158 - d\_loss: 0.0807 - g\_loss: 4.1925 - gen\_acc: 0.9887 - real\_acc: 0.9844\
\
``\
\
15/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0158 - d\_loss: 0.0807 - g\_loss: 4.1790 - gen\_acc: 0.9888 - real\_acc: 0.9841\
\
``\
\
16/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0159 - d\_loss: 0.0807 - g\_loss: 4.1631 - gen\_acc: 0.9887 - real\_acc: 0.9840\
\
``\
\
17/46 ━━━━━━━\[37m━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0159 - d\_loss: 0.0807 - g\_loss: 4.1518 - gen\_acc: 0.9887 - real\_acc: 0.9838\
\
``\
\
18/46 ━━━━━━━\[37m━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0159 - d\_loss: 0.0807 - g\_loss: 4.1398 - gen\_acc: 0.9887 - real\_acc: 0.9837\
\
``\
\
19/46 ━━━━━━━━\[37m━━━━━━━━━━━━ 4s 180ms/step - aug\_p: 0.0160 - d\_loss: 0.0809 - g\_loss: 4.1255 - gen\_acc: 0.9887 - real\_acc: 0.9837\
\
``\
\
20/46 ━━━━━━━━\[37m━━━━━━━━━━━━ 4s 180ms/step - aug\_p: 0.0160 - d\_loss: 0.0810 - g\_loss: 4.1171 - gen\_acc: 0.9887 - real\_acc: 0.9835\
\
``\
\
21/46 ━━━━━━━━━\[37m━━━━━━━━━━━ 4s 180ms/step - aug\_p: 0.0160 - d\_loss: 0.0810 - g\_loss: 4.1116 - gen\_acc: 0.9886 - real\_acc: 0.9835\
\
``\
\
22/46 ━━━━━━━━━\[37m━━━━━━━━━━━ 4s 180ms/step - aug\_p: 0.0161 - d\_loss: 0.0811 - g\_loss: 4.1037 - gen\_acc: 0.9885 - real\_acc: 0.9834\
\
``\
\
23/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 4s 180ms/step - aug\_p: 0.0161 - d\_loss: 0.0812 - g\_loss: 4.1013 - gen\_acc: 0.9885 - real\_acc: 0.9833\
\
``\
\
24/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 3s 180ms/step - aug\_p: 0.0161 - d\_loss: 0.0813 - g\_loss: 4.1000 - gen\_acc: 0.9884 - real\_acc: 0.9832\
\
``\
\
25/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 3s 180ms/step - aug\_p: 0.0162 - d\_loss: 0.0814 - g\_loss: 4.0967 - gen\_acc: 0.9883 - real\_acc: 0.9832\
\
``\
\
26/46 ━━━━━━━━━━━\[37m━━━━━━━━━ 3s 180ms/step - aug\_p: 0.0162 - d\_loss: 0.0815 - g\_loss: 4.0951 - gen\_acc: 0.9882 - real\_acc: 0.9831\
\
``\
\
27/46 ━━━━━━━━━━━\[37m━━━━━━━━━ 3s 180ms/step - aug\_p: 0.0162 - d\_loss: 0.0815 - g\_loss: 4.0930 - gen\_acc: 0.9882 - real\_acc: 0.9830\
\
``\
\
28/46 ━━━━━━━━━━━━\[37m━━━━━━━━ 3s 180ms/step - aug\_p: 0.0163 - d\_loss: 0.0817 - g\_loss: 4.0887 - gen\_acc: 0.9880 - real\_acc: 0.9830\
\
``\
\
29/46 ━━━━━━━━━━━━\[37m━━━━━━━━ 3s 180ms/step - aug\_p: 0.0163 - d\_loss: 0.0818 - g\_loss: 4.0890 - gen\_acc: 0.9879 - real\_acc: 0.9829\
\
``\
\
30/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 181ms/step - aug\_p: 0.0163 - d\_loss: 0.0819 - g\_loss: 4.0918 - gen\_acc: 0.9878 - real\_acc: 0.9828\
\
``\
\
31/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 181ms/step - aug\_p: 0.0164 - d\_loss: 0.0821 - g\_loss: 4.0923 - gen\_acc: 0.9877 - real\_acc: 0.9826\
\
``\
\
32/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 181ms/step - aug\_p: 0.0164 - d\_loss: 0.0823 - g\_loss: 4.0957 - gen\_acc: 0.9876 - real\_acc: 0.9826\
\
``\
\
33/46 ━━━━━━━━━━━━━━\[37m━━━━━━ 2s 181ms/step - aug\_p: 0.0164 - d\_loss: 0.0824 - g\_loss: 4.1014 - gen\_acc: 0.9874 - real\_acc: 0.9825\
\
``\
\
34/46 ━━━━━━━━━━━━━━\[37m━━━━━━ 2s 181ms/step - aug\_p: 0.0165 - d\_loss: 0.0824 - g\_loss: 4.1072 - gen\_acc: 0.9873 - real\_acc: 0.9824\
\
``\
\
35/46 ━━━━━━━━━━━━━━━\[37m━━━━━ 1s 180ms/step - aug\_p: 0.0165 - d\_loss: 0.0825 - g\_loss: 4.1116 - gen\_acc: 0.9872 - real\_acc: 0.9823\
\
``\
\
36/46 ━━━━━━━━━━━━━━━\[37m━━━━━ 1s 180ms/step - aug\_p: 0.0165 - d\_loss: 0.0826 - g\_loss: 4.1168 - gen\_acc: 0.9871 - real\_acc: 0.9822\
\
``\
\
37/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 181ms/step - aug\_p: 0.0166 - d\_loss: 0.0827 - g\_loss: 4.1217 - gen\_acc: 0.9870 - real\_acc: 0.9822\
\
``\
\
38/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 180ms/step - aug\_p: 0.0166 - d\_loss: 0.0827 - g\_loss: 4.1262 - gen\_acc: 0.9869 - real\_acc: 0.9821\
\
``\
\
39/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 180ms/step - aug\_p: 0.0166 - d\_loss: 0.0828 - g\_loss: 4.1298 - gen\_acc: 0.9868 - real\_acc: 0.9820\
\
``\
\
40/46 ━━━━━━━━━━━━━━━━━\[37m━━━ 1s 180ms/step - aug\_p: 0.0167 - d\_loss: 0.0828 - g\_loss: 4.1333 - gen\_acc: 0.9868 - real\_acc: 0.9820\
\
``\
\
41/46 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 181ms/step - aug\_p: 0.0167 - d\_loss: 0.0828 - g\_loss: 4.1361 - gen\_acc: 0.9867 - real\_acc: 0.9819\
\
``\
\
42/46 ━━━━━━━━━━━━━━━━━━\[37m━━ 0s 181ms/step - aug\_p: 0.0167 - d\_loss: 0.0828 - g\_loss: 4.1389 - gen\_acc: 0.9866 - real\_acc: 0.9819\
\
``\
\
43/46 ━━━━━━━━━━━━━━━━━━\[37m━━ 0s 181ms/step - aug\_p: 0.0168 - d\_loss: 0.0828 - g\_loss: 4.1408 - gen\_acc: 0.9866 - real\_acc: 0.9819\
\
``\
\
44/46 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 181ms/step - aug\_p: 0.0168 - d\_loss: 0.0828 - g\_loss: 4.1438 - gen\_acc: 0.9865 - real\_acc: 0.9818\
\
``\
\
45/46 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 181ms/step - aug\_p: 0.0168 - d\_loss: 0.0828 - g\_loss: 4.1466 - gen\_acc: 0.9865 - real\_acc: 0.9818\
\
``\
\
46/46 ━━━━━━━━━━━━━━━━━━━━ 0s 181ms/step - aug\_p: 0.0168 - d\_loss: 0.0829 - g\_loss: 4.1480 - gen\_acc: 0.9864 - real\_acc: 0.9818\
\
``\
\
46/46 ━━━━━━━━━━━━━━━━━━━━ 14s 316ms/step - aug\_p: 0.0169 - d\_loss: 0.0829 - g\_loss: 4.1493 - gen\_acc: 0.9863 - real\_acc: 0.9817 - val\_kid: 6.6764\
\
`Epoch 5/10`\
\
1/46 \[37m━━━━━━━━━━━━━━━━━━━━ 10s 237ms/step - aug\_p: 0.0212 - d\_loss: 0.3046 - g\_loss: 11.2403 - gen\_acc: 1.0000 - real\_acc: 0.7734\
\
``\
\
2/46 \[37m━━━━━━━━━━━━━━━━━━━━ 8s 197ms/step - aug\_p: 0.0212 - d\_loss: 0.2549 - g\_loss: 10.8464 - gen\_acc: 1.0000 - real\_acc: 0.8086\
\
``\
\
3/46 ━\[37m━━━━━━━━━━━━━━━━━━━ 8s 190ms/step - aug\_p: 0.0212 - d\_loss: 0.2217 - g\_loss: 10.0394 - gen\_acc: 0.9983 - real\_acc: 0.8359\
\
``\
\
4/46 ━\[37m━━━━━━━━━━━━━━━━━━━ 7s 187ms/step - aug\_p: 0.0212 - d\_loss: 0.2183 - g\_loss: 9.2019 - gen\_acc: 0.9753 - real\_acc: 0.8560\
\
``\
\
5/46 ━━\[37m━━━━━━━━━━━━━━━━━━ 7s 185ms/step - aug\_p: 0.0212 - d\_loss: 0.2125 - g\_loss: 8.8056 - gen\_acc: 0.9652 - real\_acc: 0.8676\
\
``\
\
6/46 ━━\[37m━━━━━━━━━━━━━━━━━━ 7s 185ms/step - aug\_p: 0.0213 - d\_loss: 0.2060 - g\_loss: 8.5755 - gen\_acc: 0.9606 - real\_acc: 0.8755\
\
``\
\
7/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 7s 184ms/step - aug\_p: 0.0213 - d\_loss: 0.1995 - g\_loss: 8.3695 - gen\_acc: 0.9579 - real\_acc: 0.8823\
\
``\
\
8/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 7s 184ms/step - aug\_p: 0.0213 - d\_loss: 0.1938 - g\_loss: 8.1574 - gen\_acc: 0.9561 - real\_acc: 0.8884\
\
``\
\
9/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 6s 184ms/step - aug\_p: 0.0214 - d\_loss: 0.1881 - g\_loss: 7.9590 - gen\_acc: 0.9552 - real\_acc: 0.8939\
\
``\
\
10/46 ━━━━\[37m━━━━━━━━━━━━━━━━ 6s 184ms/step - aug\_p: 0.0214 - d\_loss: 0.1827 - g\_loss: 7.7719 - gen\_acc: 0.9550 - real\_acc: 0.8989\
\
``\
\
11/46 ━━━━\[37m━━━━━━━━━━━━━━━━ 6s 183ms/step - aug\_p: 0.0214 - d\_loss: 0.1785 - g\_loss: 7.5867 - gen\_acc: 0.9546 - real\_acc: 0.9034\
\
``\
\
12/46 ━━━━━\[37m━━━━━━━━━━━━━━━ 6s 183ms/step - aug\_p: 0.0214 - d\_loss: 0.1748 - g\_loss: 7.4330 - gen\_acc: 0.9546 - real\_acc: 0.9072\
\
``\
\
13/46 ━━━━━\[37m━━━━━━━━━━━━━━━ 6s 183ms/step - aug\_p: 0.0215 - d\_loss: 0.1717 - g\_loss: 7.2895 - gen\_acc: 0.9548 - real\_acc: 0.9103\
\
``\
\
14/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 183ms/step - aug\_p: 0.0215 - d\_loss: 0.1693 - g\_loss: 7.1489 - gen\_acc: 0.9544 - real\_acc: 0.9132\
\
``\
\
15/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 182ms/step - aug\_p: 0.0215 - d\_loss: 0.1674 - g\_loss: 7.0344 - gen\_acc: 0.9543 - real\_acc: 0.9153\
\
``\
\
16/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 182ms/step - aug\_p: 0.0215 - d\_loss: 0.1654 - g\_loss: 6.9321 - gen\_acc: 0.9544 - real\_acc: 0.9173\
\
``\
\
17/46 ━━━━━━━\[37m━━━━━━━━━━━━━ 5s 182ms/step - aug\_p: 0.0216 - d\_loss: 0.1637 - g\_loss: 6.8304 - gen\_acc: 0.9541 - real\_acc: 0.9191\
\
``\
\
18/46 ━━━━━━━\[37m━━━━━━━━━━━━━ 5s 183ms/step - aug\_p: 0.0216 - d\_loss: 0.1620 - g\_loss: 6.7449 - gen\_acc: 0.9540 - real\_acc: 0.9209\
\
``\
\
19/46 ━━━━━━━━\[37m━━━━━━━━━━━━ 4s 183ms/step - aug\_p: 0.0216 - d\_loss: 0.1603 - g\_loss: 6.6702 - gen\_acc: 0.9540 - real\_acc: 0.9225\
\
``\
\
20/46 ━━━━━━━━\[37m━━━━━━━━━━━━ 4s 182ms/step - aug\_p: 0.0217 - d\_loss: 0.1587 - g\_loss: 6.5977 - gen\_acc: 0.9541 - real\_acc: 0.9240\
\
``\
\
21/46 ━━━━━━━━━\[37m━━━━━━━━━━━ 4s 182ms/step - aug\_p: 0.0217 - d\_loss: 0.1572 - g\_loss: 6.5271 - gen\_acc: 0.9542 - real\_acc: 0.9255\
\
``\
\
22/46 ━━━━━━━━━\[37m━━━━━━━━━━━ 4s 182ms/step - aug\_p: 0.0217 - d\_loss: 0.1556 - g\_loss: 6.4626 - gen\_acc: 0.9544 - real\_acc: 0.9269\
\
``\
\
23/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 4s 182ms/step - aug\_p: 0.0217 - d\_loss: 0.1540 - g\_loss: 6.4028 - gen\_acc: 0.9546 - real\_acc: 0.9282\
\
``\
\
24/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 4s 182ms/step - aug\_p: 0.0218 - d\_loss: 0.1525 - g\_loss: 6.3440 - gen\_acc: 0.9548 - real\_acc: 0.9295\
\
``\
\
25/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 3s 183ms/step - aug\_p: 0.0218 - d\_loss: 0.1510 - g\_loss: 6.2898 - gen\_acc: 0.9551 - real\_acc: 0.9307\
\
``\
\
26/46 ━━━━━━━━━━━\[37m━━━━━━━━━ 3s 183ms/step - aug\_p: 0.0218 - d\_loss: 0.1495 - g\_loss: 6.2380 - gen\_acc: 0.9554 - real\_acc: 0.9318\
\
``\
\
27/46 ━━━━━━━━━━━\[37m━━━━━━━━━ 3s 183ms/step - aug\_p: 0.0219 - d\_loss: 0.1481 - g\_loss: 6.1880 - gen\_acc: 0.9558 - real\_acc: 0.9330\
\
``\
\
28/46 ━━━━━━━━━━━━\[37m━━━━━━━━ 3s 182ms/step - aug\_p: 0.0219 - d\_loss: 0.1468 - g\_loss: 6.1413 - gen\_acc: 0.9561 - real\_acc: 0.9340\
\
``\
\
29/46 ━━━━━━━━━━━━\[37m━━━━━━━━ 3s 183ms/step - aug\_p: 0.0219 - d\_loss: 0.1454 - g\_loss: 6.0966 - gen\_acc: 0.9565 - real\_acc: 0.9350\
\
``\
\
30/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 182ms/step - aug\_p: 0.0220 - d\_loss: 0.1441 - g\_loss: 6.0534 - gen\_acc: 0.9569 - real\_acc: 0.9360\
\
``\
\
31/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 183ms/step - aug\_p: 0.0220 - d\_loss: 0.1428 - g\_loss: 6.0122 - gen\_acc: 0.9573 - real\_acc: 0.9370\
\
``\
\
32/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 182ms/step - aug\_p: 0.0220 - d\_loss: 0.1415 - g\_loss: 5.9738 - gen\_acc: 0.9577 - real\_acc: 0.9379\
\
``\
\
33/46 ━━━━━━━━━━━━━━\[37m━━━━━━ 2s 182ms/step - aug\_p: 0.0220 - d\_loss: 0.1403 - g\_loss: 5.9369 - gen\_acc: 0.9581 - real\_acc: 0.9388\
\
``\
\
34/46 ━━━━━━━━━━━━━━\[37m━━━━━━ 2s 182ms/step - aug\_p: 0.0221 - d\_loss: 0.1390 - g\_loss: 5.9020 - gen\_acc: 0.9585 - real\_acc: 0.9396\
\
``\
\
35/46 ━━━━━━━━━━━━━━━\[37m━━━━━ 2s 182ms/step - aug\_p: 0.0221 - d\_loss: 0.1378 - g\_loss: 5.8680 - gen\_acc: 0.9589 - real\_acc: 0.9404\
\
``\
\
36/46 ━━━━━━━━━━━━━━━\[37m━━━━━ 1s 182ms/step - aug\_p: 0.0221 - d\_loss: 0.1366 - g\_loss: 5.8355 - gen\_acc: 0.9592 - real\_acc: 0.9412\
\
``\
\
37/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 182ms/step - aug\_p: 0.0222 - d\_loss: 0.1355 - g\_loss: 5.8042 - gen\_acc: 0.9596 - real\_acc: 0.9420\
\
``\
\
38/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 182ms/step - aug\_p: 0.0222 - d\_loss: 0.1344 - g\_loss: 5.7737 - gen\_acc: 0.9600 - real\_acc: 0.9427\
\
``\
\
39/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 182ms/step - aug\_p: 0.0222 - d\_loss: 0.1333 - g\_loss: 5.7447 - gen\_acc: 0.9604 - real\_acc: 0.9434\
\
``\
\
40/46 ━━━━━━━━━━━━━━━━━\[37m━━━ 1s 182ms/step - aug\_p: 0.0223 - d\_loss: 0.1323 - g\_loss: 5.7161 - gen\_acc: 0.9608 - real\_acc: 0.9441\
\
``\
\
41/46 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 182ms/step - aug\_p: 0.0223 - d\_loss: 0.1313 - g\_loss: 5.6892 - gen\_acc: 0.9611 - real\_acc: 0.9447\
\
``\
\
42/46 ━━━━━━━━━━━━━━━━━━\[37m━━ 0s 182ms/step - aug\_p: 0.0223 - d\_loss: 0.1304 - g\_loss: 5.6621 - gen\_acc: 0.9615 - real\_acc: 0.9453\
\
``\
\
43/46 ━━━━━━━━━━━━━━━━━━\[37m━━ 0s 182ms/step - aug\_p: 0.0223 - d\_loss: 0.1296 - g\_loss: 5.6390 - gen\_acc: 0.9618 - real\_acc: 0.9458\
\
``\
\
44/46 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 182ms/step - aug\_p: 0.0224 - d\_loss: 0.1288 - g\_loss: 5.6185 - gen\_acc: 0.9621 - real\_acc: 0.9463\
\
``\
\
45/46 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 182ms/step - aug\_p: 0.0224 - d\_loss: 0.1280 - g\_loss: 5.5982 - gen\_acc: 0.9623 - real\_acc: 0.9468\
\
``\
\
46/46 ━━━━━━━━━━━━━━━━━━━━ 0s 182ms/step - aug\_p: 0.0224 - d\_loss: 0.1273 - g\_loss: 5.5795 - gen\_acc: 0.9626 - real\_acc: 0.9473\
\
![png](https://keras.io/img/examples/generative/gan_ada/gan_ada_18_265.png)\
\
``\
\
46/46 ━━━━━━━━━━━━━━━━━━━━ 14s 317ms/step - aug\_p: 0.0225 - d\_loss: 0.1265 - g\_loss: 5.5616 - gen\_acc: 0.9629 - real\_acc: 0.9478 - val\_kid: 4.7496\
\
`Epoch 6/10`\
\
1/46 \[37m━━━━━━━━━━━━━━━━━━━━ 10s 236ms/step - aug\_p: 0.0268 - d\_loss: 0.0745 - g\_loss: 5.1780 - gen\_acc: 0.9922 - real\_acc: 0.9688\
\
``\
\
2/46 \[37m━━━━━━━━━━━━━━━━━━━━ 8s 184ms/step - aug\_p: 0.0269 - d\_loss: 0.0774 - g\_loss: 4.5412 - gen\_acc: 0.9883 - real\_acc: 0.9766\
\
``\
\
3/46 ━\[37m━━━━━━━━━━━━━━━━━━━ 7s 183ms/step - aug\_p: 0.0269 - d\_loss: 0.0743 - g\_loss: 4.5406 - gen\_acc: 0.9887 - real\_acc: 0.9783\
\
``\
\
4/46 ━\[37m━━━━━━━━━━━━━━━━━━━ 7s 184ms/step - aug\_p: 0.0269 - d\_loss: 0.0724 - g\_loss: 4.5764 - gen\_acc: 0.9896 - real\_acc: 0.9779\
\
``\
\
5/46 ━━\[37m━━━━━━━━━━━━━━━━━━ 7s 183ms/step - aug\_p: 0.0270 - d\_loss: 0.0732 - g\_loss: 4.5209 - gen\_acc: 0.9882 - real\_acc: 0.9785\
\
``\
\
6/46 ━━\[37m━━━━━━━━━━━━━━━━━━ 7s 182ms/step - aug\_p: 0.0270 - d\_loss: 0.0738 - g\_loss: 4.5449 - gen\_acc: 0.9878 - real\_acc: 0.9782\
\
``\
\
7/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 7s 182ms/step - aug\_p: 0.0270 - d\_loss: 0.0747 - g\_loss: 4.5880 - gen\_acc: 0.9878 - real\_acc: 0.9769\
\
``\
\
8/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 6s 182ms/step - aug\_p: 0.0271 - d\_loss: 0.0766 - g\_loss: 4.5791 - gen\_acc: 0.9857 - real\_acc: 0.9763\
\
``\
\
9/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 6s 183ms/step - aug\_p: 0.0271 - d\_loss: 0.0777 - g\_loss: 4.6269 - gen\_acc: 0.9844 - real\_acc: 0.9757\
\
``\
\
10/46 ━━━━\[37m━━━━━━━━━━━━━━━━ 6s 182ms/step - aug\_p: 0.0271 - d\_loss: 0.0786 - g\_loss: 4.7075 - gen\_acc: 0.9836 - real\_acc: 0.9749\
\
``\
\
11/46 ━━━━\[37m━━━━━━━━━━━━━━━━ 6s 182ms/step - aug\_p: 0.0271 - d\_loss: 0.0792 - g\_loss: 4.7786 - gen\_acc: 0.9826 - real\_acc: 0.9745\
\
``\
\
12/46 ━━━━━\[37m━━━━━━━━━━━━━━━ 6s 182ms/step - aug\_p: 0.0272 - d\_loss: 0.0793 - g\_loss: 4.8440 - gen\_acc: 0.9820 - real\_acc: 0.9744\
\
``\
\
13/46 ━━━━━\[37m━━━━━━━━━━━━━━━ 6s 183ms/step - aug\_p: 0.0272 - d\_loss: 0.0792 - g\_loss: 4.9001 - gen\_acc: 0.9816 - real\_acc: 0.9744\
\
``\
\
14/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 182ms/step - aug\_p: 0.0272 - d\_loss: 0.0789 - g\_loss: 4.9354 - gen\_acc: 0.9814 - real\_acc: 0.9745\
\
``\
\
15/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 182ms/step - aug\_p: 0.0273 - d\_loss: 0.0785 - g\_loss: 4.9643 - gen\_acc: 0.9813 - real\_acc: 0.9747\
\
``\
\
16/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 182ms/step - aug\_p: 0.0273 - d\_loss: 0.0781 - g\_loss: 4.9864 - gen\_acc: 0.9814 - real\_acc: 0.9749\
\
``\
\
17/46 ━━━━━━━\[37m━━━━━━━━━━━━━ 5s 182ms/step - aug\_p: 0.0273 - d\_loss: 0.0778 - g\_loss: 4.9973 - gen\_acc: 0.9814 - real\_acc: 0.9751\
\
``\
\
18/46 ━━━━━━━\[37m━━━━━━━━━━━━━ 5s 182ms/step - aug\_p: 0.0274 - d\_loss: 0.0774 - g\_loss: 5.0125 - gen\_acc: 0.9815 - real\_acc: 0.9753\
\
``\
\
19/46 ━━━━━━━━\[37m━━━━━━━━━━━━ 4s 182ms/step - aug\_p: 0.0274 - d\_loss: 0.0770 - g\_loss: 5.0280 - gen\_acc: 0.9816 - real\_acc: 0.9755\
\
``\
\
20/46 ━━━━━━━━\[37m━━━━━━━━━━━━ 4s 182ms/step - aug\_p: 0.0274 - d\_loss: 0.0765 - g\_loss: 5.0398 - gen\_acc: 0.9818 - real\_acc: 0.9757\
\
``\
\
21/46 ━━━━━━━━━\[37m━━━━━━━━━━━ 4s 182ms/step - aug\_p: 0.0275 - d\_loss: 0.0760 - g\_loss: 5.0455 - gen\_acc: 0.9819 - real\_acc: 0.9759\
\
``\
\
22/46 ━━━━━━━━━\[37m━━━━━━━━━━━ 4s 182ms/step - aug\_p: 0.0275 - d\_loss: 0.0756 - g\_loss: 5.0535 - gen\_acc: 0.9820 - real\_acc: 0.9760\
\
``\
\
23/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 4s 181ms/step - aug\_p: 0.0275 - d\_loss: 0.0752 - g\_loss: 5.0590 - gen\_acc: 0.9822 - real\_acc: 0.9762\
\
``\
\
24/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 3s 181ms/step - aug\_p: 0.0276 - d\_loss: 0.0749 - g\_loss: 5.0595 - gen\_acc: 0.9823 - real\_acc: 0.9763\
\
``\
\
25/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 3s 181ms/step - aug\_p: 0.0276 - d\_loss: 0.0746 - g\_loss: 5.0650 - gen\_acc: 0.9825 - real\_acc: 0.9764\
\
``\
\
26/46 ━━━━━━━━━━━\[37m━━━━━━━━━ 3s 181ms/step - aug\_p: 0.0276 - d\_loss: 0.0743 - g\_loss: 5.0742 - gen\_acc: 0.9826 - real\_acc: 0.9765\
\
``\
\
27/46 ━━━━━━━━━━━\[37m━━━━━━━━━ 3s 181ms/step - aug\_p: 0.0277 - d\_loss: 0.0740 - g\_loss: 5.0823 - gen\_acc: 0.9828 - real\_acc: 0.9766\
\
``\
\
28/46 ━━━━━━━━━━━━\[37m━━━━━━━━ 3s 181ms/step - aug\_p: 0.0277 - d\_loss: 0.0737 - g\_loss: 5.0871 - gen\_acc: 0.9829 - real\_acc: 0.9767\
\
``\
\
29/46 ━━━━━━━━━━━━\[37m━━━━━━━━ 3s 181ms/step - aug\_p: 0.0277 - d\_loss: 0.0734 - g\_loss: 5.0913 - gen\_acc: 0.9831 - real\_acc: 0.9768\
\
``\
\
30/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 181ms/step - aug\_p: 0.0278 - d\_loss: 0.0731 - g\_loss: 5.0957 - gen\_acc: 0.9832 - real\_acc: 0.9769\
\
``\
\
31/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 181ms/step - aug\_p: 0.0278 - d\_loss: 0.0727 - g\_loss: 5.0986 - gen\_acc: 0.9834 - real\_acc: 0.9770\
\
``\
\
32/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 181ms/step - aug\_p: 0.0278 - d\_loss: 0.0725 - g\_loss: 5.0992 - gen\_acc: 0.9835 - real\_acc: 0.9771\
\
``\
\
33/46 ━━━━━━━━━━━━━━\[37m━━━━━━ 2s 181ms/step - aug\_p: 0.0278 - d\_loss: 0.0722 - g\_loss: 5.1012 - gen\_acc: 0.9836 - real\_acc: 0.9772\
\
``\
\
34/46 ━━━━━━━━━━━━━━\[37m━━━━━━ 2s 181ms/step - aug\_p: 0.0279 - d\_loss: 0.0719 - g\_loss: 5.1022 - gen\_acc: 0.9838 - real\_acc: 0.9773\
\
``\
\
35/46 ━━━━━━━━━━━━━━━\[37m━━━━━ 1s 181ms/step - aug\_p: 0.0279 - d\_loss: 0.0718 - g\_loss: 5.1007 - gen\_acc: 0.9838 - real\_acc: 0.9773\
\
``\
\
36/46 ━━━━━━━━━━━━━━━\[37m━━━━━ 1s 181ms/step - aug\_p: 0.0279 - d\_loss: 0.0717 - g\_loss: 5.1026 - gen\_acc: 0.9839 - real\_acc: 0.9773\
\
``\
\
37/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 181ms/step - aug\_p: 0.0280 - d\_loss: 0.0716 - g\_loss: 5.1070 - gen\_acc: 0.9840 - real\_acc: 0.9772\
\
``\
\
38/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 181ms/step - aug\_p: 0.0280 - d\_loss: 0.0715 - g\_loss: 5.1124 - gen\_acc: 0.9840 - real\_acc: 0.9772\
\
``\
\
39/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 181ms/step - aug\_p: 0.0280 - d\_loss: 0.0714 - g\_loss: 5.1178 - gen\_acc: 0.9841 - real\_acc: 0.9773\
\
``\
\
40/46 ━━━━━━━━━━━━━━━━━\[37m━━━ 1s 181ms/step - aug\_p: 0.0281 - d\_loss: 0.0712 - g\_loss: 5.1221 - gen\_acc: 0.9842 - real\_acc: 0.9773\
\
``\
\
41/46 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 181ms/step - aug\_p: 0.0281 - d\_loss: 0.0710 - g\_loss: 5.1258 - gen\_acc: 0.9843 - real\_acc: 0.9773\
\
``\
\
42/46 ━━━━━━━━━━━━━━━━━━\[37m━━ 0s 181ms/step - aug\_p: 0.0281 - d\_loss: 0.0708 - g\_loss: 5.1290 - gen\_acc: 0.9843 - real\_acc: 0.9773\
\
``\
\
43/46 ━━━━━━━━━━━━━━━━━━\[37m━━ 0s 181ms/step - aug\_p: 0.0282 - d\_loss: 0.0707 - g\_loss: 5.1315 - gen\_acc: 0.9844 - real\_acc: 0.9774\
\
``\
\
44/46 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 181ms/step - aug\_p: 0.0282 - d\_loss: 0.0705 - g\_loss: 5.1332 - gen\_acc: 0.9845 - real\_acc: 0.9774\
\
``\
\
45/46 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 181ms/step - aug\_p: 0.0282 - d\_loss: 0.0703 - g\_loss: 5.1347 - gen\_acc: 0.9845 - real\_acc: 0.9775\
\
``\
\
46/46 ━━━━━━━━━━━━━━━━━━━━ 0s 181ms/step - aug\_p: 0.0283 - d\_loss: 0.0701 - g\_loss: 5.1357 - gen\_acc: 0.9846 - real\_acc: 0.9775\
\
``\
\
46/46 ━━━━━━━━━━━━━━━━━━━━ 12s 267ms/step - aug\_p: 0.0283 - d\_loss: 0.0699 - g\_loss: 5.1367 - gen\_acc: 0.9846 - real\_acc: 0.9776 - val\_kid: 6.2893\
\
`Epoch 7/10`\
\
1/46 \[37m━━━━━━━━━━━━━━━━━━━━ 7s 174ms/step - aug\_p: 0.0328 - d\_loss: 0.0456 - g\_loss: 3.5202 - gen\_acc: 1.0000 - real\_acc: 1.0000\
\
``\
\
2/46 \[37m━━━━━━━━━━━━━━━━━━━━ 7s 179ms/step - aug\_p: 0.0329 - d\_loss: 0.0466 - g\_loss: 3.7961 - gen\_acc: 0.9980 - real\_acc: 0.9980\
\
``\
\
3/46 ━\[37m━━━━━━━━━━━━━━━━━━━ 7s 179ms/step - aug\_p: 0.0329 - d\_loss: 0.0471 - g\_loss: 3.9462 - gen\_acc: 0.9970 - real\_acc: 0.9961\
\
``\
\
4/46 ━\[37m━━━━━━━━━━━━━━━━━━━ 7s 179ms/step - aug\_p: 0.0329 - d\_loss: 0.0469 - g\_loss: 4.0184 - gen\_acc: 0.9967 - real\_acc: 0.9946\
\
``\
\
5/46 ━━\[37m━━━━━━━━━━━━━━━━━━ 7s 180ms/step - aug\_p: 0.0330 - d\_loss: 0.0463 - g\_loss: 4.0670 - gen\_acc: 0.9968 - real\_acc: 0.9941\
\
``\
\
6/46 ━━\[37m━━━━━━━━━━━━━━━━━━ 7s 180ms/step - aug\_p: 0.0330 - d\_loss: 0.0458 - g\_loss: 4.1012 - gen\_acc: 0.9969 - real\_acc: 0.9938\
\
``\
\
7/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 7s 180ms/step - aug\_p: 0.0330 - d\_loss: 0.0451 - g\_loss: 4.1240 - gen\_acc: 0.9970 - real\_acc: 0.9937\
\
``\
\
8/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 6s 180ms/step - aug\_p: 0.0331 - d\_loss: 0.0444 - g\_loss: 4.1347 - gen\_acc: 0.9971 - real\_acc: 0.9938\
\
``\
\
9/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 6s 180ms/step - aug\_p: 0.0331 - d\_loss: 0.0438 - g\_loss: 4.1433 - gen\_acc: 0.9971 - real\_acc: 0.9937\
\
``\
\
10/46 ━━━━\[37m━━━━━━━━━━━━━━━━ 6s 180ms/step - aug\_p: 0.0331 - d\_loss: 0.0434 - g\_loss: 4.1560 - gen\_acc: 0.9970 - real\_acc: 0.9936\
\
``\
\
11/46 ━━━━\[37m━━━━━━━━━━━━━━━━ 6s 180ms/step - aug\_p: 0.0332 - d\_loss: 0.0431 - g\_loss: 4.1654 - gen\_acc: 0.9969 - real\_acc: 0.9936\
\
``\
\
12/46 ━━━━━\[37m━━━━━━━━━━━━━━━ 6s 180ms/step - aug\_p: 0.0332 - d\_loss: 0.0429 - g\_loss: 4.1695 - gen\_acc: 0.9969 - real\_acc: 0.9935\
\
``\
\
13/46 ━━━━━\[37m━━━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0333 - d\_loss: 0.0428 - g\_loss: 4.1758 - gen\_acc: 0.9969 - real\_acc: 0.9934\
\
``\
\
14/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0333 - d\_loss: 0.0427 - g\_loss: 4.1789 - gen\_acc: 0.9969 - real\_acc: 0.9932\
\
``\
\
15/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0333 - d\_loss: 0.0426 - g\_loss: 4.1799 - gen\_acc: 0.9970 - real\_acc: 0.9929\
\
``\
\
16/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0334 - d\_loss: 0.0425 - g\_loss: 4.1823 - gen\_acc: 0.9970 - real\_acc: 0.9927\
\
``\
\
17/46 ━━━━━━━\[37m━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0334 - d\_loss: 0.0425 - g\_loss: 4.1836 - gen\_acc: 0.9970 - real\_acc: 0.9926\
\
``\
\
18/46 ━━━━━━━\[37m━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0334 - d\_loss: 0.0425 - g\_loss: 4.1854 - gen\_acc: 0.9971 - real\_acc: 0.9923\
\
``\
\
19/46 ━━━━━━━━\[37m━━━━━━━━━━━━ 4s 180ms/step - aug\_p: 0.0335 - d\_loss: 0.0426 - g\_loss: 4.1843 - gen\_acc: 0.9971 - real\_acc: 0.9921\
\
``\
\
20/46 ━━━━━━━━\[37m━━━━━━━━━━━━ 4s 180ms/step - aug\_p: 0.0335 - d\_loss: 0.0427 - g\_loss: 4.1873 - gen\_acc: 0.9971 - real\_acc: 0.9920\
\
``\
\
21/46 ━━━━━━━━━\[37m━━━━━━━━━━━ 4s 180ms/step - aug\_p: 0.0335 - d\_loss: 0.0427 - g\_loss: 4.1927 - gen\_acc: 0.9972 - real\_acc: 0.9918\
\
``\
\
22/46 ━━━━━━━━━\[37m━━━━━━━━━━━ 4s 180ms/step - aug\_p: 0.0336 - d\_loss: 0.0428 - g\_loss: 4.1952 - gen\_acc: 0.9972 - real\_acc: 0.9916\
\
``\
\
23/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 4s 180ms/step - aug\_p: 0.0336 - d\_loss: 0.0428 - g\_loss: 4.2017 - gen\_acc: 0.9972 - real\_acc: 0.9915\
\
``\
\
24/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 3s 180ms/step - aug\_p: 0.0336 - d\_loss: 0.0428 - g\_loss: 4.2106 - gen\_acc: 0.9972 - real\_acc: 0.9914\
\
``\
\
25/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 3s 180ms/step - aug\_p: 0.0337 - d\_loss: 0.0428 - g\_loss: 4.2181 - gen\_acc: 0.9972 - real\_acc: 0.9913\
\
``\
\
26/46 ━━━━━━━━━━━\[37m━━━━━━━━━ 3s 180ms/step - aug\_p: 0.0337 - d\_loss: 0.0428 - g\_loss: 4.2229 - gen\_acc: 0.9972 - real\_acc: 0.9912\
\
``\
\
27/46 ━━━━━━━━━━━\[37m━━━━━━━━━ 3s 180ms/step - aug\_p: 0.0337 - d\_loss: 0.0429 - g\_loss: 4.2318 - gen\_acc: 0.9972 - real\_acc: 0.9911\
\
``\
\
28/46 ━━━━━━━━━━━━\[37m━━━━━━━━ 3s 180ms/step - aug\_p: 0.0338 - d\_loss: 0.0429 - g\_loss: 4.2416 - gen\_acc: 0.9972 - real\_acc: 0.9910\
\
``\
\
29/46 ━━━━━━━━━━━━\[37m━━━━━━━━ 3s 180ms/step - aug\_p: 0.0338 - d\_loss: 0.0430 - g\_loss: 4.2491 - gen\_acc: 0.9971 - real\_acc: 0.9909\
\
``\
\
30/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 180ms/step - aug\_p: 0.0338 - d\_loss: 0.0430 - g\_loss: 4.2604 - gen\_acc: 0.9971 - real\_acc: 0.9908\
\
``\
\
31/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 180ms/step - aug\_p: 0.0339 - d\_loss: 0.0431 - g\_loss: 4.2736 - gen\_acc: 0.9971 - real\_acc: 0.9907\
\
``\
\
32/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 180ms/step - aug\_p: 0.0339 - d\_loss: 0.0432 - g\_loss: 4.2834 - gen\_acc: 0.9970 - real\_acc: 0.9906\
\
``\
\
33/46 ━━━━━━━━━━━━━━\[37m━━━━━━ 2s 180ms/step - aug\_p: 0.0339 - d\_loss: 0.0439 - g\_loss: 4.3010 - gen\_acc: 0.9968 - real\_acc: 0.9901\
\
``\
\
34/46 ━━━━━━━━━━━━━━\[37m━━━━━━ 2s 180ms/step - aug\_p: 0.0340 - d\_loss: 0.0444 - g\_loss: 4.3187 - gen\_acc: 0.9967 - real\_acc: 0.9897\
\
``\
\
35/46 ━━━━━━━━━━━━━━━\[37m━━━━━ 1s 180ms/step - aug\_p: 0.0340 - d\_loss: 0.0455 - g\_loss: 4.3319 - gen\_acc: 0.9961 - real\_acc: 0.9892\
\
``\
\
36/46 ━━━━━━━━━━━━━━━\[37m━━━━━ 1s 180ms/step - aug\_p: 0.0340 - d\_loss: 0.0464 - g\_loss: 4.3508 - gen\_acc: 0.9956 - real\_acc: 0.9889\
\
``\
\
37/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 180ms/step - aug\_p: 0.0341 - d\_loss: 0.0474 - g\_loss: 4.3765 - gen\_acc: 0.9951 - real\_acc: 0.9884\
\
``\
\
38/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 180ms/step - aug\_p: 0.0341 - d\_loss: 0.0483 - g\_loss: 4.4070 - gen\_acc: 0.9947 - real\_acc: 0.9880\
\
``\
\
39/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 180ms/step - aug\_p: 0.0341 - d\_loss: 0.0492 - g\_loss: 4.4400 - gen\_acc: 0.9943 - real\_acc: 0.9875\
\
``\
\
40/46 ━━━━━━━━━━━━━━━━━\[37m━━━ 1s 180ms/step - aug\_p: 0.0342 - d\_loss: 0.0499 - g\_loss: 4.4739 - gen\_acc: 0.9939 - real\_acc: 0.9872\
\
``\
\
41/46 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 180ms/step - aug\_p: 0.0342 - d\_loss: 0.0506 - g\_loss: 4.5070 - gen\_acc: 0.9935 - real\_acc: 0.9868\
\
``\
\
42/46 ━━━━━━━━━━━━━━━━━━\[37m━━ 0s 180ms/step - aug\_p: 0.0342 - d\_loss: 0.0513 - g\_loss: 4.5375 - gen\_acc: 0.9932 - real\_acc: 0.9865\
\
``\
\
43/46 ━━━━━━━━━━━━━━━━━━\[37m━━ 0s 180ms/step - aug\_p: 0.0343 - d\_loss: 0.0519 - g\_loss: 4.5646 - gen\_acc: 0.9929 - real\_acc: 0.9862\
\
``\
\
44/46 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 180ms/step - aug\_p: 0.0343 - d\_loss: 0.0525 - g\_loss: 4.5904 - gen\_acc: 0.9925 - real\_acc: 0.9859\
\
``\
\
45/46 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 180ms/step - aug\_p: 0.0343 - d\_loss: 0.0530 - g\_loss: 4.6149 - gen\_acc: 0.9923 - real\_acc: 0.9857\
\
``\
\
46/46 ━━━━━━━━━━━━━━━━━━━━ 0s 180ms/step - aug\_p: 0.0344 - d\_loss: 0.0536 - g\_loss: 4.6368 - gen\_acc: 0.9920 - real\_acc: 0.9854\
\
``\
\
46/46 ━━━━━━━━━━━━━━━━━━━━ 13s 294ms/step - aug\_p: 0.0344 - d\_loss: 0.0542 - g\_loss: 4.6579 - gen\_acc: 0.9917 - real\_acc: 0.9852 - val\_kid: 6.7378\
\
`Epoch 8/10`\
\
1/46 \[37m━━━━━━━━━━━━━━━━━━━━ 7s 167ms/step - aug\_p: 0.0384 - d\_loss: 0.1191 - g\_loss: 4.3279 - gen\_acc: 1.0000 - real\_acc: 0.9219\
\
``\
\
2/46 \[37m━━━━━━━━━━━━━━━━━━━━ 7s 179ms/step - aug\_p: 0.0384 - d\_loss: 0.1470 - g\_loss: 3.7525 - gen\_acc: 0.9590 - real\_acc: 0.9219\
\
``\
\
3/46 ━\[37m━━━━━━━━━━━━━━━━━━━ 7s 180ms/step - aug\_p: 0.0384 - d\_loss: 0.1768 - g\_loss: 4.0819 - gen\_acc: 0.9544 - real\_acc: 0.8950\
\
``\
\
4/46 ━\[37m━━━━━━━━━━━━━━━━━━━ 7s 180ms/step - aug\_p: 0.0384 - d\_loss: 0.1801 - g\_loss: 4.1693 - gen\_acc: 0.9551 - real\_acc: 0.8910\
\
``\
\
5/46 ━━\[37m━━━━━━━━━━━━━━━━━━ 7s 180ms/step - aug\_p: 0.0384 - d\_loss: 0.1829 - g\_loss: 4.1280 - gen\_acc: 0.9491 - real\_acc: 0.8934\
\
``\
\
6/46 ━━\[37m━━━━━━━━━━━━━━━━━━ 7s 180ms/step - aug\_p: 0.0384 - d\_loss: 0.1828 - g\_loss: 4.2346 - gen\_acc: 0.9471 - real\_acc: 0.8949\
\
``\
\
7/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 7s 180ms/step - aug\_p: 0.0385 - d\_loss: 0.1806 - g\_loss: 4.3823 - gen\_acc: 0.9470 - real\_acc: 0.8968\
\
``\
\
8/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 6s 180ms/step - aug\_p: 0.0385 - d\_loss: 0.1765 - g\_loss: 4.5079 - gen\_acc: 0.9478 - real\_acc: 0.8997\
\
``\
\
9/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 6s 180ms/step - aug\_p: 0.0385 - d\_loss: 0.1723 - g\_loss: 4.5814 - gen\_acc: 0.9486 - real\_acc: 0.9028\
\
``\
\
10/46 ━━━━\[37m━━━━━━━━━━━━━━━━ 6s 180ms/step - aug\_p: 0.0385 - d\_loss: 0.1679 - g\_loss: 4.6213 - gen\_acc: 0.9496 - real\_acc: 0.9061\
\
``\
\
11/46 ━━━━\[37m━━━━━━━━━━━━━━━━ 6s 180ms/step - aug\_p: 0.0385 - d\_loss: 0.1637 - g\_loss: 4.6466 - gen\_acc: 0.9507 - real\_acc: 0.9092\
\
``\
\
12/46 ━━━━━\[37m━━━━━━━━━━━━━━━ 6s 180ms/step - aug\_p: 0.0386 - d\_loss: 0.1595 - g\_loss: 4.6599 - gen\_acc: 0.9520 - real\_acc: 0.9122\
\
``\
\
13/46 ━━━━━\[37m━━━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0386 - d\_loss: 0.1561 - g\_loss: 4.6625 - gen\_acc: 0.9531 - real\_acc: 0.9148\
\
``\
\
14/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0386 - d\_loss: 0.1535 - g\_loss: 4.6513 - gen\_acc: 0.9537 - real\_acc: 0.9172\
\
``\
\
15/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0386 - d\_loss: 0.1530 - g\_loss: 4.6600 - gen\_acc: 0.9544 - real\_acc: 0.9175\
\
``\
\
16/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0387 - d\_loss: 0.1612 - g\_loss: 4.6490 - gen\_acc: 0.9512 - real\_acc: 0.9180\
\
``\
\
17/46 ━━━━━━━\[37m━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0387 - d\_loss: 0.1727 - g\_loss: 4.6715 - gen\_acc: 0.9488 - real\_acc: 0.9157\
\
``\
\
18/46 ━━━━━━━\[37m━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0387 - d\_loss: 0.1825 - g\_loss: 4.7072 - gen\_acc: 0.9469 - real\_acc: 0.9135\
\
``\
\
19/46 ━━━━━━━━\[37m━━━━━━━━━━━━ 4s 180ms/step - aug\_p: 0.0387 - d\_loss: 0.1904 - g\_loss: 4.7428 - gen\_acc: 0.9454 - real\_acc: 0.9118\
\
``\
\
20/46 ━━━━━━━━\[37m━━━━━━━━━━━━ 4s 179ms/step - aug\_p: 0.0387 - d\_loss: 0.1970 - g\_loss: 4.7693 - gen\_acc: 0.9440 - real\_acc: 0.9106\
\
``\
\
21/46 ━━━━━━━━━\[37m━━━━━━━━━━━ 4s 179ms/step - aug\_p: 0.0387 - d\_loss: 0.2029 - g\_loss: 4.7854 - gen\_acc: 0.9424 - real\_acc: 0.9098\
\
``\
\
22/46 ━━━━━━━━━\[37m━━━━━━━━━━━ 4s 180ms/step - aug\_p: 0.0387 - d\_loss: 0.2079 - g\_loss: 4.7960 - gen\_acc: 0.9409 - real\_acc: 0.9092\
\
``\
\
23/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 4s 180ms/step - aug\_p: 0.0388 - d\_loss: 0.2119 - g\_loss: 4.8033 - gen\_acc: 0.9397 - real\_acc: 0.9090\
\
``\
\
24/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 3s 179ms/step - aug\_p: 0.0388 - d\_loss: 0.2153 - g\_loss: 4.8076 - gen\_acc: 0.9387 - real\_acc: 0.9088\
\
``\
\
25/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 3s 179ms/step - aug\_p: 0.0388 - d\_loss: 0.2182 - g\_loss: 4.8077 - gen\_acc: 0.9378 - real\_acc: 0.9087\
\
``\
\
26/46 ━━━━━━━━━━━\[37m━━━━━━━━━ 3s 179ms/step - aug\_p: 0.0388 - d\_loss: 0.2207 - g\_loss: 4.8051 - gen\_acc: 0.9371 - real\_acc: 0.9087\
\
``\
\
27/46 ━━━━━━━━━━━\[37m━━━━━━━━━ 3s 179ms/step - aug\_p: 0.0388 - d\_loss: 0.2229 - g\_loss: 4.8007 - gen\_acc: 0.9365 - real\_acc: 0.9086\
\
``\
\
28/46 ━━━━━━━━━━━━\[37m━━━━━━━━ 3s 180ms/step - aug\_p: 0.0388 - d\_loss: 0.2249 - g\_loss: 4.7934 - gen\_acc: 0.9360 - real\_acc: 0.9086\
\
``\
\
29/46 ━━━━━━━━━━━━\[37m━━━━━━━━ 3s 180ms/step - aug\_p: 0.0388 - d\_loss: 0.2265 - g\_loss: 4.7860 - gen\_acc: 0.9355 - real\_acc: 0.9086\
\
``\
\
30/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 180ms/step - aug\_p: 0.0389 - d\_loss: 0.2278 - g\_loss: 4.7775 - gen\_acc: 0.9352 - real\_acc: 0.9087\
\
``\
\
31/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 180ms/step - aug\_p: 0.0389 - d\_loss: 0.2290 - g\_loss: 4.7677 - gen\_acc: 0.9349 - real\_acc: 0.9087\
\
``\
\
32/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 180ms/step - aug\_p: 0.0389 - d\_loss: 0.2299 - g\_loss: 4.7575 - gen\_acc: 0.9347 - real\_acc: 0.9089\
\
``\
\
33/46 ━━━━━━━━━━━━━━\[37m━━━━━━ 2s 180ms/step - aug\_p: 0.0389 - d\_loss: 0.2305 - g\_loss: 4.7470 - gen\_acc: 0.9346 - real\_acc: 0.9091\
\
``\
\
34/46 ━━━━━━━━━━━━━━\[37m━━━━━━ 2s 180ms/step - aug\_p: 0.0389 - d\_loss: 0.2310 - g\_loss: 4.7363 - gen\_acc: 0.9345 - real\_acc: 0.9093\
\
``\
\
35/46 ━━━━━━━━━━━━━━━\[37m━━━━━ 1s 180ms/step - aug\_p: 0.0389 - d\_loss: 0.2314 - g\_loss: 4.7249 - gen\_acc: 0.9344 - real\_acc: 0.9095\
\
``\
\
36/46 ━━━━━━━━━━━━━━━\[37m━━━━━ 1s 180ms/step - aug\_p: 0.0389 - d\_loss: 0.2317 - g\_loss: 4.7149 - gen\_acc: 0.9344 - real\_acc: 0.9098\
\
``\
\
37/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 180ms/step - aug\_p: 0.0390 - d\_loss: 0.2319 - g\_loss: 4.7045 - gen\_acc: 0.9345 - real\_acc: 0.9101\
\
``\
\
38/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 180ms/step - aug\_p: 0.0390 - d\_loss: 0.2319 - g\_loss: 4.6937 - gen\_acc: 0.9345 - real\_acc: 0.9104\
\
``\
\
39/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 179ms/step - aug\_p: 0.0390 - d\_loss: 0.2319 - g\_loss: 4.6838 - gen\_acc: 0.9346 - real\_acc: 0.9107\
\
``\
\
40/46 ━━━━━━━━━━━━━━━━━\[37m━━━ 1s 179ms/step - aug\_p: 0.0390 - d\_loss: 0.2318 - g\_loss: 4.6734 - gen\_acc: 0.9347 - real\_acc: 0.9110\
\
``\
\
41/46 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 179ms/step - aug\_p: 0.0390 - d\_loss: 0.2316 - g\_loss: 4.6636 - gen\_acc: 0.9349 - real\_acc: 0.9114\
\
``\
\
42/46 ━━━━━━━━━━━━━━━━━━\[37m━━ 0s 179ms/step - aug\_p: 0.0390 - d\_loss: 0.2313 - g\_loss: 4.6532 - gen\_acc: 0.9350 - real\_acc: 0.9117\
\
``\
\
43/46 ━━━━━━━━━━━━━━━━━━\[37m━━ 0s 180ms/step - aug\_p: 0.0391 - d\_loss: 0.2310 - g\_loss: 4.6442 - gen\_acc: 0.9352 - real\_acc: 0.9120\
\
``\
\
44/46 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 180ms/step - aug\_p: 0.0391 - d\_loss: 0.2306 - g\_loss: 4.6361 - gen\_acc: 0.9354 - real\_acc: 0.9124\
\
``\
\
45/46 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 180ms/step - aug\_p: 0.0391 - d\_loss: 0.2302 - g\_loss: 4.6279 - gen\_acc: 0.9356 - real\_acc: 0.9127\
\
``\
\
46/46 ━━━━━━━━━━━━━━━━━━━━ 0s 180ms/step - aug\_p: 0.0391 - d\_loss: 0.2297 - g\_loss: 4.6201 - gen\_acc: 0.9358 - real\_acc: 0.9131\
\
``\
\
46/46 ━━━━━━━━━━━━━━━━━━━━ 12s 266ms/step - aug\_p: 0.0391 - d\_loss: 0.2292 - g\_loss: 4.6126 - gen\_acc: 0.9361 - real\_acc: 0.9134 - val\_kid: 5.7109\
\
`Epoch 9/10`\
\
1/46 \[37m━━━━━━━━━━━━━━━━━━━━ 8s 180ms/step - aug\_p: 0.0422 - d\_loss: 0.0668 - g\_loss: 3.8939 - gen\_acc: 0.9922 - real\_acc: 0.9922\
\
``\
\
2/46 \[37m━━━━━━━━━━━━━━━━━━━━ 8s 187ms/step - aug\_p: 0.0422 - d\_loss: 0.0676 - g\_loss: 3.8295 - gen\_acc: 0.9863 - real\_acc: 0.9941\
\
``\
\
3/46 ━\[37m━━━━━━━━━━━━━━━━━━━ 7s 185ms/step - aug\_p: 0.0422 - d\_loss: 0.0659 - g\_loss: 3.8676 - gen\_acc: 0.9865 - real\_acc: 0.9944\
\
``\
\
4/46 ━\[37m━━━━━━━━━━━━━━━━━━━ 7s 183ms/step - aug\_p: 0.0423 - d\_loss: 0.0703 - g\_loss: 3.8084 - gen\_acc: 0.9831 - real\_acc: 0.9928\
\
``\
\
5/46 ━━\[37m━━━━━━━━━━━━━━━━━━ 7s 183ms/step - aug\_p: 0.0423 - d\_loss: 0.0755 - g\_loss: 3.9384 - gen\_acc: 0.9821 - real\_acc: 0.9880\
\
``\
\
6/46 ━━\[37m━━━━━━━━━━━━━━━━━━ 7s 183ms/step - aug\_p: 0.0423 - d\_loss: 0.0781 - g\_loss: 4.0291 - gen\_acc: 0.9818 - real\_acc: 0.9846\
\
``\
\
7/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 7s 182ms/step - aug\_p: 0.0424 - d\_loss: 0.0831 - g\_loss: 4.0366 - gen\_acc: 0.9779 - real\_acc: 0.9828\
\
``\
\
8/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 6s 182ms/step - aug\_p: 0.0424 - d\_loss: 0.0888 - g\_loss: 4.1585 - gen\_acc: 0.9756 - real\_acc: 0.9782\
\
``\
\
9/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 6s 182ms/step - aug\_p: 0.0424 - d\_loss: 0.0921 - g\_loss: 4.3258 - gen\_acc: 0.9744 - real\_acc: 0.9750\
\
``\
\
10/46 ━━━━\[37m━━━━━━━━━━━━━━━━ 6s 182ms/step - aug\_p: 0.0424 - d\_loss: 0.0937 - g\_loss: 4.4967 - gen\_acc: 0.9737 - real\_acc: 0.9729\
\
``\
\
11/46 ━━━━\[37m━━━━━━━━━━━━━━━━ 6s 182ms/step - aug\_p: 0.0425 - d\_loss: 0.0944 - g\_loss: 4.6444 - gen\_acc: 0.9732 - real\_acc: 0.9715\
\
``\
\
12/46 ━━━━━\[37m━━━━━━━━━━━━━━━ 6s 181ms/step - aug\_p: 0.0425 - d\_loss: 0.0945 - g\_loss: 4.7625 - gen\_acc: 0.9730 - real\_acc: 0.9706\
\
``\
\
13/46 ━━━━━\[37m━━━━━━━━━━━━━━━ 5s 181ms/step - aug\_p: 0.0425 - d\_loss: 0.0943 - g\_loss: 4.8487 - gen\_acc: 0.9728 - real\_acc: 0.9701\
\
``\
\
14/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 181ms/step - aug\_p: 0.0425 - d\_loss: 0.0940 - g\_loss: 4.9110 - gen\_acc: 0.9726 - real\_acc: 0.9698\
\
``\
\
15/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 181ms/step - aug\_p: 0.0426 - d\_loss: 0.0935 - g\_loss: 4.9645 - gen\_acc: 0.9725 - real\_acc: 0.9696\
\
``\
\
16/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 181ms/step - aug\_p: 0.0426 - d\_loss: 0.0931 - g\_loss: 5.0047 - gen\_acc: 0.9726 - real\_acc: 0.9694\
\
``\
\
17/46 ━━━━━━━\[37m━━━━━━━━━━━━━ 5s 181ms/step - aug\_p: 0.0426 - d\_loss: 0.0930 - g\_loss: 5.0287 - gen\_acc: 0.9723 - real\_acc: 0.9693\
\
``\
\
18/46 ━━━━━━━\[37m━━━━━━━━━━━━━ 5s 181ms/step - aug\_p: 0.0426 - d\_loss: 0.0941 - g\_loss: 5.0578 - gen\_acc: 0.9721 - real\_acc: 0.9679\
\
``\
\
19/46 ━━━━━━━━\[37m━━━━━━━━━━━━ 4s 181ms/step - aug\_p: 0.0427 - d\_loss: 0.0976 - g\_loss: 5.0709 - gen\_acc: 0.9702 - real\_acc: 0.9669\
\
``\
\
20/46 ━━━━━━━━\[37m━━━━━━━━━━━━ 4s 181ms/step - aug\_p: 0.0427 - d\_loss: 0.1023 - g\_loss: 5.0961 - gen\_acc: 0.9687 - real\_acc: 0.9645\
\
``\
\
21/46 ━━━━━━━━━\[37m━━━━━━━━━━━ 4s 181ms/step - aug\_p: 0.0427 - d\_loss: 0.1064 - g\_loss: 5.1232 - gen\_acc: 0.9674 - real\_acc: 0.9623\
\
``\
\
22/46 ━━━━━━━━━\[37m━━━━━━━━━━━ 4s 181ms/step - aug\_p: 0.0427 - d\_loss: 0.1101 - g\_loss: 5.1442 - gen\_acc: 0.9662 - real\_acc: 0.9603\
\
``\
\
23/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 4s 181ms/step - aug\_p: 0.0428 - d\_loss: 0.1136 - g\_loss: 5.1570 - gen\_acc: 0.9649 - real\_acc: 0.9587\
\
``\
\
24/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 3s 181ms/step - aug\_p: 0.0428 - d\_loss: 0.1166 - g\_loss: 5.1674 - gen\_acc: 0.9638 - real\_acc: 0.9573\
\
``\
\
25/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 3s 181ms/step - aug\_p: 0.0428 - d\_loss: 0.1192 - g\_loss: 5.1751 - gen\_acc: 0.9628 - real\_acc: 0.9561\
\
``\
\
26/46 ━━━━━━━━━━━\[37m━━━━━━━━━ 3s 180ms/step - aug\_p: 0.0428 - d\_loss: 0.1216 - g\_loss: 5.1786 - gen\_acc: 0.9620 - real\_acc: 0.9550\
\
``\
\
27/46 ━━━━━━━━━━━\[37m━━━━━━━━━ 3s 180ms/step - aug\_p: 0.0428 - d\_loss: 0.1238 - g\_loss: 5.1785 - gen\_acc: 0.9612 - real\_acc: 0.9539\
\
``\
\
28/46 ━━━━━━━━━━━━\[37m━━━━━━━━ 3s 180ms/step - aug\_p: 0.0429 - d\_loss: 0.1258 - g\_loss: 5.1765 - gen\_acc: 0.9605 - real\_acc: 0.9530\
\
``\
\
29/46 ━━━━━━━━━━━━\[37m━━━━━━━━ 3s 180ms/step - aug\_p: 0.0429 - d\_loss: 0.1276 - g\_loss: 5.1726 - gen\_acc: 0.9599 - real\_acc: 0.9521\
\
``\
\
30/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 180ms/step - aug\_p: 0.0429 - d\_loss: 0.1294 - g\_loss: 5.1667 - gen\_acc: 0.9595 - real\_acc: 0.9513\
\
``\
\
31/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 180ms/step - aug\_p: 0.0429 - d\_loss: 0.1309 - g\_loss: 5.1594 - gen\_acc: 0.9590 - real\_acc: 0.9506\
\
``\
\
32/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 180ms/step - aug\_p: 0.0429 - d\_loss: 0.1323 - g\_loss: 5.1512 - gen\_acc: 0.9587 - real\_acc: 0.9500\
\
``\
\
33/46 ━━━━━━━━━━━━━━\[37m━━━━━━ 2s 180ms/step - aug\_p: 0.0429 - d\_loss: 0.1335 - g\_loss: 5.1414 - gen\_acc: 0.9584 - real\_acc: 0.9494\
\
``\
\
34/46 ━━━━━━━━━━━━━━\[37m━━━━━━ 2s 180ms/step - aug\_p: 0.0430 - d\_loss: 0.1346 - g\_loss: 5.1320 - gen\_acc: 0.9582 - real\_acc: 0.9489\
\
``\
\
35/46 ━━━━━━━━━━━━━━━\[37m━━━━━ 1s 180ms/step - aug\_p: 0.0430 - d\_loss: 0.1356 - g\_loss: 5.1216 - gen\_acc: 0.9580 - real\_acc: 0.9484\
\
``\
\
36/46 ━━━━━━━━━━━━━━━\[37m━━━━━ 1s 180ms/step - aug\_p: 0.0430 - d\_loss: 0.1365 - g\_loss: 5.1109 - gen\_acc: 0.9579 - real\_acc: 0.9479\
\
``\
\
37/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 180ms/step - aug\_p: 0.0430 - d\_loss: 0.1373 - g\_loss: 5.0996 - gen\_acc: 0.9578 - real\_acc: 0.9475\
\
``\
\
38/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 180ms/step - aug\_p: 0.0430 - d\_loss: 0.1379 - g\_loss: 5.0882 - gen\_acc: 0.9577 - real\_acc: 0.9472\
\
``\
\
39/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 180ms/step - aug\_p: 0.0431 - d\_loss: 0.1385 - g\_loss: 5.0769 - gen\_acc: 0.9577 - real\_acc: 0.9468\
\
``\
\
40/46 ━━━━━━━━━━━━━━━━━\[37m━━━ 1s 180ms/step - aug\_p: 0.0431 - d\_loss: 0.1391 - g\_loss: 5.0648 - gen\_acc: 0.9577 - real\_acc: 0.9466\
\
``\
\
41/46 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 180ms/step - aug\_p: 0.0431 - d\_loss: 0.1395 - g\_loss: 5.0535 - gen\_acc: 0.9577 - real\_acc: 0.9463\
\
``\
\
42/46 ━━━━━━━━━━━━━━━━━━\[37m━━ 0s 180ms/step - aug\_p: 0.0431 - d\_loss: 0.1400 - g\_loss: 5.0419 - gen\_acc: 0.9576 - real\_acc: 0.9461\
\
``\
\
43/46 ━━━━━━━━━━━━━━━━━━\[37m━━ 0s 180ms/step - aug\_p: 0.0431 - d\_loss: 0.1403 - g\_loss: 5.0307 - gen\_acc: 0.9577 - real\_acc: 0.9459\
\
``\
\
44/46 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 180ms/step - aug\_p: 0.0431 - d\_loss: 0.1406 - g\_loss: 5.0198 - gen\_acc: 0.9577 - real\_acc: 0.9458\
\
``\
\
45/46 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 180ms/step - aug\_p: 0.0432 - d\_loss: 0.1408 - g\_loss: 5.0087 - gen\_acc: 0.9577 - real\_acc: 0.9456\
\
``\
\
46/46 ━━━━━━━━━━━━━━━━━━━━ 0s 180ms/step - aug\_p: 0.0432 - d\_loss: 0.1410 - g\_loss: 4.9981 - gen\_acc: 0.9578 - real\_acc: 0.9455\
\
``\
\
46/46 ━━━━━━━━━━━━━━━━━━━━ 14s 300ms/step - aug\_p: 0.0432 - d\_loss: 0.1411 - g\_loss: 4.9879 - gen\_acc: 0.9579 - real\_acc: 0.9455 - val\_kid: 3.6018\
\
`Epoch 10/10`\
\
1/46 \[37m━━━━━━━━━━━━━━━━━━━━ 5:15 7s/step - aug\_p: 0.0464 - d\_loss: 0.0324 - g\_loss: 4.1750 - gen\_acc: 1.0000 - real\_acc: 0.9922\
\
``\
\
2/46 \[37m━━━━━━━━━━━━━━━━━━━━ 8s 195ms/step - aug\_p: 0.0464 - d\_loss: 0.0337 - g\_loss: 4.0349 - gen\_acc: 0.9980 - real\_acc: 0.9941\
\
``\
\
3/46 ━\[37m━━━━━━━━━━━━━━━━━━━ 8s 186ms/step - aug\_p: 0.0464 - d\_loss: 0.0367 - g\_loss: 4.0199 - gen\_acc: 0.9978 - real\_acc: 0.9918\
\
``\
\
4/46 ━\[37m━━━━━━━━━━━━━━━━━━━ 7s 184ms/step - aug\_p: 0.0465 - d\_loss: 0.0374 - g\_loss: 4.0297 - gen\_acc: 0.9979 - real\_acc: 0.9909\
\
``\
\
5/46 ━━\[37m━━━━━━━━━━━━━━━━━━ 7s 183ms/step - aug\_p: 0.0465 - d\_loss: 0.0380 - g\_loss: 4.0271 - gen\_acc: 0.9980 - real\_acc: 0.9902\
\
``\
\
6/46 ━━\[37m━━━━━━━━━━━━━━━━━━ 7s 183ms/step - aug\_p: 0.0465 - d\_loss: 0.0383 - g\_loss: 4.0130 - gen\_acc: 0.9981 - real\_acc: 0.9901\
\
``\
\
7/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 7s 183ms/step - aug\_p: 0.0466 - d\_loss: 0.0385 - g\_loss: 4.0148 - gen\_acc: 0.9982 - real\_acc: 0.9901\
\
``\
\
8/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 6s 182ms/step - aug\_p: 0.0466 - d\_loss: 0.0389 - g\_loss: 4.0141 - gen\_acc: 0.9983 - real\_acc: 0.9902\
\
``\
\
9/46 ━━━\[37m━━━━━━━━━━━━━━━━━ 6s 182ms/step - aug\_p: 0.0467 - d\_loss: 0.0393 - g\_loss: 4.0076 - gen\_acc: 0.9984 - real\_acc: 0.9903\
\
``\
\
10/46 ━━━━\[37m━━━━━━━━━━━━━━━━ 6s 182ms/step - aug\_p: 0.0467 - d\_loss: 0.0397 - g\_loss: 4.0031 - gen\_acc: 0.9985 - real\_acc: 0.9903\
\
``\
\
11/46 ━━━━\[37m━━━━━━━━━━━━━━━━ 6s 182ms/step - aug\_p: 0.0467 - d\_loss: 0.0402 - g\_loss: 3.9981 - gen\_acc: 0.9985 - real\_acc: 0.9902\
\
``\
\
12/46 ━━━━━\[37m━━━━━━━━━━━━━━━ 6s 182ms/step - aug\_p: 0.0468 - d\_loss: 0.0406 - g\_loss: 3.9968 - gen\_acc: 0.9985 - real\_acc: 0.9902\
\
``\
\
13/46 ━━━━━\[37m━━━━━━━━━━━━━━━ 5s 181ms/step - aug\_p: 0.0468 - d\_loss: 0.0411 - g\_loss: 3.9967 - gen\_acc: 0.9985 - real\_acc: 0.9899\
\
``\
\
14/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 181ms/step - aug\_p: 0.0468 - d\_loss: 0.0418 - g\_loss: 3.9930 - gen\_acc: 0.9984 - real\_acc: 0.9897\
\
``\
\
15/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 181ms/step - aug\_p: 0.0469 - d\_loss: 0.0428 - g\_loss: 3.9956 - gen\_acc: 0.9982 - real\_acc: 0.9893\
\
``\
\
16/46 ━━━━━━\[37m━━━━━━━━━━━━━━ 5s 181ms/step - aug\_p: 0.0469 - d\_loss: 0.0436 - g\_loss: 3.9957 - gen\_acc: 0.9980 - real\_acc: 0.9890\
\
``\
\
17/46 ━━━━━━━\[37m━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0469 - d\_loss: 0.0443 - g\_loss: 3.9983 - gen\_acc: 0.9978 - real\_acc: 0.9887\
\
``\
\
18/46 ━━━━━━━\[37m━━━━━━━━━━━━━ 5s 180ms/step - aug\_p: 0.0470 - d\_loss: 0.0450 - g\_loss: 3.9978 - gen\_acc: 0.9977 - real\_acc: 0.9885\
\
``\
\
19/46 ━━━━━━━━\[37m━━━━━━━━━━━━ 4s 180ms/step - aug\_p: 0.0470 - d\_loss: 0.0457 - g\_loss: 3.9987 - gen\_acc: 0.9976 - real\_acc: 0.9883\
\
``\
\
20/46 ━━━━━━━━\[37m━━━━━━━━━━━━ 4s 180ms/step - aug\_p: 0.0470 - d\_loss: 0.0464 - g\_loss: 3.9966 - gen\_acc: 0.9974 - real\_acc: 0.9880\
\
``\
\
21/46 ━━━━━━━━━\[37m━━━━━━━━━━━ 4s 180ms/step - aug\_p: 0.0471 - d\_loss: 0.0472 - g\_loss: 3.9956 - gen\_acc: 0.9973 - real\_acc: 0.9877\
\
``\
\
22/46 ━━━━━━━━━\[37m━━━━━━━━━━━ 4s 180ms/step - aug\_p: 0.0471 - d\_loss: 0.0482 - g\_loss: 3.9910 - gen\_acc: 0.9969 - real\_acc: 0.9874\
\
``\
\
23/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 4s 180ms/step - aug\_p: 0.0471 - d\_loss: 0.0501 - g\_loss: 3.9936 - gen\_acc: 0.9965 - real\_acc: 0.9862\
\
``\
\
24/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 3s 180ms/step - aug\_p: 0.0472 - d\_loss: 0.0532 - g\_loss: 3.9900 - gen\_acc: 0.9949 - real\_acc: 0.9853\
\
``\
\
25/46 ━━━━━━━━━━\[37m━━━━━━━━━━ 3s 180ms/step - aug\_p: 0.0472 - d\_loss: 0.0576 - g\_loss: 3.9964 - gen\_acc: 0.9935 - real\_acc: 0.9832\
\
``\
\
26/46 ━━━━━━━━━━━\[37m━━━━━━━━━ 3s 180ms/step - aug\_p: 0.0472 - d\_loss: 0.0624 - g\_loss: 3.9986 - gen\_acc: 0.9917 - real\_acc: 0.9813\
\
``\
\
27/46 ━━━━━━━━━━━\[37m━━━━━━━━━ 3s 181ms/step - aug\_p: 0.0472 - d\_loss: 0.0667 - g\_loss: 4.0030 - gen\_acc: 0.9901 - real\_acc: 0.9795\
\
``\
\
28/46 ━━━━━━━━━━━━\[37m━━━━━━━━ 3s 181ms/step - aug\_p: 0.0473 - d\_loss: 0.0707 - g\_loss: 4.0083 - gen\_acc: 0.9887 - real\_acc: 0.9778\
\
``\
\
29/46 ━━━━━━━━━━━━\[37m━━━━━━━━ 3s 181ms/step - aug\_p: 0.0473 - d\_loss: 0.0744 - g\_loss: 4.0128 - gen\_acc: 0.9873 - real\_acc: 0.9762\
\
``\
\
30/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 181ms/step - aug\_p: 0.0473 - d\_loss: 0.0776 - g\_loss: 4.0161 - gen\_acc: 0.9862 - real\_acc: 0.9748\
\
``\
\
31/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 181ms/step - aug\_p: 0.0473 - d\_loss: 0.0806 - g\_loss: 4.0186 - gen\_acc: 0.9851 - real\_acc: 0.9735\
\
``\
\
32/46 ━━━━━━━━━━━━━\[37m━━━━━━━ 2s 181ms/step - aug\_p: 0.0474 - d\_loss: 0.0832 - g\_loss: 4.0199 - gen\_acc: 0.9841 - real\_acc: 0.9724\
\
``\
\
33/46 ━━━━━━━━━━━━━━\[37m━━━━━━ 2s 182ms/step - aug\_p: 0.0474 - d\_loss: 0.0856 - g\_loss: 4.0204 - gen\_acc: 0.9832 - real\_acc: 0.9714\
\
``\
\
34/46 ━━━━━━━━━━━━━━\[37m━━━━━━ 2s 182ms/step - aug\_p: 0.0474 - d\_loss: 0.0878 - g\_loss: 4.0206 - gen\_acc: 0.9825 - real\_acc: 0.9705\
\
``\
\
35/46 ━━━━━━━━━━━━━━━\[37m━━━━━ 1s 182ms/step - aug\_p: 0.0474 - d\_loss: 0.0898 - g\_loss: 4.0206 - gen\_acc: 0.9818 - real\_acc: 0.9697\
\
``\
\
36/46 ━━━━━━━━━━━━━━━\[37m━━━━━ 1s 182ms/step - aug\_p: 0.0475 - d\_loss: 0.0916 - g\_loss: 4.0200 - gen\_acc: 0.9811 - real\_acc: 0.9690\
\
``\
\
37/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 182ms/step - aug\_p: 0.0475 - d\_loss: 0.0933 - g\_loss: 4.0193 - gen\_acc: 0.9805 - real\_acc: 0.9683\
\
``\
\
38/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 182ms/step - aug\_p: 0.0475 - d\_loss: 0.0948 - g\_loss: 4.0185 - gen\_acc: 0.9800 - real\_acc: 0.9677\
\
``\
\
39/46 ━━━━━━━━━━━━━━━━\[37m━━━━ 1s 182ms/step - aug\_p: 0.0475 - d\_loss: 0.0961 - g\_loss: 4.0171 - gen\_acc: 0.9796 - real\_acc: 0.9672\
\
``\
\
40/46 ━━━━━━━━━━━━━━━━━\[37m━━━ 1s 182ms/step - aug\_p: 0.0475 - d\_loss: 0.0974 - g\_loss: 4.0158 - gen\_acc: 0.9791 - real\_acc: 0.9667\
\
``\
\
41/46 ━━━━━━━━━━━━━━━━━\[37m━━━ 0s 182ms/step - aug\_p: 0.0476 - d\_loss: 0.0985 - g\_loss: 4.0146 - gen\_acc: 0.9787 - real\_acc: 0.9662\
\
``\
\
42/46 ━━━━━━━━━━━━━━━━━━\[37m━━ 0s 182ms/step - aug\_p: 0.0476 - d\_loss: 0.0995 - g\_loss: 4.0133 - gen\_acc: 0.9784 - real\_acc: 0.9658\
\
``\
\
43/46 ━━━━━━━━━━━━━━━━━━\[37m━━ 0s 182ms/step - aug\_p: 0.0476 - d\_loss: 0.1005 - g\_loss: 4.0119 - gen\_acc: 0.9781 - real\_acc: 0.9655\
\
``\
\
44/46 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 182ms/step - aug\_p: 0.0476 - d\_loss: 0.1013 - g\_loss: 4.0102 - gen\_acc: 0.9778 - real\_acc: 0.9652\
\
``\
\
45/46 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 182ms/step - aug\_p: 0.0476 - d\_loss: 0.1021 - g\_loss: 4.0083 - gen\_acc: 0.9775 - real\_acc: 0.9649\
\
``\
\
46/46 ━━━━━━━━━━━━━━━━━━━━ 0s 182ms/step - aug\_p: 0.0477 - d\_loss: 0.1028 - g\_loss: 4.0070 - gen\_acc: 0.9773 - real\_acc: 0.9647\
\
![png](https://keras.io/img/examples/generative/gan_ada/gan_ada_18_506.png)\
\
``\
\
46/46 ━━━━━━━━━━━━━━━━━━━━ 21s 304ms/step - aug\_p: 0.0477 - d\_loss: 0.1035 - g\_loss: 4.0058 - gen\_acc: 0.9771 - real\_acc: 0.9644 - val\_kid: 3.0212\
\
`<keras.src.callbacks.history.History at 0x794f705d3390>`\
\
* * *\
\
Inference\
---------\
\
Copied!\
\
`# load the best model and generate images model.load_weights(checkpoint_path) model.plot_images()`\
\
![png](https://keras.io/img/examples/generative/gan_ada/gan_ada_20_0.png)\
\
* * *\
\
Results\
-------\
\
By running the training for 400 epochs (which takes 2-3 hours in a Colab notebook), one can get high quality image generations using this code example.\
\
The evolution of a random batch of images over a 400 epoch training (ema=0.999 for animation smoothness): ![birds evolution gif](https://i.imgur.com/ecGuCcz.gif)\
\
Latent-space interpolation between a batch of selected images: ![birds interpolation gif](https://i.imgur.com/nGvzlsC.gif)\
\
I also recommend trying out training on other datasets, such as [CelebA](https://www.tensorflow.org/datasets/catalog/celeb_a)\
 for example. In my experience good results can be achieved without changing any hyperparameters (though discriminator augmentation might not be necessary).\
\
* * *\
\
GAN tips and tricks\
-------------------\
\
My goal with this example was to find a good tradeoff between ease of implementation and generation quality for GANs. During preparation, I have run numerous ablations using [this repository](https://github.com/beresandras/gan-flavours-keras)\
.\
\
In this section I list the lessons learned and my recommendations in my subjective order of importance.\
\
I recommend checking out the [DCGAN paper](https://arxiv.org/abs/1511.06434)\
, this [NeurIPS talk](https://www.youtube.com/watch?v=myGAju4L7O8)\
, and this [large scale GAN study](https://arxiv.org/abs/1711.10337)\
 for others' takes on this subject.\
\
### Architectural tips\
\
*   **resolution**: Training GANs at higher resolutions tends to get more difficult, I recommend experimenting at 32x32 or 64x64 resolutions initially.\
*   **initialization**: If you see strong colorful patterns early on in the training, the initialization might be the issue. Set the kernel\_initializer parameters of layers to [random normal](https://keras.io/api/layers/initializers/#randomnormal-class)\
    , and decrease the standard deviation (recommended value: 0.02, following DCGAN) until the issue disappears.\
*   **upsampling**: There are two main methods for upsampling in the generator. [Transposed convolution](https://keras.io/api/layers/convolution_layers/convolution2d_transpose/)\
     is faster, but can lead to [checkerboard artifacts](https://distill.pub/2016/deconv-checkerboard/)\
    , which can be reduced by using a kernel size that is divisible with the stride (recommended kernel size is 4 for a stride of 2). [Upsampling](https://keras.io/api/layers/reshaping_layers/up_sampling2d/)\
     + [standard convolution](https://keras.io/api/layers/convolution_layers/convolution2d/)\
     can have slightly lower quality, but checkerboard artifacts are not an issue. I recommend using nearest-neighbor interpolation over bilinear for it.\
*   **batch normalization in discriminator**: Sometimes has a high impact, I recommend trying out both ways.\
*   **[spectral normalization](https://www.tensorflow.org/addons/api_docs/python/tfa/layers/SpectralNormalization)\
    **: A popular technique for training GANs, can help with stability. I recommend disabling batch normalization's learnable scale parameters along with it.\
*   **[residual connections](https://keras.io/guides/functional_api/#a-toy-resnet-model)\
    **: While residual discriminators behave similarly, residual generators are more difficult to train in my experience. They are however necessary for training large and deep architectures. I recommend starting with non-residual architectures.\
*   **dropout**: Using dropout before the last layer of the discriminator improves generation quality in my experience. Recommended dropout rate is below 0.5.\
*   **[leaky ReLU](https://keras.io/api/layers/activation_layers/leaky_relu/)\
    **: Use leaky ReLU activations in the discriminator to make its gradients less sparse. Recommended slope/alpha is 0.2 following DCGAN.\
\
### Algorithmic tips\
\
*   **loss functions**: Numerous losses have been proposed over the years for training GANs, promising improved performance and stability. I have implemented 5 of them in [this repository](https://github.com/beresandras/gan-flavours-keras)\
    , and my experience is in line with [this GAN study](https://arxiv.org/abs/1711.10337)\
    : no loss seems to consistently outperform the default non-saturating GAN loss. I recommend using that as a default.\
*   **Adam's beta\_1 parameter**: The beta\_1 parameter in Adam can be interpreted as the momentum of mean gradient estimation. Using 0.5 or even 0.0 instead of the default 0.9 value was proposed in DCGAN and is important. This example would not work using its default value.\
*   **separate batch normalization for generated and real images**: The forward pass of the discriminator should be separate for the generated and real images. Doing otherwise can lead to artifacts (45 degree stripes in my case) and decreased performance.\
*   **exponential moving average of generator's weights**: This helps to reduce the variance of the KID measurement, and helps in averaging out the rapid color palette changes during training.\
*   **[different learning rate for generator and discriminator](https://arxiv.org/abs/1706.08500)\
    **: If one has the resources, it can help to tune the learning rates of the two networks separately. A similar idea is to update either network's (usually the discriminator's) weights multiple times for each of the other network's updates. I recommend using the same learning rate of 2e-4 (Adam), following DCGAN for both networks, and only updating both of them once as a default.\
*   **label noise**: [One-sided label smoothing](https://arxiv.org/abs/1606.03498)\
     (using less than 1.0 for real labels), or adding noise to the labels can regularize the discriminator not to get overconfident, however in my case they did not improve performance.\
*   **adaptive data augmentation**: Since it adds another dynamic component to the training process, disable it as a default, and only enable it when the other components already work well.\
\
* * *\
\
Related works\
-------------\
\
Other GAN-related Keras code examples:\
\
*   [DCGAN + CelebA](https://keras.io/examples/generative/dcgan_overriding_train_step/)\
    \
*   [WGAN + FashionMNIST](https://keras.io/examples/generative/wgan_gp/)\
    \
*   [WGAN + Molecules](https://keras.io/examples/generative/wgan-graphs/)\
    \
*   [ConditionalGAN + MNIST](https://keras.io/examples/generative/conditional_gan/)\
    \
*   [CycleGAN + Horse2Zebra](https://keras.io/examples/generative/cyclegan/)\
    \
*   [StyleGAN](https://keras.io/examples/generative/stylegan/)\
    \
\
Modern GAN architecture-lines:\
\
*   [SAGAN](https://arxiv.org/abs/1805.08318)\
    , [BigGAN](https://arxiv.org/abs/1809.11096)\
    \
*   [ProgressiveGAN](https://arxiv.org/abs/1710.10196)\
    , [StyleGAN](https://arxiv.org/abs/1812.04948)\
    , [StyleGAN2](https://arxiv.org/abs/1912.04958)\
    , [StyleGAN2-ADA](https://arxiv.org/abs/2006.06676)\
    , [AliasFreeGAN](https://arxiv.org/abs/2106.12423)\
    \
\
Concurrent papers on discriminator data augmentation: [1](https://arxiv.org/abs/2006.02595)\
, [2](https://arxiv.org/abs/2006.05338)\
, [3](https://arxiv.org/abs/2006.10738)\
\
Recent literature overview on GANs: [talk](https://www.youtube.com/watch?v=3ktD752xq5k)\
\
* * *\
\
Relevant Chapters from Deep Learning with Python\
------------------------------------------------\
\
*   [Chapter 17: Image generation](https://deeplearningwithpython.io/chapters/chapter17_image-generation)\
    \
\
[Data-efficient GANs with Adaptive Discriminator Augmentation](https://keras.io/examples/generative/gan_ada/#dataefficient-gans-with-adaptive-discriminator-augmentation)\
\
[Introduction](https://keras.io/examples/generative/gan_ada/#introduction)\
\
[GANs](https://keras.io/examples/generative/gan_ada/#gans)\
\
[Data augmentation for GANS](https://keras.io/examples/generative/gan_ada/#data-augmentation-for-gans)\
\
[Invertible data augmentation](https://keras.io/examples/generative/gan_ada/#invertible-data-augmentation)\
\
[Setup](https://keras.io/examples/generative/gan_ada/#setup)\
\
[Hyperparameterers](https://keras.io/examples/generative/gan_ada/#hyperparameterers)\
\
[Data pipeline](https://keras.io/examples/generative/gan_ada/#data-pipeline)\
\
[Kernel inception distance](https://keras.io/examples/generative/gan_ada/#kernel-inception-distance)\
\
[Adaptive discriminator augmentation](https://keras.io/examples/generative/gan_ada/#adaptive-discriminator-augmentation)\
\
[Network architecture](https://keras.io/examples/generative/gan_ada/#network-architecture)\
\
[GAN model](https://keras.io/examples/generative/gan_ada/#gan-model)\
\
[Training](https://keras.io/examples/generative/gan_ada/#training)\
\
[Inference](https://keras.io/examples/generative/gan_ada/#inference)\
\
[Results](https://keras.io/examples/generative/gan_ada/#results)\
\
[GAN tips and tricks](https://keras.io/examples/generative/gan_ada/#gan-tips-and-tricks)\
\
[Architectural tips](https://keras.io/examples/generative/gan_ada/#architectural-tips)\
\
[Algorithmic tips](https://keras.io/examples/generative/gan_ada/#algorithmic-tips)\
\
[Related works](https://keras.io/examples/generative/gan_ada/#related-works)\
\
[Relevant Chapters from Deep Learning with Python](https://keras.io/examples/generative/gan_ada/#relevant-chapters-from-deep-learning-with-python)