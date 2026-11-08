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
 / GPT text generation from scratch with KerasHub

GPT text generation from scratch with KerasHub
==============================================

**Author:** [Jesse Chan](https://github.com/jessechancy)
  
**Date created:** 2022/07/25  
**Last modified:** 2022/07/25  
**Description:** Using KerasHub to train a mini-GPT model for text generation.

ⓘ This example uses Keras 3

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/generative/ipynb/text_generation_gpt.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/examples/generative/text_generation_gpt.py)

* * *

Introduction
------------

In this example, we will use KerasHub to build a scaled down Generative Pre-Trained (GPT) model. GPT is a Transformer-based model that allows you to generate sophisticated text from a prompt.

We will train the model on the [simplebooks-92](https://arxiv.org/abs/1911.12391)
 corpus, which is a dataset made from several novels. It is a good dataset for this example since it has a small vocabulary and high word frequency, which is beneficial when training a model with few parameters.

This example combines concepts from [Text generation with a miniature GPT](https://keras.io/examples/generative/text_generation_with_miniature_gpt/)
 with KerasHub abstractions. We will demonstrate how KerasHub tokenization, layers and metrics simplify the training process, and then show how to generate output text using the KerasHub sampling utilities.

Note: If you are running this example on a Colab, make sure to enable GPU runtime for faster training.

This example requires KerasHub. You can install it via the following command: `pip install keras-hub`

* * *

Setup
-----

Copied!

`!pip install -q --upgrade keras-hub !pip install -q --upgrade keras  # Upgrade to Keras 3.`

Copied!

`import os import keras_hub import keras  import tensorflow.data as tf_data import tensorflow.strings as tf_strings`

* * *

Settings & hyperparameters
--------------------------

Copied!

`# Data BATCH_SIZE = 64 MIN_STRING_LEN = 512  # Strings shorter than this will be discarded SEQ_LEN = 128  # Length of training sequences, in tokens  # Model EMBED_DIM = 256 FEED_FORWARD_DIM = 128 NUM_HEADS = 3 NUM_LAYERS = 2 VOCAB_SIZE = 5000  # Limits parameters in model.  # Training EPOCHS = 5  # Inference NUM_TOKENS_TO_GENERATE = 80`

* * *

Load the data
-------------

Now, let's download the dataset! The SimpleBooks dataset consists of 1,573 Gutenberg books, and has one of the smallest vocabulary size to word-level tokens ratio. It has a vocabulary size of ~98k, a third of WikiText-103's, with around the same number of tokens (~100M). This makes it easy to fit a small model.

Copied!

`keras.utils.get_file(     origin="https://dldata-public.s3.us-east-2.amazonaws.com/simplebooks.zip",     extract=True, ) dir = os.path.expanduser("~/.keras/datasets/simplebooks/")  # Load simplebooks-92 train set and filter out short lines. raw_train_ds = (     tf_data.TextLineDataset(dir + "simplebooks-92-raw/train.txt")     .filter(lambda x: tf_strings.length(x) > MIN_STRING_LEN)     .batch(BATCH_SIZE)     .shuffle(buffer_size=256) )  # Load simplebooks-92 validation set and filter out short lines. raw_val_ds = (     tf_data.TextLineDataset(dir + "simplebooks-92-raw/valid.txt")     .filter(lambda x: tf_strings.length(x) > MIN_STRING_LEN)     .batch(BATCH_SIZE) )`

`Downloading data from https://dldata-public.s3.us-east-2.amazonaws.com/simplebooks.zip  282386239/282386239 ━━━━━━━━━━━━━━━━━━━━ 7s 0us/step`

* * *

Train the tokenizer
-------------------

We train the tokenizer from the training dataset for a vocabulary size of `VOCAB_SIZE`, which is a tuned hyperparameter. We want to limit the vocabulary as much as possible, as we will see later on that it has a large effect on the number of model parameters. We also don't want to include _too few_ vocabulary terms, or there would be too many out-of-vocabulary (OOV) sub-words. In addition, three tokens are reserved in the vocabulary:

*   `"[PAD]"` for padding sequences to `SEQ_LEN`. This token has index 0 in both `reserved_tokens` and `vocab`, since `WordPieceTokenizer` (and other layers) consider `0`/`vocab[0]` as the default padding.
*   `"[UNK]"` for OOV sub-words, which should match the default `oov_token="[UNK]"` in `WordPieceTokenizer`.
*   `"[BOS]"` stands for beginning of sentence, but here technically it is a token representing the beginning of each line of training data.

Copied!

`# Train tokenizer vocabulary vocab = keras_hub.tokenizers.compute_word_piece_vocabulary(     raw_train_ds,     vocabulary_size=VOCAB_SIZE,     lowercase=True,     reserved_tokens=["[PAD]", "[UNK]", "[BOS]"], )`

* * *

Load tokenizer
--------------

We use the vocabulary data to initialize [`keras_hub.tokenizers.WordPieceTokenizer`](https://keras.io/keras_hub/api/tokenizers/word_piece_tokenizer#wordpiecetokenizer-class)
. WordPieceTokenizer is an efficient implementation of the WordPiece algorithm used by BERT and other models. It will strip, lower-case and do other irreversible preprocessing operations.

Copied!

`tokenizer = keras_hub.tokenizers.WordPieceTokenizer(     vocabulary=vocab,     sequence_length=SEQ_LEN,     lowercase=True, )`

* * *

Tokenize data
-------------

We preprocess the dataset by tokenizing and splitting it into `features` and `labels`.

Copied!

`# packer adds a start token start_packer = keras_hub.layers.StartEndPacker(     sequence_length=SEQ_LEN,     start_value=tokenizer.token_to_id("[BOS]"), )  def preprocess(inputs):     outputs = tokenizer(inputs)     features = start_packer(outputs)     labels = outputs     return features, labels  # Tokenize and split into train and label sequences. train_ds = raw_train_ds.map(preprocess, num_parallel_calls=tf_data.AUTOTUNE).prefetch(     tf_data.AUTOTUNE ) val_ds = raw_val_ds.map(preprocess, num_parallel_calls=tf_data.AUTOTUNE).prefetch(     tf_data.AUTOTUNE )`

* * *

Build the model
---------------

We create our scaled down GPT model with the following layers:

*   One [`keras_hub.layers.TokenAndPositionEmbedding`](https://keras.io/keras_hub/api/modeling_layers/token_and_position_embedding#tokenandpositionembedding-class)
     layer, which combines the embedding for the token and its position.
*   Multiple [`keras_hub.layers.TransformerDecoder`](https://keras.io/keras_hub/api/modeling_layers/transformer_decoder#transformerdecoder-class)
     layers, with the default causal masking. The layer has no cross-attention when run with decoder sequence only.
*   One final dense linear layer

Copied!

`inputs = keras.layers.Input(shape=(None,), dtype="int32") # Embedding. embedding_layer = keras_hub.layers.TokenAndPositionEmbedding(     vocabulary_size=VOCAB_SIZE,     sequence_length=SEQ_LEN,     embedding_dim=EMBED_DIM,     mask_zero=True, ) x = embedding_layer(inputs) # Transformer decoders. for _ in range(NUM_LAYERS):     decoder_layer = keras_hub.layers.TransformerDecoder(         num_heads=NUM_HEADS,         intermediate_dim=FEED_FORWARD_DIM,     )     x = decoder_layer(x)  # Giving one argument only skips cross-attention. # Output. outputs = keras.layers.Dense(VOCAB_SIZE)(x) model = keras.Model(inputs=inputs, outputs=outputs) loss_fn = keras.losses.SparseCategoricalCrossentropy(from_logits=True) perplexity = keras_hub.metrics.Perplexity(from_logits=True, mask_token_id=0) model.compile(optimizer="adam", loss=loss_fn, metrics=[perplexity])`

Let's take a look at our model summary - a large majority of the parameters are in the `token_and_position_embedding` and the output `dense` layer! This means that the vocabulary size (`VOCAB_SIZE`) has a large effect on the size of the model, while the number of Transformer decoder layers (`NUM_LAYERS`) doesn't affect it as much.

Copied!

`model.summary()`

Model: "functional\_1"

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Layer (type)                    ┃ Output Shape              ┃    Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ input\_layer (InputLayer)        │ (None, None)              │          0 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ token\_and\_position\_embedding    │ (None, None, 256)         │  1,312,768 │
│ (TokenAndPositionEmbedding)     │                           │            │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ transformer\_decoder             │ (None, None, 256)         │    329,085 │
│ (TransformerDecoder)            │                           │            │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ transformer\_decoder\_1           │ (None, None, 256)         │    329,085 │
│ (TransformerDecoder)            │                           │            │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ dense (Dense)                   │ (None, None, 5000)        │  1,285,000 │
└─────────────────────────────────┴───────────────────────────┴────────────┘

 Total params: 3,255,938 (12.42 MB)

 Trainable params: 3,255,938 (12.42 MB)

 Non-trainable params: 0 (0.00 B)

* * *

Training
--------

Now that we have our model, let's train it with the `fit()` method.

Copied!

`model.fit(train_ds, validation_data=val_ds, epochs=EPOCHS)`

`Epoch 1/5  2445/2445 ━━━━━━━━━━━━━━━━━━━━ 216s 66ms/step - loss: 5.0008 - perplexity: 180.0715 - val_loss: 4.2176 - val_perplexity: 68.0438 Epoch 2/5  2445/2445 ━━━━━━━━━━━━━━━━━━━━ 127s 48ms/step - loss: 4.1699 - perplexity: 64.7740 - val_loss: 4.0553 - val_perplexity: 57.7996 Epoch 3/5  2445/2445 ━━━━━━━━━━━━━━━━━━━━ 126s 47ms/step - loss: 4.0286 - perplexity: 56.2138 - val_loss: 4.0134 - val_perplexity: 55.4446 Epoch 4/5  2445/2445 ━━━━━━━━━━━━━━━━━━━━ 134s 50ms/step - loss: 3.9576 - perplexity: 52.3643 - val_loss: 3.9900 - val_perplexity: 54.1153 Epoch 5/5  2445/2445 ━━━━━━━━━━━━━━━━━━━━ 135s 51ms/step - loss: 3.9080 - perplexity: 49.8242 - val_loss: 3.9500 - val_perplexity: 52.0006  <keras.src.callbacks.history.History at 0x7f7de0365ba0>`

* * *

Inference
---------

With our trained model, we can test it out to gauge its performance. To do this we can seed our model with an input sequence starting with the `"[BOS]"` token, and progressively sample the model by making predictions for each subsequent token in a loop.

To start lets build a prompt with the same shape as our model inputs, containing only the `"[BOS]"` token.

Copied!

`# The "packer" layers adds the [BOS] token for us. prompt_tokens = start_packer(tokenizer([""])) prompt_tokens`

`<tf.Tensor: shape=(1, 128), dtype=int32, numpy= array([[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],       dtype=int32)>`

We will use the `keras_hub.samplers` module for inference, which requires a callback function wrapping the model we just trained. This wrapper calls the model and returns the logit predictions for the current token we are generating.

Note: There are two pieces of more advanced functionality available when defining your callback. The first is the ability to take in a `cache` of states computed in previous generation steps, which can be used to speed up generation. The second is the ability to output the final dense "hidden state" of each generated token. This is used by [`keras_hub.samplers.ContrastiveSampler`](https://keras.io/keras_hub/api/samplers/contrastive_sampler#contrastivesampler-class)
, which avoids repetition by penalizing repeated hidden states. Both are optional, and we will ignore them for now.

Copied!

`def next(prompt, cache, index):     logits = model(prompt)[:, index - 1, :]     # Ignore hidden states for now; only needed for contrastive search.     hidden_states = None     return logits, hidden_states, cache`

Creating the wrapper function is the most complex part of using these functions. Now that it's done, let's test out the different utilities, starting with greedy search.

### Greedy search

We greedily pick the most probable token at each timestep. In other words, we get the argmax of the model output.

Copied!

`sampler = keras_hub.samplers.GreedySampler() output_tokens = sampler(     next=next,     prompt=prompt_tokens,     index=1,  # Start sampling immediately after the [BOS] token. ) txt = tokenizer.detokenize(output_tokens) print(f"Greedy search generated text: \n{txt}\n")`

`Greedy search generated text:  [b'[BOS] " i \' m going to tell you , " said the boy , " i \' ll tell you , and you \' ll be a good friend , and you \' ll be a good friend , and you \' ll be a good friend , and you \' ll be a good friend , and you \' ll be a good friend , and you \' ll be a good friend , and you \' ll be a good friend , and you \' ll be a good friend , and you \' ll be a good friend , and you \' ll be a good friend , and you \' ll be a good friend , and you \' ll be a good']`

As you can see, greedy search starts out making some sense, but quickly starts repeating itself. This is a common problem with text generation that can be fixed by some of the probabilistic text generation utilities shown later on!

### Beam search

At a high-level, beam search keeps track of the `num_beams` most probable sequences at each timestep, and predicts the best next token from all sequences. It is an improvement over greedy search since it stores more possibilities. However, it is less efficient than greedy search since it has to compute and store multiple potential sequences.

**Note:** beam search with `num_beams=1` is identical to greedy search.

Copied!

`sampler = keras_hub.samplers.BeamSampler(num_beams=10) output_tokens = sampler(     next=next,     prompt=prompt_tokens,     index=1, ) txt = tokenizer.detokenize(output_tokens) print(f"Beam search generated text: \n{txt}\n")`

`Beam search generated text:  [b'[BOS] " i don \' t know anything about it , " she said . " i don \' t know anything about it . i don \' t know anything about it , but i don \' t know anything about it . i don \' t know anything about it , but i don \' t know anything about it . i don \' t know anything about it , but i don \' t know it . i don \' t know it , but i don \' t know it . i don \' t know it , but i don \' t know it . i don \' t know it , but i don \' t know it . i don \'']`

Similar to greedy search, beam search quickly starts repeating itself, since it is still a deterministic method.

### Random search

Random search is our first probabilistic method. At each time step, it samples the next token using the softmax probabilities provided by the model.

Copied!

`sampler = keras_hub.samplers.RandomSampler() output_tokens = sampler(     next=next,     prompt=prompt_tokens,     index=1, ) txt = tokenizer.detokenize(output_tokens) print(f"Random search generated text: \n{txt}\n")`

`Random search generated text:  [b'[BOS] eleanor . like ice , not children would have suspicious forehead . they will see him , no goods in her plums . i have made a stump one , on the occasion , - - it is sacred , and one is unholy - plaything - - the partial consequences , and one refuge in a style of a boy , who was his grandmother . it was a young gentleman who bore off upon the middle of the day , rush and as he maltreated the female society , were growing at once . in and out of the craid little plays , stopping']`

Voilà, no repetitions! However, with random search, we may see some nonsensical words appearing since any word in the vocabulary has a chance of appearing with this sampling method. This is fixed by our next search utility, top-k search.

### Top-K search

Similar to random search, we sample the next token from the probability distribution provided by the model. The only difference is that here, we select out the top `k` most probable tokens, and distribute the probability mass over them before sampling. This way, we won't be sampling from low probability tokens, and hence we would have less nonsensical words!

Copied!

`sampler = keras_hub.samplers.TopKSampler(k=10) output_tokens = sampler(     next=next,     prompt=prompt_tokens,     index=1, ) txt = tokenizer.detokenize(output_tokens) print(f"Top-K search generated text: \n{txt}\n")`

`Top-K search generated text:  [b'[BOS] " the young man was not the one , and the boy went away to the green forest . they were a little girl \' s wife , and the child loved him as much as he did , and he had often heard of a little girl who lived near the house . they were too tired to go , and when they went down to the barns and get into the barn , and they got the first of the barns that they had been taught to do so , and the little people went to their homes . she did , she told them that she had been a very clever , and they had made the first . she knew they']`

### Top-P search

Even with the top-k search, there is something to improve upon. With top-k search, the number `k` is fixed, which means it selects the same number of tokens for any probability distribution. Consider two scenarios, one where the probability mass is concentrated over 2 words and another where the probability mass is evenly concentrated across 10. Should we choose `k=2` or `k=10`? There is no one size that fits all `k` here.

This is where top-p search comes in! Instead of choosing a `k`, we choose a probability `p` that we want the probabilities of the top tokens to sum up to. This way, we can dynamically adjust the `k` based on the probability distribution. By setting `p=0.9`, if 90% of the probability mass is concentrated on the top 2 tokens, we can filter out the top 2 tokens to sample from. If instead the 90% is distributed over 10 tokens, it will similarly filter out the top 10 tokens to sample from.

Copied!

`sampler = keras_hub.samplers.TopPSampler(p=0.5) output_tokens = sampler(     next=next,     prompt=prompt_tokens,     index=1, ) txt = tokenizer.detokenize(output_tokens) print(f"Top-P search generated text: \n{txt}\n")`

`Top-P search generated text:  [b'[BOS] the children were both born in the spring , and the youngest sister were very much like the other children , but they did not see them . they were very happy , and their mother was a beautiful one . the youngest was one of the youngest sister of the youngest , and the youngest baby was very fond of the children . when they came home , they would see a little girl in the house , and had the beautiful family , and the children of the children had to sit and look on their backs , and the eldest children were very long , and they were so bright and happy , as they were , they had never noticed their hair ,']`

### Using callbacks for text generation

We can also wrap the utilities in a callback, which allows you to print out a prediction sequence for every epoch of the model! Here is an example of a callback for top-k search:

Copied!

`class TopKTextGenerator(keras.callbacks.Callback):     """A callback to generate text from a trained model using top-k."""      def __init__(self, k):         self.sampler = keras_hub.samplers.TopKSampler(k)      def on_epoch_end(self, epoch, logs=None):         output_tokens = self.sampler(             next=next,             prompt=prompt_tokens,             index=1,         )         txt = tokenizer.detokenize(output_tokens)         print(f"Top-K search generated text: \n{txt}\n")  text_generation_callback = TopKTextGenerator(k=10) # Dummy training loop to demonstrate callback. model.fit(train_ds.take(1), verbose=2, epochs=2, callbacks=[text_generation_callback])`

`Epoch 1/2 Top-K search generated text:  [b"[BOS] the young man was in the middle of a month , and he was able to take the crotch , but a long time , for he felt very well for himself in the sepoys ' s hands were chalks . he was the only boy , and he had a few years before been married , and the man said he was a tall one . he was a very handsome , and he was a very handsome young fellow , and a handsome , noble young man , but a boy , and man . he was a very handsome man , and was tall and handsome , and he looked like a gentleman . he was an"]`

`1/1 - 16s - 16s/step - loss: 3.9454 - perplexity: 51.6987 Epoch 2/2 Top-K search generated text:  [b'[BOS] " well , it is true . it is true that i should go to the house of a collector , in the matter of prussia that there is no other way there . there is no chance of being in the habit of being in the way of an invasion . i know not what i have done , but i have seen the man in the middle of a day . the next morning i shall take him to my father , for i am not the very day of the town , which would have been a little more than the one \' s daughter , i think it over and the whole affair will be']`

`1/1 - 17s - 17s/step - loss: 3.7860 - perplexity: 44.0932  <keras.src.callbacks.history.History at 0x7f7de0325600>`

* * *

Conclusion
----------

To recap, in this example, we use KerasHub layers to train a sub-word vocabulary, tokenize training data, create a miniature GPT model, and perform inference with the text generation library.

If you would like to understand how Transformers work, or learn more about training the full GPT model, here are some further readings:

*   Attention Is All You Need [Vaswani et al., 2017](https://arxiv.org/abs/1706.03762)
    
*   GPT-3 Paper [Brown et al., 2020](https://arxiv.org/abs/2005.14165)
    

* * *

Relevant Chapters from Deep Learning with Python
------------------------------------------------

*   [Chapter 15: Language models and the Transformer](https://deeplearningwithpython.io/chapters/chapter15_language-models-and-the-transformer)
    
*   [Chapter 16: Text generation](https://deeplearningwithpython.io/chapters/chapter16_text-generation)
    

[GPT text generation from scratch with KerasHub](https://keras.io/examples/generative/text_generation_gpt/#gpt-text-generation-from-scratch-with-kerashub)

[Introduction](https://keras.io/examples/generative/text_generation_gpt/#introduction)

[Setup](https://keras.io/examples/generative/text_generation_gpt/#setup)

[Settings & hyperparameters](https://keras.io/examples/generative/text_generation_gpt/#settings-amp-hyperparameters)

[Load the data](https://keras.io/examples/generative/text_generation_gpt/#load-the-data)

[Train the tokenizer](https://keras.io/examples/generative/text_generation_gpt/#train-the-tokenizer)

[Load tokenizer](https://keras.io/examples/generative/text_generation_gpt/#load-tokenizer)

[Tokenize data](https://keras.io/examples/generative/text_generation_gpt/#tokenize-data)

[Build the model](https://keras.io/examples/generative/text_generation_gpt/#build-the-model)

[Training](https://keras.io/examples/generative/text_generation_gpt/#training)

[Inference](https://keras.io/examples/generative/text_generation_gpt/#inference)

[Greedy search](https://keras.io/examples/generative/text_generation_gpt/#greedy-search)

[Beam search](https://keras.io/examples/generative/text_generation_gpt/#beam-search)

[Random search](https://keras.io/examples/generative/text_generation_gpt/#random-search)

[Top-K search](https://keras.io/examples/generative/text_generation_gpt/#topk-search)

[Top-P search](https://keras.io/examples/generative/text_generation_gpt/#topp-search)

[Using callbacks for text generation](https://keras.io/examples/generative/text_generation_gpt/#using-callbacks-for-text-generation)

[Conclusion](https://keras.io/examples/generative/text_generation_gpt/#conclusion)

[Relevant Chapters from Deep Learning with Python](https://keras.io/examples/generative/text_generation_gpt/#relevant-chapters-from-deep-learning-with-python)