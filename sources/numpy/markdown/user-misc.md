[Skip to main content](https://numpy.org/doc/stable/user/misc.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Miscellaneous[#](https://numpy.org/doc/stable/user/misc.html#miscellaneous "Link to this heading")

===================================================================================================

IEEE 754 floating point special values[#](https://numpy.org/doc/stable/user/misc.html#ieee-754-floating-point-special-values "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

Special values defined in numpy: [`nan`](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "numpy.nan")
, [`inf`](https://numpy.org/doc/stable/reference/constants.html#numpy.inf "numpy.inf")

NaNs can be used as a poor-man’s mask (if you don’t care what the original value was)

Note: cannot use equality to test NaNs. E.g.:

\>>> myarr \= np.array(\[1., 0., np.nan, 3.\])
\>>> np.nonzero(myarr \== np.nan)
(array(\[\], dtype=int64),)

Copy to clipboard

\>>> np.nan \== np.nan  \# is always False! Use special numpy functions instead.
False

Copy to clipboard

\>>> myarr\[myarr \== np.nan\] \= 0. \# doesn't work
\>>> myarr
array(\[  1.,   0.,  nan,   3.\])

Copy to clipboard

\>>> myarr\[np.isnan(myarr)\] \= 0. \# use this instead find
\>>> myarr
array(\[1.,  0.,  0.,  3.\])

Copy to clipboard

Other related special value functions:

*   [`isnan`](https://numpy.org/doc/stable/reference/generated/numpy.isnan.html#numpy.isnan "numpy.isnan")
     - True if value is nan
    
*   [`isinf`](https://numpy.org/doc/stable/reference/generated/numpy.isinf.html#numpy.isinf "numpy.isinf")
     - True if value is inf
    
*   [`isfinite`](https://numpy.org/doc/stable/reference/generated/numpy.isfinite.html#numpy.isfinite "numpy.isfinite")
     - True if not nan or inf
    
*   [`nan_to_num`](https://numpy.org/doc/stable/reference/generated/numpy.nan_to_num.html#numpy.nan_to_num "numpy.nan_to_num")
     - Map nan to 0, inf to max float, -inf to min float
    

The following corresponds to the usual functions except that nans are excluded from the results:

*   [`nansum`](https://numpy.org/doc/stable/reference/generated/numpy.nansum.html#numpy.nansum "numpy.nansum")
    
*   [`nanmax`](https://numpy.org/doc/stable/reference/generated/numpy.nanmax.html#numpy.nanmax "numpy.nanmax")
    
*   [`nanmin`](https://numpy.org/doc/stable/reference/generated/numpy.nanmin.html#numpy.nanmin "numpy.nanmin")
    
*   [`nanargmax`](https://numpy.org/doc/stable/reference/generated/numpy.nanargmax.html#numpy.nanargmax "numpy.nanargmax")
    
*   [`nanargmin`](https://numpy.org/doc/stable/reference/generated/numpy.nanargmin.html#numpy.nanargmin "numpy.nanargmin")
    

\>>> x \= np.arange(10.)
\>>> x\[3\] \= np.nan
\>>> x.sum()
nan
\>>> np.nansum(x)
42.0

Copy to clipboard

On this page