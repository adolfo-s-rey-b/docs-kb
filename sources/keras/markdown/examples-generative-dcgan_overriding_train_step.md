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
 / DCGAN to generate face images

DCGAN to generate face images
=============================

**Author:** [fchollet](https://twitter.com/fchollet)
  
**Date created:** 2019/04/29  
**Last modified:** 2023/12/21  
**Description:** A simple DCGAN trained using `fit()` by overriding `train_step` on CelebA images.

ⓘ This example uses Keras 3

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/generative/ipynb/dcgan_overriding_train_step.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/examples/generative/dcgan_overriding_train_step.py)

* * *

Setup
-----

Copied!

`import keras import tensorflow as tf  from keras import layers from keras import ops import matplotlib.pyplot as plt import os import gdown from zipfile import ZipFile`

* * *

Prepare CelebA data
-------------------

We'll use face images from the CelebA dataset, resized to 64x64.

Copied!

`os.makedirs("celeba_gan")  url = "https://drive.google.com/uc?id=1O7m1010EJjLE5QxLZiM9Fpjs7Oj6e684" output = "celeba_gan/data.zip" gdown.download(url, output, quiet=True)  with ZipFile("celeba_gan/data.zip", "r") as zipobj:     zipobj.extractall("celeba_gan")`

Create a dataset from our folder, and rescale the images to the \[0-1\] range:

Copied!

`dataset = keras.utils.image_dataset_from_directory(     "celeba_gan", label_mode=None, image_size=(64, 64), batch_size=32 ) dataset = dataset.map(lambda x: x / 255.0)`

`Found 202599 files.`

Let's display a sample image:

Copied!

`for x in dataset:     plt.axis("off")     plt.imshow((x.numpy() * 255).astype("int32")[0])     break`

