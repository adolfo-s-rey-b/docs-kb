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
 / Text Generation using FNet

Text Generation using FNet
==========================

**Author:** [Darshan Deshpande](https://twitter.com/getdarshan)
  
**Date created:** 2021/10/05  
**Last modified:** 2026/03/18  
**Description:** FNet transformer for text generation in Keras.

ⓘ This example uses Keras 3

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/generative/ipynb/text_generation_fnet.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/examples/generative/text_generation_fnet.py)

* * *

Introduction
------------

The original transformer implementation (Vaswani et al., 2017) was one of the major breakthroughs in Natural Language Processing, giving rise to important architectures such BERT and GPT. However, the drawback of these architectures is that the self-attention mechanism they use is computationally expensive. The FNet architecture proposes to replace this self-attention attention with a leaner mechanism: a Fourier transformation-based linear mixer for input tokens.

The FNet model was able to achieve 92-97% of BERT's accuracy while training 80% faster on GPUs and almost 70% faster on TPUs. This type of design provides an efficient and small model size, leading to faster inference times.

In this example, we will implement and train this architecture on the Cornell Movie Dialog corpus to show the applicability of this model to text generation.

* * *

Imports
-------

Copied!

`import os  os.environ["KERAS_BACKEND"] = "tensorflow"  # or "jax" , "torch" import keras from keras import layers, ops import tensorflow as tf  # Defining hyperparameters  VOCAB_SIZE = 8192 MAX_SAMPLES = 50000 BUFFER_SIZE = 20000 MAX_LENGTH = 40 EMBED_DIM = 256 LATENT_DIM = 512 NUM_HEADS = 8 BATCH_SIZE = 64`

* * *

Loading data
------------

We will be using the Cornell Dialog Corpus. We will parse the movie conversations into questions and answers sets.

Copied!

`path_to_zip = keras.utils.get_file(     "cornell_movie_dialogs.zip",     origin="http://www.cs.cornell.edu/~cristian/data/cornell_movie_dialogs_corpus.zip",     extract=True, )  path_to_dataset = os.path.join(     os.path.dirname(path_to_zip),     "cornell_movie_dialogs_extracted",     "cornell movie-dialogs corpus", ) path_to_movie_lines = os.path.join(path_to_dataset, "movie_lines.txt") path_to_movie_conversations = os.path.join(path_to_dataset, "movie_conversations.txt")  def load_conversations():     # Helper function for loading the conversation splits     id2line = {}     with open(path_to_movie_lines, errors="ignore") as file:         lines = file.readlines()     for line in lines:         parts = line.replace("\n", "").split(" +++$+++ ")         id2line[parts[0]] = parts[4]      inputs, outputs = [], []     with open(path_to_movie_conversations, "r") as file:         lines = file.readlines()     for line in lines:         parts = line.replace("\n", "").split(" +++$+++ ")         # get conversation in a list of line ID         conversation = [line[1:-1] for line in parts[3][1:-1].split(", ")]         for i in range(len(conversation) - 1):             inputs.append(id2line[conversation[i]])             outputs.append(id2line[conversation[i + 1]])             if len(inputs) >= MAX_SAMPLES:                 return inputs, outputs     return inputs, outputs  questions, answers = load_conversations()  # Splitting training and validation sets  train_dataset = tf.data.Dataset.from_tensor_slices((questions[:40000], answers[:40000])) val_dataset = tf.data.Dataset.from_tensor_slices((questions[40000:], answers[40000:]))`

### Preprocessing and Tokenization

Copied!

