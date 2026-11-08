None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Data loading](https://keras.io/api/data_loading/)
 [Tree API](https://keras.io/api/tree/)
 [Built-in small datasets](https://keras.io/api/datasets/)
 [MNIST digits classification dataset](https://keras.io/api/datasets/mnist/)
 [CIFAR10 small images classification dataset](https://keras.io/api/datasets/cifar10/)
 [CIFAR100 small images classification dataset](https://keras.io/api/datasets/cifar100/)
 [IMDB movie review sentiment classification dataset](https://keras.io/api/datasets/imdb/)
 [Reuters newswire classification dataset](https://keras.io/api/datasets/reuters/)
 [Fashion MNIST dataset, an alternative to MNIST](https://keras.io/api/datasets/fashion_mnist/)
 [California Housing price regression dataset](https://keras.io/api/datasets/california_housing/)
 [Boston Housing price regression dataset](https://keras.io/api/datasets/boston_housing/)
 [Keras Applications](https://keras.io/api/applications/)
 [Mixed precision](https://keras.io/api/mixed_precision/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Built-in small datasets](https://keras.io/api/datasets/)
 / IMDB movie review sentiment classification dataset

IMDB movie review sentiment classification dataset
==================================================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/datasets/imdb.py#L13)

### `load_data` function

Copied!

`keras.datasets.imdb.load_data(     path="imdb.npz",     num_words=None,     skip_top=0,     maxlen=None,     seed=113,     start_char=1,     oov_char=2,     index_from=3,     **kwargs )`

Loads the [IMDB dataset](https://ai.stanford.edu/~amaas/data/sentiment/)
.

This is a dataset of 25,000 movies reviews from IMDB, labeled by sentiment (positive/negative). Reviews have been preprocessed, and each review is encoded as a list of word indexes (integers). For convenience, words are indexed by overall frequency in the dataset, so that for instance the integer "3" encodes the 3rd most frequent word in the data. This allows for quick filtering operations such as: "only consider the top 10,000 most common words, but eliminate the top 20 most common words".

As a convention, "0" does not stand for a specific word, but instead is used to encode the pad token.

**Arguments**

*   **path**: where to cache the data (relative to `~/.keras/dataset`).
*   **num\_words**: integer or None. Words are ranked by how often they occur (in the training set) and only the `num_words` most frequent words are kept. Any less frequent word will appear as `oov_char` value in the sequence data. If None, all words are kept. Defaults to `None`.
*   **skip\_top**: skip the top N most frequently occurring words (which may not be informative). These words will appear as `oov_char` value in the dataset. When 0, no words are skipped. Defaults to `0`.
*   **maxlen**: int or None. Maximum sequence length. Any longer sequence will be truncated. None, means no truncation. Defaults to `None`.
*   **seed**: int. Seed for reproducible data shuffling.
*   **start\_char**: int. The start of a sequence will be marked with this character. 0 is usually the padding character. Defaults to `1`.
*   **oov\_char**: int. The out-of-vocabulary character. Words that were cut out because of the `num_words` or `skip_top` limits will be replaced with this character.
*   **index\_from**: int. Index actual words with this index and higher.

**Returns**

*   **Tuple of Numpy arrays**: `(x_train, y_train), (x_test, y_test)`.

**`x_train`, `x_test`**: lists of sequences, which are lists of indexes (integers). If the num\_words argument was specific, the maximum possible index value is `num_words - 1`. If the `maxlen` argument was specified, the largest possible sequence length is `maxlen`.

**`y_train`, `y_test`**: lists of integer labels (1 or 0).

**Note**: The 'out of vocabulary' character is only used for words that were present in the training set but are not included because they're not making the `num_words` cut here. Words that were not seen in the training set but are in the test set have simply been skipped.

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/datasets/imdb.py#L147)

### `get_word_index` function

Copied!

`keras.datasets.imdb.get_word_index(path="imdb_word_index.json")`

Retrieves a dict mapping words to their index in the IMDB dataset.

**Arguments**

*   **path**: where to cache the data (relative to `~/.keras/dataset`).

**Returns**

The word index dictionary. Keys are word strings, values are their index.

**Example**

Copied!

``# Use the default parameters to keras.datasets.imdb.load_data start_char = 1 oov_char = 2 index_from = 3 # Retrieve the training sequences. (x_train, _), _ = keras.datasets.imdb.load_data(     start_char=start_char, oov_char=oov_char, index_from=index_from ) # Retrieve the word index file mapping words to indices word_index = keras.datasets.imdb.get_word_index() # Reverse the word index to obtain a dict mapping indices to words # And add `index_from` to indices to sync with `x_train` inverted_word_index = dict(     (i + index_from, word) for (word, i) in word_index.items() ) # Update `inverted_word_index` to include `start_char` and `oov_char` inverted_word_index[start_char] = "[START]" inverted_word_index[oov_char] = "[OOV]" # Decode the first sequence in the dataset decoded_sequence = " ".join(inverted_word_index[i] for i in x_train[0])``

* * *

[IMDB movie review sentiment classification dataset](https://keras.io/api/datasets/imdb/#imdb-movie-review-sentiment-classification-dataset)

[`load_data` function](https://keras.io/api/datasets/imdb/#loaddata-function)

[`get_word_index` function](https://keras.io/api/datasets/imdb/#getwordindex-function)