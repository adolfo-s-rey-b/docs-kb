None

[KerasHub: Pretrained Models](https://keras.io/keras_hub/)

[Getting started](https://keras.io/keras_hub/getting_started/)
 [Developer guides](https://keras.io/keras_hub/guides/)
 [Uploading Models](https://keras.io/keras_hub/guides/upload/)
 [Stable Diffusion 3](https://keras.io/keras_hub/guides/stable_diffusion_3_in_keras_hub/)
 [Segment Anything](https://keras.io/keras_hub/guides/segment_anything_in_keras_hub/)
 [Image Classification](https://keras.io/keras_hub/guides/classification_with_keras_hub/)
 [Semantic Segmentation](https://keras.io/keras_hub/guides/semantic_segmentation_deeplab_v3/)
 [Object Detection Fine-tuning with KerasHub](https://keras.io/keras_hub/guides/object_detection_retinanet/)
 [Pretraining a Transformer from scratch](https://keras.io/keras_hub/guides/transformer_pretraining/)
 [Loading Hugging Face Transformers Checkpoints](https://keras.io/keras_hub/guides/hugging_face_keras_integration/)
 [Function Calling with KerasHub models](https://keras.io/keras_hub/guides/function_calling_with_keras_hub/)
 [RAG Pipeline with KerasHub](https://keras.io/keras_hub/guides/rag_pipeline_with_keras_hub/)
 [Native Function Calling with FunctionGemma](https://keras.io/keras_hub/guides/function_gemma_with_keras/)
 [Multimodal and Agentic Workflows with Gemma 4 in KerasHub](https://keras.io/keras_hub/guides/gemma4_multimodal_and_agentic_workflows/)
 [Serving KerasHub models with vLLM on TPU](https://keras.io/keras_hub/guides/serving_with_vllm/)
 [API documentation](https://keras.io/keras_hub/api/)
 [Pretrained models list](https://keras.io/keras_hub/presets/)

► [KerasHub: Pretrained Models](https://keras.io/keras_hub/)
 / [Developer guides](https://keras.io/keras_hub/guides/)
 / Uploading Models with KerasHub

Uploading Models with KerasHub
==============================

**Author:** [Samaneh Saadat](https://github.com/SamanehSaadat/)
, [Matthew Watson](https://github.com/mattdangerw/)
  
**Date created:** 2024/04/29  
**Last modified:** 2024/04/29  
**Description:** An introduction on how to upload a fine-tuned KerasHub model to model hubs.

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/guides/ipynb/keras_hub/upload.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/guides/keras_hub/upload.py)

Introduction
============

Fine-tuning a machine learning model can yield impressive results for specific tasks. Uploading your fine-tuned model to a model hub allows you to share it with the broader community. By sharing your models, you'll enhance accessibility for other researchers and developers, making your contributions an integral part of the machine learning landscape. This can also streamline the integration of your model into real-world applications.

This guide walks you through how to upload your fine-tuned models to popular model hubs such as [Kaggle Models](https://www.kaggle.com/models)
 and [Hugging Face Hub](https://huggingface.co/models)
.

Setup
=====

Let's start by installing and importing all the libraries we need. We use KerasHub for this guide.

Copied!

`!pip install -q --upgrade keras-hub huggingface-hub kagglehub`

Copied!

`import os  os.environ["KERAS_BACKEND"] = "jax"  import keras_hub`

Data
====

We can use the IMDB reviews dataset for this guide. Let's load the dataset from `tensorflow_dataset`.

Copied!

`import tensorflow_datasets as tfds  imdb_train, imdb_test = tfds.load(     "imdb_reviews",     split=["train", "test"],     as_supervised=True,     batch_size=4, )`

We only use a small subset of the training samples to make the guide run faster. However, if you need a higher quality model, consider using a larger number of training samples.

Copied!

`imdb_train = imdb_train.take(100)`

Task Upload
===========

A [`keras_hub.models.Task`](https://keras.io/keras_hub/api/base_classes/task#task-class)
, wraps a [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 and a [`keras_hub.models.Preprocessor`](https://keras.io/keras_hub/api/base_classes/preprocessor#preprocessor-class)
 to create a model that can be directly used for training, fine-tuning, and prediction for a given text problem. In this section, we explain how to create a `Task`, fine-tune and upload it to a model hub.

* * *

Load Model
----------

If you want to build a Causal LM based on a base model, simply call [`keras_hub.models.CausalLM.from_preset`](https://keras.io/keras_hub/api/base_classes/causal_lm#frompreset-method)
 and pass a built-in preset identifier.

Copied!

`causal_lm = keras_hub.models.CausalLM.from_preset("gpt2_base_en")`

`Downloading from https://www.kaggle.com/api/v1/models/keras/gpt2/keras/gpt2_base_en/2/download/task.json...  Downloading from https://www.kaggle.com/api/v1/models/keras/gpt2/keras/gpt2_base_en/2/download/preprocessor.json...`

* * *

Fine-tune Model
---------------

After loading the model, you can call `.fit()` on the model to fine-tune it. Here, we fine-tune the model on the IMDB reviews which makes the model movie domain-specific.

Copied!

`# Drop labels and keep the review text only for the Causal LM. imdb_train_reviews = imdb_train.map(lambda x, y: x)  # Fine-tune the Causal LM. causal_lm.fit(imdb_train_reviews)`

100/100 ━━━━━━━━━━━━━━━━━━━━ 151s 1s/step - loss: 1.0198 - sparse\_categorical\_accuracy: 0.3271

* * *

Save the Model Locally
----------------------

To upload a model, you need to first save the model locally using `save_to_preset`.

Copied!

`preset_dir = "./gpt2_imdb" causal_lm.save_to_preset(preset_dir)`

Let's see the saved files.

Copied!

`os.listdir(preset_dir)`

`['preprocessor.json',  'tokenizer.json',  'task.json',  'model.weights.h5',  'config.json',  'metadata.json',  'assets']`

### Load a Locally Saved Model

A model that is saved to a local preset can be loaded using `from_preset`. What you save in, is what you get back out.

Copied!

`causal_lm = keras_hub.models.CausalLM.from_preset(preset_dir)`

You can also load the [`keras_hub.models.Backbone`](https://keras.io/keras_hub/api/base_classes/backbone#backbone-class)
 and `keras_hub.models.Tokenizer` objects from this preset directory. Note that these objects are equivalent to `causal_lm.backbone` and `causal_lm.preprocessor.tokenizer` above.

Copied!

`backbone = keras_hub.models.Backbone.from_preset(preset_dir) tokenizer = keras_hub.models.Tokenizer.from_preset(preset_dir)`

* * *

Upload the Model to a Model Hub
-------------------------------

After saving a preset to a directory, this directory can be uploaded to a model hub such as Kaggle or Hugging Face directly from the KerasHub library. To upload the model to Kaggle, the URI must start with `kaggle://` and to upload to Hugging Face, it should start with `hf://`.

### Upload to Kaggle

To upload a model to Kaggle, first, we need to authenticate with Kaggle. This can in one of the following ways: 1. Set environment variables `KAGGLE_USERNAME` and `KAGGLE_KEY`. 2. Provide a local `~/.kaggle/kaggle.json`. 3. Call `kagglehub.login()`.

Let's make sure we are logged in before continuing.

Copied!

`import kagglehub  if "KAGGLE_USERNAME" not in os.environ or "KAGGLE_KEY" not in os.environ:     kagglehub.login()`

To upload a model we can use `keras_hub.upload_preset(uri, preset_dir)` API where `uri` has the format of `kaggle://<KAGGLE_USERNAME>/<MODEL>/Keras/<VARIATION>` for uploading to Kaggle and `preset_dir` is the directory that the model is saved in.

Running the following uploads the model that is saved in `preset_dir` to Kaggle:

Copied!

`kaggle_username = kagglehub.whoami()["username"] kaggle_uri = f"kaggle://{kaggle_username}/gpt2/keras/gpt2_imdb" keras_hub.upload_preset(kaggle_uri, preset_dir)`

`Upload successful: preprocessor.json (834B) Upload successful: tokenizer.json (322B) Upload successful: task.json (2KB) Upload successful: model.weights.h5 (475MB) Upload successful: config.json (431B) Upload successful: metadata.json (142B) Upload successful: merges.txt (446KB) Upload successful: vocabulary.json (1018KB)  Your model instance version has been created.`

### Upload to Hugging Face

To upload a model to Hugging Face, first, we need to authenticate with Hugging Face. This can in one of the following ways: 1. Set environment variables `HF_USERNAME` and `HF_TOKEN`. 2. Call `huggingface_hub.notebook_login()`.

Let's make sure we are logged in before coninuing.

Copied!

`import huggingface_hub  if "HF_USERNAME" not in os.environ or "HF_TOKEN" not in os.environ:     huggingface_hub.notebook_login()`

`keras_hub.upload_preset(uri, preset_dir)` can be used to upload a model to Hugging Face if `uri` has the format of `kaggle://<HF_USERNAME>/<MODEL>`.

Running the following uploads the model that is saved in `preset_dir` to Hugging Face:

Copied!

`hf_username = huggingface_hub.whoami()["name"] hf_uri = f"hf://{hf_username}/gpt2_imdb" keras_hub.upload_preset(hf_uri, preset_dir)`

* * *

Load a User Uploaded Model
--------------------------

After verifying that the model is uploaded to Kaggle, we can load the model by calling `from_preset`.

Copied!

`causal_lm = keras_hub.models.CausalLM.from_preset(     f"kaggle://{kaggle_username}/gpt2/keras/gpt2_imdb" )`

We can also load the model uploaded to Hugging Face by calling `from_preset`.

Copied!

`causal_lm = keras_hub.models.CausalLM.from_preset(f"hf://{hf_username}/gpt2_imdb")`

Classifier Upload
=================

Uploading a classifier model is similar to Causal LM upload. To upload the fine-tuned model, first, the model should be saved to a local directory using `save_to_preset` API and then it can be uploaded via [`keras_hub.upload_preset`](https://keras.io/keras_hub/api/base_classes/upload_preset#uploadpreset-function)
.

Copied!

`# Load the base model. classifier = keras_hub.models.Classifier.from_preset(     "bert_tiny_en_uncased", num_classes=2 )  # Fine-tune the classifier. classifier.fit(imdb_train)  # Save the model to a local preset directory. preset_dir = "./bert_tiny_imdb" classifier.save_to_preset(preset_dir)  # Upload to Kaggle. keras_hub.upload_preset(     f"kaggle://{kaggle_username}/bert/keras/bert_tiny_imdb", preset_dir )`

100/100 ━━━━━━━━━━━━━━━━━━━━ 7s 31ms/step - loss: 0.6975 - sparse\_categorical\_accuracy: 0.5164

`Upload successful: preprocessor.json (947B) Upload successful: tokenizer.json (461B) Upload successful: task.json (2KB) Upload successful: task.weights.h5 (50MB) Upload successful: model.weights.h5 (17MB) Upload successful: config.json (454B) Upload successful: metadata.json (140B) Upload successful: vocabulary.txt (226KB)  Your model instance version has been created.`

After verifying that the model is uploaded to Kaggle, we can load the model by calling `from_preset`.

Copied!

`classifier = keras_hub.models.Classifier.from_preset(     f"kaggle://{kaggle_username}/bert/keras/bert_tiny_imdb" )`

[Uploading Models with KerasHub](https://keras.io/keras_hub/guides/upload/#uploading-models-with-kerashub)

[Introduction](https://keras.io/keras_hub/guides/upload/#introduction)

[Setup](https://keras.io/keras_hub/guides/upload/#setup)

[Data](https://keras.io/keras_hub/guides/upload/#data)

[Task Upload](https://keras.io/keras_hub/guides/upload/#task-upload)

[Load Model](https://keras.io/keras_hub/guides/upload/#load-model)

[Fine-tune Model](https://keras.io/keras_hub/guides/upload/#finetune-model)

[Save the Model Locally](https://keras.io/keras_hub/guides/upload/#save-the-model-locally)

[Load a Locally Saved Model](https://keras.io/keras_hub/guides/upload/#load-a-locally-saved-model)

[Upload the Model to a Model Hub](https://keras.io/keras_hub/guides/upload/#upload-the-model-to-a-model-hub)

[Upload to Kaggle](https://keras.io/keras_hub/guides/upload/#upload-to-kaggle)

[Upload to Hugging Face](https://keras.io/keras_hub/guides/upload/#upload-to-hugging-face)

[Load a User Uploaded Model](https://keras.io/keras_hub/guides/upload/#load-a-user-uploaded-model)

[Classifier Upload](https://keras.io/keras_hub/guides/upload/#classifier-upload)