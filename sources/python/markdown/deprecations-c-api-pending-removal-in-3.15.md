### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Pending removal in Python 3.15](https://docs.python.org/3/deprecations/c-api-pending-removal-in-3.15.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Pending removal in Python 3.15[¶](https://docs.python.org/3/deprecations/c-api-pending-removal-in-3.15.html#pending-removal-in-python-3-15 "Link to this heading")

===================================================================================================================================================================

*   The `PyImport_ImportModuleNoBlock()`: Use [`PyImport_ImportModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModule "PyImport_ImportModule")
     instead.
    
*   `PyWeakref_GetObject()` and `PyWeakref_GET_OBJECT()`: Use [`PyWeakref_GetRef()`](https://docs.python.org/3/c-api/weakref.html#c.PyWeakref_GetRef "PyWeakref_GetRef")
     instead. The [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)
     can be used to get `PyWeakref_GetRef()` on Python 3.12 and older.
    
*   `PyUnicode_AsDecodedObject()`: Use [`PyCodec_Decode()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Decode "PyCodec_Decode")
     instead.
    
*   `PyUnicode_AsDecodedUnicode()`: Use [`PyCodec_Decode()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Decode "PyCodec_Decode")
     instead; Note that some codecs (for example, “base64”) may return a type other than [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    , such as [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
    .
    
*   `PyUnicode_AsEncodedObject()`: Use [`PyCodec_Encode()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Encode "PyCodec_Encode")
     instead.
    
