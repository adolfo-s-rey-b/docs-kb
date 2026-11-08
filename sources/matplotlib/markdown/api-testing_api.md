[Skip to main content](https://matplotlib.org/stable/api/testing_api.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

`matplotlib.testing`[#](https://matplotlib.org/stable/api/testing_api.html#matplotlib-testing "Link to this heading")

======================================================================================================================

[`matplotlib.testing`](https://matplotlib.org/stable/api/testing_api.html#module-matplotlib.testing "matplotlib.testing")
[#](https://matplotlib.org/stable/api/testing_api.html#id1 "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Helper functions for testing.

matplotlib.testing.ipython\_in\_subprocess(_requested\_backend\_or\_gui\_framework_, _all\_expected\_backends_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/testing/__init__.py#L221-L252)
[#](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.ipython_in_subprocess "Link to this definition")

matplotlib.testing.is\_ci\_environment()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/testing/__init__.py#L255-L274)
[#](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.is_ci_environment "Link to this definition")

matplotlib.testing.set\_font\_settings\_for\_testing()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/testing/__init__.py#L20-L22)
[#](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.set_font_settings_for_testing "Link to this definition")

matplotlib.testing.set\_reproducibility\_for\_testing()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/testing/__init__.py#L25-L26)
[#](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.set_reproducibility_for_testing "Link to this definition")

matplotlib.testing.setup()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/testing/__init__.py#L29-L51)
[#](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.setup "Link to this definition")

matplotlib.testing.subprocess\_run\_for\_testing(_command_, _env\=None_, _timeout\=60_, _stdout\=None_, _stderr\=None_, _check\=False_, _text\=True_, _capture\_output\=False_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/testing/__init__.py#L54-L129)
[#](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.subprocess_run_for_testing "Link to this definition")

Create and run a subprocess.

Thin wrapper around [`subprocess.run`](https://docs.python.org/3/library/subprocess.html#subprocess.run "(in Python v3.14)")
, intended for testing. Will mark fork() failures on Cygwin as expected failures: not a success, but not indicating a problem with the code either.

Parameters:

**args**list of str

**env**dict\[str, str\]

**timeout**float

**stdout, stderr**

**check**bool

**text**bool

Also called `universal_newlines` in subprocess. I chose this name since the main effect is returning bytes ([`False`](https://docs.python.org/3/library/constants.html#False "(in Python v3.14)")
) vs. str ([`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
), though it also tries to normalize newlines across platforms.

**capture\_output**bool

Set stdout and stderr to subprocess.PIPE

Returns:

**proc**subprocess.Popen

Raises:

pytest.skip

If running on emscripten, which does not support subprocesses.

pytest.xfail

If platform is Cygwin and subprocess reports a fork() failure.

See also

[`subprocess.run`](https://docs.python.org/3/library/subprocess.html#subprocess.run "(in Python v3.14)")

matplotlib.testing.subprocess\_run\_helper(_func_, _\*args_, _timeout_, _extra\_env\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/testing/__init__.py#L132-L181)
[#](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.subprocess_run_helper "Link to this definition")

Run a function in a sub-process.

Parameters:

**func**function

The function to be run. It must be in a module that is importable.

**\*args**str

Any additional command line arguments to be passed in the first argument to `subprocess.run`.

**extra\_env**dict\[str, str\]

Any additional environment variables to be set for the subprocess.

matplotlib.testing.conftest.text\_placeholders(_monkeypatch_)[#](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.conftest.text_placeholders "Link to this definition")

Replace texts with placeholder rectangles.

The rectangle size only depends on the font size and the number of characters. It is thus insensitive to font properties and rendering details. This should be used for tests that depend on text geometries but not the actual text rendering, e.g. layout tests.

[`matplotlib.testing.compare`](https://matplotlib.org/stable/api/testing_api.html#module-matplotlib.testing.compare "matplotlib.testing.compare")
[#](https://matplotlib.org/stable/api/testing_api.html#module-matplotlib.testing.compare "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Utilities for comparing image results.

matplotlib.testing.compare.calculate\_rms(_expected\_image_, _actual\_image_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/testing/compare.py#L386-L395)
[#](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.compare.calculate_rms "Link to this definition")

Calculate the per-pixel errors, then compute the root mean square error.

matplotlib.testing.compare.comparable\_formats()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/testing/compare.py#L271-L282)
[#](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.compare.comparable_formats "Link to this definition")

Return the list of file formats that [`compare_images`](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.compare.compare_images "matplotlib.testing.compare.compare_images")
 can compare on this system.

Returns:

list of str

E.g. `['png', 'pdf', 'svg', 'eps']`.

matplotlib.testing.compare.compare\_images(_expected_, _actual_, _tol_, _in\_decorator\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/testing/compare.py#L417-L513)
[#](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.compare.compare_images "Link to this definition")

Compare two "image" files checking differences within a tolerance.

The two given filenames may point to files which are convertible to PNG via the `converter` dictionary. The underlying RMS is calculated in a similar way to the [`calculate_rms`](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.compare.calculate_rms "matplotlib.testing.compare.calculate_rms")
 function.

Parameters:

**expected**str

The filename of the expected image.

**actual**str

The filename of the actual image.

**tol**float

The tolerance (a color value difference, where 255 is the maximal difference). The test fails if the average pixel difference is greater than this value.

**in\_decorator**bool

Determines the output format. If called from image\_comparison decorator, this should be True. (default=False)

Returns:

None or dict or str

Return _None_ if the images are equal within the given tolerance.

If the images differ, the return value depends on _in\_decorator_. If _in\_decorator_ is true, a dict with the following entries is returned:

*   _rms_: The RMS of the image difference.
    
*   _expected_: The filename of the expected image.
    
*   _actual_: The filename of the actual image.
    
*   _diff\_image_: The filename of the difference image.
    
*   _tol_: The comparison tolerance.
    

Otherwise, a human-readable multi-line string representation of this information is returned.

Examples

img1 \= "./baseline/plot.png"
img2 \= "./output/plot.png"
compare\_images(img1, img2, 0.001)

[`matplotlib.testing.decorators`](https://matplotlib.org/stable/api/testing_api.html#module-matplotlib.testing.decorators "matplotlib.testing.decorators")
[#](https://matplotlib.org/stable/api/testing_api.html#module-matplotlib.testing.decorators "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

matplotlib.testing.decorators.check\_figures\_equal(_\*_, _extensions\=('png',)_, _tol\=0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/testing/decorators.py#L362-L460)
[#](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.decorators.check_figures_equal "Link to this definition")

Decorator for test cases that generate and compare two figures.

The decorated function must take two keyword arguments, _fig\_test_ and _fig\_ref_, and draw the test and reference images on them. After the function returns, the figures are saved and compared.

This decorator should be preferred over [`image_comparison`](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.decorators.image_comparison "matplotlib.testing.decorators.image_comparison")
 when possible in order to keep the size of the test suite from ballooning.

Parameters:

**extensions**list, default: \["png"\]

The extensions to test. Supported extensions are "png", "pdf", "svg".

Testing with the one default extension is sufficient if the output is not format dependent, e.g. if you test that a `bar()` plot yields the same result as some manually placed Rectangles. You should use all extensions if a renderer property is involved, e.g. correct alpha blending.

**tol**float

The RMS threshold above which the test is considered failed.

Raises:

RuntimeError

If any new figures are created (and not subsequently closed) inside the test function.

Examples

Check that calling [`Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
 with a single argument plots it against `[0, 1, 2, ...]`:

@check\_figures\_equal()
def test\_plot(fig\_test, fig\_ref):
    fig\_test.subplots().plot(\[1, 3, 5\])
    fig\_ref.subplots().plot(\[0, 1, 2\], \[1, 3, 5\])

matplotlib.testing.decorators.image\_comparison(_baseline\_images_, _extensions\=None_, _tol\=0_, _freetype\_version\=None_, _remove\_text\=False_, _savefig\_kwarg\=None_, _style\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/testing/decorators.py#L263-L359)
[#](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.decorators.image_comparison "Link to this definition")

Compare images generated by the test with those specified in _baseline\_images_, which must correspond, else an [`ImageComparisonFailure`](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.exceptions.ImageComparisonFailure "matplotlib.testing.exceptions.ImageComparisonFailure")
 exception will be raised.

Parameters:

**baseline\_images**list or None

A list of strings specifying the names of the images generated by calls to [`Figure.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
.

If _None_, the test function must use the `baseline_images` fixture, either as a parameter or with [`pytest.mark.usefixtures`](https://pytest.org/en/stable/reference/reference.html#pytest.mark.usefixtures "(in pytest v9.1.1)")
. This value is only allowed when using pytest.

**extensions**None or list of str

The list of extensions to test, e.g. `['png', 'pdf']`.

If _None_, defaults to: png, pdf, and svg.

When testing a single extension, it can be directly included in the names passed to _baseline\_images_. In that case, _extensions_ must not be set.

In order to keep the size of the test suite from ballooning, we only include the `svg` or `pdf` outputs if the test is explicitly exercising a feature dependent on that backend (see also the [`check_figures_equal`](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.decorators.check_figures_equal "matplotlib.testing.decorators.check_figures_equal")
 decorator for that purpose).

**tol**float, default: 0

The RMS threshold above which the test is considered failed.

Due to expected small differences in floating-point calculations, on 32-bit systems an additional 0.06 is added to this threshold.

**freetype\_version**str or tuple

The expected freetype version or range of versions for this test to pass.

**remove\_text**bool

Remove the title and tick text from the figure before comparison. This is useful to make the baseline images independent of variations in text rendering between different versions of FreeType.

This does not remove other, more deliberate, text, such as legends and annotations.

**savefig\_kwarg**dict

Optional arguments that are passed to the savefig method.

**style**str, dict, or list

The style(s) to apply to the image test. The test itself can also apply additional styles if desired.

Changed in version 3.11: This defaults to `['classic', '_classic_test_patch']`, but will be changing to `'mpl20'` as of Matplotlib 3.13. A warning is raised if not explicitly passed.

matplotlib.testing.decorators.remove\_ticks\_and\_titles(_figure_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/testing/decorators.py#L57-L75)
[#](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.decorators.remove_ticks_and_titles "Link to this definition")

[`matplotlib.testing.exceptions`](https://matplotlib.org/stable/api/testing_api.html#module-matplotlib.testing.exceptions "matplotlib.testing.exceptions")
[#](https://matplotlib.org/stable/api/testing_api.html#module-matplotlib.testing.exceptions "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

exception matplotlib.testing.exceptions.ImageComparisonFailure[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/testing/exceptions.py#L1-L4)
[#](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.exceptions.ImageComparisonFailure "Link to this definition")

Bases: [`AssertionError`](https://docs.python.org/3/library/exceptions.html#AssertionError "(in Python v3.14)")

Raise this exception to mark a test as a comparison between two images.

Testing with optional dependencies[#](https://matplotlib.org/stable/api/testing_api.html#testing-with-optional-dependencies "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

For more information on fixtures, see [pytest fixtures](https://pytest.org/en/stable/explanation/fixtures.html#about-fixtures "(in pytest v9.1.1)")
.

matplotlib.testing.conftest.pd()[#](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.conftest.pd "Link to this definition")

Fixture to import and configure pandas. Using this fixture, the test is skipped when pandas is not installed. Use this fixture instead of importing pandas in test files.

Examples

Request the pandas fixture by passing in `pd` as an argument to the test

def test\_matshow\_pandas(pd):

    df \= pd.DataFrame({'x':\[1,2,3\], 'y':\[4,5,6\]})
    im \= plt.figure().subplots().matshow(df)
    np.testing.assert\_array\_equal(im.get\_array(), df)

matplotlib.testing.conftest.xr()[#](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.conftest.xr "Link to this definition")

Fixture to import xarray so that the test is skipped when xarray is not installed. Use this fixture instead of importing xrray in test files.

Examples

Request the xarray fixture by passing in `xr` as an argument to the test

def test\_imshow\_xarray(xr):

    ds \= xr.DataArray(np.random.randn(2, 3))
    im \= plt.figure().subplots().imshow(ds)
    np.testing.assert\_array\_equal(im.get\_array(), ds)

On this page