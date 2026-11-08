[Skip to main content](https://numpy.org/doc/stable/reference/simd/build-options.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/simd/build-options.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/simd/build-options.html)
[2.4](https://numpy.org/doc/2.4/reference/simd/build-options.html)
[2.3](https://numpy.org/doc/2.3/reference/simd/build-options.html)
[2.2](https://numpy.org/doc/2.2/reference/simd/build-options.html)
[2.1](https://numpy.org/doc/2.1/reference/simd/build-options.html)
[2.0](https://numpy.org/doc/2.0/reference/simd/build-options.html)
[1.26](https://numpy.org/doc/1.26/reference/simd/build-options.html)
[1.25](https://numpy.org/doc/1.25/reference/simd/build-options.html)
[1.24](https://numpy.org/doc/1.24/reference/simd/build-options.html)
[1.23](https://numpy.org/doc/1.23/reference/simd/build-options.html)
[1.22](https://numpy.org/doc/1.22/reference/simd/build-options.html)
[1.21](https://numpy.org/doc/1.21/reference/simd/build-options.html)
[1.20](https://numpy.org/doc/1.20/reference/simd/build-options.html)
[1.19](https://numpy.org/doc/1.19/reference/simd/build-options.html)
[1.18](https://numpy.org/doc/1.18/reference/simd/build-options.html)
[1.17](https://numpy.org/doc/1.17/reference/simd/build-options.html)
[1.16](https://numpy.org/doc/1.16/reference/simd/build-options.html)
[1.15](https://numpy.org/doc/1.15/reference/simd/build-options.html)
[1.14](https://numpy.org/doc/1.14/reference/simd/build-options.html)
[1.13](https://numpy.org/doc/1.13/reference/simd/build-options.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

CPU Build Options[#](https://numpy.org/doc/stable/reference/simd/build-options.html#cpu-build-options "Link to this heading")

==============================================================================================================================

Overview[#](https://numpy.org/doc/stable/reference/simd/build-options.html#overview "Link to this heading")

------------------------------------------------------------------------------------------------------------

NumPy provides configuration options to optimize performance based on CPU capabilities. These options allow you to specify which CPU features to support, balancing performance, compatibility, and binary size. This document explains how to use these options effectively across various CPU architectures.

Key Configuration Options[#](https://numpy.org/doc/stable/reference/simd/build-options.html#key-configuration-options "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

NumPy uses several build options to control CPU optimizations:

*   `cpu-baseline`: The minimum set of CPU features required to run the compiled NumPy.
    
    *   Default: `min` (provides compatibility across a wide range of platforms)
        
    *   If your target CPU doesn’t support all specified baseline features, NumPy will fail to load with a Python runtime error
        
*   `cpu-baseline-detect`: controls detection of CPU baseline based on compiler flags. Default value is `auto` that enables detection if `-march=` or a similar compiler flag is used. The other possible values are `enabled` and `disabled` to respective enable or disable it unconditionally.
    
*   `cpu-dispatch`: Additional CPU features for which optimized code paths will be generated.
    
    *   Default: `max` (enables all available optimizations)
        
    *   At runtime, NumPy will automatically select the fastest available code path based on your CPU’s capabilities
        
*   `disable-optimization`: Completely disables all CPU optimizations.
    
    *   Default: `false` (optimizations are enabled)
        
    *   When set to `true`, disables all CPU optimized code including dispatch, SIMD, and loop unrolling
        
    *   Useful for debugging, testing, or in environments where optimization causes issues
        

These options are specified at build time via meson-python arguments:

pip install . \-Csetup\-args\=-Dcpu\-baseline\="min" \-Csetup\-args\=-Dcpu\-dispatch\="max"
\# or through spin
spin build \-- \-Dcpu\-baseline\="min" \-Dcpu\-dispatch\="max"

Copy to clipboard

`cpu-baseline` and `cpu-dispatch` can be set to specific [CPU groups, features](https://numpy.org/doc/stable/reference/simd/build-options.html#opt-supported-features)
, or [special options](https://numpy.org/doc/stable/reference/simd/build-options.html#opt-special-options)
 that perform specific actions. The following sections describe these options in detail.

Common Usage Scenarios[#](https://numpy.org/doc/stable/reference/simd/build-options.html#common-usage-scenarios "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

### Building for Local Use Only[#](https://numpy.org/doc/stable/reference/simd/build-options.html#building-for-local-use-only "Link to this heading")

When building for your machine only and not planning to distribute:

python \-m build \--wheel \-Csetup\-args\=-Dcpu\-baseline\="native" \-Csetup\-args\=-Dcpu\-dispatch\="none"

Copy to clipboard

This automatically detects and uses all CPU features available on your machine.

Note

A fatal error will be raised if `native` isn’t supported by the host platform.

### Excluding Specific Features[#](https://numpy.org/doc/stable/reference/simd/build-options.html#excluding-specific-features "Link to this heading")

You may want to exclude certain CPU features from the dispatched features:

\# For x86-64: exclude all AVX-512 features
python \-m build \--wheel \-Csetup\-args\=-Dcpu\-dispatch\="max -X86\_V4"

\# For ARM64: exclude SVE
python \-m build \--wheel \-Csetup\-args\=-Dcpu\-dispatch\="max -SVE"

Copy to clipboard

Note

Excluding a feature will also exclude any successor features that are implied by the excluded feature. For example, excluding `X86_V4` will exclude `AVX512_ICL` and `AVX512_SPR` as well.

### Targeting Older CPUs[#](https://numpy.org/doc/stable/reference/simd/build-options.html#targeting-older-cpus "Link to this heading")

On `x86-64`, by default the baseline is set to `min` which maps to `X86_V2`. This unsuitable for older CPUs (before 2009) or old virtual machines. To address this, set the baseline to `none`:

python \-m build \--wheel \-Csetup\-args\=-Dcpu\-baseline\="none"

Copy to clipboard

This will create a build that is compatible with all x86 CPUs, but without any manual optimizations or SIMD code paths for the baseline. The build will rely only on dispatched code paths for optimization.

### Targeting Newer CPUs[#](https://numpy.org/doc/stable/reference/simd/build-options.html#targeting-newer-cpus "Link to this heading")

Raising the baseline improves performance for two main reasons:

1.  Dispatched kernels don’t cover all code paths
    
2.  A higher baseline leads to smaller binary size as the compiler won’t generate code paths for excluded dispatched features
    

For CPUs from 2015 and newer, setting the baseline to `X86_V3` may be suitable:

python \-m build \--wheel \-Csetup\-args\=-Dcpu\-baseline\="min+X86\_V3"

Copy to clipboard

Supported CPU Features By Architecture[#](https://numpy.org/doc/stable/reference/simd/build-options.html#supported-cpu-features-by-architecture "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

NumPy supports optimized code paths for multiple CPU architectures. Below are the supported feature groups for each architecture. The name of the feature group can be used in the build options `cpu-baseline` and `cpu-dispatch`.

### X86[#](https://numpy.org/doc/stable/reference/simd/build-options.html#x86 "Link to this heading")

| Name | Implies | Includes |
| --- | --- | --- |
| `X86_V2` |     | `SSE` `SSE2` `SSE3` `SSSE3` `SSE4_1` `SSE4_2` `POPCNT` `CX16` `LAHF` |
| `X86_V3` | `X86_V2` | `AVX` `AVX2` `FMA3` `BMI` `BMI2` `LZCNT` `F16C` `MOVBE` |
| `X86_V4` | `X86_V3` | `AVX512F` `AVX512CD` `AVX512VL` `AVX512BW` `AVX512DQ` |
| `AVX512_ICL` | `X86_V4` | `AVX512VBMI` `AVX512VBMI2` `AVX512VNNI` `AVX512BITALG` `AVX512VPOPCNTDQ` `AVX512IFMA` `VAES` `GFNI` `VPCLMULQDQ` |
| `AVX512_SPR` | `AVX512_ICL` | `AVX512FP16` |

These groups correspond to CPU generations:

*   `X86_V2`: x86-64-v2 microarchitectures (CPUs since 2009)
    
*   `X86_V3`: x86-64-v3 microarchitectures (CPUs since 2015)
    
*   `X86_V4`: x86-64-v4 microarchitectures (AVX-512 capable CPUs)
    
*   `AVX512_ICL`: Intel Ice Lake and similar CPUs
    
*   `AVX512_SPR`: Intel Sapphire Rapids and newer CPUs
    

Note

On 32-bit x86, `cx16` is excluded from `X86_V2`.

### On IBM/POWER big-endian[#](https://numpy.org/doc/stable/reference/simd/build-options.html#on-ibm-power-big-endian "Link to this heading")

| Name | Implies |
| --- | --- |
| `VSX` |     |
| `VSX2` | `VSX` |
| `VSX3` | `VSX` `VSX2` |
| `VSX4` | `VSX` `VSX2` `VSX3` |

### On IBM/POWER little-endian[#](https://numpy.org/doc/stable/reference/simd/build-options.html#on-ibm-power-little-endian "Link to this heading")

| Name | Implies |
| --- | --- |
| `VSX` | `VSX2` |
| `VSX2` | `VSX` |
| `VSX3` | `VSX` `VSX2` |
| `VSX4` | `VSX` `VSX2` `VSX3` |

### On ARMv7/A32[#](https://numpy.org/doc/stable/reference/simd/build-options.html#on-armv7-a32 "Link to this heading")

| Name | Implies |
| --- | --- |
| `NEON` |     |
| `NEON_FP16` | `NEON` |
| `NEON_VFPV4` | `NEON` `NEON_FP16` |
| `ASIMD` | `NEON` `NEON_FP16` `NEON_VFPV4` |
| `ASIMDHP` | `NEON` `NEON_FP16` `NEON_VFPV4` `ASIMD` |
| `ASIMDDP` | `NEON` `NEON_FP16` `NEON_VFPV4` `ASIMD` |
| `ASIMDFHM` | `NEON` `NEON_FP16` `NEON_VFPV4` `ASIMD` `ASIMDHP` |

### On ARMv8/A64[#](https://numpy.org/doc/stable/reference/simd/build-options.html#on-armv8-a64 "Link to this heading")

| Name | Implies |
| --- | --- |
| `NEON` | `NEON_FP16` `NEON_VFPV4` `ASIMD` |
| `NEON_FP16` | `NEON` `NEON_VFPV4` `ASIMD` |
| `NEON_VFPV4` | `NEON` `NEON_FP16` `ASIMD` |
| `ASIMD` | `NEON` `NEON_FP16` `NEON_VFPV4` |
| `ASIMDHP` | `NEON` `NEON_FP16` `NEON_VFPV4` `ASIMD` |
| `ASIMDDP` | `NEON` `NEON_FP16` `NEON_VFPV4` `ASIMD` |
| `ASIMDFHM` | `NEON` `NEON_FP16` `NEON_VFPV4` `ASIMD` `ASIMDHP` |

### On IBM/ZSYSTEM(S390X)[#](https://numpy.org/doc/stable/reference/simd/build-options.html#on-ibm-zsystem-s390x "Link to this heading")

| Name | Implies |
| --- | --- |
| `VX` |     |
| `VXE` | `VX` |
| `VXE2` | `VX` `VXE` |

### On RISCV64[#](https://numpy.org/doc/stable/reference/simd/build-options.html#on-riscv64 "Link to this heading")

| Name | Implies |
| --- | --- |
| `RVV` |     |

Special Options[#](https://numpy.org/doc/stable/reference/simd/build-options.html#special-options "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

Beyond specific feature names, you can use these special values:

### `NONE`[#](https://numpy.org/doc/stable/reference/simd/build-options.html#none "Link to this heading")

Enables no features (equivalent to an empty string).

### `NATIVE`[#](https://numpy.org/doc/stable/reference/simd/build-options.html#native "Link to this heading")

Enables all features supported by the host CPU.

### `DETECT`[#](https://numpy.org/doc/stable/reference/simd/build-options.html#detect "Link to this heading")

Detects the features enabled by the compiler. This option is appended by default to `cpu-baseline` if `-march`, `-mcpu`, `-xhost`, or `/QxHost` is set in the environment variable `CFLAGS` unless `cpu-baseline-detect` is `disabled`.

### `MIN`[#](https://numpy.org/doc/stable/reference/simd/build-options.html#min "Link to this heading")

Enables the minimum CPU features for each architecture:

| For Arch | Implies |
| --- | --- |
| x86 (32-bit) | `X86_V2` |
| x86-64 | `X86_V2` |
| IBM/POWER (big-endian) | `NONE` |
| IBM/POWER (little-endian) | `VSX` `VSX2` |
| ARMv7/ARMHF | `NONE` |
| ARMv8/AArch64 | `NEON` `NEON_FP16` `NEON_VFPV4` `ASIMD` |
| IBM/ZSYSTEM(S390X) | `NONE` |
| riscv64 | `NONE` |

### `MAX`[#](https://numpy.org/doc/stable/reference/simd/build-options.html#max "Link to this heading")

Enables all features supported by the compiler and platform.

### Operator Operators (`-`/`+`)[#](https://numpy.org/doc/stable/reference/simd/build-options.html#operator-operators "Link to this heading")

Remove or add specific features, useful with `MAX`, `MIN`, and `NATIVE`:

*   Adding a feature (`+`) includes all implied features
    
*   Removing a feature (`-`) excludes all successor features that imply the removed feature
    

Examples:

python \-m build \--wheel \-Csetup\-args\=-Dcpu\-dispatch\="max-X86\_V4"
python \-m build \--wheel \-Csetup\-args\=-Dcpu\-baseline\="min+X86\_V4"

Copy to clipboard

Usage And Behaviors[#](https://numpy.org/doc/stable/reference/simd/build-options.html#usage-and-behaviors "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

### Case Insensitivity[#](https://numpy.org/doc/stable/reference/simd/build-options.html#case-insensitivity "Link to this heading")

CPU features and options are case-insensitive:

python \-m build \--wheel \-Csetup\-args\=-Dcpu\-dispatch\="X86\_v4"

Copy to clipboard

### Mixing Features across Architectures[#](https://numpy.org/doc/stable/reference/simd/build-options.html#mixing-features-across-architectures "Link to this heading")

You can mix features from different architectures:

python \-m build \--wheel \-Csetup\-args\=-Dcpu\-baseline\="X86\_V4 VSX4 SVE"

Copy to clipboard

### Order Independence[#](https://numpy.org/doc/stable/reference/simd/build-options.html#order-independence "Link to this heading")

The order of specified features doesn’t matter:

python \-m build \--wheel \-Csetup\-args\=-Dcpu\-dispatch\="SVE X86\_V4 x86\_v3"

Copy to clipboard

### Separators[#](https://numpy.org/doc/stable/reference/simd/build-options.html#separators "Link to this heading")

You can use spaces or commas as separators:

\# All of these are equivalent
python \-m build \--wheel \-Csetup\-args\=-Dcpu\-dispatch\="X86\_V2 X86\_V4"
python \-m build \--wheel \-Csetup\-args\=-Dcpu\-dispatch\=X86\_V2,X86\_V4

Copy to clipboard

### Feature Combination[#](https://numpy.org/doc/stable/reference/simd/build-options.html#feature-combination "Link to this heading")

Features specified in options are automatically combined with all implied features:

python \-m build \--wheel \-Csetup\-args\=-Dcpu\-baseline\=X86\_V4

Copy to clipboard

Equivalent to:

python \-m build \--wheel \-Csetup\-args\=-Dcpu\-baseline\="X86\_V2 X86\_V3 X86\_V4"

Copy to clipboard

### Baseline Overlapping[#](https://numpy.org/doc/stable/reference/simd/build-options.html#baseline-overlapping "Link to this heading")

Features specified in `cpu-baseline` will be excluded from the `cpu-dispatch` features, along with their implied features, but without excluding successor features that imply them.

For instance, if you specify `cpu-baseline="X86_V4"`, it will exclude `X86_V4` and its implied features `X86_V2` and `X86_V3` from the `cpu-dispatch` features.

### Compile-time Detection[#](https://numpy.org/doc/stable/reference/simd/build-options.html#compile-time-detection "Link to this heading")

Specifying features to `cpu-dispatch` or `cpu-baseline` doesn’t explicitly enable them. Features are detected at compile time, and the maximum available features based on your specified options will be enabled according to toolchain and platform support.

This detection occurs by testing feature availability in the compiler through compile-time source files containing common intrinsics for the specified features. If both the compiler and assembler support the feature, it will be enabled.

For example, if you specify `cpu-dispatch="AVX512_ICL"` but your compiler doesn’t support it, the feature will be excluded from the build. However, any implied features will still be enabled if they’re supported.

Platform differences[#](https://numpy.org/doc/stable/reference/simd/build-options.html#platform-differences "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

Some exceptional conditions force us to link some features together when it come to certain compilers or architectures, resulting in the impossibility of building them separately.

These conditions can be divided into two parts, as follows:

**Architectural compatibility**

The need to align certain CPU features that are assured to be supported by successive generations of the same architecture, some cases:

*   On ppc64le `VSX(ISA 2.06)` and `VSX2(ISA 2.07)` both imply one another since the first generation that supports little-endian mode is `Power-8(ISA 2.07)`
    
*   On AArch64 `NEON NEON_FP16 NEON_VFPV4 ASIMD` implies each other since they are part of the hardware baseline.
    

For example:

\# On ARMv8/A64, specify NEON is going to enable Advanced SIMD
\# and all predecessor extensions
python \-m build \--wheel \-Csetup\-args\=-Dcpu\-baseline\=neon
\# which is equivalent to
python \-m build \--wheel \-Csetup\-args\=-Dcpu\-baseline\="neon neon\_fp16 neon\_vfpv4 asimd"

Copy to clipboard

Note

Please take a deep look at [Supported CPU Features By Architecture](https://numpy.org/doc/stable/reference/simd/build-options.html#opt-supported-features)
, in order to determine the features that imply one another.

Build report[#](https://numpy.org/doc/stable/reference/simd/build-options.html#build-report "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

In most cases, the CPU build options do not produce any fatal errors that lead to hanging the build. Most of the errors that may appear in the build log serve as heavy warnings due to the lack of some expected CPU features by the compiler.

So we strongly recommend checking the final report log, to be aware of what kind of CPU features are enabled and what are not.

You can find the final report of CPU optimizations by tracing meson build log, and here is how it looks on x86\_64/gcc:

Test features "X86\_V2" : Supported 
Test features "X86\_V3" : Supported 
Test features "X86\_V4" : Supported 
Test features "AVX512\_ICL" : Supported 
Test features "AVX512\_SPR" : Supported 
Configuring npy\_cpu\_dispatch\_config.h using configuration
Message: 
CPU Optimization Options
  baseline:
    Requested : min
    Enabled   : X86\_V2
  dispatch:
    Requested : max
    Enabled   : X86\_V3 X86\_V4 AVX512\_ICL AVX512\_SPR

Generating multi-targets for "\_umath\_tests.dispatch.h" 
  Enabled targets: X86\_V3, baseline
Generating multi-targets for "argfunc.dispatch.h" 
  Enabled targets: X86\_V4, X86\_V3, baseline
Generating multi-targets for "x86\_simd\_argsort.dispatch.h" 
  Enabled targets: X86\_V4, X86\_V3
Generating multi-targets for "x86\_simd\_qsort.dispatch.h" 
  Enabled targets: X86\_V4, X86\_V3
Generating multi-targets for "x86\_simd\_qsort\_16bit.dispatch.h" 
  Enabled targets: AVX512\_SPR, AVX512\_ICL
Generating multi-targets for "highway\_qsort.dispatch.h" 
  Enabled targets: 
Generating multi-targets for "highway\_qsort\_16bit.dispatch.h" 
  Enabled targets: 
Generating multi-targets for "loops\_arithm\_fp.dispatch.h" 
  Enabled targets: X86\_V3, baseline
Generating multi-targets for "loops\_arithmetic.dispatch.h" 
  Enabled targets: X86\_V4, X86\_V3, baseline
Generating multi-targets for "loops\_comparison.dispatch.h" 
  Enabled targets: X86\_V4, X86\_V3, baseline
Generating multi-targets for "loops\_exponent\_log.dispatch.h" 
  Enabled targets: X86\_V4, X86\_V3, baseline
Generating multi-targets for "loops\_hyperbolic.dispatch.h" 
  Enabled targets: X86\_V4, X86\_V3, baseline
Generating multi-targets for "loops\_logical.dispatch.h" 
  Enabled targets: X86\_V4, X86\_V3, baseline
Generating multi-targets for "loops\_minmax.dispatch.h" 
  Enabled targets: X86\_V4, X86\_V3, baseline
Generating multi-targets for "loops\_modulo.dispatch.h" 
  Enabled targets: baseline
Generating multi-targets for "loops\_trigonometric.dispatch.h" 
  Enabled targets: X86\_V4, X86\_V3, baseline
Generating multi-targets for "loops\_umath\_fp.dispatch.h" 
  Enabled targets: X86\_V4, baseline
Generating multi-targets for "loops\_unary.dispatch.h" 
  Enabled targets: X86\_V4, baseline
Generating multi-targets for "loops\_unary\_fp.dispatch.h" 
  Enabled targets: baseline
Generating multi-targets for "loops\_unary\_fp\_le.dispatch.h" 
  Enabled targets: baseline
Generating multi-targets for "loops\_unary\_complex.dispatch.h" 
  Enabled targets: X86\_V3, baseline
Generating multi-targets for "loops\_autovec.dispatch.h" 
  Enabled targets: X86\_V3, baseline
Generating multi-targets for "loops\_half.dispatch.h" 
  Enabled targets: AVX512\_SPR, X86\_V4, baseline
WARNING: Project targets '>=1.5.2' but uses feature deprecated since '1.3.0': Source file src/umath/svml/linux/avx512/svml\_z0\_acos\_d\_la.s in the 'objects' kwarg is not an object..
Generating multi-targets for "\_simd.dispatch.h" 
  Enabled targets: X86\_V3, X86\_V4, baseline

Copy to clipboard

Runtime Dispatch[#](https://numpy.org/doc/stable/reference/simd/build-options.html#runtime-dispatch "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

Importing NumPy triggers a scan of the available CPU features from the set of dispatchable features. You can restrict this scan by setting the environment variable `NPY_DISABLE_CPU_FEATURES` to a comma-, tab-, or space-separated list of features to disable.

For instance, on `x86_64` this will disable `X86_V4`:

NPY\_DISABLE\_CPU\_FEATURES\="X86\_V4"

Copy to clipboard

This will raise an error if parsing fails or if the feature was not enabled through the `cpu-dispatch` build option. If the feature is supported by the build but not available on the current CPU, a warning will be emitted instead.

Tracking Dispatched Functions[#](https://numpy.org/doc/stable/reference/simd/build-options.html#tracking-dispatched-functions "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

You can discover which CPU targets are enabled for different optimized functions using the Python function `numpy.lib.introspect.opt_func_info`.

This function offers two optional arguments for filtering results:

1.  `func_name` - For refining function names
    
2.  `signature` - For specifying data types in the signatures
    

For example:

 \>> func\_info \= numpy.lib.introspect.opt\_func\_info(func\_name\='add|abs', signature\='float64|complex64')
 \>> print(json.dumps(func\_info, indent\=2))
 {
  "absolute": {
    "dd": {
      "current": "baseline(X86\_V2)",
      "available": "baseline(X86\_V2)"
    },
    "Ff": {
      "current": "X86\_V3",
      "available": "X86\_V3 baseline(X86\_V2)"
    },
    "Dd": {
      "current": "X86\_V3",
      "available": "X86\_V3 baseline(X86\_V2)"
    }
  },
  "add": {
    "ddd": {
      "current": "X86\_V3",
      "available": "X86\_V3 baseline(X86\_V2)"
    },
    "FFF": {
      "current": "X86\_V3",
      "available": "X86\_V3 baseline(X86\_V2)"
    }
  }
}

Copy to clipboard

On this page