*   `PyUnicode_AsEncodedUnicode()`: Use [`PyCodec_Encode()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Encode "PyCodec_Encode")
     instead; Note that some codecs (for example, “base64”) may return a type other than [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
    , such as [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    .
    
*   Python initialization functions, deprecated in Python 3.13:
    
    *   `Py_GetPath()`: Use [`PyConfig_Get("module_search_paths")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         ([`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
        ) instead.
        
    *   `Py_GetPrefix()`: Use [`PyConfig_Get("base_prefix")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         ([`sys.base_prefix`](https://docs.python.org/3/library/sys.html#sys.base_prefix "sys.base_prefix")
        ) instead. Use `PyConfig_Get("prefix")` ([`sys.prefix`](https://docs.python.org/3/library/sys.html#sys.prefix "sys.prefix")
        ) if [virtual environments](https://docs.python.org/3/library/venv.html#venv-def)
         need to be handled.
        
    *   `Py_GetExecPrefix()`: Use [`PyConfig_Get("base_exec_prefix")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         ([`sys.base_exec_prefix`](https://docs.python.org/3/library/sys.html#sys.base_exec_prefix "sys.base_exec_prefix")
        ) instead. Use `PyConfig_Get("exec_prefix")` ([`sys.exec_prefix`](https://docs.python.org/3/library/sys.html#sys.exec_prefix "sys.exec_prefix")
        ) if [virtual environments](https://docs.python.org/3/library/venv.html#venv-def)
         need to be handled.
        
    *   `Py_GetProgramFullPath()`: Use [`PyConfig_Get("executable")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         ([`sys.executable`](https://docs.python.org/3/library/sys.html#sys.executable "sys.executable")
        ) instead.
        
    *   `Py_GetProgramName()`: Use [`PyConfig_Get("executable")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         ([`sys.executable`](https://docs.python.org/3/library/sys.html#sys.executable "sys.executable")
        ) instead.
        
    *   `Py_GetPythonHome()`: Use [`PyConfig_Get("home")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         or the [`PYTHONHOME`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHOME)
         environment variable instead.
        
    
    The [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)
     can be used to get [`PyConfig_Get()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
     on Python 3.13 and older.
    
*   Functions to configure Python’s initialization, deprecated in Python 3.11:
    
    *   `PySys_SetArgvEx()`: Set [`PyConfig.argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")
         instead.
        
    *   `PySys_SetArgv()`: Set [`PyConfig.argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")
         instead.
        
    *   `Py_SetProgramName()`: Set [`PyConfig.program_name`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.program_name "PyConfig.program_name")
         instead.
        
    *   `Py_SetPythonHome()`: Set [`PyConfig.home`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.home "PyConfig.home")
         instead.
        
    *   `PySys_ResetWarnOptions()`: Clear [`sys.warnoptions`](https://docs.python.org/3/library/sys.html#sys.warnoptions "sys.warnoptions")
         and `warnings.filters` instead.
        
    
    The [`Py_InitializeFromConfig()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig "Py_InitializeFromConfig")
     API should be used with [`PyConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
     instead.
    
*   Global configuration variables:
    
    *   [`Py_DebugFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_DebugFlag "Py_DebugFlag")
        : Use [`PyConfig.parser_debug`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.parser_debug "PyConfig.parser_debug")
         or [`PyConfig_Get("parser_debug")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_VerboseFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_VerboseFlag "Py_VerboseFlag")
        : Use [`PyConfig.verbose`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.verbose "PyConfig.verbose")
         or [`PyConfig_Get("verbose")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_QuietFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_QuietFlag "Py_QuietFlag")
        : Use [`PyConfig.quiet`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.quiet "PyConfig.quiet")
         or [`PyConfig_Get("quiet")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_InteractiveFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InteractiveFlag "Py_InteractiveFlag")
        : Use [`PyConfig.interactive`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.interactive "PyConfig.interactive")
         or [`PyConfig_Get("interactive")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_InspectFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InspectFlag "Py_InspectFlag")
        : Use [`PyConfig.inspect`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.inspect "PyConfig.inspect")
         or [`PyConfig_Get("inspect")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_OptimizeFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_OptimizeFlag "Py_OptimizeFlag")
        : Use [`PyConfig.optimization_level`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.optimization_level "PyConfig.optimization_level")
         or [`PyConfig_Get("optimization_level")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_NoSiteFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_NoSiteFlag "Py_NoSiteFlag")
        : Use [`PyConfig.site_import`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.site_import "PyConfig.site_import")
         or [`PyConfig_Get("site_import")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_BytesWarningFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_BytesWarningFlag "Py_BytesWarningFlag")
        : Use [`PyConfig.bytes_warning`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.bytes_warning "PyConfig.bytes_warning")
         or [`PyConfig_Get("bytes_warning")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_FrozenFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_FrozenFlag "Py_FrozenFlag")
        : Use [`PyConfig.pathconfig_warnings`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.pathconfig_warnings "PyConfig.pathconfig_warnings")
         or [`PyConfig_Get("pathconfig_warnings")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_IgnoreEnvironmentFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_IgnoreEnvironmentFlag "Py_IgnoreEnvironmentFlag")
        : Use [`PyConfig.use_environment`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.use_environment "PyConfig.use_environment")
         or [`PyConfig_Get("use_environment")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_DontWriteBytecodeFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_DontWriteBytecodeFlag "Py_DontWriteBytecodeFlag")
        : Use [`PyConfig.write_bytecode`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.write_bytecode "PyConfig.write_bytecode")
         or [`PyConfig_Get("write_bytecode")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_NoUserSiteDirectory`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_NoUserSiteDirectory "Py_NoUserSiteDirectory")
        : Use [`PyConfig.user_site_directory`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.user_site_directory "PyConfig.user_site_directory")
         or [`PyConfig_Get("user_site_directory")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_UnbufferedStdioFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_UnbufferedStdioFlag "Py_UnbufferedStdioFlag")
        : Use [`PyConfig.buffered_stdio`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.buffered_stdio "PyConfig.buffered_stdio")
         or [`PyConfig_Get("buffered_stdio")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_HashRandomizationFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_HashRandomizationFlag "Py_HashRandomizationFlag")
        : Use [`PyConfig.use_hash_seed`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.use_hash_seed "PyConfig.use_hash_seed")
         and [`PyConfig.hash_seed`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.hash_seed "PyConfig.hash_seed")
         or [`PyConfig_Get("hash_seed")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_IsolatedFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_IsolatedFlag "Py_IsolatedFlag")
        : Use [`PyConfig.isolated`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.isolated "PyConfig.isolated")
         or [`PyConfig_Get("isolated")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_LegacyWindowsFSEncodingFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_LegacyWindowsFSEncodingFlag "Py_LegacyWindowsFSEncodingFlag")
        : Use [`PyPreConfig.legacy_windows_fs_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.legacy_windows_fs_encoding "PyPreConfig.legacy_windows_fs_encoding")
         or [`PyConfig_Get("legacy_windows_fs_encoding")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_LegacyWindowsStdioFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_LegacyWindowsStdioFlag "Py_LegacyWindowsStdioFlag")
        : Use [`PyConfig.legacy_windows_stdio`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.legacy_windows_stdio "PyConfig.legacy_windows_stdio")
         or [`PyConfig_Get("legacy_windows_stdio")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   `Py_FileSystemDefaultEncoding`, `Py_HasFileSystemDefaultEncoding`: Use [`PyConfig.filesystem_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_encoding "PyConfig.filesystem_encoding")
         or [`PyConfig_Get("filesystem_encoding")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   `Py_FileSystemDefaultEncodeErrors`: Use [`PyConfig.filesystem_errors`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_errors "PyConfig.filesystem_errors")
         or [`PyConfig_Get("filesystem_errors")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   `Py_UTF8Mode`: Use [`PyPreConfig.utf8_mode`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.utf8_mode "PyPreConfig.utf8_mode")
         or [`PyConfig_Get("utf8_mode")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead. (see [`Py_PreInitialize()`](https://docs.python.org/3/c-api/init_config.html#c.Py_PreInitialize "Py_PreInitialize")
        )
        
    
    The [`Py_InitializeFromConfig()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig "Py_InitializeFromConfig")
     API should be used with [`PyConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
     to set these options. Or [`PyConfig_Get()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
     can be used to get these options at runtime.
    

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Pending+removal+in+Python+3.15&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fdeprecations%2Fc-api-pending-removal-in-3.15.html&pagesource=deprecations%2Fc-api-pending-removal-in-3.15.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/deprecations/c-api-pending-removal-in-3.15.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Pending removal in Python 3.15](https://docs.python.org/3/deprecations/c-api-pending-removal-in-3.15.html)
    
*    
    
    |
*   Theme Auto Light Dark |