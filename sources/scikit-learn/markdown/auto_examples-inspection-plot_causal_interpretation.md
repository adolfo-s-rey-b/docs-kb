[Skip to main content](https://scikit-learn.org/stable/auto_examples/inspection/plot_causal_interpretation.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/inspection/plot_causal_interpretation.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/inspection/plot_causal_interpretation.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/inspection/plot_causal_interpretation.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/inspection/plot_causal_interpretation.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/inspection/plot_causal_interpretation.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/inspection/plot_causal_interpretation.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/inspection/plot_causal_interpretation.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/inspection/plot_causal_interpretation.html#sphx-glr-download-auto-examples-inspection-plot-causal-interpretation-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Failure of Machine Learning to infer causal effects[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_causal_interpretation.html#failure-of-machine-learning-to-infer-causal-effects "Link to this heading")

============================================================================================================================================================================================================================

Machine Learning models are great for measuring statistical associations. Unfortunately, unless we’re willing to make strong assumptions about the data, those models are unable to infer causal effects.

To illustrate this, we will simulate a situation in which we try to answer one of the most important questions in economics of education: **what is the causal effect of earning a college degree on hourly wages?** Although the answer to this question is crucial to policy makers, [Omitted-Variable Biases](https://en.wikipedia.org/wiki/Omitted-variable_bias)
 (OVB) prevent us from identifying that causal effect.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

The dataset: simulated hourly wages[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_causal_interpretation.html#the-dataset-simulated-hourly-wages "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The data generating process is laid out in the code below. Work experience in years and a measure of ability are drawn from Normal distributions; the hourly wage of one of the parents is drawn from Beta distribution. We then create an indicator of college degree which is positively impacted by ability and parental hourly wage. Finally, we model hourly wages as a linear function of all the previous variables and a random component. Note that all variables have a positive effect on hourly wages.

import numpy as np
import pandas as pd

n\_samples \= 10\_000
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(32)

experiences \= rng.normal(20, 10, size\=n\_samples).astype(int)
experiences\[experiences < 0\] \= 0
abilities \= rng.normal(0, 0.15, size\=n\_samples)
parent\_hourly\_wages \= 50 \* rng.beta(2, 8, size\=n\_samples)
parent\_hourly\_wages\[parent\_hourly\_wages < 0\] \= 0
college\_degrees \= (
    9 \* abilities + 0.02 \* parent\_hourly\_wages + rng.randn(n\_samples) \> 0.7
).astype(int)

true\_coef \= [pd.Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
(
    {
        "college degree": 2.0,
        "ability": 5.0,
        "experience": 0.2,
        "parent hourly wage": 1.0,
    }
)
hourly\_wages \= (
    true\_coef\["experience"\] \* experiences
    + true\_coef\["parent hourly wage"\] \* parent\_hourly\_wages
    + true\_coef\["college degree"\] \* college\_degrees
    + true\_coef\["ability"\] \* abilities
    + rng.normal(0, 1, size\=n\_samples)
)

hourly\_wages\[hourly\_wages < 0\] \= 0

Copy to clipboard

Description of the simulated data[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_causal_interpretation.html#description-of-the-simulated-data "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following plot shows the distribution of each variable, and pairwise scatter plots. Key to our OVB story is the positive relationship between ability and college degree.

import seaborn as sns

df \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(
    {
        "college degree": college\_degrees,
        "ability": abilities,
        "hourly wage": hourly\_wages,
        "experience": experiences,
        "parent hourly wage": parent\_hourly\_wages,
    }
)

grid \= [sns.pairplot](https://seaborn.pydata.org/generated/seaborn.pairplot.html#seaborn.pairplot "seaborn.pairplot")
(df, diag\_kind\="kde", corner\=True)

Copy to clipboard

![plot causal interpretation](https://scikit-learn.org/stable/_images/sphx_glr_plot_causal_interpretation_001.png)

In the next section, we train predictive models and we therefore split the target column from over features and we split the data into a training and a testing set.

from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

target\_name \= "hourly wage"
X, y \= df.drop(columns\=target\_name), df\[target\_name\]
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, test\_size\=0.2, random\_state\=0)

Copy to clipboard

Income prediction with fully observed variables[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_causal_interpretation.html#income-prediction-with-fully-observed-variables "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

First, we train a predictive model, a [`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
 model. In this experiment, we assume that all variables used by the true generative model are available.

from sklearn.linear\_model import [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
from sklearn.metrics import [r2\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")

features\_names \= \["experience", "parent hourly wage", "college degree", "ability"\]

regressor\_with\_ability \= [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
()
regressor\_with\_ability.fit(X\_train\[features\_names\], y\_train)
y\_pred\_with\_ability \= regressor\_with\_ability.predict(X\_test\[features\_names\])
R2\_with\_ability \= [r2\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
(y\_test, y\_pred\_with\_ability)

print(f"R2 score with ability: {R2\_with\_ability:.3f}")

Copy to clipboard

R2 score with ability: 0.975

Copy to clipboard

This model predicts well the hourly wages as shown by the high R2 score. We plot the model coefficients to show that we exactly recover the values of the true generative model.

import matplotlib.pyplot as plt

model\_coef \= [pd.Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
(regressor\_with\_ability.coef\_, index\=features\_names)
coef \= [pd.concat](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html#pandas.concat "pandas.concat")
(
    \[true\_coef\[features\_names\], model\_coef\],
    keys\=\["Coefficients of true generative model", "Model coefficients"\],
    axis\=1,
)
ax \= coef.plot.barh()
ax.set\_xlabel("Coefficient values")
ax.set\_title("Coefficients of the linear regression including the ability features")
\_ \= [plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()

Copy to clipboard

![Coefficients of the linear regression including the ability features](https://scikit-learn.org/stable/_images/sphx_glr_plot_causal_interpretation_002.png)

Income prediction with partial observations[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_causal_interpretation.html#income-prediction-with-partial-observations "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In practice, intellectual abilities are not observed or are only estimated from proxies that inadvertently measure education as well (e.g. by IQ tests). But omitting the “ability” feature from a linear model inflates the estimate via a positive OVB.

features\_names \= \["experience", "parent hourly wage", "college degree"\]

regressor\_without\_ability \= [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
()
regressor\_without\_ability.fit(X\_train\[features\_names\], y\_train)
y\_pred\_without\_ability \= regressor\_without\_ability.predict(X\_test\[features\_names\])
R2\_without\_ability \= [r2\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")
(y\_test, y\_pred\_without\_ability)

print(f"R2 score without ability: {R2\_without\_ability:.3f}")

Copy to clipboard

R2 score without ability: 0.968

Copy to clipboard

The predictive power of our model is similar when we omit the ability feature in terms of R2 score. We now check if the coefficient of the model are different from the true generative model.

model\_coef \= [pd.Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
(regressor\_without\_ability.coef\_, index\=features\_names)
coef \= [pd.concat](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html#pandas.concat "pandas.concat")
(
    \[true\_coef\[features\_names\], model\_coef\],
    keys\=\["Coefficients of true generative model", "Model coefficients"\],
    axis\=1,
)
ax \= coef.plot.barh()
ax.set\_xlabel("Coefficient values")
\_ \= ax.set\_title("Coefficients of the linear regression excluding the ability feature")
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Coefficients of the linear regression excluding the ability feature](https://scikit-learn.org/stable/_images/sphx_glr_plot_causal_interpretation_003.png)

To compensate for the omitted variable, the model inflates the coefficient of the college degree feature. Therefore, interpreting this coefficient value as a causal effect of the true generative model is incorrect.

Lessons learned[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_causal_interpretation.html#lessons-learned "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

Machine learning models are not designed for the estimation of causal effects. While we showed this with a linear model, OVB can affect any type of model.

Whenever interpreting a coefficient or a change in predictions brought about by a change in one of the features, it is important to keep in mind potentially unobserved variables that could be correlated with both the feature in question and the target variable. Such variables are called [Confounding Variables](https://en.wikipedia.org/wiki/Confounding)
. In order to still estimate causal effect in the presence of confounding, researchers usually conduct experiments in which the treatment variable (e.g. college degree) is randomized. When an experiment is prohibitively expensive or unethical, researchers can sometimes use other causal inference techniques such as [Instrumental Variables](https://en.wikipedia.org/wiki/Instrumental_variables_estimation)
 (IV) estimations.

**Total running time of the script:** (0 minutes 1.629 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo17.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/inspection/plot_causal_interpretation.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo17.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/inspection/plot_causal_interpretation.ipynb)

[`Download Jupyter notebook: plot_causal_interpretation.ipynb`](https://scikit-learn.org/stable/_downloads/ff3bc184e1a2d8d99b77058ba52b764f/plot_causal_interpretation.ipynb)

[`Download Python source code: plot_causal_interpretation.py`](https://scikit-learn.org/stable/_downloads/34b53ad148e36f98b6de8ddc15e3dfd3/plot_causal_interpretation.py)

[`Download zipped: plot_causal_interpretation.zip`](https://scikit-learn.org/stable/_downloads/3ad3d8de76dc79e282240ff9d4aec996/plot_causal_interpretation.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_thumb.png)

[Common pitfalls in the interpretation of coefficients of linear models](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html)

Common pitfalls in the interpretation of coefficients of linear models

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_nnls_thumb.png)

[Non-negative least squares](https://scikit-learn.org/stable/auto_examples/linear_model/plot_nnls.html)

Non-negative least squares

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ridge_coeffs_thumb.png)

[Ridge coefficients as a function of the L2 Regularization](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_coeffs.html)

Ridge coefficients as a function of the L2 Regularization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_train_error_vs_test_error_thumb.png)

[Effect of model regularization on training and test error](https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html)

Effect of model regularization on training and test error

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/34b53ad148e36f98b6de8ddc15e3dfd3/plot_causal_interpretation.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/ff3bc184e1a2d8d99b77058ba52b764f/plot_causal_interpretation.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/3ad3d8de76dc79e282240ff9d4aec996/plot_causal_interpretation.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo17.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/inspection/plot_causal_interpretation.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo17.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/inspection/plot_causal_interpretation.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)