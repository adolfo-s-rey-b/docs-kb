### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/memory.html "Memory Management")
     |
*   [previous](https://docs.python.org/3/c-api/profiling.html "Profiling and tracing")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [Python Initialization Configuration](https://docs.python.org/3/c-api/init_config.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Python Initialization Configuration[¶](https://docs.python.org/3/c-api/init_config.html#python-initialization-configuration "Link to this heading")

====================================================================================================================================================

PyInitConfig C API[¶](https://docs.python.org/3/c-api/init_config.html#pyinitconfig-c-api "Link to this heading")

------------------------------------------------------------------------------------------------------------------

Added in version 3.14.

Python can be initialized with [`Py_InitializeFromInitConfig()`](https://docs.python.org/3/c-api/init_config.html#c.Py_InitializeFromInitConfig "Py_InitializeFromInitConfig")
.

The [`Py_RunMain()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_RunMain "Py_RunMain")
 function can be used to write a customized Python program.

See also [Initialization, Finalization, and Threads](https://docs.python.org/3/c-api/interp-lifecycle.html#initialization)
.

See also

[**PEP 741**](https://peps.python.org/pep-0741/)
 “Python Configuration C API”.

### Example[¶](https://docs.python.org/3/c-api/init_config.html#example "Link to this heading")

Example of customized Python always running with the [Python Development Mode](https://docs.python.org/3/library/devmode.html#devmode)
 enabled; return `-1` on error:

int init\_python(void)
{
    PyInitConfig \*config \= PyInitConfig\_Create();
    if (config \== NULL) {
        printf("PYTHON INIT ERROR: memory allocation failed\\n");
        return \-1;
    }

    // Enable the Python Development Mode
    if (PyInitConfig\_SetInt(config, "dev\_mode", 1) < 0) {
        goto error;
    }

    // Initialize Python with the configuration
    if (Py\_InitializeFromInitConfig(config) < 0) {
        goto error;
    }
    PyInitConfig\_Free(config);
    return 0;

error:
    {
        // Display the error message.
        //
        // This uncommon braces style is used, because you cannot make
        // goto targets point to variable declarations.
        const char \*err\_msg;
        (void)PyInitConfig\_GetError(config, &err\_msg);
        printf("PYTHON INIT ERROR: %s\\n", err\_msg);
        PyInitConfig\_Free(config);
        return \-1;
    }
}

### Create Config[¶](https://docs.python.org/3/c-api/init_config.html#create-config "Link to this heading")

struct PyInitConfig[¶](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig "Link to this definition")
  

Opaque structure to configure the Python initialization.

[PyInitConfig](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig "PyInitConfig")
 \*PyInitConfig\_Create(void)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig_Create "Link to this definition")
  

Create a new initialization configuration using [Isolated Configuration](https://docs.python.org/3/c-api/init_config.html#init-isolated-conf)
 default values.

It must be freed by [`PyInitConfig_Free()`](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig_Free "PyInitConfig_Free")
.

Return `NULL` on memory allocation failure.

void PyInitConfig\_Free([PyInitConfig](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig "PyInitConfig")
 \*config)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig_Free "Link to this definition")
  

Free memory of the initialization configuration _config_.

If _config_ is `NULL`, no operation is performed.

### Error Handling[¶](https://docs.python.org/3/c-api/init_config.html#error-handling "Link to this heading")

int PyInitConfig\_GetError([PyInitConfig](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig "PyInitConfig")
 \*config, const char \*\*err\_msg)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig_GetError "Link to this definition")
  

Get the _config_ error message.

*   Set _\*err\_msg_ and return `1` if an error is set.
    
*   Set _\*err\_msg_ to `NULL` and return `0` otherwise.
    

An error message is a UTF-8 encoded string.

If _config_ has an exit code, format the exit code as an error message.

The error message remains valid until another `PyInitConfig` function is called with _config_. The caller doesn’t have to free the error message.

int PyInitConfig\_GetExitCode([PyInitConfig](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig "PyInitConfig")
 \*config, int \*exitcode)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig_GetExitCode "Link to this definition")
  

Get the _config_ exit code.

*   Set _\*exitcode_ and return `1` if _config_ has an exit code set.
    
*   Return `0` if _config_ has no exit code set.
    

Only the `Py_InitializeFromInitConfig()` function can set an exit code if the `parse_argv` option is non-zero.

An exit code can be set when parsing the command line failed (exit code `2`) or when a command line option asks to display the command line help (exit code `0`).

### Get Options[¶](https://docs.python.org/3/c-api/init_config.html#get-options "Link to this heading")

The configuration option _name_ parameter must be a non-NULL null-terminated UTF-8 encoded string. See [Configuration Options](https://docs.python.org/3/c-api/init_config.html#pyinitconfig-opts)
.

int PyInitConfig\_HasOption([PyInitConfig](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig "PyInitConfig")
 \*config, const char \*name)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig_HasOption "Link to this definition")
  

Test if the configuration has an option called _name_.

Return `1` if the option exists, or return `0` otherwise.

int PyInitConfig\_GetInt([PyInitConfig](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig "PyInitConfig")
 \*config, const char \*name, int64\_t \*value)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig_GetInt "Link to this definition")
  

Get an integer configuration option.

*   Set _\*value_, and return `0` on success.
    
*   Set an error in _config_ and return `-1` on error.
    

int PyInitConfig\_GetStr([PyInitConfig](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig "PyInitConfig")
 \*config, const char \*name, char \*\*value)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig_GetStr "Link to this definition")
  

Get a string configuration option as a null-terminated UTF-8 encoded string.

*   Set _\*value_, and return `0` on success.
    
*   Set an error in _config_ and return `-1` on error.
    

_\*value_ can be set to `NULL` if the option is unset or if the option is an optional string. Optional strings are documented with the type `str | None` in the [Configuration Options](https://docs.python.org/3/c-api/init_config.html#pyinitconfig-opts)
 table.

On success, the string must be released with `free(value)` if it’s not `NULL`.

int PyInitConfig\_GetStrList([PyInitConfig](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig "PyInitConfig")
 \*config, const char \*name, size\_t \*length, char \*\*\*items)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig_GetStrList "Link to this definition")
  

Get a string list configuration option as an array of null-terminated UTF-8 encoded strings.

*   Set _\*length_ and _\*items_, and return `0` on success.
    
*   Set an error in _config_ and return `-1` on error.
    

On success, the string list must be released with `PyInitConfig_FreeStrList(length, items)`.

void PyInitConfig\_FreeStrList(size\_t length, char \*\*items)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig_FreeStrList "Link to this definition")
  

Free memory of a string list created by `PyInitConfig_GetStrList()`.

### Set Options[¶](https://docs.python.org/3/c-api/init_config.html#set-options "Link to this heading")

The configuration option _name_ parameter must be a non-NULL null-terminated UTF-8 encoded string. See [Configuration Options](https://docs.python.org/3/c-api/init_config.html#pyinitconfig-opts)
.

Some configuration options have side effects on other options. This logic is only implemented when `Py_InitializeFromInitConfig()` is called, not by the “Set” functions below. For example, setting `dev_mode` to `1` does not set `faulthandler` to `1`.

int PyInitConfig\_SetInt([PyInitConfig](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig "PyInitConfig")
 \*config, const char \*name, int64\_t value)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig_SetInt "Link to this definition")
  

Set an integer configuration option.

*   Return `0` on success.
    
*   Set an error in _config_ and return `-1` on error.
    

int PyInitConfig\_SetStr([PyInitConfig](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig "PyInitConfig")
 \*config, const char \*name, const char \*value)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig_SetStr "Link to this definition")
  

Set a string configuration option from a null-terminated UTF-8 encoded string. The string is copied.

Options documented with the type `str | None` in the [Configuration Options](https://docs.python.org/3/c-api/init_config.html#pyinitconfig-opts)
 table can be set to `NULL`.

*   Return `0` on success.
    
*   Set an error in _config_ and return `-1` on error.
    

int PyInitConfig\_SetStrList([PyInitConfig](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig "PyInitConfig")
 \*config, const char \*name, size\_t length, char \*const \*items)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig_SetStrList "Link to this definition")
  

Set a string list configuration option from an array of null-terminated UTF-8 encoded strings. The string list is copied.

*   Return `0` on success.
    
*   Set an error in _config_ and return `-1` on error.
    

### Module[¶](https://docs.python.org/3/c-api/init_config.html#module "Link to this heading")

int PyInitConfig\_AddModule([PyInitConfig](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig "PyInitConfig")
 \*config, const char \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*(\*initfunc)(void))[¶](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig_AddModule "Link to this definition")
  

Add a built-in extension module to the table of built-in modules.

The new module can be imported by the name _name_, and uses the function _initfunc_ as the initialization function called on the first attempted import.

*   Return `0` on success.
    
*   Set an error in _config_ and return `-1` on error.
    

If Python is initialized multiple times, `PyInitConfig_AddModule()` must be called at each Python initialization.

Similar to the [`PyImport_AppendInittab()`](https://docs.python.org/3/c-api/import.html#c.PyImport_AppendInittab "PyImport_AppendInittab")
 function.

### Initialize Python[¶](https://docs.python.org/3/c-api/init_config.html#initialize-python "Link to this heading")

int Py\_InitializeFromInitConfig([PyInitConfig](https://docs.python.org/3/c-api/init_config.html#c.PyInitConfig "PyInitConfig")
 \*config)[¶](https://docs.python.org/3/c-api/init_config.html#c.Py_InitializeFromInitConfig "Link to this definition")
  

Initialize Python from the initialization configuration.

*   Return `0` on success.
    
*   Set an error in _config_ and return `-1` on error.
    
*   Set an exit code in _config_ and return `-1` if Python wants to exit.
    

See `PyInitConfig_GetExitcode()` for the exit code case.

Configuration Options[¶](https://docs.python.org/3/c-api/init_config.html#configuration-options "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

| Option | PyConfig/PyPreConfig member | Type | Visibility |
| --- | --- | --- | --- |
| `"allocator"` | [`allocator`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.allocator "PyPreConfig.allocator") | `int` | Read-only |
| `"argv"` | [`argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv") | `list[str]` | Public |
| `"base_exec_prefix"` | [`base_exec_prefix`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.base_exec_prefix "PyConfig.base_exec_prefix") | `str \| None` | Public |
| `"base_executable"` | [`base_executable`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.base_executable "PyConfig.base_executable") | `str \| None` | Public |
| `"base_prefix"` | [`base_prefix`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.base_prefix "PyConfig.base_prefix") | `str \| None` | Public |
| `"buffered_stdio"` | [`buffered_stdio`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.buffered_stdio "PyConfig.buffered_stdio") | `bool` | Read-only |
| `"bytes_warning"` | [`bytes_warning`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.bytes_warning "PyConfig.bytes_warning") | `int` | Public |
| `"check_hash_pycs_mode"` | [`check_hash_pycs_mode`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.check_hash_pycs_mode "PyConfig.check_hash_pycs_mode") | `str` | Read-only |
| `"code_debug_ranges"` | [`code_debug_ranges`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.code_debug_ranges "PyConfig.code_debug_ranges") | `bool` | Read-only |
| `"coerce_c_locale"` | [`coerce_c_locale`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.coerce_c_locale "PyPreConfig.coerce_c_locale") | `bool` | Read-only |
| `"coerce_c_locale_warn"` | [`coerce_c_locale_warn`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.coerce_c_locale_warn "PyPreConfig.coerce_c_locale_warn") | `bool` | Read-only |
| `"configure_c_stdio"` | [`configure_c_stdio`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.configure_c_stdio "PyConfig.configure_c_stdio") | `bool` | Read-only |
| `"configure_locale"` | [`configure_locale`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.configure_locale "PyPreConfig.configure_locale") | `bool` | Read-only |
| `"cpu_count"` | [`cpu_count`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.cpu_count "PyConfig.cpu_count") | `int` | Public |
| `"dev_mode"` | [`dev_mode`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.dev_mode "PyConfig.dev_mode") | `bool` | Read-only |
| `"dump_refs"` | [`dump_refs`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.dump_refs "PyConfig.dump_refs") | `bool` | Read-only |
| `"dump_refs_file"` | [`dump_refs_file`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.dump_refs_file "PyConfig.dump_refs_file") | `str \| None` | Read-only |
| `"exec_prefix"` | [`exec_prefix`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.exec_prefix "PyConfig.exec_prefix") | `str \| None` | Public |
| `"executable"` | [`executable`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.executable "PyConfig.executable") | `str \| None` | Public |
| `"faulthandler"` | [`faulthandler`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.faulthandler "PyConfig.faulthandler") | `bool` | Read-only |
| `"filesystem_encoding"` | [`filesystem_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_encoding "PyConfig.filesystem_encoding") | `str` | Read-only |
| `"filesystem_errors"` | [`filesystem_errors`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_errors "PyConfig.filesystem_errors") | `str` | Read-only |
| `"hash_seed"` | [`hash_seed`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.hash_seed "PyConfig.hash_seed") | `int` | Read-only |
| `"home"` | [`home`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.home "PyConfig.home") | `str \| None` | Read-only |
| `"import_time"` | [`import_time`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.import_time "PyConfig.import_time") | `int` | Read-only |
| `"inspect"` | [`inspect`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.inspect "PyConfig.inspect") | `bool` | Public |
| `"install_signal_handlers"` | [`install_signal_handlers`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.install_signal_handlers "PyConfig.install_signal_handlers") | `bool` | Read-only |
| `"int_max_str_digits"` | [`int_max_str_digits`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.int_max_str_digits "PyConfig.int_max_str_digits") | `int` | Public |
| `"interactive"` | [`interactive`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.interactive "PyConfig.interactive") | `bool` | Public |
| `"isolated"` | [`isolated`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.isolated "PyConfig.isolated") | `bool` | Read-only |
| `"lazy_imports"` | [`lazy_imports`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.lazy_imports "PyConfig.lazy_imports") | `int` | Public |
| `"legacy_windows_fs_encoding"` | [`legacy_windows_fs_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.legacy_windows_fs_encoding "PyPreConfig.legacy_windows_fs_encoding") | `bool` | Read-only |
| `"legacy_windows_stdio"` | [`legacy_windows_stdio`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.legacy_windows_stdio "PyConfig.legacy_windows_stdio") | `bool` | Read-only |
| `"malloc_stats"` | [`malloc_stats`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.malloc_stats "PyConfig.malloc_stats") | `bool` | Read-only |
| `"module_search_paths"` | [`module_search_paths`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.module_search_paths "PyConfig.module_search_paths") | `list[str]` | Public |
| `"optimization_level"` | [`optimization_level`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.optimization_level "PyConfig.optimization_level") | `int` | Public |
| `"orig_argv"` | [`orig_argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.orig_argv "PyConfig.orig_argv") | `list[str]` | Read-only |
| `"parse_argv"` | [`parse_argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.parse_argv "PyConfig.parse_argv") | `bool` | Read-only |
| `"parser_debug"` | [`parser_debug`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.parser_debug "PyConfig.parser_debug") | `bool` | Public |
| `"pathconfig_warnings"` | [`pathconfig_warnings`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.pathconfig_warnings "PyConfig.pathconfig_warnings") | `bool` | Read-only |
| `"perf_profiling"` | [`perf_profiling`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.perf_profiling "PyConfig.perf_profiling") | `bool` | Read-only |
| `"platlibdir"` | [`platlibdir`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.platlibdir "PyConfig.platlibdir") | `str` | Public |
| `"prefix"` | [`prefix`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.prefix "PyConfig.prefix") | `str \| None` | Public |
| `"program_name"` | [`program_name`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.program_name "PyConfig.program_name") | `str` | Read-only |
| `"pycache_prefix"` | [`pycache_prefix`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.pycache_prefix "PyConfig.pycache_prefix") | `str \| None` | Public |
| `"quiet"` | [`quiet`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.quiet "PyConfig.quiet") | `bool` | Public |
| `"run_command"` | [`run_command`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.run_command "PyConfig.run_command") | `str \| None` | Read-only |
| `"run_filename"` | [`run_filename`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.run_filename "PyConfig.run_filename") | `str \| None` | Read-only |
| `"run_module"` | [`run_module`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.run_module "PyConfig.run_module") | `str \| None` | Read-only |
| `"run_presite"` | [`run_presite`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.run_presite "PyConfig.run_presite") | `str \| None` | Read-only |
| `"safe_path"` | [`safe_path`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.safe_path "PyConfig.safe_path") | `bool` | Read-only |
| `"show_ref_count"` | [`show_ref_count`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.show_ref_count "PyConfig.show_ref_count") | `bool` | Read-only |
| `"site_import"` | [`site_import`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.site_import "PyConfig.site_import") | `bool` | Read-only |
| `"skip_source_first_line"` | [`skip_source_first_line`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.skip_source_first_line "PyConfig.skip_source_first_line") | `bool` | Read-only |
| `"stdio_encoding"` | [`stdio_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.stdio_encoding "PyConfig.stdio_encoding") | `str \| None` | Read-only |
| `"stdio_errors"` | [`stdio_errors`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.stdio_errors "PyConfig.stdio_errors") | `str` | Read-only |
| `"stdlib_dir"` | [`stdlib_dir`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.stdlib_dir "PyConfig.stdlib_dir") | `str \| None` | Public |
| `"tracemalloc"` | [`tracemalloc`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.tracemalloc "PyConfig.tracemalloc") | `int` | Read-only |
| `"use_environment"` | [`use_environment`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.use_environment "PyConfig.use_environment") | `bool` | Public |
| `"use_frozen_modules"` | [`use_frozen_modules`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.use_frozen_modules "PyConfig.use_frozen_modules") | `bool` | Read-only |
| `"use_hash_seed"` | [`use_hash_seed`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.use_hash_seed "PyConfig.use_hash_seed") | `bool` | Read-only |
| `"use_system_logger"` | [`use_system_logger`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.use_system_logger "PyConfig.use_system_logger") | `bool` | Read-only |
| `"user_site_directory"` | [`user_site_directory`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.user_site_directory "PyConfig.user_site_directory") | `bool` | Read-only |
| `"utf8_mode"` | [`utf8_mode`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.utf8_mode "PyPreConfig.utf8_mode") | `bool` | Read-only |
| `"verbose"` | [`verbose`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.verbose "PyConfig.verbose") | `int` | Public |
| `"warn_default_encoding"` | [`warn_default_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.warn_default_encoding "PyConfig.warn_default_encoding") | `bool` | Read-only |
| `"warnoptions"` | [`warnoptions`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.warnoptions "PyConfig.warnoptions") | `list[str]` | Public |
| `"write_bytecode"` | [`write_bytecode`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.write_bytecode "PyConfig.write_bytecode") | `bool` | Public |
| `"xoptions"` | [`xoptions`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.xoptions "PyConfig.xoptions") | `dict[str, str]` | Public |
| `"_pystats"` | [`_pystats`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig._pystats "PyConfig._pystats") | `bool` | Read-only |

The type `str | None` means that the option is an optional string which can be set to `NULL`.

Visibility:

*   Public: Can be retrieved by [`PyConfig_Get()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
     and set by [`PyConfig_Set()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Set "PyConfig_Set")
    .
    
*   Read-only: Can be retrieved by [`PyConfig_Get()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
    , but cannot be set by [`PyConfig_Set()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Set "PyConfig_Set")
    .
    

Runtime Python configuration API[¶](https://docs.python.org/3/c-api/init_config.html#runtime-python-configuration-api "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

At runtime, it’s possible to get and set configuration options using [`PyConfig_Get()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
 and [`PyConfig_Set()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Set "PyConfig_Set")
 functions.

The configuration option _name_ parameter must be a non-NULL null-terminated UTF-8 encoded string. See [Configuration Options](https://docs.python.org/3/c-api/init_config.html#pyinitconfig-opts)
.

Some options are read from the [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.")
 attributes. For example, the option `"argv"` is read from [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyConfig\_Get(const char \*name)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "Link to this definition")
  

Get the current runtime value of a configuration option as a Python object.

*   Return a new reference on success.
    
*   Set an exception and return `NULL` on error.
    

The object type depends on the configuration option. It can be:

*   `bool`
    
*   `int`
    
*   `str`
    
*   `list[str]`
    
*   `dict[str, str]`
    

The caller must have an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
. The function cannot be called before Python initialization nor after Python finalization.

Added in version 3.14.

int PyConfig\_GetInt(const char \*name, int \*value)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_GetInt "Link to this definition")
  

Similar to [`PyConfig_Get()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
, but get the value as a C int.

*   Return `0` on success.
    
*   Set an exception and return `-1` on error.
    

Added in version 3.14.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyConfig\_Names(void)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Names "Link to this definition")
  

Get all configuration option names as a `frozenset`.

*   Return a new reference on success.
    
*   Set an exception and return `NULL` on error.
    

The caller must have an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
. The function cannot be called before Python initialization nor after Python finalization.

Added in version 3.14.

int PyConfig\_Set(const char \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*value)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Set "Link to this definition")
  

Set the current runtime value of a configuration option.

*   Raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
     if there is no option _name_.
    
*   Raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
     if _value_ is an invalid value.
    
*   Raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
     if the option is read-only (cannot be set).
    
*   Raise a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
     if _value_ has not the proper type.
    

The caller must have an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
. The function cannot be called before Python initialization nor after Python finalization.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `cpython.PyConfig_Set` with arguments `name`, `value`.

Added in version 3.14.

Changed in version 3.15: The function now replaces [`sys.flags`](https://docs.python.org/3/library/sys.html#sys.flags "sys.flags")
 (create a new object), instead of modifying `sys.flags` in-place.

PyConfig C API[¶](https://docs.python.org/3/c-api/init_config.html#pyconfig-c-api "Link to this heading")

----------------------------------------------------------------------------------------------------------

Added in version 3.8.

Python can be initialized with [`Py_InitializeFromConfig()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig "Py_InitializeFromConfig")
 and the [`PyConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
 structure. It can be preinitialized with [`Py_PreInitialize()`](https://docs.python.org/3/c-api/init_config.html#c.Py_PreInitialize "Py_PreInitialize")
 and the [`PyPreConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig "PyPreConfig")
 structure.

There are two kinds of configuration:

*   The [Python Configuration](https://docs.python.org/3/c-api/init_config.html#init-python-config)
     can be used to build a customized Python which behaves as the regular Python. For example, environment variables and command line arguments are used to configure Python.
    
*   The [Isolated Configuration](https://docs.python.org/3/c-api/init_config.html#init-isolated-conf)
     can be used to embed Python into an application. It isolates Python from the system. For example, environment variables are ignored, the LC\_CTYPE locale is left unchanged and no signal handler is registered.
    

The [`Py_RunMain()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_RunMain "Py_RunMain")
 function can be used to write a customized Python program.

See also [Initialization, Finalization, and Threads](https://docs.python.org/3/c-api/interp-lifecycle.html#initialization)
.

See also

[**PEP 587**](https://peps.python.org/pep-0587/)
 “Python Initialization Configuration”.

### Example[¶](https://docs.python.org/3/c-api/init_config.html#id1 "Link to this heading")

Example of customized Python always running in isolated mode:

int main(int argc, char \*\*argv)
{
    PyStatus status;

    PyConfig config;
    PyConfig\_InitPythonConfig(&config);
    config.isolated \= 1;

    /\* Decode command line arguments.
       Implicitly preinitialize Python (in isolated mode). \*/
    status \= PyConfig\_SetBytesArgv(&config, argc, argv);
    if (PyStatus\_Exception(status)) {
        goto exception;
    }

    status \= Py\_InitializeFromConfig(&config);
    if (PyStatus\_Exception(status)) {
        goto exception;
    }
    PyConfig\_Clear(&config);

    return Py\_RunMain();

exception:
    PyConfig\_Clear(&config);
    if (PyStatus\_IsExit(status)) {
        return status.exitcode;
    }
    /\* Display the error message and exit the process with
       non-zero exit code \*/
    Py\_ExitStatusException(status);
}

### PyWideStringList[¶](https://docs.python.org/3/c-api/init_config.html#pywidestringlist "Link to this heading")

type PyWideStringList[¶](https://docs.python.org/3/c-api/init_config.html#c.PyWideStringList "Link to this definition")
  

List of `wchar_t*` strings.

If _length_ is non-zero, _items_ must be non-`NULL` and all strings must be non-`NULL`.

Methods:

[PyStatus](https://docs.python.org/3/c-api/init_config.html#c.PyStatus "PyStatus")
 PyWideStringList\_Append([PyWideStringList](https://docs.python.org/3/c-api/init_config.html#c.PyWideStringList "PyWideStringList")
 \*list, const wchar\_t \*item)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyWideStringList_Append "Link to this definition")
  

Append _item_ to _list_.

Python must be preinitialized to call this function.

[PyStatus](https://docs.python.org/3/c-api/init_config.html#c.PyStatus "PyStatus")
 PyWideStringList\_Insert([PyWideStringList](https://docs.python.org/3/c-api/init_config.html#c.PyWideStringList "PyWideStringList")
 \*list, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 index, const wchar\_t \*item)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyWideStringList_Insert "Link to this definition")
  

Insert _item_ into _list_ at _index_.

If _index_ is greater than or equal to _list_ length, append _item_ to _list_.

_index_ must be greater than or equal to `0`.

Python must be preinitialized to call this function.

Structure fields:

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 length[¶](https://docs.python.org/3/c-api/init_config.html#c.PyWideStringList.length "Link to this definition")
  

List length.

wchar\_t \*\*items[¶](https://docs.python.org/3/c-api/init_config.html#c.PyWideStringList.items "Link to this definition")
  

List items.

### PyStatus[¶](https://docs.python.org/3/c-api/init_config.html#pystatus "Link to this heading")

type PyStatus[¶](https://docs.python.org/3/c-api/init_config.html#c.PyStatus "Link to this definition")
  

Structure to store an initialization function status: success, error or exit.

For an error, it can store the C function name which created the error.

Structure fields:

int exitcode[¶](https://docs.python.org/3/c-api/init_config.html#c.PyStatus.exitcode "Link to this definition")
  

Exit code. Argument passed to `exit()`.

const char \*err\_msg[¶](https://docs.python.org/3/c-api/init_config.html#c.PyStatus.err_msg "Link to this definition")
  

Error message.

const char \*func[¶](https://docs.python.org/3/c-api/init_config.html#c.PyStatus.func "Link to this definition")
  

Name of the function which created an error, can be `NULL`.

Functions to create a status:

[PyStatus](https://docs.python.org/3/c-api/init_config.html#c.PyStatus "PyStatus")
 PyStatus\_Ok(void)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyStatus_Ok "Link to this definition")
  

Success.

[PyStatus](https://docs.python.org/3/c-api/init_config.html#c.PyStatus "PyStatus")
 PyStatus\_Error(const char \*err\_msg)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyStatus_Error "Link to this definition")
  

Initialization error with a message.

_err\_msg_ must not be `NULL`.

[PyStatus](https://docs.python.org/3/c-api/init_config.html#c.PyStatus "PyStatus")
 PyStatus\_NoMemory(void)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyStatus_NoMemory "Link to this definition")
  

Memory allocation failure (out of memory).

[PyStatus](https://docs.python.org/3/c-api/init_config.html#c.PyStatus "PyStatus")
 PyStatus\_Exit(int exitcode)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyStatus_Exit "Link to this definition")
  

Exit Python with the specified exit code.

Functions to handle a status:

int PyStatus\_Exception([PyStatus](https://docs.python.org/3/c-api/init_config.html#c.PyStatus "PyStatus")
 status)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyStatus_Exception "Link to this definition")
  

Is the status an error or an exit? If true, the exception must be handled; by calling [`Py_ExitStatusException()`](https://docs.python.org/3/c-api/init_config.html#c.Py_ExitStatusException "Py_ExitStatusException")
 for example.

int PyStatus\_IsError([PyStatus](https://docs.python.org/3/c-api/init_config.html#c.PyStatus "PyStatus")
 status)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyStatus_IsError "Link to this definition")
  

Is the result an error?

int PyStatus\_IsExit([PyStatus](https://docs.python.org/3/c-api/init_config.html#c.PyStatus "PyStatus")
 status)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyStatus_IsExit "Link to this definition")
  

Is the result an exit?

void Py\_ExitStatusException([PyStatus](https://docs.python.org/3/c-api/init_config.html#c.PyStatus "PyStatus")
 status)[¶](https://docs.python.org/3/c-api/init_config.html#c.Py_ExitStatusException "Link to this definition")
  

Call `exit(exitcode)` if _status_ is an exit. Print the error message and exit with a non-zero exit code if _status_ is an error. Must only be called if `PyStatus_Exception(status)` is non-zero.

Note

Internally, Python uses macros which set `PyStatus.func`, whereas functions to create a status set `func` to `NULL`.

Example:

PyStatus alloc(void \*\*ptr, size\_t size)
{
    \*ptr \= PyMem\_RawMalloc(size);
    if (\*ptr \== NULL) {
        return PyStatus\_NoMemory();
    }
    return PyStatus\_Ok();
}

int main(int argc, char \*\*argv)
{
    void \*ptr;
    PyStatus status \= alloc(&ptr, 16);
    if (PyStatus\_Exception(status)) {
        Py\_ExitStatusException(status);
    }
    PyMem\_RawFree(ptr);
    return 0;
}

### PyPreConfig[¶](https://docs.python.org/3/c-api/init_config.html#pypreconfig "Link to this heading")

type PyPreConfig[¶](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig "Link to this definition")
  

Structure used to preinitialize Python.

Function to initialize a preconfiguration:

void PyPreConfig\_InitPythonConfig([PyPreConfig](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig "PyPreConfig")
 \*preconfig)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig_InitPythonConfig "Link to this definition")
  

Initialize the preconfiguration with [Python Configuration](https://docs.python.org/3/c-api/init_config.html#init-python-config)
.

void PyPreConfig\_InitIsolatedConfig([PyPreConfig](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig "PyPreConfig")
 \*preconfig)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig_InitIsolatedConfig "Link to this definition")
  

Initialize the preconfiguration with [Isolated Configuration](https://docs.python.org/3/c-api/init_config.html#init-isolated-conf)
.

Structure fields:

int allocator[¶](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.allocator "Link to this definition")
  

Name of the Python memory allocators:

*   `PYMEM_ALLOCATOR_NOT_SET` (`0`): don’t change memory allocators (use defaults).
    
*   `PYMEM_ALLOCATOR_DEFAULT` (`1`): [default memory allocators](https://docs.python.org/3/c-api/memory.html#default-memory-allocators)
    .
    
*   `PYMEM_ALLOCATOR_DEBUG` (`2`): [default memory allocators](https://docs.python.org/3/c-api/memory.html#default-memory-allocators)
     with [debug hooks](https://docs.python.org/3/c-api/memory.html#pymem-debug-hooks)
    .
    
*   `PYMEM_ALLOCATOR_MALLOC` (`3`): use `malloc()` of the C library.
    
*   `PYMEM_ALLOCATOR_MALLOC_DEBUG` (`4`): force usage of `malloc()` with [debug hooks](https://docs.python.org/3/c-api/memory.html#pymem-debug-hooks)
    .
    
*   `PYMEM_ALLOCATOR_PYMALLOC` (`5`): [Python pymalloc memory allocator](https://docs.python.org/3/c-api/memory.html#pymalloc)
    .
    
*   `PYMEM_ALLOCATOR_PYMALLOC_DEBUG` (`6`): [Python pymalloc memory allocator](https://docs.python.org/3/c-api/memory.html#pymalloc)
     with [debug hooks](https://docs.python.org/3/c-api/memory.html#pymem-debug-hooks)
    .
    
*   `PYMEM_ALLOCATOR_MIMALLOC` (`7`): use `mimalloc`, a fast malloc replacement.
    
*   `PYMEM_ALLOCATOR_MIMALLOC_DEBUG` (`8`): use `mimalloc`, a fast malloc replacement with [debug hooks](https://docs.python.org/3/c-api/memory.html#pymem-debug-hooks)
    .
    

`PYMEM_ALLOCATOR_PYMALLOC` and `PYMEM_ALLOCATOR_PYMALLOC_DEBUG` are not supported if Python is [`configured using --without-pymalloc`](https://docs.python.org/3/using/configure.html#cmdoption-without-pymalloc)
.

`PYMEM_ALLOCATOR_MIMALLOC` and `PYMEM_ALLOCATOR_MIMALLOC_DEBUG` are not supported if Python is [`configured using --without-mimalloc`](https://docs.python.org/3/using/configure.html#cmdoption-without-mimalloc)
 or if the underlying atomic support isn’t available.

See [Memory Management](https://docs.python.org/3/c-api/memory.html#memory)
.

Default: `PYMEM_ALLOCATOR_NOT_SET`.

int configure\_locale[¶](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.configure_locale "Link to this definition")
  

Set the LC\_CTYPE locale to the user preferred locale.

If equals to `0`, set [`coerce_c_locale`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.coerce_c_locale "PyPreConfig.coerce_c_locale")
 and [`coerce_c_locale_warn`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.coerce_c_locale_warn "PyPreConfig.coerce_c_locale_warn")
 members to `0`.

See the [locale encoding](https://docs.python.org/3/glossary.html#term-locale-encoding)
.

Default: `1` in Python config, `0` in isolated config.

int coerce\_c\_locale[¶](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.coerce_c_locale "Link to this definition")
  

If equals to `2`, coerce the C locale.

If equals to `1`, read the LC\_CTYPE locale to decide if it should be coerced.

See the [locale encoding](https://docs.python.org/3/glossary.html#term-locale-encoding)
.

Default: `-1` in Python config, `0` in isolated config.

int coerce\_c\_locale\_warn[¶](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.coerce_c_locale_warn "Link to this definition")
  

If non-zero, emit a warning if the C locale is coerced.

Default: `-1` in Python config, `0` in isolated config.

int dev\_mode[¶](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.dev_mode "Link to this definition")
  

[Python Development Mode](https://docs.python.org/3/library/devmode.html#devmode)
: see [`PyConfig.dev_mode`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.dev_mode "PyConfig.dev_mode")
.

Default: `-1` in Python mode, `0` in isolated mode.

int isolated[¶](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.isolated "Link to this definition")
  

Isolated mode: see [`PyConfig.isolated`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.isolated "PyConfig.isolated")
.

Default: `0` in Python mode, `1` in isolated mode.

int legacy\_windows\_fs\_encoding[¶](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.legacy_windows_fs_encoding "Link to this definition")
  

If non-zero:

*   Set [`PyPreConfig.utf8_mode`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.utf8_mode "PyPreConfig.utf8_mode")
     to `0`,
    
*   Set [`PyConfig.filesystem_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_encoding "PyConfig.filesystem_encoding")
     to `"mbcs"`,
    
*   Set [`PyConfig.filesystem_errors`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_errors "PyConfig.filesystem_errors")
     to `"replace"`.
    

Initialized from the [`PYTHONLEGACYWINDOWSFSENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING)
 environment variable value.

Only available on Windows. `#ifdef MS_WINDOWS` macro can be used for Windows specific code.

Default: `0`.

int parse\_argv[¶](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.parse_argv "Link to this definition")
  

If non-zero, [`Py_PreInitializeFromArgs()`](https://docs.python.org/3/c-api/init_config.html#c.Py_PreInitializeFromArgs "Py_PreInitializeFromArgs")
 and [`Py_PreInitializeFromBytesArgs()`](https://docs.python.org/3/c-api/init_config.html#c.Py_PreInitializeFromBytesArgs "Py_PreInitializeFromBytesArgs")
 parse their `argv` argument the same way the regular Python parses command line arguments: see [Command Line Arguments](https://docs.python.org/3/using/cmdline.html#using-on-cmdline)
.

Default: `1` in Python config, `0` in isolated config.

int use\_environment[¶](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.use_environment "Link to this definition")
  

Use [environment variables](https://docs.python.org/3/using/cmdline.html#using-on-envvars)
? See [`PyConfig.use_environment`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.use_environment "PyConfig.use_environment")
.

Default: `1` in Python config and `0` in isolated config.

int utf8\_mode[¶](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.utf8_mode "Link to this definition")
  

If non-zero, enable the [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode)
.

Set to `0` or `1` by the [`-X utf8`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command line option and the [`PYTHONUTF8`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUTF8)
 environment variable.

Default: `1`.

### Preinitialize Python with PyPreConfig[¶](https://docs.python.org/3/c-api/init_config.html#preinitialize-python-with-pypreconfig "Link to this heading")

The preinitialization of Python:

*   Set the Python memory allocators ([`PyPreConfig.allocator`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.allocator "PyPreConfig.allocator")
    )
    
*   Configure the LC\_CTYPE locale ([locale encoding](https://docs.python.org/3/glossary.html#term-locale-encoding)
    )
    
*   Set the [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode)
     ([`PyPreConfig.utf8_mode`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.utf8_mode "PyPreConfig.utf8_mode")
    )
    

The current preconfiguration (`PyPreConfig` type) is stored in `_PyRuntime.preconfig`.

Functions to preinitialize Python:

[PyStatus](https://docs.python.org/3/c-api/init_config.html#c.PyStatus "PyStatus")
 Py\_PreInitialize(const [PyPreConfig](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig "PyPreConfig")
 \*preconfig)[¶](https://docs.python.org/3/c-api/init_config.html#c.Py_PreInitialize "Link to this definition")
  

Preinitialize Python from _preconfig_ preconfiguration.

_preconfig_ must not be `NULL`.

[PyStatus](https://docs.python.org/3/c-api/init_config.html#c.PyStatus "PyStatus")
 Py\_PreInitializeFromBytesArgs(const [PyPreConfig](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig "PyPreConfig")
 \*preconfig, int argc, char \*const \*argv)[¶](https://docs.python.org/3/c-api/init_config.html#c.Py_PreInitializeFromBytesArgs "Link to this definition")
  

Preinitialize Python from _preconfig_ preconfiguration.

Parse _argv_ command line arguments (bytes strings) if [`parse_argv`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.parse_argv "PyPreConfig.parse_argv")
 of _preconfig_ is non-zero.

_preconfig_ must not be `NULL`.

[PyStatus](https://docs.python.org/3/c-api/init_config.html#c.PyStatus "PyStatus")
 Py\_PreInitializeFromArgs(const [PyPreConfig](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig "PyPreConfig")
 \*preconfig, int argc, wchar\_t \*const \*argv)[¶](https://docs.python.org/3/c-api/init_config.html#c.Py_PreInitializeFromArgs "Link to this definition")
  

Preinitialize Python from _preconfig_ preconfiguration.

Parse _argv_ command line arguments (wide strings) if [`parse_argv`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.parse_argv "PyPreConfig.parse_argv")
 of _preconfig_ is non-zero.

_preconfig_ must not be `NULL`.

The caller is responsible to handle exceptions (error or exit) using [`PyStatus_Exception()`](https://docs.python.org/3/c-api/init_config.html#c.PyStatus_Exception "PyStatus_Exception")
 and [`Py_ExitStatusException()`](https://docs.python.org/3/c-api/init_config.html#c.Py_ExitStatusException "Py_ExitStatusException")
.

For [Python Configuration](https://docs.python.org/3/c-api/init_config.html#init-python-config)
 ([`PyPreConfig_InitPythonConfig()`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig_InitPythonConfig "PyPreConfig_InitPythonConfig")
), if Python is initialized with command line arguments, the command line arguments must also be passed to preinitialize Python, since they have an effect on the pre-configuration like encodings. For example, the [`-X utf8`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command line option enables the [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode)
.

`PyMem_SetAllocator()` can be called after [`Py_PreInitialize()`](https://docs.python.org/3/c-api/init_config.html#c.Py_PreInitialize "Py_PreInitialize")
 and before [`Py_InitializeFromConfig()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig "Py_InitializeFromConfig")
 to install a custom memory allocator. It can be called before `Py_PreInitialize()` if [`PyPreConfig.allocator`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.allocator "PyPreConfig.allocator")
 is set to `PYMEM_ALLOCATOR_NOT_SET`.

Python memory allocation functions like [`PyMem_RawMalloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawMalloc "PyMem_RawMalloc")
 must not be used before the Python preinitialization, whereas calling directly `malloc()` and `free()` is always safe. [`Py_DecodeLocale()`](https://docs.python.org/3/c-api/sys.html#c.Py_DecodeLocale "Py_DecodeLocale")
 must not be called before the Python preinitialization.

Example using the preinitialization to enable the [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode)
:

PyStatus status;
PyPreConfig preconfig;
PyPreConfig\_InitPythonConfig(&preconfig);

preconfig.utf8\_mode \= 1;

status \= Py\_PreInitialize(&preconfig);
if (PyStatus\_Exception(status)) {
    Py\_ExitStatusException(status);
}

/\* at this point, Python speaks UTF-8 \*/

Py\_Initialize();
/\* ... use Python API here ... \*/
Py\_Finalize();

### PyConfig[¶](https://docs.python.org/3/c-api/init_config.html#pyconfig "Link to this heading")

type PyConfig[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "Link to this definition")
  

Structure containing most parameters to configure Python.

When done, the [`PyConfig_Clear()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Clear "PyConfig_Clear")
 function must be used to release the configuration memory.

Structure methods:

void PyConfig\_InitPythonConfig([PyConfig](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
 \*config)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_InitPythonConfig "Link to this definition")
  

Initialize configuration with the [Python Configuration](https://docs.python.org/3/c-api/init_config.html#init-python-config)
.

void PyConfig\_InitIsolatedConfig([PyConfig](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
 \*config)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_InitIsolatedConfig "Link to this definition")
  

Initialize configuration with the [Isolated Configuration](https://docs.python.org/3/c-api/init_config.html#init-isolated-conf)
.

[PyStatus](https://docs.python.org/3/c-api/init_config.html#c.PyStatus "PyStatus")
 PyConfig\_SetString([PyConfig](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
 \*config, wchar\_t \*const \*config\_str, const wchar\_t \*str)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_SetString "Link to this definition")
  

Copy the wide character string _str_ into `*config_str`.

[Preinitialize Python](https://docs.python.org/3/c-api/init_config.html#c-preinit)
 if needed.

[PyStatus](https://docs.python.org/3/c-api/init_config.html#c.PyStatus "PyStatus")
 PyConfig\_SetBytesString([PyConfig](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
 \*config, wchar\_t \*const \*config\_str, const char \*str)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_SetBytesString "Link to this definition")
  

Decode _str_ using [`Py_DecodeLocale()`](https://docs.python.org/3/c-api/sys.html#c.Py_DecodeLocale "Py_DecodeLocale")
 and set the result into `*config_str`.

[Preinitialize Python](https://docs.python.org/3/c-api/init_config.html#c-preinit)
 if needed.

[PyStatus](https://docs.python.org/3/c-api/init_config.html#c.PyStatus "PyStatus")
 PyConfig\_SetArgv([PyConfig](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
 \*config, int argc, wchar\_t \*const \*argv)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_SetArgv "Link to this definition")
  

Set command line arguments ([`argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")
 member of _config_) from the _argv_ list of wide character strings.

[Preinitialize Python](https://docs.python.org/3/c-api/init_config.html#c-preinit)
 if needed.

[PyStatus](https://docs.python.org/3/c-api/init_config.html#c.PyStatus "PyStatus")
 PyConfig\_SetBytesArgv([PyConfig](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
 \*config, int argc, char \*const \*argv)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_SetBytesArgv "Link to this definition")
  

Set command line arguments ([`argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")
 member of _config_) from the _argv_ list of bytes strings. Decode bytes using [`Py_DecodeLocale()`](https://docs.python.org/3/c-api/sys.html#c.Py_DecodeLocale "Py_DecodeLocale")
.

[Preinitialize Python](https://docs.python.org/3/c-api/init_config.html#c-preinit)
 if needed.

[PyStatus](https://docs.python.org/3/c-api/init_config.html#c.PyStatus "PyStatus")
 PyConfig\_SetWideStringList([PyConfig](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
 \*config, [PyWideStringList](https://docs.python.org/3/c-api/init_config.html#c.PyWideStringList "PyWideStringList")
 \*list, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 length, wchar\_t \*\*items)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_SetWideStringList "Link to this definition")
  

Set the list of wide strings _list_ to _length_ and _items_.

[Preinitialize Python](https://docs.python.org/3/c-api/init_config.html#c-preinit)
 if needed.

[PyStatus](https://docs.python.org/3/c-api/init_config.html#c.PyStatus "PyStatus")
 PyConfig\_Read([PyConfig](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
 \*config)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Read "Link to this definition")
  

Read all Python configuration.

Fields which are already initialized are left unchanged.

Fields for [path configuration](https://docs.python.org/3/c-api/init_config.html#init-path-config)
 are no longer calculated or modified when calling this function, as of Python 3.11.

The [`PyConfig_Read()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Read "PyConfig_Read")
 function only parses [`PyConfig.argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")
 arguments once: [`PyConfig.parse_argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.parse_argv "PyConfig.parse_argv")
 is set to `2` after arguments are parsed. Since Python arguments are stripped from `PyConfig.argv`, parsing arguments twice would parse the application options as Python options.

[Preinitialize Python](https://docs.python.org/3/c-api/init_config.html#c-preinit)
 if needed.

Changed in version 3.10: The [`PyConfig.argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")
 arguments are now only parsed once, [`PyConfig.parse_argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.parse_argv "PyConfig.parse_argv")
 is set to `2` after arguments are parsed, and arguments are only parsed if `PyConfig.parse_argv` equals `1`.

Changed in version 3.11: [`PyConfig_Read()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Read "PyConfig_Read")
 no longer calculates all paths, and so fields listed under [Python Path Configuration](https://docs.python.org/3/c-api/init_config.html#init-path-config)
 may no longer be updated until [`Py_InitializeFromConfig()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig "Py_InitializeFromConfig")
 is called.

void PyConfig\_Clear([PyConfig](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
 \*config)[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Clear "Link to this definition")
  

Release configuration memory.

Most `PyConfig` methods [preinitialize Python](https://docs.python.org/3/c-api/init_config.html#c-preinit)
 if needed. In that case, the Python preinitialization configuration ([`PyPreConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig "PyPreConfig")
) is based on the [`PyConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
. If configuration fields which are in common with `PyPreConfig` are tuned, they must be set before calling a `PyConfig` method:

*   [`PyConfig.dev_mode`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.dev_mode "PyConfig.dev_mode")
    
*   [`PyConfig.isolated`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.isolated "PyConfig.isolated")
    
*   [`PyConfig.parse_argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.parse_argv "PyConfig.parse_argv")
    
*   [`PyConfig.use_environment`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.use_environment "PyConfig.use_environment")
    

Moreover, if [`PyConfig_SetArgv()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_SetArgv "PyConfig_SetArgv")
 or [`PyConfig_SetBytesArgv()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_SetBytesArgv "PyConfig_SetBytesArgv")
 is used, this method must be called before other methods, since the preinitialization configuration depends on command line arguments (if [`parse_argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.parse_argv "PyConfig.parse_argv")
 is non-zero).

The caller of these methods is responsible to handle exceptions (error or exit) using `PyStatus_Exception()` and `Py_ExitStatusException()`.

Structure fields:

[PyWideStringList](https://docs.python.org/3/c-api/init_config.html#c.PyWideStringList "PyWideStringList")
 argv[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "Link to this definition")
  

Set [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv")
 command line arguments based on [`argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")
. These parameters are similar to those passed to the program’s `main()` function with the difference that the first entry should refer to the script file to be executed rather than the executable hosting the Python interpreter. If there isn’t a script that will be run, the first entry in `argv` can be an empty string.

Set [`parse_argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.parse_argv "PyConfig.parse_argv")
 to `1` to parse [`argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")
 the same way the regular Python parses Python command line arguments and then to strip Python arguments from `argv`.

If [`argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")
 is empty, an empty string is added to ensure that [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv")
 always exists and is never empty.

Default: `NULL`.

See also the [`orig_argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.orig_argv "PyConfig.orig_argv")
 member.

int safe\_path[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.safe_path "Link to this definition")
  

If equals to zero, `Py_RunMain()` prepends a potentially unsafe path to [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
 at startup:

*   If [`argv[0]`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")
     is equal to `L"-m"` (`python -m module`), prepend the current working directory.
    
*   If running a script (`python script.py`), prepend the script’s directory. If it’s a symbolic link, resolve symbolic links.
    
*   Otherwise (`python -c code` and `python`), prepend an empty string, which means the current working directory.
    

Set to `1` by the [`-P`](https://docs.python.org/3/using/cmdline.html#cmdoption-P)
 command line option and the [`PYTHONSAFEPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSAFEPATH)
 environment variable.

Default: `0` in Python config, `1` in isolated config.

Added in version 3.11.

wchar\_t \*base\_exec\_prefix[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.base_exec_prefix "Link to this definition")
  

[`sys.base_exec_prefix`](https://docs.python.org/3/library/sys.html#sys.base_exec_prefix "sys.base_exec_prefix")
.

Default: `NULL`.

Part of the [Python Path Configuration](https://docs.python.org/3/c-api/init_config.html#init-path-config)
 output.

See also [`PyConfig.exec_prefix`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.exec_prefix "PyConfig.exec_prefix")
.

wchar\_t \*base\_executable[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.base_executable "Link to this definition")
  

Python base executable: `sys._base_executable`.

Set by the `__PYVENV_LAUNCHER__` environment variable.

Set from [`PyConfig.executable`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.executable "PyConfig.executable")
 if `NULL`.

Default: `NULL`.

Part of the [Python Path Configuration](https://docs.python.org/3/c-api/init_config.html#init-path-config)
 output.

See also [`PyConfig.executable`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.executable "PyConfig.executable")
.

wchar\_t \*base\_prefix[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.base_prefix "Link to this definition")
  

[`sys.base_prefix`](https://docs.python.org/3/library/sys.html#sys.base_prefix "sys.base_prefix")
.

Default: `NULL`.

Part of the [Python Path Configuration](https://docs.python.org/3/c-api/init_config.html#init-path-config)
 output.

See also [`PyConfig.prefix`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.prefix "PyConfig.prefix")
.

int buffered\_stdio[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.buffered_stdio "Link to this definition")
  

If equals to `0` and [`configure_c_stdio`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.configure_c_stdio "PyConfig.configure_c_stdio")
 is non-zero, disable buffering on the C streams stdout and stderr.

Set to `0` by the [`-u`](https://docs.python.org/3/using/cmdline.html#cmdoption-u)
 command line option and the [`PYTHONUNBUFFERED`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUNBUFFERED)
 environment variable.

stdin is always opened in buffered mode.

Default: `1`.

int bytes\_warning[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.bytes_warning "Link to this definition")
  

If equals to `1`, issue a warning when comparing [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 or [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
 with [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, or comparing `bytes` with [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
.

If equal or greater to `2`, raise a [`BytesWarning`](https://docs.python.org/3/builtins/exceptions.html#BytesWarning "BytesWarning")
 exception in these cases.

Incremented by the [`-b`](https://docs.python.org/3/using/cmdline.html#cmdoption-b)
 command line option.

Default: `0`.

Deprecated since version 3.15, will be removed in version 3.17: The [`-b`](https://docs.python.org/3/using/cmdline.html#cmdoption-b)
 and `-bb` options will become no-op in 3.17. [`bytes_warning`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.bytes_warning "PyConfig.bytes_warning")
 member will be removed in 3.17.

int warn\_default\_encoding[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.warn_default_encoding "Link to this definition")
  

If non-zero, emit a [`EncodingWarning`](https://docs.python.org/3/builtins/exceptions.html#EncodingWarning "EncodingWarning")
 warning when [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper")
 uses its default encoding. See [Opt-in EncodingWarning](https://docs.python.org/3/library/io.html#io-encoding-warning)
 for details.

Default: `0`.

Added in version 3.10.

int code\_debug\_ranges[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.code_debug_ranges "Link to this definition")
  

If equals to `0`, disables the inclusion of the end line and column mappings in code objects. Also disables traceback printing carets to specific error locations.

Set to `0` by the [`PYTHONNODEBUGRANGES`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONNODEBUGRANGES)
 environment variable and by the [`-X no_debug_ranges`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command line option.

Default: `1`.

Added in version 3.11.

wchar\_t \*check\_hash\_pycs\_mode[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.check_hash_pycs_mode "Link to this definition")
  

Control the validation behavior of hash-based `.pyc` files: value of the [`--check-hash-based-pycs`](https://docs.python.org/3/using/cmdline.html#cmdoption-check-hash-based-pycs)
 command line option.

Valid values:

*   `L"always"`: Hash the source file for invalidation regardless of value of the ‘check\_source’ flag.
    
*   `L"never"`: Assume that hash-based pycs always are valid.
    
*   `L"default"`: The ‘check\_source’ flag in hash-based pycs determines invalidation.
    

Default: `L"default"`.

See also [**PEP 552**](https://peps.python.org/pep-0552/)
 “Deterministic pycs”.

int configure\_c\_stdio[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.configure_c_stdio "Link to this definition")
  

If non-zero, configure C standard streams:

*   On Windows, set the binary mode (`O_BINARY`) on stdin, stdout and stderr.
    
*   If [`buffered_stdio`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.buffered_stdio "PyConfig.buffered_stdio")
     equals zero, disable buffering of stdin, stdout and stderr streams.
    
*   If [`interactive`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.interactive "PyConfig.interactive")
     is non-zero, enable stream buffering on stdin and stdout (only stdout on Windows).
    

Default: `1` in Python config, `0` in isolated config.

int dev\_mode[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.dev_mode "Link to this definition")
  

If non-zero, enable the [Python Development Mode](https://docs.python.org/3/library/devmode.html#devmode)
.

Set to `1` by the [`-X dev`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 option and the [`PYTHONDEVMODE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDEVMODE)
 environment variable.

Default: `-1` in Python mode, `0` in isolated mode.

int dump\_refs[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.dump_refs "Link to this definition")
  

Dump Python references?

If non-zero, dump all objects which are still alive at exit.

Set to `1` by the [`PYTHONDUMPREFS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDUMPREFS)
 environment variable.

Needs a special build of Python with the `Py_TRACE_REFS` macro defined: see the [`configure --with-trace-refs option`](https://docs.python.org/3/using/configure.html#cmdoption-with-trace-refs)
.

Default: `0`.

wchar\_t \*dump\_refs\_file[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.dump_refs_file "Link to this definition")
  

Filename where to dump Python references.

Set by the [`PYTHONDUMPREFSFILE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDUMPREFSFILE)
 environment variable.

Default: `NULL`.

Added in version 3.11.

wchar\_t \*exec\_prefix[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.exec_prefix "Link to this definition")
  

The site-specific directory prefix where the platform-dependent Python files are installed: [`sys.exec_prefix`](https://docs.python.org/3/library/sys.html#sys.exec_prefix "sys.exec_prefix")
.

Default: `NULL`.

Part of the [Python Path Configuration](https://docs.python.org/3/c-api/init_config.html#init-path-config)
 output.

See also [`PyConfig.base_exec_prefix`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.base_exec_prefix "PyConfig.base_exec_prefix")
.

wchar\_t \*executable[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.executable "Link to this definition")
  

The absolute path of the executable binary for the Python interpreter: [`sys.executable`](https://docs.python.org/3/library/sys.html#sys.executable "sys.executable")
.

Default: `NULL`.

Part of the [Python Path Configuration](https://docs.python.org/3/c-api/init_config.html#init-path-config)
 output.

See also [`PyConfig.base_executable`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.base_executable "PyConfig.base_executable")
.

int faulthandler[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.faulthandler "Link to this definition")
  

Enable faulthandler?

If non-zero, call [`faulthandler.enable()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.enable "faulthandler.enable")
 at startup.

Set to `1` by [`-X faulthandler`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 and the [`PYTHONFAULTHANDLER`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONFAULTHANDLER)
 environment variable.

Default: `-1` in Python mode, `0` in isolated mode.

wchar\_t \*filesystem\_encoding[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_encoding "Link to this definition")
  

[Filesystem encoding](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
: [`sys.getfilesystemencoding()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencoding "sys.getfilesystemencoding")
.

On macOS, Android and VxWorks: use `"utf-8"` by default.

On Windows: use `"utf-8"` by default, or `"mbcs"` if [`legacy_windows_fs_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.legacy_windows_fs_encoding "PyPreConfig.legacy_windows_fs_encoding")
 of [`PyPreConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig "PyPreConfig")
 is non-zero.

Default encoding on other platforms:

*   `"utf-8"` if [`PyPreConfig.utf8_mode`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.utf8_mode "PyPreConfig.utf8_mode")
     is non-zero.
    
*   `"ascii"` if Python detects that `nl_langinfo(CODESET)` announces the ASCII encoding, whereas the `mbstowcs()` function decodes from a different encoding (usually Latin1).
    
*   `"utf-8"` if `nl_langinfo(CODESET)` returns an empty string.
    
*   Otherwise, use the [locale encoding](https://docs.python.org/3/glossary.html#term-locale-encoding)
    : `nl_langinfo(CODESET)` result.
    

At Python startup, the encoding name is normalized to the Python codec name. For example, `"ANSI_X3.4-1968"` is replaced with `"ascii"`.

See also the [`filesystem_errors`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_errors "PyConfig.filesystem_errors")
 member.

See also [`PyUnicode_EncodeFSDefault()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_EncodeFSDefault "PyUnicode_EncodeFSDefault")
 and [related functions](https://docs.python.org/3/c-api/unicode.html#capi-filesystem-encoding)
 for encoding paths at runtime.

wchar\_t \*filesystem\_errors[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_errors "Link to this definition")
  

[Filesystem error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
: [`sys.getfilesystemencodeerrors()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencodeerrors "sys.getfilesystemencodeerrors")
.

On Windows: use `"surrogatepass"` by default, or `"replace"` if [`legacy_windows_fs_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.legacy_windows_fs_encoding "PyPreConfig.legacy_windows_fs_encoding")
 of [`PyPreConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig "PyPreConfig")
 is non-zero.

On other platforms: use `"surrogateescape"` by default.

Supported error handlers:

*   `"strict"`
    
*   `"surrogateescape"`
    
*   `"surrogatepass"` (only supported with the UTF-8 encoding)
    

See also the [`filesystem_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_encoding "PyConfig.filesystem_encoding")
 member.

int use\_frozen\_modules[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.use_frozen_modules "Link to this definition")
  

If non-zero, use frozen modules.

Set by the [`PYTHON_FROZEN_MODULES`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_FROZEN_MODULES)
 environment variable.

Default: `1` in a release build, or `0` in a [debug build](https://docs.python.org/3/using/configure.html#debug-build)
.

unsigned long hash\_seed[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.hash_seed "Link to this definition")
  

int use\_hash\_seed[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.use_hash_seed "Link to this definition")
  

Randomized hash function seed.

If [`use_hash_seed`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.use_hash_seed "PyConfig.use_hash_seed")
 is zero, a seed is chosen randomly at Python startup, and [`hash_seed`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.hash_seed "PyConfig.hash_seed")
 is ignored.

Set by the [`PYTHONHASHSEED`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHASHSEED)
 environment variable.

Default _use\_hash\_seed_ value: `-1` in Python mode, `0` in isolated mode.

wchar\_t \*home[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.home "Link to this definition")
  

Set the default Python “home” directory, that is, the location of the standard Python libraries (see [`PYTHONHOME`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHOME)
).

Set by the [`PYTHONHOME`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHOME)
 environment variable.

Default: `NULL`.

Part of the [Python Path Configuration](https://docs.python.org/3/c-api/init_config.html#init-path-config)
 input.

int import\_time[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.import_time "Link to this definition")
  

> If `1`, profile import time. If `2`, include additional output that indicates when an imported module has already been loaded.
> 
> Set by the [`-X importtime`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
>  option and the [`PYTHONPROFILEIMPORTTIME`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPROFILEIMPORTTIME)
>  environment variable.
> 
> Default: `0`.

Changed in version 3.14: Added support for `import_time = 2`

int inspect[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.inspect "Link to this definition")
  

Enter interactive mode after executing a script or a command.

If greater than `0`, enable inspect: when a script is passed as first argument or the -c option is used, enter interactive mode after executing the script or the command, even when [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin")
 does not appear to be a terminal.

Incremented by the [`-i`](https://docs.python.org/3/using/cmdline.html#cmdoption-i)
 command line option. Set to `1` if the [`PYTHONINSPECT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONINSPECT)
 environment variable is non-empty.

Default: `0`.

int install\_signal\_handlers[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.install_signal_handlers "Link to this definition")
  

Install Python signal handlers?

Default: `1` in Python mode, `0` in isolated mode.

int interactive[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.interactive "Link to this definition")
  

If greater than `0`, enable the interactive mode (REPL).

Incremented by the [`-i`](https://docs.python.org/3/using/cmdline.html#cmdoption-i)
 command line option.

Default: `0`.

int int\_max\_str\_digits[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.int_max_str_digits "Link to this definition")
  

Configures the [integer string conversion length limitation](https://docs.python.org/3/builtins/stdtypes.html#int-max-str-digits)
. An initial value of `-1` means the value will be taken from the command line or environment or otherwise default to 4300 ([`sys.int_info.default_max_str_digits`](https://docs.python.org/3/library/sys.html#sys.int_info.default_max_str_digits "sys.int_info.default_max_str_digits")
). A value of `0` disables the limitation. Values greater than zero but less than 640 ([`sys.int_info.str_digits_check_threshold`](https://docs.python.org/3/library/sys.html#sys.int_info.str_digits_check_threshold "sys.int_info.str_digits_check_threshold")
) are unsupported and will produce an error.

Configured by the [`-X int_max_str_digits`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command line flag or the [`PYTHONINTMAXSTRDIGITS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONINTMAXSTRDIGITS)
 environment variable.

Default: `-1` in Python mode. 4300 ([`sys.int_info.default_max_str_digits`](https://docs.python.org/3/library/sys.html#sys.int_info.default_max_str_digits "sys.int_info.default_max_str_digits")
) in isolated mode.

Added in version 3.12.

int cpu\_count[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.cpu_count "Link to this definition")
  

If the value of [`cpu_count`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.cpu_count "PyConfig.cpu_count")
 is not `-1` then it will override the return values of [`os.cpu_count()`](https://docs.python.org/3/library/os.html#os.cpu_count "os.cpu_count")
, [`os.process_cpu_count()`](https://docs.python.org/3/library/os.html#os.process_cpu_count "os.process_cpu_count")
, and [`multiprocessing.cpu_count()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.cpu_count "multiprocessing.cpu_count")
.

Configured by the `-X cpu_count=_n|default_` command line flag or the [`PYTHON_CPU_COUNT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_CPU_COUNT)
 environment variable.

Default: `-1`.

Added in version 3.13.

int isolated[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.isolated "Link to this definition")
  

If greater than `0`, enable isolated mode:

*   Set [`safe_path`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.safe_path "PyConfig.safe_path")
     to `1`: don’t prepend a potentially unsafe path to [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
     at Python startup, such as the current directory, the script’s directory or an empty string.
    
*   Set [`use_environment`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.use_environment "PyConfig.use_environment")
     to `0`: ignore `PYTHON` environment variables.
    
*   Set [`user_site_directory`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.user_site_directory "PyConfig.user_site_directory")
     to `0`: don’t add the user site directory to [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
    .
    
*   Python REPL doesn’t import [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.")
     nor enable default readline configuration on interactive prompts.
    

Set to `1` by the [`-I`](https://docs.python.org/3/using/cmdline.html#cmdoption-I)
 command line option.

Default: `0` in Python mode, `1` in isolated mode.

See also the [Isolated Configuration](https://docs.python.org/3/c-api/init_config.html#init-isolated-conf)
 and [`PyPreConfig.isolated`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.isolated "PyPreConfig.isolated")
.

int lazy\_imports[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.lazy_imports "Link to this definition")
  

Control [lazy imports](https://docs.python.org/3/reference/simple_stmts.html#lazy-imports)
.

A value of `-1` keeps the default behaviour, where only imports marked with the `lazy` keyword are lazy. A value of `1` makes every import lazy. `0` is rejected.

Configured by the [`-X lazy_imports`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command line option or the [`PYTHON_LAZY_IMPORTS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_LAZY_IMPORTS)
 environment variable.

Default: `-1`.

Added in version 3.15.

int legacy\_windows\_stdio[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.legacy_windows_stdio "Link to this definition")
  

If non-zero, use [`io.FileIO`](https://docs.python.org/3/library/io.html#io.FileIO "io.FileIO")
 instead of `io._WindowsConsoleIO` for [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin")
, [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
 and [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr")
.

Set to `1` if the [`PYTHONLEGACYWINDOWSSTDIO`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSSTDIO)
 environment variable is set to a non-empty string.

Only available on Windows. `#ifdef MS_WINDOWS` macro can be used for Windows specific code.

Default: `0`.

See also the [**PEP 528**](https://peps.python.org/pep-0528/)
 (Change Windows console encoding to UTF-8).

int malloc\_stats[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.malloc_stats "Link to this definition")
  

If non-zero, dump statistics on [Python pymalloc memory allocator](https://docs.python.org/3/c-api/memory.html#pymalloc)
 at exit.

Set to `1` by the [`PYTHONMALLOCSTATS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONMALLOCSTATS)
 environment variable.

The option is ignored if Python is [`configured using the --without-pymalloc option`](https://docs.python.org/3/using/configure.html#cmdoption-without-pymalloc)
.

Default: `0`.

wchar\_t \*platlibdir[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.platlibdir "Link to this definition")
  

Platform library directory name: [`sys.platlibdir`](https://docs.python.org/3/library/sys.html#sys.platlibdir "sys.platlibdir")
.

Set by the [`PYTHONPLATLIBDIR`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPLATLIBDIR)
 environment variable.

Default: value of the `PLATLIBDIR` macro which is set by the [`configure --with-platlibdir option`](https://docs.python.org/3/using/configure.html#cmdoption-with-platlibdir)
 (default: `"lib"`, or `"DLLs"` on Windows).

Part of the [Python Path Configuration](https://docs.python.org/3/c-api/init_config.html#init-path-config)
 input.

Added in version 3.9.

Changed in version 3.11: This macro is now used on Windows to locate the standard library extension modules, typically under `DLLs`. However, for compatibility, note that this value is ignored for any non-standard layouts, including in-tree builds and virtual environments.

wchar\_t \*pythonpath\_env[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.pythonpath_env "Link to this definition")
  

Module search paths ([`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
) as a string separated by `DELIM` ([`os.pathsep`](https://docs.python.org/3/library/os.html#os.pathsep "os.pathsep")
).

Set by the [`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)
 environment variable.

Default: `NULL`.

Part of the [Python Path Configuration](https://docs.python.org/3/c-api/init_config.html#init-path-config)
 input.

[PyWideStringList](https://docs.python.org/3/c-api/init_config.html#c.PyWideStringList "PyWideStringList")
 module\_search\_paths[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.module_search_paths "Link to this definition")
  

int module\_search\_paths\_set[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.module_search_paths_set "Link to this definition")
  

Module search paths: [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
.

If [`module_search_paths_set`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.module_search_paths_set "PyConfig.module_search_paths_set")
 is equal to `0`, [`Py_InitializeFromConfig()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig "Py_InitializeFromConfig")
 will replace [`module_search_paths`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.module_search_paths "PyConfig.module_search_paths")
 and sets `module_search_paths_set` to `1`.

Default: empty list (`module_search_paths`) and `0` (`module_search_paths_set`).

Part of the [Python Path Configuration](https://docs.python.org/3/c-api/init_config.html#init-path-config)
 output.

int optimization\_level[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.optimization_level "Link to this definition")
  

Compilation optimization level:

*   `0`: Peephole optimizer, set `__debug__` to `True`.
    
*   `1`: Level 0, remove assertions, set `__debug__` to `False`.
    
*   `2`: Level 1, strip docstrings.
    

Incremented by the [`-O`](https://docs.python.org/3/using/cmdline.html#cmdoption-O)
 command line option. Set to the [`PYTHONOPTIMIZE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONOPTIMIZE)
 environment variable value.

Default: `0`.

[PyWideStringList](https://docs.python.org/3/c-api/init_config.html#c.PyWideStringList "PyWideStringList")
 orig\_argv[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.orig_argv "Link to this definition")
  

The list of the original command line arguments passed to the Python executable: [`sys.orig_argv`](https://docs.python.org/3/library/sys.html#sys.orig_argv "sys.orig_argv")
.

If [`orig_argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.orig_argv "PyConfig.orig_argv")
 list is empty and [`argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")
 is not a list only containing an empty string, [`PyConfig_Read()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Read "PyConfig_Read")
 copies `argv` into `orig_argv` before modifying `argv` (if [`parse_argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.parse_argv "PyConfig.parse_argv")
 is non-zero).

See also the [`argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")
 member and the [`Py_GetArgcArgv()`](https://docs.python.org/3/c-api/init_config.html#c.Py_GetArgcArgv "Py_GetArgcArgv")
 function.

Default: empty list.

Added in version 3.10.

int parse\_argv[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.parse_argv "Link to this definition")
  

Parse command line arguments?

If equals to `1`, parse [`argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")
 the same way the regular Python parses [command line arguments](https://docs.python.org/3/using/cmdline.html#using-on-cmdline)
, and strip Python arguments from `argv`.

The [`PyConfig_Read()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Read "PyConfig_Read")
 function only parses [`PyConfig.argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")
 arguments once: [`PyConfig.parse_argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.parse_argv "PyConfig.parse_argv")
 is set to `2` after arguments are parsed. Since Python arguments are stripped from `PyConfig.argv`, parsing arguments twice would parse the application options as Python options.

Default: `1` in Python mode, `0` in isolated mode.

Changed in version 3.10: The [`PyConfig.argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")
 arguments are now only parsed if [`PyConfig.parse_argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.parse_argv "PyConfig.parse_argv")
 equals to `1`.

int parser\_debug[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.parser_debug "Link to this definition")
  

Parser debug mode. If greater than `0`, turn on parser debugging output (for expert only, depending on compilation options).

Incremented by the [`-d`](https://docs.python.org/3/using/cmdline.html#cmdoption-d)
 command line option. Set to the [`PYTHONDEBUG`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDEBUG)
 environment variable value.

Needs a [debug build of Python](https://docs.python.org/3/using/configure.html#debug-build)
 (the `Py_DEBUG` macro must be defined).

Default: `0`.

int pathconfig\_warnings[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.pathconfig_warnings "Link to this definition")
  

If non-zero, calculation of path configuration is allowed to log warnings into `stderr`. If equals to `0`, suppress these warnings.

Default: `1` in Python mode, `0` in isolated mode.

Part of the [Python Path Configuration](https://docs.python.org/3/c-api/init_config.html#init-path-config)
 input.

Changed in version 3.11: Now also applies on Windows.

wchar\_t \*prefix[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.prefix "Link to this definition")
  

The site-specific directory prefix where the platform independent Python files are installed: [`sys.prefix`](https://docs.python.org/3/library/sys.html#sys.prefix "sys.prefix")
.

Default: `NULL`.

Part of the [Python Path Configuration](https://docs.python.org/3/c-api/init_config.html#init-path-config)
 output.

See also [`PyConfig.base_prefix`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.base_prefix "PyConfig.base_prefix")
.

wchar\_t \*program\_name[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.program_name "Link to this definition")
  

Program name used to initialize [`executable`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.executable "PyConfig.executable")
 and in early error messages during Python initialization.

*   On macOS, use [`PYTHONEXECUTABLE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONEXECUTABLE)
     environment variable if set.
    
*   If the `WITH_NEXT_FRAMEWORK` macro is defined, use `__PYVENV_LAUNCHER__` environment variable if set.
    
*   Use `argv[0]` of [`argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")
     if available and non-empty.
    
*   Otherwise, use `L"python"` on Windows, or `L"python3"` on other platforms.
    

Default: `NULL`.

Part of the [Python Path Configuration](https://docs.python.org/3/c-api/init_config.html#init-path-config)
 input.

wchar\_t \*pycache\_prefix[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.pycache_prefix "Link to this definition")
  

Directory where cached `.pyc` files are written: [`sys.pycache_prefix`](https://docs.python.org/3/library/sys.html#sys.pycache_prefix "sys.pycache_prefix")
.

Set by the [`-X pycache_prefix=PATH`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command line option and the [`PYTHONPYCACHEPREFIX`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPYCACHEPREFIX)
 environment variable. The command-line option takes precedence.

If `NULL`, [`sys.pycache_prefix`](https://docs.python.org/3/library/sys.html#sys.pycache_prefix "sys.pycache_prefix")
 is set to `None`.

Default: `NULL`.

int quiet[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.quiet "Link to this definition")
  

Quiet mode. If greater than `0`, don’t display the copyright and version at Python startup in interactive mode.

Incremented by the [`-q`](https://docs.python.org/3/using/cmdline.html#cmdoption-q)
 command line option.

Default: `0`.

wchar\_t \*run\_command[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.run_command "Link to this definition")
  

Value of the [`-c`](https://docs.python.org/3/using/cmdline.html#cmdoption-c)
 command line option.

Used by [`Py_RunMain()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_RunMain "Py_RunMain")
.

Default: `NULL`.

wchar\_t \*run\_filename[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.run_filename "Link to this definition")
  

Filename passed on the command line: trailing command line argument without [`-c`](https://docs.python.org/3/using/cmdline.html#cmdoption-c)
 or [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m)
. It is used by the [`Py_RunMain()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_RunMain "Py_RunMain")
 function.

For example, it is set to `script.py` by the `python3 script.py arg` command line.

See also the [`PyConfig.skip_source_first_line`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.skip_source_first_line "PyConfig.skip_source_first_line")
 option.

Default: `NULL`.

wchar\_t \*run\_module[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.run_module "Link to this definition")
  

Value of the [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m)
 command line option.

Used by [`Py_RunMain()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_RunMain "Py_RunMain")
.

Default: `NULL`.

wchar\_t \*run\_presite[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.run_presite "Link to this definition")
  

`module` or `module:func` entry point that should be executed before the [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.")
 module is imported.

Set by the [`-X presite=module:func`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command-line option and the [`PYTHON_PRESITE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_PRESITE)
 environment variable. The command-line option takes precedence.

Needs a [debug build of Python](https://docs.python.org/3/using/configure.html#debug-build)
 (the `Py_DEBUG` macro must be defined).

Default: `NULL`.

int show\_ref\_count[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.show_ref_count "Link to this definition")
  

Show total reference count at exit (excluding [immortal](https://docs.python.org/3/glossary.html#term-immortal)
 objects)?

Set to `1` by [`-X showrefcount`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command line option.

Needs a [debug build of Python](https://docs.python.org/3/using/configure.html#debug-build)
 (the `Py_REF_DEBUG` macro must be defined).

Default: `0`.

int site\_import[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.site_import "Link to this definition")
  

Import the [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.")
 module at startup?

If equal to zero, disable the import of the module site and the site-dependent manipulations of [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
 that it entails.

Also disable these manipulations if the [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.")
 module is explicitly imported later (call [`site.main()`](https://docs.python.org/3/library/site.html#site.main "site.main")
 if you want them to be triggered).

Set to `0` by the [`-S`](https://docs.python.org/3/using/cmdline.html#cmdoption-S)
 command line option.

[`sys.flags.no_site`](https://docs.python.org/3/library/sys.html#sys.flags "sys.flags")
 is set to the inverted value of [`site_import`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.site_import "PyConfig.site_import")
.

Default: `1`.

int skip\_source\_first\_line[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.skip_source_first_line "Link to this definition")
  

If non-zero, skip the first line of the [`PyConfig.run_filename`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.run_filename "PyConfig.run_filename")
 source.

It allows the usage of non-Unix forms of `#!cmd`. This is intended for a DOS specific hack only.

Set to `1` by the [`-x`](https://docs.python.org/3/using/cmdline.html#cmdoption-x)
 command line option.

Default: `0`.

wchar\_t \*stdio\_encoding[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.stdio_encoding "Link to this definition")
  

wchar\_t \*stdio\_errors[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.stdio_errors "Link to this definition")
  

Encoding and encoding errors of [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin")
, [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
 and [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr")
 (but `sys.stderr` always uses `"backslashreplace"` error handler).

Use the [`PYTHONIOENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONIOENCODING)
 environment variable if it is non-empty.

Default encoding:

*   `"UTF-8"` if [`PyPreConfig.utf8_mode`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.utf8_mode "PyPreConfig.utf8_mode")
     is non-zero.
    
*   Otherwise, use the [locale encoding](https://docs.python.org/3/glossary.html#term-locale-encoding)
    .
    

Default error handler:

*   On Windows: use `"surrogateescape"`.
    
*   `"surrogateescape"` if [`PyPreConfig.utf8_mode`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.utf8_mode "PyPreConfig.utf8_mode")
     is non-zero, or if the LC\_CTYPE locale is “C” or “POSIX”.
    
*   `"strict"` otherwise.
    

See also [`PyConfig.legacy_windows_stdio`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.legacy_windows_stdio "PyConfig.legacy_windows_stdio")
.

int tracemalloc[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.tracemalloc "Link to this definition")
  

Enable tracemalloc?

If non-zero, call [`tracemalloc.start()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.start "tracemalloc.start")
 at startup.

Set by [`-X tracemalloc=N`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command line option and by the [`PYTHONTRACEMALLOC`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONTRACEMALLOC)
 environment variable.

Default: `-1` in Python mode, `0` in isolated mode.

int perf\_profiling[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.perf_profiling "Link to this definition")
  

Enable the Linux `perf` profiler support?

If equals to `1`, enable support for the Linux `perf` profiler.

If equals to `2`, enable support for the Linux `perf` profiler with DWARF JIT support.

Set to `1` by [`-X perf`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command-line option and the [`PYTHONPERFSUPPORT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPERFSUPPORT)
 environment variable.

Set to `2` by the [`-X perf_jit`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command-line option and the [`PYTHON_PERF_JIT_SUPPORT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_PERF_JIT_SUPPORT)
 environment variable.

Default: `-1`.

See also

See [Python support for the perf map compatible profilers](https://docs.python.org/3/howto/perf_profiling.html#perf-profiling)
 for more information.

Added in version 3.12.

wchar\_t \*stdlib\_dir[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.stdlib_dir "Link to this definition")
  

Directory of the Python standard library.

Default: `NULL`.

Added in version 3.11.

int use\_environment[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.use_environment "Link to this definition")
  

Use [environment variables](https://docs.python.org/3/using/cmdline.html#using-on-envvars)
?

If equals to zero, ignore the [environment variables](https://docs.python.org/3/using/cmdline.html#using-on-envvars)
.

Set to `0` by the [`-E`](https://docs.python.org/3/using/cmdline.html#cmdoption-E)
 command-line option.

Default: `1` in Python config and `0` in isolated config.

int use\_system\_logger[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.use_system_logger "Link to this definition")
  

If non-zero, `stdout` and `stderr` will be redirected to the system log.

Only available on macOS 10.12 and later, and on iOS.

Default: `0` (don’t use the system log) on macOS; `1` on iOS (use the system log).

Added in version 3.14.

int user\_site\_directory[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.user_site_directory "Link to this definition")
  

If non-zero, add the user site directory to [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
.

Set to `0` by the [`-s`](https://docs.python.org/3/using/cmdline.html#cmdoption-s)
 and [`-I`](https://docs.python.org/3/using/cmdline.html#cmdoption-I)
 command line options.

Set to `0` by the [`PYTHONNOUSERSITE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONNOUSERSITE)
 environment variable.

Default: `1` in Python mode, `0` in isolated mode.

int verbose[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.verbose "Link to this definition")
  

Verbose mode. If greater than `0`, print a message each time a module is imported, showing the place (filename or built-in module) from which it is loaded.

If greater than or equal to `2`, print a message for each file that is checked for when searching for a module. Also provides information on module cleanup at exit.

Incremented by the [`-v`](https://docs.python.org/3/using/cmdline.html#cmdoption-v)
 command line option.

Set by the [`PYTHONVERBOSE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONVERBOSE)
 environment variable value.

Default: `0`.

[PyWideStringList](https://docs.python.org/3/c-api/init_config.html#c.PyWideStringList "PyWideStringList")
 warnoptions[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.warnoptions "Link to this definition")
  

Options of the [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "warnings: Issue warning messages and control their disposition.")
 module to build warnings filters, lowest to highest priority: [`sys.warnoptions`](https://docs.python.org/3/library/sys.html#sys.warnoptions "sys.warnoptions")
.

The [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "warnings: Issue warning messages and control their disposition.")
 module adds [`sys.warnoptions`](https://docs.python.org/3/library/sys.html#sys.warnoptions "sys.warnoptions")
 in the reverse order: the last [`PyConfig.warnoptions`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.warnoptions "PyConfig.warnoptions")
 item becomes the first item of `warnings.filters` which is checked first (highest priority).

The [`-W`](https://docs.python.org/3/using/cmdline.html#cmdoption-W)
 command line options adds its value to [`warnoptions`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.warnoptions "PyConfig.warnoptions")
, it can be used multiple times.

The [`PYTHONWARNINGS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONWARNINGS)
 environment variable can also be used to add warning options. Multiple options can be specified, separated by commas (`,`).

Default: empty list.

int write\_bytecode[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.write_bytecode "Link to this definition")
  

If equal to `0`, Python won’t try to write `.pyc` files on the import of source modules.

Set to `0` by the [`-B`](https://docs.python.org/3/using/cmdline.html#cmdoption-B)
 command line option and the [`PYTHONDONTWRITEBYTECODE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE)
 environment variable.

[`sys.dont_write_bytecode`](https://docs.python.org/3/library/sys.html#sys.dont_write_bytecode "sys.dont_write_bytecode")
 is initialized to the inverted value of [`write_bytecode`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.write_bytecode "PyConfig.write_bytecode")
.

Default: `1`.

[PyWideStringList](https://docs.python.org/3/c-api/init_config.html#c.PyWideStringList "PyWideStringList")
 xoptions[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.xoptions "Link to this definition")
  

Values of the [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command line options: [`sys._xoptions`](https://docs.python.org/3/library/sys.html#sys._xoptions "sys._xoptions")
.

Default: empty list.

int \_pystats[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig._pystats "Link to this definition")
  

If non-zero, write performance statistics at Python exit.

Need a special build with the `Py_STATS` macro: see [`--enable-pystats`](https://docs.python.org/3/using/configure.html#cmdoption-enable-pystats)
.

Default: `0`.

If [`parse_argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.parse_argv "PyConfig.parse_argv")
 is non-zero, [`argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")
 arguments are parsed the same way the regular Python parses [command line arguments](https://docs.python.org/3/using/cmdline.html#using-on-cmdline)
, and Python arguments are stripped from `argv`.

The [`xoptions`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.xoptions "PyConfig.xoptions")
 options are parsed to set other options: see the [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command line option.

Changed in version 3.9: The `show_alloc_count` field has been removed.

### Initialization with PyConfig[¶](https://docs.python.org/3/c-api/init_config.html#initialization-with-pyconfig "Link to this heading")

Initializing the interpreter from a populated configuration struct is handled by calling [`Py_InitializeFromConfig()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig "Py_InitializeFromConfig")
.

The caller is responsible to handle exceptions (error or exit) using [`PyStatus_Exception()`](https://docs.python.org/3/c-api/init_config.html#c.PyStatus_Exception "PyStatus_Exception")
 and [`Py_ExitStatusException()`](https://docs.python.org/3/c-api/init_config.html#c.Py_ExitStatusException "Py_ExitStatusException")
.

If [`PyImport_FrozenModules()`](https://docs.python.org/3/c-api/import.html#c.PyImport_FrozenModules "PyImport_FrozenModules")
, [`PyImport_AppendInittab()`](https://docs.python.org/3/c-api/import.html#c.PyImport_AppendInittab "PyImport_AppendInittab")
 or [`PyImport_ExtendInittab()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ExtendInittab "PyImport_ExtendInittab")
 are used, they must be set or called after Python preinitialization and before the Python initialization. If Python is initialized multiple times, `PyImport_AppendInittab()` or `PyImport_ExtendInittab()` must be called before each Python initialization.

The current configuration (`PyConfig` type) is stored in `PyInterpreterState.config`.

Example setting the program name:

void init\_python(void)
{
    PyStatus status;

    PyConfig config;
    PyConfig\_InitPythonConfig(&config);

    /\* Set the program name. Implicitly preinitialize Python. \*/
    status \= PyConfig\_SetString(&config, &config.program\_name,
                                L"/path/to/my\_program");
    if (PyStatus\_Exception(status)) {
        goto exception;
    }

    status \= Py\_InitializeFromConfig(&config);
    if (PyStatus\_Exception(status)) {
        goto exception;
    }
    PyConfig\_Clear(&config);
    return;

exception:
    PyConfig\_Clear(&config);
    Py\_ExitStatusException(status);
}

More complete example modifying the default configuration, read the configuration, and then override some parameters. Note that since 3.11, many parameters are not calculated until initialization, and so values cannot be read from the configuration structure. Any values set before initialize is called will be left unchanged by initialization:

PyStatus init\_python(const char \*program\_name)
{
    PyStatus status;

    PyConfig config;
    PyConfig\_InitPythonConfig(&config);

    /\* Set the program name before reading the configuration
       (decode byte string from the locale encoding).

       Implicitly preinitialize Python. \*/
    status \= PyConfig\_SetBytesString(&config, &config.program\_name,
                                     program\_name);
    if (PyStatus\_Exception(status)) {
        goto done;
    }

    /\* Read all configuration at once \*/
    status \= PyConfig\_Read(&config);
    if (PyStatus\_Exception(status)) {
        goto done;
    }

    /\* Specify sys.path explicitly \*/
    /\* If you want to modify the default set of paths, finish
       initialization first and then use PySys\_GetAttrString("path") \*/
    config.module\_search\_paths\_set \= 1;
    status \= PyWideStringList\_Append(&config.module\_search\_paths,
                                     L"/path/to/stdlib");
    if (PyStatus\_Exception(status)) {
        goto done;
    }
    status \= PyWideStringList\_Append(&config.module\_search\_paths,
                                     L"/path/to/more/modules");
    if (PyStatus\_Exception(status)) {
        goto done;
    }

    /\* Override executable computed by PyConfig\_Read() \*/
    status \= PyConfig\_SetString(&config, &config.executable,
                                L"/path/to/my\_executable");
    if (PyStatus\_Exception(status)) {
        goto done;
    }

    status \= Py\_InitializeFromConfig(&config);

done:
    PyConfig\_Clear(&config);
    return status;
}

### Isolated Configuration[¶](https://docs.python.org/3/c-api/init_config.html#isolated-configuration "Link to this heading")

[`PyPreConfig_InitIsolatedConfig()`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig_InitIsolatedConfig "PyPreConfig_InitIsolatedConfig")
 and [`PyConfig_InitIsolatedConfig()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_InitIsolatedConfig "PyConfig_InitIsolatedConfig")
 functions create a configuration to isolate Python from the system. For example, to embed Python into an application.

This configuration ignores global configuration variables, environment variables, command line arguments ([`PyConfig.argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")
 is not parsed) and user site directory. The C standard streams (ex: `stdout`) and the LC\_CTYPE locale are left unchanged. Signal handlers are not installed.

Configuration files are still used with this configuration to determine paths that are unspecified. Ensure [`PyConfig.home`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.home "PyConfig.home")
 is specified to avoid computing the default path configuration.

### Python Configuration[¶](https://docs.python.org/3/c-api/init_config.html#python-configuration "Link to this heading")

[`PyPreConfig_InitPythonConfig()`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig_InitPythonConfig "PyPreConfig_InitPythonConfig")
 and [`PyConfig_InitPythonConfig()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_InitPythonConfig "PyConfig_InitPythonConfig")
 functions create a configuration to build a customized Python which behaves as the regular Python.

Environments variables and command line arguments are used to configure Python, whereas global configuration variables are ignored.

This function enables C locale coercion ([**PEP 538**](https://peps.python.org/pep-0538/)
) and [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode)
 ([**PEP 540**](https://peps.python.org/pep-0540/)
) depending on the LC\_CTYPE locale, [`PYTHONUTF8`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUTF8)
 and [`PYTHONCOERCECLOCALE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONCOERCECLOCALE)
 environment variables.

### Python Path Configuration[¶](https://docs.python.org/3/c-api/init_config.html#python-path-configuration "Link to this heading")

[`PyConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
 contains multiple fields for the path configuration:

*   Path configuration inputs:
    
    *   [`PyConfig.home`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.home "PyConfig.home")
        
    *   [`PyConfig.platlibdir`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.platlibdir "PyConfig.platlibdir")
        
    *   [`PyConfig.pathconfig_warnings`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.pathconfig_warnings "PyConfig.pathconfig_warnings")
        
    *   [`PyConfig.program_name`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.program_name "PyConfig.program_name")
        
    *   [`PyConfig.pythonpath_env`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.pythonpath_env "PyConfig.pythonpath_env")
        
    *   current working directory: to get absolute paths
        
    *   `PATH` environment variable to get the program full path (from [`PyConfig.program_name`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.program_name "PyConfig.program_name")
        )
        
    *   `__PYVENV_LAUNCHER__` environment variable
        
    *   (Windows only) Application paths in the registry under “SoftwarePythonPythonCoreX.YPythonPath” of HKEY\_CURRENT\_USER and HKEY\_LOCAL\_MACHINE (where X.Y is the Python version).
        
*   Path configuration output fields:
    
    *   [`PyConfig.base_exec_prefix`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.base_exec_prefix "PyConfig.base_exec_prefix")
        
    *   [`PyConfig.base_executable`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.base_executable "PyConfig.base_executable")
        
    *   [`PyConfig.base_prefix`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.base_prefix "PyConfig.base_prefix")
        
    *   [`PyConfig.exec_prefix`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.exec_prefix "PyConfig.exec_prefix")
        
    *   [`PyConfig.executable`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.executable "PyConfig.executable")
        
    *   [`PyConfig.module_search_paths_set`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.module_search_paths_set "PyConfig.module_search_paths_set")
        , [`PyConfig.module_search_paths`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.module_search_paths "PyConfig.module_search_paths")
        
    *   [`PyConfig.prefix`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.prefix "PyConfig.prefix")
        

If at least one “output field” is not set, Python calculates the path configuration to fill unset fields. If [`module_search_paths_set`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.module_search_paths_set "PyConfig.module_search_paths_set")
 is equal to `0`, [`module_search_paths`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.module_search_paths "PyConfig.module_search_paths")
 is overridden and `module_search_paths_set` is set to `1`.

It is possible to completely ignore the function calculating the default path configuration by setting explicitly all path configuration output fields listed above. A string is considered as set even if it is non-empty. `module_search_paths` is considered as set if `module_search_paths_set` is set to `1`. In this case, `module_search_paths` will be used without modification.

Set [`pathconfig_warnings`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.pathconfig_warnings "PyConfig.pathconfig_warnings")
 to `0` to suppress warnings when calculating the path configuration (Unix only, Windows does not log any warning).

If [`base_prefix`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.base_prefix "PyConfig.base_prefix")
 or [`base_exec_prefix`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.base_exec_prefix "PyConfig.base_exec_prefix")
 fields are not set, they inherit their value from [`prefix`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.prefix "PyConfig.prefix")
 and [`exec_prefix`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.exec_prefix "PyConfig.exec_prefix")
 respectively.

[`Py_RunMain()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_RunMain "Py_RunMain")
 and [`Py_Main()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_Main "Py_Main")
 modify [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
:

*   If [`run_filename`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.run_filename "PyConfig.run_filename")
     is set and is a directory which contains a `__main__.py` script, prepend `run_filename` to [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
    .
    
*   If [`isolated`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.isolated "PyConfig.isolated")
     is zero:
    
    *   If [`run_module`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.run_module "PyConfig.run_module")
         is set, prepend the current directory to [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
        . Do nothing if the current directory cannot be read.
        
    *   If [`run_filename`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.run_filename "PyConfig.run_filename")
         is set, prepend the directory of the filename to [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
        .
        
    *   Otherwise, prepend an empty string to [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
        .
        

If [`site_import`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.site_import "PyConfig.site_import")
 is non-zero, [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
 can be modified by the [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.")
 module. If [`user_site_directory`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.user_site_directory "PyConfig.user_site_directory")
 is non-zero and the user’s site-package directory exists, the `site` module appends the user’s site-package directory to `sys.path`.

The following configuration files are used by the path configuration:

*   `pyvenv.cfg`
    
*   `._pth` file (ex: `python._pth`)
    
*   `pybuilddir.txt` (Unix only)
    

If a `._pth` file is present:

*   Set [`isolated`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.isolated "PyConfig.isolated")
     to `1`.
    
*   Set [`use_environment`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.use_environment "PyConfig.use_environment")
     to `0`.
    
*   Set [`site_import`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.site_import "PyConfig.site_import")
     to `0`.
    
*   Set [`user_site_directory`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.user_site_directory "PyConfig.user_site_directory")
     to `0` (since 3.15).
    
*   Set [`safe_path`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.safe_path "PyConfig.safe_path")
     to `1`.
    

If [`home`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.home "PyConfig.home")
 is not set and a `pyvenv.cfg` file is present in the same directory as [`executable`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.executable "PyConfig.executable")
, or its parent, [`prefix`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.prefix "PyConfig.prefix")
 and [`exec_prefix`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.exec_prefix "PyConfig.exec_prefix")
 are set that location. When this happens, [`base_prefix`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.base_prefix "PyConfig.base_prefix")
 and [`base_exec_prefix`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.base_exec_prefix "PyConfig.base_exec_prefix")
 still keep their value, pointing to the base installation. See [Virtual Environments](https://docs.python.org/3/library/sys_path_init.html#sys-path-init-virtual-environments)
 for more information.

The `__PYVENV_LAUNCHER__` environment variable is used to set [`PyConfig.base_executable`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.base_executable "PyConfig.base_executable")
.

Changed in version 3.14: [`prefix`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.prefix "PyConfig.prefix")
, and [`exec_prefix`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.exec_prefix "PyConfig.exec_prefix")
, are now set to the `pyvenv.cfg` directory. This was previously done by [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.")
, therefore affected by [`-S`](https://docs.python.org/3/using/cmdline.html#cmdoption-S)
.

Changed in version 3.15: [`user_site_directory`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.user_site_directory "PyConfig.user_site_directory")
 is now set to `0` when a `._pth` file is present.

Py\_GetArgcArgv()[¶](https://docs.python.org/3/c-api/init_config.html#py-getargcargv "Link to this heading")

-------------------------------------------------------------------------------------------------------------

void Py\_GetArgcArgv(int \*argc, wchar\_t \*\*\*argv)[¶](https://docs.python.org/3/c-api/init_config.html#c.Py_GetArgcArgv "Link to this definition")
  

Get the original command line arguments, before Python modified them.

See also [`PyConfig.orig_argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.orig_argv "PyConfig.orig_argv")
 member.

Multi-Phase Initialization Private Provisional API[¶](https://docs.python.org/3/c-api/init_config.html#multi-phase-initialization-private-provisional-api "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This section is a private provisional API introducing multi-phase initialization, the core feature of [**PEP 432**](https://peps.python.org/pep-0432/)
:

*   “Core” initialization phase, “bare minimum Python”:
    
    *   Builtin types;
        
    *   Builtin exceptions;
        
    *   Builtin and frozen modules;
        
    *   The [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.")
         module is only partially initialized (ex: [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
         doesn’t exist yet).
        
*   “Main” initialization phase, Python is fully initialized:
    
    *   Install and configure [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
        ;
        
    *   Apply the [Path Configuration](https://docs.python.org/3/c-api/init_config.html#init-path-config)
        ;
        
    *   Install signal handlers;
        
    *   Finish [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.")
         module initialization (ex: create [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
         and [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
        );
        
    *   Enable optional features like [`faulthandler`](https://docs.python.org/3/library/faulthandler.html#module-faulthandler "faulthandler: Dump the Python traceback.")
         and [`tracemalloc`](https://docs.python.org/3/library/tracemalloc.html#module-tracemalloc "tracemalloc: Trace memory allocations.")
        ;
        
    *   Import the [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.")
         module;
        
    *   etc.
        

Private provisional API:

int [PyConfig](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
.\_init\_main[¶](https://docs.python.org/3/c-api/init_config.html#c.PyConfig._init_main "Link to this definition")
  

If set to `0`, [`Py_InitializeFromConfig()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig "Py_InitializeFromConfig")
 stops at the “Core” initialization phase.

[PyStatus](https://docs.python.org/3/c-api/init_config.html#c.PyStatus "PyStatus")
 \_Py\_InitializeMain(void)[¶](https://docs.python.org/3/c-api/init_config.html#c._Py_InitializeMain "Link to this definition")
  

Move to the “Main” initialization phase, finish the Python initialization.

No module is imported during the “Core” phase and the `importlib` module is not configured: the [Path Configuration](https://docs.python.org/3/c-api/init_config.html#init-path-config)
 is only applied during the “Main” phase. It may allow to customize Python in Python to override or tune the [Path Configuration](https://docs.python.org/3/c-api/init_config.html#init-path-config)
, maybe install a custom [`sys.meta_path`](https://docs.python.org/3/library/sys.html#sys.meta_path "sys.meta_path")
 importer or an import hook, etc.

It may become possible to calculate the [Path Configuration](https://docs.python.org/3/c-api/init_config.html#init-path-config)
 in Python, after the Core phase and before the Main phase, which is one of the [**PEP 432**](https://peps.python.org/pep-0432/)
 motivation.

The “Core” phase is not properly defined: what should be and what should not be available at this phase is not specified yet. The API is marked as private and provisional: the API can be modified or even be removed anytime until a proper public API is designed.

Example running Python code between “Core” and “Main” initialization phases:

void init\_python(void)
{
    PyStatus status;

    PyConfig config;
    PyConfig\_InitPythonConfig(&config);
    config.\_init\_main \= 0;

    /\* ... customize 'config' configuration ... \*/

    status \= Py\_InitializeFromConfig(&config);
    PyConfig\_Clear(&config);
    if (PyStatus\_Exception(status)) {
        Py\_ExitStatusException(status);
    }

    /\* Use sys.stderr because sys.stdout is only created
       by \_Py\_InitializeMain() \*/
    int res \= PyRun\_SimpleString(
        "import sys; "
        "print('Run Python code before \_Py\_InitializeMain', "
               "file=sys.stderr)");
    if (res < 0) {
        exit(1);
    }

    /\* ... put more configuration code here ... \*/

    status \= \_Py\_InitializeMain();
    if (PyStatus\_Exception(status)) {
        Py\_ExitStatusException(status);
    }
}

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Python Initialization Configuration](https://docs.python.org/3/c-api/init_config.html#)
    *   [PyInitConfig C API](https://docs.python.org/3/c-api/init_config.html#pyinitconfig-c-api)
        *   [Example](https://docs.python.org/3/c-api/init_config.html#example)
            
        *   [Create Config](https://docs.python.org/3/c-api/init_config.html#create-config)
            
        *   [Error Handling](https://docs.python.org/3/c-api/init_config.html#error-handling)
            
        *   [Get Options](https://docs.python.org/3/c-api/init_config.html#get-options)
            
        *   [Set Options](https://docs.python.org/3/c-api/init_config.html#set-options)
            
        *   [Module](https://docs.python.org/3/c-api/init_config.html#module)
            
        *   [Initialize Python](https://docs.python.org/3/c-api/init_config.html#initialize-python)
            
    *   [Configuration Options](https://docs.python.org/3/c-api/init_config.html#configuration-options)
        
    *   [Runtime Python configuration API](https://docs.python.org/3/c-api/init_config.html#runtime-python-configuration-api)
        
    *   [PyConfig C API](https://docs.python.org/3/c-api/init_config.html#pyconfig-c-api)
        *   [Example](https://docs.python.org/3/c-api/init_config.html#id1)
            
        *   [PyWideStringList](https://docs.python.org/3/c-api/init_config.html#pywidestringlist)
            
        *   [PyStatus](https://docs.python.org/3/c-api/init_config.html#pystatus)
            
        *   [PyPreConfig](https://docs.python.org/3/c-api/init_config.html#pypreconfig)
            
        *   [Preinitialize Python with PyPreConfig](https://docs.python.org/3/c-api/init_config.html#preinitialize-python-with-pypreconfig)
            
        *   [PyConfig](https://docs.python.org/3/c-api/init_config.html#pyconfig)
            
        *   [Initialization with PyConfig](https://docs.python.org/3/c-api/init_config.html#initialization-with-pyconfig)
            
        *   [Isolated Configuration](https://docs.python.org/3/c-api/init_config.html#isolated-configuration)
            
        *   [Python Configuration](https://docs.python.org/3/c-api/init_config.html#python-configuration)
            
        *   [Python Path Configuration](https://docs.python.org/3/c-api/init_config.html#python-path-configuration)
            
    *   [Py\_GetArgcArgv()](https://docs.python.org/3/c-api/init_config.html#py-getargcargv)
        
    *   [Multi-Phase Initialization Private Provisional API](https://docs.python.org/3/c-api/init_config.html#multi-phase-initialization-private-provisional-api)
        

#### Previous topic

[Profiling and tracing](https://docs.python.org/3/c-api/profiling.html "previous chapter")

#### Next topic

[Memory Management](https://docs.python.org/3/c-api/memory.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Python+Initialization+Configuration&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Finit_config.html&pagesource=c-api%2Finit_config.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/init_config.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/memory.html "Memory Management")
     |
*   [previous](https://docs.python.org/3/c-api/profiling.html "Profiling and tracing")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [Python Initialization Configuration](https://docs.python.org/3/c-api/init_config.html)
    
*    
    
    |
*   Theme Auto Light Dark |