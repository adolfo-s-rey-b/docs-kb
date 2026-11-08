[NEW: GEMMA 4 NOW IN KERASHUB](https://keras.io/keras_hub/api/models/gemma4/)

A superpower for ML developers
==============================

Keras 3 is the high-level API for building, training, and shipping models on the backend of your choice: JAX, PyTorch, MLX, and more.

[GET STARTED](https://keras.io/getting_started/)
 [TRY GEMMA IN KERASHUB](https://keras.io/keras_hub/)
 [API DOCS](https://keras.io/api/)

![K graphic](https://keras.io/img/k-graphic.png)

Copied

    inputs = keras.Input(shape=(32, 32, 3))
    x = layers.Conv2D(32, 3, activation="relu")(inputs)
    x = layers.Conv2D(64, 3, activation="relu")(x)
    residual = x = layers.MaxPooling2D(3)(x)
    
    x = layers.Conv2D(64, 3, padding="same")(x)
    x = layers.Activation("relu")(x)
    x = layers.Conv2D(64, 3, padding="same")(x)
    x = layers.Activation("relu")(x)
    x = x + residual
    
    x = layers.Conv2D(64, 3, activation="relu")(x)
    x = layers.GlobalAveragePooling2D()(x)
    outputs = layers.Dense(10, activation="softmax")(x)
    
    model = keras.Model(inputs, outputs, name="mini_resnet")
    keras.utils.plot_model(model, "mini_resnet.png")
    model.fit(dataset, epochs=10)

[Run quickstart](https://colab.research.google.com/github/keras-team/keras-io/blob/master/quickstarts/keras_quickstart.ipynb)

Copied

    causal_lm = keras_hub.models.CausalLM.from_preset(
      "gemma4_instruct_2b",
      dtype="bfloat16",
    )
    prompt = """<|turn>user
    Write python code to print the first 100 primes.<turn|>
    <|turn>model
    """
    text_output = causal_lm.generate(prompt, max_length=512)
    
    text_to_image = keras_hub.models.TextToImage.from_preset(
        "stable_diffusion_3_medium",
        dtype="float16",
    )
    prompt = "Astronaut in a jungle, detailed"
    image_output = text_to_image.generate(prompt)

[Run quickstart](https://colab.research.google.com/github/keras-team/keras-io/blob/master/quickstarts/keras_hub_quickstart.ipynb)

![Backend logos](https://keras.io/img/logo-row.png)

Welcome to multi-framework machine learning
-------------------------------------------

With its multi-backend approach, Keras gives you the freedom to work with JAX, TensorFlow, and PyTorch. Build models that can move seamlessly across these frameworks and leverage the strengths of each ecosystem.

[GET STARTED](https://keras.io/getting_started/)

Developer Guides
----------------

[VIEW ALL](https://keras.io/guides/)

Copied

    inputs = keras.Input(shape=(28, 28, 1))
    x = inputs
    x = layers.Conv2D(16, 3, activation="relu")(x)
    x = layers.Conv2D(32, 3, activation="relu")(x)
    x = layers.MaxPooling2D(3)(x)
    x = layers.Conv2D(32, 3, activation="relu")(x)
    x = layers.Conv2D(16, 3, activation="relu")(x)
    x = layers.GlobalMaxPooling2D()(x)
    x = layers.Dropout(0.5)(x)
    outputs = layers.Dense(10)(x)
    
    model = keras.Model(inputs, outputs)
    model.summary()

### The Functional API

Starting from the beginning and learn how to build models using the functional building pattern.

[VIEW GUIDE](https://keras.io/guides/functional_api/)

Copied

    model.compile(
        optimizer="rmsprop",
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )
    
    history = model.fit(
        x_train,
        y_train,
        batch_size=64,
        epochs=2,
        validation_data=(x_val, y_val),
    )

### Training & evaluation with the built-in methods

Train and evaluate your model using model.fit(...).

[VIEW GUIDE](https://keras.io/guides/training_with_built_in_methods/)

Copied

    class MLPBlock(keras.layers.Layer):
        def __init__(self):
            super().__init__()
            self.dense_1 = layers.Dense(32)
            self.dense_2 = layers.Dense(32)
            self.dense_3 = layers.Dense(1)
    
        def call(self, inputs):
            x = self.dense_1(inputs)
            x = keras.activations.relu(x)
            x = self.dense_2(x)
            x = keras.activations.relu(x)
            return self.dense_3(x)

### Making new layers and models via subclassing

Learn how to customize your model via subclassing Keras layers.

[VIEW GUIDE](https://keras.io/guides/making_new_layers_and_models_via_subclassing/)

[VIEW ALL](https://keras.io/guides/)

KerasHub
--------

The KerasHub library provides Keras 3 implementations of popular model architectures, paired with a collection of pretrained checkpoints available on Kaggle Models. Models can be used for both training and inference, on any of the TensorFlow, JAX, and PyTorch backends.

[SEE ALL](https://keras.io/keras_hub/)

#### GEMMA 4

Google’s family of open multimodal and agentic models built from the same research and technology used to create Gemini.

[VIEW DOCUMENTATION](https://keras.io/keras_hub/api/models/gemma4/)
 [KAGGLE DETAILS](https://www.kaggle.com/models/keras/gemma4)

#### QWEN 3.8

Alibaba’s flagship open-weight multimodal and reasoning models, excelling at coding, math, and agentic workflows.

[VIEW DOCUMENTATION](https://keras.io/keras_hub/api/models/qwen3_5/)
 [KAGGLE DETAILS](https://www.kaggle.com/models/keras/qwen3-8)

#### GPT-OSS

OpenAI’s open-weight Mixture-of-Experts reasoning models built for high-efficiency text generation across 128k context.

[VIEW DOCUMENTATION](https://keras.io/keras_hub/api/models/gpt_oss/)
 [KAGGLE DETAILS](https://www.kaggle.com/models/keras/gpt-oss)

#### MISTRAL

Open-weight generative language models from the French company Mistral AI, making frontier models accessible to all.

[VIEW DOCUMENTATION](https://keras.io/keras_hub/api/models/mistral/)
 [KAGGLE DETAILS](https://www.kaggle.com/models/keras/mistral)

[SEE ALL](https://keras.io/keras_hub/)

Code examples
-------------

[VIEW ALL](https://keras.io/examples/)

![eye](https://keras.io/img/vision.png)

### Computer vision

Take a look at our examples for doing image classification, object detection, video processing, and more.

[SEE EXAMPLE](https://keras.io/examples/vision/)

![text](https://keras.io/img/nlp.png)

### Natural Language Processing

We also have many guides for doing NLP including text classification, machine translation, and language modeling.

[SEE EXAMPLE](https://keras.io/examples/nlp/)

![flower](https://keras.io/img/generative.png)

### Generative Deep Learning

Get started with generative deep learning with our wealth of guides involving state-of-the-art diffusion models, GANs, and transformer models.

[SEE EXAMPLE](https://keras.io/examples/generative/)

[VIEW ALL](https://keras.io/examples/)

Trusted for research and production
-----------------------------------

Keras is used by CERN, NASA, NIH, and many more scientific organizations around the world (and yes, Keras is used at the Large Hadron Collider). Keras is used by Waymo to power self-driving vehicles. Keras partners with Kaggle and HuggingFace to meet ML developers in the tools they use daily.

*   ![youtube logo](https://keras.io/img/youtube-logo.png)
*   ![google logo](https://keras.io/img/google-logo.png)
*   ![waymo logo](https://keras.io/img/waymo-logo.png)
*   ![amazon logo](https://keras.io/img/amazon-logo.png)
*   ![spotify logo](https://keras.io/img/spotify-logo.png)
*   ![uber logo](https://keras.io/img/uber-logo.png)
*   ![netflix logo](https://keras.io/img/netflix-logo.png)
*   ![youtube logo](https://keras.io/img/youtube-logo.png)
*   ![google logo](https://keras.io/img/google-logo.png)
*   ![waymo logo](https://keras.io/img/waymo-logo.png)
*   ![amazon logo](https://keras.io/img/amazon-logo.png)
*   ![spotify logo](https://keras.io/img/spotify-logo.png)
*   ![uber logo](https://keras.io/img/uber-logo.png)
*   ![netflix logo](https://keras.io/img/netflix-logo.png)
*   ![youtube logo](https://keras.io/img/youtube-logo.png)
*   ![google logo](https://keras.io/img/google-logo.png)
*   ![waymo logo](https://keras.io/img/waymo-logo.png)
*   ![amazon logo](https://keras.io/img/amazon-logo.png)
*   ![spotify logo](https://keras.io/img/spotify-logo.png)
*   ![uber logo](https://keras.io/img/uber-logo.png)
*   ![netflix logo](https://keras.io/img/netflix-logo.png)

Stay in touch
-------------

Sign up to our mailing list for regular updates and discussions about the Keras ecosystem. Listen in at our community meetings, and follow us on social media!

[JOIN GOOGLE GROUP](https://groups.google.com/g/keras-users?pli=1)
 [JOIN COMMUNITY MEETING](https://calendar.google.com/calendar/u/0/r/eventedit/copy/NGIybm44M3BucGd0aWVua3Q5ODhsM2RldG9fMjAyNTAyMDdUMTkwMDAwWiBjXzg1YWE3YzQ1Yjk1YzJlYmI5MmNlY2YzYmU0NzJjMGYyYmU1M2MxZTMyNjdkMzNhNGQ2NTFkMDMxMTBmYjA1NTNAZw/YWxleC5hYmJvdHRAYnluZC5jb20?scp=ALL)
 [DISCORD](https://discord.com/invite/google-dev-community)
 [GOOGLE AI FORUM](https://discuss.ai.google.dev/c/keras/22)

Contributions welcome!
----------------------

We welcome your code, ideas, and feedback as we continue to grow. Visit our roadmap, contribution guide or GitHub for more information.

[VIEW ROADMAP](https://github.com/keras-team/keras/issues/19519)
 [CONTRIBUTION GUIDE](https://github.com/keras-team/keras/issues/18442)
 [GITHUB](https://github.com/keras-team)