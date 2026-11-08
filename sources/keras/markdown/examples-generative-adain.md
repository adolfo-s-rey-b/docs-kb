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
 / Neural Style Transfer with AdaIN

Neural Style Transfer with AdaIN
================================

**Author:** [Aritra Roy Gosthipaty](https://twitter.com/arig23498)
, [Ritwik Raha](https://twitter.com/ritwik_raha)
  
**Date created:** 2021/11/08  
**Last modified:** 2026/04/13  
**Description:** Neural Style Transfer with Adaptive Instance Normalization.

ⓘ This example uses Keras 3

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/generative/ipynb/adain.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/examples/generative/adain.py)

Introduction
============

[Neural Style Transfer](https://en.wikipedia.org/wiki/Neural_style_transfer)
 is the process of transferring the style of one image onto the content of another. This was first introduced in the seminal paper ["A Neural Algorithm of Artistic Style"](https://arxiv.org/abs/1508.06576)
 by Gatys et al. A major limitation of the technique proposed in this work is in its runtime, as the algorithm uses a slow iterative optimization process.

Follow-up papers that introduced [Batch Normalization](https://arxiv.org/abs/1502.03167)
, [Instance Normalization](https://arxiv.org/abs/1701.02096)
 and [Conditional Instance Normalization](https://arxiv.org/abs/1610.07629)
 allowed Style Transfer to be performed in new ways, no longer requiring a slow iterative process.

Following these papers, the authors Xun Huang and Serge Belongie propose [Adaptive Instance Normalization](https://arxiv.org/abs/1703.06868)
 (AdaIN), which allows arbitrary style transfer in real time.

In this example we implement Adaptive Instance Normalization for Neural Style Transfer. We show in the below figure the output of our AdaIN model trained for only **30 epochs**.

![Style transfer sample gallery](https://i.imgur.com/zDjDuea.png)

You can also try out the model with your own images with this [Hugging Face demo](https://huggingface.co/spaces/ariG23498/nst)
.

Setup
=====

We begin by importing the packages used throughout the example and defining a few global hyperparameters that control image size, batch size, and training duration.

Copied!

`import os import numpy as np import keras import matplotlib.pyplot as plt from keras import layers  # Defining the global variables. IMAGE_SIZE = (224, 224) BATCH_SIZE = 64 # Training for 30 epochs. Reduce for faster iteration. EPOCHS = 30`

* * *

Style transfer sample gallery
-----------------------------

For Neural Style Transfer we need style images and content images. In this example we will use the [Best Artworks of All Time](https://www.kaggle.com/ikarus777/best-artworks-of-all-time)
 as our style dataset and [Pascal VOC](https://host.robots.ox.ac.uk/pascal/VOC/)
 images as our content dataset.

This is a deviation from the original paper implementation by the authors, where they use [WIKI-Art](https://paperswithcode.com/dataset/wikiart)
 as style and [MSCOCO](https://cocodataset.org/#home)
 as content datasets respectively. We do this to create a minimal yet reproducible example.

* * *

Downloading the dataset from Kaggle
-----------------------------------

The [Best Artworks of All Time](https://www.kaggle.com/ikarus777/best-artworks-of-all-time)
 dataset is hosted on Kaggle and one can easily download it in Colab by following these steps:

*   Follow the instructions [here](https://github.com/Kaggle/kaggle-api)
     in order to obtain your Kaggle API keys in case you don't have them.
*   Use the following command to upload the Kaggle API keys.

Copied!

`from google.colab import files files.upload()`

*   Use the following commands to move the API keys to the proper directory and download the style dataset.

Copied!

`$ mkdir ~/.kaggle $ cp kaggle.json ~/.kaggle/ $ chmod 600 ~/.kaggle/kaggle.json $ kaggle datasets download ikarus777/best-artworks-of-all-time $ unzip -qq best-artworks-of-all-time.zip $ rm -rf images $ mv resized artwork $ rm best-artworks-of-all-time.zip artists.csv`

*   Download Pascal VOC 2012 images and extract them under `/content/VOCdevkit/VOC2012/JPEGImages`.

* * *

`PyDataset` pipeline
--------------------

In this section, we build a [`keras.utils.PyDataset`](https://keras.io/api/utils/preprocessing_utils#pydataset-class)
 input pipeline with no `tensorflow_datasets` dependency.

Both style and content images are read from local folders, decoded, resized, and paired inside a custom `PyDataset` implementation.

After loading image paths, we create train, validation, and test `PyDataset` instances that the model will consume.

Copied!

`class StyleContentPyDataset(keras.utils.PyDataset):     def __init__(         self, style_paths, content_paths, batch_size, image_size, shuffle=True     ):         super().__init__()         self.style_paths = style_paths         self.content_paths = content_paths         self.batch_size = batch_size         self.image_size = image_size         self.shuffle = shuffle          self.num_style = len(self.style_paths)         self.num_content = len(self.content_paths)         self.num_samples = max(self.num_style, self.num_content)          self.indices = np.arange(self.num_samples)         if self.shuffle:             np.random.shuffle(self.indices)      def __len__(self):         return int(np.ceil(self.num_samples / self.batch_size))      def on_epoch_end(self):         if self.shuffle:             np.random.shuffle(self.indices)      def _load_image(self, image_path):         image = keras.utils.load_img(image_path, target_size=self.image_size)         image = keras.utils.img_to_array(image).astype("float32") / 255.0         return image      def __getitem__(self, index):         start = index * self.batch_size         end = min(start + self.batch_size, self.num_samples)         batch_indices = self.indices[start:end]          style_batch = [             self._load_image(self.style_paths[i % self.num_style])             for i in batch_indices         ]         content_batch = [             self._load_image(self.content_paths[i % self.num_content])             for i in batch_indices         ]          # Return x only as a length-1 tuple so fit() treats (style, content) as model input.         return ((np.stack(style_batch), np.stack(content_batch)),)  def list_image_paths(image_root):     valid_exts = (".jpg", ".jpeg", ".png", ".bmp", ".webp")     image_paths = [         os.path.join(image_root, name)         for name in os.listdir(image_root)         if os.path.isfile(os.path.join(image_root, name))         and name.lower().endswith(valid_exts)     ]     image_paths.sort()      if not image_paths:         raise ValueError(f"No images found under: {image_root}")     return image_paths  def split_paths(paths):     total = len(paths)     train_end = max(1, int(0.8 * total))     val_end = max(train_end + 1, int(0.9 * total))      train = paths[:train_end]     val = paths[train_end:val_end]     test = paths[val_end:]      # Ensure no split is empty for very small fallback datasets.     if not val:         val = train[: min(len(train), 1)]     if not test:         test = train[: min(len(train), 1)]      return train, val, test  def ensure_fallback_image_dirs(style_root, content_root, image_size):     if os.path.isdir(style_root) and os.path.isdir(content_root):         if os.listdir(style_root) and os.listdir(content_root):             return style_root, content_root      fallback_style = "/tmp/adain_data/style"     fallback_content = "/tmp/adain_data/content"     os.makedirs(fallback_style, exist_ok=True)     os.makedirs(fallback_content, exist_ok=True)      (x_train, _), _ = keras.datasets.cifar10.load_data()     x_train = x_train[:1000]      for i, image in enumerate(x_train):         pil_img = keras.utils.array_to_img(image)         pil_img = pil_img.resize((image_size[1], image_size[0]))         if i % 2 == 0:             pil_img.save(os.path.join(fallback_style, f"style_{i:04d}.jpg"))         else:             pil_img.save(os.path.join(fallback_content, f"content_{i:04d}.jpg"))      print(         "Using fallback local data at /tmp/adain_data because /content paths were not found."     )     return fallback_style, fallback_content  # Dataset roots style_root = "/content/artwork/resized" content_root = "/content/VOCdevkit/VOC2012/JPEGImages" style_root, content_root = ensure_fallback_image_dirs(     style_root, content_root, IMAGE_SIZE )  # Build path lists style_paths = list_image_paths(style_root) content_paths = list_image_paths(content_root)  # Shuffle before splitting so the split doesn't depend on filesystem order. rng = np.random.default_rng(seed=42) rng.shuffle(style_paths) rng.shuffle(content_paths)  # Split style/content paths train_style, val_style, test_style = split_paths(style_paths) train_content, val_content, test_content = split_paths(content_paths)  # Build PyDataset objects train_ds = StyleContentPyDataset(     train_style,     train_content,     batch_size=BATCH_SIZE,     image_size=IMAGE_SIZE,     shuffle=True, ) val_ds = StyleContentPyDataset(     val_style, val_content, batch_size=BATCH_SIZE, image_size=IMAGE_SIZE, shuffle=False ) test_ds = StyleContentPyDataset(     test_style, test_content, batch_size=BATCH_SIZE, image_size=IMAGE_SIZE, shuffle=True )`

Using fallback local data at /tmp/adain\_data because /content paths were not found.

* * *

Visualizing the data
--------------------

It is always better to visualize the data before training. To ensure the correctness of our preprocessing pipeline, we visualize 10 samples from our dataset.

Copied!

`((style, content),) = train_ds[0] fig, axes = plt.subplots(nrows=10, ncols=2, figsize=(5, 30)) [ax.axis("off") for ax in np.ravel(axes)]  for axis, style_image, content_image in zip(axes, style[0:10], content[0:10]):     ax_style, ax_content = axis     ax_style.imshow(style_image)     ax_style.set_title("Style Image")      ax_content.imshow(content_image)     ax_content.set_title("Content Image")`

![png](https://keras.io/img/examples/generative/adain/adain_8_0.png)

* * *

Architecture
------------

The style transfer network takes a content image and a style image as inputs and outputs the style transferred image. The authors of AdaIN propose a simple encoder-decoder structure for achieving this.

![AdaIN architecture](https://i.imgur.com/JbIfoyE.png)

The content image (`C`) and the style image (`S`) are both fed to the encoder networks. The output from these encoder networks (feature maps) are then fed to the AdaIN layer. The AdaIN layer computes a combined feature map. This feature map is then fed into a randomly initialized decoder network that serves as the generator for the neural style transferred image.

![AdaIn equation](https://i.imgur.com/hqhcBQS.png)

The style feature map (`fs`) and the content feature map (`fc`) are fed to the AdaIN layer. This layer produced the combined feature map `t`. The function `g` represents the decoder (generator) network.

### Encoder

The encoder is a part of the pretrained (pretrained on [imagenet](https://www.image-net.org/)
) VGG19 model. We slice the model from the `block4-conv1` layer. The output layer is as suggested by the authors in their paper.

Copied!

`def get_encoder():     vgg19 = keras.applications.VGG19(         include_top=False,         weights="imagenet",         input_shape=(*IMAGE_SIZE, 3),     )     vgg19.trainable = False     mini_vgg19 = keras.Model(vgg19.input, vgg19.get_layer("block4_conv1").output)      inputs = layers.Input([*IMAGE_SIZE, 3])     mini_vgg19_out = mini_vgg19(inputs)     return keras.Model(inputs, mini_vgg19_out, name="mini_vgg19")`

### Adaptive Instance Normalization

The AdaIN layer takes in the features of the content and style image. The layer can be defined via the following equation:

![AdaIn formula](https://i.imgur.com/tWq3VKP.png)

where `sigma` is the standard deviation and `mu` is the mean for the concerned variable. In the above equation the mean and variance of the content feature map `fc` is aligned with the mean and variance of the style feature maps `fs`.

It is important to note that the AdaIN layer proposed by the authors uses no other parameters apart from mean and variance. The layer also does not have any trainable parameters. This is why we use a _Python function_ instead of using a _Keras layer_. The function takes style and content feature maps, computes the mean and standard deviation of the images and returns the adaptive instance normalized feature map.

Copied!

`def get_mean_std(x, epsilon=1e-5):     axes = [1, 2]      # Compute the mean and standard deviation of a tensor.     mean, variance = keras.ops.moments(x, axes=axes, keepdims=True)     standard_deviation = keras.ops.sqrt(variance + epsilon)     return mean, standard_deviation  def ada_in(style, content):     """Computes the AdaIn feature map.      Args:         style: The style feature map.         content: The content feature map.      Returns:         The AdaIN feature map.     """     content_mean, content_std = get_mean_std(content)     style_mean, style_std = get_mean_std(style)     t = style_std * (content - content_mean) / content_std + style_mean     return t`

### Decoder

The authors specify that the decoder network must mirror the encoder network. We have symmetrically inverted the encoder to build our decoder. We have used `UpSampling2D` layers to increase the spatial resolution of the feature maps.

Note that the authors warn against using any normalization layer in the decoder network, and do indeed go on to show that including batch normalization or instance normalization hurts the performance of the overall network.

This is the only portion of the entire architecture that is trainable.

Copied!

`def get_decoder():     config = {"kernel_size": 3, "strides": 1, "padding": "same", "activation": "relu"}     decoder = keras.Sequential(         [             layers.InputLayer((None, None, 512)),             layers.Conv2D(filters=512, **config),             layers.UpSampling2D(),             layers.Conv2D(filters=256, **config),             layers.Conv2D(filters=256, **config),             layers.Conv2D(filters=256, **config),             layers.Conv2D(filters=256, **config),             layers.UpSampling2D(),             layers.Conv2D(filters=128, **config),             layers.Conv2D(filters=128, **config),             layers.UpSampling2D(),             layers.Conv2D(filters=64, **config),             layers.Conv2D(                 filters=3,                 kernel_size=3,                 strides=1,                 padding="same",                 activation="sigmoid",             ),         ]     )     return decoder`

### Loss functions

Here we build the loss functions for the neural style transfer model. The authors propose to use a pretrained VGG-19 to compute the loss function of the network. It is important to keep in mind that this will be used for training only the decoder network. The total loss (`Lt`) is a weighted combination of content loss (`Lc`) and style loss (`Ls`). The `lambda` term is used to vary the amount of style transferred.

![The total loss](https://i.imgur.com/Q5y1jUM.png)

### Content Loss

This is the Euclidean distance between the content image features and the features of the neural style transferred image.

![The content loss](https://i.imgur.com/dZ0uD0N.png)

Here the authors propose to use the output from the AdaIn layer `t` as the content target rather than using features of the original image as target. This is done to speed up convergence.

### Style Loss

Rather than using the more commonly used [Gram Matrix](https://mathworld.wolfram.com/GramMatrix.html)
, the authors propose to compute the difference between the statistical features (mean and variance) which makes it conceptually cleaner. This can be easily visualized via the following equation:

![The style loss](https://i.imgur.com/Ctclhn3.png)

where `theta` denotes the layers in VGG-19 used to compute the loss. In this case this corresponds to:

*   `block1_conv1`
*   `block2_conv1`
*   `block3_conv1`
*   `block4_conv1`

Copied!

`def get_loss_net():     vgg19 = keras.applications.VGG19(         include_top=False, weights="imagenet", input_shape=(*IMAGE_SIZE, 3)     )     vgg19.trainable = False     layer_names = ["block1_conv1", "block2_conv1", "block3_conv1", "block4_conv1"]     outputs = [vgg19.get_layer(name).output for name in layer_names]     mini_vgg19 = keras.Model(vgg19.input, outputs)      inputs = layers.Input([*IMAGE_SIZE, 3])     mini_vgg19_out = mini_vgg19(inputs)     return keras.Model(inputs, mini_vgg19_out, name="loss_net")`

* * *

Neural Style Transfer
---------------------

This is the trainer module. We wrap the encoder and decoder inside a [`keras.Model`](https://keras.io/api/models/model#model-class)
 subclass and migrate training logic into `compute_loss()`. This lets Keras run the backend-native training step while we keep custom loss computation for AdaIN.

Copied!

`class NeuralStyleTransfer(keras.Model):     def __init__(self, encoder, decoder, loss_net, style_weight, **kwargs):         super().__init__(**kwargs)         self.encoder = encoder         self.decoder = decoder         self.loss_net = loss_net         self.style_weight = style_weight          self.style_loss_tracker = keras.metrics.Mean(name="style_loss")         self.content_loss_tracker = keras.metrics.Mean(name="content_loss")         self.total_loss_tracker = keras.metrics.Mean(name="total_loss")      def compile(self, optimizer, loss_fn, **kwargs):         super().compile(optimizer=optimizer, **kwargs)         self.loss_fn = loss_fn      def call(self, inputs, training=False):         style, content = inputs          # Encode style and content, then construct AdaIN target.         style_encoded = self.encoder(style, training=False)         content_encoded = self.encoder(content, training=False)         target_features = ada_in(style=style_encoded, content=content_encoded)          # Decode back into image space.         reconstructed_image = self.decoder(target_features, training=training)          return {             "reconstructed_image": reconstructed_image,             "target_features": target_features,             "style": style,         }      def compute_loss(self, x=None, y=None, y_pred=None, sample_weight=None):         # Loss content comes from target AdaIN features vs reconstructed features.         reconstructed_vgg_features = self.loss_net(             y_pred["reconstructed_image"], training=False         )         style_vgg_features = self.loss_net(y_pred["style"], training=False)          loss_content = self.loss_fn(             y_pred["target_features"], reconstructed_vgg_features[-1]         )          # Style loss matches means/variances at each VGG feature level.         loss_style = 0.0         for inp, out in zip(style_vgg_features, reconstructed_vgg_features):             mean_inp, std_inp = get_mean_std(inp)             mean_out, std_out = get_mean_std(out)             loss_style += self.loss_fn(mean_inp, mean_out) + self.loss_fn(                 std_inp, std_out             )         loss_style = self.style_weight * loss_style          total_loss = loss_content + loss_style          # Update trackers for progress logs.         self.style_loss_tracker.update_state(loss_style)         self.content_loss_tracker.update_state(loss_content)         self.total_loss_tracker.update_state(total_loss)          return total_loss      @property     def metrics(self):         return [             self.style_loss_tracker,             self.content_loss_tracker,             self.total_loss_tracker,         ]`

* * *

Train Monitor callback
----------------------

This callback is used to visualize the style transfer output of the model at the end of each epoch. The objective of style transfer cannot be quantified properly, and is to be subjectively evaluated by an audience. For this reason, visualization is a key aspect of evaluating the model.

Copied!

`((test_style, test_content),) = next(iter(test_ds))  class TrainMonitor(keras.callbacks.Callback):     def on_epoch_end(self, epoch, logs=None):         # Encode the style and content image.         test_style_encoded = self.model.encoder(test_style)         test_content_encoded = self.model.encoder(test_content)          # Compute the AdaIN features.         test_t = ada_in(style=test_style_encoded, content=test_content_encoded)         test_reconstructed_image = self.model.decoder(test_t)          # Plot the Style, Content and the NST image.         fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(20, 5))         ax[0].imshow(keras.utils.array_to_img(test_style[0]))         ax[0].set_title(f"Style: {epoch:03d}")          ax[1].imshow(keras.utils.array_to_img(test_content[0]))         ax[1].set_title(f"Content: {epoch:03d}")          ax[2].imshow(keras.utils.array_to_img(test_reconstructed_image[0]))         ax[2].set_title(f"NST: {epoch:03d}")          plt.show()         plt.close()`

* * *

Train the model
---------------

In this section, we define the optimizer, the loss function, and the trainer module. We compile the trainer module with the optimizer and the loss function and then train it.

_Note_: We train the model for 30 epochs here, but you can reduce this for faster iteration.

Copied!

`optimizer = keras.optimizers.Adam(learning_rate=1e-5) loss_fn = keras.losses.MeanSquaredError()  encoder = get_encoder() loss_net = get_loss_net() decoder = get_decoder()  model = NeuralStyleTransfer(     encoder=encoder, decoder=decoder, loss_net=loss_net, style_weight=4.0 )  model.compile(optimizer=optimizer, loss_fn=loss_fn)  train_steps = min(50, len(train_ds)) val_steps = min(50, len(val_ds))  history = model.fit(     train_ds,     epochs=EPOCHS,     steps_per_epoch=train_steps,     validation_data=val_ds,     validation_steps=val_steps,     callbacks=[TrainMonitor()], )`

Epoch 1/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 69.3327 - style\_loss: 140.9464 - total\_loss: 210.2792

![png](https://keras.io/img/examples/generative/adain/adain_23_8.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 25s 3s/step - content\_loss: 64.4736 - style\_loss: 129.5553 - total\_loss: 194.0289 - val\_content\_loss: 61.5842 - val\_style\_loss: 121.2355 - val\_total\_loss: 182.8197 Epoch 2/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 58.3413 - style\_loss: 110.8445 - total\_loss: 169.1858

![png](https://keras.io/img/examples/generative/adain/adain_23_18.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 58.0459 - style\_loss: 108.7533 - total\_loss: 166.7992 - val\_content\_loss: 58.5479 - val\_style\_loss: 110.1745 - val\_total\_loss: 168.7224 Epoch 3/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 55.2051 - style\_loss: 100.6297 - total\_loss: 155.8348

![png](https://keras.io/img/examples/generative/adain/adain_23_28.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 54.5550 - style\_loss: 97.7767 - total\_loss: 152.3318 - val\_content\_loss: 56.7784 - val\_style\_loss: 99.6632 - val\_total\_loss: 156.4415 Epoch 4/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 52.8162 - style\_loss: 89.3740 - total\_loss: 142.1902

![png](https://keras.io/img/examples/generative/adain/adain_23_38.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 52.2626 - style\_loss: 88.3876 - total\_loss: 140.6502 - val\_content\_loss: 53.1038 - val\_style\_loss: 90.5593 - val\_total\_loss: 143.6631 Epoch 5/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 3s/step - content\_loss: 48.9089 - style\_loss: 79.1898 - total\_loss: 128.0987

![png](https://keras.io/img/examples/generative/adain/adain_23_48.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 48.3021 - style\_loss: 77.6323 - total\_loss: 125.9344 - val\_content\_loss: 49.3859 - val\_style\_loss: 76.2716 - val\_total\_loss: 125.6575 Epoch 6/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 46.5736 - style\_loss: 66.7209 - total\_loss: 113.2945

![png](https://keras.io/img/examples/generative/adain/adain_23_58.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 46.2035 - style\_loss: 64.3224 - total\_loss: 110.5259 - val\_content\_loss: 46.8296 - val\_style\_loss: 55.3400 - val\_total\_loss: 102.1695 Epoch 7/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 45.0892 - style\_loss: 49.0773 - total\_loss: 94.1665

![png](https://keras.io/img/examples/generative/adain/adain_23_68.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 43.8027 - style\_loss: 45.6226 - total\_loss: 89.4253 - val\_content\_loss: 44.6162 - val\_style\_loss: 47.6259 - val\_total\_loss: 92.2422 Epoch 8/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 41.9670 - style\_loss: 42.2324 - total\_loss: 84.1994

![png](https://keras.io/img/examples/generative/adain/adain_23_78.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 41.9080 - style\_loss: 41.7055 - total\_loss: 83.6135 - val\_content\_loss: 42.9081 - val\_style\_loss: 44.1262 - val\_total\_loss: 87.0343 Epoch 9/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 41.0440 - style\_loss: 39.7052 - total\_loss: 80.7492

![png](https://keras.io/img/examples/generative/adain/adain_23_88.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 40.8874 - style\_loss: 38.1873 - total\_loss: 79.0748 - val\_content\_loss: 42.6833 - val\_style\_loss: 38.9655 - val\_total\_loss: 81.6487 Epoch 10/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 40.2837 - style\_loss: 33.6737 - total\_loss: 73.9575

![png](https://keras.io/img/examples/generative/adain/adain_23_98.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 39.9428 - style\_loss: 34.1020 - total\_loss: 74.0449 - val\_content\_loss: 40.4202 - val\_style\_loss: 36.6194 - val\_total\_loss: 77.0396 Epoch 11/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 37.7901 - style\_loss: 32.1251 - total\_loss: 69.9152

![png](https://keras.io/img/examples/generative/adain/adain_23_108.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 37.6326 - style\_loss: 32.0121 - total\_loss: 69.6447 - val\_content\_loss: 38.7432 - val\_style\_loss: 33.8374 - val\_total\_loss: 72.5806 Epoch 12/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 36.8127 - style\_loss: 30.6076 - total\_loss: 67.4203

![png](https://keras.io/img/examples/generative/adain/adain_23_118.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 36.4167 - style\_loss: 29.9773 - total\_loss: 66.3941 - val\_content\_loss: 36.4050 - val\_style\_loss: 30.8240 - val\_total\_loss: 67.2290 Epoch 13/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 33.8249 - style\_loss: 27.3473 - total\_loss: 61.1722

![png](https://keras.io/img/examples/generative/adain/adain_23_128.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 33.0191 - style\_loss: 26.5015 - total\_loss: 59.5206 - val\_content\_loss: 33.8826 - val\_style\_loss: 28.0350 - val\_total\_loss: 61.9177 Epoch 14/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 30.7907 - style\_loss: 24.0908 - total\_loss: 54.8815

![png](https://keras.io/img/examples/generative/adain/adain_23_138.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 30.9472 - style\_loss: 24.6625 - total\_loss: 55.6098 - val\_content\_loss: 31.0826 - val\_style\_loss: 25.6283 - val\_total\_loss: 56.7110 Epoch 15/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 28.0676 - style\_loss: 22.0865 - total\_loss: 50.1541

![png](https://keras.io/img/examples/generative/adain/adain_23_148.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 27.8455 - style\_loss: 22.1264 - total\_loss: 49.9719 - val\_content\_loss: 28.5455 - val\_style\_loss: 23.5957 - val\_total\_loss: 52.1412 Epoch 16/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 26.2761 - style\_loss: 21.0945 - total\_loss: 47.3706

![png](https://keras.io/img/examples/generative/adain/adain_23_158.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 25.7858 - style\_loss: 21.1223 - total\_loss: 46.9081 - val\_content\_loss: 26.5362 - val\_style\_loss: 21.9274 - val\_total\_loss: 48.4636 Epoch 17/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 3s/step - content\_loss: 23.6390 - style\_loss: 18.7739 - total\_loss: 42.4129

![png](https://keras.io/img/examples/generative/adain/adain_23_168.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 23.7391 - style\_loss: 19.0580 - total\_loss: 42.7971 - val\_content\_loss: 24.9193 - val\_style\_loss: 20.4144 - val\_total\_loss: 45.3337 Epoch 18/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 3s/step - content\_loss: 22.4734 - style\_loss: 17.9847 - total\_loss: 40.4581

![png](https://keras.io/img/examples/generative/adain/adain_23_178.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 22.4346 - style\_loss: 18.0033 - total\_loss: 40.4380 - val\_content\_loss: 23.3949 - val\_style\_loss: 19.1585 - val\_total\_loss: 42.5533 Epoch 19/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 21.3290 - style\_loss: 17.0995 - total\_loss: 38.4285

![png](https://keras.io/img/examples/generative/adain/adain_23_188.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 21.0454 - style\_loss: 16.8622 - total\_loss: 37.9076 - val\_content\_loss: 22.4199 - val\_style\_loss: 18.0265 - val\_total\_loss: 40.4464 Epoch 20/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 19.8949 - style\_loss: 15.9196 - total\_loss: 35.8146

![png](https://keras.io/img/examples/generative/adain/adain_23_198.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 20.2994 - style\_loss: 16.1616 - total\_loss: 36.4610 - val\_content\_loss: 21.6341 - val\_style\_loss: 17.2532 - val\_total\_loss: 38.8873 Epoch 21/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 19.9996 - style\_loss: 15.7381 - total\_loss: 35.7377

![png](https://keras.io/img/examples/generative/adain/adain_23_208.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 19.5869 - style\_loss: 15.2180 - total\_loss: 34.8049 - val\_content\_loss: 20.7572 - val\_style\_loss: 16.6049 - val\_total\_loss: 37.3621 Epoch 22/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 19.2298 - style\_loss: 15.3685 - total\_loss: 34.5983

![png](https://keras.io/img/examples/generative/adain/adain_23_218.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 18.9491 - style\_loss: 14.7553 - total\_loss: 33.7044 - val\_content\_loss: 20.2151 - val\_style\_loss: 15.9647 - val\_total\_loss: 36.1798 Epoch 23/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 18.6367 - style\_loss: 14.3806 - total\_loss: 33.0173

![png](https://keras.io/img/examples/generative/adain/adain_23_228.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 18.5593 - style\_loss: 14.2651 - total\_loss: 32.8244 - val\_content\_loss: 19.5625 - val\_style\_loss: 15.5629 - val\_total\_loss: 35.1255 Epoch 24/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 18.5452 - style\_loss: 14.5071 - total\_loss: 33.0524

![png](https://keras.io/img/examples/generative/adain/adain_23_238.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 18.0261 - style\_loss: 14.1054 - total\_loss: 32.1316 - val\_content\_loss: 19.1599 - val\_style\_loss: 15.1159 - val\_total\_loss: 34.2758 Epoch 25/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 17.6185 - style\_loss: 13.5009 - total\_loss: 31.1194

![png](https://keras.io/img/examples/generative/adain/adain_23_248.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 17.7612 - style\_loss: 13.4830 - total\_loss: 31.2442 - val\_content\_loss: 18.9258 - val\_style\_loss: 14.6126 - val\_total\_loss: 33.5383 Epoch 26/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 3s/step - content\_loss: 17.5533 - style\_loss: 12.5722 - total\_loss: 30.1255

![png](https://keras.io/img/examples/generative/adain/adain_23_258.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 17.3663 - style\_loss: 13.0496 - total\_loss: 30.4158 - val\_content\_loss: 18.3139 - val\_style\_loss: 14.6291 - val\_total\_loss: 32.9430 Epoch 27/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 17.6558 - style\_loss: 13.8729 - total\_loss: 31.5287

![png](https://keras.io/img/examples/generative/adain/adain_23_268.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 17.2391 - style\_loss: 13.4659 - total\_loss: 30.7049 - val\_content\_loss: 18.0461 - val\_style\_loss: 14.3104 - val\_total\_loss: 32.3565 Epoch 28/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 17.0192 - style\_loss: 13.0646 - total\_loss: 30.0838

![png](https://keras.io/img/examples/generative/adain/adain_23_278.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 16.6298 - style\_loss: 12.8305 - total\_loss: 29.4603 - val\_content\_loss: 17.8203 - val\_style\_loss: 14.0111 - val\_total\_loss: 31.8314 Epoch 29/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 2s/step - content\_loss: 16.4851 - style\_loss: 12.4063 - total\_loss: 28.8914

![png](https://keras.io/img/examples/generative/adain/adain_23_288.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 16.2729 - style\_loss: 12.4816 - total\_loss: 28.7545 - val\_content\_loss: 17.5812 - val\_style\_loss: 13.7577 - val\_total\_loss: 31.3390 Epoch 30/30 7/7 ━━━━━━━━━━━━━━━━━━━━ 0s 3s/step - content\_loss: 15.9445 - style\_loss: 12.1650 - total\_loss: 28.1095

![png](https://keras.io/img/examples/generative/adain/adain_23_298.png)

7/7 ━━━━━━━━━━━━━━━━━━━━ 20s 3s/step - content\_loss: 16.0177 - style\_loss: 12.2860 - total\_loss: 28.3037 - val\_content\_loss: 17.2777 - val\_style\_loss: 13.4660 - val\_total\_loss: 30.7437

* * *

Inference
---------

After we train the model, we now need to run inference with it. We will pass arbitrary content and style images from the test dataset and take a look at the output images.

_NOTE_: To try out the model on your own images, you can use this [Hugging Face demo](https://huggingface.co/spaces/ariG23498/nst)
.

Copied!

`((style, content),) = test_ds[0] style_encoded = model.encoder(style) content_encoded = model.encoder(content) t = ada_in(style=style_encoded, content=content_encoded) reconstructed_image = model.decoder(t) fig, axes = plt.subplots(nrows=10, ncols=3, figsize=(10, 30)) [ax.axis("off") for ax in np.ravel(axes)]  for axis, style_image, content_image, recon_image in zip(     axes, style[0:10], content[0:10], reconstructed_image[0:10] ):     ax_style, ax_content, ax_reconstructed = axis     ax_style.imshow(style_image)     ax_style.set_title("Style Image")     ax_content.imshow(content_image)     ax_content.set_title("Content Image")     ax_reconstructed.imshow(recon_image)     ax_reconstructed.set_title("NST Image")`

![png](https://keras.io/img/examples/generative/adain/adain_25_0.png)

* * *

Conclusion
----------

Adaptive Instance Normalization allows arbitrary style transfer in real time. It is also important to note that the novel proposition of the authors is to achieve this only by aligning the statistical features (mean and standard deviation) of the style and the content images.

_Note_: AdaIN also serves as the base for [Style-GANs](https://arxiv.org/abs/1812.04948)
.

* * *

Reference
---------

*   [TF implementation](https://github.com/ftokarev/tf-adain)
    

* * *

Acknowledgement
---------------

We thank [Luke Wood](https://lukewood.xyz/)
 for his detailed review.

* * *

Relevant Chapters from Deep Learning with Python
------------------------------------------------

*   [Chapter 17: Image generation](https://deeplearningwithpython.io/chapters/chapter17_image-generation)
    

[Neural Style Transfer with AdaIN](https://keras.io/examples/generative/adain/#neural-style-transfer-with-adain)

[Introduction](https://keras.io/examples/generative/adain/#introduction)

[Setup](https://keras.io/examples/generative/adain/#setup)

[Style transfer sample gallery](https://keras.io/examples/generative/adain/#style-transfer-sample-gallery)

[Downloading the dataset from Kaggle](https://keras.io/examples/generative/adain/#downloading-the-dataset-from-kaggle)

[`PyDataset` pipeline](https://keras.io/examples/generative/adain/#pydataset-pipeline)

[Visualizing the data](https://keras.io/examples/generative/adain/#visualizing-the-data)

[Architecture](https://keras.io/examples/generative/adain/#architecture)

[Encoder](https://keras.io/examples/generative/adain/#encoder)

[Adaptive Instance Normalization](https://keras.io/examples/generative/adain/#adaptive-instance-normalization)

[Decoder](https://keras.io/examples/generative/adain/#decoder)

[Loss functions](https://keras.io/examples/generative/adain/#loss-functions)

[Content Loss](https://keras.io/examples/generative/adain/#content-loss)

[Style Loss](https://keras.io/examples/generative/adain/#style-loss)

[Neural Style Transfer](https://keras.io/examples/generative/adain/#neural-style-transfer)

[Train Monitor callback](https://keras.io/examples/generative/adain/#train-monitor-callback)

[Train the model](https://keras.io/examples/generative/adain/#train-the-model)

[Inference](https://keras.io/examples/generative/adain/#inference)

[Conclusion](https://keras.io/examples/generative/adain/#conclusion)

[Reference](https://keras.io/examples/generative/adain/#reference)

[Acknowledgement](https://keras.io/examples/generative/adain/#acknowledgement)

[Relevant Chapters from Deep Learning with Python](https://keras.io/examples/generative/adain/#relevant-chapters-from-deep-learning-with-python)