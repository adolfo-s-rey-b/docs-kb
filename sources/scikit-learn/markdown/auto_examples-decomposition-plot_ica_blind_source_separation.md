[Skip to main content](https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_blind_source_separation.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/decomposition/plot_ica_blind_source_separation.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_blind_source_separation.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/decomposition/plot_ica_blind_source_separation.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/decomposition/plot_ica_blind_source_separation.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/decomposition/plot_ica_blind_source_separation.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/decomposition/plot_ica_blind_source_separation.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/decomposition/plot_ica_blind_source_separation.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_blind_source_separation.html#sphx-glr-download-auto-examples-decomposition-plot-ica-blind-source-separation-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Blind source separation using FastICA[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_blind_source_separation.html#blind-source-separation-using-fastica "Link to this heading")

=========================================================================================================================================================================================================

An example of estimating sources from noisy data.

[Independent component analysis (ICA)](https://scikit-learn.org/stable/modules/decomposition.html#ica)
 is used to estimate sources given noisy measurements. Imagine 3 instruments playing simultaneously and 3 microphones recording the mixed signals. ICA is used to recover the sources ie. what is played by each instrument. Importantly, PCA fails at recovering our `instruments` since the related signals reflect non-Gaussian processes.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Generate sample data[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_blind_source_separation.html#generate-sample-data "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np
from scipy import signal

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)
n\_samples \= 2000
time \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 8, n\_samples)

s1 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(2 \* time)  \# Signal 1 : sinusoidal signal
s2 \= [np.sign](https://numpy.org/doc/stable/reference/generated/numpy.sign.html#numpy.sign "numpy.sign")
([np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(3 \* time))  \# Signal 2 : square signal
s3 \= [signal.sawtooth](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.sawtooth.html#scipy.signal.sawtooth "scipy.signal.sawtooth")
(2 \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 \* time)  \# Signal 3: saw tooth signal

S \= [np.c\_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")
\[s1, s2, s3\]
S += 0.2 \* [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(size\=S.shape)  \# Add noise

S /= S.std(axis\=0)  \# Standardize data
\# Mix data
A \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[1, 1, 1\], \[0.5, 2, 1.0\], \[1.5, 1.0, 2.0\]\])  \# Mixing matrix
X \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(S, A.T)  \# Generate observations

Copy to clipboard

Fit ICA and PCA models[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_blind_source_separation.html#fit-ica-and-pca-models "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
, [FastICA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA "sklearn.decomposition.FastICA")

\# Compute ICA
ica \= [FastICA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA "sklearn.decomposition.FastICA")
(n\_components\=3, whiten\="arbitrary-variance")
S\_ \= ica.fit\_transform(X)  \# Reconstruct signals
A\_ \= ica.mixing\_  \# Get estimated mixing matrix

\# We can \`prove\` that the ICA model applies by reverting the unmixing.
assert [np.allclose](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html#numpy.allclose "numpy.allclose")
(X, [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(S\_, A\_.T) + ica.mean\_)

\# For comparison, compute PCA
pca \= [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(n\_components\=3)
H \= pca.fit\_transform(X)  \# Reconstruct signals based on orthogonal components

Copy to clipboard

Plot results[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_blind_source_separation.html#plot-results "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()

models \= \[X, S, S\_, H\]
names \= \[\
    "Observations (mixed signal)",\
    "True Sources",\
    "ICA recovered signals",\
    "PCA recovered signals",\
\]
colors \= \["red", "steelblue", "orange"\]

for ii, (model, name) in enumerate(zip(models, names), 1):
    [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(4, 1, ii)
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(name)
    for sig, color in zip(model.T, colors):
        [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(sig, color\=color)

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Observations (mixed signal), True Sources, ICA recovered signals, PCA recovered signals](https://scikit-learn.org/stable/_images/sphx_glr_plot_ica_blind_source_separation_001.png)

**Total running time of the script:** (0 minutes 0.391 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo10.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/decomposition/plot_ica_blind_source_separation.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo10.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_ica_blind_source_separation.ipynb)

[`Download Jupyter notebook: plot_ica_blind_source_separation.ipynb`](https://scikit-learn.org/stable/_downloads/3018e0d07b27e25beba9764116709763/plot_ica_blind_source_separation.ipynb)

[`Download Python source code: plot_ica_blind_source_separation.py`](https://scikit-learn.org/stable/_downloads/b122040dba159b8887080828461a517e/plot_ica_blind_source_separation.py)

[`Download zipped: plot_ica_blind_source_separation.zip`](https://scikit-learn.org/stable/_downloads/2cb37d76ae6c02821275d6ef8b96620f/plot_ica_blind_source_separation.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ica_vs_pca_thumb.png)

[FastICA on 2D point clouds](https://scikit-learn.org/stable/auto_examples/decomposition/plot_ica_vs_pca.html)

FastICA on 2D point clouds

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_omp_thumb.png)

[Orthogonal Matching Pursuit](https://scikit-learn.org/stable/auto_examples/linear_model/plot_omp.html)

Orthogonal Matching Pursuit

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_gpr_krr_thumb.png)

[Comparison of kernel ridge and Gaussian process regression](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_compare_gpr_krr.html)

Comparison of kernel ridge and Gaussian process regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_noisy_thumb.png)

[Ability of Gaussian process regression (GPR) to estimate data noise-level](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy.html)

Ability of Gaussian process regression (GPR) to estimate data noise-level

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/b122040dba159b8887080828461a517e/plot_ica_blind_source_separation.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/3018e0d07b27e25beba9764116709763/plot_ica_blind_source_separation.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/2cb37d76ae6c02821275d6ef8b96620f/plot_ica_blind_source_separation.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo10.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_ica_blind_source_separation.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo10.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/decomposition/plot_ica_blind_source_separation.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)