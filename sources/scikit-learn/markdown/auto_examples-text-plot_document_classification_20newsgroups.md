[Skip to main content](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/text/plot_document_classification_20newsgroups.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/text/plot_document_classification_20newsgroups.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/text/plot_document_classification_20newsgroups.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/text/plot_document_classification_20newsgroups.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/text/plot_document_classification_20newsgroups.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/text/plot_document_classification_20newsgroups.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html#sphx-glr-download-auto-examples-text-plot-document-classification-20newsgroups-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Classification of text documents using sparse features[#](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html#classification-of-text-documents-using-sparse-features "Link to this heading")

===========================================================================================================================================================================================================================================

This is an example showing how scikit-learn can be used to classify documents by topics using a [Bag of Words approach](https://en.wikipedia.org/wiki/Bag-of-words_model)
. This example uses a Tf-idf-weighted document-term sparse matrix to encode the features and demonstrates various classifiers that can efficiently handle sparse matrices.

For document analysis via an unsupervised learning approach, see the example script [Clustering text documents using k-means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html#sphx-glr-auto-examples-text-plot-document-clustering-py)
.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Loading and vectorizing the 20 newsgroups text dataset[#](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html#loading-and-vectorizing-the-20-newsgroups-text-dataset "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We define a function to load data from [The 20 newsgroups text dataset](https://scikit-learn.org/stable/datasets/real_world.html#newsgroups-dataset)
, which comprises around 18,000 newsgroups posts on 20 topics split in two subsets: one for training (or development) and the other one for testing (or for performance evaluation). Note that, by default, the text samples contain some message metadata such as `'headers'`, `'footers'` (signatures) and `'quotes'` to other posts. The `fetch_20newsgroups` function therefore accepts a parameter named `remove` to attempt stripping such information that can make the classification problem “too easy”. This is achieved using simple heuristics that are neither perfect nor standard, hence disabled by default.

from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")

from sklearn.datasets import [fetch\_20newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")
from sklearn.feature\_extraction.text import [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")

categories \= \[\
    "alt.atheism",\
    "talk.religion.misc",\
    "comp.graphics",\
    "sci.space",\
\]

def size\_mb(docs):
    return sum(len(s.encode("utf-8")) for s in docs) / 1e6

def load\_dataset(verbose\=False, remove\=()):
    """Load and vectorize the 20 newsgroups dataset."""

    data\_train \= [fetch\_20newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")
(
        subset\="train",
        categories\=categories,
        shuffle\=True,
        random\_state\=42,
        remove\=remove,
    )

    data\_test \= [fetch\_20newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")
(
        subset\="test",
        categories\=categories,
        shuffle\=True,
        random\_state\=42,
        remove\=remove,
    )

    \# order of labels in \`target\_names\` can be different from \`categories\`
    target\_names \= data\_train.target\_names

    \# split target in a training set and a test set
    y\_train, y\_test \= data\_train.target, data\_test.target

    \# Extracting features from the training data using a sparse vectorizer
    t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    vectorizer \= [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
(
        sublinear\_tf\=True, max\_df\=0.5, min\_df\=5, stop\_words\="english"
    )
    X\_train \= vectorizer.fit\_transform(data\_train.data)
    duration\_train \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0

    \# Extracting features from the test data using the same vectorizer
    t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    X\_test \= vectorizer.transform(data\_test.data)
    duration\_test \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0

    feature\_names \= vectorizer.get\_feature\_names\_out()

    if verbose:
        \# compute size of loaded data
        data\_train\_size\_mb \= size\_mb(data\_train.data)
        data\_test\_size\_mb \= size\_mb(data\_test.data)

        print(
            f"{len(data\_train.data)} documents - "
            f"{data\_train\_size\_mb:.2f}MB (training set)"
        )
        print(f"{len(data\_test.data)} documents - {data\_test\_size\_mb:.2f}MB (test set)")
        print(f"{len(target\_names)} categories")
        print(
            f"vectorize training done in {duration\_train:.3f}s "
            f"at {data\_train\_size\_mb / duration\_train:.3f}MB/s"
        )
        print(f"n\_samples: {X\_train.shape\[0\]}, n\_features: {X\_train.shape\[1\]}")
        print(
            f"vectorize testing done in {duration\_test:.3f}s "
            f"at {data\_test\_size\_mb / duration\_test:.3f}MB/s"
        )
        print(f"n\_samples: {X\_test.shape\[0\]}, n\_features: {X\_test.shape\[1\]}")

    return X\_train, X\_test, y\_train, y\_test, feature\_names, target\_names

Copy to clipboard

Analysis of a bag-of-words document classifier[#](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html#analysis-of-a-bag-of-words-document-classifier "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We will now train a classifier twice, once on the text samples including metadata and once after stripping the metadata. For both cases we will analyze the classification errors on a test set using a confusion matrix and inspect the coefficients that define the classification function of the trained models.

### Model without metadata stripping[#](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html#model-without-metadata-stripping "Link to this heading")

We start by using the custom function `load_dataset` to load the data without metadata stripping.

X\_train, X\_test, y\_train, y\_test, feature\_names, target\_names \= load\_dataset(
    verbose\=True
)

Copy to clipboard

2034 documents - 3.98MB (training set)
1353 documents - 2.87MB (test set)
4 categories
vectorize training done in 0.365s at 10.890MB/s
n\_samples: 2034, n\_features: 7831
vectorize testing done in 0.232s at 12.384MB/s
n\_samples: 1353, n\_features: 7831

Copy to clipboard

Our first model is an instance of the [`RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")
 class. This is a linear classification model that uses the mean squared error on {-1, 1} encoded targets, one for each possible class. Contrary to [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
, [`RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")
 does not provide probabilistic predictions (no `predict_proba` method), but it is often faster to train.

from sklearn.linear\_model import [RidgeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")

clf \= [RidgeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")
(tol\=1e-2, solver\="sparse\_cg")
clf.fit(X\_train, y\_train)
pred \= clf.predict(X\_test)

Copy to clipboard

We plot the confusion matrix of this classifier to find if there is a pattern in the classification errors.

import matplotlib.pyplot as plt

from sklearn.metrics import ConfusionMatrixDisplay

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(10, 5))
[ConfusionMatrixDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_predictions "sklearn.metrics.ConfusionMatrixDisplay.from_predictions")
(y\_test, pred, ax\=ax)
ax.xaxis.set\_ticklabels(target\_names)
ax.yaxis.set\_ticklabels(target\_names)
\_ \= ax.set\_title(
    f"Confusion Matrix for {clf.\_\_class\_\_.\_\_name\_\_}\\non the original documents"
)

Copy to clipboard

![Confusion Matrix for RidgeClassifier on the original documents](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_classification_20newsgroups_001.png)

The confusion matrix highlights that documents of the `alt.atheism` class are often confused with documents with the class `talk.religion.misc` class and vice-versa which is expected since the topics are semantically related.

We also observe that some documents of the `sci.space` class can be misclassified as `comp.graphics` while the converse is much rarer. A manual inspection of those badly classified documents would be required to get some insights on this asymmetry. It could be the case that the vocabulary of the space topic could be more specific than the vocabulary for computer graphics.

We can gain a deeper understanding of how this classifier makes its decisions by looking at the words with the highest average feature effects:

import numpy as np
import pandas as pd

def plot\_feature\_effects():
    \# learned coefficients weighted by frequency of appearance
    average\_feature\_effects \= clf.coef\_ \* [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
(X\_train.mean(axis\=0)).ravel()

    for i, label in enumerate(target\_names):
        top5 \= [np.argsort](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")
(average\_feature\_effects\[i\])\[\-5:\]\[::\-1\]
        if i \== 0:
            top \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(feature\_names\[top5\], columns\=\[label\])
            top\_indices \= top5
        else:
            top\[label\] \= feature\_names\[top5\]
            top\_indices \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
((top\_indices, top5), axis\=None)
    top\_indices \= [np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
(top\_indices)
    predictive\_words \= feature\_names\[top\_indices\]

    \# plot feature effects
    bar\_size \= 0.25
    padding \= 0.75
    y\_locs \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len(top\_indices)) \* (4 \* bar\_size + padding)

    fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(10, 8))
    for i, label in enumerate(target\_names):
        ax.barh(
            y\_locs + (i \- 2) \* bar\_size,
            average\_feature\_effects\[i, top\_indices\],
            height\=bar\_size,
            label\=label,
        )
    ax.set(
        yticks\=y\_locs,
        yticklabels\=predictive\_words,
        ylim\=\[\
            0 \- 4 \* bar\_size,\
            len(top\_indices) \* (4 \* bar\_size + padding) \- 4 \* bar\_size,\
        \],
    )
    ax.legend(loc\="lower right")

    print("top 5 keywords per class:")
    print(top)

    return ax

\_ \= plot\_feature\_effects().set\_title("Average feature effect on the original data")

Copy to clipboard

![Average feature effect on the original data](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_classification_20newsgroups_002.png)

top 5 keywords per class:
  alt.atheism comp.graphics sci.space talk.religion.misc
0       keith      graphics     space          christian
1         god    university      nasa                com
2    atheists        thanks     orbit                god
3      people          does      moon           morality
4     caltech         image    access             people

Copy to clipboard

We can observe that the most predictive words are often strongly positively associated with a single class and negatively associated with all the other classes. Most of those positive associations are quite easy to interpret. However, some words such as `"god"` and `"people"` are positively associated to both `"talk.misc.religion"` and `"alt.atheism"` as those two classes expectedly share some common vocabulary. Notice however that there are also words such as `"christian"` and `"morality"` that are only positively associated with `"talk.misc.religion"`. Furthermore, in this version of the dataset, the word `"caltech"` is one of the top predictive features for atheism due to pollution in the dataset coming from some sort of metadata such as the email addresses of the sender of previous emails in the discussion as can be seen below:

data\_train \= [fetch\_20newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")
(
    subset\="train", categories\=categories, shuffle\=True, random\_state\=42
)

for doc in data\_train.data:
    if "caltech" in doc:
        print(doc)
        break

Copy to clipboard

From: livesey@solntze.wpd.sgi.com (Jon Livesey)
Subject: Re: Morality? (was Re: <Political Atheists?)
Organization: sgi
Lines: 93
Distribution: world
NNTP-Posting-Host: solntze.wpd.sgi.com

In article <1qlettINN8oi@gap.caltech.edu>, keith@cco.caltech.edu (Keith Allan Schneider) writes:
|> livesey@solntze.wpd.sgi.com (Jon Livesey) writes:
|>
|> >>>Explain to me
|> >>>how instinctive acts can be moral acts, and I am happy to listen.
|> >>For example, if it were instinctive not to murder...
|> >
|> >Then not murdering would have no moral significance, since there
|> >would be nothing voluntary about it.
|>
|> See, there you go again, saying that a moral act is only significant
|> if it is "voluntary."  Why do you think this?

If you force me to do something, am I morally responsible for it?

|>
|> And anyway, humans have the ability to disregard some of their instincts.

Well, make up your mind.    Is it to be "instinctive not to murder"
or not?

|>
|> >>So, only intelligent beings can be moral, even if the bahavior of other
|> >>beings mimics theirs?
|> >
|> >You are starting to get the point.  Mimicry is not necessarily the
|> >same as the action being imitated.  A Parrot saying "Pretty Polly"
|> >isn't necessarily commenting on the pulchritude of Polly.
|>
|> You are attaching too many things to the term "moral," I think.
|> Let's try this:  is it "good" that animals of the same species
|> don't kill each other.  Or, do you think this is right?

It's not even correct.    Animals of the same species do kill
one another.

|>
|> Or do you think that animals are machines, and that nothing they do
|> is either right nor wrong?

Sigh.   I wonder how many times we have been round this loop.

I think that instinctive bahaviour has no moral significance.
I am quite prepared to believe that higher animals, such as
primates, have the beginnings of a moral sense, since they seem
to exhibit self-awareness.

|>
|>
|> >>Animals of the same species could kill each other arbitarily, but
|> >>they don't.
|> >
|> >They do.  I and other posters have given you many examples of exactly
|> >this, but you seem to have a very short memory.
|>
|> Those weren't arbitrary killings.  They were slayings related to some
|> sort of mating ritual or whatnot.

So what?     Are you trying to say that some killing in animals
has a moral significance and some does not?   Is this your
natural morality>


|>
|> >>Are you trying to say that this isn't an act of morality because
|> >>most animals aren't intelligent enough to think like we do?
|> >
|> >I'm saying:
|> >    "There must be the possibility that the organism - it's not
|> >    just people we are talking about - can consider alternatives."
|> >
|> >It's right there in the posting you are replying to.
|>
|> Yes it was, but I still don't understand your distinctions.  What
|> do you mean by "consider?"  Can a small child be moral?  How about
|> a gorilla?  A dolphin?  A platypus?  Where is the line drawn?  Does
|> the being need to be self aware?

Are you blind?   What do you think that this sentence means?

        "There must be the possibility that the organism - it's not
        just people we are talking about - can consider alternatives."

What would that imply?

|>
|> What \*do\* you call the mechanism which seems to prevent animals of
|> the same species from (arbitrarily) killing each other?  Don't
|> you find the fact that they don't at all significant?

I find the fact that they do to be significant.

jon.

Copy to clipboard

Such headers, signature footers (and quoted metadata from previous messages) can be considered side information that artificially reveals the newsgroup by identifying the registered members and one would rather want our text classifier to only learn from the “main content” of each text document instead of relying on the leaked identity of the writers.

### Model with metadata stripping[#](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html#model-with-metadata-stripping "Link to this heading")

The `remove` option of the 20 newsgroups dataset loader in scikit-learn allows to heuristically attempt to filter out some of this unwanted metadata that makes the classification problem artificially easier. Be aware that such filtering of the text contents is far from perfect.

Let us try to leverage this option to train a text classifier that does not rely too much on this kind of metadata to make its decisions:

(
    X\_train,
    X\_test,
    y\_train,
    y\_test,
    feature\_names,
    target\_names,
) \= load\_dataset(remove\=("headers", "footers", "quotes"))

clf \= [RidgeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")
(tol\=1e-2, solver\="sparse\_cg")
clf.fit(X\_train, y\_train)
pred \= clf.predict(X\_test)

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(10, 5))
[ConfusionMatrixDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_predictions "sklearn.metrics.ConfusionMatrixDisplay.from_predictions")
(y\_test, pred, ax\=ax)
ax.xaxis.set\_ticklabels(target\_names)
ax.yaxis.set\_ticklabels(target\_names)
\_ \= ax.set\_title(
    f"Confusion Matrix for {clf.\_\_class\_\_.\_\_name\_\_}\\non filtered documents"
)

Copy to clipboard

![Confusion Matrix for RidgeClassifier on filtered documents](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_classification_20newsgroups_003.png)

By looking at the confusion matrix, it is more evident that the scores of the model trained with metadata were over-optimistic. The classification problem without access to the metadata is less accurate but more representative of the intended text classification problem.

\_ \= plot\_feature\_effects().set\_title("Average feature effects on filtered documents")

Copy to clipboard

![Average feature effects on filtered documents](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_classification_20newsgroups_004.png)

top 5 keywords per class:
  alt.atheism comp.graphics sci.space talk.religion.misc
0         don      graphics     space                god
1      people          file      like          christian
2         say        thanks      nasa              jesus
3    religion         image     orbit         christians
4        post          does    launch              wrong

Copy to clipboard

In the next section we keep the dataset without metadata to compare several classifiers.

Benchmarking classifiers[#](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html#benchmarking-classifiers "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Scikit-learn provides many different kinds of classification algorithms. In this section we will train a selection of those classifiers on the same text classification problem and measure both their generalization performance (accuracy on the test set) and their computation performance (speed), both at training time and testing time. For such purpose we define the following benchmarking utilities:

from sklearn import metrics
from sklearn.utils.extmath import [density](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.density.html#sklearn.utils.extmath.density "sklearn.utils.extmath.density")

def benchmark(clf, custom\_name\=False):
    print("\_" \* 80)
    print("Training: ")
    print(clf)
    t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    clf.fit(X\_train, y\_train)
    train\_time \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0
    print(f"train time: {train\_time:.3}s")

    t0 \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    pred \= clf.predict(X\_test)
    test\_time \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- t0
    print(f"test time:  {test\_time:.3}s")

    score \= [metrics.accuracy\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
(y\_test, pred)
    print(f"accuracy:   {score:.3}")

    if hasattr(clf, "coef\_"):
        print(f"dimensionality: {clf.coef\_.shape\[1\]}")
        print(f"density: {[density](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.density.html#sklearn.utils.extmath.density "sklearn.utils.extmath.density")
(clf.coef\_)}")
        print()

    print()
    if custom\_name:
        clf\_descr \= str(custom\_name)
    else:
        clf\_descr \= clf.\_\_class\_\_.\_\_name\_\_
    return clf\_descr, score, train\_time, test\_time

Copy to clipboard

We now train and test the datasets with 8 different classification models and get performance results for each model. The goal of this study is to highlight the computation/accuracy tradeoffs of different types of classifiers for such a multi-class text classification problem.

Notice that the most important hyperparameters values were tuned using a grid search procedure not shown in this notebook for the sake of simplicity. See the example script [Sample pipeline for text feature extraction and evaluation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html#sphx-glr-auto-examples-model-selection-plot-grid-search-text-feature-extraction-py)
 for a demo on how such tuning can be done.

from sklearn.ensemble import [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
, [SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
from sklearn.naive\_bayes import [ComplementNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.ComplementNB.html#sklearn.naive_bayes.ComplementNB "sklearn.naive_bayes.ComplementNB")
from sklearn.neighbors import [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
, [NearestCentroid](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid "sklearn.neighbors.NearestCentroid")
from sklearn.svm import [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")

results \= \[\]
for clf, name in (
    ([LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(C\=5, max\_iter\=1000), "Logistic Regression"),
    ([RidgeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")
(alpha\=1.0, solver\="sparse\_cg"), "Ridge Classifier"),
    ([KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
(n\_neighbors\=100), "kNN"),
    ([RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
(), "Random Forest"),
    \# L2 penalty Linear SVC
    ([LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
(C\=0.1, dual\=False, max\_iter\=1000), "Linear SVC"),
    \# L2 penalty Linear SGD
    (
        [SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
(
            loss\="log\_loss", alpha\=1e-4, n\_iter\_no\_change\=3, early\_stopping\=True
        ),
        "log-loss SGD",
    ),
    \# NearestCentroid (aka Rocchio classifier)
    ([NearestCentroid](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid "sklearn.neighbors.NearestCentroid")
(), "NearestCentroid"),
    \# Sparse naive Bayes classifier
    ([ComplementNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.ComplementNB.html#sklearn.naive_bayes.ComplementNB "sklearn.naive_bayes.ComplementNB")
(alpha\=0.1), "Complement naive Bayes"),
):
    print("=" \* 80)
    print(name)
    results.append(benchmark(clf, name))

Copy to clipboard

\================================================================================
Logistic Regression
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Training:
LogisticRegression(C=5, max\_iter=1000)
train time: 0.174s
test time:  0.00075s
accuracy:   0.772
dimensionality: 5316
density: 1.0


================================================================================
Ridge Classifier
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Training:
RidgeClassifier(solver='sparse\_cg')
train time: 0.0326s
test time:  0.000774s
accuracy:   0.76
dimensionality: 5316
density: 1.0


================================================================================
kNN
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Training:
KNeighborsClassifier(n\_neighbors=100)
train time: 0.00114s
test time:  0.0377s
accuracy:   0.752

================================================================================
Random Forest
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Training:
RandomForestClassifier()
train time: 1.55s
test time:  0.0648s
accuracy:   0.7

================================================================================
Linear SVC
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Training:
LinearSVC(C=0.1, dual=False)
train time: 0.0298s
test time:  0.000752s
accuracy:   0.752
dimensionality: 5316
density: 1.0


================================================================================
log-loss SGD
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Training:
SGDClassifier(early\_stopping=True, loss='log\_loss', n\_iter\_no\_change=3)
train time: 0.0399s
test time:  0.000759s
accuracy:   0.764
dimensionality: 5316
density: 1.0


================================================================================
NearestCentroid
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Training:
NearestCentroid()
train time: 0.12s
test time:  0.00189s
accuracy:   0.748

================================================================================
Complement naive Bayes
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Training:
ComplementNB(alpha=0.1)
train time: 0.00245s
test time:  0.000597s
accuracy:   0.779

Copy to clipboard

Plot accuracy, training and test time of each classifier[#](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html#plot-accuracy-training-and-test-time-of-each-classifier "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The scatter plots show the trade-off between the test accuracy and the training and testing time of each classifier.

indices \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len(results))

results \= \[\[x\[i\] for x in results\] for i in range(4)\]

clf\_names, score, training\_time, test\_time \= results
training\_time \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(training\_time)
test\_time \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(test\_time)

fig, ax1 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(10, 8))
ax1.scatter(score, training\_time, s\=60)
ax1.set(
    title\="Score-training time trade-off",
    yscale\="log",
    xlabel\="test accuracy",
    ylabel\="training time (s)",
)
fig, ax2 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(10, 8))
ax2.scatter(score, test\_time, s\=60)
ax2.set(
    title\="Score-test time trade-off",
    yscale\="log",
    xlabel\="test accuracy",
    ylabel\="test time (s)",
)

for i, txt in enumerate(clf\_names):
    ax1.annotate(txt, (score\[i\], training\_time\[i\]))
    ax2.annotate(txt, (score\[i\], test\_time\[i\]))

Copy to clipboard

*   ![Score-training time trade-off](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_classification_20newsgroups_005.png)
*   ![Score-test time trade-off](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_classification_20newsgroups_006.png)

The naive Bayes model has the best trade-off between score and training/testing time, while Random Forest is both slow to train, expensive to predict and has a comparatively bad accuracy. This is expected: for high-dimensional prediction problems, linear models are often better suited as most problems become linearly separable when the feature space has 10,000 dimensions or more.

The difference in training speed and accuracy of the linear models can be explained by the choice of the loss function they optimize and the kind of regularization they use. Be aware that some linear models with the same loss but a different solver or regularization configuration may yield different fitting times and test accuracy. We can observe on the second plot that once trained, all linear models have approximately the same prediction speed which is expected because they all implement the same prediction function.

KNeighborsClassifier has a relatively low accuracy and has the highest testing time. The long prediction time is also expected: for each prediction the model has to compute the pairwise distances between the testing sample and each document in the training set, which is computationally expensive. Furthermore, the “curse of dimensionality” harms the ability of this model to yield competitive accuracy in the high dimensional feature space of text classification problems.

**Total running time of the script:** (0 minutes 6.605 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo32.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/text/plot_document_classification_20newsgroups.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo32.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/text/plot_document_classification_20newsgroups.ipynb)

[`Download Jupyter notebook: plot_document_classification_20newsgroups.ipynb`](https://scikit-learn.org/stable/_downloads/7ff1697c60d48929305821f39296dbb9/plot_document_classification_20newsgroups.ipynb)

[`Download Python source code: plot_document_classification_20newsgroups.py`](https://scikit-learn.org/stable/_downloads/b95d2be91f59162cfa269bdb32134d31/plot_document_classification_20newsgroups.py)

[`Download zipped: plot_document_classification_20newsgroups.zip`](https://scikit-learn.org/stable/_downloads/06e5cfec52777b1f220312b4ada9469d/plot_document_classification_20newsgroups.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_text_feature_extraction_thumb.png)

[Sample pipeline for text feature extraction and evaluation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html)

Sample pipeline for text feature extraction and evaluation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_bicluster_newsgroups_thumb.png)

[Biclustering documents with the Spectral Co-clustering algorithm](https://scikit-learn.org/stable/auto_examples/bicluster/plot_bicluster_newsgroups.html)

Biclustering documents with the Spectral Co-clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_clustering_thumb.png)

[Clustering text documents using k-means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html)

Clustering text documents using k-means

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hashing_vs_dict_vectorizer_thumb.png)

[FeatureHasher and DictVectorizer Comparison](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html)

FeatureHasher and DictVectorizer Comparison

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/b95d2be91f59162cfa269bdb32134d31/plot_document_classification_20newsgroups.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/7ff1697c60d48929305821f39296dbb9/plot_document_classification_20newsgroups.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/06e5cfec52777b1f220312b4ada9469d/plot_document_classification_20newsgroups.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo32.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/text/plot_document_classification_20newsgroups.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo32.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/text/plot_document_classification_20newsgroups.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)