`def preprocess_text(sentence):     sentence = tf.strings.lower(sentence)     # Adding a space between the punctuation and the last word to allow better tokenization     sentence = tf.strings.regex_replace(sentence, r"([?.!,])", r" \1 ")     # Replacing multiple continuous spaces with a single space     sentence = tf.strings.regex_replace(sentence, r"\s\s+", " ")     # Replacing non english words with spaces     sentence = tf.strings.regex_replace(sentence, r"[^a-z?.!,]+", " ")     sentence = tf.strings.strip(sentence)     sentence = tf.strings.join(["[start]", sentence, "[end]"], separator=" ")     return sentence  vectorizer = layers.TextVectorization(     VOCAB_SIZE,     standardize=preprocess_text,     output_mode="int",     output_sequence_length=MAX_LENGTH, )  # We will adapt the vectorizer to both the questions and answers # This dataset is batched to parallelize and speed up the process vectorizer.adapt(tf.data.Dataset.from_tensor_slices((questions + answers)).batch(128))`

### Tokenizing and padding sentences using `TextVectorization`

Copied!

`def vectorize_text(inputs, outputs):     inputs, outputs = vectorizer(inputs), vectorizer(outputs)     # One extra padding token to the right to match the output shape     outputs = tf.pad(outputs, [[0, 1]])     return (         {"encoder_inputs": inputs, "decoder_inputs": outputs[:-1]},         outputs[1:],     )  train_dataset = train_dataset.map(vectorize_text, num_parallel_calls=tf.data.AUTOTUNE) val_dataset = val_dataset.map(vectorize_text, num_parallel_calls=tf.data.AUTOTUNE)  train_dataset = (     train_dataset.cache()     .shuffle(BUFFER_SIZE)     .batch(BATCH_SIZE)     .prefetch(tf.data.AUTOTUNE) ) val_dataset = val_dataset.cache().batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)`

* * *

Creating the FNet Encoder
-------------------------

The FNet paper proposes a replacement for the standard attention mechanism used by the Transformer architecture (Vaswani et al., 2017).

