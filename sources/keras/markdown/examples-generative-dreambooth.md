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
 / DreamBooth

DreamBooth
==========

**Author:** [Sayak Paul](https://twitter.com/RisingSayak)
, [Chansung Park](https://twitter.com/algo_diver)
  
**Date created:** 2023/02/01  
**Last modified:** 2026/03/06  
**Description:** Implementing DreamBooth.

ⓘ This example uses Keras 3

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/generative/ipynb/dreambooth.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/examples/generative/dreambooth.py)

* * *

Introduction
------------

In this example, we implement DreamBooth, a fine-tuning technique to teach new visual concepts to text-conditioned Diffusion models with just 3 - 5 images. DreamBooth was proposed in [DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation](https://arxiv.org/abs/2208.12242)
 by Ruiz et al.

DreamBooth, in a sense, is similar to the [traditional way of fine-tuning a text-conditioned Diffusion model except](https://keras.io/examples/generative/finetune_stable_diffusion/)
 for a few gotchas. This example assumes that you have basic familiarity with Diffusion models and how to fine-tune them. Here are some reference examples that might help you to get familiarized quickly:

*   [Teach StableDiffusion new concepts via Textual Inversion](https://keras.io/examples/generative/fine_tune_via_textual_inversion/)
    
*   [Fine-tuning Stable Diffusion](https://keras.io/examples/generative/finetune_stable_diffusion/)
    

This example is resource-intensive. For reliable execution, use a GPU with at least 80 GB of VRAM.

* * *

Initial imports
---------------

Copied!

`import math  import keras import keras_hub import matplotlib.pyplot as plt import numpy as np from imutils import paths`

`WARNING: All log messages before absl::InitializeLog() is called are written to STDERR E0000 00:00:1775110433.373311    5778 cuda_dnn.cc:8579] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered E0000 00:00:1775110433.377650    5778 cuda_blas.cc:1407] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered W0000 00:00:1775110433.388657    5778 computation_placer.cc:177] computation placer already registered. Please check linkage and avoid linking the same target more than once. W0000 00:00:1775110433.388668    5778 computation_placer.cc:177] computation placer already registered. Please check linkage and avoid linking the same target more than once. W0000 00:00:1775110433.388669    5778 computation_placer.cc:177] computation placer already registered. Please check linkage and avoid linking the same target more than once. W0000 00:00:1775110433.388671    5778 computation_placer.cc:177] computation placer already registered. Please check linkage and avoid linking the same target more than once.`

* * *

Usage of DreamBooth
-------------------

... is very versatile. By teaching Stable Diffusion about your favorite visual concepts, you can

*   Recontextualize objects in interesting ways:
    
    ![](https://i.imgur.com/4Da9ozw.png)
    

*   Generate artistic renderings of the underlying visual concept:
    
    ![](https://i.imgur.com/nI2N8bI.png)
    

And many other applications. We welcome you to check out the original [DreamBooth paper](https://arxiv.org/abs/2208.12242)
 in this regard.

Copied!

`instance_images_root = keras.utils.get_file(     origin="https://huggingface.co/datasets/sayakpaul/sample-datasets/resolve/main/instance-images.tar.gz",     untar=True, ) class_images_root = keras.utils.get_file(     origin="https://huggingface.co/datasets/sayakpaul/sample-datasets/resolve/main/class-images.tar.gz",     untar=True, )`

Downloading data from https://huggingface.co/datasets/sayakpaul/sample-datasets/resolve/main/instance-images.tar.gz 5556967/5556967 ━━━━━━━━━━━━━━━━━━━━ 1s 0us/step Downloading data from https://huggingface.co/datasets/sayakpaul/sample-datasets/resolve/main/class-images.tar.gz 9093120/9093120 ━━━━━━━━━━━━━━━━━━━━ 1s 0us/step

* * *

Visualize images
----------------

First, let's load the image paths.

Copied!

`instance_image_paths = list(paths.list_images(instance_images_root)) class_image_paths = list(paths.list_images(class_images_root))`

Then we load the images from the paths.

Copied!

`def load_images(image_paths):     images = [np.array(keras.utils.load_img(path)) for path in image_paths]     return images`

And then we make use a utility function to plot the loaded images.

Copied!

`def plot_images(images, title=None):     plt.figure(figsize=(20, 20))     for i in range(len(images)):         ax = plt.subplot(1, len(images), i + 1)         if title is not None:             plt.title(title)         plt.imshow(images[i])         plt.axis("off")`

**Instance images**:

Copied!

`plot_images(load_images(instance_image_paths[:5]))`

![png](https://keras.io/examples/generative/img/dreambooth/dreambooth_14_0.png)

**Class images**:

Copied!

`plot_images(load_images(class_image_paths[:5]))`

![png](https://keras.io/examples/generative/img/dreambooth/dreambooth_16_0.png)

* * *

Prepare datasets
----------------

Dataset preparation includes two stages: (1): preparing the captions, (2) processing the images.

### Prepare the captions

Copied!

`new_instance_image_paths = [     instance_image_paths[index % len(instance_image_paths)]     for index in range(len(class_image_paths)) ] instance_count = len(new_instance_image_paths) class_count = len(class_image_paths)  unique_id = "sks" class_label = "dog"  instance_prompt = f"a photo of {unique_id} {class_label}" class_prompt = f"a photo of {class_label}"`

Next, we embed the prompts to save some compute.

Copied!

`print("Loading Stable Diffusion 3 (will be reused for training)...") sd3_backbone = keras_hub.models.StableDiffusion3Backbone.from_preset(     "stable_diffusion_3_medium",     image_shape=(512, 512, 3), ) sd3_preprocessor = keras_hub.models.StableDiffusion3TextToImagePreprocessor.from_preset(     "stable_diffusion_3_medium" )  unique_prompts = [instance_prompt, class_prompt] print(     f"Encoding {len(unique_prompts)} unique prompts (instead of {instance_count + class_count})..." )  token_ids = sd3_preprocessor.generate_preprocess(unique_prompts) negative_token_ids = sd3_preprocessor.generate_preprocess(["", ""])  (     positive_embeddings,     _,     positive_pooled,     _, ) = sd3_backbone.encode_text_step(token_ids, negative_token_ids)  instance_embedding = positive_embeddings[0:1] class_embedding = positive_embeddings[1:2] instance_pooled = positive_pooled[0:1] class_pooled_single = positive_pooled[1:2]  def repeat_embedding(embedding, count):     return np.repeat(embedding, count, axis=0)  instance_embedded_texts = repeat_embedding(instance_embedding, instance_count) class_embedded_texts = repeat_embedding(class_embedding, class_count) instance_pooled_embeddings = repeat_embedding(instance_pooled, instance_count) class_pooled_embeddings = repeat_embedding(class_pooled_single, class_count)  print(     f"Text embedding shapes: {instance_embedded_texts.shape}, {class_embedded_texts.shape}" ) print(     f"Pooled embedding shapes: {instance_pooled_embeddings.shape}, {class_pooled_embeddings.shape}" )`

Loading Stable Diffusion 3 (will be reused for training)... Downloading to /home/kharshith/.cache/kagglehub/models/keras/stablediffusion3/keras/stable\_diffusion\_3\_medium/5/config.json...

0%███████████████████████████████████████████████████████████████████████████████████████100%| 4.19k/4.19k \[00:00<00:00, 9.05MB/s\]

Downloading to /home/kharshith/.cache/kagglehub/models/keras/stablediffusion3/keras/stable\_diffusion\_3\_medium/5/model.weights.h5...

0%███████████████████████████████████████████████████████████████████████████████████████100%| 5.57G/5.57G \[00:43<00:00, 137MB/s\]

Downloading to /home/kharshith/.cache/kagglehub/models/keras/stablediffusion3/keras/stable\_diffusion\_3\_medium/5/preprocessor.json...

0%███████████████████████████████████████████████████████████████████████████████████████100%| 4.08k/4.08k \[00:00<00:00, 14.2MB/s\]

Downloading to /home/kharshith/.cache/kagglehub/models/keras/stablediffusion3/keras/stable\_diffusion\_3\_medium/5/assets/clip\_l\_tokenizer/vocabulary.json...

0%███████████████████████████████████████████████████████████████████████████████████████100%| 976k/976k \[00:00<00:00, 5.01MB/s\]

Downloading to /home/kharshith/.cache/kagglehub/models/keras/stablediffusion3/keras/stable\_diffusion\_3\_medium/5/assets/clip\_l\_tokenizer/merges.txt...

0%███████████████████████████████████████████████████████████████████████████████████████100%| 512k/512k \[00:00<00:00, 3.07MB/s\]

Downloading to /home/kharshith/.cache/kagglehub/models/keras/stablediffusion3/keras/stable\_diffusion\_3\_medium/5/assets/clip\_g\_tokenizer/vocabulary.json...

0%███████████████████████████████████████████████████████████████████████████████████████100%| 976k/976k \[00:00<00:00, 5.04MB/s\]

Downloading to /home/kharshith/.cache/kagglehub/models/keras/stablediffusion3/keras/stable\_diffusion\_3\_medium/5/assets/clip\_g\_tokenizer/merges.txt...

0%███████████████████████████████████████████████████████████████████████████████████████100%| 512k/512k \[00:00<00:00, 3.50MB/s\]

Encoding 2 unique prompts (instead of 400)... Text embedding shapes: (200, 154, 4096), (200, 154, 4096)  
Pooled embedding shapes: (200, 2048), (200, 2048)

* * *

Prepare the images
------------------

Copied!

`resolution = 512  augmenter = keras.Sequential(     layers=[         keras.layers.CenterCrop(resolution, resolution),         keras.layers.RandomFlip(),         keras.layers.Rescaling(scale=1.0 / 127.5, offset=-1),     ] )  class DreamBoothDataset(keras.utils.PyDataset):     """Backend-agnostic dataset for DreamBooth training.      This dataset handles both instance and class images for prior preservation.     """      def __init__(         self,         instance_image_paths,         class_image_paths,         instance_embedded_texts,         class_embedded_texts,         instance_pooled_embeddings,         class_pooled_embeddings,         augmenter,         batch_size=1,         shuffle=True,         seed=42,         **kwargs,     ):         super().__init__(**kwargs)         self.instance_image_paths = instance_image_paths         self.class_image_paths = class_image_paths         self.instance_embedded_texts = instance_embedded_texts         self.class_embedded_texts = class_embedded_texts         self.instance_pooled_embeddings = instance_pooled_embeddings         self.class_pooled_embeddings = class_pooled_embeddings         self.augmenter = augmenter         self.batch_size = batch_size         self.shuffle = shuffle         self.seed = seed         self.rng = np.random.default_rng(seed)          self.num_samples = len(class_image_paths)          self.on_epoch_end()      def __len__(self):         return int(np.ceil(self.num_samples / self.batch_size))      def on_epoch_end(self):         """Shuffle indices at end of epoch if shuffle=True."""         self.indices = np.arange(self.num_samples)         if self.shuffle:             self.rng.shuffle(self.indices)      def _get_batch_indices(self, batch_indices, num_items=None):         if num_items is None:             return batch_indices         return [index % num_items for index in batch_indices]      def _load_batch_images(self, image_paths, batch_indices, repeat=False):         indices = self._get_batch_indices(             batch_indices, len(image_paths) if repeat else None         )         images = [             keras.utils.img_to_array(                 keras.utils.load_img(                     image_paths[index], target_size=(resolution, resolution)                 )             )             for index in indices         ]         return np.array(images)      def _gather_batch(self, values, batch_indices, repeat=False):         indices = self._get_batch_indices(             batch_indices, len(values) if repeat else None         )         return np.array([values[index] for index in indices])      def __getitem__(self, idx):         """Generate one batch of data."""         batch_indices = self.indices[             idx * self.batch_size : (idx + 1) * self.batch_size         ]          instance_images = self._load_batch_images(             self.instance_image_paths, batch_indices, repeat=True         )         class_images = self._load_batch_images(self.class_image_paths, batch_indices)          instance_embeds = self._gather_batch(             self.instance_embedded_texts, batch_indices, repeat=True         )         class_embeds = self._gather_batch(self.class_embedded_texts, batch_indices)          instance_pooled = self._gather_batch(             self.instance_pooled_embeddings, batch_indices, repeat=True         )         class_pooled = self._gather_batch(self.class_pooled_embeddings, batch_indices)          instance_images = self.augmenter(instance_images, training=True)         class_images = self.augmenter(class_images, training=True)          instance_batch = {             "instance_images": instance_images,             "instance_embedded_texts": instance_embeds,             "instance_pooled_embeddings": instance_pooled,         }         class_batch = {             "class_images": class_images,             "class_embedded_texts": class_embeds,             "class_pooled_embeddings": class_pooled,         }          return (instance_batch, class_batch)`

* * *

Assemble dataset
----------------

Copied!

`train_dataset = DreamBoothDataset(     instance_image_paths=new_instance_image_paths,     class_image_paths=class_image_paths,     instance_embedded_texts=instance_embedded_texts,     class_embedded_texts=class_embedded_texts,     instance_pooled_embeddings=instance_pooled_embeddings,     class_pooled_embeddings=class_pooled_embeddings,     augmenter=augmenter,     batch_size=1,     shuffle=True,     workers=2,     use_multiprocessing=False, )`

* * *

Check shapes
------------

Now that the dataset has been prepared, let's quickly check what's inside it.

Copied!

`sample_batch = next(iter(train_dataset)) print(sample_batch[0].keys(), sample_batch[1].keys())  for k in sample_batch[0]:     print(k, sample_batch[0][k].shape)  for k in sample_batch[1]:     print(k, sample_batch[1][k].shape)`

dict\_keys(\['instance\_images', 'instance\_embedded\_texts', 'instance\_pooled\_embeddings'\]) dict\_keys(\['class\_images', 'class\_embedded\_texts', 'class\_pooled\_embeddings'\])  
instance\_images (1, 512, 512, 3)  
instance\_embedded\_texts (1, 154, 4096)  
instance\_pooled\_embeddings (1, 2048)  
class\_images (1, 512, 512, 3)  
class\_embedded\_texts (1, 154, 4096)  
class\_pooled\_embeddings (1, 2048)

During training, we make use of these keys to gather the images and text embeddings and concat them accordingly.

* * *

DreamBooth training loop
------------------------

Our DreamBooth training loop is very much inspired by [this script](https://github.com/huggingface/diffusers/blob/main/examples/dreambooth/train_dreambooth.py)
 provided by the Diffusers team at Hugging Face. However, there is an important difference to note. We only fine-tune the diffusion model (the component responsible for predicting noise / velocity) and don't fine-tune the text encoder in this example. If you're looking for an implementation that also performs the additional fine-tuning of the text encoder, refer to [this repository](https://github.com/sayakpaul/dreambooth-keras/)
.

Copied!

`class DreamBoothTrainer(keras.Model):     def __init__(         self,         diffusion_model,         vae,         backbone,         noise_scheduler,         use_mixed_precision=False,         prior_loss_weight=1.0,         max_grad_norm=1.0,         **kwargs,     ):         super().__init__(**kwargs)          self.diffusion_model = diffusion_model         self.vae = vae         self.backbone = backbone         self.noise_scheduler = noise_scheduler         self.prior_loss_weight = prior_loss_weight         self.max_grad_norm = max_grad_norm          self.use_mixed_precision = use_mixed_precision         self.vae.trainable = False         self.backbone.trainable = False         self.diffusion_model.trainable = True      def call(self, inputs):         return inputs      def compute_loss(self, x, y, y_pred, sample_weight):         """Backend-agnostic loss computation override.          The default train_step calls this method inside a gradient recording scope         (e.g., GradientTape for TF, Autograd for Torch), so we don't need to manually         handle gradients.         """         instance_batch = x         class_batch = y          instance_images = instance_batch["instance_images"]         instance_embedded_text = instance_batch["instance_embedded_texts"]         instance_pooled = instance_batch["instance_pooled_embeddings"]         class_images = class_batch["class_images"]         class_embedded_text = class_batch["class_embedded_texts"]         class_pooled = class_batch["class_pooled_embeddings"]          images = keras.ops.concatenate([instance_images, class_images], axis=0)         embedded_texts = keras.ops.concatenate(             [instance_embedded_text, class_embedded_text], axis=0         )         pooled_embeddings = keras.ops.concatenate(             [instance_pooled, class_pooled], axis=0         )         batch_size = keras.ops.shape(images)[0]          return self._compute_dreambooth_loss(             images, embedded_texts, pooled_embeddings, batch_size         )      def _compute_dreambooth_loss(         self, images, embedded_texts, pooled_embeddings, batch_size     ):         """Internal logic for DreamBooth loss (Flow Matching)."""         latents = self.backbone.encode_image_step(images)          noise = keras.random.normal(keras.ops.shape(latents))          timesteps = keras.random.uniform(             shape=(batch_size,),             minval=0,             maxval=1,             dtype="float32",         )          noisy_latents = keras.ops.add(             keras.ops.multiply(                 keras.ops.subtract(1.0, keras.ops.reshape(timesteps, (-1, 1, 1, 1))),                 latents,             ),             keras.ops.multiply(keras.ops.reshape(timesteps, (-1, 1, 1, 1)), noise),         )          target = keras.ops.subtract(noise, latents)          model_pred = self.diffusion_model(             {                 "latent": noisy_latents,                 "context": embedded_texts,                 "pooled_projection": pooled_embeddings,                 "timestep": keras.ops.reshape(timesteps, (-1, 1)),             },             training=True,         )          loss = self._compute_split_loss(target, model_pred)         return loss      def _compute_split_loss(self, target, model_pred):         """Compute split loss for instance and class images."""         model_pred, model_pred_prior = keras.ops.split(model_pred, 2, axis=0)         target, target_prior = keras.ops.split(target, 2, axis=0)          target = keras.ops.cast(target, "float32")         model_pred = keras.ops.cast(model_pred, "float32")         target_prior = keras.ops.cast(target_prior, "float32")         model_pred_prior = keras.ops.cast(model_pred_prior, "float32")          loss = keras.ops.mean(keras.ops.square(target - model_pred))         prior_loss = keras.ops.mean(keras.ops.square(target_prior - model_pred_prior))          return loss + self.prior_loss_weight * prior_loss      def save_weights(self, filepath, overwrite=True, save_format=None, options=None):         self.diffusion_model.save_weights(filepath=filepath)      def load_weights(self, filepath, by_name=False, skip_mismatch=False, options=None):         self.diffusion_model.load_weights(filepath=filepath)`

* * *

Trainer initialization
----------------------

Copied!

`use_mp = True  keras.mixed_precision.set_global_policy("mixed_float16")  print("Reusing SD3 backbone from text encoding step...")  diffusion_model = sd3_backbone.diffuser  vae = sd3_backbone.vae`

Reusing SD3 backbone from text encoding step...

* * *

Train!
------

We first calculate the number of epochs, we need to train for.

Copied!

`num_update_steps_per_epoch = len(train_dataset) max_train_steps = 1200 epochs = math.ceil(max_train_steps / num_update_steps_per_epoch) print(f"Training for {epochs} epochs.")`

Training for 6 epochs.

And then we start training!

Copied!

`dreambooth_trainer = DreamBoothTrainer(     diffusion_model=sd3_backbone.diffuser,     vae=sd3_backbone.vae,     backbone=sd3_backbone,     noise_scheduler=None,     use_mixed_precision=use_mp,     prior_loss_weight=1.0, )  learning_rate = 1e-5 optimizer = keras.optimizers.AdamW(     learning_rate=learning_rate,     weight_decay=0.0,     beta_1=0.9,     beta_2=0.999,     epsilon=1e-08,     clipnorm=1.0, )  dreambooth_trainer.compile(optimizer=optimizer, loss="mse")  print("Starting training (resolution: 512x512)...") ckpt_path = "dreambooth-unet.weights.h5" ckpt_callback = keras.callbacks.ModelCheckpoint(     ckpt_path,     save_weights_only=True,     monitor="loss",     mode="min", )  dreambooth_trainer.fit(train_dataset, epochs=epochs, callbacks=[ckpt_callback])`

Starting training (resolution: 512x512)... Epoch 1/6 200/200 ━━━━━━━━━━━━━━━━━━━━ 2037s 10s/step - loss: 0.9379 Epoch 2/6 200/200 ━━━━━━━━━━━━━━━━━━━━ 1962s 10s/step - loss: 0.8031 Epoch 3/6 200/200 ━━━━━━━━━━━━━━━━━━━━ 1964s 10s/step - loss: 0.6908 Epoch 4/6 200/200 ━━━━━━━━━━━━━━━━━━━━ 1972s 10s/step - loss: 0.6907 Epoch 5/6 200/200 ━━━━━━━━━━━━━━━━━━━━ 1971s 10s/step - loss: 0.6913 Epoch 6/6 200/200 ━━━━━━━━━━━━━━━━━━━━ 1970s 10s/step - loss: 0.6932

* * *

Experiments and inference
-------------------------

We ran various experiments with a slightly modified version of this example. Our experiments are based on [this repository](https://github.com/sayakpaul/dreambooth-keras/)
 and are inspired by [this blog post](https://huggingface.co/blog/dreambooth)
 from Hugging Face.

First, let's see how we can use the fine-tuned checkpoint for running inference.

Copied!

`import numpy as np  print("Loading Stable Diffusion 3 with 512x512 resolution (float32)...") dreambooth_model_512 = keras_hub.models.StableDiffusion3TextToImage.from_preset(     "stable_diffusion_3_medium",     image_shape=(512, 512, 3),     dtype="float32", )  print(f"Loading fine-tuned weights from {ckpt_path}...") dreambooth_model_512.backbone.diffuser.load_weights(ckpt_path)`

Loading Stable Diffusion 3 with 512x512 resolution (float32)... Loading fine-tuned weights from dreambooth-unet.weights.h5...

The default number of steps for generating an image with Stable Diffusion 3 is 50. Let's increase it to 100 for potentially better quality.

Copied!

`prompt = f"A photo of {unique_id} {class_label} in a bucket" print(f"Generating images for prompt: '{prompt}'...")  prompts = [prompt] * 3  images_dreamboothed = dreambooth_model_512.generate(prompts, num_steps=100, seed=42)  images_dreamboothed = np.array(images_dreamboothed) if images_dreamboothed.ndim == 3:     images_dreamboothed = np.expand_dims(images_dreamboothed, axis=0)  plot_images(images_dreamboothed, title=prompt)`

Generating images for prompt: 'A photo of sks dog in a bucket'...

![png](https://keras.io/examples/generative/img/dreambooth/dreambooth_40_1.png)

Feel free to experiment with different prompts (don't forget to add the unique identifier and the class label!) to see how the results change. We welcome you to check out our codebase and more experimental results [here](https://github.com/sayakpaul/dreambooth-keras#results)
. You can also read [this blog post](https://huggingface.co/blog/dreambooth)
 to get more ideas.

* * *

Acknowledgements
----------------

*   Thanks to the [DreamBooth example script](https://github.com/huggingface/diffusers/blob/main/examples/dreambooth/train_dreambooth.py)
     provided by Hugging Face which helped us a lot in getting the initial implementation ready quickly.
*   Getting DreamBooth to work on human faces can be challenging. We have compiled some general recommendations [here](https://github.com/sayakpaul/dreambooth-keras#notes-on-preparing-data-for-dreambooth-training-of-faces)
    . Thanks to [Abhishek Thakur](https://no.linkedin.com/in/abhi1thakur)
     for helping with these.

* * *

Relevant Chapters from Deep Learning with Python
------------------------------------------------

*   [Chapter 17: Image generation](https://deeplearningwithpython.io/chapters/chapter17_image-generation)
    

[DreamBooth](https://keras.io/examples/generative/dreambooth/#dreambooth)

[Introduction](https://keras.io/examples/generative/dreambooth/#introduction)

[Initial imports](https://keras.io/examples/generative/dreambooth/#initial-imports)

[Usage of DreamBooth](https://keras.io/examples/generative/dreambooth/#usage-of-dreambooth)

[Visualize images](https://keras.io/examples/generative/dreambooth/#visualize-images)

[Prepare datasets](https://keras.io/examples/generative/dreambooth/#prepare-datasets)

[Prepare the captions](https://keras.io/examples/generative/dreambooth/#prepare-the-captions)

[Prepare the images](https://keras.io/examples/generative/dreambooth/#prepare-the-images)

[Assemble dataset](https://keras.io/examples/generative/dreambooth/#assemble-dataset)

[Check shapes](https://keras.io/examples/generative/dreambooth/#check-shapes)

[DreamBooth training loop](https://keras.io/examples/generative/dreambooth/#dreambooth-training-loop)

[Trainer initialization](https://keras.io/examples/generative/dreambooth/#trainer-initialization)

[Train!](https://keras.io/examples/generative/dreambooth/#train)

[Experiments and inference](https://keras.io/examples/generative/dreambooth/#experiments-and-inference)

[Acknowledgements](https://keras.io/examples/generative/dreambooth/#acknowledgements)

[Relevant Chapters from Deep Learning with Python](https://keras.io/examples/generative/dreambooth/#relevant-chapters-from-deep-learning-with-python)