[Skip to main content](https://numpy.org/doc/stable/reference/simd/index.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

CPU/SIMD optimizations[#](https://numpy.org/doc/stable/reference/simd/index.html#cpu-simd-optimizations "Link to this heading")

================================================================================================================================

NumPy comes with a flexible working mechanism that allows it to harness the SIMD features that CPUs own, in order to provide faster and more stable performance on all popular platforms. Currently, NumPy supports the X86, IBM/Power, ARM7 and ARM8 architectures.

The optimization process in NumPy is carried out in three layers:

*   Code is _written_ using the universal intrinsics which is a set of types, macros and functions that are mapped to each supported instruction-sets by using guards that will enable use of the them only when the compiler recognizes them. This allow us to generate multiple kernels for the same functionality, in which each generated kernel represents a set of instructions that related one or multiple certain CPU features. The first kernel represents the minimum (baseline) CPU features, and the other kernels represent the additional (dispatched) CPU features.
    
*   At _compile_ time, CPU build options are used to define the minimum and additional features to support, based on user choice and compiler support. The appropriate intrinsics are overlaid with the platform / architecture intrinsics, and multiple kernels are compiled.
    
*   At _runtime import_, the CPU is probed for the set of supported CPU features. A mechanism is used to grab the pointer to the most appropriate kernel, and this will be the one called for the function.
    

Note

NumPy community had a deep discussion before implementing this work, please check [NEP 38 — Using SIMD optimization instructions for performance](https://numpy.org/neps/nep-0038-SIMD-optimizations.html "(in NumPy Enhancement Proposals)")
 for more clarification.

*   [CPU Build Options](https://numpy.org/doc/stable/reference/simd/build-options.html)
    *   [Overview](https://numpy.org/doc/stable/reference/simd/build-options.html#overview)
        
    *   [Key Configuration Options](https://numpy.org/doc/stable/reference/simd/build-options.html#key-configuration-options)
        
    *   [Common Usage Scenarios](https://numpy.org/doc/stable/reference/simd/build-options.html#common-usage-scenarios)
        *   [Building for Local Use Only](https://numpy.org/doc/stable/reference/simd/build-options.html#building-for-local-use-only)
            
        *   [Excluding Specific Features](https://numpy.org/doc/stable/reference/simd/build-options.html#excluding-specific-features)
            
        *   [Targeting Older CPUs](https://numpy.org/doc/stable/reference/simd/build-options.html#targeting-older-cpus)
            
        *   [Targeting Newer CPUs](https://numpy.org/doc/stable/reference/simd/build-options.html#targeting-newer-cpus)
            
    *   [Supported CPU Features By Architecture](https://numpy.org/doc/stable/reference/simd/build-options.html#supported-cpu-features-by-architecture)
        *   [X86](https://numpy.org/doc/stable/reference/simd/build-options.html#x86)
            
        *   [On IBM/POWER big-endian](https://numpy.org/doc/stable/reference/simd/build-options.html#on-ibm-power-big-endian)
            
        *   [On IBM/POWER little-endian](https://numpy.org/doc/stable/reference/simd/build-options.html#on-ibm-power-little-endian)
            
        *   [On ARMv7/A32](https://numpy.org/doc/stable/reference/simd/build-options.html#on-armv7-a32)
            
        *   [On ARMv8/A64](https://numpy.org/doc/stable/reference/simd/build-options.html#on-armv8-a64)
            
        *   [On IBM/ZSYSTEM(S390X)](https://numpy.org/doc/stable/reference/simd/build-options.html#on-ibm-zsystem-s390x)
            
        *   [On RISCV64](https://numpy.org/doc/stable/reference/simd/build-options.html#on-riscv64)
            
    *   [Special Options](https://numpy.org/doc/stable/reference/simd/build-options.html#special-options)
        *   [`NONE`](https://numpy.org/doc/stable/reference/simd/build-options.html#none)
            
        *   [`NATIVE`](https://numpy.org/doc/stable/reference/simd/build-options.html#native)
            
        *   [`DETECT`](https://numpy.org/doc/stable/reference/simd/build-options.html#detect)
            
        *   [`MIN`](https://numpy.org/doc/stable/reference/simd/build-options.html#min)
            
        *   [`MAX`](https://numpy.org/doc/stable/reference/simd/build-options.html#max)
            
        *   [Operator Operators (`-`/`+`)](https://numpy.org/doc/stable/reference/simd/build-options.html#operator-operators)
            
    *   [Usage And Behaviors](https://numpy.org/doc/stable/reference/simd/build-options.html#usage-and-behaviors)
        *   [Case Insensitivity](https://numpy.org/doc/stable/reference/simd/build-options.html#case-insensitivity)
            
        *   [Mixing Features across Architectures](https://numpy.org/doc/stable/reference/simd/build-options.html#mixing-features-across-architectures)
            
        *   [Order Independence](https://numpy.org/doc/stable/reference/simd/build-options.html#order-independence)
            
        *   [Separators](https://numpy.org/doc/stable/reference/simd/build-options.html#separators)
            
        *   [Feature Combination](https://numpy.org/doc/stable/reference/simd/build-options.html#feature-combination)
            
        *   [Baseline Overlapping](https://numpy.org/doc/stable/reference/simd/build-options.html#baseline-overlapping)
            
        *   [Compile-time Detection](https://numpy.org/doc/stable/reference/simd/build-options.html#compile-time-detection)
            
    *   [Platform differences](https://numpy.org/doc/stable/reference/simd/build-options.html#platform-differences)
        
    *   [Build report](https://numpy.org/doc/stable/reference/simd/build-options.html#build-report)
        
    *   [Runtime Dispatch](https://numpy.org/doc/stable/reference/simd/build-options.html#runtime-dispatch)
        
    *   [Tracking Dispatched Functions](https://numpy.org/doc/stable/reference/simd/build-options.html#tracking-dispatched-functions)
        
*   [How does the CPU dispatcher work?](https://numpy.org/doc/stable/reference/simd/how-it-works.html)
    *   [1- Configuration](https://numpy.org/doc/stable/reference/simd/how-it-works.html#configuration)
        
    *   [2- Discovering the environment](https://numpy.org/doc/stable/reference/simd/how-it-works.html#discovering-the-environment)
        
    *   [3- Validating the requested optimizations](https://numpy.org/doc/stable/reference/simd/how-it-works.html#validating-the-requested-optimizations)
        
    *   [4- Generating the main configuration header](https://numpy.org/doc/stable/reference/simd/how-it-works.html#generating-the-main-configuration-header)
        
    *   [5- Dispatch-able sources and configuration statements](https://numpy.org/doc/stable/reference/simd/how-it-works.html#dispatch-able-sources-and-configuration-statements)