![Architecture](https://i.imgur.com/rLg47qU.png)

The outputs of the FFT layer are complex numbers. To avoid dealing with complex layers, only the real part (the magnitude) is extracted.

The dense layers that follow the Fourier transformation act as convolutions applied on the frequency domain.

Copied!

`class FNetEncoder(layers.Layer):     def __init__(self, embed_dim, dense_dim, **kwargs):         super().__init__(**kwargs)         self.embed_dim = embed_dim         self.dense_dim = dense_dim         self.dense_proj = keras.Sequential(             [                 layers.Dense(dense_dim, activation="relu"),                 layers.Dense(embed_dim),             ]         )         self.layernorm_1 = layers.LayerNormalization()         self.layernorm_2 = layers.LayerNormalization()      def call(self, inputs):         # Cast inputs to float32 and create imaginary component         inp_real = ops.cast(inputs, "float32")         inp_imag = ops.zeros_like(inp_real)          # Apply 2D FFT - returns tuple of (real, imaginary)         fft_real, fft_imag = ops.fft((inp_real, inp_imag))         # Use only the real component         proj_input = self.layernorm_1(inputs + fft_real)         proj_output = self.dense_proj(proj_input)         return self.layernorm_2(proj_input + proj_output)`

* * *

Creating the Decoder
--------------------

The decoder architecture remains the same as the one proposed by (Vaswani et al., 2017) in the original transformer architecture, consisting of an embedding, positional encoding, two masked multi-head attention layers and finally the dense output layers. The architecture that follows is taken from [Deep Learning with Python, second edition, chapter 11](https://www.manning.com/books/deep-learning-with-python-second-edition)
.

Copied!

`class PositionalEmbedding(layers.Layer):     def __init__(self, sequence_length, vocab_size, embed_dim, **kwargs):         super().__init__(**kwargs)         self.token_embeddings = layers.Embedding(             input_dim=vocab_size, output_dim=embed_dim         )         self.position_embeddings = layers.Embedding(             input_dim=sequence_length, output_dim=embed_dim         )         self.sequence_length = sequence_length         self.vocab_size = vocab_size         self.embed_dim = embed_dim      def call(self, inputs):         length = ops.shape(inputs)[-1]         positions = ops.arange(0, length, 1)         embedded_tokens = self.token_embeddings(inputs)         embedded_positions = self.position_embeddings(positions)         return embedded_tokens + embedded_positions      def compute_mask(self, inputs, mask=None):         return ops.not_equal(inputs, 0)  class FNetDecoder(layers.Layer):     def __init__(self, embed_dim, latent_dim, num_heads, **kwargs):         super().__init__(**kwargs)         self.embed_dim = embed_dim         self.latent_dim = latent_dim         self.num_heads = num_heads         self.attention_1 = layers.MultiHeadAttention(             num_heads=num_heads, key_dim=embed_dim         )         self.attention_2 = layers.MultiHeadAttention(             num_heads=num_heads, key_dim=embed_dim         )         self.dense_proj = keras.Sequential(             [                 layers.Dense(latent_dim, activation="relu"),                 layers.Dense(embed_dim),             ]         )         self.layernorm_1 = layers.LayerNormalization()         self.layernorm_2 = layers.LayerNormalization()         self.layernorm_3 = layers.LayerNormalization()         self.supports_masking = True      def call(self, inputs, encoder_outputs, mask=None):         causal_mask = self.get_causal_attention_mask(inputs)          if mask is not None:             padding_mask = ops.cast(mask[:, None, :], "int32")         else:             padding_mask = None          attention_output_1 = self.attention_1(             query=inputs, value=inputs, key=inputs, attention_mask=causal_mask         )         out_1 = self.layernorm_1(inputs + attention_output_1)          attention_output_2 = self.attention_2(             query=out_1,             value=encoder_outputs,             key=encoder_outputs,             attention_mask=padding_mask,         )         out_2 = self.layernorm_2(out_1 + attention_output_2)          proj_output = self.dense_proj(out_2)         return self.layernorm_3(out_2 + proj_output)      def get_causal_attention_mask(self, inputs):         input_shape = ops.shape(inputs)         batch_size, sequence_length = input_shape[0], input_shape[1]         i = ops.arange(sequence_length)[:, None]         j = ops.arange(sequence_length)         mask = ops.cast(i >= j, dtype="int32")         mask = ops.reshape(mask, (1, input_shape[1], input_shape[1]))         multiples = [batch_size, 1, 1]         return ops.tile(mask, multiples)  def create_model():     encoder_inputs = keras.Input(shape=(None,), dtype="int32", name="encoder_inputs")     x = PositionalEmbedding(MAX_LENGTH, VOCAB_SIZE, EMBED_DIM)(encoder_inputs)     encoder_outputs = FNetEncoder(EMBED_DIM, LATENT_DIM)(x)     encoder = keras.Model(encoder_inputs, encoder_outputs)     decoder_inputs = keras.Input(shape=(None,), dtype="int32", name="decoder_inputs")     encoded_seq_inputs = keras.Input(         shape=(None, EMBED_DIM), name="decoder_state_inputs"     )     x = PositionalEmbedding(MAX_LENGTH, VOCAB_SIZE, EMBED_DIM)(decoder_inputs)     x = FNetDecoder(EMBED_DIM, LATENT_DIM, NUM_HEADS)(x, encoded_seq_inputs)     x = layers.Dropout(0.5)(x)     decoder_outputs = layers.Dense(VOCAB_SIZE, activation="softmax")(x)     decoder = keras.Model(         [decoder_inputs, encoded_seq_inputs], decoder_outputs, name="outputs"     )     decoder_outputs = decoder([decoder_inputs, encoder_outputs])     fnet = keras.Model([encoder_inputs, decoder_inputs], decoder_outputs, name="fnet")     return fnet`

* * *

Creating and Training the model
-------------------------------

Copied!

`fnet = create_model() fnet.compile("adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])`

The model as configured here uses a simplified architecture to keep training time manageable for a tutorial. The text generation quality will be limited - outputs may be generic. Although accuracy is not a good measure for this task, we will use it just to get a hint of the improvement of the network.

Copied!

`fnet.fit(train_dataset, epochs=1, validation_data=val_dataset)`

`625/625 ━━━━━━━━━━━━━━━━━━━━ 558s 890ms/step - accuracy: 0.2864 - loss: 4.3480 - val_accuracy: 0.3189 - val_loss: 3.9545  <keras.src.callbacks.history.History at 0x104c17250>`

* * *

Performing inference
--------------------

Copied!

`VOCAB = vectorizer.get_vocabulary()  def decode_sentence(input_sentence):     # Mapping the input sentence to tokens and adding start and end tokens     tokenized_input_sentence = vectorizer(         "[start] " + preprocess_text(input_sentence) + " [end]"     )      # Start token     start_token_index = VOCAB.index("[start]")     end_token_index = VOCAB.index("[end]")      tokenized_target_sentence = ops.expand_dims(start_token_index, axis=0)     decoded_sentence = []      for i in range(MAX_LENGTH):         # Get the predictions         predictions = fnet.predict(             {                 "encoder_inputs": ops.expand_dims(tokenized_input_sentence, axis=0),                 "decoder_inputs": ops.expand_dims(                     ops.pad(                         tokenized_target_sentence,                         [[0, MAX_LENGTH - ops.shape(tokenized_target_sentence)[0]]],                     ),                     axis=0,                 ),             }         )         # Calculating the token with maximum probability and getting the corresponding word         sampled_token_index = ops.argmax(predictions[0, i, :])         sampled_token_index = int(sampled_token_index)          if sampled_token_index == end_token_index:             break          decoded_sentence.append(VOCAB[sampled_token_index])          tokenized_target_sentence = ops.concatenate(             [tokenized_target_sentence, ops.expand_dims(sampled_token_index, axis=0)],             axis=0,         )      return " ".join(decoded_sentence)  decode_sentence("Where have you been all this time?")`

`1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 19ms/step  'i m not a little .'`

* * *

Conclusion
----------

This example shows how to train and perform inference using the FNet model. For getting insight into the architecture or for further reading, you can refer to:

1.  [FNet: Mixing Tokens with Fourier Transforms](https://arxiv.org/abs/2105.03824v3)
     (Lee-Thorp et al., 2021)
2.  [Attention Is All You Need](https://arxiv.org/abs/1706.03762v5)
     (Vaswani et al., 2017)

Thanks to François Chollet for his Keras example on [English-to-Spanish translation with a sequence-to-sequence Transformer](https://keras.io/examples/nlp/neural_machine_translation_with_transformer/)
 from which the decoder implementation was extracted.

* * *

Relevant Chapters from Deep Learning with Python
------------------------------------------------

*   [Chapter 15: Language models and the Transformer](https://deeplearningwithpython.io/chapters/chapter15_language-models-and-the-transformer)
    
*   [Chapter 16: Text generation](https://deeplearningwithpython.io/chapters/chapter16_text-generation)
    

[Text Generation using FNet](https://keras.io/examples/generative/text_generation_fnet/#text-generation-using-fnet)

[Introduction](https://keras.io/examples/generative/text_generation_fnet/#introduction)

[Imports](https://keras.io/examples/generative/text_generation_fnet/#imports)

[Loading data](https://keras.io/examples/generative/text_generation_fnet/#loading-data)

[Preprocessing and Tokenization](https://keras.io/examples/generative/text_generation_fnet/#preprocessing-and-tokenization)

[Tokenizing and padding sentences using `TextVectorization`](https://keras.io/examples/generative/text_generation_fnet/#tokenizing-and-padding-sentences-using-textvectorization)

[Creating the FNet Encoder](https://keras.io/examples/generative/text_generation_fnet/#creating-the-fnet-encoder)

[Creating the Decoder](https://keras.io/examples/generative/text_generation_fnet/#creating-the-decoder)

[Creating and Training the model](https://keras.io/examples/generative/text_generation_fnet/#creating-and-training-the-model)

[Performing inference](https://keras.io/examples/generative/text_generation_fnet/#performing-inference)

[Conclusion](https://keras.io/examples/generative/text_generation_fnet/#conclusion)

[Relevant Chapters from Deep Learning with Python](https://keras.io/examples/generative/text_generation_fnet/#relevant-chapters-from-deep-learning-with-python)