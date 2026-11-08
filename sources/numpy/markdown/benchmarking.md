[Skip to main content](https://numpy.org/doc/stable/benchmarking.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

NumPy benchmarks[#](https://numpy.org/doc/stable/benchmarking.html#numpy-benchmarks "Link to this heading")

============================================================================================================

Benchmarking NumPy with Airspeed Velocity.

Usage[#](https://numpy.org/doc/stable/benchmarking.html#usage "Link to this heading")

--------------------------------------------------------------------------------------

Airspeed Velocity manages building and Python virtualenvs by itself, unless told otherwise. To run the benchmarks, you do not need to install a development version of NumPy to your current Python environment.

Before beginning, ensure that _airspeed velocity_ is installed. By default, _asv_ ships with support for anaconda and virtualenv:

pip install asv
pip install virtualenv

Copy to clipboard

After contributing new benchmarks, you should test them locally before submitting a pull request.

To run all benchmarks, navigate to the root NumPy directory at the command line and execute:

spin bench

Copy to clipboard

This builds NumPy and runs all available benchmarks defined in `benchmarks/`. (Note: this could take a while. Each benchmark is run multiple times to measure the distribution in execution times.)

For **testing** benchmarks locally, it may be better to run these without replications:

cd benchmarks/
export REGEXP="bench.\*Ufunc"
asv run --dry-run --show-stderr --python=same --quick -b $REGEXP

Copy to clipboard

Where the regular expression used to match benchmarks is stored in `$REGEXP`, and _–quick_ is used to avoid repetitions.

To run benchmarks from a particular benchmark module, such as `bench_core.py`, simply append the filename without the extension:

spin bench \-t bench\_core

Copy to clipboard

To run a benchmark defined in a class, such as `MeshGrid` from `bench_creation.py`:

spin bench \-t bench\_creation.MeshGrid

Copy to clipboard

Compare changes in benchmark results to another version/commit/branch, use the `--compare` option (or the equivalent `-c`):

spin bench \--compare v1.6.2 \-t bench\_core
spin bench \--compare 20d03bcfd \-t bench\_core
spin bench \-c main \-t bench\_core

Copy to clipboard

All of the commands above display the results in plain text in the console, and the results are not saved for comparison with future commits. For greater control, a graphical view, and to have results saved for future comparison you can run ASV commands (record results and generate HTML):

cd benchmarks
asv run \-n \-e \--python\=same
asv publish
asv preview

Copy to clipboard

More on how to use `asv` can be found in [ASV documentation](https://asv.readthedocs.io/)
 Command-line help is available as usual via `asv --help` and `asv run --help`.

Benchmarking versions[#](https://numpy.org/doc/stable/benchmarking.html#benchmarking-versions "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

To benchmark or visualize only releases on different machines locally, the tags with their commits can be generated, before being run with `asv`, that is:

cd benchmarks
# Get commits for tags
# delete tag\_commits.txt before re-runs
for gtag in $(git tag --list --sort taggerdate | grep "^v"); do
git log $gtag --oneline -n1 --decorate=no | awk '{print $1;}' >> tag\_commits.txt
done
# Use the last 20
tail --lines=20 tag\_commits.txt > 20\_vers.txt
asv run HASHFILE:20\_vers.txt
# Publish and view
asv publish
asv preview

Copy to clipboard

For details on contributing these, see the [benchmark results repository](https://github.com/HaoZeke/asv-numpy)
.

Writing benchmarks[#](https://numpy.org/doc/stable/benchmarking.html#writing-benchmarks "Link to this heading")

----------------------------------------------------------------------------------------------------------------

See [ASV documentation](https://asv.readthedocs.io/)
 for basics on how to write benchmarks.

Some things to consider:

*   The benchmark suite should be importable with any NumPy version.
    
*   The benchmark parameters etc. should not depend on which NumPy version is installed.
    
*   Try to keep the runtime of the benchmark reasonable.
    
*   Prefer ASV’s `time_` methods for benchmarking times rather than cooking up time measurements via `time.clock`, even if it requires some juggling when writing the benchmark.
    
*   Preparing arrays etc. should generally be put in the `setup` method rather than the `time_` methods, to avoid counting preparation time together with the time of the benchmarked operation.
    
*   Be mindful that large arrays created with `np.empty` or `np.zeros` might not be allocated in physical memory until the memory is accessed. If this is desired behaviour, make sure to comment it in your setup function. If you are benchmarking an algorithm, it is unlikely that a user will be executing said algorithm on a newly created empty/zero array. One can force pagefaults to occur in the setup phase either by calling `np.ones` or `arr.fill(value)` after creating the array.
    

On this page