[Skip to main content](https://docs.conda.io/projects/conda/en/stable/configuration.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

Configuration[#](https://docs.conda.io/projects/conda/en/stable/configuration.html#configuration "Link to this heading")

=========================================================================================================================

\# ######################################################
# ##              Channel Configuration               ##
# ######################################################

# # channels (sequence: primitive)
# #   aliases: channel
# #   env var string delimiter: ','
# #   The list of conda channels to include for relevant operations.
# # 
# channels: \[\]

# # channel\_alias (str)
# #   The prepended url location to associate with channel names.
# # 
# channel\_alias: https://conda.anaconda.org

# # channel\_settings (sequence: map)
# #   env var string delimiter: ','
# #   A list of mappings that allows overriding certain settings for a
# #   single channel. Each list item should include at least the "channel"
# #   key and the setting you would like to override. The "channel" value
# #   may be a channel name, multichannel name, channel URL, or glob-like
# #   URL pattern. Supported settings include auth-related plugin settings
# #   and exclude\_newer.
# # 
# channel\_settings: \[\]

# # default\_channels (sequence: primitive)
# #   env var string delimiter: ','
# #   The list of channel names and/or urls used for the 'defaults'
# #   multichannel. Can be overridden by 'custom\_multichannels.defaults'.
# # 
# default\_channels:
#   - https://repo.anaconda.com/pkgs/main
#   - https://repo.anaconda.com/pkgs/r

# # override\_channels\_enabled (bool)
# #   Permit use of the --override-channels command-line flag.
# # 
# override\_channels\_enabled: true

# # allowlist\_channels (sequence: primitive)
# #   aliases: whitelist\_channels
# #   env var string delimiter: ','
# #   The exclusive list of channels allowed to be used on the system. Use
# #   of any other channels will result in an error. If conda-build channels
# #   are to be allowed, along with the --use-local command line flag, be
# #   sure to include the 'local' channel in the list. If the list is empty
# #   or left undefined, no channel exclusions will be enforced.
# # 
# allowlist\_channels: \[\]

# # denylist\_channels (sequence: primitive)
# #   env var string delimiter: ','
# #   The list of channels that are denied to be used on the system. Use of
# #   any of these channels will result in an error. If conda-build channels
# #   are to be allowed, along with the --use-local command line flag, be
# #   sure to not include the 'local' channel in the list. If the list is
# #   empty or left undefined, no channel exclusions will be enforced.
# # 
# denylist\_channels: \[\]

# # custom\_channels (map: primitive)
# #   A map of key-value pairs where the key is a channel name and the value
# #   is a channel location. Channels defined here override the default
# #   'channel\_alias' value. The channel name (key) is not included in the
# #   channel location (value).  For example, to override the location of
# #   the 'conda-forge' channel where the url to repodata is
# #   https://anaconda-repo.dev/packages/conda-forge/linux-64/repodata.json,
# #   add an entry 'conda-forge: https://anaconda-repo.dev/packages'.
# # 
# custom\_channels:
#   pkgs/pro: https://repo.anaconda.com

# # custom\_multichannels (map: sequence)
# #   A multichannel is a metachannel composed of multiple channels. The
# #   only reserved multichannel is 'local', which is a list of file://
# #   channel locations where conda-build stashes successfully-built
# #   packages and cannot be overridden. Other multichannels, including
# #   'defaults', can be defined or customized with custom\_multichannels,
# #   where the key is the multichannel name and the value is a list of
# #   channel names and/or channel urls. The 'defaults' multichannel can
# #   also be customized using the 'default\_channels' parameter (a
# #   historical setting from when 'defaults' was reserved). If both are
# #   defined, 'custom\_multichannels.defaults' takes precedence.
# # 
# custom\_multichannels: {}

# # migrated\_channel\_aliases (sequence: primitive)
# #   env var string delimiter: ','
# #   A list of previously-used channel\_alias values. Useful when switching
# #   between different Anaconda Repository instances.
# # 
# migrated\_channel\_aliases: \[\]

# # migrated\_custom\_channels (map: primitive)
# #   A map of key-value pairs where the key is a channel name and the value
# #   is the previous location of the channel.
# # 
# migrated\_custom\_channels: {}

# # add\_anaconda\_token (bool)
# #   aliases: add\_binstar\_token
# #   In conjunction with the anaconda command-line client (installed with
# #   \`conda install anaconda-client\`), and following logging into an
# #   Anaconda Server API site using \`anaconda login\`, automatically apply a
# #   matching private token to enable access to private packages and
# #   channels.
# # 
# add\_anaconda\_token: true

# # allow\_non\_channel\_urls (bool)
# #   Warn, but do not fail, when conda detects a channel url is not a valid
# #   channel.
# # 
# allow\_non\_channel\_urls: false

# # repodata\_fns (sequence: primitive)
# #   env var string delimiter: ','
# #   Specify filenames for repodata fetching. The default is
# #   ('current\_repodata.json', 'repodata.json'), which tries a subset of
# #   the full index containing only the latest version for each package,
# #   then falls back to repodata.json.  You may want to specify something
# #   else to use an alternate index that has been reduced somehow.
# # 
# repodata\_fns:
#   - current\_repodata.json
#   - repodata.json

# # use\_only\_tar\_bz2 (NoneType, bool)
# #   A boolean indicating that only .tar.bz2 conda packages should be
# #   downloaded. This is forced to True if conda-build is installed and
# #   older than 3.18.3, because older versions of conda break when conda
# #   feeds it the new file format.
# # 
# use\_only\_tar\_bz2:

# # repodata\_threads (int)
# #   Threads to use when downloading and reading repodata.  When not set,
# #   defaults to None, which uses the default ThreadPoolExecutor behavior.
# # 
# repodata\_threads: 0

# # fetch\_threads (int)
# #   Threads to use when downloading packages.  When not set, defaults to
# #   None, which uses the default ThreadPoolExecutor behavior.
# # 
# fetch\_threads: 0

# # experimental (sequence: primitive)
# #   env var string delimiter: ','
# #   List of experimental features to enable.
# # 
# experimental: \[\]

# # no\_lock (bool)
# #   Disable index cache lock (defaults to enabled).
# # 
# no\_lock: false

# # repodata\_use\_zst (bool)
# #   Use \`repodata.json.zst\` if available.
# # 
# repodata\_use\_zst: true

# # repodata\_use\_shards (bool)
# #   Use sharded repodata if available.
# # 
# repodata\_use\_shards: true


# ######################################################
# ##            Basic Conda Configuration             ##
# ######################################################

# # envs\_dirs (sequence: primitive)
# #   aliases: envs\_path
# #   env var string delimiter: ':'
# #   The list of directories to search for named environments. When
# #   creating a new named environment, the environment will be placed in
# #   the first writable location.
# # 
# envs\_dirs: \[\]

# # pkgs\_dirs (sequence: primitive)
# #   env var string delimiter: ','
# #   The list of directories where locally-available packages are linked
# #   from at install time. Packages not locally available are downloaded
# #   and extracted into the first writable directory.
# # 
# pkgs\_dirs: \[\]

# # default\_threads (int)
# #   Threads to use by default for parallel operations.  Default is None,
# #   which allows operations to choose themselves.  For more specific
# #   control, see the other \*\_threads parameters:     \* repodata\_threads -
# #   for fetching/loading repodata     \* verify\_threads - for verifying
# #   package contents in transactions     \* execute\_threads - for carrying
# #   out the unlinking and linking steps
# # 
# default\_threads: 0

# # preview (sequence: primitive)
# #   env var string delimiter: ','
# #   List of preview features to opt into.
# # 
# preview: \[\]


# ######################################################
# ##              Network Configuration               ##
# ######################################################

# # client\_ssl\_cert (NoneType, str)
# #   aliases: client\_cert
# #   A path to a single file containing a private key and certificate (e.g.
# #   .pem file). Alternately, use client\_ssl\_cert\_key in conjunction with
# #   client\_ssl\_cert for individual files.
# # 
# client\_ssl\_cert:

# # client\_ssl\_cert\_key (NoneType, str)
# #   aliases: client\_cert\_key
# #   Used in conjunction with client\_ssl\_cert for a matching key file.
# # 
# client\_ssl\_cert\_key:

# # local\_repodata\_ttl (bool, int)
# #   For a value of False or 0, always fetch remote repodata (HTTP 304
# #   responses respected). For a value of True or 1, respect the HTTP
# #   Cache-Control max-age header. Any other positive integer values is the
# #   number of seconds to locally cache repodata before checking the remote
# #   server for an update.
# # 
# local\_repodata\_ttl: 1

# # offline (bool)
# #   Restrict conda to cached download content and file:// based urls.
# # 
# offline: false

# # proxy\_servers (map: primitive)
# #   A mapping to enable proxy settings. Keys can be either (1) a
# #   scheme://hostname form, which will match any request to the given
# #   scheme and exact hostname, or (2) just a scheme, which will match
# #   requests to that scheme. Values are are the actual proxy server, and
# #   are of the form 'scheme://\[user:password@\]host\[:port\]'. The optional
# #   'user:password' inclusion enables HTTP Basic Auth with your proxy.
# # 
# proxy\_servers: {}

# # remote\_connect\_timeout\_secs (float)
# #   The number seconds conda will wait for your client to establish a
# #   connection to a remote url resource.
# # 
# remote\_connect\_timeout\_secs: 9.15

# # remote\_max\_retries (int)
# #   The maximum number of retries each HTTP connection should attempt.
# # 
# remote\_max\_retries: 3

# # remote\_backoff\_factor (int)
# #   The factor determines the time HTTP connection should wait for
# #   attempt.
# # 
# remote\_backoff\_factor: 1

# # remote\_read\_timeout\_secs (float)
# #   Once conda has connected to a remote resource and sent an HTTP
# #   request, the read timeout is the number of seconds conda will wait for
# #   the server to send a response.
# # 
# remote\_read\_timeout\_secs: 60.0

# # ssl\_verify (bool, str)
# #   aliases: verify\_ssl
# #   Conda verifies SSL certificates for HTTPS requests, just like a web
# #   browser. By default, SSL verification is enabled, and conda operations
# #   will fail if a required url's certificate cannot be verified. Setting
# #   ssl\_verify to False disables certification verification. The value for
# #   ssl\_verify can also be (1) a path to a CA bundle file, (2) a path to a
# #   directory containing certificates of trusted CA, or (3) 'truststore'
# #   to use the operating system certificate store.
# # 
# ssl\_verify: true


# ######################################################
# ##               Solver Configuration               ##
# ######################################################

# # add\_pip\_as\_python\_dependency (bool)
# #   Add pip as a dependency of python. This ensures pip will always be
# #   installed any time python is installed.
# # 
# add\_pip\_as\_python\_dependency: true

# # aggressive\_update\_packages (sequence: primitive)
# #   env var string delimiter: ','
# #   A list of packages that, if installed, are always updated to the
# #   latest possible version.
# # 
# aggressive\_update\_packages:
#   - ca-certificates
#   - certifi
#   - openssl

# # auto\_update\_conda (bool)
# #   aliases: self\_update
# #   Automatically update conda when a newer or higher priority version is
# #   detected.
# # 
# auto\_update\_conda: true

# # channel\_priority (ChannelPriority)
# #   Accepts values of 'strict', 'flexible', and 'disabled'. The default
# #   value is 'flexible'. With strict channel priority, packages in lower
# #   priority channels are not considered if a package with the same name
# #   appears in a higher priority channel. With flexible channel priority,
# #   the solver may reach into lower priority channels to fulfill
# #   dependencies, rather than raising an unsatisfiable error. With channel
# #   priority disabled, package version takes precedence, and the
# #   configured priority of channels is used only to break ties. In
# #   previous versions of conda, this parameter was configured as either
# #   True or False. True is now an alias to 'flexible'.
# # 
# channel\_priority: flexible

# # exclude\_newer (str)
# #   aliases: cooldown
# #   Exclude packages published more recently than the given threshold.
# #   Accepts durations (7d, 3d12h, 1w, P7D), ISO 8601 dates (2026-04-01),
# #   RFC 3339 timestamps (2026-04-01T12:00:00Z), or a plain number of
# #   seconds. Date-only values are interpreted as the start of the next day
# #   in UTC. Set to 0 for no delay, using the current time as the cutoff.
# #   Leave empty to disable (the default). Packages without an
# #   indexed\_timestamp or timestamp are included for compatibility.
# #   Channel-specific cutoffs can be set with exclude\_newer entries in
# #   channel\_settings, and per-package overrides can be set with
# #   exclude\_newer\_package.
# # 
# exclude\_newer: ''

# # exclude\_newer\_package (map: primitive)
# #   aliases: cooldown\_exclude
# #   Per-package overrides for the exclude\_newer policy. Maps package names
# #   to a duration string (e.g. "30d"), a timestamp, or false to exempt the
# #   package entirely. For example:   exclude\_newer\_package:     openssl:
# #   false     numpy: 30d
# # 
# exclude\_newer\_package: {}

# # create\_default\_packages (sequence: primitive)
# #   env var string delimiter: ','
# #   Packages that are by default added to a newly created environments.
# # 
# create\_default\_packages: \[\]

# # disallowed\_packages (sequence: primitive)
# #   aliases: disallow
# #   env var string delimiter: '&'
# #   Package specifications to disallow installing. The default is to allow
# #   all packages.
# # 
# disallowed\_packages: \[\]

# # force\_reinstall (bool)
# #   Ensure that any user-requested package for the current operation is
# #   uninstalled and reinstalled, even if that package already exists in
# #   the environment.
# # 
# force\_reinstall: false

# # pinned\_packages (sequence: primitive)
# #   env var string delimiter: '&'
# #   A list of package specs to pin for every environment resolution. This
# #   parameter is in BETA, and its behavior may change in a future release.
# # 
# pinned\_packages: \[\]

# # prefix\_data\_interoperability (bool)
# #   aliases: pip\_interop\_enabled
# #   Enable plugins to allow conda to interact with non-conda-installed
# #   packages.
# # 
# prefix\_data\_interoperability: false

# # track\_features (sequence: primitive)
# #   env var string delimiter: ','
# #   A list of features that are tracked by default. An entry here is
# #   similar to adding an entry to the create\_default\_packages list.
# # 
# track\_features: \[\]

# # solver (str)
# #   aliases: experimental\_solver
# #   A string to choose between the different solver logics implemented in
# #   conda. A solver logic takes care of turning your requested packages
# #   into a list of specs to add and/or remove from a given environment,
# #   based on their dependencies and specified constraints.
# # 
# solver: rattler


# ######################################################
# ##  Package Linking and Install-time Configuration  ##
# ######################################################

# # allow\_softlinks (bool)
# #   When allow\_softlinks is True, conda uses hard-links when possible, and
# #   soft-links (symlinks) when hard-links are not possible, such as when
# #   installing on a different filesystem than the one that the package
# #   cache is on. When allow\_softlinks is False, conda still uses hard-
# #   links when possible, but when it is not possible, conda copies files.
# #   Individual packages can override this setting, specifying that certain
# #   files should never be soft-linked (see the no\_link option in the build
# #   recipe documentation).
# # 
# allow\_softlinks: false

# # always\_copy (bool)
# #   aliases: copy
# #   Register a preference that files be copied into a prefix during
# #   install rather than hard-linked.
# # 
# always\_copy: false

# # always\_softlink (bool)
# #   aliases: softlink
# #   Register a preference that files be soft-linked (symlinked) into a
# #   prefix during install rather than hard-linked. The link source is the
# #   'pkgs\_dir' package cache from where the package is being linked.
# #   WARNING: Using this option can result in corruption of long-lived
# #   conda environments. Package caches are \*caches\*, which means there is
# #   some churn and invalidation. With this option, the contents of
# #   environments can be switched out (or erased) via operations on other
# #   environments.
# # 
# always\_softlink: false

# # path\_conflict (PathConflict)
# #   The method by which conda handle's conflicting/overlapping paths
# #   during a create, install, or update operation. The value must be one
# #   of 'clobber', 'warn', or 'prevent'. The '--clobber' command-line flag
# #   or clobber configuration parameter overrides path\_conflict set to
# #   'prevent'.
# # 
# path\_conflict: clobber

# # rollback\_enabled (bool)
# #   Should any error occur during an unlink/link transaction, revert any
# #   disk mutations made to that point in the transaction.
# # 
# rollback\_enabled: true

# # safety\_checks (SafetyChecks)
# #   Enforce available safety guarantees during package installation. The
# #   value must be one of 'enabled', 'warn', or 'disabled'.
# # 
# safety\_checks: warn

# # extra\_safety\_checks (bool)
# #   Spend extra time validating package contents.  Currently, runs sha256
# #   verification on every file within each package during installation.
# # 
# extra\_safety\_checks: false

# # signing\_metadata\_url\_base (NoneType, str)
# #   Base URL for obtaining trust metadata updates (i.e., the \`\*.root.json\`
# #   and \`key\_mgr.json\` files) used to verify metadata and (eventually)
# #   package signatures.
# # 
# signing\_metadata\_url\_base:

# # shortcuts (bool)
# #   Allow packages to create OS-specific shortcuts (e.g. in the Windows
# #   Start Menu) at install time.
# # 
# shortcuts: true

# # shortcuts\_only (sequence: primitive)
# #   env var string delimiter: ','
# #   Create shortcuts only for the specified package names.
# # 
# shortcuts\_only: \[\]

# # non\_admin\_enabled (bool)
# #   Allows completion of conda's create, install, update, and remove
# #   operations, for non-privileged (non-root or non-administrator) users.
# # 
# non\_admin\_enabled: true

# # separate\_format\_cache (bool)
# #   Treat .tar.bz2 files as different from .conda packages when filenames
# #   are otherwise similar. This defaults to False, so that your package
# #   cache doesn't churn when rolling out the new package format. If you'd
# #   rather not assume that a .tar.bz2 and .conda from the same place
# #   represent the same content, set this to True.
# # 
# separate\_format\_cache: false

# # verify\_threads (int)
# #   Threads to use when performing the transaction verification step.
# #   When not set, defaults to 1.
# # 
# verify\_threads: 0

# # execute\_threads (int)
# #   Threads to use when performing the unlink/link transaction.  When not
# #   set, defaults to 1.  This step is pretty strongly I/O limited, and you
# #   may not see much benefit here.
# # 
# execute\_threads: 0


# ######################################################
# ##            Conda-build Configuration             ##
# ######################################################

# # bld\_path (str)
# #   The location where conda-build will put built packages. Same as
# #   'croot', but 'croot' takes precedence when both are defined. Also used
# #   in construction of the 'local' multichannel.
# # 
# bld\_path: ''

# # croot (str)
# #   The location where conda-build will put built packages. Same as
# #   'bld\_path', but 'croot' takes precedence when both are defined. Also
# #   used in construction of the 'local' multichannel.
# # 
# croot: ''

# # anaconda\_upload (NoneType, bool)
# #   aliases: binstar\_upload
# #   Automatically upload packages built with conda build to anaconda.org.
# # 
# anaconda\_upload:

# # conda\_build (map: primitive)
# #   aliases: conda-build
# #   General configuration parameters for conda-build.
# # 
# conda\_build: {}


# ######################################################
# ##  Output, Prompt, and Flow Control Configuration  ##
# ######################################################

# # always\_yes (NoneType, bool)
# #   aliases: yes
# #   Automatically choose the 'yes' option whenever asked to proceed with a
# #   conda operation, such as when running \`conda install\`.
# # 
# always\_yes:

# # auto\_activate (bool)
# #   aliases: auto\_activate\_base
# #   Automatically activate the environment given at
# #   'default\_activation\_env' during shell initialization.
# # 
# auto\_activate: true

# # default\_activation\_env (str)
# #   The environment to be automatically activated on startup if
# #   'auto\_activate' is True. Also sets the default environment to activate
# #   when 'conda activate' receives no arguments.
# # 
# default\_activation\_env: base

# # auto\_stack (int)
# #   Implicitly use --stack when using activate if current level of nesting
# #   (as indicated by CONDA\_SHLVL environment variable) is less than or
# #   equal to specified value. 0 or false disables automatic stacking, 1 or
# #   true enables it for one level.
# # 
# auto\_stack: 0

# # changeps1 (bool)
# #   When using activate, change the command prompt ($PS1) to include the
# #   activated environment.
# # 
# changeps1: true

# # env\_prompt (str)
# #   Template for prompt modification based on the active environment.
# #   Currently supported template variables are '{prefix}', '{name}', and
# #   '{default\_env}'. '{prefix}' is the absolute path to the active
# #   environment. '{name}' is the basename of the active environment
# #   prefix. '{default\_env}' holds the value of '{name}' if the active
# #   environment is a conda named environment ('-n' flag), or otherwise
# #   holds the value of '{prefix}'. Templating uses python's str.format()
# #   method.
# # 
# env\_prompt: '({default\_env}) '

# # json (bool)
# #   Ensure all output written to stdout is structured json.
# # 
# json: false

# # console (str)
# #   Configure different backends to be used while rendering normal console
# #   output. Defaults to "classic".
# # 
# console: classic

# # notify\_outdated\_conda (bool)
# #   Notify if a newer version of conda is detected during a create,
# #   install, update, or remove operation.
# # 
# notify\_outdated\_conda: true

# # quiet (bool)
# #   Disable progress bar display and other output.
# # 
# quiet: false

# # report\_errors (NoneType, bool)
# #   Opt in, or opt out, of automatic error reporting to core maintainers.
# #   Error reports are anonymous, with only the error stack trace and
# #   information given by \`conda info\` being sent.
# # 
# report\_errors:

# # show\_channel\_urls (NoneType, bool)
# #   Show channel URLs when displaying what is going to be downloaded.
# # 
# show\_channel\_urls:

# # list\_fields (sequence: primitive)
# #   env var string delimiter: ','
# #   Default fields to report as columns in the output of \`conda list\`.
# # 
# list\_fields:
#   - name
#   - version
#   - build
#   - channel\_name

# # verbosity (int)
# #   aliases: verbose
# #   Sets output log level. 0 is warn. 1 is info. 2 is debug. 3 is trace.
# # 
# verbosity: 0

# # unsatisfiable\_hints (bool)
# #   A boolean to determine if conda should find conflicting packages in
# #   the case of a failed install.
# # 
# unsatisfiable\_hints: true

# # unsatisfiable\_hints\_check\_depth (int)
# #   An integer that specifies how many levels deep to search for
# #   unsatisfiable dependencies. If this number is 1 it will complete the
# #   unsatisfiable hints fastest (but perhaps not the most complete). The
# #   higher this number, the longer the generation of the unsat hint will
# #   take. Defaults to 3.
# # 
# unsatisfiable\_hints\_check\_depth: 2

# # number\_channel\_notices (int)
# #   Sets the number of channel notices to be displayed when running
# #   commands the "install", "create", "update", "env create", and "env
# #   update" . Defaults to 5. In order to completely suppress channel
# #   notices, set this to 0.
# # 
# number\_channel\_notices: 5

# # envvars\_force\_uppercase (bool)
# #   Force uppercase for new environment variable names. Defaults to True.
# # 
# envvars\_force\_uppercase: true

# # export\_platforms (sequence: primitive)
# #   aliases: extra\_platforms
# #   env var string delimiter: ','
# #   Additional platform(s)/subdir(s) for export (e.g., linux-64, osx-64,
# #   win-64), current platform is always included.
# # 
# export\_platforms: \[\]

# # override\_virtual\_packages (map: primitive)
# #   aliases: virtual\_packages
# #   Set override values for virtual packages.
# # 
# override\_virtual\_packages: {}


# ######################################################
# ##               Plugin Configuration               ##
# ######################################################

# # no\_plugins (bool)
# #   Disable all currently-registered plugins, except built-in conda
# #   plugins.
# # 
# no\_plugins: false


# ######################################################
# ##                   Experimental                   ##
# ######################################################

# # environment\_specifier (NoneType, str)
# #   aliases: env\_spec
# #   \*\*EXPERIMENTAL\*\* While experimental, expect both major and minor
# #   changes across minor releases.  The name of the environment specifier
# #   plugin that should be used for this context. If not specified, the
# #   plugin manager will try to detect the plugin to use.
# # 
# environment\_specifier:

Copy to clipboard

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/configuration.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/configuration.rst.txt)