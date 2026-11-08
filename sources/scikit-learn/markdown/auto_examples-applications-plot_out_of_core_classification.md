[Skip to main content](https://scikit-learn.org/stable/auto_examples/applications/plot_out_of_core_classification.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/applications/plot_out_of_core_classification.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/applications/plot_out_of_core_classification.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/applications/plot_out_of_core_classification.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/applications/plot_out_of_core_classification.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/applications/plot_out_of_core_classification.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/applications/plot_out_of_core_classification.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/applications/plot_out_of_core_classification.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/applications/plot_out_of_core_classification.html#sphx-glr-download-auto-examples-applications-plot-out-of-core-classification-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Out-of-core classification of text documents[#](https://scikit-learn.org/stable/auto_examples/applications/plot_out_of_core_classification.html#out-of-core-classification-of-text-documents "Link to this heading")

=====================================================================================================================================================================================================================

This is an example showing how scikit-learn can be used for classification using an out-of-core approach: learning from data that doesn’t fit into main memory. We make use of an online classifier, i.e., one that supports the partial\_fit method, that will be fed with batches of examples. To guarantee that the features space remains the same over time we leverage a HashingVectorizer that will project each example into the same feature space. This is especially useful in the case of text classification where new features (words) may appear in each batch.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import itertools
import re
import sys
import tarfile
import time
from hashlib import [sha256](https://docs.python.org/3/library/hashlib.html#hashlib.sha256 "hashlib.sha256")
from html.parser import [HTMLParser](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser "html.parser.HTMLParser")
from pathlib import [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")
from urllib.request import [urlretrieve](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlretrieve "urllib.request.urlretrieve")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import [rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")

from sklearn.datasets import [get\_data\_home](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.get_data_home.html#sklearn.datasets.get_data_home "sklearn.datasets.get_data_home")
from sklearn.feature\_extraction.text import [HashingVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")
from sklearn.linear\_model import [Perceptron](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html#sklearn.linear_model.Perceptron "sklearn.linear_model.Perceptron")
, [SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
from sklearn.naive\_bayes import [MultinomialNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB "sklearn.naive_bayes.MultinomialNB")

def \_not\_in\_sphinx():
    \# Hack to detect whether we are running by the sphinx builder
    return "\_\_file\_\_" in globals()

Copy to clipboard

Reuters Dataset related routines[#](https://scikit-learn.org/stable/auto_examples/applications/plot_out_of_core_classification.html#reuters-dataset-related-routines "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The dataset used in this example is Reuters-21578 as provided by the UCI ML repository. It will be automatically downloaded and uncompressed on first run.

class ReutersParser([HTMLParser](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser "html.parser.HTMLParser")
):
    """Utility class to parse an SGML file and yield documents one at a time."""

    def \_\_init\_\_(self, encoding\="latin-1"):
        [HTMLParser](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser "html.parser.HTMLParser")
.\_\_init\_\_(self)
        self.\_reset()
        self.encoding \= encoding

    def handle\_starttag(self, tag, attrs):
        method \= "start\_" + tag
        getattr(self, method, lambda x: None)(attrs)

    def handle\_endtag(self, tag):
        method \= "end\_" + tag
        getattr(self, method, lambda: None)()

    def \_reset(self):
        self.in\_title \= 0
        self.in\_body \= 0
        self.in\_topics \= 0
        self.in\_topic\_d \= 0
        self.title \= ""
        self.body \= ""
        self.topics \= \[\]
        self.topic\_d \= ""

    def parse(self, fd):
        self.docs \= \[\]
        for chunk in fd:
            self.feed(chunk.decode(self.encoding))
            for doc in self.docs:
                yield doc
            self.docs \= \[\]
        self.close()

    def handle\_data(self, data):
        if self.in\_body:
            self.body += data
        elif self.in\_title:
            self.title += data
        elif self.in\_topic\_d:
            self.topic\_d += data

    def start\_reuters(self, attributes):
        pass

    def end\_reuters(self):
        self.body \= [re.sub](https://docs.python.org/3/library/re.html#re.sub "re.sub")
(r"\\s+", r" ", self.body)
        self.docs.append(
            {"title": self.title, "body": self.body, "topics": self.topics}
        )
        self.\_reset()

    def start\_title(self, attributes):
        self.in\_title \= 1

    def end\_title(self):
        self.in\_title \= 0

    def start\_body(self, attributes):
        self.in\_body \= 1

    def end\_body(self):
        self.in\_body \= 0

    def start\_topics(self, attributes):
        self.in\_topics \= 1

    def end\_topics(self):
        self.in\_topics \= 0

    def start\_d(self, attributes):
        self.in\_topic\_d \= 1

    def end\_d(self):
        self.in\_topic\_d \= 0
        self.topics.append(self.topic\_d)
        self.topic\_d \= ""

def stream\_reuters\_documents(data\_path\=None):
    """Iterate over documents of the Reuters dataset.

    The Reuters archive will automatically be downloaded and uncompressed if
    the \`data\_path\` directory does not exist.

    Documents are represented as dictionaries with 'body' (str),
    'title' (str), 'topics' (list(str)) keys.

    """

    DOWNLOAD\_URL \= "https://kdd.ics.uci.edu/databases/reuters21578/reuters21578.tar.gz"
    ARCHIVE\_SHA256 \= "3bae43c9b14e387f76a61b6d82bf98a4fb5d3ef99ef7e7075ff2ccbcf59f9d30"
    ARCHIVE\_FILENAME \= "reuters21578.tar.gz"

    if data\_path is None:
        data\_path \= [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")
([get\_data\_home](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.get_data_home.html#sklearn.datasets.get_data_home "sklearn.datasets.get_data_home")
()) / "reuters"
    else:
        data\_path \= [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")
(data\_path)
    if not data\_path.exists():
        """Download the dataset."""
        print("downloading dataset (once and for all) into %s" % data\_path)
        data\_path.mkdir(parents\=True, exist\_ok\=True)

        def progress(blocknum, bs, size):
            total\_sz\_mb \= "%.2f MB" % (size / 1e6)
            current\_sz\_mb \= "%.2f MB" % ((blocknum \* bs) / 1e6)
            if \_not\_in\_sphinx():
                sys.stdout.write("\\rdownloaded %s / %s" % (current\_sz\_mb, total\_sz\_mb))

        archive\_path \= data\_path / ARCHIVE\_FILENAME

        [urlretrieve](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlretrieve "urllib.request.urlretrieve")
(DOWNLOAD\_URL, filename\=archive\_path, reporthook\=progress)
        if \_not\_in\_sphinx():
            sys.stdout.write("\\r")

        \# Check that the archive was not tampered:
        assert [sha256](https://docs.python.org/3/library/hashlib.html#hashlib.sha256 "hashlib.sha256")
(archive\_path.read\_bytes()).hexdigest() \== ARCHIVE\_SHA256

        print("untarring Reuters dataset...")
        with [tarfile.open](https://docs.python.org/3/library/tarfile.html#tarfile.open "tarfile.open")
(archive\_path, "r:gz") as fp:
            fp.extractall(data\_path, filter\="data")
        print("done.")

    parser \= ReutersParser()
    for filename in data\_path.glob("\*.sgm"):
        for doc in parser.parse(open(filename, "rb")):
            yield doc

Copy to clipboard

Main[#](https://scikit-learn.org/stable/auto_examples/applications/plot_out_of_core_classification.html#main "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

Create the vectorizer and limit the number of features to a reasonable maximum

vectorizer \= [HashingVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")
(
    decode\_error\="ignore", n\_features\=2\*\*18, alternate\_sign\=False
)

\# Iterator over parsed Reuters SGML files.
data\_stream \= stream\_reuters\_documents()

\# We learn a binary classification between the "acq" class and all the others.
\# "acq" was chosen as it is more or less evenly distributed in the Reuters
\# files. For other datasets, one should take care of creating a test set with
\# a realistic portion of positive instances.
all\_classes \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[0, 1\])
positive\_class \= "acq"

\# Here are some classifiers that support the \`partial\_fit\` method
partial\_fit\_classifiers \= {
    "SGD": [SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
(max\_iter\=5),
    "Perceptron": [Perceptron](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html#sklearn.linear_model.Perceptron "sklearn.linear_model.Perceptron")
(),
    "NB Multinomial": [MultinomialNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB "sklearn.naive_bayes.MultinomialNB")
(alpha\=0.01),
    "Passive-Aggressive": [SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
(
        loss\="hinge", penalty\=None, learning\_rate\="pa1", eta0\=1.0
    ),
}

def get\_minibatch(doc\_iter, size, pos\_class\=positive\_class):
    """Extract a minibatch of examples, return a tuple X\_text, y.

    Note: size is before excluding invalid docs with no topics assigned.

    """
    data \= \[\
        ("{title}\\n\\n{body}".format(\*\*doc), pos\_class in doc\["topics"\])\
        for doc in [itertools.islice](https://docs.python.org/3/library/itertools.html#itertools.islice "itertools.islice")\
(doc\_iter, size)\
        if doc\["topics"\]\
    \]
    if not len(data):
        return [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
(\[\], dtype\=int), [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
(\[\], dtype\=int)
    X\_text, y \= zip(\*data)
    return X\_text, [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
(y, dtype\=int)

def iter\_minibatches(doc\_iter, minibatch\_size):
    """Generator of minibatches."""
    X\_text, y \= get\_minibatch(doc\_iter, minibatch\_size)
    while len(X\_text):
        yield X\_text, y
        X\_text, y \= get\_minibatch(doc\_iter, minibatch\_size)

\# test data statistics
test\_stats \= {"n\_test": 0, "n\_test\_pos": 0}

\# First we hold out a number of examples to estimate accuracy
n\_test\_documents \= 1000
tick \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
X\_test\_text, y\_test \= get\_minibatch(data\_stream, 1000)
parsing\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- tick
tick \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
X\_test \= vectorizer.transform(X\_test\_text)
vectorizing\_time \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- tick
test\_stats\["n\_test"\] += len(y\_test)
test\_stats\["n\_test\_pos"\] += sum(y\_test)
print("Test set is %d documents (%d positive)" % (len(y\_test), sum(y\_test)))

def progress(cls\_name, stats):
    """Report progress information, return a string."""
    duration \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- stats\["t0"\]
    s \= "%20s classifier : \\t" % cls\_name
    s += "%(n\_train)6d train docs (%(n\_train\_pos)6d positive) " % stats
    s += "%(n\_test)6d test docs (%(n\_test\_pos)6d positive) " % test\_stats
    s += "accuracy: %(accuracy).3f " % stats
    s += "in %.2fs (%5d docs/s)" % (duration, stats\["n\_train"\] / duration)
    return s

cls\_stats \= {}

for cls\_name in partial\_fit\_classifiers:
    stats \= {
        "n\_train": 0,
        "n\_train\_pos": 0,
        "accuracy": 0.0,
        "accuracy\_history": \[(0, 0)\],
        "t0": [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
(),
        "runtime\_history": \[(0, 0)\],
        "total\_fit\_time": 0.0,
    }
    cls\_stats\[cls\_name\] \= stats

get\_minibatch(data\_stream, n\_test\_documents)
\# Discard test set

\# We will feed the classifier with mini-batches of 1000 documents; this means
\# we have at most 1000 docs in memory at any time.  The smaller the document
\# batch, the bigger the relative overhead of the partial fit methods.
minibatch\_size \= 1000

\# Create the data\_stream that parses Reuters SGML files and iterates on
\# documents as a stream.
minibatch\_iterators \= iter\_minibatches(data\_stream, minibatch\_size)
total\_vect\_time \= 0.0

\# Main loop : iterate on mini-batches of examples
for i, (X\_train\_text, y\_train) in enumerate(minibatch\_iterators):
    tick \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    X\_train \= vectorizer.transform(X\_train\_text)
    total\_vect\_time += [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- tick

    for cls\_name, cls in partial\_fit\_classifiers.items():
        tick \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
        \# update estimator with examples in the current mini-batch
        cls.partial\_fit(X\_train, y\_train, classes\=all\_classes)

        \# accumulate test accuracy stats
        cls\_stats\[cls\_name\]\["total\_fit\_time"\] += [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- tick
        cls\_stats\[cls\_name\]\["n\_train"\] += X\_train.shape\[0\]
        cls\_stats\[cls\_name\]\["n\_train\_pos"\] += sum(y\_train)
        tick \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
        cls\_stats\[cls\_name\]\["accuracy"\] \= cls.score(X\_test, y\_test)
        cls\_stats\[cls\_name\]\["prediction\_time"\] \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- tick
        acc\_history \= (cls\_stats\[cls\_name\]\["accuracy"\], cls\_stats\[cls\_name\]\["n\_train"\])
        cls\_stats\[cls\_name\]\["accuracy\_history"\].append(acc\_history)
        run\_history \= (
            cls\_stats\[cls\_name\]\["accuracy"\],
            total\_vect\_time + cls\_stats\[cls\_name\]\["total\_fit\_time"\],
        )
        cls\_stats\[cls\_name\]\["runtime\_history"\].append(run\_history)

        if i % 3 \== 0:
            print(progress(cls\_name, cls\_stats\[cls\_name\]))
    if i % 3 \== 0:
        print("\\n")

Copy to clipboard

Test set is 878 documents (108 positive)
                 SGD classifier :          962 train docs (   132 positive)    878 test docs (   108 positive) accuracy: 0.915 in 0.51s ( 1901 docs/s)
          Perceptron classifier :          962 train docs (   132 positive)    878 test docs (   108 positive) accuracy: 0.855 in 0.51s ( 1888 docs/s)
      NB Multinomial classifier :          962 train docs (   132 positive)    878 test docs (   108 positive) accuracy: 0.877 in 0.52s ( 1854 docs/s)
  Passive-Aggressive classifier :          962 train docs (   132 positive)    878 test docs (   108 positive) accuracy: 0.933 in 0.52s ( 1841 docs/s)


                 SGD classifier :         3911 train docs (   517 positive)    878 test docs (   108 positive) accuracy: 0.938 in 1.46s ( 2671 docs/s)
          Perceptron classifier :         3911 train docs (   517 positive)    878 test docs (   108 positive) accuracy: 0.936 in 1.47s ( 2665 docs/s)
      NB Multinomial classifier :         3911 train docs (   517 positive)    878 test docs (   108 positive) accuracy: 0.885 in 1.48s ( 2650 docs/s)
  Passive-Aggressive classifier :         3911 train docs (   517 positive)    878 test docs (   108 positive) accuracy: 0.941 in 1.48s ( 2645 docs/s)


                 SGD classifier :         6821 train docs (   891 positive)    878 test docs (   108 positive) accuracy: 0.952 in 2.39s ( 2851 docs/s)
          Perceptron classifier :         6821 train docs (   891 positive)    878 test docs (   108 positive) accuracy: 0.952 in 2.40s ( 2847 docs/s)
      NB Multinomial classifier :         6821 train docs (   891 positive)    878 test docs (   108 positive) accuracy: 0.900 in 2.40s ( 2837 docs/s)
  Passive-Aggressive classifier :         6821 train docs (   891 positive)    878 test docs (   108 positive) accuracy: 0.953 in 2.41s ( 2833 docs/s)


                 SGD classifier :         9759 train docs (  1276 positive)    878 test docs (   108 positive) accuracy: 0.949 in 3.36s ( 2905 docs/s)
          Perceptron classifier :         9759 train docs (  1276 positive)    878 test docs (   108 positive) accuracy: 0.953 in 3.36s ( 2903 docs/s)
      NB Multinomial classifier :         9759 train docs (  1276 positive)    878 test docs (   108 positive) accuracy: 0.909 in 3.37s ( 2896 docs/s)
  Passive-Aggressive classifier :         9759 train docs (  1276 positive)    878 test docs (   108 positive) accuracy: 0.958 in 3.37s ( 2893 docs/s)


                 SGD classifier :        11680 train docs (  1499 positive)    878 test docs (   108 positive) accuracy: 0.944 in 4.20s ( 2778 docs/s)
          Perceptron classifier :        11680 train docs (  1499 positive)    878 test docs (   108 positive) accuracy: 0.956 in 4.21s ( 2777 docs/s)
      NB Multinomial classifier :        11680 train docs (  1499 positive)    878 test docs (   108 positive) accuracy: 0.915 in 4.21s ( 2771 docs/s)
  Passive-Aggressive classifier :        11680 train docs (  1499 positive)    878 test docs (   108 positive) accuracy: 0.950 in 4.22s ( 2769 docs/s)


                 SGD classifier :        14625 train docs (  1865 positive)    878 test docs (   108 positive) accuracy: 0.965 in 5.18s ( 2822 docs/s)
          Perceptron classifier :        14625 train docs (  1865 positive)    878 test docs (   108 positive) accuracy: 0.903 in 5.19s ( 2820 docs/s)
      NB Multinomial classifier :        14625 train docs (  1865 positive)    878 test docs (   108 positive) accuracy: 0.924 in 5.19s ( 2815 docs/s)
  Passive-Aggressive classifier :        14625 train docs (  1865 positive)    878 test docs (   108 positive) accuracy: 0.957 in 5.20s ( 2814 docs/s)


                 SGD classifier :        17360 train docs (  2179 positive)    878 test docs (   108 positive) accuracy: 0.957 in 6.06s ( 2864 docs/s)
          Perceptron classifier :        17360 train docs (  2179 positive)    878 test docs (   108 positive) accuracy: 0.933 in 6.06s ( 2863 docs/s)
      NB Multinomial classifier :        17360 train docs (  2179 positive)    878 test docs (   108 positive) accuracy: 0.932 in 6.07s ( 2859 docs/s)
  Passive-Aggressive classifier :        17360 train docs (  2179 positive)    878 test docs (   108 positive) accuracy: 0.952 in 6.07s ( 2858 docs/s)

Copy to clipboard

Plot results[#](https://scikit-learn.org/stable/auto_examples/applications/plot_out_of_core_classification.html#plot-results "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

The plot represents the learning curve of the classifier: the evolution of classification accuracy over the course of the mini-batches. Accuracy is measured on the first 1000 samples, held out as a validation set.

To limit the memory consumption, we queue examples up to a fixed amount before feeding them to the learner.

def plot\_accuracy(x, y, x\_legend):
    """Plot accuracy as a function of x."""
    x \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(x)
    y \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(y)
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Classification accuracy as a function of %s" % x\_legend)
    [plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("%s" % x\_legend)
    [plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Accuracy")
    [plt.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid "matplotlib.pyplot.grid")
(True)
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(x, y)

[rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
\["legend.fontsize"\] \= 10
cls\_names \= list(sorted(cls\_stats.keys()))

\# Plot accuracy evolution
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
for \_, stats in sorted(cls\_stats.items()):
    \# Plot accuracy evolution with #examples
    accuracy, n\_examples \= zip(\*stats\["accuracy\_history"\])
    plot\_accuracy(n\_examples, accuracy, "training examples (#)")
    ax \= [plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
()
    ax.set\_ylim((0.8, 1))
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(cls\_names, loc\="best")

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
for \_, stats in sorted(cls\_stats.items()):
    \# Plot accuracy evolution with runtime
    accuracy, runtime \= zip(\*stats\["runtime\_history"\])
    plot\_accuracy(runtime, accuracy, "runtime (s)")
    ax \= [plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
()
    ax.set\_ylim((0.8, 1))
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(cls\_names, loc\="best")

\# Plot fitting times
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
fig \= [plt.gcf](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gcf.html#matplotlib.pyplot.gcf "matplotlib.pyplot.gcf")
()
cls\_runtime \= \[stats\["total\_fit\_time"\] for cls\_name, stats in sorted(cls\_stats.items())\]

cls\_runtime.append(total\_vect\_time)
cls\_names.append("Vectorization")
bar\_colors \= \["b", "g", "r", "c", "m", "y"\]

ax \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(111)
rectangles \= [plt.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "matplotlib.pyplot.bar")
(range(len(cls\_names)), cls\_runtime, width\=0.5, color\=bar\_colors)

ax.set\_xticks([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, len(cls\_names) \- 1, len(cls\_names)))
ax.set\_xticklabels(cls\_names, fontsize\=10)
ymax \= max(cls\_runtime) \* 1.2
ax.set\_ylim((0, ymax))
ax.set\_ylabel("runtime (s)")
ax.set\_title("Training Times")

def autolabel(rectangles):
    """attach some text vi autolabel on rectangles."""
    for rect in rectangles:
        height \= rect.get\_height()
        ax.text(
            rect.get\_x() + rect.get\_width() / 2.0,
            1.05 \* height,
            "%.4f" % height,
            ha\="center",
            va\="bottom",
        )
        [plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
([plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
()\[1\], rotation\=30)

autolabel(rectangles)
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

\# Plot prediction times
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
cls\_runtime \= \[\]
cls\_names \= list(sorted(cls\_stats.keys()))
for cls\_name, stats in sorted(cls\_stats.items()):
    cls\_runtime.append(stats\["prediction\_time"\])
cls\_runtime.append(parsing\_time)
cls\_names.append("Read/Parse\\n+Feat.Extr.")
cls\_runtime.append(vectorizing\_time)
cls\_names.append("Hashing\\n+Vect.")

ax \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(111)
rectangles \= [plt.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "matplotlib.pyplot.bar")
(range(len(cls\_names)), cls\_runtime, width\=0.5, color\=bar\_colors)

ax.set\_xticks([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, len(cls\_names) \- 1, len(cls\_names)))
ax.set\_xticklabels(cls\_names, fontsize\=8)
[plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
([plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
()\[1\], rotation\=30)
ymax \= max(cls\_runtime) \* 1.2
ax.set\_ylim((0, ymax))
ax.set\_ylabel("runtime (s)")
ax.set\_title("Prediction Times (%d instances)" % n\_test\_documents)
autolabel(rectangles)
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

*   ![Classification accuracy as a function of training examples (#)](https://scikit-learn.org/stable/_images/sphx_glr_plot_out_of_core_classification_001.png)
*   ![Classification accuracy as a function of runtime (s)](https://scikit-learn.org/stable/_images/sphx_glr_plot_out_of_core_classification_002.png)
*   ![Training Times](https://scikit-learn.org/stable/_images/sphx_glr_plot_out_of_core_classification_003.png)
*   ![Prediction Times (1000 instances)](https://scikit-learn.org/stable/_images/sphx_glr_plot_out_of_core_classification_004.png)

**Total running time of the script:** (0 minutes 6.993 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_out_of_core_classification.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_out_of_core_classification.ipynb)

[`Download Jupyter notebook: plot_out_of_core_classification.ipynb`](https://scikit-learn.org/stable/_downloads/c08598f3ffe66017f7cad294026ee0b9/plot_out_of_core_classification.ipynb)

[`Download Python source code: plot_out_of_core_classification.py`](https://scikit-learn.org/stable/_downloads/f7c999465d2f8d68e0c04bec778aa48e/plot_out_of_core_classification.py)

[`Download zipped: plot_out_of_core_classification.zip`](https://scikit-learn.org/stable/_downloads/553e920694cd9978815f721f868d3509/plot_out_of_core_classification.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_classification_20newsgroups_thumb.png)

[Classification of text documents using sparse features](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html)

Classification of text documents using sparse features

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_prediction_latency_thumb.png)

[Prediction Latency](https://scikit-learn.org/stable/auto_examples/applications/plot_prediction_latency.html)

Prediction Latency

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_column_transformer_thumb.png)

[Column Transformer with Heterogeneous Data Sources](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer.html)

Column Transformer with Heterogeneous Data Sources

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hashing_vs_dict_vectorizer_thumb.png)

[FeatureHasher and DictVectorizer Comparison](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html)

FeatureHasher and DictVectorizer Comparison

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/f7c999465d2f8d68e0c04bec778aa48e/plot_out_of_core_classification.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/c08598f3ffe66017f7cad294026ee0b9/plot_out_of_core_classification.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/553e920694cd9978815f721f868d3509/plot_out_of_core_classification.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_out_of_core_classification.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_out_of_core_classification.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)