![png](https://keras.io/img/examples/generative/dcgan_overriding_train_step/dcgan_overriding_train_step_8_0.png)

* * *

Create the discriminator
------------------------

It maps a 64x64 image to a binary classification score.

Copied!

`discriminator = keras.Sequential(     [         keras.Input(shape=(64, 64, 3)),         layers.Conv2D(64, kernel_size=4, strides=2, padding="same"),         layers.LeakyReLU(negative_slope=0.2),         layers.Conv2D(128, kernel_size=4, strides=2, padding="same"),         layers.LeakyReLU(negative_slope=0.2),         layers.Conv2D(128, kernel_size=4, strides=2, padding="same"),         layers.LeakyReLU(negative_slope=0.2),         layers.Flatten(),         layers.Dropout(0.2),         layers.Dense(1, activation="sigmoid"),     ],     name="discriminator", ) discriminator.summary()`

Model: "discriminator"

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Layer (type)                    ┃ Output Shape              ┃    Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ conv2d (Conv2D)                 │ (None, 32, 32, 64)        │      3,136 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ leaky\_re\_lu (LeakyReLU)         │ (None, 32, 32, 64)        │          0 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ conv2d\_1 (Conv2D)               │ (None, 16, 16, 128)       │    131,200 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ leaky\_re\_lu\_1 (LeakyReLU)       │ (None, 16, 16, 128)       │          0 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ conv2d\_2 (Conv2D)               │ (None, 8, 8, 128)         │    262,272 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ leaky\_re\_lu\_2 (LeakyReLU)       │ (None, 8, 8, 128)         │          0 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ flatten (Flatten)               │ (None, 8192)              │          0 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ dropout (Dropout)               │ (None, 8192)              │          0 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ dense (Dense)                   │ (None, 1)                 │      8,193 │
└─────────────────────────────────┴───────────────────────────┴────────────┘

 Total params: 404,801 (1.54 MB)

 Trainable params: 404,801 (1.54 MB)

 Non-trainable params: 0 (0.00 B)

* * *

Create the generator
--------------------

It mirrors the discriminator, replacing `Conv2D` layers with `Conv2DTranspose` layers.

Copied!

`latent_dim = 128  generator = keras.Sequential(     [         keras.Input(shape=(latent_dim,)),         layers.Dense(8 * 8 * 128),         layers.Reshape((8, 8, 128)),         layers.Conv2DTranspose(128, kernel_size=4, strides=2, padding="same"),         layers.LeakyReLU(negative_slope=0.2),         layers.Conv2DTranspose(256, kernel_size=4, strides=2, padding="same"),         layers.LeakyReLU(negative_slope=0.2),         layers.Conv2DTranspose(512, kernel_size=4, strides=2, padding="same"),         layers.LeakyReLU(negative_slope=0.2),         layers.Conv2D(3, kernel_size=5, padding="same", activation="sigmoid"),     ],     name="generator", ) generator.summary()`

Model: "generator"

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Layer (type)                    ┃ Output Shape              ┃    Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ dense\_1 (Dense)                 │ (None, 8192)              │  1,056,768 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ reshape (Reshape)               │ (None, 8, 8, 128)         │          0 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ conv2d\_transpose                │ (None, 16, 16, 128)       │    262,272 │
│ (Conv2DTranspose)               │                           │            │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ leaky\_re\_lu\_3 (LeakyReLU)       │ (None, 16, 16, 128)       │          0 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ conv2d\_transpose\_1              │ (None, 32, 32, 256)       │    524,544 │
│ (Conv2DTranspose)               │                           │            │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ leaky\_re\_lu\_4 (LeakyReLU)       │ (None, 32, 32, 256)       │          0 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ conv2d\_transpose\_2              │ (None, 64, 64, 512)       │  2,097,664 │
│ (Conv2DTranspose)               │                           │            │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ leaky\_re\_lu\_5 (LeakyReLU)       │ (None, 64, 64, 512)       │          0 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ conv2d\_3 (Conv2D)               │ (None, 64, 64, 3)         │     38,403 │
└─────────────────────────────────┴───────────────────────────┴────────────┘

 Total params: 3,979,651 (15.18 MB)

 Trainable params: 3,979,651 (15.18 MB)

 Non-trainable params: 0 (0.00 B)

* * *

Override `train_step`
---------------------

Copied!

`class GAN(keras.Model):     def __init__(self, discriminator, generator, latent_dim):         super().__init__()         self.discriminator = discriminator         self.generator = generator         self.latent_dim = latent_dim         self.seed_generator = keras.random.SeedGenerator(1337)      def compile(self, d_optimizer, g_optimizer, loss_fn):         super().compile()         self.d_optimizer = d_optimizer         self.g_optimizer = g_optimizer         self.loss_fn = loss_fn         self.d_loss_metric = keras.metrics.Mean(name="d_loss")         self.g_loss_metric = keras.metrics.Mean(name="g_loss")      @property     def metrics(self):         return [self.d_loss_metric, self.g_loss_metric]      def train_step(self, real_images):         # Sample random points in the latent space         batch_size = ops.shape(real_images)[0]         random_latent_vectors = keras.random.normal(             shape=(batch_size, self.latent_dim), seed=self.seed_generator         )          # Decode them to fake images         generated_images = self.generator(random_latent_vectors)          # Combine them with real images         combined_images = ops.concatenate([generated_images, real_images], axis=0)          # Assemble labels discriminating real from fake images         labels = ops.concatenate(             [ops.ones((batch_size, 1)), ops.zeros((batch_size, 1))], axis=0         )         # Add random noise to the labels - important trick!         labels += 0.05 * tf.random.uniform(tf.shape(labels))          # Train the discriminator         with tf.GradientTape() as tape:             predictions = self.discriminator(combined_images)             d_loss = self.loss_fn(labels, predictions)         grads = tape.gradient(d_loss, self.discriminator.trainable_weights)         self.d_optimizer.apply_gradients(             zip(grads, self.discriminator.trainable_weights)         )          # Sample random points in the latent space         random_latent_vectors = keras.random.normal(             shape=(batch_size, self.latent_dim), seed=self.seed_generator         )          # Assemble labels that say "all real images"         misleading_labels = ops.zeros((batch_size, 1))          # Train the generator (note that we should *not* update the weights         # of the discriminator)!         with tf.GradientTape() as tape:             predictions = self.discriminator(self.generator(random_latent_vectors))             g_loss = self.loss_fn(misleading_labels, predictions)         grads = tape.gradient(g_loss, self.generator.trainable_weights)         self.g_optimizer.apply_gradients(zip(grads, self.generator.trainable_weights))          # Update metrics         self.d_loss_metric.update_state(d_loss)         self.g_loss_metric.update_state(g_loss)         return {             "d_loss": self.d_loss_metric.result(),             "g_loss": self.g_loss_metric.result(),         }`

* * *

Create a callback that periodically saves generated images
----------------------------------------------------------

Copied!

`class GANMonitor(keras.callbacks.Callback):     def __init__(self, num_img=3, latent_dim=128):         self.num_img = num_img         self.latent_dim = latent_dim         self.seed_generator = keras.random.SeedGenerator(42)      def on_epoch_end(self, epoch, logs=None):         random_latent_vectors = keras.random.normal(             shape=(self.num_img, self.latent_dim), seed=self.seed_generator         )         generated_images = self.model.generator(random_latent_vectors)         generated_images *= 255         generated_images.numpy()         for i in range(self.num_img):             img = keras.utils.array_to_img(generated_images[i])             img.save("generated_img_%03d_%d.png" % (epoch, i))`

* * *

Train the end-to-end model
--------------------------

Copied!

`epochs = 1  # In practice, use ~100 epochs  gan = GAN(discriminator=discriminator, generator=generator, latent_dim=latent_dim) gan.compile(     d_optimizer=keras.optimizers.Adam(learning_rate=0.0001),     g_optimizer=keras.optimizers.Adam(learning_rate=0.0001),     loss_fn=keras.losses.BinaryCrossentropy(), )  gan.fit(     dataset, epochs=epochs, callbacks=[GANMonitor(num_img=10, latent_dim=latent_dim)] )`

    `2/6332 [37m━━━━━━━━━━━━━━━━━━━━  9:54 94ms/step - d_loss: 0.6792 - g_loss: 0.7880     WARNING: All log messages before absl::InitializeLog() is called are written to STDERR I0000 00:00:1704214667.959762    1319 device_compiler.h:186] Compiled cluster using XLA!  This line is logged at most once for the lifetime of the process.   6332/6332 ━━━━━━━━━━━━━━━━━━━━ 557s 84ms/step - d_loss: 0.5616 - g_loss: 1.4099  <keras.src.callbacks.history.History at 0x7f251d32bc40>`

Some of the last generated images around epoch 30 (results keep improving after that):

![results](https://i.imgur.com/h5MtQZ7l.png)

* * *

Relevant Chapters from Deep Learning with Python
------------------------------------------------

*   [Chapter 17: Image generation](https://deeplearningwithpython.io/chapters/chapter17_image-generation)
    

[DCGAN to generate face images](https://keras.io/examples/generative/dcgan_overriding_train_step/#dcgan-to-generate-face-images)

[Setup](https://keras.io/examples/generative/dcgan_overriding_train_step/#setup)

[Prepare CelebA data](https://keras.io/examples/generative/dcgan_overriding_train_step/#prepare-celeba-data)

[Create the discriminator](https://keras.io/examples/generative/dcgan_overriding_train_step/#create-the-discriminator)

[Create the generator](https://keras.io/examples/generative/dcgan_overriding_train_step/#create-the-generator)

[Override `train_step`](https://keras.io/examples/generative/dcgan_overriding_train_step/#override-trainstep)

[Create a callback that periodically saves generated images](https://keras.io/examples/generative/dcgan_overriding_train_step/#create-a-callback-that-periodically-saves-generated-images)

[Train the end-to-end model](https://keras.io/examples/generative/dcgan_overriding_train_step/#train-the-endtoend-model)

[Relevant Chapters from Deep Learning with Python](https://keras.io/examples/generative/dcgan_overriding_train_step/#relevant-chapters-from-deep-learning-with-python)