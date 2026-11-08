[Skip to main content](https://numpy.org/doc/stable/reference/random/c-api.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/c-api.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/c-api.html)
[2.4](https://numpy.org/doc/2.4/reference/random/c-api.html)
[2.3](https://numpy.org/doc/2.3/reference/random/c-api.html)
[2.2](https://numpy.org/doc/2.2/reference/random/c-api.html)
[2.1](https://numpy.org/doc/2.1/reference/random/c-api.html)
[2.0](https://numpy.org/doc/2.0/reference/random/c-api.html)
[1.26](https://numpy.org/doc/1.26/reference/random/c-api.html)
[1.25](https://numpy.org/doc/1.25/reference/random/c-api.html)
[1.24](https://numpy.org/doc/1.24/reference/random/c-api.html)
[1.23](https://numpy.org/doc/1.23/reference/random/c-api.html)
[1.22](https://numpy.org/doc/1.22/reference/random/c-api.html)
[1.21](https://numpy.org/doc/1.21/reference/random/c-api.html)
[1.20](https://numpy.org/doc/1.20/reference/random/c-api.html)
[1.19](https://numpy.org/doc/1.19/reference/random/c-api.html)
[1.18](https://numpy.org/doc/1.18/reference/random/c-api.html)
[1.17](https://numpy.org/doc/1.17/reference/random/c-api.html)
[1.16](https://numpy.org/doc/1.16/reference/random/c-api.html)
[1.15](https://numpy.org/doc/1.15/reference/random/c-api.html)
[1.14](https://numpy.org/doc/1.14/reference/random/c-api.html)
[1.13](https://numpy.org/doc/1.13/reference/random/c-api.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

C API for random[#](https://numpy.org/doc/stable/reference/random/c-api.html#c-api-for-random "Link to this heading")

======================================================================================================================

Access to various distributions below is available via Cython or C-wrapper libraries like CFFI. All the functions accept a [`bitgen_t`](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 as their first argument. To access these from Cython or C, you must link with the `npyrandom` static library which is part of the NumPy distribution, located in `numpy/random/lib`. Note that you must _also_ link with `npymath`, see [Linking against the core math library in an extension](https://numpy.org/doc/stable/reference/c-api/coremath.html#linking-npymath)
.

type bitgen\_t[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "Link to this definition")
  

The [`bitgen_t`](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 holds the current state of the BitGenerator and pointers to functions that return standard C types while advancing the state.

struct bitgen:
    void \*state
    npy\_uint64 (\*next\_uint64)(void \*st) nogil
    uint32\_t (\*next\_uint32)(void \*st) nogil
    double (\*next\_double)(void \*st) nogil
    npy\_uint64 (\*next\_raw)(void \*st) nogil

ctypedef bitgen bitgen\_t

Copy to clipboard

See [Extending](https://numpy.org/doc/stable/reference/random/extending.html)
 for examples of using these functions.

The functions are named with the following conventions:

*   “standard” refers to the reference values for any parameters. For instance “standard\_uniform” means a uniform distribution on the interval `0.0` to `1.0`
    
*   “fill” functions will fill the provided `out` with `cnt` values.
    
*   The functions without “standard” in their name require additional parameters to describe the distributions.
    
*   Functions with `inv` in their name are based on the slower inverse method instead of a ziggurat lookup algorithm, which is significantly faster. The non-ziggurat variants are used in corner cases and for legacy compatibility.
    

double random\_standard\_uniform([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_standard_uniform "Link to this definition")
  

void random\_standard\_uniform\_fill([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 cnt, double \*out)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_standard_uniform_fill "Link to this definition")
  

double random\_standard\_exponential([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_standard_exponential "Link to this definition")
  

void random\_standard\_exponential\_fill([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 cnt, double \*out)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_standard_exponential_fill "Link to this definition")
  

void random\_standard\_exponential\_inv\_fill([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 cnt, double \*out)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_standard_exponential_inv_fill "Link to this definition")
  

double random\_standard\_normal([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_standard_normal "Link to this definition")
  

void random\_standard\_normal\_fill([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 count, double \*out)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_standard_normal_fill "Link to this definition")
  

void random\_standard\_normal\_fill\_f([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 count, float \*out)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_standard_normal_fill_f "Link to this definition")
  

double random\_standard\_gamma([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double shape)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_standard_gamma "Link to this definition")
  

float random\_standard\_uniform\_f([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_standard_uniform_f "Link to this definition")
  

void random\_standard\_uniform\_fill\_f([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 cnt, float \*out)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_standard_uniform_fill_f "Link to this definition")
  

float random\_standard\_exponential\_f([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_standard_exponential_f "Link to this definition")
  

void random\_standard\_exponential\_fill\_f([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 cnt, float \*out)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_standard_exponential_fill_f "Link to this definition")
  

void random\_standard\_exponential\_inv\_fill\_f([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 cnt, float \*out)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_standard_exponential_inv_fill_f "Link to this definition")
  

float random\_standard\_normal\_f([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_standard_normal_f "Link to this definition")
  

float random\_standard\_gamma\_f([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, float shape)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_standard_gamma_f "Link to this definition")
  

double random\_normal([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double loc, double scale)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_normal "Link to this definition")
  

double random\_gamma([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double shape, double scale)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_gamma "Link to this definition")
  

float random\_gamma\_f([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, float shape, float scale)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_gamma_f "Link to this definition")
  

double random\_exponential([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double scale)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_exponential "Link to this definition")
  

double random\_uniform([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double lower, double range)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_uniform "Link to this definition")
  

double random\_beta([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double a, double b)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_beta "Link to this definition")
  

double random\_chisquare([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double df)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_chisquare "Link to this definition")
  

double random\_f([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double dfnum, double dfden)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_f "Link to this definition")
  

double random\_standard\_cauchy([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_standard_cauchy "Link to this definition")
  

double random\_pareto([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double a)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_pareto "Link to this definition")
  

double random\_weibull([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double a)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_weibull "Link to this definition")
  

double random\_power([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double a)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_power "Link to this definition")
  

double random\_laplace([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double loc, double scale)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_laplace "Link to this definition")
  

double random\_gumbel([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double loc, double scale)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_gumbel "Link to this definition")
  

double random\_logistic([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double loc, double scale)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_logistic "Link to this definition")
  

double random\_lognormal([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double mean, double sigma)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_lognormal "Link to this definition")
  

double random\_rayleigh([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double mode)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_rayleigh "Link to this definition")
  

double random\_standard\_t([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double df)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_standard_t "Link to this definition")
  

double random\_noncentral\_chisquare([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double df, double nonc)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_noncentral_chisquare "Link to this definition")
  

double random\_noncentral\_f([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double dfnum, double dfden, double nonc)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_noncentral_f "Link to this definition")
  

double random\_wald([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double mean, double scale)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_wald "Link to this definition")
  

double random\_vonmises([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double mu, double kappa)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_vonmises "Link to this definition")
  

double random\_triangular([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double left, double mode, double right)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_triangular "Link to this definition")
  

[npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 random\_poisson([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double lam)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_poisson "Link to this definition")
  

[npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 random\_negative\_binomial([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double n, double p)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_negative_binomial "Link to this definition")
  

type binomial\_t[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.binomial_t "Link to this definition")
  

typedef struct s\_binomial\_t {
  int has\_binomial; /\* !=0: following parameters initialized for binomial \*/
  double psave;
  RAND\_INT\_TYPE nsave;
  double r;
  double q;
  double fm;
  RAND\_INT\_TYPE m;
  double p1;
  double xm;
  double xl;
  double xr;
  double c;
  double laml;
  double lamr;
  double p2;
  double p3;
  double p4;
} binomial\_t;

Copy to clipboard

[npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 random\_binomial([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double p, [npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 n, [binomial\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.binomial_t "binomial_t")
 \*binomial)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_binomial "Link to this definition")
  

[npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 random\_logseries([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double p)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_logseries "Link to this definition")
  

[npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 random\_geometric\_search([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double p)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_geometric_search "Link to this definition")
  

[npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 random\_geometric\_inversion([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double p)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_geometric_inversion "Link to this definition")
  

[npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 random\_geometric([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double p)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_geometric "Link to this definition")
  

[npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 random\_zipf([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, double a)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_zipf "Link to this definition")
  

[npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 random\_hypergeometric([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, [npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 good, [npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 bad, [npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 sample)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_hypergeometric "Link to this definition")
  

[npy\_uint64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint64 "npy_uint64")
 random\_interval([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, [npy\_uint64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint64 "npy_uint64")
 max)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_interval "Link to this definition")
  

void random\_multinomial([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, [npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 n, [npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 \*mnix, double \*pix, [npy\_intp](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_intp "npy_intp")
 d, [binomial\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.binomial_t "binomial_t")
 \*binomial)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_multinomial "Link to this definition")
  

int random\_multivariate\_hypergeometric\_count([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, [npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 total, size\_t num\_colors, [npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 \*colors, [npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 nsample, size\_t num\_variates, [npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 \*variates)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_multivariate_hypergeometric_count "Link to this definition")
  

void random\_multivariate\_hypergeometric\_marginals([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, [npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 total, size\_t num\_colors, [npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 \*colors, [npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 nsample, size\_t num\_variates, [npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 \*variates)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_multivariate_hypergeometric_marginals "Link to this definition")
  

Generate a single integer

[npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 random\_positive\_int64([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_positive_int64 "Link to this definition")
  

[npy\_int32](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int32 "npy_int32")
 random\_positive\_int32([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_positive_int32 "Link to this definition")
  

[npy\_int64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_int64 "npy_int64")
 random\_positive\_int([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_positive_int "Link to this definition")
  

[npy\_uint64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint64 "npy_uint64")
 random\_uint([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_uint "Link to this definition")
  

Generate random uint64 numbers in closed interval \[off, off + rng\].

[npy\_uint64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint64 "npy_uint64")
 random\_bounded\_uint64([bitgen\_t](https://numpy.org/doc/stable/reference/random/c-api.html#c.bitgen_t "bitgen_t")
 \*bitgen\_state, [npy\_uint64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint64 "npy_uint64")
 off, [npy\_uint64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint64 "npy_uint64")
 rng, [npy\_uint64](https://numpy.org/doc/stable/reference/c-api/dtype.html#c.npy_uint64 "npy_uint64")
 mask, bool use\_masked)[#](https://numpy.org/doc/stable/reference/random/c-api.html#c.random_bounded_uint64 "Link to this definition")