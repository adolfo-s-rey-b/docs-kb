[Skip to main content](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/text/plot_hashing_vs_dict_vectorizer.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/text/plot_hashing_vs_dict_vectorizer.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/text/plot_hashing_vs_dict_vectorizer.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/text/plot_hashing_vs_dict_vectorizer.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/text/plot_hashing_vs_dict_vectorizer.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/text/plot_hashing_vs_dict_vectorizer.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html#sphx-glr-download-auto-examples-text-plot-hashing-vs-dict-vectorizer-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

FeatureHasher and DictVectorizer Comparison[#](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html#featurehasher-and-dictvectorizer-comparison "Link to this heading")

===========================================================================================================================================================================================================

In this example we illustrate text vectorization, which is the process of representing non-numerical input data (such as dictionaries or text documents) as vectors of real numbers.

We first compare [`FeatureHasher`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")
 and [`DictVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "sklearn.feature_extraction.DictVectorizer")
 by using both methods to vectorize text documents that are preprocessed (tokenized) with the help of a custom Python function.

Later we introduce and analyze the text-specific vectorizers [`HashingVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")
, [`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
 and [`TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
 that handle both the tokenization and the assembling of the feature matrix within a single class.

The objective of the example is to demonstrate the usage of text vectorization API and to compare their processing time. See the example scripts [Classification of text documents using sparse features](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html#sphx-glr-auto-examples-text-plot-document-classification-20newsgroups-py)
 and [Clustering text documents using k-means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html#sphx-glr-auto-examples-text-plot-document-clustering-py)
 for actual learning on text documents.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Load Data[#](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html#load-data "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

We load data from [The 20 newsgroups text dataset](https://scikit-learn.org/stable/datasets/real_world.html#newsgroups-dataset)
, which comprises around 18000 newsgroups posts on 20 topics split in two subsets: one for training and one for testing. For the sake of simplicity and reducing the computational cost, we select a subset of 7 topics and use the training set only.

from sklearn.datasets import [fetch\_20newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")

categories \= \[\
    "alt.atheism",\
    "comp.graphics",\
    "comp.sys.ibm.pc.hardware",\
    "misc.forsale",\
    "rec.autos",\
    "sci.space",\
    "talk.religion.misc",\
\]

print("Loading 20 newsgroups training data")
raw\_data, \_ \= [fetch\_20newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")
(subset\="train", categories\=categories, return\_X\_y\=True)
data\_size\_mb \= sum(len(s.encode("utf-8")) for s in raw\_data) / 1e6
print(f"{len(raw\_data)} documents - {data\_size\_mb:.3f}MB")

Copy to clipboard

Loading 20 newsgroups training data
3803 documents - 6.245MB

Copy to clipboard

Define preprocessing functions[#](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html#define-preprocessing-functions "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A token may be a word, part of a word or anything comprised between spaces or symbols in a string. Here we define a function that extracts the tokens using a simple regular expression (regex) that matches Unicode word characters. This includes most characters that can be part of a word in any language, as well as numbers and the underscore:

import re

def tokenize(doc):
    """Extract tokens from doc.

    This uses a simple regex that matches word characters to break strings
    into tokens. For a more principled approach, see CountVectorizer or
    TfidfVectorizer.
    """
    return (tok.lower() for tok in [re.findall](https://docs.python.org/3/library/re.html#re.findall "re.findall")
(r"\\w+", doc))

list(tokenize("This is a simple example, isn't it?"))

Copy to clipboard

\['this', 'is', 'a', 'simple', 'example', 'isn', 't', 'it'\]

Copy to clipboard

We define an additional function that counts the (frequency of) occurrence of each token in a given document. It returns a frequency dictionary to be used by the vectorizers.

from collections import [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict")

def token\_freqs(doc):
    """Extract a dict mapping tokens from doc to their occurrences."""

    freq \= [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict")
(int)
    for tok in tokenize(doc):
        freq\[tok\] += 1
    return freq

token\_freqs("That is one example, but this is another one")

Copy to clipboard

defaultdict(<class 'int'>, {'that': 1, 'is': 2, 'one': 2, 'example': 1, 'but': 1, 'this': 1, 'another': 1})

Copy to clipboard

Observe in particular that the repeated token `"is"` is counted twice for instance.

Breaking a text document into word tokens, potentially losing the order information between the words in a sentence is often called a [Bag of Words representation](https://en.wikipedia.org/wiki/Bag-of-words_model)
.

DictVectorizer[#](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html#dictvectorizer "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

First we benchmark the [`DictVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "sklearn.feature_extraction.DictVectorizer")
, then we compare it to [`FeatureHasher`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")
 as both of them receive dictionaries as input.

from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")

from sklearn.feature\_extraction import [DictVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "sklearn.feature_extraction.DictVectorizer")

dict\_count\_vectorizers \= [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict")
(list)

t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
vectorizer \= [DictVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "sklearn.feature_extraction.DictVectorizer")
()
vectorizer.fit\_transform(token\_freqs(d) for d in raw\_data)
duration \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0
dict\_count\_vectorizers\["vectorizer"\].append(
    vectorizer.\_\_class\_\_.\_\_name\_\_ + "\\non freq dicts"
)
dict\_count\_vectorizers\["speed"\].append(data\_size\_mb / duration)
print(f"done in {duration:.3f} s at {data\_size\_mb / duration:.1f} MB/s")
print(f"Found {len(vectorizer.get\_feature\_names\_out())} unique terms")

Copy to clipboard

done in 0.929 s at 6.7 MB/s
Found 47928 unique terms

Copy to clipboard

The actual mapping from text token to column index is explicitly stored in the `.vocabulary_` attribute which is a potentially very large Python dictionary:

type(vectorizer.vocabulary\_)

Copy to clipboard

len(vectorizer.vocabulary\_)

Copy to clipboard

47928

Copy to clipboard

vectorizer.vocabulary\_\["example"\]

Copy to clipboard

19145

Copy to clipboard

FeatureHasher[#](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html#featurehasher "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

Dictionaries take up a large amount of storage space and grow in size as the training set grows. Instead of growing the vectors along with a dictionary, feature hashing builds a vector of pre-defined length by applying a hash function `h` to the features (e.g., tokens), then using the hash values directly as feature indices and updating the resulting vector at those indices. When the feature space is not large enough, hashing functions tend to map distinct values to the same hash code (hash collisions). As a result, it is impossible to determine what object generated any particular hash code.

Because of the above it is impossible to recover the original tokens from the feature matrix and the best approach to estimate the number of unique terms in the original dictionary is to count the number of active columns in the encoded feature matrix. For such a purpose we define the following function:

import numpy as np

def n\_nonzero\_columns(X):
    """Number of columns with at least one non-zero value in a CSR matrix.

    This is useful to count the number of features columns that are effectively
    active when using the FeatureHasher.
    """
    return len([np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
(X.nonzero()\[1\]))

Copy to clipboard

The default number of features for the [`FeatureHasher`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")
 is 2\*\*20. Here we set `n_features = 2**18` to illustrate hash collisions.

**FeatureHasher on frequency dictionaries**

from sklearn.feature\_extraction import [FeatureHasher](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")

t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
hasher \= [FeatureHasher](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")
(n\_features\=2\*\*18)
X \= hasher.transform(token\_freqs(d) for d in raw\_data)
duration \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0
dict\_count\_vectorizers\["vectorizer"\].append(
    hasher.\_\_class\_\_.\_\_name\_\_ + "\\non freq dicts"
)
dict\_count\_vectorizers\["speed"\].append(data\_size\_mb / duration)
print(f"done in {duration:.3f} s at {data\_size\_mb / duration:.1f} MB/s")
print(f"Found {n\_nonzero\_columns(X)} unique tokens")

Copy to clipboard

done in 0.541 s at 11.5 MB/s
Found 43873 unique tokens

Copy to clipboard

The number of unique tokens when using the [`FeatureHasher`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")
 is lower than those obtained using the [`DictVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "sklearn.feature_extraction.DictVectorizer")
. This is due to hash collisions.

The number of collisions can be reduced by increasing the feature space. Notice that the speed of the vectorizer does not change significantly when setting a large number of features, though it causes larger coefficient dimensions and then requires more memory usage to store them, even if a majority of them is inactive.

t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
hasher \= [FeatureHasher](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")
(n\_features\=2\*\*22)
X \= hasher.transform(token\_freqs(d) for d in raw\_data)
duration \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0

print(f"done in {duration:.3f} s at {data\_size\_mb / duration:.1f} MB/s")
print(f"Found {n\_nonzero\_columns(X)} unique tokens")

Copy to clipboard

done in 0.550 s at 11.4 MB/s
Found 47668 unique tokens

Copy to clipboard

We confirm that the number of unique tokens gets closer to the number of unique terms found by the [`DictVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "sklearn.feature_extraction.DictVectorizer")
.

**FeatureHasher on raw tokens**

Alternatively, one can set `input_type="string"` in the [`FeatureHasher`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")
 to vectorize the strings output directly from the customized `tokenize` function. This is equivalent to passing a dictionary with an implied frequency of 1 for each feature name.

t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
hasher \= [FeatureHasher](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")
(n\_features\=2\*\*18, input\_type\="string")
X \= hasher.transform(tokenize(d) for d in raw\_data)
duration \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0
dict\_count\_vectorizers\["vectorizer"\].append(
    hasher.\_\_class\_\_.\_\_name\_\_ + "\\non raw tokens"
)
dict\_count\_vectorizers\["speed"\].append(data\_size\_mb / duration)
print(f"done in {duration:.3f} s at {data\_size\_mb / duration:.1f} MB/s")
print(f"Found {n\_nonzero\_columns(X)} unique tokens")

Copy to clipboard

done in 0.514 s at 12.1 MB/s
Found 43873 unique tokens

Copy to clipboard

We now plot the speed of the above methods for vectorizing.

import matplotlib.pyplot as plt

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(12, 6))

y\_pos \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len(dict\_count\_vectorizers\["vectorizer"\]))
ax.barh(y\_pos, dict\_count\_vectorizers\["speed"\], align\="center")
ax.set\_yticks(y\_pos)
ax.set\_yticklabels(dict\_count\_vectorizers\["vectorizer"\])
ax.invert\_yaxis()
\_ \= ax.set\_xlabel("speed (MB/s)")

Copy to clipboard

![plot hashing vs dict vectorizer](https://scikit-learn.org/stable/_images/sphx_glr_plot_hashing_vs_dict_vectorizer_001.png)

In both cases [`FeatureHasher`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")
 is approximately twice as fast as [`DictVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "sklearn.feature_extraction.DictVectorizer")
. This is handy when dealing with large amounts of data, with the downside of losing the invertibility of the transformation, which in turn makes the interpretation of a model a more complex task.

The `FeatureHeasher` with `input_type="string"` is slightly faster than the variant that works on frequency dict because it does not count repeated tokens: each token is implicitly counted once, even if it was repeated. Depending on the downstream machine learning task, it can be a limitation or not.

Comparison with special purpose text vectorizers[#](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html#comparison-with-special-purpose-text-vectorizers "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
 accepts raw data as it internally implements tokenization and occurrence counting. It is similar to the [`DictVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "sklearn.feature_extraction.DictVectorizer")
 when used along with the customized function `token_freqs` as done in the previous section. The difference being that [`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
 is more flexible. In particular it accepts various regex patterns through the `token_pattern` parameter.

from sklearn.feature\_extraction.text import [CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")

t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
vectorizer \= [CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
()
vectorizer.fit\_transform(raw\_data)
duration \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0
dict\_count\_vectorizers\["vectorizer"\].append(vectorizer.\_\_class\_\_.\_\_name\_\_)
dict\_count\_vectorizers\["speed"\].append(data\_size\_mb / duration)
print(f"done in {duration:.3f} s at {data\_size\_mb / duration:.1f} MB/s")
print(f"Found {len(vectorizer.get\_feature\_names\_out())} unique terms")

Copy to clipboard

done in 0.667 s at 9.4 MB/s
Found 47885 unique terms

Copy to clipboard

We see that using the [`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
 implementation is approximately twice as fast as using the [`DictVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "sklearn.feature_extraction.DictVectorizer")
 along with the simple function we defined for mapping the tokens. The reason is that [`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
 is optimized by reusing a compiled regular expression for the full training set instead of creating one per document as done in our naive tokenize function.

Now we make a similar experiment with the [`HashingVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")
, which is equivalent to combining the “hashing trick” implemented by the [`FeatureHasher`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")
 class and the text preprocessing and tokenization of the [`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
.

from sklearn.feature\_extraction.text import [HashingVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")

t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
vectorizer \= [HashingVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")
(n\_features\=2\*\*18)
vectorizer.fit\_transform(raw\_data)
duration \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0
dict\_count\_vectorizers\["vectorizer"\].append(vectorizer.\_\_class\_\_.\_\_name\_\_)
dict\_count\_vectorizers\["speed"\].append(data\_size\_mb / duration)
print(f"done in {duration:.3f} s at {data\_size\_mb / duration:.1f} MB/s")

Copy to clipboard

done in 0.492 s at 12.7 MB/s

Copy to clipboard

We can observe that this is the fastest text tokenization strategy so far, assuming that the downstream machine learning task can tolerate a few collisions.

TfidfVectorizer[#](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html#tfidfvectorizer "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

In a large text corpus, some words appear with higher frequency (e.g. “the”, “a”, “is” in English) and do not carry meaningful information about the actual contents of a document. If we were to feed the word count data directly to a classifier, those very common terms would shadow the frequencies of rarer yet more informative terms. In order to re-weight the count features into floating point values suitable for usage by a classifier it is very common to use the tf-idf transform as implemented by the [`TfidfTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer")
. TF stands for “term-frequency” while “tf-idf” means term-frequency times inverse document-frequency.

We now benchmark the [`TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
, which is equivalent to combining the tokenization and occurrence counting of the [`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
 along with the normalizing and weighting from a [`TfidfTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer")
.

from sklearn.feature\_extraction.text import [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")

t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
vectorizer \= [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
()
vectorizer.fit\_transform(raw\_data)
duration \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0
dict\_count\_vectorizers\["vectorizer"\].append(vectorizer.\_\_class\_\_.\_\_name\_\_)
dict\_count\_vectorizers\["speed"\].append(data\_size\_mb / duration)
print(f"done in {duration:.3f} s at {data\_size\_mb / duration:.1f} MB/s")
print(f"Found {len(vectorizer.get\_feature\_names\_out())} unique terms")

Copy to clipboard

done in 0.666 s at 9.4 MB/s
Found 47885 unique terms

Copy to clipboard

Summary[#](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html#summary "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

Let’s conclude this notebook by summarizing all the recorded processing speeds in a single plot:

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(12, 6))

y\_pos \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len(dict\_count\_vectorizers\["vectorizer"\]))
ax.barh(y\_pos, dict\_count\_vectorizers\["speed"\], align\="center")
ax.set\_yticks(y\_pos)
ax.set\_yticklabels(dict\_count\_vectorizers\["vectorizer"\])
ax.invert\_yaxis()
\_ \= ax.set\_xlabel("speed (MB/s)")

Copy to clipboard

![plot hashing vs dict vectorizer](https://scikit-learn.org/stable/_images/sphx_glr_plot_hashing_vs_dict_vectorizer_002.png)

Notice from the plot that [`TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
 is slightly slower than [`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
 because of the extra operation induced by the [`TfidfTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer")
.

Also notice that, by setting the number of features `n_features = 2**18`, the [`HashingVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")
 performs better than the [`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
 at the expense of inversibility of the transformation due to hash collisions.

We highlight that [`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
 and [`HashingVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")
 perform better than their equivalent [`DictVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "sklearn.feature_extraction.DictVectorizer")
 and [`FeatureHasher`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")
 on manually tokenized documents since the internal tokenization step of the former vectorizers compiles a regular expression once and then reuses it for all the documents.

**Total running time of the script:** (0 minutes 4.936 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo32.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/text/plot_hashing_vs_dict_vectorizer.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo32.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/text/plot_hashing_vs_dict_vectorizer.ipynb)

[`Download Jupyter notebook: plot_hashing_vs_dict_vectorizer.ipynb`](https://scikit-learn.org/stable/_downloads/06cfc926acb27652fb2aa5bfc583e7cb/plot_hashing_vs_dict_vectorizer.ipynb)

[`Download Python source code: plot_hashing_vs_dict_vectorizer.py`](https://scikit-learn.org/stable/_downloads/5775388ede077a05b00514ecbaa17f32/plot_hashing_vs_dict_vectorizer.py)

[`Download zipped: plot_hashing_vs_dict_vectorizer.zip`](https://scikit-learn.org/stable/_downloads/0358b1921962fd7c6f5a94c5abc91476/plot_hashing_vs_dict_vectorizer.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_clustering_thumb.png)

[Clustering text documents using k-means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html)

Clustering text documents using k-means

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_classification_20newsgroups_thumb.png)

[Classification of text documents using sparse features](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html)

Classification of text documents using sparse features

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_bicluster_newsgroups_thumb.png)

[Biclustering documents with the Spectral Co-clustering algorithm](https://scikit-learn.org/stable/auto_examples/bicluster/plot_bicluster_newsgroups.html)

Biclustering documents with the Spectral Co-clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_column_transformer_thumb.png)

[Column Transformer with Heterogeneous Data Sources](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer.html)

Column Transformer with Heterogeneous Data Sources

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/5775388ede077a05b00514ecbaa17f32/plot_hashing_vs_dict_vectorizer.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/06cfc926acb27652fb2aa5bfc583e7cb/plot_hashing_vs_dict_vectorizer.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/0358b1921962fd7c6f5a94c5abc91476/plot_hashing_vs_dict_vectorizer.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo32.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/text/plot_hashing_vs_dict_vectorizer.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo32.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/text/plot_hashing_vs_dict_vectorizer.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)