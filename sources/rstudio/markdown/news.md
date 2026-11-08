Copy for LLM View as Markdown

Introduction[](https://docs.posit.co/ide/news/#introduction)

-------------------------------------------------------------

This page provides the release notes associated with each release of RStudio and Posit Workbench. Please contact customer support using the [Posit support form](https://support.posit.co/hc/en-us/requests/new)
 for questions about the described changes.

2026.10.1[](https://docs.posit.co/ide/news/#rstudio-2026.10.1)

---------------------------------------------------------------

**“Blue Mistflower”** | Date: 2026-10-28

### Fixed[](https://docs.posit.co/ide/news/#fixed)

#### RStudio[](https://docs.posit.co/ide/news/#rstudio)

*   ([#19118](https://github.com/rstudio/rstudio/issues/19118)
    ): Fixed an issue where sessions failed to start when a project’s `.Rproj.user` directory lived on a filesystem that refuses ACL writes, such as an NTFS mount.

#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench)

*   (rstudio-pro#13041) Fixed an issue where Kubernetes-backed session starts could be delayed by up to 60 seconds unnecessarily.

2026.10.0[](https://docs.posit.co/ide/news/#rstudio-2026.10.0)

---------------------------------------------------------------

**“Blue Mistflower”** | Date: 2026-10-14

### New[](https://docs.posit.co/ide/news/#new)

#### RStudio[](https://docs.posit.co/ide/news/#rstudio-1)

*   ([#19026](https://github.com/rstudio/rstudio/issues/19026)
    ): The Git pane’s branch menu now lists the repository’s worktrees. Selecting one (or a branch checked out in one) opens that worktree as a project, in this window or in a new session, and More > New Worktree… checks a branch out into a new worktree (New Branch can also create its branch in a new worktree, and More > Remove Worktree… deletes one). A project opened from a worktree is labelled with the primary checkout’s name and the worktree directory, e.g. “rstudio \[feature-x\]”.
*   ([#19027](https://github.com/rstudio/rstudio/issues/19027)
    ): Vim key mappings can now also be loaded from `$XDG_CONFIG_HOME/vim/vimrc` (or `~/.config/vim/vimrc` when `XDG_CONFIG_HOME` is unset), which is checked after `~/.rstudio-vimrc` and `~/.vimrc`. Thanks to [@layne-cooper](https://github.com/layne-cooper)
    .
*   ([#4422](https://github.com/rstudio/rstudio/issues/4422)
    ): Plots can now be drawn at a fixed size instead of the size of the Plots pane (Plots > Fixed Size…, or the size menu in the Plots pane toolbar). The plot is scaled down to fit the pane without being redrawn when the pane is resized, and exported plots default to the same size. Save Plot as Image can also save bitmaps at a chosen resolution (up to 600 DPI) without changing the plot’s layout, and shows the image’s size in inches and pixels.
*   ([#17787](https://github.com/rstudio/rstudio/issues/17787)
    ): Columns in the data viewer can now be hidden and shown from the summary panel, individually or all at once.
*   ([#9755](https://github.com/rstudio/rstudio/issues/9755)
    ): Objects whose names begin with a dot (e.g. `.data` arguments while debugging) can now be shown in the Environment pane with Show Hidden Objects in the pane’s List/Grid menu. The menu also offers Show .Last.value, previously only in Global Options, and the pane now refreshes as soon as either setting changes.
*   ([#18692](https://github.com/rstudio/rstudio/issues/18692)
    ): The active document tab now has a bold label and a blue overline to make it easier to identify. This is enabled by default and can be disabled in Global Options > General > Basic > Other.
*   ([#14485](https://github.com/rstudio/rstudio/issues/14485)
    ): R diagnostics now warn about characters in code that look like ASCII but are not (e.g. a Cyrillic ‘c’, typographic quotes, or a no-break space), and about invisible characters such as a zero-width space. This can be disabled in Global Options > Code > Diagnostics.
*   ([#19012](https://github.com/rstudio/rstudio/issues/19012)
    ): R diagnostics now warn when a format string passed to `sprintf()` or `gettextf()` uses the `0` flag with `%s` (e.g. `%05s`), since zero-padding strings is platform-dependent.
*   ([#18977](https://github.com/rstudio/rstudio/issues/18977)
    ): R diagnostics now report a repeated formal argument in a function definition (`function(x, x)`).
*   ([#18977](https://github.com/rstudio/rstudio/issues/18977)
    ): R diagnostics now report a named argument that matches the same formal more than once (`rnorm(n = 1, n = 2)`) when argument checking is enabled (Global Options > Code > Diagnostics). Names absorbed by `...`, as in `c(a = 1, a = 2)`, are still allowed.
*   ([#18978](https://github.com/rstudio/rstudio/issues/18978)
    ): R diagnostics now report an assignment to a constant, such as `TRUE <- 1` or `1 <- x`.
*   ([#18979](https://github.com/rstudio/rstudio/issues/18979)
    ): R diagnostics now warn about a bare `return` used without parentheses, which evaluates to the `return` function instead of returning from the enclosing one.
*   ([#18980](https://github.com/rstudio/rstudio/issues/18980)
    ): R diagnostics now warn about `if (x<-1)` and `while (x<-1)`, which assign rather than compare, when `x < -1` was likely intended.
*   ([#9156](https://github.com/rstudio/rstudio/issues/9156)
    ): R diagnostics now report too many arguments in a call to a function that takes none, such as `Sys.time(1)`, when argument checking is enabled.
*   ([#9157](https://github.com/rstudio/rstudio/issues/9157)
    ): R diagnostics now report an empty trailing argument in calls that reject one, such as `c(1, 2, )` or `paste("a", )`, when argument checking is enabled. Functions that accept a trailing empty argument, including `switch()` and tidyverse functions, are not affected.
*   ([#18981](https://github.com/rstudio/rstudio/issues/18981)
    ): R diagnostics now warn about a `library()` or `require()` call for a package that is not installed.
*   ([#18982](https://github.com/rstudio/rstudio/issues/18982)
    ): R diagnostics now give a specific message for invalid characters, such as a pasted smart quote, an unterminated raw string, or a lone `%`, instead of “unexpected token”.
*   ([#16102](https://github.com/rstudio/rstudio/issues/16102)
    ): Added Code > Select Current Statement (Ctrl+Alt+Shift+S), which selects the whole R statement containing the cursor, including statements that span several lines.
*   ([#12223](https://github.com/rstudio/rstudio/issues/12223)
    ): Added Edit > Change Spelling Language… (also in the Command Palette) to switch the spelling dictionary in one step. Dictionary changes now take effect immediately in open documents, without restarting RStudio.
*   ([#6781](https://github.com/rstudio/rstudio/issues/6781)
    ): Added Show Document’s Directory to the document tab context menu, and Show Current Document’s Directory in Files Pane to the Command Palette, to navigate the Files pane to the folder containing a document, including one open in a separate source window. The tab menu’s Set Working Directory item now also moves the Files pane when used from a separate source window.
*   ([#14226](https://github.com/rstudio/rstudio/issues/14226)
    ): Files can now be opened in the source editor from the Terminal pane with `rstudio <file>[:line[:column]]` (macOS, Linux, and RStudio Server).
*   ([#18804](https://github.com/rstudio/rstudio/issues/18804)
    ): File paths printed in the Terminal pane (for example by `git status`, `ls`, or compiler diagnostics) can now be opened in RStudio with Ctrl+Click (Cmd+Click on macOS); a `file:line:column` suffix opens the file at that position. This can be disabled in Global Options > Terminal.
*   ([#1687](https://github.com/rstudio/rstudio/issues/1687)
    ): Ctrl+Shift+C now copies the selection and Ctrl+Shift+V pastes in the Terminal pane, matching the shortcuts used by common terminal emulators.
*   ([#15261](https://github.com/rstudio/rstudio/issues/15261)
    ): The Insert Pipe Operator command (Ctrl+Shift+M) now inserts `+` when the cursor is within a ggplot2 chain. This can be disabled in Global Options > Code > Editing.
*   ([#12379](https://github.com/rstudio/rstudio/issues/12379)
    ): Customized editor keyboard shortcuts (e.g. Remove Word Left) now also apply to the Console input.
*   ([#14696](https://github.com/rstudio/rstudio/issues/14696)
    ): Added a “Use smooth scrolling” option (Global Options > Code > Display) that animates source editor scrolling when the cursor moves off screen or when jumping to a line.
*   ([#13505](https://github.com/rstudio/rstudio/issues/13505)
    ): The document outline is now available for plain Markdown (.md) documents.
*   ([#12838](https://github.com/rstudio/rstudio/issues/12838)
    ): Rendering a Quarto document with the preview option set to “(No Preview)” now runs a one-shot `quarto render` in a background job that finishes when the render does, instead of leaving a `quarto preview` server running.
*   ([#11622](https://github.com/rstudio/rstudio/issues/11622)
    ): A minimized Console pane is minimized again after a successful render (R Markdown or Quarto) instead of staying open; it stays open when the render fails so the output can be inspected.
*   ([#16386](https://github.com/rstudio/rstudio/issues/16386)
    ): The console scrollback limit (Global Options > Console, “Maximum lines of output to keep in the console”) now takes effect immediately rather than at the next session start, and the option no longer accepts values below the minimum the session enforces.
*   ([#18857](https://github.com/rstudio/rstudio/issues/18857)
    ): The Console pane now shows the R version as soon as the session starts, instead of displaying “(unknown)” until the session had finished initializing.
*   ([#18739](https://github.com/rstudio/rstudio/issues/18739)
    ): Optimized RStudio Desktop startup time.
*   ([#18738](https://github.com/rstudio/rstudio/issues/18738)
    ): Reduced the disk space used by RStudio installations: Copilot Language Server binaries for other platforms are no longer installed, JavaScript source maps are no longer packaged, GWT symbol maps are stored compressed, and macOS application bundles are now transparently compressed on disk.
*   ([#18911](https://github.com/rstudio/rstudio/issues/18911)
    ): RStudio now saves its state files (preferences, UI and project state, recent files and projects, unsaved source documents, and similar) by writing a new copy and renaming it into place, so an RStudio crash or a killed process can no longer leave them empty or truncated, and a write that fails (for example on a full disk) leaves the previous contents in place. A symlinked `rstudio-prefs.json` stays a symlink, and a state file left owned by another user (e.g. after running RStudio with `sudo`) is replaced as long as its directory is writable.
*   ([#18658](https://github.com/rstudio/rstudio/issues/18658)
    ): Posit Assistant now installs each version into its own directory under `pai/versions`, selected through `pai/selected.json`, instead of replacing `pai/bin`. An update no longer modifies the installation a running session uses, so it no longer requires closing other sessions that are running Posit Assistant, and RStudio releases sharing a home directory no longer compete for one install. An existing `pai/bin` is left in place for older releases; this release downloads its own copy once, even of a version already installed there.
*   ([#18658](https://github.com/rstudio/rstudio/issues/18658)
    ): When Check for Posit Assistant Updates finds that the Posit Assistant you installed is already the latest version, it now offers to reinstall it. Copies provided by an administrator or bundled with RStudio are not offered. Reinstalling downloads a fresh copy into a new directory, which can fix an installation whose files were damaged; the previous copy is left in place.
*   ([#18774](https://github.com/rstudio/rstudio/issues/18774)
    ): RStudio now runs the newest compatible Posit Assistant installation, whether bundled with RStudio or installed per-user, instead of always preferring the user’s own. A per-user installation no longer shadows a newer bundled copy.
*   ([#18973](https://github.com/rstudio/rstudio/issues/18973)
    ): RStudio Server reads administrator-installed Posit Assistant versions from the `posit-assistant` directory beside the session binary (`/usr/lib/rstudio-server/bin/posit-assistant` on Linux). Versions installed there go under `versions` inside the copy bundled with Workbench, selected through `selected.json` in the same layout as a user’s own installation. RStudio runs the newest compatible of the selected version, the bundled copy, and the user’s own installation.
*   ([#18803](https://github.com/rstudio/rstudio/issues/18803)
    ): RStudio Desktop now logs detailed renderer, GPU, and utility process failures to help diagnose crashes.
*   ([#18937](https://github.com/rstudio/rstudio/issues/18937)
    ): On macOS, RStudio now warns when a package loads a second copy of the OpenMP runtime (libomp) into the R session, which can crash R as soon as a package runs OpenMP code, and names the packages to reinstall to fix it.
*   ([#10173](https://github.com/rstudio/rstudio/issues/10173)
    , [#7566](https://github.com/rstudio/rstudio/issues/7566)
    ): The Tutorial pane now has a filter box that narrows the list of tutorials by package name, tutorial name, or title. Several words can be combined, e.g. a package name followed by a word from the tutorial title.

#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-1)

*   (rstudio-pro#11913) Added Agent Activity (Preview), which shows each user their own AI coding-agent sessions, usage, and estimated costs on the Workbench homepage.
*   (rstudio-pro#12936) Added `profiles-level-precedence-enabled` to resolve `/etc/rstudio/profiles` like Job Launcher profiles, where `[username]` overrides `[@group]` overrides `[*]`. A future release will enable this by default.
*   (rstudio-pro#12981) Added `rstudio-server upgrade posit-assistant`, which installs, selects, lists, and cleans up administrator-managed versions of Posit Assistant for RStudio Pro sessions independently of Workbench upgrades.
*   (rstudio-pro#11659) The `pwb_sessions` Prometheus metric now includes a `session_host` label identifying the host each session is running on
*   (rstudio-pro#9557) Added a per-cluster preference in Settings for whether new sessions start from your last-used image or the administrator’s default image.
*   (rstudio-pro#12344) Workbench can now export OpenTelemetry logs and traces to more than one OTLP endpoint. Additional destinations, each with its own headers, batch interval, and export timeout, are configured in the new `/etc/rstudio/otel.conf` using the same `[OTLPEndpoint "name"]` syntax as Posit Connect, so a deployment can send telemetry to Chronicle and a third-party observability platform at once. Custom authorization headers can now be encrypted with `rstudio-server encrypt-password`.
*   (rstudio-pro#12100) The status tooltip for a failed session now shows the reason reported by the Job Launcher, and the tooltip retains the reported failure reason when `session-use-file-storage=0` is set.
*   (rstudio-pro#12105) Strengthened protection for stored AWS credentials.
*   (rstudio-pro#12570) Snowflake integrations accept an optional `host` key in `snowflake.conf`, which Workbench writes to the managed `connections.toml`. Set it when Snowflake traffic must reach an endpoint that cannot be derived from the account, such as restricted caller’s rights (RCR).
*   (rstudio-pro#12057) Added support for identifying users by GUID or unique key to `rstudio-server` command line tools.
*   (rstudio/launcher#1690) In the Kubernetes plugin’s image registry configuration, `repository-list` entries accept an optional `::Display Name` suffix. Workbench groups that repository’s images under the display name in the New Session dialog.
*   (rstudio/launcher#1691) The Kubernetes plugin’s new `container-repositories` profile setting restricts which registry repositories a user can see and launch discovered images from.
*   (rstudio-pro#12039) Added a new API endpoint that Admins can use to display banner notifications on all users’ homepage.
*   (rstudio-pro#11730) Added support for defining environment variables in `/etc/rstudio/profiles` that are added into session environments and can be scoped by username, group, or globally.

### Fixed[](https://docs.posit.co/ide/news/#fixed-1)

#### RStudio[](https://docs.posit.co/ide/news/#rstudio-2)

*   ([#8729](https://github.com/rstudio/rstudio/issues/8729)
    ): Fixed several issues where the R session could fail to start because of a problem with a file in RStudio’s data directory (`~/.local/share/rstudio`), such as one left unreadable or unwritable by running RStudio with `sudo`. On macOS and Linux, if the data directory itself can’t be written, RStudio now keeps session state in a temporary directory and explains the problem in the console, instead of failing to start. A suspended session whose restore crashed R is no longer restored again on every start; RStudio starts a new session and keeps the saved session aside for 30 days.
*   ([#18718](https://github.com/rstudio/rstudio/issues/18718)
    ): Fixed an issue where an R error during session initialization could leave the session hung forever at startup, with RStudio Server reporting that R was taking longer than usual to start.
*   ([#18735](https://github.com/rstudio/rstudio/issues/18735)
    ): Fixed an issue on Windows where RStudio failed to start when the command prompt was disabled by Group Policy.
*   ([#18318](https://github.com/rstudio/rstudio/issues/18318)
    ): Fixed a potential crash at exit when background threads were still running while the R session shut down, including when the session exited after losing its parent RStudio Desktop process.
*   ([#18899](https://github.com/rstudio/rstudio/issues/18899)
    ): Fixed an issue on RStudio Server where restarting R, or otherwise relaunching a session, could occasionally stall for about a minute with “Unable to connect to service” errors before the session came back.
*   ([#18963](https://github.com/rstudio/rstudio/issues/18963)
    ): Fixed an issue on RStudio Server where a response or error from the session being replaced during a restart could clear the replacement’s pending launch, so the next request launched the session a second time.
*   ([#18864](https://github.com/rstudio/rstudio/issues/18864)
    ): Fixed an RStudio Server crash (segfault) when downloading or exporting a file the user has no read permission on. The download now fails with an HTTP error instead.
*   ([#18870](https://github.com/rstudio/rstudio/issues/18870)
    ): Fixed an issue where a Restart R that took more than about ten seconds to come back left the console without focus and its prompt unrefreshed, and kept showing the previous R version after a restart into a different R.
*   ([#18784](https://github.com/rstudio/rstudio/issues/18784)
    ): Fixed an issue where quitting, closing a project, or switching projects shortly after a session restart prompted to save the workspace image even when Save workspace was set to Never.
*   ([#18818](https://github.com/rstudio/rstudio/issues/18818)
    ): Fixed an issue on RStudio Desktop where cancelling the quit prompted by closing the main window left every later close of that window exiting immediately, without prompting to save open documents or the workspace. The window’s position and size are now also saved from the close that actually happens, rather than from a close that was cancelled.
*   ([#18754](https://github.com/rstudio/rstudio/issues/18754)
    ): Fixed an issue where debugging a package function called from another function failed to show and step through its source code.
*   ([#18842](https://github.com/rstudio/rstudio/issues/18842)
    ): Fixed an issue where `View()` failed on data frames with integer columns when a package masking R’s summary functions (e.g. mosaic or mobilizr) was attached before RStudio’s own tools environment, as an `.Rprofile` `library()` call leaves it.
*   ([#18843](https://github.com/rstudio/rstudio/issues/18843)
    ): Fixed an issue where `View()` failed with “invalid multibyte string” on data frames holding text that is not valid in the session’s encoding.
*   ([#18620](https://github.com/rstudio/rstudio/issues/18620)
    ): Fixed an issue where the Data Viewer, with overlay scrollbars disabled, jumped back up and hid the last row under the horizontal scrollbar when scrolled to the bottom, and where its row numbers could fall a row out of step with the data at maximum scroll.
*   ([#18988](https://github.com/rstudio/rstudio/issues/18988)
    ): Fixed an issue where the Data Viewer jumped back up from the bottom of a table and left the last row cut off when the operating system’s animation effects were turned off (e.g. “Animation effects” in Windows’ accessibility settings), and where, on RStudio Server in recent versions of Chrome, it scrolled about half as far as the mouse wheel asked and flickered while its scrollbar was dragged.
*   ([#11506](https://github.com/rstudio/rstudio/issues/11506)
    ): Fixed an issue where a new Quarto document opened in visual mode when “Use visual markdown editor” was unchecked in the New Quarto Document dialog, if visual editing was the default for new documents or the project. The dialog now also offers this option for Shiny and Observable JS documents.
*   ([#18799](https://github.com/rstudio/rstudio/issues/18799)
    ): Closing a Quarto document’s source tab no longer cancels an in-progress render when the preview option is set to “(No Preview)”.
*   ([#18922](https://github.com/rstudio/rstudio/issues/18922)
    ): Fixed an issue where accepting RStudio’s own file chooser (RStudio Server, or Desktop with native file dialogs disabled) before its directory listing had loaded closed it without saving or opening anything. The chooser now completes the action once the listing arrives.
*   ([#14363](https://github.com/rstudio/rstudio/issues/14363)
    ): Fixed an issue where hexadecimal literals with binary exponents (e.g. `0x1p3`), fractions, uppercase `0X` prefixes, or an imaginary suffix were reported as parse errors.
*   ([#18717](https://github.com/rstudio/rstudio/issues/18717)
    ): Fixed an issue where the diagnostics system reported a spurious parse error for indexed numeric literals, e.g. `1[TRUE]`.
*   ([#18722](https://github.com/rstudio/rstudio/issues/18722)
    ): Fixed an issue where the diagnostics system reported “unexpected end of document” for R scripts ending with a semicolon.
*   ([#18914](https://github.com/rstudio/rstudio/issues/18914)
    ): Fixed an issue where console hyperlinks terminated with `ESC \` (as emitted by cli with `R_CLI_HYPERLINK_MODE=posix`) were displayed as raw escape text instead of links.
*   ([#18916](https://github.com/rstudio/rstudio/issues/18916)
    ): Fixed several issues with ANSI escape sequences in console output: `ESC[m` now resets colors, uncommon sequences (e.g. `ESC[4:3m`) no longer cause the rest of the output to go missing, other terminal sequences (e.g. window titles) are no longer shown as text, and hyperlinks are kept intact when a line is rewritten.\
*   ([#13292](https://github.com/rstudio/rstudio/issues/13292)\
    ): Fixed inline HTML tables produced by `knitr::kable()` retaining dark text when using a dark editor theme.\
*   ([#18874](https://github.com/rstudio/rstudio/issues/18874)\
    ): Inline data frame and `paged_table()` chunk output now uses the IDE’s proportional font instead of its own font stack, which rendered every cell in bold on Windows machines where the only installed “Lucida Sans” face is the demibold one.\
*   ([#4067](https://github.com/rstudio/rstudio/issues/4067)\
    ): Inline R Notebook plots now honor the knitr `dev.args` chunk option (e.g. `dev.args = list(type = "cairo")`), matching the output of a knit, and keep the graphics backend preference when they are resized.\
*   ([#9275](https://github.com/rstudio/rstudio/issues/9275)\
    ): The “(Default)” graphics backend and antialiasing preferences no longer override the `RStudioGD.backend` and `RStudioGD.antialias` options when they are set in an R profile (e.g. `Rprofile.site`), so a site-wide default graphics device can be configured there.\
*   ([#2142](https://github.com/rstudio/rstudio/issues/2142)\
    ): Global Options > General > Graphics now explains that the Windows graphics device antialiases text only, when that device is the selected or default backend.\
*   ([#4422](https://github.com/rstudio/rstudio/issues/4422)\
    ): On macOS, plot images saved from the Plots pane or copied to the clipboard now record their resolution, so applications such as Word insert them at the intended size. R’s Quartz graphics devices leave it out ([PR#19076](https://bugs.r-project.org/show_bug.cgi?id=19076)\
    ).\
*   ([#18744](https://github.com/rstudio/rstudio/issues/18744)\
    ): RStudio Desktop now uses link-based file locks by default on macOS and Linux, matching RStudio Server, so sessions from both editions sharing a data directory or a project on a network drive no longer mistake each other’s live locks for stale ones. RStudio also now checks both lock types before recovering source documents, and reports an error instead of reusing a source database held by another session.\
*   ([#18793](https://github.com/rstudio/rstudio/issues/18793)\
    ): Fixed an issue where custom Editor keyboard shortcuts were sometimes not applied to the Console at startup until a source document was opened.\
*   ([#18777](https://github.com/rstudio/rstudio/issues/18777)\
    ): Fixed an issue where each session restart added another copy of the Git and SVN directories to the `PATH` of restored terminals.\
*   ([#18921](https://github.com/rstudio/rstudio/issues/18921)\
    ): Fixed an issue where View > Panes > Console on Right placed the Console in the top-right quadrant after it had been placed bottom-right in the Pane Layout options, and where other options that default to on (such as “Use device pixel ratio” in Save Plot as Image) could not be saved as off.\
*   ([#18760](https://github.com/rstudio/rstudio/issues/18760)\
    ): Fixed an issue where long R version names in Global Options > General could push the R version selector outside the dialog.\
*   ([#18742](https://github.com/rstudio/rstudio/issues/18742)\
    ): Fixed an issue where the Global Options dialog could push the OK and Apply buttons off screen in short windows.\
*   ([#18736](https://github.com/rstudio/rstudio/issues/18736)\
    ): Fixed an issue where delayed document outline initialization could reactivate a closed Source column and leave a new document without an active editor.\
*   ([#18948](https://github.com/rstudio/rstudio/issues/18948)\
    ): Fixed an issue where, with Vim keybindings, `:e <file>` (and `:tabe`, `:badd`) did not open the file, `:e` with no file did not create a new R script, and `]f` / `[f` did not open the next or previous file in the directory. A relative file name given to `:e` is now opened relative to R’s working directory.\
*   ([#15669](https://github.com/rstudio/rstudio/issues/15669)\
    ): Fixed an issue on macOS where the Dock icon’s “New RStudio Window” command opened the project that was already open in the current window. The new window now starts with no project, in the default working directory.\
*   ([#18677](https://github.com/rstudio/rstudio/issues/18677)\
    ): Fixed Windows subprocess detection reporting unrelated processes as children after process ID reuse.\
*   ([#18794](https://github.com/rstudio/rstudio/issues/18794)\
    ): Python interpreter discovery (Global Options > Python > Select…) now bounds each interpreter probe, so a hung Python or conda executable no longer leaves the dialog stuck at “Finding interpreters…”.\
*   ([#18903](https://github.com/rstudio/rstudio/issues/18903)\
    ): Fixed an issue where Python function argument completions and their help were missing with Python 3.11 and newer, and for functions with keyword-only arguments or annotations.\
*   ([#9179](https://github.com/rstudio/rstudio/issues/9179)\
    ): Fixed an issue where `rstudioapi::writeRStudioPreference()` failed with “Type mismatch” when writing a whole number such as `14` (rather than `14L`) to an integer preference, or any value to a numeric preference like `font_size_points` after it had been set to a whole number in Global Options. `rstudioapi::readRStudioPreference()` now also returns numeric preferences as numbers, rather than as integers when their value is whole.\
*   ([#18831](https://github.com/rstudio/rstudio/issues/18831)\
    ): Fixed an issue where updating Posit Assistant from the chat pane left the new version being served under the previous version’s Content-Security-Policy until RStudio was restarted, which could break the chat pane.\
*   ([#18929](https://github.com/rstudio/rstudio/issues/18929)\
    ): Fixed an issue where Posit Assistant wasn’t notified of the first object created in an empty global environment, such as after Clear Workspace.\
*   ([#18882](https://github.com/rstudio/rstudio/issues/18882)\
    ): Fixed an issue where the background job that installs a feature’s required R packages reported success, and claimed the packages were installed, even when the installation had failed.\
*   ([#18896](https://github.com/rstudio/rstudio/issues/18896)\
    ): Removed a spurious `getLastCryptoError called with no pending error` warning from the logs.\
*   ([#18949](https://github.com/rstudio/rstudio/issues/18949)\
    ): Fixed an issue where the Publish command could be hidden after a save changed a document’s type, such as saving a new R script as R Markdown, or saving an R Markdown document as Quarto while more than one source column was open.\
*   ([#18956](https://github.com/rstudio/rstudio/issues/18956)\
    ): Fixed an issue where the editor’s Git commands were not updated after using Save As to move a file into or out of a project, until switching tabs.\
*   ([#18975](https://github.com/rstudio/rstudio/issues/18975)\
    ): Fixed an issue where Posit Assistant wrote no `positai.log` in Posit Workbench sessions. The log is now written to the session user’s RStudio log directory, next to the `rsession` log.\
*   ([#18955](https://github.com/rstudio/rstudio/issues/18955)\
    ): Fixed an issue where saving or closing a document in another source column could hide or disable commands for the active document, such as File > Publish.\
*   ([#18976](https://github.com/rstudio/rstudio/issues/18976)\
    ): Closing a terminal now terminates its shell. Previously the shell was only interrupted, so it kept running in the background, and the prompt it redrew was logged as `Unknown handle` errors in the session log.\
*   ([#18976](https://github.com/rstudio/rstudio/issues/18976)\
    ): Fixed an issue where RStudio Desktop wrote every line of the session log (`rsession-<user>.log`) twice.\
*   ([#18991](https://github.com/rstudio/rstudio/issues/18991)\
    ): Fixed an issue on Linux where the R session could become unresponsive, using all of a CPU core, when a process started by the session (for example, a parallel worker) exited while RStudio was computing memory usage.\
*   ([#18987](https://github.com/rstudio/rstudio/issues/18987)\
    ): Fixed an issue on RStudio Server where a document or Data Viewer window opened with “Show in New Window” and then closed was reopened the next time the session was restored, so closed windows accumulated over time.\
*   ([#18987](https://github.com/rstudio/rstudio/issues/18987)\
    ): Fixed an issue on RStudio Server where closing the window of a Plumber API run with “Run in Window” did not stop the API.\
*   ([#18987](https://github.com/rstudio/rstudio/issues/18987)\
    ): Fixed an issue where a Shiny application run with “Run in Window” kept running after its window was closed, if the application’s page had cancelled an earlier attempt to close the window.\
*   ([#19008](https://github.com/rstudio/rstudio/issues/19008)\
    ): Fixed an issue on RStudio Server where closing a popped-out editor window that had never been clicked or typed in lost its unsaved changes without a prompt, because the browser suppresses the unsaved-changes prompt in such a window; the unsaved documents now move back to the main window instead.\
*   ([#18845](https://github.com/rstudio/rstudio/issues/18845)\
    ): Fixed the Zotero 10 desktop client not being available as a citation source on macOS.\
*   ([#18845](https://github.com/rstudio/rstudio/issues/18845)\
    ): Fixed recently added Zotero 10 references not appearing in citations.\
*   ([#18787](https://github.com/rstudio/rstudio/issues/18787)\
    ): Fixed an issue on Windows where Posit Assistant failed to start in a second RStudio instance with “A Posit Assistant update is in progress”.\
*   ([#9075](https://github.com/rstudio/rstudio/issues/9075)\
    ): Fixed an issue where the source editor’s file type menu listed both C and C++ as “C/C++”, and offered no way to switch a file back to C. C and C++ sources, C/C++ headers (`.h`), and C++ headers (`.hpp`, `.hh`) now have distinct names.\
*   ([#16594](https://github.com/rstudio/rstudio/issues/16594)\
    ): Fixed an issue where setting `--ozone-platform` in `electron-flags.conf` could cause RStudio Desktop to open with a blank window on Linux. Thanks to [@victorwon2001](https://github.com/victorwon2001)\
    .\
*   ([#19005](https://github.com/rstudio/rstudio/issues/19005)\
    ): Fixed an error being logged when Refresh was clicked in the Find in Files pane before any search had been run.\
*   ([#19003](https://github.com/rstudio/rstudio/issues/19003)\
    ): Fixed an issue where installing a connection package that provides no connection extension, such as odbc, from the New Connection dialog logged a `No such file or directory` error in the session log.\
*   (rstudio-pro#12202): Fixed an issue where code diagnostics sometimes failed to render properly.\
*   (rstudio-pro#12203): Fixed an issue where the autocompletion help preview could render data values incorrectly.\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-2)\
\
*   (rstudio-pro#13139) Fixed the “Use Positron preview” option not appearing in the New Session dialog for Positron Pro sessions on Kubernetes when `session-use-file-storage=0` is set\
*   (rstudio-pro#13001) Fixed Databricks sign-in never taking effect, and sessions receiving an expired token, when a token from a previous OAuth flow (such as Entra ID before `native-oauth=1` was set) was still stored for the same workspace\
*   (rstudio-pro#13034) Fixed Workbench-managed credentials (AWS, Databricks, Snowflake, Posit Connect) that could stay missing or stale for a session after a failed refresh. Failed refreshes now retry quickly with backoff.\
*   (rstudio-pro#12982) Fixed Workbench failing to start when running as non-root with empty storage mounted at `/var/lib/rstudio-server`, such as newly provisioned shared storage on Kubernetes\
*   (rstudio-pro#12589) Fixed favicon to use the workbench icon for popped-out tabs or apps from editors, like a Shiny app from a Positron Pro, RStudio Pro, or VS Code session.\
*   (rstudio-pro#12920) Fixed provisioned users (JIT/SCIM) being unable to log in or launch sessions for up to 30 seconds after user provisioning was newly enabled, or after a restart where the Job Launcher came up before rserver\
*   (rstudio-pro#12566) Workbench Jobs launched without a name are now labeled “Workbench Job” instead of “RStudio Job” in Positron and VS Code, or “Unnamed Launcher Job” in RStudio\
*   (rstudio-pro#11659) Fixed the `pwb_sessions` Prometheus metric growing without bound in deployments that run sessions without the Job Launcher, where it counted the same sessions again on every poll and never dropped sessions that had exited\
*   (rstudio-pro#12514) Fixed `session.launch` OpenTelemetry traces being incomplete or missing in load-balanced deployments when launch stages were handled by different nodes. Trace and span ids are now derived deterministically from the session row, so any node can emit any span of the trace; resuming a session now produces its own launch trace distinct from the original launch’s.\
*   (rstudio-pro#12685) Log messages from Workbench’s Go services now honor the `log-level` and `log-message-format` settings in `logging.conf`, and are emitted as JSON when `log-message-format=json` is set\
*   (rstudio-pro#12683) Fixed logging stopping until restart when reloading an invalid `logging.conf`\
*   (rstudio-pro#12344) Fixed OpenTelemetry trace export never starting when `otel-traces-enabled=1` was set without also setting `otel-logs-enabled=1`.\
*   (rstudio-pro#6127) Fixed the default VS Code terminal profile setting shipping an invalid value, which prevented it from selecting the `bash` profile\
*   (rstudio-pro#11184) Fixed change of behavior where the port would get appended to `launcher-sessions-callback-address` even if it had the http/https prefix.\
*   (rstudio-pro#11721): Fixed `run-diagnostics` capturing the wrong NSS module config (or none) on installs with a custom `RSTUDIO_CONFIG_DIR`; it now always captures the fixed path (`/etc/rstudio/workbench-nss.conf`) the module reads.\
*   (rstudio/launcher#1681) Fixed Kubernetes plugin watches discarding their resume point on HTTP 429 (Too Many Requests) responses. Watches now reconnect with jittered backoff that honors the server’s `Retry-After` interval.\
*   (rstudio/launcher#1658) The Job Launcher `address` option now accepts bracketed IPv6 literals such as `[::1]`, and a wildcard bind address (`0.0.0.0` or `::`) falls back to whichever address family the host supports.\
*   (rstudio/launcher#1753) Fixed a Job Launcher plugin crash when job output contained a multi-byte UTF-8 character split across two output chunks.\
\
### Deprecated / Removed[](https://docs.posit.co/ide/news/#deprecated-removed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-3)\
\
*   ([#18658](https://github.com/rstudio/rstudio/issues/18658)\
    ): Removed the “Uninstall Posit Assistant” command. To remove a downloaded Posit Assistant, delete its `pai` directory by hand as described in the [user guide](https://docs.posit.co/ide/user/ide/guide/tools/posit-ai.html#removing-posit-assistant)\
    .\
*   ([#18973](https://github.com/rstudio/rstudio/issues/18973)\
    ): RStudio no longer uses the `posit-assistant-path` session option: sessions ignore it, and RStudio Server logs a warning at startup when `rsession.conf` sets it. RStudio also no longer reads a Posit Assistant from `pai` in the system configuration directory. RStudio Server administrators who installed one in either location should move it to `versions/<version>` in `/usr/lib/rstudio-server/bin/posit-assistant`.\
\
### Upgrade Instructions[](https://docs.posit.co/ide/news/#upgrade-instructions)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-3)\
\
*   (rstudio-pro#12981) RStudio Pro sessions no longer read a Posit Assistant from the `posit-assistant-path` option in `rsession.conf` or from `/etc/rstudio/pai/bin`, and run the copy bundled with Workbench or the user’s own copy instead. If that version is newer than the bundled copy, install it with `rstudio-server upgrade posit-assistant --version <version>`, or with `--file` for a package you have locally, to keep running it. An older version does not run even when selected. Remove `posit-assistant-path` from `rsession.conf`.\
*   (rstudio-pro#12344) `otel-logs-enabled` and `otel-traces-enabled` now default to the value of `otel-enabled` instead of defaulting to off. A deployment that previously set only `otel-enabled=1` – without explicitly setting either per-signal option – had both signals off before this release and now has both on, so it exports logs and traces to whatever destinations it has configured. Set `otel-logs-enabled=0` and/or `otel-traces-enabled=0` explicitly to keep exporting only a subset of signals.\
*   (rstudio-pro#12344) When both `otel-endpoint` and `otel-logs-endpoint` are set in `rserver.conf`, logs are now sent to `otel-logs-endpoint`. Previously `otel-endpoint` took precedence for logs and `otel-logs-endpoint` was ignored, so a deployment that sets both will start sending log records – and the credentials in `otel-logs-headers` – to a collector that was inert before this release. To keep the previous routing, either remove `otel-logs-endpoint`, or set it to the `otel-endpoint` value with `/v1/logs` appended: unlike `otel-endpoint`, `otel-logs-endpoint` is used verbatim and gets no signal path added. Traces already behaved this way and are unchanged.\
\
### Dependencies[](https://docs.posit.co/ide/news/#dependencies)\
\
*   (rstudio-pro#11771) The administrative dashboard now ships Bootstrap 5.1.1, replacing the end-of-life Bootstrap 2.3.2\
*   AgentsView 0.38.1\
*   Copilot Language Server 1.551.2\
*   Electron 43.7.7\
*   Job Launcher Service 2.29.0\
*   Node.js 24.21.0 (GitHub Copilot, Posit Assistant)\
*   PWB Code Server 2026.10-b3210, Code OSS 1.134.0\
*   Posit Assistant for RStudio 1.7.0\
*   rserver-openid 0.9.1\
*   rserver-saml 0.9.3\
\
2026.09.0[](https://docs.posit.co/ide/news/#rstudio-2026.09.0)\
\
---------------------------------------------------------------\
\
**“Autumn Hawkbit”** | Date: 2026-09-10\
\
### New[](https://docs.posit.co/ide/news/#new-1)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-4)\
\
*   ([#18443](https://github.com/rstudio/rstudio/issues/18443)\
    ): Added the `posit-assistant-installation-enabled` session option and the `RSTUDIO_DISABLE_POSIT_ASSISTANT_INSTALLATION` environment variable, which stop users from installing, updating, or uninstalling Posit Assistant. RStudio then runs only the administrator’s installation and makes no update checks.\
*   ([#18687](https://github.com/rstudio/rstudio/issues/18687)\
    ): Added the `posit-assistant-path` session option, for pointing RStudio at an administrator-managed Posit Assistant installation outside the system configuration directory.\
*   ([#18649](https://github.com/rstudio/rstudio/issues/18649)\
    ): Renamed references to the Posit AI service to Posit AI Pass in the IDE user interface.\
*   ([#2129](https://github.com/rstudio/rstudio/issues/2129)\
    ): Added horizontal and vertical split source editor views, with shared edits and independent navigation state.\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-4)\
\
*   (rstudio-pro#12254) Workbench now asks the configured Package Manager instance which Linux distributions it serves binaries for, extending precompiled R package installs beyond the built-in distro list. Workbench falls back to the previous behavior if Package Manager cannot be reached.\
*   (rstudio-pro#12483) Posit Assistant for RStudio is now bundled with Workbench, so RStudio Pro sessions can use it without downloading it first, for example in air-gapped environments.\
*   (rstudio-pro#12534) Added the `assistant-installation-enabled` profile setting, which controls whether users can install and upgrade their own copy of Posit Assistant in RStudio Pro, or are locked to the administrator-managed or bundled copy.\
*   (rstudio-pro#11920) Added a preview “Assistant” page to the new homepage showing your own AI coding activity: session counts, recent sessions, tool and model usage, and cache-efficiency and prompting-quality insights.\
*   (rstudio-pro#12298) Added the `assistant-settings-enforced` and `assistant-settings-default` profile settings, which supply Posit Assistant settings that users respectively cannot and can override.\
*   (rstudio-pro#12297) Added the `ai-providers-default` profile setting, which supplies a starting AI-provider configuration for Posit Assistant that users can override in their own `providers.json`, alongside the existing `ai-providers-enforced` setting that they cannot.\
*   (rstudio-pro#12271) The `ai-providers-enforced` profile setting now applies to RStudio Pro sessions in addition to Positron Pro sessions.\
*   (rstudio-pro#12515) Added a `native-oauth` option to Databricks workspace sections in `databricks.conf`, letting Azure-hosted workspaces opt into the native Databricks OAuth sign-in flow instead of the Microsoft Entra ID flow.\
*   (rstudio-pro#11495) The Available Credentials view in VS Code and Positron Pro sessions now supports Databricks and Snowflake advanced integrations alongside custom OAuth, letting you sign in, activate, switch Snowflake roles, and deactivate these credentials without leaving your session.\
*   (rstudio-pro#12134) Positron Pro session logs now record the Positron version as a single-line JSON record in the same schema as `log-message-format=json`, so log aggregators can index the version fields instead of a multi-line text block.\
*   (rstudio-pro#12101) Added package enumeration to the environment inspection tool, which can now report the packages installed in each R and Python library location it discovers.\
*   (rstudio/launcher#1612) The Kubernetes plugin’s image registry integration now supports AWS Elastic Container Registry (`type: ecr`), authenticating with the launcher’s AWS credential chain.\
*   (rstudio/launcher#1673) The Slurm plugin now skips polling jobs that lack the `[RStudio Launcher]` job-name prefix, avoiding wasted parsing and per-job detail lookups on busy shared clusters.\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-2)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-5)\
\
*   ([#12229](https://github.com/rstudio/rstudio-pro/issues/12229)\
    ): Fixed an issue where the default CRAN repository was configured under Ubuntu `resolute` and Debian `trixie` rather than the Posit Public Package Manager, leading to R package installations building from source.\
*   ([#18668](https://github.com/rstudio/rstudio/issues/18668)\
    ): Expand All now clears nested folds in R Markdown documents after Collapse All.\
*   ([#18683](https://github.com/rstudio/rstudio/issues/18683)\
    ): Fixed intermittent user and group lookup failures on Linux when a remote user directory is slow to respond.\
*   ([#16540](https://github.com/rstudio/rstudio/issues/16540)\
    ): Fixed an issue where opening Find in the visual editor left the search box as it was, rather than filling it with the selected text the way source mode does. A selection made inside a code chunk now seeds the box too, and is what Use Selection for Find looks for there; both previously read the surrounding document selection, which sees a chunk as a single unit.\
*   ([#16540](https://github.com/rstudio/rstudio/issues/16540)\
    ): Fixed an issue where the Find and Add Next and Find All commands did nothing in the visual editor. In prose text, these commands are reported as unavailable rather than silently doing nothing.\
*   ([#16540](https://github.com/rstudio/rstudio/issues/16540)\
    ): Fixed a client error (“Cannot read properties of null”) that could follow a Reload Now of the visual editor after a format change, when the editor’s idle save of the editing location fired before the rebuilt editor existed.\
*   ([#18620](https://github.com/rstudio/rstudio/issues/18620)\
    ): The Data Viewer’s last row is no longer hidden underneath the horizontal scrollbar when scrolled to the bottom.\
*   ([#18139](https://github.com/rstudio/rstudio/issues/18139)\
    ): Fixed Windows locale drift that corrupted non-ASCII Console input and other locale-sensitive operations.\
*   ([#18635](https://github.com/rstudio/rstudio/issues/18635)\
    ): Running code from a popped-out source window no longer moves focus to the console when “Focus console after executing code from the source pane” is off.\
*   ([#18441](https://github.com/rstudio/rstudio/issues/18441)\
    ): The sign-in page and the logged-out dialog now pause polling while their tab is hidden and back off over time, and the dialog offers a “Try again now” button.\
*   ([#18356](https://github.com/rstudio/rstudio/issues/18356)\
    ): Declining the Posit Assistant install prompt now restores the previously selected code assistant.\
*   ([#18631](https://github.com/rstudio/rstudio/issues/18631)\
    ): RStudio Desktop now shows What’s New once per release instead of after every patch update.\
*   ([#18602](https://github.com/rstudio/rstudio/issues/18602)\
    ): Fixed folding and outline hierarchy for section headers decorated with `#` characters.\
*   ([#18597](https://github.com/rstudio/rstudio/issues/18597)\
    ): Posit Assistant code suggestions now honor system-wide installations.\
*   ([#18451](https://github.com/rstudio/rstudio/issues/18451)\
    ): Truncated AI assistant startup errors and logs to avoid dumping minified bundles while retaining useful diagnostics.\
*   ([#18570](https://github.com/rstudio/rstudio/issues/18570)\
    ): Posit Assistant manifest download errors now show the underlying DNS, proxy, or TLS failure.\
*   ([#18610](https://github.com/rstudio/rstudio/issues/18610)\
    ): Posit Assistant install and update downloads now preserve detailed errors, report warning-only failures, and honor configured timeouts.\
*   ([#18531](https://github.com/rstudio/rstudio/issues/18531)\
    ): Fixed breakpoints in methods registered on S7 generics.\
*   ([#18572](https://github.com/rstudio/rstudio/issues/18572)\
    ): Prevented RStudio Server session relaunches from starting duplicate orphaned sessions.\
*   ([#18571](https://github.com/rstudio/rstudio/issues/18571)\
    ): Fixed Posit Assistant chat incorrectly remaining in an “update in progress” state after an R session restart.\
*   ([#18425](https://github.com/rstudio/rstudio/issues/18425)\
    ): Fixed snippet help and insertion errors when the cursor moves between language modes.\
*   ([#18526](https://github.com/rstudio/rstudio/issues/18526)\
    ): Fixed S7 method breakpoints on R versions before 4.3.0 and for package-scoped classes.\
*   ([#18559](https://github.com/rstudio/rstudio/issues/18559)\
    ): The Plots pane now activates after a busy command finishes even when the plot was rendered earlier.\
*   ([#18533](https://github.com/rstudio/rstudio/issues/18533)\
    ): Prevented spurious “Error Listing Objects” dialogs after RStudio Server session restarts.\
*   ([#18527](https://github.com/rstudio/rstudio/issues/18527)\
    ): On Windows, environment variable updates and removals made by RStudio are now visible to R and in-process libraries.\
*   ([#18527](https://github.com/rstudio/rstudio/issues/18527)\
    ): On Windows, sessions started in untrusted directories no longer read user-level `.Renviron` files.\
*   ([#10756](https://github.com/rstudio/rstudio/issues/10756)\
    ): Improved crash reporting and thread safety during session startup.\
*   ([#18507](https://github.com/rstudio/rstudio/issues/18507)\
    ): Reduced macOS file-monitor overload by excluding high-churn and nested-worktree directories, batching events, and debouncing recovery scans.\
*   ([#18493](https://github.com/rstudio/rstudio/issues/18493)\
    ): Fixed invisible checkbox and radio button states in Windows high-contrast dark themes.\
*   ([#18474](https://github.com/rstudio/rstudio/issues/18474)\
    ): Fixed a math-preview keyboard handler leak that consumed subsequent Escape keypresses.\
*   ([#18423](https://github.com/rstudio/rstudio/issues/18423)\
    ): The Data Viewer’s global search no longer re-converts every non-character column to text on each request. Extending a search now refines the previous result instead of rescanning the whole frame.\
*   ([#17806](https://github.com/rstudio/rstudio/issues/17806)\
    ): Improved Data Viewer searching, filtering, scrolling, and Summary panel performance.\
*   ([#17806](https://github.com/rstudio/rstudio/issues/17806)\
    ): Fixed a Data Viewer memory leak when viewed objects change.\
*   ([#18472](https://github.com/rstudio/rstudio/issues/18472)\
    ): Fixed stale syntax highlighting after edits in Markdown and YAML documents.\
*   ([#18447](https://github.com/rstudio/rstudio/issues/18447)\
    ): Console line-navigation shortcuts now move or select to the ends of the whole command instead of the wrapped visual line.\
*   ([#18469](https://github.com/rstudio/rstudio/issues/18469)\
    ): Fixed R raw strings corrupting editor state and breaking later header folds.\
*   ([#18468](https://github.com/rstudio/rstudio/issues/18468)\
    ): Fixed indentation in C++ chunks and formatting of Quarto `#|` comment lines.\
*   ([#18464](https://github.com/rstudio/rstudio/issues/18464)\
    ): Fixed rainbow fenced-div colors to reflect nesting.\
*   ([#18501](https://github.com/rstudio/rstudio/issues/18501)\
    ): Restricted localhost proxy resolution to the requested IP address family.\
*   ([#18444](https://github.com/rstudio/rstudio/issues/18444)\
    ): Fixed repeated pane-layout collapse caused by stale zoom state.\
*   ([#18448](https://github.com/rstudio/rstudio/issues/18448)\
    ): Fixed pane zoom state after column, sidebar, source-column, and pane-size changes.\
*   ([#18482](https://github.com/rstudio/rstudio/issues/18482)\
    ): Prevented spurious Windows crash reports when closing an R session with a running terminal.\
*   ([#18546](https://github.com/rstudio/rstudio/issues/18546)\
    ): RStudio Server’s localhost proxy now streams response bodies instead of buffering them in memory.\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-5)\
\
*   (rstudio-pro#12127) Fixed `RS_SERVER_URL` being blank in RStudio Pro sessions.\
*   (rstudio-pro#12051) Fixed `rserver` logging normal status messages from subprocesses like `rserver-launcher` as ERROR instead of their actual log level.\
*   (rstudio-pro#11957) Fixed the “Last-used” image tag in the homepage session launcher never updating after starting a session. The last-used image is now remembered separately for each workbench, so one workbench’s image choice no longer appears as the last-used image for another. Any previously remembered image is cleared once when upgrading.\
*   (rstudio-pro#12300) Fixed default `extensions.autoUpdate` setting for VS Code and Positron sessions to match Code OSS’s updated setting type.\
*   (rstudio-pro#12101) Fixed environment inspection finding no R installations when no R search paths were configured.\
*   (rstudio-pro#12101) Fixed audited job environment summaries recording R package names as row numbers when the same package was installed in more than one library on the search path, which is the usual case when a user library shadows the site library.\
*   (rstudio-pro#12101) Fixed audited job environment summaries truncating R library paths that contain spaces.\
*   (rstudio-pro#12208) Fixed an issue with parsing HTTP POST requests that do not comply with RFC 1341.\
*   (rstudio-pro#12503) Fixed login hangs with new users logging in with just in time user provisioning.\
*   (rstudio-pro#12441) Fixed intermittent errors from user database lookups tied to slow user directory requests.\
*   (rstudio/launcher#1647) Fixed a slow or stuck Job Launcher plugin restart freezing API requests for other clusters.\
*   (rstudio/launcher#1683) Fixed a Job Launcher heartbeat-timer race that could count phantom missed heartbeats under heavy load and spuriously restart healthy plugins.\
*   (rstudio/launcher#1692) Fixed Kubernetes API requests that never complete (for example, silently dropped connections from NAT idle timeouts) permanently consuming request queue slots.\
*   (rstudio/launcher#1666) A missing Slurm CLI (for example, a wrong or unmounted `slurm-bin-path`) now reports a command-not-found error with configuration guidance instead of a generic unknown Slurm error.\
*   (rstudio/launcher#1666) The Job Launcher now logs rsandbox validation failures at startup as warnings, including rsandbox’s output and a `CAP_SYS_ADMIN` hint for unprivileged containers, and includes them in Slurm plugin startup errors.\
*   (rstudio/launcher#1699) The Kubernetes plugin now logs unparsable third-party Jobs in shared namespaces at warning level instead of error, reducing log noise.\
\
### Deprecated / Removed[](https://docs.posit.co/ide/news/#deprecated-removed-1)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-6)\
\
*   ([#18605](https://github.com/rstudio/rstudio/issues/18605)\
    ): Marked RPubs and ShinyApps.io publishing destinations as deprecated ahead of their sunset; see [the migration guide](https://posit.co/blog/migrating-connect-cloud-posits-unified-publishing-solution)\
    .\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-6)\
\
*   The Slurm plugin no longer recognizes jobs that pre-2020 Launcher versions submitted with base64-encoded job names.\
\
### Upgrade Instructions[](https://docs.posit.co/ide/news/#upgrade-instructions-1)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-7)\
\
*   If you set `posit-assistant-path`, check that it points at a valid Posit Assistant installation. The search now ends if it does not find a valid installation, and RStudio reports Posit Assistant as not installed rather than falling back to the copy bundled with Workbench.\
*   If you set `posit-assistant-installation-enabled=0`, users who had already installed Posit Assistant themselves are switched to the administrator-managed or bundled copy, which might be an older version. Their own copy is ignored, not removed.\
*   If you enforce `extensions.autoUpdate` for Positron Pro or VS Code sessions (e.g., via `positron-enforced-settings`), update it from the boolean `false` to the string `"off"`. Code OSS 1.130.0 changed this setting from a boolean to a string enum, so a boolean value is no longer valid and the enforced setting will silently stop applying, falling back to Code OSS’s new default of `"on"`.\
\
### Dependencies[](https://docs.posit.co/ide/news/#dependencies-1)\
\
*   Copilot Language Server 1.531.0\
*   Electron 42.11.1\
*   Job Launcher Service 2.28.0-615\
*   Node.js 22.23.2 (GitHub Copilot, Posit Assistant)\
*   PWB Code Server 2026.09-b3134, Code OSS 1.130.0\
*   Posit Assistant for RStudio 1.3.0\
*   Positron 2026.09.0-150\
*   Quarto 1.10.18\
\
2026.08.2[](https://docs.posit.co/ide/news/#rstudio-2026.08.2)\
\
---------------------------------------------------------------\
\
**“Yellow Yarrow”** | Date: 2026-08-25\
\
### Dependencies[](https://docs.posit.co/ide/news/#dependencies-2)\
\
*   Positron 2026.08.2-4\
\
2026.08.1[](https://docs.posit.co/ide/news/#rstudio-2026.08.1)\
\
---------------------------------------------------------------\
\
**“Yellow Yarrow”** | Date: 2026-08-18\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2026.08.1-fixed)\
\
*   ([#18551](https://github.com/rstudio/rstudio/issues/18551)\
    ): Fixed an issue introduced in RStudio 2026.08.0 where LaTeX math failed to render in the visual editor: equations appeared blank or invisible, switching to visual mode could unexpectedly modify math text in the document, and after visiting visual mode, inline math previews in the source editor could also stop appearing for the remainder of the session.\
*   ([#18515](https://github.com/rstudio/rstudio/issues/18515)\
    ): Fixed an issue on Windows where the 32-bit session binaries were missing from the installer, so RStudio Desktop failed to start a session when a 32-bit R installation was selected. The binaries were built and code-signed, but were dropped before packaging.\
*   ([#18512](https://github.com/rstudio/rstudio/issues/18512)\
    ): Fixed an issue on Windows where `rsession.dll` was shipped without a code signature. The signed `rsession.exe` and `rsession-utf8.exe` are thin launcher stubs, so nearly all of the R session implementation lives in that DLL; policies that verify every loaded module rather than only the launching executable could block or flag it.\
\
2026.08.0[](https://docs.posit.co/ide/news/#rstudio-2026.08.0)\
\
---------------------------------------------------------------\
\
**“Yellow Yarrow”** | Date: 2026-08-13\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2026.08.0-new)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-7)\
\
*   ([#1634](https://github.com/rstudio/rstudio/issues/1634)\
    ): The Windows installer now lets you choose between installing for all users (the default, which prompts for administrator rights) and installing for the current user only (no administrator rights required). A current-user install no longer prompts for elevation, and uninstalling one now removes its files, Start Menu shortcut, and registry entries cleanly. Note for automated deployments: silent installs must now specify the install mode. A bare `/S` exits with an error, so pass `/allusers /S` (the previous behavior) or `/currentuser /S`.\
*   ([#18153](https://github.com/rstudio/rstudio/issues/18153)\
    ): Added a preference (General > Basic) to disable the “What’s New” window that RStudio Desktop shows after updating to a new version.\
*   ([#18158](https://github.com/rstudio/rstudio/issues/18158)\
    ): On macOS, the Files pane now follows Finder aliases: clicking an alias to a folder navigates to that folder, and clicking an alias to a file opens the file. The File and Folder Open dialogs follow aliases as well.\
*   ([#9924](https://github.com/rstudio/rstudio/issues/9924)\
    ): The Files pane now shows a link indicator on symbolic links and macOS Finder aliases, with the link target shown in the icon’s tooltip.\
*   ([#18274](https://github.com/rstudio/rstudio/issues/18274)\
    ): On Windows, the Files pane now follows .lnk shortcuts: clicking a shortcut to a folder navigates to that folder, and clicking a shortcut to a file opens the file. The File and Folder Open dialogs follow shortcuts as well. Shortcuts are marked with a link indicator, like symbolic links and macOS Finder aliases.\
*   ([#8715](https://github.com/rstudio/rstudio/issues/8715)\
    ): Inline LaTeX / math previews in the source editor and visual editor are now rendered with MathJax 4 (previously MathJax 2.7), adding support for the TeX input extensions introduced in MathJax 3 and later. Rendered R Markdown documents using `mathjax = "local"` continue to use the bundled MathJax 2.7.\
*   ([#7350](https://github.com/rstudio/rstudio/issues/7350)\
    ): RStudio can now load custom Vim key mappings from `~/.rstudio-vimrc` (or `~/.vimrc`) when Vim editor keybindings are in use. Enable the new preference under Tools > Global Options > Code > Editing. Key mapping commands (`map`, `noremap`, `unmap`, and friends) and `set` commands supported by the editor’s Vim emulation are applied, and other vimrc content is ignored.\
*   ([#18060](https://github.com/rstudio/rstudio/issues/18060)\
    ): The installed-package scan used to track package load and attach events now runs on a background thread, so session startup (and package installation) no longer blocks while enumerating library paths on slow or remote filesystems.\
*   ([#18248](https://github.com/rstudio/rstudio/issues/18248)\
    ): RStudio can now be built without Posit Assistant support (including its chat pane and Posit AI Next Edit Suggestions) via the new `RSTUDIO_ENABLE_POSIT_ASSISTANT` CMake option; GitHub Copilot, including Copilot-provided suggestions, remains available. A new `RSTUDIO_ENABLE_AI_FEATURES` master option removes all AI features (GitHub Copilot and Posit Assistant) from the build when disabled.\
*   ([#18330](https://github.com/rstudio/rstudio/pull/18330)\
    ): RStudio Server now verifies that the localhost port targeted by a proxied request (a `/p/` or `/p6/` URL) is owned by the requesting user, and denies the request with HTTP 403 Forbidden otherwise. Localhost services owned by other users, including root-owned listeners such as ports published by rootful Docker or system services, are no longer reachable through the session proxy by default. A new rserver.conf configuration option, `www-proxy-localhost-verify-port-owner=false`, can be set to restore the original behavior. On systems where the kernel’s `NETLINK_SOCK_DIAG` facility is unavailable, a warning is logged and the previous behavior is retained. _With thanks to Luiz Felipe Mol (Paldata S.A.)_\
*   ([#18253](https://github.com/rstudio/rstudio/issues/18253)\
    ): Added a “Check for Posit Assistant updates” command to the Help menu. It always reports its result in a dialog: whether Posit Assistant is up to date, an update is available (with the option to install it), or a newer Posit Assistant requires a newer version of RStudio.\
*   ([#12806](https://github.com/rstudio/rstudio/issues/12806)\
    ): On Windows, the R session is now long-path aware, so R can read and write paths longer than the traditional 260-character limit (for example, files in deeply nested project libraries created by `renv`). R has supported long paths since R 4.3.0, but the opt-in applies per process. RStudio runs R in its own, so it previously had no effect in the IDE. This requires Windows 10 version 1607 or later with the `LongPathsEnabled` registry value set, which is off by default. A project whose own directory exceeds 260 characters remains unsupported, because Windows cannot launch child processes (Git, terminals, builds) from a working directory that long.\
*   ([rstudio/rstudio-pro#10794](https://github.com/rstudio/rstudio-pro/issues/10794)\
    ): Added support for Ubuntu Linux 26 (Resolute Raccoon) as an install target for RStudio Desktop and RStudio Server.\
*   ([#18437](https://github.com/rstudio/rstudio/issues/18437)\
    ): Edit suggestion previews (Copilot / Posit AI next edit suggestions, and suggestions shown through the RStudio API) now highlight changes at the word level. For example, renaming a variable marks the old and new words cleanly instead of showing interleaved character fragments. The previous character-level highlighting can be restored with the new “Highlight changes in edit suggestions by” preference, shown in Tools > Global Options > Assistant when an assistant is enabled, or by setting `edit_suggestion_diff_granularity` to `"character"` in rstudio-prefs.json.\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-8)\
\
*   (rstudio-pro#11715) Added a `login` home-directory creation mode that provisions a user’s home directory via a short-lived elevated job at sign-in.\
*   (rstudio-pro#11715) Rootless Kubernetes deployments are now generally available and no longer a preview feature.\
*   (rstudio-pro#11147): The Job Launcher session and Positron init containers now default to the `posit/workbench-*-init` images with version-only tags.\
*   (rstudio-pro#9113) Custom OAuth integrations are now applied when the server is reloaded, without requiring a full restart.\
*   (rstudio-pro#9113) Invalid Databricks or Snowflake integration configuration no longer prevents Workbench from starting. The affected integration is disabled and the error is logged instead.\
*   (rstudio/launcher#1626): The Kubernetes plugin’s `Container` job-submission schema now accepts a `capabilitiesDrop` list, which the plugin renders as the container-level `securityContext.capabilities.drop`. Combined with `capabilitiesAdd` (for example, drop `ALL` and add `CHOWN`/`DAC_OVERRIDE`), this allows running a non-root container with a tightly-scoped capability set.\
*   (rstudio/launcher#1596): The Kubernetes plugin now automatically provisions dynamic image registry pull secrets for templated jobs (`use-templating=1`), including customized job templates.\
*   (rstudio/launcher#1561): The Slurm plugin adds an opt-in `profile-merge-fields` option to union-merge `allowed-partitions` and `resource-profiles` across resource profile levels instead of using only the last match. This deprecates the `singularity-image-directory-mode` option in favor of `profile-merge-fields`.\
*   (rstudio/launcher#1645): The Job Launcher now logs its effective resource limits (`RLIMIT_NOFILE`, `RLIMIT_NPROC`, `RLIMIT_CORE`) at startup and warns when the number of open file descriptors approaches the soft `RLIMIT_NOFILE` limit.\
*   (rstudio-pro#11844) Administrators can supply a base AI-provider configuration (in the `providers.json` schema) for Posit Assistant in Positron Pro sessions with the `ai-providers-enforced` profile setting in `/etc/rstudio/profiles`. The setting points at a JSON file forwarded to sessions and can be scoped globally, per group, or per user.\
*   (rstudio-pro#10794): Added support for Ubuntu Linux 26 (Resolute Raccoon) as an install target for Posit Workbench, RStudio Desktop Pro, and the bundled session components, on both x86-64 and ARM (aarch64).\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2026.08.0-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-8)\
\
*   ([#13605](https://github.com/rstudio/rstudio/issues/13605)\
    ): Fixed an issue where a source editor tab could become permanently inoperable (for example, mouse text selection not working, typed input silently discarded, multi-cursor editing stuck, and editor shortcuts landing in a different tab) until the IDE was reloaded. An error raised while editing with multiple cursors could leave the editor’s selection machinery in a corrupt state. That state is now restored when the error occurs, and editors additionally detect and repair leftover corruption when their tab is activated or focused.\
*   ([#18394](https://github.com/rstudio/rstudio/issues/18394)\
    ): Fixed a hang when switching or closing projects (and restarting R) while the Posit Assistant chat backend or code assistant agent was running. The session’s shutdown wait could dispatch unrelated background work mid-teardown and block indefinitely, leaving the window stuck on the old, dead session. An assistant process that ignores the shutdown request is now also force-killed instead of being left running. RStudio Desktop shows the session error page when the replacement session fails to start during a project switch instead of hanging silently.\
*   ([#12806](https://github.com/rstudio/rstudio/issues/12806)\
    ): Shortened the temporary file names used while executing an R Notebook chunk, which frees up about 24 characters of path length. Plotting from a notebook in a deeply nested project on Windows could previously fail with a “cannot open the connection” error; this makes it work without needing long paths enabled.\
*   ([#18391](https://github.com/rstudio/rstudio/issues/18391)\
    ): Fixed RStudio Desktop error logging that reported `TypeError: Cannot read properties of undefined (reading 'logErrorAtLevel')` in place of the actual error when a background operation failed. Closing the main window after its renderer has crashed now also exits RStudio instead of leaving a headless process running.\
*   ([#18152](https://github.com/rstudio/rstudio/issues/18152)\
    ): Fixed a compilation error when building RStudio Server against SOCI 4.1.4 or newer.\
*   ([#18287](https://github.com/rstudio/rstudio/issues/18287)\
    ): Fixed another compilation error when building RStudio against system SOCI packages (4.1 or newer), which no longer expose the SQLite C API through their headers.\
*   ([#18174](https://github.com/rstudio/rstudio/issues/18174)\
    ): Fixed an error when viewing an object from the Object Explorer with the French user interface language enabled.\
*   ([#18255](https://github.com/rstudio/rstudio/issues/18255)\
    ): Fixed a regression where an unprivileged RStudio Server would fail to start when it could not read a system secure key file (for example, a root-owned key baked into an HPC container image), rather than falling back to its per-user cache.\
*   ([#18198](https://github.com/rstudio/rstudio/issues/18198)\
    ): Fixed tar errors and warnings printed to the console after installing a package from a URL with `install.packages(..., repos = NULL)`.\
*   ([#18197](https://github.com/rstudio/rstudio/issues/18197)\
    ): Fixed an issue where the Render button failed to render a Quarto document living within a sub-directory of a Quarto project.\
*   ([#18208](https://github.com/rstudio/rstudio/issues/18208)\
    ): Fixed an issue in RStudio Server where requests could fail with “Unable to connect to service” for 30 seconds or more while a suspended session was relaunching.\
*   ([#18179](https://github.com/rstudio/rstudio/issues/18179)\
    ): RStudio Desktop now shows an error dialog at startup when folders it needs to write (for example, `~/.local/share/rstudio`) cannot be created or written, instead of failing silently, and log messages now fall back to stderr when the log directory is not writable.\
*   ([#17650](https://github.com/rstudio/rstudio/issues/17650)\
    ): Fixed unreadable label text in dark modal dialogs when using third-party themes (for example, rsthemes) that style dialog labels for light backgrounds.\
*   ([#17191](https://github.com/rstudio/rstudio/issues/17191)\
    ): Fixed per-session memory limits not being enforced for Workbench sessions running in a container with a read-only cgroup filesystem, and made the memory gauge, memory-usage report, and abort gate reflect the container rather than the host. Added an `rsession.conf` `memory-usage-mode` option to control how session and total memory usage are computed and reported.\
*   ([#18225](https://github.com/rstudio/rstudio/issues/18225)\
    ): Clicking a console hyperlink to a package source file that no longer exists (for example, srcref paths recording the temporary directory used during package installation) now recovers the source from the package’s srcref database when available, instead of showing a “No such file” error.\
*   ([#13078](https://github.com/rstudio/rstudio/issues/13078)\
    ): Fixed an issue on Windows where `utils::choose.dir()` returned `NA` without showing the folder-selection dialog when running R 4.3.0 or newer.\
*   ([#17608](https://github.com/rstudio/rstudio/issues/17608)\
    ): Switching between editor tabs no longer blocks the session on GitHub Copilot / Posit Assistant work: the document-focus notification no longer reads document contents from disk, no longer tries to launch the assistant agent (previously up to a 10-second stall per focus when the agent failed to start), and no longer holds up subsequent requests while it completes. Also removed a stray 25ms pause from every source-document metadata read.\
*   ([#18317](https://github.com/rstudio/rstudio/issues/18317)\
    ): Fixed spurious `.mapply` warnings (“longer argument not a multiple of length of shorter”) printed to the console after creating or modifying a data.table with more than 50 columns (for example, via `data.table::setDT()`). Also fixed the same class of bug in R Notebook chunk output, where a data.table with more columns than `cols.max.print` (default 1000) was rendered as a single column of integers instead of the table’s leading columns.\
*   ([#18271](https://github.com/rstudio/rstudio/issues/18271)\
    ): Updating or uninstalling Posit Assistant while another RStudio session for the same user is running it could corrupt or break the shared installation. These operations are now coordinated across sessions: they are refused with a clear message while another session is using or updating Posit Assistant, and Posit Assistant will not start while an update is in progress elsewhere.\
*   ([#18199](https://github.com/rstudio/rstudio/issues/18199)\
    ): RStudio no longer prompts to install packages that are no longer dependencies of rmarkdown (e.g. stringr, glue) when rendering R Markdown or Quarto documents, most visibly in renv projects with minimal project libraries. Required packages are now validated against the dependencies declared by the installed packages themselves, rather than a hard-coded dependency tree.\
*   ([#18257](https://github.com/rstudio/rstudio/issues/18257)\
    ): Fixed the IDE becoming unresponsive for an extended period after a large number of git-tracked files changed at once (e.g. moving or committing thousands of files); Git pane updates are now batched instead of rebuilding the changelist once per changed file.\
*   ([#18260](https://github.com/rstudio/rstudio/issues/18260)\
    ): Fixed an issue on macOS where a file change landing just after a bulk change of many files could go undetected by the Files and Git panes until a manual refresh or unrelated later file activity.\
*   ([#18273](https://github.com/rstudio/rstudio/issues/18273)\
    ): Fixed an issue on Windows where a failure to load the Start Menu Git shortcut while auto-detecting the Git installation went undetected, causing detection to fail later with a less accurate error.\
*   ([#18277](https://github.com/rstudio/rstudio/issues/18277)\
    ): Fixed an issue where the GitHub Copilot or Posit Assistant agent could fail to start for the rest of the session after an early startup failure (for example, a misconfigured Node.js path). The agent now retries and starts once the underlying problem is corrected, without restarting the session.\
*   ([#18270](https://github.com/rstudio/rstudio/issues/18270)\
    ): Fixed an issue on Windows where native dialogs shown by R (e.g. via `utils::askYesNo()`, or when `install.packages()` asks about installing from sources) could open behind the RStudio Desktop window, making the IDE appear frozen while R waited on a dialog the user could not see.\
*   ([#8345](https://github.com/rstudio/rstudio/issues/8345)\
    ): Help pages opened via the Help pane’s “Show in new window” button now follow the IDE’s editor theme, instead of always rendering with a light palette.\
*   ([#18305](https://github.com/rstudio/rstudio/issues/18305)\
    ): The first run of a new RStudio build now always checks for Posit Assistant updates, instead of the check being suppressed for up to the update-check interval (two hours by default) when the previous build had checked recently.\
*   ([#18326](https://github.com/rstudio/rstudio/issues/18326)\
    ): Fixed an issue where “Restart R and Run All Chunks” (and “Restart R and Clear Output”) could intermittently restart R without then running the chunks (or clearing the output).\
*   ([#18315](https://github.com/rstudio/rstudio/issues/18315)\
    ): Fixed the GitHub Copilot section of the Assistant preferences showing a mislabeled “Display account and billing messages from Posit Assistant” checkbox that had no effect. It is now correctly labeled for GitHub Copilot and controls whether Copilot’s account and billing messages are shown.\
*   ([#18350](https://github.com/rstudio/rstudio/issues/18350)\
    ): Fixed an issue where selecting a Posit Assistant code assistant or chat provider and confirming Global Options before its install/update check finished could leave the provider selected but never installed, with completions silently unavailable. The dialog’s OK button now waits for the check to finish, so the install prompt is not skipped.\
*   ([#18398](https://github.com/rstudio/rstudio/issues/18398)\
    ): Fixed an issue where the R session could spin at 100% CPU, flooding its logs with “system error 5 (Input/output error)” messages, after the terminal it was launched from went away while stderr logging was enabled.\
*   ([#18340](https://github.com/rstudio/rstudio/issues/18340)\
    ): Fixed an issue in RStudio Server where the IDE could stop receiving updates from the session after an R session restart until the user’s next interaction.\
*   ([#12572](https://github.com/rstudio/rstudio/issues/12572)\
    ): The macOS `diagnostics` and `rpostback` helper binaries are now universal (Apple Silicon + Intel). RStudio no longer prompts to install Rosetta 2 at startup on Apple Silicon.\
*   ([#9026](https://github.com/rstudio/rstudio/issues/9026)\
    ): The Review Changes window (Git and SVN commit and history) now follows the active theme, instead of always rendering with a light palette. The changelist and diff panes use the editor theme, as they do in the Git pane. The file lists in the Review Changes window and in the Git and SVN panes also show a “No changes” placeholder when there is nothing to review, instead of appearing blank.\
*   ([#18194](https://github.com/rstudio/rstudio/issues/18194)\
    ): The terminal buffer returned by `rstudioapi::terminalBuffer()` and by the “Copy Terminal to Editor” command no longer contains OSC escape sequences and their payloads. Escape sequences that fall outside the previously recognized forms (for example, colon-separated color codes (`ESC[38:5:196m`), bracketed-paste markers, and the window-title sequences emitted by GNU screen and tmux) are now also stripped instead of leaving fragments of their parameters or payloads behind.\
*   ([#18393](https://github.com/rstudio/rstudio/issues/18393)\
    ): Fixed an issue where a Terminal tab stopped displaying typed input and shell output for the rest of its life after losing its WebGL context (for example, after a GPU crash, a graphics driver reset, or too many open WebGL-rendered terminals). The terminal now falls back to the DOM renderer and keeps rendering.\
*   ([#18378](https://github.com/rstudio/rstudio/issues/18378)\
    ): Fixed an issue in the Data Viewer where jumping to the bottom with End or Ctrl+End stopped short, leaving the last row partly hidden below the bottom edge, on platforms whose user-interface font renders taller than expected (Windows, and Linux distributions such as Fedora and RHEL 10 that default to Noto Sans).\
*   ([#18434](https://github.com/rstudio/rstudio/pull/18434)\
    ): Hardened the session against background-thread use of the R runtime. R function invocations made off the main thread are now refused, and log an error, instead of racing the R interpreter (a potential cause of memory corruption and crashes).\
*   ([#18382](https://github.com/rstudio/rstudio/issues/18382)\
    ): Fixed an intermittent “Error restoring session (console\_actions): An error occurred while parsing json” error when resuming a session whose console output contained multi-byte (e.g. Unicode block or CJK) characters. Console output is no longer split mid-character when the console replay (the `console_actions` session state file) is saved. Raw output bytes that are not valid UTF-8 (e.g. from `cat("\xff")`) are now replaced with `?` in the restored console. A saved `console_actions` file that fails to parse anyway (for example, one written by a build without this fix) is now discarded with a logged warning instead of failing session restore.\
*   ([#18414](https://github.com/rstudio/rstudio/issues/18414)\
    ): Fixed an issue on Windows where an R session launched with a console attached and stderr logging enabled could flood its logs at full CPU speed if the console later became unwritable; console echo failures and output-capture read errors are now logged once instead of unboundedly.\
*   ([#18430](https://github.com/rstudio/rstudio/issues/18430)\
    ): Fixed an issue on Windows where child processes could outlive an R session that had been started inside another job object. An inverted error check reported the failed kill-on-close job assignment as success, so the session ran unprotected and the intended recovery (relaunching detached from the confining job) never ran. Job setup failures are now also logged once the session’s logging is available.\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-9)\
\
*   (rstudio-pro#11714) Fixed startup failure when `launcher.pem` was made group-readable by a Kubernetes `fsGroup`; group-read is now accepted when the file’s group matches a group of the server process.\
*   (rstudio-pro#11351) Fixed misleading `database.conf` permission warnings at startup when the file is mounted read-only, such as from a Kubernetes secret.\
*   (rstudio-pro#11266): Fixed an “Error launching session” (HTTP 500) when launching a new session from the homepage for a project stored on a filesystem mounted only on Slurm or Kubernetes compute nodes and not on the Workbench host.\
*   (rstudio-pro#11960): Fixed VS Code and Positron sessions failing to save project metadata and send session heartbeat updates when the server uses file-based session storage.\
*   (rstudio-pro#11824): Fixed in-session sign-in failing in VS Code and Positron sessions for custom OAuth integrations whose `client_id` contains a `+` character.\
*   (rstudio-pro#11823): Fixed sessions in some container environments (such as OpenShift) failing to connect after launch, showing a client initialization or “version mismatch” error.\
*   (rstudio-pro#11756): Fixed the Job Launcher being silently disabled some hours after a restart when the license verify file was not readable by the server user.\
*   (rstudio-pro#11830): Fixed bottleneck with user-provisioning when the database has lots of users, and new users were being added quickly.\
*   (rstudio-pro#11713) Rootless (NSS mode) launcher sessions no longer grant the session user the Workbench service account’s group.\
*   (rstudio-pro#11167): Fixed bug that allowed a query-param bypass of audit download events. Added `track-resource-downloads=1` option to rsession.conf to allow audit events for non-system resource downloads made by RStudio to prevent HTTP header bypass.\
*   (rstudio-pro#9652): Fixed consistency of RStudio project sharing links so they both work more reliably, and guide the user into a session with that project (i.e., join an existing one, resume one that is suspended, or start a new one).\
*   (rstudio-pro#11884): Hardened request handling in the session storage API.\
*   (rstudio-pro#11886): Hardened request handling in the session metadata API.\
*   (rstudio-pro#12001): Strengthened protection for stored integration credentials (OAuth2).\
*   (rstudio-pro#11999): Hardened internal handling in load balancer configuration and node management.\
*   (rstudio-pro#12000): Improved database initialization tooling.\
*   (rstudio/launcher#1533): Kubernetes session control operations that fail due to a missing Kubernetes permission (such as `pods/exec`) now report the operation and the missing permission instead of a generic error.\
*   (rstudio/launcher#1609): The Kubernetes plugin now reports a job’s termination reason (such as `OOMKilled`) in the job’s status message instead of only a generic exit code, matching the Slurm plugin’s wording.\
*   (rstudio/launcher#1635): Fixed an error in the Kubernetes plugin’s job-status watch that, under load, could tear down the watch and flood the Kubernetes API server with reconnect attempts.\
\
### Deprecated / Removed[](https://docs.posit.co/ide/news/#rstudio-2026.08.0-deprecated)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-9)\
\
*   ([rstudio/rstudio-pro#12259](https://github.com/rstudio/rstudio-pro/issues/12259)\
    ): Discontinued support for Debian 12 for RStudio Desktop and RStudio Server.\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-10)\
\
*   (rstudio-pro#12259): Discontinued support for Debian 12 for Posit Workbench, RStudio Desktop Pro, and the bundled session components.\
\
### Upgrade Instructions[](https://docs.posit.co/ide/news/#rstudio-2026.08.0-upgrade)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-11)\
\
*   The Positron migration to the `providers.json` schema intentionally drops the `positron.assistant.models.include` setting (posit-dev/positron#14928). If you enforced it through `positron-enforced-settings`, it no longer restricts the models offered to Posit Assistant, leaving a gap in model enforcement. To restore the restriction, migrate to the `ai-providers-enforced` setting in `/etc/rstudio/profiles`, which points at a `providers.json` file. That schema matches models by exact name rather than by glob, so enumerate each model in the allow list. See [AI Provider Admin Controls](https://docs.posit.co/ide/server-pro/admin/ai/ai-provider-controls.html)\
     for details.\
\
### Dependencies[](https://docs.posit.co/ide/news/#rstudio-2026.08.0-dependencies)\
\
*   Copilot Language Server 1.520.0\
*   Electron 42.7.1\
*   Job Launcher Service 2.27.1-596\
*   MathJax 4.1.3 (inline LaTeX / math previews)\
*   PWB Code Server 2026.08-b2942, Code OSS 1.124.0\
*   nginx 1.30.4\
*   Positron 2026.08.0-331\
\
2026.07.1[](https://docs.posit.co/ide/news/#rstudio-2026.07.1)\
\
---------------------------------------------------------------\
\
**“Pacific Dogwood”** | Date: 2026-07-21\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2026.07.1-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-10)\
\
*   ([#18230](https://github.com/rstudio/rstudio/issues/18230)\
    ): Fixed an error printed to the console after evaluating an expression containing a `[` subset with an empty argument (e.g. `mtcars[, 1:3]`).\
*   ([#18221](https://github.com/rstudio/rstudio/issues/18221)\
    ): Fixed an issue on Windows where scrolling the Data Viewer with the mouse wheel could get stuck when the pointer was over the table body.\
*   ([#18215](https://github.com/rstudio/rstudio/issues/18215)\
    ): Fixed an issue where the Data Viewer could lose its scroll position, or render an empty grid, after switching to another tab and back.\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-12)\
\
*   (rstudio-pro#11381): Fixed an authorization error when removing a project on the homepage when using a Basic-tier license.\
*   (rstudio-pro#11333): Fixed an issue when using database session metadata (`session-use-file-storage=0`) where use of VS Code/Positron would cause invalid RStudio sessions to be migrated into the homepage the first login after a restart.\
\
### Dependencies[](https://docs.posit.co/ide/news/#rstudio-2026.07.1-dependencies)\
\
*   Ace 1.43.5\
*   Copilot Language Server 1.509.1\
*   Electron 41.9.0\
*   Node.js 22.22.2 (copilot, Posit Assistant)\
*   Quarto 1.9.38\
*   xterm.js 6.0.0\
\
2026.07.0[](https://docs.posit.co/ide/news/#rstudio-2026.07.0)\
\
---------------------------------------------------------------\
\
**“Pacific Dogwood”** | Date: 2026-07-14\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2026.07.0-new)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-11)\
\
*   ([#5908](https://github.com/rstudio/rstudio/issues/5908)\
    ): Dates and times (such as the Files pane Modified column) are now formatted according to the system region by default, rather than always using a US-style format. A new settings menu on the Files pane toolbar adds options to use ISO-8601 formatting or the UTC time zone instead.\
*   ([#18077](https://github.com/rstudio/rstudio/issues/18077)\
    ): The Quarto Document dialog now offers separate PDF (Typst) and PDF (LaTeX) output options. Typst is bundled with Quarto and requires no additional software.\
*   ([#18020](https://github.com/rstudio/rstudio/pull/18020)\
    ): Added `rserver --check-config` (and the `rstudio-server check-config` admin subcommand) to validate the configuration file without starting the service, reporting all unrecognized options in a single pass. `--test-config` is now a deprecated alias for `--check-config` with the same behavior; it previously stopped at the first unrecognized option. Using `--test-config` prints a deprecation warning, and it will be removed in a future release. `--check-config` now also validates that configured file paths (secure-cookie-key-file, rsession-config-file, database-config-file) exist on disk, and reports the detected R installation (informational). In Posit Workbench builds, the check also covers database connectivity and license status.\
*   ([#17992](https://github.com/rstudio/rstudio/issues/17992)\
    ): The Find in Files replace preview and Replace All results no longer present matches whose proposed replacement is identical to the matched text. Lines that would be unchanged are omitted entirely.\
*   ([#15830](https://github.com/rstudio/rstudio/issues/15830)\
    ): Added a Code menu and command-palette entry to re-enable the editor’s missing-package banner for a file after dismissing it. Updated the banner’s dismissal label to “Don’t show for this file” to make the per-file scope explicit.\
*   ([#11198](https://github.com/rstudio/rstudio-pro/issues/11198)\
    ): The session launcher is now a full-screen, multi-step workflow (Session / IDE, Integrations, Environment) with IDE cards, step-preserving close/reopen, and a Launch Session action on the Environment step.\
*   ([#10417](https://github.com/rstudio/rstudio/issues/10417)\
    ): RStudio can now reduce background file operations (recursive file monitoring, code indexing, and external-edit checks) for projects located on network or remote filesystems, improving responsiveness on slow storage. This applies automatically when a remote filesystem is detected, and can be configured globally (Tools > Global Options > General > Advanced) or overridden per-project (Project Options > General).\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-13)\
\
*   (rstudio-pro#11596): Added default Local Job Launcher resource profiles to new Workbench installations.\
*   (rstudio-pro#10826): Added support for applying `/etc/rstudio/profiles` changes with `rstudio-server reload` (SIGHUP) without restarting Workbench. See [Applying profile changes](https://docs.posit.co/ide/server-pro/admin/rstudio_pro_sessions/user_and_group_profiles.html#applying-profile-changes)\
     in the Admin Guide for more information on how profiles configuration changes are applied on reload.\
*   (rstudio-pro#11502): Posit Workbench’s `rserver --check-config` now also reports the audit database configuration and configured SSL certificate paths, alongside the database-connectivity and license checks. All of these overlay checks are informational and never cause the check to fail, so the command can be run before the database, license, or certificates are in place.\
*   (rstudio/launcher#1576): The Slurm plugin now supports Slurm 26.05.\
*   (rstudio/launcher#1593): The Kubernetes plugin can now discover session images from a configured registry via the new `launcher.kubernetes.images.conf` file, with automatic image pull secret provisioning for discovered images. See [Image registry](https://docs.posit.co/ide/server-pro/admin/job_launcher/kubernetes_plugin.html#kube-image-registry)\
     in the Admin Guide.\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2026.07.0-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-12)\
\
*   ([#18148](https://github.com/rstudio/rstudio/issues/18148)\
    ): Fixed the editor’s missing-packages banner sometimes failing to reappear when “Toggle Detect Missing Packages” was used to re-enable it after a per-file dismissal. Package discovery could race with the dismissal property being cleared, silently suppressing the banner.\
*   ([#18145](https://github.com/rstudio/rstudio/issues/18145)\
    ): Fixed the visual editor hanging at its loading spinner for every subsequently opened document after a visual-mode document (for example, a freshly created Quarto document) was closed while its Markdown conversion was still in flight. Fixed an `IndexOutOfBoundsException` when a Markdown conversion completed after the tab was closed.\
*   ([#18138](https://github.com/rstudio/rstudio/issues/18138)\
    ): Fixed `View()` failing with `'length = 2' in coercion to 'logical(1)'` for objects containing a component whose class provides a `length()` method returning more than one value (for example, the `Formula` objects stored in `mlogit` models). The Object Explorer now uses the internal length when inspecting such objects.\
*   ([#18134](https://github.com/rstudio/rstudio/issues/18134)\
    ): Errors raised while activating the visual editor are now logged and reported through the standard error dialog instead of silently leave the editor stuck on its loading spinner indefinitely.\
*   ([#18125](https://github.com/rstudio/rstudio/issues/18125)\
    ): Fixed autocompletion inside `geom_*()` calls failing to offer a ggplot2 aesthetic when the typed token matched only an aesthetic and not one of the function’s formal arguments (for example, `linet` now completes to `linetype`).\
*   ([#18089](https://github.com/rstudio/rstudio/issues/18089)\
    ): Restored the Cmd+Alt+F (Ctrl+Alt+F) keyboard shortcut for “Run Current Function Definition”, which had been unintentionally overridden by the “Find in Console” command. Find in Console is still available via the console toolbar and by pressing the Find (Cmd+F / Ctrl+F) shortcut while the console has focus.\
*   ([#14040](https://github.com/rstudio/rstudio/issues/14040)\
    ): Fixed the visual editor’s “Editor content width” resetting to the default (full) width when more than one R Markdown or Quarto document was open in visual mode and the user interacted with one of them (for example, right-clicking a misspelled word, opening a toolbar menu, switching tabs, or resizing a pane). Hidden visual-editor tabs no longer overwrite the shared content-width style.\
*   ([#17831](https://github.com/rstudio/rstudio/issues/17831)\
    ): Fixed autocomplete not updating when deleting a colon to go from `pkg:::` to `pkg::`. The completion list now correctly narrows from all objects to only exported objects.\
*   ([#17796](https://github.com/rstudio/rstudio/issues/17796)\
    ): The Title, Author, and Date fields in the New R Markdown, New Quarto Document, and Compile Notebook dialogs no longer show the browser’s native spell-checking squiggles.\
*   ([#17758](https://github.com/rstudio/rstudio/issues/17758)\
    ): Fixed the console becoming unresponsive (sometimes for minutes, with the session entering uninterruptible sleep) after running a command that merely contained a word like “remove” or “update” in a comment, a string, or as part of another function name such as `str_remove_all()`.\
*   ([#18091](https://github.com/rstudio/rstudio/pull/18091)\
    ): RStudio Server sessions now suspend and shut down faster. Stopping the server (or a session timing out) no longer waits for a now-disconnected browser to retrieve final events, and suspending no longer spends time serializing internal RStudio-managed options that are recreated on resume.\
*   ([#18046](https://github.com/rstudio/rstudio/issues/18046)\
    ): Fixed Copilot completions sometimes appearing only as a gutter icon (rather than inline) when the first completion in a document fell back to a next edit suggestion. Such fallback suggestions now honor the “automatically display next edit suggestions” preference instead of being collapsed to the gutter.\
*   ([#6796](https://github.com/rstudio/rstudio/issues/6796)\
    ): The Git History pane now shows the full commit message body (not just the subject line) when viewing commit details.\
*   ([#17982](https://github.com/rstudio/rstudio/issues/17982)\
    ): Fixed a race condition in RStudio Desktop where the viewer pane iframe could be blocked by Electron’s navigation policy, causing cross-origin SecurityErrors when previewing Markdown files or R Notebooks as HTML.\
*   ([#18057](https://github.com/rstudio/rstudio/issues/18057)\
    ): Reduced the padding on text input fields and drop-down (select) controls, which had grown overly large (most noticeably in dark themes). Made the padding consistent across text inputs, password fields, and selects in both light and dark themes.\
*   ([#18037](https://github.com/rstudio/rstudio/issues/18037)\
    ): Fixed the Plots pane not being brought to the front when Posit Assistant runs code that produces a plot. Interactive agent code now activates the Plots pane like a console command does.\
*   ([#18033](https://github.com/rstudio/rstudio/issues/18033)\
    ): Fixed ghost text set via `rstudioapi::setGhostText()` not being dismissed when navigating the cursor away or typing a non-matching character, which left it insertable by Tab even after it appeared to be gone.\
*   ([#17970](https://github.com/rstudio/rstudio/issues/17970)\
    ): Fixed the Packages pane vulnerability dialog listing vulnerabilities that affect a different installed version of the clicked package. The dialog now shows only the vulnerabilities for that row’s version. A package with vulnerability records from multiple repositories now shows a single combined warning icon and dialog instead of one per repository.\
*   ([#17985](https://github.com/rstudio/rstudio/issues/17985)\
    ): Fixed an issue where the Import Dataset preview dialog failed to display error messages when the readr preview subprocess encountered an error, causing the dialog to hang indefinitely waiting for data that would never arrive.\
*   ([#18003](https://github.com/rstudio/rstudio/issues/18003)\
    ): Fixed an issue where reformat-on-save with Air configured as an external formatter ignored the project’s air.toml configuration.\
*   ([#17774](https://github.com/rstudio/rstudio/issues/17774)\
    ): Fixed reformat-on-save not formatting R scripts opened outside of an RStudio project (or with no project open), even though the “Reformat Document” command worked. Format-on-save is no longer restricted to files inside the active project.\
*   ([#6147](https://github.com/rstudio/rstudio/issues/6147)\
    ): The data viewer now scrolls continuously through the columns of a very wide data frame instead of paging through fixed blocks of columns, so a column’s filter, sort, and pin are no longer limited to (or lost when leaving) the currently visible set of columns.\
*   ([#6147](https://github.com/rstudio/rstudio/issues/6147)\
    ): The data viewer’s column-pagination arrows are replaced by a “Go to column” box in the toolbar that jumps to a column by name or number.\
*   ([#6147](https://github.com/rstudio/rstudio/issues/6147)\
    ): The data viewer’s summary sidebar now lists every column of the frame, loading each column’s summary as it scrolls into view.\
*   ([#6147](https://github.com/rstudio/rstudio/issues/6147)\
    ): The data viewer’s summary sidebar now reflects the active filter and search, rather than always describing the whole frame.\
*   ([#17979](https://github.com/rstudio/rstudio/issues/17979)\
    ): Added a “Show Filter UI by default” toggle to the data viewer’s Settings menu. When enabled, the filter bar is shown automatically each time a data frame is opened, instead of requiring a click to reveal it.\
*   ([#17993](https://github.com/rstudio/rstudio/issues/17993)\
    ): Added a “Use overlay scrollbars” toggle to the data viewer’s Settings menu. When disabled, the data viewer uses native, always-visible scrollbars instead of the auto-hiding overlay scrollbars.\
*   ([#17807](https://github.com/rstudio/rstudio/issues/17807)\
    ): Fixed a startup stall and missing package vulnerability badges that could occur when an intermediary (such as a proxy) kept the connection to Posit Package Manager open after responding.\
*   ([#18019](https://github.com/rstudio/rstudio/issues/18019)\
    ): Fixed an issue where a transient connection failure while writing user state during startup could leave the IDE stuck on an empty grey screen.\
*   ([#1667](https://github.com/rstudio/rstudio/issues/1667)\
    ): On Linux Desktop, hardened middle-click (primary selection) paste in the editor and console. A selection is now flushed to the primary selection on mouse release rather than only after a short delay, and a middle-click paste falls back to the event’s clipboard text when the tracked selection is empty, so quickly selecting and middle-click-pasting no longer pastes nothing.\
*   ([#18065](https://github.com/rstudio/rstudio/issues/18065)\
    ): Fixed an uncaught JavaScript exception thrown when an r2d3 widget requested the editor theme, caused by an uninjected user-state provider in the page’s message listener. r2d3 widgets now honor the editor theme.\
*   ([#18068](https://github.com/rstudio/rstudio/issues/18068)\
    ): Auto-downloaded copies of the Air formatter are now installed under RStudio’s per-user data directory (for example, `~/.local/share/rstudio/air` on Linux or `%LOCALAPPDATA%\rstudio\air` on Windows) instead of `~/.local/lib/air`. Copies installed by older versions of RStudio in the previous location are still detected and used.\
*   ([#18093](https://github.com/rstudio/rstudio/issues/18093)\
    ): Fixed interactive execution of `sql` chunks that use the `--|` cell-option comment syntax (for example, `--| connection: con`). The option line is now stripped from the chunk body before the query is sent to the database, so backends such as MySQL and MariaDB that reject `--|` as invalid SQL syntax no longer raise an error.\
*   ([#18139](https://github.com/rstudio/rstudio/issues/18139)\
    ): Fixed an issue on Windows where the R session started in the “C” locale instead of the operating system’s locale, corrupting non-ASCII console input and breaking `list.files()` and other locale-sensitive operations for users whose locale is not ASCII-compatible (for example, Turkish on Windows 11). The session now adopts the operating system locale at startup, restores the session locale rather than pinning it to “C” after rendering an R Markdown document, and logs locale synchronization failures instead of failing silently.\
*   ([#18101](https://github.com/rstudio/rstudio/issues/18101)\
    ): Fixed “Run Selection as Background Job” (and the related Source/Launcher job commands) appearing to do nothing when invoked from a detached source window on Windows Desktop. The job launcher dialog is shown in the main window, which is now brought forward so the dialog is visible.\
*   ([#18143](https://github.com/rstudio/rstudio/issues/18143)\
    ): Fixed the Object Explorer emitting `Setting class(x) to "environment"` warnings (and showing no description) for S4 objects wrapping environments, such as reference class instances. The explorer also no longer temporarily modifies the class of an environment being described.\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-14)\
\
*   (rstudio-pro#11597): Fixed `rstudio-server interpreters inspect` and `rstudio-server verify-installation` failing on Job Launcher clusters that require a resource profile (`allow-custom-resources=0`).\
*   (rstudio-pro#11475): Fixed `rstudio-server interpreters inspect` and interpreter inspection from the admin interface always timing out after 5 minutes on Local and Slurm clusters, even when the inspection job succeeded.\
*   (rstudio-pro#9120): Fixed the SQLite-to-PostgreSQL database migration failing with a foreign key constraint error.\
*   (rstudio-pro#10885): Fixed a “database is locked” error that could interrupt OAuth (Snowflake) token refresh under concurrent session load.\
*   (rstudio-pro#11529): Fixed the homepage launcher UI so that selecting a resource profile that pins a SLURM queue (partition) locks the queue input and no longer submits the incorrect queue on launch.\
*   (rstudio-pro#11576): Fixed race condition with websockets and load balancing that could cause `bad record mac` errors in rserver.log that led to websockets being reconnected.\
*   (rstudio-pro#11646): Lowered default value for the timeout for `launcher-sessions-proxy-timeout` to reduce the overhead of client requests for missing sessions.\
*   (rstudio-pro#11256): Fixed problem where VS Code and Positron sessions could bypass the login timeouts even when idle.\
*   (rstudio/launcher#1555): The Launcher now sets the `HOME`, `USER`, and `LOGNAME` environment variables for plugin processes to match the configured `server-user` after dropping privilege.\
*   (rstudio/launcher#1557): The Kubernetes plugin no longer issues redundant `getJob` calls to the API server for jobs already known to be deleted, reducing connection load on busy multi-replica clusters.\
\
### Upgrade Instructions[](https://docs.posit.co/ide/news/#rstudio-2026.07.0-upgrade)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-15)\
\
*   The Positron version bundled with this release no longer supports the `positron.assistant.enable` setting, and Posit Assistant is enabled by default. Administrators who used `positron.assistant.enable` in `positron-user-settings.json` or `enforced-settings.json` to control assistant availability should set `assistant-enabled` in `/etc/rstudio/profiles` instead; otherwise Posit Assistant becomes available to all users after upgrading. See [Posit Assistant Admin Controls](https://docs.posit.co/ide/server-pro/admin/ai/assistant-controls.html)\
    .\
\
### Dependencies[](https://docs.posit.co/ide/news/#rstudio-2026.07.0-dependencies)\
\
*   Ace 1.43.5\
*   Copilot Language Server 1.509.1\
*   Electron 41.9.0\
*   Job Launcher Service 2.26.1-574\
*   Node.js 22.22.2 (copilot, Posit Assistant)\
*   PWB Code Server 2026.07-b2876, Code OSS 1.118.0\
*   Positron 2026.07.1-5\
*   Quarto 1.9.38\
*   xterm.js 6.0.0\
\
2026.06.0[](https://docs.posit.co/ide/news/#rstudio-2026.06.0)\
\
---------------------------------------------------------------\
\
**“Blue Plumbago”** | Date: 2026-06-29\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2026.06.0-new)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-13)\
\
*   ([#15830](https://github.com/rstudio/rstudio/issues/15830)\
    ): Add a Code menu and command-palette entry to re-enable the editor’s missing-package banner for a file after dismissing it, and rename the banner’s dismissal label to “Don’t show for this file” to make the per-file scope explicit.\
*   ([#17734](https://github.com/rstudio/rstudio/issues/17734)\
    ): Support em dashes and box-drawing characters as native R code section delimiters.\
*   ([#8541](https://github.com/rstudio/rstudio/issues/8541)\
    ): Add a “Change active editor tab with mouse wheel” preference (General > Basic > Other) to disable switching the active editor tab by scrolling the mouse wheel over the tab bar.\
*   ([#2350](https://github.com/rstudio/rstudio/issues/2350)\
    ): Add an Appearance pane to Project Options for setting a project-specific editor theme; leaving it at “(Default)” uses the global theme. A new “Ignore project-specific appearance settings” option (Global Options > Appearance) keeps the global editor theme even when a project sets its own.\
*   ([#17923](https://github.com/rstudio/rstudio/pull/17923)\
    ): Posit Assistant now runs R code expression by expression, interleaving each expression with its output in the chat pane, rather than running the whole block at once and showing all output at the end.\
*   ([#14965](https://github.com/rstudio/rstudio/issues/14965)\
    ): The Insert Pipe Operator command (Ctrl+Shift+M / Cmd+Shift+M) now inserts the native R pipe operator `|>` by default; the magrittr pipe `%>%` can be restored via the “Use R’s native pipe operator, |>” preference.\
*   ([#17501](https://github.com/rstudio/rstudio/issues/17501)\
    ): Move the Find in Files refresh button to the right side of the toolbar, matching the convention used by other panes, and make the replace preview’s match highlight colors theme-aware so they no longer look out of place under dark editor themes.\
*   ([#17912](https://github.com/rstudio/rstudio/issues/17912)\
    ): Add a `project-trust-required` session option (off by default) that treats all projects as untrusted by default – including projects in the user’s home directory – prompting users to trust each project when opened even if it contains no auto-executing files. Additionally, the visual editor is now disabled in untrusted projects, whether or not this option is set; only the source editor is available for markdown documents.\
*   ([#17748](https://github.com/rstudio/rstudio/issues/17748)\
    ): When “Use Air for code formatting” is enabled, Air now formats R documents even when no `air.toml` file is present, using the editor’s indentation settings (indent style and width). The previous behavior of formatting only in projects containing an `air.toml` can be restored with the new “Only use Air when an air.toml file is found” option (Global Options > Code > Formatting).\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-16)\
\
*   (rstudio-pro#11044): **Preview:** Workbench can run an embedded Posit Chronicle observability service, collecting session telemetry, audit events, and runtime metrics as Parquet files.\
*   (rstudio-pro#11215): Kubernetes admins can now offer a preview version of Positron to users. Enable it with the new `launcher-positron-preview-init-container-enabled` rserver.conf option.\
*   (rstudio-pro#10954): The session init container and Positron init container now run as the configured server user by default. Set the new `launcher-sessions-init-container-run-user` rserver.conf option to `root` for the legacy behavior.\
*   (rstudio-pro#10956): Launcher sessions can now run rootless in Kubernetes when using SCIM or JIT through NSS.\
*   (rstudio/launcher#1350): Slurm cluster admins can now configure a default value for custom placement constraints (e.g. `Time=time:1:30:00`); the session launch dialog pre-fills the input and the default is submitted when the user leaves it empty.\
*   (rstudio-pro#10835): Added `--uid` and `--home` arguments to `rstudio-server add-user`.\
*   (rstudio-pro#10835): Added `rstudio-server` `update-user`|`user-info`|`delete-user`.\
*   (rstudio-pro#10890): `rstudio-server verify-installation` prints a filesystem permission summary for the invoking user, covering `/etc/rstudio`, the secure cookie and session RPC keys, `database.conf`, and the Positron install directory.\
*   (rstudio-workbench-vscode-ext#471): Added Foundry Audience configuration option for use with Foundry models in Positron Pro sessions.\
*   (rstudio-pro#11114): The Projects table on the homepage now defaults to a smart sort order: running sessions appear first, followed by the most recent projects based on user activity or session state changes.\
*   (rstudio/launcher#1443): Added opt-in `container-images-mode` option to `launcher.kubernetes.conf` to control how the Launcher Kubernetes plugin resolves `container-images` when a user matches multiple profile levels. See the Kubernetes plugin documentation for details.\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2026.06.0-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-14)\
\
*   ([#17990](https://github.com/rstudio/rstudio/issues/17990)\
    ): Fix the data viewer becoming unusable when a numeric column’s histogram computation fails; such a failure now leaves that one column without a sparkline instead of aborting the whole data frame.\
*   ([#17937](https://github.com/rstudio/rstudio/issues/17937)\
    ): Fix the Object Explorer showing the first element’s contents for every same-named element when a list has duplicated names; such elements are now retrieved by index instead of by name.\
*   ([#17944](https://github.com/rstudio/rstudio/issues/17944)\
    ): Fix the Source pane occasionally restoring the wrong active tab after a reload or session restart when tabs had been drag-reordered or documents opened mid-session; the active document is now remembered by ID rather than by tab position.\
*   ([#17521](https://github.com/rstudio/rstudio/issues/17521)\
    ): Fix R Notebook previews failing with “object not found” when the document contains inline R code referencing objects in the global environment; inline chunks are now evaluated in the user’s R session and their outputs passed to the background notebook render. This can be disabled with the new “Execute inline R code when previewing notebooks” preference (Global Options > R Markdown).\
*   ([#17501](https://github.com/rstudio/rstudio/issues/17501)\
    ): Fix the secondary toolbars in the Find in Files and Presentation panes rendering 2px shorter than the space reserved for them, which left a small dead strip below the toolbar border.\
*   ([#17892](https://github.com/rstudio/rstudio/issues/17892)\
    ): Added a “Use the system certificate store” option (Tools > Global Options > Assistant) so the GitHub Copilot agent and Posit Assistant trust the operating system certificate store (Windows Certificate Store, macOS Keychain) when connecting – useful behind a TLS-inspecting proxy on RStudio Desktop.\
*   ([#17898](https://github.com/rstudio/rstudio/issues/17898)\
    ): Recognize the Posit Assistant’s `.posit/assistant` project-state directory (in addition to the legacy `.positai`) when updating a project’s `.gitignore`, `.Rbuildignore`, and `svn:ignore` files, so it is ignored automatically once it appears. The rest of `.posit` – such as the Posit Publisher extension’s `.posit/publisher` – is left tracked.\
*   ([#17147](https://github.com/rstudio/rstudio/issues/17147)\
    ): Fix code suggestions being silently accepted off-screen. Inline (at-cursor) ghost text is now dismissed when the cursor moves elsewhere; accepting a next edit suggestion that is scrolled out of view first navigates to it, with a second key press accepting it; an arrow indicator pinned to the edge of the gutter now points toward an active off-screen suggestion, and clicking it navigates there.\
*   ([#17900](https://github.com/rstudio/rstudio/issues/17900)\
    ): Fix Find in Files (and project code search) returning no results in a Quarto or R Markdown website project whose output directory is set to the project directory itself (for example `output-dir: .` in `_quarto.yml`); the project root is no longer treated as ignored output content.\
*   ([#14202](https://github.com/rstudio/rstudio/issues/14202)\
    ): Fixed an issue where RStudio Desktop could hang on startup when offline or on an unreliable network connection.\
*   ([#17701](https://github.com/rstudio/rstudio/issues/17701)\
    ): Honor newline characters in `rstudioapi::showDialog()` and `rstudioapi::showPrompt()` messages.\
*   ([#17729](https://github.com/rstudio/rstudio/issues/17729)\
    ): Show distinct copy in the Posit Assistant chat pane and preferences install prompt when the recommended Posit Assistant version is older than the installed one.\
*   ([#17738](https://github.com/rstudio/rstudio/issues/17738)\
    ): Fix `file.edit()` (and other Source pane open events) silently dropping when invoked during an in-flight `closeAllSourceDocs`.\
*   ([#17745](https://github.com/rstudio/rstudio/issues/17745)\
    ): Fix the bundled `air` formatter being copied without the `.exe` extension on Windows, which prevented format-on-save with Air from working.\
*   ([#17750](https://github.com/rstudio/rstudio/issues/17750)\
    ): Cache the resolved path to the Air formatter, and prefer an already-installed copy of Air over querying GitHub for the latest release, so format-on-save with the auto-installed Air no longer pings GitHub (a delay of 600ms or more) on every save.\
*   ([#17746](https://github.com/rstudio/rstudio/issues/17746)\
    ): Fix the automatic download of the Air formatter failing on slow connections. The download now uses the `curl` binary when available, which only times out on inactivity rather than on total download time; when `curl` is unavailable, the `download.file()` fallback raises R’s download timeout to at least 300 seconds for this download.\
*   ([#17737](https://github.com/rstudio/rstudio/issues/17737)\
    ): Restore the “Show .Last.value in environment listing” preference, which had stopped surfacing `.Last.value` in the Environment pane.\
*   ([#17743](https://github.com/rstudio/rstudio/issues/17743)\
    ): Fix the debugger failing to capture the browser environment for functions loaded by the `box` package.\
*   ([#17712](https://github.com/rstudio/rstudio/issues/17712)\
    ): Fix Quarto rendering failing on Windows when the user’s home folder path contains an ampersand.\
*   ([#17669](https://github.com/rstudio/rstudio/issues/17669)\
    ): Avoid re-scanning the watched directory on every Files pane notification on macOS by enabling FSEvents per-file event reporting for non-recursive watches.\
*   ([#17768](https://github.com/rstudio/rstudio/issues/17768)\
    ): Handle the ANSI cursor-movement escape sequences cursor-up (CSI A), cursor-down (CSI B), cursor-next-line (CSI E), cursor-previous-line (CSI F), and cursor-horizontal-absolute (CSI G) in the console so that multiple `cli` progress bars render on separate lines instead of overwriting each other.\
*   ([#17225](https://github.com/rstudio/rstudio/issues/17225)\
    ): Fix duplicate entries appearing in the recent projects list when the same project was recorded under both aliased (`~/...`) and absolute path forms.\
*   ([#17777](https://github.com/rstudio/rstudio/issues/17777)\
    ): Fix “Import Dataset” from the Environment pane failing with “could not find function ‘.rs.digest’” when previewing a CSV (or other readr/readxl/haven source).\
*   ([#3798](https://github.com/rstudio/rstudio/issues/3798)\
    ): The Windows terminal now uses the native Windows pseudoconsole (ConPTY) instead of the legacy winpty library, improving Ctrl+C handling in console programs.\
*   ([#17800](https://github.com/rstudio/rstudio/issues/17800)\
    ): Fix the data viewer’s horizontal scrollbar staying hidden after returning to the tab, and fix Ctrl+C/Cmd+C copying only the active cell instead of the user’s multi-cell text selection.\
*   ([#17958](https://github.com/rstudio/rstudio/issues/17958)\
    ): Restore the data viewer’s End and Ctrl+End behavior: they once again scroll to the last row of the current column instead of jumping to the last column, and the jump now lands with the last row fully visible rather than stopping a header-height short of the bottom.\
*   ([#17806](https://github.com/rstudio/rstudio/issues/17806)\
    ): Fix the data viewer becoming slow to open, scroll, and search – and freezing for several seconds when opening very wide data frames – when there are many columns or the summary panel is shown. The grid now renders only the rows and columns currently in view.\
*   ([#17835](https://github.com/rstudio/rstudio/issues/17835)\
    ): Fix a pinned column in the data viewer jumping to a different column after paging to another set of columns in a very wide data frame; the pinned column now stays visible and tracks its original column across column pagination.\
*   ([#17861](https://github.com/rstudio/rstudio/issues/17861)\
    ): Preserve the data viewer’s scroll position when the displayed data is refreshed in place – for example after adding or removing a column, or changing values in an existing column – so the grid no longer jumps back to the first row. The view still returns to the top when the underlying row count changes (the data was subset, reassigned, or had rows added or removed). Adding a column to a viewed data frame now also displays the new column, instead of keeping the previous set of columns.\
*   ([#17278](https://github.com/rstudio/rstudio/issues/17278)\
    ): Fix a `data.table` returned invisibly from a `:=` update (e.g. `dt[, x := y]`) being auto-printed in notebook chunks, when its output should be suppressed as it is in the console.\
*   ([#17810](https://github.com/rstudio/rstudio/issues/17810)\
    ): Fix the “Run Tests” button modifying the active test file’s timestamp even when the file had no unsaved changes.\
*   ([#17735](https://github.com/rstudio/rstudio/issues/17735)\
    ): Hide the redundant column-summary sidebar in the data frame preview shown in the Help pane.\
*   ([posit-dev/positron#13964](https://github.com/posit-dev/positron/issues/13964)\
    ): Serve Positron docs with an `.html` fallback so links like Show Release Notes resolve.\
*   ([#17066](https://github.com/rstudio/rstudio/issues/17066)\
    ): Fix the Assistant preferences pane showing a stale code-assistant account after switching back and forth between GitHub Copilot and Posit Assistant.\
*   ([#17579](https://github.com/rstudio/rstudio/issues/17579)\
    ): On RStudio Desktop, serve Viewer pane content via `127.0.0.1` instead of `localhost`, so HTML files and htmlwidgets display on systems where `localhost` does not resolve to the IPv4 loopback address that R’s help server binds to.\
*   ([#17327](https://github.com/rstudio/rstudio/issues/17327)\
    ): Stop requesting code completions and next-edit suggestions while editing in visual mode, where suggestions aren’t shown, so document contents are no longer sent to the completion backend for suggestions there.\
*   ([#17493](https://github.com/rstudio/rstudio/issues/17493)\
    ): Fix the comment/uncomment shortcut inserting the comment character at the start of an empty indented line instead of after the indent.\
*   ([#17868](https://github.com/rstudio/rstudio/issues/17868)\
    ): Restrict the Python help URL handler (`/python/`) to valid help-topic names, accepting only plain dotted qualified names.\
*   ([#17833](https://github.com/rstudio/rstudio/issues/17833)\
    ): Fix saving a file silently appearing to succeed when the write actually failed (for example, when the disk is full or a disk quota is exceeded); such failures are now reported and the document keeps its unsaved state.\
*   ([#17845](https://github.com/rstudio/rstudio/issues/17845)\
    ): Fix Find in Files “Replace All” overwriting a source file with truncated or empty contents when the write failed (for example, when the disk is full or a disk quota is exceeded); the replacement is now written atomically and durably, so on failure the original file is left untouched and the error is reported.\
*   ([#17863](https://github.com/rstudio/rstudio/issues/17863)\
    ): Fix the Data Viewer entering a “Failed to fetch” error state when clicking the header of a list column to sort it; such columns are no longer sortable.\
*   ([#17874](https://github.com/rstudio/rstudio/issues/17874)\
    ): Fix the Render button reusing a running Quarto preview and ignoring changes to project options in `_quarto.yml` / `_quarto.yaml` (for example `pdf-engine`); RStudio now restarts the preview when the project config changes so the new options take effect.\
*   ([#17872](https://github.com/rstudio/rstudio/issues/17872)\
    ): Fix a newly added file appearing at the bottom of the Files pane instead of in its sorted position when the pane is sorted by a column.\
*   ([#17439](https://github.com/rstudio/rstudio/issues/17439)\
    ): Fix the Shiny app window (Run App > Run in Window) becoming impossible to close – and staying orphaned in a grayed-out state across subsequent runs – when the app registers a `beforeunload` handler that prevents unload. RStudio Desktop now shows a “Leave page?” confirmation (mirroring browser behavior) and closes the window when the user confirms.\
*   ([#17865](https://github.com/rstudio/rstudio/issues/17865)\
    ): Fix project paths on a mapped network drive (e.g. `S:`) being resolved to their UNC target (e.g. `\\server\share`) on Windows, which caused functions such as `here::here()` and `getwd()` to report the UNC path instead of the mapped drive.\
*   ([#17870](https://github.com/rstudio/rstudio/issues/17870)\
    ): Fix an uncaught “Object has been destroyed” error in RStudio Desktop when quitting with a plot zoom (or other child) window still open.\
*   ([#17830](https://github.com/rstudio/rstudio/issues/17830)\
    ): Fix the data viewer not clearing a data set’s saved sorts and filters when its tab is explicitly closed, so reopening the data set no longer restores stale filters; the saved state still persists across a session suspend/restore or a page reload. Restored filters now also reveal the filter row, instead of being applied with no visible filter UI.\
*   ([#17178](https://github.com/rstudio/rstudio/issues/17178)\
    ): Fix RStudio locking up when clicking “Run examples” in a help page whose examples launch a blocking application such as a Shiny app. Such examples now run in the console (like `example()`) instead of being rendered inline by the help server.\
*   ([#17909](https://github.com/rstudio/rstudio/issues/17909)\
    ): Fix the Files pane on macOS briefly showing and then emptying the contents of a symlinked directory; file change events are now reported against the path the directory was opened as, rather than its resolved target. Opening a project via a symlinked path on macOS also no longer rewrites the project directory (as reported by `getwd()` and `here::here()`) to the symlink’s target.\
*   ([#17929](https://github.com/rstudio/rstudio/issues/17929)\
    ): Fix the “Show code suggestions after keyboard idle (ms)” field never appearing in the Assistant preferences pane (Global Options > Assistant), so the automatic code-completion delay can again be configured from the options UI.\
*   ([#17942](https://github.com/rstudio/rstudio/issues/17942)\
    ): Fix the Data Viewer’s Summary sidebar visibility resetting to the preference default when the viewed object’s columns changed (for example, after adding a column from the console).\
*   ([#17941](https://github.com/rstudio/rstudio/issues/17941)\
    ): Fix the terminal silently dropping entire output chunks when a multi-byte UTF-8 character was split across PTY reads and the terminal was connected over WebSockets (the default), which severely corrupted the output of programs emitting non-ASCII output at volume (modern TUIs, R packages printing Unicode). A split character is now reassembled across chunks, which also fixes the stray replacement characters previously seen at chunk boundaries when the “Connect with WebSockets” option was disabled.\
*   ([#17951](https://github.com/rstudio/rstudio/issues/17951)\
    ): Fix `View()` failing with “missing value where TRUE/FALSE needed” on data frames containing an integer column whose range exceeds `.Machine$integer.max` (for example, values spanning -2000000000 to 2000000000).\
*   ([#17950](https://github.com/rstudio/rstudio/issues/17950)\
    ): Fix data viewer column filters being silently re-applied after being dismissed – a value typed or brushed just before pressing Escape, clicking the clear button, or clicking away could land after the header had reverted to “All”, leaving the grid filtered with no visible filter. A factor filter restored when its column scrolls back into view now displays its level name instead of a blank box, and pressing Enter in the numeric filter popup now applies the typed value immediately.\
*   ([#17969](https://github.com/rstudio/rstudio/issues/17969)\
    ): Fix switching AI assistants while the previous agent was still initializing occasionally double-initializing the new agent and applying the previous assistant’s configuration to it; a stale initialization callback is now discarded when cancelled.\
*   ([#17994](https://github.com/rstudio/rstudio/pull/17994)\
    ): Fix an “Error” dialog (“Cannot read properties of null (reading ‘document’)”) appearing if Global Options was dismissed while the editor theme preview was still finishing its initial Ace JavaScript load; the deferred load callbacks now bail out cleanly when the preview frame has already been detached.\
*   ([#17994](https://github.com/rstudio/rstudio/pull/17994)\
    ): Fix the macOS desktop GWT output cache occasionally producing installer builds without the visual editor’s `panmirror.js` bundle (which manifested as a 404 and a visual editor that never finished mounting); the panmirror build output now lands inside the cached gwt directory rather than the source tree, so cache-hit builds keep it. Affects builds that reuse the cached GWT output via `--build-gwt=0`.\
*   ([#18022](https://github.com/rstudio/rstudio/issues/18022)\
    ): On Windows, fix the final chunk of a child process’s standard output being dropped, and fix a rare session crash when draining a process’s output at exit; the remaining output is now read directly instead of on a short-lived helper thread.\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-17)\
\
*   (rstudio/launcher#1562): Fixed Kubernetes plugin watch reconnect loop that could cause the plugin to stop tracking running sessions on busy clusters.\
*   (rstudio-pro#11274): Fixed missing OpenTelemetry session events when suspending, ending, or killing a session from the home screen on file-storage deployments.\
*   (rstudio-pro#7471): Fixed `rstudio-server` `delete-user`|`lock-user`|`unlock-user` silently accepting multiple usernames and operating only on the first.\
*   (rstudio-pro#11269): Fixed sessions failing to start when `www-frame-origin` is configured with multiple space-separated origins.\
*   (rstudio-pro#11269): Fixed `/workspaces/perf` returning 404 in single-session deployments.\
*   (rstudio-pro#6968): Fixed SCIM-driven user deletion so that orphaned username-keyed records are cleaned up alongside the user.\
*   (rstudio-pro#10835): Fixed `rstudio-server list-users` always reporting Admin as `false`.\
*   (rstudio-pro#10842): Event `username` and `data` fields are no longer truncated to 32 characters in the session audit log (`r-sessions.jsonl`/`.csv`), so full file paths and long usernames are recorded for compliance auditing.\
*   (rstudio-pro#11281): Fixed Slurm session launches sending an empty placement constraint argument (e.g. `--account=`, `--time=`) when a constraint has no configured default and the field is left blank, which SLURM rejected. Empty constraints are now omitted, and user-typed values are applied on named (non-`custom`) profiles.\
*   (rstudio-pro#11251): Fixed Positron sessions failing to launch when a registered enforced-settings file contains a single quote (or other shell metacharacters) by passing the settings to the session via the environment instead of interpolating them into the launch command.\
*   (rstudio-pro#10789): Fixed the encrypted sign-in form so that empty-field validation errors are programmatically associated with the Username and Password inputs (`aria-describedby`), letting screen readers announce the error when focus is on the field (WCAG 3.3.1).\
\
### Upgrade Instructions[](https://docs.posit.co/ide/news/#rstudio-2026.06.0-upgrade)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-18)\
\
*   Removed `feature-flag-user-deletion`. User deletion is officially supported.\
\
### Dependencies[](https://docs.posit.co/ide/news/#rstudio-2026.06.0-dependencies)\
\
*   Ace 1.43.5\
*   Copilot Language Server 1.500.0\
*   Electron 41.7.2\
*   Job Launcher 2.25.0\
*   Node.js 22.22.2 (copilot, Posit AI)\
*   PWB Code Server 2026.06-b2861, Code OSS 1.118.0\
*   Quarto 1.9.38\
*   xterm.js 6.0.0\
*   Positron 2026.06.1-6\
\
2026.05.1[](https://docs.posit.co/ide/news/#rstudio-2026.05.1)\
\
---------------------------------------------------------------\
\
**“Golden Wattle”** | Date: 2026-06-16\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2026.05.1-new)\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2026.05.1-fixed)\
\
*   ([#17737](https://github.com/rstudio/rstudio/issues/17737)\
    ): Restore the “Show .Last.value in environment listing” preference, which had stopped surfacing `.Last.value` in the Environment pane.\
*   ([#17777](https://github.com/rstudio/rstudio/issues/17777)\
    ): Fix “Import Dataset” from the Environment pane failing with “could not find function ‘.rs.digest’” when previewing a CSV (or other readr/readxl/haven source).\
*   ([#17807](https://github.com/rstudio/rstudio/issues/17807)\
    ): Fix 60 second startup delay on Posit Package Manager vulnerability check.\
*   ([#17278](https://github.com/rstudio/rstudio/issues/17278)\
    ): Fix a `data.table` returned invisibly from a `:=` update (e.g. `dt[, x := y]`) being auto-printed in notebook chunks, when its output should be suppressed as it is in the console.\
*   ([#17822](https://github.com/rstudio/rstudio/pull/17822)\
    ): Fix Posit Package Manager vulnerability badges no longer appearing in the Packages pane for sessions that point `options(repos)` at a PPM instance without Workbench PPM integration configured.\
\
### Dependencies[](https://docs.posit.co/ide/news/#rstudio-2026.05.1-dependencies)\
\
2026.05.0[](https://docs.posit.co/ide/news/#rstudio-2026.05.0)\
\
---------------------------------------------------------------\
\
**“Golden Wattle”** | Date: 2026-05-26\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2026.05.0-new)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-15)\
\
*   ([#17539](https://github.com/rstudio/rstudio/issues/17539)\
    ): The data viewer is now faster and supports pinnable columns, a Summary sidebar with type-aware stats and sparkline histograms, keyboard navigation, and clipboard copy.\
*   ([#17539](https://github.com/rstudio/rstudio/issues/17539)\
    ): Added the `data_viewer_show_summary` user preference, which controls the default visibility of the data viewer’s Summary sidebar.\
*   ([#17539](https://github.com/rstudio/rstudio/issues/17539)\
    ): Raised the default value of `data_viewer_max_columns` from 50 to 200.\
*   ([#17477](https://github.com/rstudio/rstudio/issues/17477)\
    ): Posit Assistant: the `ui/openDocument` JSON-RPC method now accepts an optional 1-based `line` parameter, and RStudio advertises the `ui/openDocument/line` capability so the assistant can open documents at a specific line.\
*   ([#17478](https://github.com/rstudio/rstudio/issues/17478)\
    ): Posit Assistant: added the `ui/revealInFilesPane` JSON-RPC method, which navigates the Files pane to a directory (or to a file’s parent directory) and brings the pane to the front.\
*   ([#17479](https://github.com/rstudio/rstudio/issues/17479)\
    ): Posit Assistant: added the `ui/previewUrl` JSON-RPC method, which navigates the Viewer pane to an `http(s)` URL (e.g., a local Shiny app); supports an optional `height` parameter that mirrors `rstudioapi::viewer()` (`-1` for maximize, `0` for no change, positive for pixels).\
*   ([#17514](https://github.com/rstudio/rstudio/issues/17514)\
    ): Added the `allow-package-source-recording` session option (default `true`); when set to `false`, RStudio will not annotate DESCRIPTION files of packages installed via `install.packages()` with the remote repository they came from.\
*   ([#5809](https://github.com/rstudio/rstudio/issues/5809)\
    ): Roxygen tag autocompletion (e.g. `@param`, `@return`) now works on `#'` lines inside R code chunks of R Markdown and Quarto documents, matching the behavior in plain `.R` files.\
*   ([rstudio/launcher#1368](https://github.com/rstudio/launcher/issues/1368)\
    ): Added opt-in `singularity-image-directory-mode` option to `launcher.slurm.conf` to control how the Launcher Slurm plugin resolves `singularity-image-directory` when a user matches multiple profile levels. See the Slurm plugin README for details.\
*   ([rstudio/launcher#522](https://github.com/rstudio/launcher/issues/522)\
    ): Added `nfs-heartbeat-poll-threshold` option to `launcher.local.conf` to tune the Launcher Local plugin’s Network File System (NFS)-mode offline detection latency (default 6 polls × 10s = 60s).\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-19)\
\
*   (rstudio-pro#10905, rstudio-pro#10828): Added the `assistant-enabled` key in `/etc/rstudio/profiles` as a preview setting for unified Posit Assistant control across RStudio Pro and Positron Pro sessions, with global, per-group, and per-user scopes\
*   (rstudio-pro#10331): Moved the project path to a sub-line under the project name on the homepage. The Path column is now hidden by default but can be re-enabled via column settings\
*   (rstudio-pro#9817): Updated Posit Workbench logo, favicon, and icons to new branded assets across the Workbench UI\
*   (rstudio-pro#10419): Added user-friendly label support to job launcher image dropdown. Use the `::` delimiter to append a user-friendly label to images in `launcher.{plugin}.profiles.conf`\
*   (rstudio-pro#9838): Added a “Quit all” sessions action to the homepage\
*   (rstudio-pro#10337): Added on-hover tooltips to launcher dialog fields, with links to relevant documentation.\
*   (rstudio-pro#9818): Multiple custom OAuth integrations can now share the same issuer URL\
*   (rstudio-pro#5766): Added Proof Key for Code Exchange (PKCE) support for OpenID Connect authentication, enabled by default\
*   (rstudio-pro#10837): CLI administrative commands (including `interpreters`, user management commands such as `add-user`, `list-users`, `lock-user`, `set-admin`, and `unlock-user`, plus `user-service` and `upgrade positron`) can now be run by the configured Workbench service account (`server-user`, default `rstudio-server`) in addition to root. Previously these commands required root privileges.\
*   (rstudio-pro#10198): Added a startup check for the SELinux policy module when required.\
*   (rstudio-pro#9128): The `client-secret` field in `oauth-clients.conf`, `databricks.conf`, and `snowflake.conf` can now be encrypted\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2026.05.0-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-16)\
\
*   ([#17621](https://github.com/rstudio/rstudio/issues/17621)\
    ): Restored top alignment of argument names in the Help pane when running against R 4.6.0 or newer. R’s dynamic help server now emits an `id` attribute on section headers (e.g. `<h3 id='_sec_arguments'>Arguments</h3>`), which broke the literal-string match RStudio used to tag the Arguments header for styling.\
*   ([#17471](https://github.com/rstudio/rstudio/issues/17471)\
    ): Reformat Document with the styler formatter no longer inserts extra blank lines on Windows. The temporary file written by styler uses platform-native line endings (CRLF on Windows), and RStudio now normalizes those to LF when computing the edits to apply, so the diff against the LF-normalized in-memory document doesn’t produce spurious `\r` insertions that Ace would convert into blank lines.\
*   ([#17363](https://github.com/rstudio/rstudio/issues/17363)\
    ): Posit Assistant: pressing Escape to dismiss a ghost-text Next Edit Suggestion now also clears the Next Edit Suggestion (NES) gutter icon; previously the gutter icon remained visible after dismissal.\
*   ([#17589](https://github.com/rstudio/rstudio/issues/17589)\
    ): The diagnostics report now includes `positai.log` alongside `rdesktop.log` and the user’s `rsession-*.log`.\
*   ([#17665](https://github.com/rstudio/rstudio/issues/17665)\
    ): `.positai` and `.claude` are no longer added to a project’s `.Rbuildignore`, `.gitignore`, or `svn:ignore` unless those files/directories actually exist in the project; previously they were added whenever the AI assistant was enabled (the default), even in projects that had never used AI features. When `.positai`/`.claude` are subsequently created mid-session, the project’s ignore files are updated automatically.\
*   ([#17581](https://github.com/rstudio/rstudio/issues/17581)\
    ): Diagnostic gutter tooltips no longer show literal `<SPAN>` markup around the message; lint annotations now keep the original text alongside any rendered HTML so the tooltip renders cleanly while the diagnostics popup continues to support ANSI-colored content.\
*   ([#17556](https://github.com/rstudio/rstudio/issues/17556)\
    ): `difftime` objects (e.g. the result of subtracting two `Sys.time()` values) now show their formatted value in the Environment pane instead of an empty cell.\
*   ([#17568](https://github.com/rstudio/rstudio/issues/17568)\
    ): Source-mode spell check now flags misspelled words inside Markdown, R Markdown, and Quarto headings; previously only paragraph text was checked.\
*   ([#17481](https://github.com/rstudio/rstudio/issues/17481)\
    ): Fixed two debugger regressions: top-level breakpoints (e.g. via `debugSource()`) no longer fail to show the debug highlight or call stack, and multi-line input at the `Browse[N]>` prompt no longer clears the captured browser context.\
*   ([#3780](https://github.com/rstudio/rstudio/issues/3780)\
    ): The Files pane delete confirmation now reflects whether the file will be moved to the system Trash/Recycle Bin or permanently deleted, based on the “Delete files to Trash/Recycle Bin” preference.\
*   ([#3780](https://github.com/rstudio/rstudio/issues/3780)\
    ): When sending a file to the system Trash/Recycle Bin fails, the Files pane now reports the error and leaves the file on disk; previously it would silently fall back to permanently deleting the file.\
*   ([#12235](https://github.com/rstudio/rstudio/issues/12235)\
    ): RStudio Desktop’s Session > New Session now opens noticeably faster.\
*   ([#15614](https://github.com/rstudio/rstudio/issues/15614)\
    ): The splash screen can again be dismissed with a mouse click or key press.\
*   ([#15711](https://github.com/rstudio/rstudio/issues/15711)\
    ): Source-mode spell check no longer disappears on Quarto and R Markdown documents when the bundled YAML diagnostics worker fails to respond; spell-check lint is now applied independently of YAML lint.\
*   ([#16067](https://github.com/rstudio/rstudio/issues/16067)\
    ): Raise the open file descriptor soft limit at session startup to avoid “Too many open files” errors during project file monitoring on Linux.\
*   ([#16541](https://github.com/rstudio/rstudio/issues/16541)\
    ): Section headers now fold hierarchically based on heading level, matching Positron’s default behavior.\
*   ([#16966](https://github.com/rstudio/rstudio/issues/16966)\
    ): Restored the desktop terminal bell on Linux, now that the underlying Electron crash has been fixed.\
*   ([#17084](https://github.com/rstudio/rstudio/issues/17084)\
    ): The Shiny test commands (Record Test, Run Tests, Compare Results) now use the `shinytest2` package; `shinytest` has been deprecated.\
*   ([#17128](https://github.com/rstudio/rstudio/issues/17128)\
    ): The Windows installer’s File Version now matches its Product Version; previously the installer concatenated the major and minor version components into a single value that exceeded NSIS’s 16-bit-per-component limit and was truncated to an unrelated number.\
*   ([#17176](https://github.com/rstudio/rstudio/issues/17176)\
    ): Fixed a startup hang when opening a Quarto project containing large directories (e.g. `_targets/`).\
*   ([#17322](https://github.com/rstudio/rstudio/issues/17322)\
    ): Posit Assistant: invoking Uninstall Posit Assistant when it is not installed now shows the message “Posit Assistant is not installed.” and skips the restart, instead of silently restarting RStudio.\
*   ([#17417](https://github.com/rstudio/rstudio/issues/17417)\
    ): Added missing French translations for newer commands and preferences, removed an orphaned French key, deduplicated stale entries in the French application strings, and normalized line endings in five English string files.\
*   ([#17440](https://github.com/rstudio/rstudio/issues/17440)\
    ): Fixed an issue where triggering tab completion inside `[` on a large Matrix-package sparse matrix could hang RStudio and exhaust system memory.\
*   ([#17450](https://github.com/rstudio/rstudio/issues/17450)\
    ): Fixed a crash on Windows when `Rprofile.site` (or `.Rprofile`) called `download.file()`, `update.packages()`, or other code that emitted console output while RStudio’s R runtime dispatch layer was not yet initialized.\
*   ([#17506](https://github.com/rstudio/rstudio/issues/17506)\
    ): Source-marker messages in the Build, Markers, and Compile PDF panes are now rendered as plain text by default; only messages that the server explicitly marks as HTML (e.g. C++ Find Usages highlighting) are rendered via `innerHTML`.\
*   ([#17508](https://github.com/rstudio/rstudio/issues/17508)\
    ): Enabled the MathJax `Safe` extension in the IDE, the HTML preview, the presentation preview, and the rendered R Markdown viewer.\
*   ([#17510](https://github.com/rstudio/rstudio/issues/17510)\
    ): Data Import: column names, character options, locale values, and import URLs are now encoded as R string literals when generating preview and import code.\
*   ([#17530](https://github.com/rstudio/rstudio/issues/17530)\
    ): The spell-check context menu now shows the full set of correction suggestions; previously a stray loop increment caused every other suggestion to be skipped, capping the menu at 3 items instead of 5.\
*   ([#17534](https://github.com/rstudio/rstudio/issues/17534)\
    ): Fix uninformative error in `rstudio::sourceMarkers()` when `marker$type` is not a length-one vector.\
*   ([#4402](https://github.com/rstudio/rstudio/issues/4402)\
    ): Reindenting C/C++ code with a brace-less control-flow statement (e.g. a `for` whose body is a single braced `if`) no longer over-indents the line that follows the body.\
*   ([rstudio/rstudio-pro#10805](https://github.com/rstudio/rstudio-pro/issues/10805)\
    ): Server: Enable TCP keepalive on accepted connections so the operating system reaps half-open sockets from disappeared clients (browser tab hibernation, NAT timeouts) instead of holding them indefinitely.\
*   ([rstudio/rstudio-pro#10771](https://github.com/rstudio/rstudio-pro/issues/10771)\
    ): Reduced filesystem work performed by the `install.packages()` hook; the before/after scan is now scoped to the requested packages and their dependency closure rather than the entire library.\
*   ([rstudio/rstudio-pro#10771](https://github.com/rstudio/rstudio-pro/issues/10771)\
    ): Tightened the heuristic used to detect package-management commands at the console prompt, reducing spurious Packages pane refreshes triggered by identifiers like `updates <-` or `installed.packages()`.\
*   ([#17446](https://github.com/rstudio/rstudio/issues/17446)\
    ): The Packages pane now retrieves vulnerability information from Posit Package Manager via the `POST /filter/packages` endpoint, replacing the legacy `GET /repos/{repo}/vulns` endpoint that was temporarily unavailable in Package Manager `2026.04.0`.\
*   ([#17613](https://github.com/rstudio/rstudio/issues/17613)\
    ): Restored the column count in the data viewer status bar (e.g. “Showing rows 1 to 18 of 100,000 total rows, 500 total columns”), which had been dropped from the info bar in the vanilla-JS rewrite (#17382).\
*   ([#17612](https://github.com/rstudio/rstudio/issues/17612)\
    ): Limit horizontal overscroll in the data viewer so the last column remains visible at maximum scroll, instead of allowing all unpinned columns to be scrolled off-screen.\
*   ([#15211](https://github.com/rstudio/rstudio/issues/15211)\
    ): Restored honoring of the `COPILOT_AUTH_PROVIDER` environment variable, used to point Copilot at a GitHub Enterprise sign-in URL.\
*   ([rstudio/launcher#522](https://github.com/rstudio/launcher/issues/522)\
    ): Launcher Local plugin sessions on a node that goes offline in a load-balanced deployment are now marked `Failed` instead of remaining stuck in `Running`.\
*   ([rstudio/launcher#1536](https://github.com/rstudio/launcher/issues/1536)\
    ): Fixed a race condition in the Launcher Kubernetes plugin that could cause an intermittent crash (SIGSEGV) during stdin writes when the Kubernetes API server rejects the websocket upgrade.\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-20)\
\
*   (rstudio-pro#10885): Fixed database-connection contention and `SQLITE_BUSY` errors on the homepage when users with multiple Snowflake roles or Databricks instances loaded the page concurrently.\
*   (rstudio-pro#10734): Fixed a regression on the homepage that prevented new sessions from launching on projects marked as “not-found”. Sessions can be started after acknowledging a warning.\
*   (rstudio-pro#4017): Load balancing — recently-offlined nodes (within 5 minutes of transition) are now included in the node-state sync sent to Job Launcher with their actual `Offline` or `Deleting` status. This lets the launcher mark sessions on offline nodes as `Failed` more promptly during admin-initiated node removals, reducing the worst-case detection window from ~3 minutes (silent-absence) to ~60 seconds (one launcher sync cycle). (Companion to rstudio/launcher#1514.)\
*   (rstudio-pro#9477): Fixed Snowflake `client-secret` field not showing as required in the admin config UI\
*   (rstudio-pro#9631): Managed credentials are now removed from the database when their section is removed from `oauth-clients.conf`, `snowflake.conf`, or `databricks.conf` and Workbench is restarted.\
*   (rstudio-pro#10884): Sign-in pages now display the inactivity timeout as a human-friendly duration (e.g., “3 days” or “2 days, 23 hours, and 59 minutes”) instead of a raw number of minutes.\
*   (rstudio-pro#9637): When Just-In-Time (JIT) user provisioning is active, users are now de-assigned from groups that have been removed from the Single Sign-On (SSO) groups claim (OpenID, SAML, and proxied-auth) on subsequent login.\
*   (rstudio-pro#9965): Direct file downloads from the Files pane now generate `session_file_download` audit events, matching the behavior of downloads via More -> Export.\
*   (rstudio-pro#9764): Fixed hang in `rstudio-server restart` when SELinux is in enforcing mode.\
*   (rstudio-pro#10974): Fixed a regression in how user settings are handled that prevented Positron Pro sessions from launching.\
*   (rstudio-pro#10720): Improved the performance of joining VS Code and Positron session by caching static resources.\
\
### Upgrade Instructions[](https://docs.posit.co/ide/news/#rstudio-2026.05.0-upgrade)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-21)\
\
*   Container image transition: Posit Workbench container images are moving from the `rstudio/*` Docker Hub organization to `posit/*` on Docker Hub (also published as `ghcr.io/posit-dev/*` on the GitHub Container Registry). Legacy `rstudio/*` images continue to be built during the transition. If you use the Workbench Helm chart, version `0.20.0` and later default to the new image repositories and include breaking changes. See the Helm chart [Migrating to Posit Images](https://docs.posit.co/helm/docs/migrating-to-posit-images.html)\
     guide for details.\
*   Existing users must re-authenticate to each Custom OAuth integration after upgrading. Snowflake and Databricks integrations are unaffected.\
*   Downgrading to a release older than 2026.05.0 (Golden Wattle) requires Custom OAuth users to re-authenticate. Snowflake and Databricks integrations are unaffected. On older releases, only the last Custom OAuth section for a given authorize or token URL is operational. Reduce the configuration to one integration per authorize or token URL before downgrading.\
*   Administrators who previously enforced `positron.assistant.enable` in Positron settings should instead set `assistant-enabled` in `/etc/rstudio/profiles`; `positron.assistant.enable` will be deprecated in a future release. See [Posit Assistant Admin Controls](https://docs.posit.co/ide/server-pro/admin/ai/assistant-controls.html)\
    .\
*   Proof Key for Code Exchange (PKCE) provides enhanced security during user logins when using OpenID Connect authentication, so it is enabled by default. It can be disabled if necessary by setting `auth-openid-pkce-enabled=0` in `rserver.conf`.\
\
### Dependencies[](https://docs.posit.co/ide/news/#rstudio-2026.05.0-dependencies)\
\
*   Ace 1.43.5\
*   Copilot Language Server 1.480.0\
*   Electron 41.5.0\
*   Job Launcher 2.24.0\
*   Node.js 22.22.2 (copilot, Posit AI)\
*   Quarto 1.9.37\
*   rserver-openid 0.9.0\
*   xterm.js 6.0.0\
*   Positron 2026.05.2-3\
*   PWB Code Server 2026.05-b2746\
*   Code OSS 1.111.0\
\
2026.04.0[](https://docs.posit.co/ide/news/#rstudio-2026.04.0)\
\
---------------------------------------------------------------\
\
**“Globemaster Allium”** | Date: 2026-04-22\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2026.04.0-new)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-17)\
\
*   Added **Posit Assistant** and **Next Edit Suggestions (NES)**, which can be powered by a [Posit AI](https://posit.ai/)\
     subscription. See the [Posit Assistant documentation](https://pos.it/assistant-docs)\
     for setup instructions.\
*   Support for the upcoming R 4.6.0 release\
*   ([#10296](https://github.com/rstudio/rstudio/issues/10296)\
    ): Modal dialogs (Global Options, Project Options, etc.) now support dark theme styling when a dark editor theme is active, controlled by the new `use_dark_theme_modal_dialogs` preference\
*   ([#17070](https://github.com/rstudio/rstudio/issues/17070)\
    ): Added support for the ANSI Erase in Line (EL / CSI K) escape sequence in the console, improving rendering of progress bars and status updates from CLI tools\
*   ([#16657](https://github.com/rstudio/rstudio/issues/16657)\
    ): Added color preview support for YAML files, highlighting hex colors and named R colors\
*   ([#16734](https://github.com/rstudio/rstudio/issues/16734)\
    ): Added mouse wheel support for scrolling pane tabs when there are more tabs than can fit in the visible area\
*   (#rstudioapi/316): The documentNew API now permits arbitrary file types and extensions\
*   ([#3780](https://github.com/rstudio/rstudio/issues/3780)\
    ): Deleting files from Files pane on Linux Desktop now sends files to the Trash\
*   ([#3780](https://github.com/rstudio/rstudio/issues/3780)\
    ): On RStudio Desktop, the Files pane dropdown menu has a new option to control if deleted files go to Trash/Recycle Bin or are permanently deleted\
*   ([#16903](https://github.com/rstudio/rstudio/issues/16903)\
    ): Changed the default location of the Sidebar pane to be on the left side of the window\
*   ([#16942](https://github.com/rstudio/rstudio/issues/16942)\
    ): Enforce a minimum width for the Sidebar pane\
*   ([#17269](https://github.com/rstudio/rstudio/issues/17269)\
    ): Added a close button to the Sidebar pane toolbar for quickly hiding the sidebar\
*   ([#17000](https://github.com/rstudio/rstudio/issues/17000)\
    ): Always show .positai folder in Files pane even when set to hide hidden files\
*   ([#16069](https://github.com/rstudio/rstudio/issues/16069)\
    ): Function auto-completion will now include arguments inherited via @inheritDotParams\
*   ([#16530](https://github.com/rstudio/rstudio/issues/16530)\
    ): Added Posit Connect Cloud as a publishing target\
*   ([#17330](https://github.com/rstudio/rstudio/issues/17330)\
    ): Added Help > Release Notes command to open the RStudio release notes in the browser\
*   ([#15360](https://github.com/rstudio/rstudio/issues/15360)\
    ): Added `r-max-connections` session option to configure the maximum number of R connections (requires R >= 4.4.0)\
*   ([#16671](https://github.com/rstudio/rstudio/issues/16671)\
    ): Added support for displaying Copilot next-edit suggestions (NES) inline in the editor\
*   ([#16722](https://github.com/rstudio/rstudio/issues/16722)\
    ): Clicking the “Copilot: Completion response received” status bar indicator now navigates to the most recent Copilot edit suggestion\
*   ([#17231](https://github.com/rstudio/rstudio/issues/17231)\
    ): Added an optional project trust dialog that prompts before executing `.Rprofile`, `.Renviron`, and `.RData` in untrusted projects; enable with `project-trust-dialogs=1` in `rsession.conf`\
*   ([#17344](https://github.com/rstudio/rstudio/issues/17344)\
    ): Console process dialogs (e.g. package installation progress) now honor the active dark editor theme\
*   ([#17369](https://github.com/rstudio/rstudio/issues/17369)\
    , [#17371](https://github.com/rstudio/rstudio/issues/17371)\
    ): Added a “What’s New” window that appears on first launch after upgrading to a new release; automation environments can suppress it by setting `RSTUDIO_DISABLE_WHATS_NEW=1`\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-22)\
\
*   Added Preview support for **Posit Assistant** in Positron Pro sessions, with Workbench-managed credentials for Amazon Bedrock, Snowflake Cortex, and Microsoft Foundry. See the [Posit Assistant documentation](https://pos.it/assistant-docs)\
     for setup instructions.\
*   (rstudio-pro#10032): Added Positron Pro support for SUSE Linux 15 SP7 and openSUSE 15.6, enabling Positron by default on these platforms\
*   (rstudio-pro#9933): Moved the Positron Pro custom bootstrap extensions directory from `/usr/lib/rstudio-server/bin/positron-server/extensions/custom-bootstrap` to `/etc/rstudio/positron-custom-bootstrap`. Existing extensions are migrated automatically on upgrade.\
*   (rstudio-pro#9824): Added support for upgrading Positron independently of Workbench upgrades, allowing administrators to install new Positron releases without performing a full Workbench upgrade\
*   (rstudio-pro#4368): Added version end of life warning banner to the admin dashboard. The warning threshold is configurable with `workbench-admin-version-expiration-warning-days` (default 182 days).\
*   (rstudio-pro#1216): Added server version and license information to the admin “server” page. Includes a mechanism to automatically check for updates and display a banner when a new version is available\
*   (rstudio-pro#9073): Added support for `rstudioapi::getDelegatedAzureToken` in VS Code and Positron sessions\
*   (rstudio-pro#9679): Added support for `getDelegatedAzureToken` for Python via the Posit SDK\
*   (rstudio-pro#9132): Added an Available Credentials pane in the Workbench Extension for discovering and using custom OAuth integration credentials in VS Code and Positron sessions\
*   (rstudio-pro#9136): Added command palette commands in VS Code and Positron for interacting with custom OAuth credentials\
*   (rstudio-pro#3060): Added console input auditing for Positron sessions, capturing both R and Python console activity when `audit-r-console` is enabled\
*   (rstudio-pro#9228): Added full support for database-backed session metadata storage by setting `session-use-file-storage=0` in `rserver.conf`\
*   (rstudio-pro#10246): Added support for setting session timeout kill hours in `/etc/rstudio/profiles` for VS Code and Positron sessions when session metadata database storage is configured with `session-use-file-storage=0` in `rserver.conf`\
*   (rstudio-pro#9294): Added support for Debian 13 (Trixie) as an install target for Posit Workbench and its bundled session components\
*   (rstudio-pro#9770): Cached SSL contexts to reduce per-request TLS handshake overhead during session launch\
*   (rstudio-pro#10013): Added the ability for Workbench to host Positron documentation locally. This ensures offline access to documentation that matches the version of Positron running in Workbench.\
*   (rstudio-pro#10346): Added a prompt asking users to confirm trust for a project before executing its startup files (`.Rprofile`, `.Renviron`, etc.) in RStudio sessions\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2026.04.0-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-18)\
\
*   ([#17005](https://github.com/rstudio/rstudio/issues/17005)\
    ): Fixed an issue where the Packages pane was empty when non-PPM repositories were configured alongside PPM repositories and certain packages were installed\
*   ([#16632](https://github.com/rstudio/rstudio/issues/16632)\
    ): Fixed an issue where not all new files would appear in the Files pane after a git pull\
*   ([#16714](https://github.com/rstudio/rstudio/issues/16714)\
    ): Fixed an issue where formatting edits with air did not behave well with the editor undo stack\
*   ([#16732](https://github.com/rstudio/rstudio/issues/16732)\
    ): Fixed an issue where TabSet1 with no tabs assigned would show the Sidebar title\
*   ([#16733](https://github.com/rstudio/rstudio/issues/16733)\
    ): Fixed an issue where a Presentation tab would be added to TabSet2 when it was assigned to the Sidebar\
*   ([#16771](https://github.com/rstudio/rstudio/issues/16771)\
    ): Clarified in documentation that additional source columns are added to the left\
*   ([#8531](https://github.com/rstudio/rstudio/issues/8531)\
    ): Fixed an issue where table chunk outputs did not use all available space when printing\
*   ([#16740](https://github.com/rstudio/rstudio/issues/16740)\
    ): Fixed an issue with opening files from operating system file manager when RStudio had a secondary window open\
*   ([#16688](https://github.com/rstudio/rstudio/issues/16688)\
    ): Fixed an issue with pane layout when exiting RStudio with a zoomed column region\
*   ([#16798](https://github.com/rstudio/rstudio/issues/16798)\
    ): Fixed an issue where whole-word search and replace would not correctly match search terms containing dots\
*   ([#16814](https://github.com/rstudio/rstudio/issues/16814)\
    ): Fixed an issue where apostrophes in file names were displayed as HTML entities in the Files pane\
*   ([#16834](https://github.com/rstudio/rstudio/issues/16834)\
    ): Fixed an issue where an error message was shown on Windows when using “Write Diagnostics File”\
*   ([#16839](https://github.com/rstudio/rstudio/issues/16839)\
    ): Fixed an issue where an inaccessible folder in the PATH on Windows would lead to unnecessary file access attempts and error logging\
*   ([#16845](https://github.com/rstudio/rstudio/issues/16845)\
    ): Fixed issue where adding source columns or changing Sidebar visibility in Pane Layout options caused Console column to fill entire window\
*   ([#16885](https://github.com/rstudio/rstudio/issues/16885)\
    ): Fixed an issue where console warning annotation boxes could include excess content\
*   ([#16842](https://github.com/rstudio/rstudio/issues/16842)\
    ): Fixed issue where Packages pane checkboxes did not display the correct state for renv projects using a shared cache\
*   ([#16985](https://github.com/rstudio/rstudio/issues/16985)\
    ): Fixed an issue where the Environment pane would drop the first list element when a user-defined `str` method existed in the global environment\
*   ([#16995](https://github.com/rstudio/rstudio/issues/16995)\
    ): Fixed an issue where the chunk toolbar could be duplicated when pressing Enter after a chunk header at the end of a document\
*   ([#17026](https://github.com/rstudio/rstudio/pull/17026)\
    ): Fixed an issue where roxygen parentheses interfered with Ctrl+Enter execution\
*   ([#14626](https://github.com/rstudio/rstudio/issues/14626)\
    ): Fixed an issue where RStudio-specific file type icons (e.g. .Rmd, .qmd, .Rpres) were not shown in file managers on Linux\
*   ([#15609](https://github.com/rstudio/rstudio/issues/15609)\
    ): Fixed an issue where RStudio startup on Windows was delayed by several seconds on systems with endpoint security software\
*   ([#15863](https://github.com/rstudio/rstudio/issues/15863)\
    ): Fixed an issue where “Use Selection for Find” (Cmd+E) incorrectly jumped to the next match instead of only populating the find bar\
*   ([#16838](https://github.com/rstudio/rstudio/issues/16838)\
    ): Fixed an issue where inline notebook and Quarto plots were blurry on HiDPI displays when custom figure dimensions were specified\
*   ([#17095](https://github.com/rstudio/rstudio/issues/17095)\
    ): Fixed an issue where declining to save a file with an unexpected extension would disable saving for that file\
*   ([#17115](https://github.com/rstudio/rstudio/issues/17115)\
    ): Fixed an issue on macOS Desktop where the “Close” keyboard shortcut in secondary windows (e.g. Shiny app, Help pop-out) were also processed by the main window\
*   ([#14882](https://github.com/rstudio/rstudio/issues/14882)\
    ): Fixed an issue where YAML comments in R Markdown documents were dropped or displaced when the front matter was modified (e.g. when toggling “Chunk Output in Console”)\
*   ([#17333](https://github.com/rstudio/rstudio/issues/17333)\
    ): Fixed an issue where the publishing wizard would fail when publishing Quarto documents with Quarto v1.9\
*   ([#6260](https://github.com/rstudio/rstudio/issues/6260)\
    ): Fixed an issue where a chunk could become unrunnable after editing the chunk’s code while its debugger was active\
*   ([#6279](https://github.com/rstudio/rstudio/issues/6279)\
    ): Fixed an issue where the Insert Chunk shortcut (Ctrl+Alt+I) did not work when the R Markdown editor was popped out into a separate window\
*   ([#13425](https://github.com/rstudio/rstudio/issues/13425)\
    ): Fixed an issue where Find and Replace with “whole word” enabled would not replace occurrences of operators such as `%>%` or `|>`\
*   ([#15631](https://github.com/rstudio/rstudio/issues/15631)\
    ): Fixed an issue where parentheses inside Roxygen comments could prevent interactive execution of the following code with Ctrl+Enter\
*   ([#16490](https://github.com/rstudio/rstudio/issues/16490)\
    ): Fixed an issue where editor breakpoints set inside S7 method definitions were ignored\
*   ([#16593](https://github.com/rstudio/rstudio/issues/16593)\
    ): Fixed an issue where RStudio on Windows could not create or open projects stored on network drives\
*   ([#16660](https://github.com/rstudio/rstudio/issues/16660)\
    ): Fixed an issue where resizing a clamped editor did not take effect until the editor was interacted with\
*   ([#16721](https://github.com/rstudio/rstudio/issues/16721)\
    ): Fixed an issue where the presence of an `air.toml` file caused Air formatting to be applied on save even when the global “Format on save” option was disabled\
*   ([#16756](https://github.com/rstudio/rstudio/issues/16756)\
    ): Fixed an issue where Find and Replace with “whole word” enabled would not replace search strings that begin with a dot\
*   ([#16766](https://github.com/rstudio/rstudio/issues/16766)\
    ): Fixed an issue where restoring a session with a very large accumulated console history could cause RStudio to freeze\
*   ([#16808](https://github.com/rstudio/rstudio/issues/16808)\
    ): Fixed an issue where apostrophes in file and folder names were displayed as the HTML entity `&#39;` in the Files pane on Windows with the French locale\
*   ([#16962](https://github.com/rstudio/rstudio/issues/16962)\
    ): Fixed an issue where Vim paragraph-navigation keybindings (`{` and `}`) could reverse direction on Swiss keyboard layouts\
*   ([#16987](https://github.com/rstudio/rstudio/issues/16987)\
    ): Fixed an issue where debugging a `[[` method on a list-class object could hang the R session\
*   ([#17007](https://github.com/rstudio/rstudio/issues/17007)\
    ): Fixed an issue where some Alt-based editor keybindings (e.g. Alt+-) did not work on Windows 11 25H2\
*   ([#17099](https://github.com/rstudio/rstudio/issues/17099)\
    ): Fixed a JavaScript “Object has been destroyed” error that could appear when quitting RStudio Desktop\
*   ([#17135](https://github.com/rstudio/rstudio/issues/17135)\
    ): Fixed an issue where RStudio Desktop could crash silently after the startup logo on some Windows 10 systems\
*   ([#17159](https://github.com/rstudio/rstudio/issues/17159)\
    ): Fixed an issue where C++ code completion stopped working in packages that set `CXX_STD = CXX20` in `Makevars`\
*   ([#17243](https://github.com/rstudio/rstudio/issues/17243)\
    ): Fixed an issue where `@inheritDotParams` autocompletion did not separate grouped argument lists (e.g. `n, prop`) or handle masked functions correctly\
*   ([#17263](https://github.com/rstudio/rstudio/issues/17263)\
    ): Fixed an issue where RStudio Desktop on Windows crashed on startup when used with R-devel at SVN revision 89661 or later\
*   ([#17353](https://github.com/rstudio/rstudio/issues/17353)\
    ): Fixed an issue where RStudio could crash at startup when a package listed in the user’s R startup environment failed to load\
*   ([#17373](https://github.com/rstudio/rstudio/issues/17373)\
    ): Fixed spurious warnings and errors shown in the console at startup when RStudio was launched against older R versions such as R 3.6.x\
*   ([#17391](https://github.com/rstudio/rstudio/issues/17391)\
    ): Fixed an issue where Push Button Deploy to Connect Cloud would fail with a confusing “function doesn’t exist” error when an outdated version of `rsconnect` was installed; RStudio now surfaces the required `rsconnect` version\
*   ([#17412](https://github.com/rstudio/rstudio/issues/17412)\
    ): Expanded Push Button Deploy to Connect Cloud so it supports the same document and project types already supported for Connect\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-23)\
\
*   (rstudio-pro#10071): Fixed an issue where `get_audited_job_details` returned HTTP 500 when public key files were missing\
*   (rstudio-pro#3334): Fixed an issue where durations over 24 hours would render incorrectly in the admin dashboard\
*   (rstudio-pro#10432): Fixed an issue where GitHub Copilot was broken in session components because Node.js was not included in session packages or init containers\
*   (rstudio-pro#10234): Fixed an issue where OIDC token expiration was incorrectly calculated during token refresh\
*   (rstudio-pro#10031): Fixed an issue where the admin configuration manager could delete configuration files\
*   (rstudio-pro#9187): Fixed an issue where the admin configuration manager was not reporting errors for incorrect section headers\
*   (rstudio-pro#9873): Fixed an issue where SAML authentication failed with large assertions\
*   (rstudio-pro#9334): Fixed an issue where SCIM or JIT provisioned users with special character usernames appeared as “Inactive” but could still start sessions\
*   (rstudio-pro#6554): Fixed an issue where locking or deactivating a SCIM or JIT provisioned user did not immediately sign them out of Workbench\
*   (rstudio-pro#9176): Fixed an issue where warnings about Databricks being enabled with a Basic license would appear even when `databricks-enabled=0` was set in `rserver.conf`\
*   (rstudio-pro#5643): Fixed an issue where locking or deactivating a single user could log other unrelated users out of their active sessions\
*   (rstudio-pro#8084): Fixed an issue where `rworkspaces` child processes were not terminated when Workbench was stopped, leaving stale processes on the system\
*   (rstudio-pro#8790): Fixed an issue where the homepage briefly displayed the full home directory path (e.g. `/home/user`) instead of `~` for a newly-started RStudio session before it had been opened\
*   (rstudio-pro#9044): Fixed an issue where resumed Workbench sessions could be removed due to a failed `ActiveSession` validation when the session was not associated with a project\
*   (rstudio-pro#9215): Corrected the spelling of “PostgreSQL” in the Connections pane\
*   (rstudio-pro#9383): Fixed a deadlock in `rserver` that could occur when database connection-health checks hung indefinitely\
*   (rstudio-pro#9417): Fixed an issue where sessions could stick in “Launching” after a single-node restart in a load-balanced cluster when `auth-pam-sessions-use-password` was enabled\
*   (rstudio-pro#9451): Fixed an issue where the Sessions dropdown in the RStudio IDE displayed the RStudio logo for Positron sessions instead of the Positron logo\
*   (rstudio-pro#9502): Fixed an issue where Positron failed to install bundled extensions into a shared global extensions directory due to file permission errors on the session user\
*   (rstudio-pro#9724): Fixed an issue where setting `XDG_DATA_HOME` to a directory that did not already exist was silently ignored; the directory is now created if possible\
*   (rstudio-pro#9730): Fixed a race condition that could cause a 30-second delay before the homepage reflected a session’s transition from “Starting” to “Active”\
*   (rstudio-pro#9747): Improved the performance of `launch_session` by removing mutex bottlenecks around license-warning checks and per-user profile lookups\
*   (rstudio-pro#9765): Fixed unnecessary error-log output on systems where cgroup control files such as `cpu.max` are not writable\
*   (rstudio-pro#9809): Fixed an issue where `rstudio-server force-suspend-session` could leave the target session in the “Failed” state instead of “Suspended”\
*   (rstudio-pro#9841): Fixed an issue with configuring multiple scopes on a single Entra ID custom OAuth provider\
*   (rstudio-pro#9847): Fixed accessibility issues with undiscoverable button labels in the admin configuration editor\
*   (rstudio-pro#9850): Fixed accessibility issues with undiscoverable button labels on the Workbench homepage\
*   (rstudio-pro#9852): Fixed accessibility issues with missing focus indicators on the Workbench homepage\
*   (rstudio-pro#9855): Fixed accessibility issues with keyboard-driven column sorting in the Projects and Jobs tables on the Workbench homepage\
*   (rstudio-pro#9856): Fixed remaining critical accessibility issues on the Projects page\
*   (rstudio-pro#9875): Fixed an intermittent “config out of range” error in `rserver` that could cause HTTP 502 responses on `launch_session` in environments affected by a Boost 1.87 issue\
*   (rstudio-pro#9879): Improved the error message for RStudio’s “Invalid session scope” startup failure to include the resolved paths\
*   (rstudio-pro#9885): Fixed an issue where quitting a session in Failed, Shutting Down, Killed, or Canceled state from the homepage did not issue a `shutdown_sessions` request, leaving the session record stuck\
*   (rstudio-pro#9938): Fixed an issue where the “New R Session” dialog displayed “undefined” for the CPU and memory limit fields when no defaults were configured\
*   (rstudio-pro#10167): Fixed quit behavior so rserver performs a clean shutdown of RStudio sessions via an authenticated server-side channel instead of an abrupt abort, and closed a related CSRF weakness on `/rpc/abort`\
*   (rstudio-pro#10205): Fixed an issue where starting a Positron or VS Code session with `XDG_DATA_HOME` set caused the default working-directory path to be auto-generated under the XDG path\
*   (rstudio-pro#10258): Fixed an issue where the `/rstudio/` URL prefix was missing from Workbench navigation when sessions were launched via the API in proxy environments\
*   (rstudio-pro#10319): Fixed Jupyter timeout and session-culling settings so inactive kernels and sessions are shut down as configured\
*   (rstudio-pro#10530): Fixed an issue where clicking Quit on a load-balanced RStudio session running on another node left the session stuck in “Shutting down” because the `quit_session` RPC bypassed the cross-node proxy\
\
### Upgrade Instructions[](https://docs.posit.co/ide/news/#rstudio-2026.04.0-upgrade)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-24)\
\
Positron Pro is now enabled by default on SUSE Linux 15 SP7 and openSUSE 15.6. On fresh installs, the default `positron.conf` and `positron-user-settings.json` configuration files are automatically generated, matching the behavior on other supported platforms. No action is needed if you are upgrading an existing installation that already has these files configured.\
\
Positron Assistant provider and model settings have changed from a centralized format to per-provider individual settings. If you have configured any of the following settings in `positron-user-settings.json` or `enforced-settings.json`, they must be updated:\
\
*   `positron.assistant.enabledProviders` — replace with individual `positron.assistant.provider.<name>.enable` settings (for example, `positron.assistant.provider.amazonBedrock.enable: true`)\
*   `positron.assistant.models.preference.byProvider` — replace with individual `positron.assistant.models.preference.<name>` settings (for example, `positron.assistant.models.preference.anthropic: "Claude Sonnet 4.5"`)\
*   `positron.assistant.models.custom` — replace with individual `positron.assistant.models.overrides.<name>` settings (for example, `positron.assistant.models.overrides.customProvider: [...]`)\
\
Positron automatically migrates these settings in a user’s personal `settings.json`, but does not auto-migrate Workbench configuration files. See the [Positron Assistant](https://docs.posit.co/ide/server-pro/2026.04.0/admin/positron_sessions/positron-assistant.html#language-model-providers)\
 admin guide for the updated settings.\
\
### Dependencies[](https://docs.posit.co/ide/news/#rstudio-2026.04.0-dependencies)\
\
*   Ace 1.43.5\
*   Copilot Language Server 1.459.0\
*   Electron 39.8.7\
*   Launcher 2.21.0\
*   Node.js 22.20.0 (vscode server)\
*   Node.js 22.22.2 (copilot, Posit AI)\
*   Quarto 1.9.36\
*   rserver-saml 0.9.2\
*   xterm.js 6.0.0\
*   nginx 1.29.8\
*   Boost 1.90\
*   PWB Code Server 1.109.2\
*   Positron 2026.04.1-10\
\
2026.01.2[](https://docs.posit.co/ide/news/#rstudio-2026.01.2)\
\
---------------------------------------------------------------\
\
**“Apple Blossom”** | Date: 2026-03-27\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2026.01.2-new)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-19)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-25)\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2026.01.2-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-20)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-26)\
\
*   (rstudio-pro#9896): Fixed an issue where sessions failed to launch with an “Invalid session scope 2” error after upgrading from 2025.09 to 2026.01\
*   (rstudio-pro#10052): Fixed an issue where IPv6 URLs were not parsed correctly\
*   (rstudio-pro#10180): Fixed an issue where R console auditing failed to generate output files when enabled\
*   (rstudio-pro#10438): Fixed an issue where Positron was incorrectly marked as being in Preview on the legacy homepage\
\
### Deprecated / Removed[](https://docs.posit.co/ide/news/#rstudio-2026.01.2-deprecated)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-21)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-27)\
\
### Dependencies[](https://docs.posit.co/ide/news/#rstudio-2026.01.2-dependencies)\
\
2026.01.1[](https://docs.posit.co/ide/news/#rstudio-2026.01.1)\
\
---------------------------------------------------------------\
\
**“Apple Blossom”** | Date: 2026-02-19\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2026.01.1-new)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-22)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-28)\
\
*   ([#7593](https://github.com/rstudio/rstudio/issues/7593)\
    ): Added Azure Load Balanced Reference Architecture\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2026.01.1-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-23)\
\
*   ([#16819](https://github.com/rstudio/rstudio/issues/16819)\
    ): Fixed an issue where Ctrl + F failed to activate Find dialog in Visual mode\
*   ([#16950](https://github.com/rstudio/rstudio/issues/16950)\
    ): Fixed an issue where Air formatting was not applied when reformatting a code selection\
*   (rstudio-pro#9882): Improved OpenSSL compatibility for RHEL 9 by building on RHEL 9.4 to ensure builds are linked against OpenSSL 3.0\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-29)\
\
*   (rstudio-pro#9880): Fixed an issue where the system logs an error when the `audited-jobs-private-key-path` configuration is missing and audited jobs remain disabled.\
*   (rstudio-pro#9790): Fixed an issue in 2026.01 where users could not login if using the option `auth-pam-sessions-use-password=1`.\
*   (rstudio-workbench-vscode-ext#422): Fixed an issue where opening the home directory as a folder in Positron or VS Code caused many files to be created in the directory `~/.local/share/pwb/recent_projects` that could affect the ability to login later.\
\
### Deprecated / Removed[](https://docs.posit.co/ide/news/#rstudio-2026.01.1-deprecated)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-24)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-30)\
\
### Dependencies[](https://docs.posit.co/ide/news/#rstudio-2026.01.1-dependencies)\
\
*   Positron 2026.02.0: Positron Assistant has switched to using a native implementation of the GitHub Copilot completion engine. Users who are already logged into GitHub Copilot need to sign out and sign back in via the Accounts menu. See this [discussion post](https://github.com/posit-dev/positron/discussions/11340)\
     for details.\
*   RHEL 9 linked against OpenSSL 3.0\
\
2026.01.0[](https://docs.posit.co/ide/news/#rstudio-2026.01.0)\
\
---------------------------------------------------------------\
\
**“Apple Blossom”** | Date: 2026-01-06\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2026.01.0-new)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-25)\
\
*   ([#10567](https://github.com/rstudio/rstudio/issues/10567)\
    ): Added tools for searching within Console output and Build output\
*   ([#15928](https://github.com/rstudio/rstudio/issues/15928)\
    ): Added support for using Air to format R code in projects configured to use it\
*   ([#16127](https://github.com/rstudio/rstudio/issues/16127)\
    ): Added a keyboard shortcut to dismiss Copilot ghost text with the Escape key\
*   ([#16415](https://github.com/rstudio/rstudio/issues/16415)\
    ): Added completions for the `_` placeholder in piped expressions in RStudio\
*   ([#16281](https://github.com/rstudio/rstudio/issues/16281)\
    ): Added `suppressTypeInference` attribute to disable inferring types during completion\
*   ([#16375](https://github.com/rstudio/rstudio/issues/16375)\
    ): Changed Copilot Language Server (completions) to launch via Node.js instead of as a standalone binary\
*   ([#16427](https://github.com/rstudio/rstudio/issues/16427)\
    ): Added diagnostic warning for invocations of `paste()` with unexpected named arguments\
*   ([#16480](https://github.com/rstudio/rstudio/issues/16480)\
    ): Added full-height “Sidebar” pane to RStudio\
*   ([#16435](https://github.com/rstudio/rstudio/issues/16435)\
    ): Added user preference to toggle visibility of the Source column in the Packages pane\
*   ([#16466](https://github.com/rstudio/rstudio/issues/16466)\
    ): Added “Soft-wrap at margin column” and “Clamp editor width to margin column” preferences\
*   ([#16580](https://github.com/rstudio/rstudio/issues/16580)\
    ): Added “Restore default pane and tab layout” command to reset pane and tab layout to defaults\
*   ([#16322](https://github.com/rstudio/rstudio/issues/16322)\
    ): Added configuration option for “Rename in Scope” in R Markdown / Quarto documents to operate on all chunks in the document or only the current chunk\
*   ([#16383](https://github.com/rstudio/rstudio/issues/16383)\
    ): Changed “Run Document” command to execute Quarto documents with `server: shiny` via `quarto serve`\
*   ([#16466](https://github.com/rstudio/rstudio/issues/16466)\
    ): Added support for soft-wrapping text at a specific column (the margin)\
*   ([#16227](https://github.com/rstudio/rstudio/issues/16227)\
    ): Added support for the `netrc` option in R >= 4.6.0\
*   (rstudio-pro#6675): Added support for RSA-OAEP when encrypting passwords on the sign-in page\
*   (rstudio-pro#6377): Added CSRF protection to the export file API\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-31)\
\
*   (rstudio-pro#9506): Added `auth-openid-aws-role-claim` and `auth-openid-aws-session-name-claim` settings to allow mapping custom OIDC claim names for AWS credentials\
*   (rstudio-pro#9088): Added support for admin-enforced settings in Positron\
*   (rstudio-pro#9106): Added support for managing R and Python interpreters for Workbench Jobs in Positron and VS Code\
*   (rstudio-pro#9106): Improved support for running Workbench Jobs using Python virtual environments in Positron\
*   (rstudio-pro#9106): Added support for running Workbench Jobs using R in Positron\
*   (rstudio-pro#9560): Updated the Posit Workbench Documentation site, the RStudio Desktop Administration Guide, the RStudio IDE User Guide, and RStudio & Posit Workbench Release Notes to v8.0.1 of the Posit product documentation theme\
*   (rstudio-pro#8920): Added option to remove recent projects from Workbench home page\
*   (rstudio-pro#9550): Added `POSIT_PRODUCT` environment variable with value “WORKBENCH” to all Sessions and jobs\
*   (rstudio-pro#9585): Added revocation logic for Session RPC cookies when a session ends (exit, suspension, or halt) or when the related user account is locked, ensuring immediate invalidation of credentials\
*   (rstudio-pro#9169): Added `use-legacy-homepage` option to allow admins to set the legacy home page as the default during the deprecation window\
*   (rstudio-pro#9065, rstudio-pro#9074): Added support for custom OAuth managed credentials\
*   (rstudio-pro#5913): Added support for managed credentials in Workbench Jobs\
*   (rstudio-pro#9224): Added support for projects in `get_session` and `launch_session` Workbench APIs\
*   (rstudio-pro#6426): Added long-polling support to `get_session` Workbench API\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2026.01.0-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-26)\
\
*   ([#16398](https://github.com/rstudio/rstudio/issues/16398)\
    ): Fixed an issue where ANSI codes were rendered incorrectly in warning messages captured while rendering plots\
*   ([#16331](https://github.com/rstudio/rstudio/issues/16331)\
    ): Fixed an issue where previously-registered global calling handlers on startup would be removed\
*   ([#13470](https://github.com/rstudio/rstudio/issues/13470)\
    ): Removed unintended positioning data when creating patchwork objects in R Markdown chunks\
*   ([#16337](https://github.com/rstudio/rstudio/issues/16337)\
    ): Fixed an issue where R error output was not displayed in rare cases\
*   ([#15963](https://github.com/rstudio/rstudio/issues/15963)\
    ): Fixed an issue where an unsaved R Markdown document could erroneously be marked as saved after executing a chunk\
*   ([#16402](https://github.com/rstudio/rstudio/issues/16402)\
    ): Fixed an issue where Quarto rendering would use the wrong Python installation\
*   ([#16457](https://github.com/rstudio/rstudio/issues/16457)\
    ): Adjusted width of the standalone Accessibility Options dialog to fully display the pane\
*   ([#16532](https://github.com/rstudio/rstudio/issues/16352)\
    ): Fixed an issue where ongoing R Markdown render output was lost after a browser refresh\
*   ([#14510](https://github.com/rstudio/rstudio/issues/14510)\
    ): Fixed an issue where gutter icons were incorrectly presented for spellcheck issues\
*   ([#16474](https://github.com/rstudio/rstudio/issues/16474)\
    ): Adjusted Pane Layout options UI to improve space utilization\
*   ([#16471](https://github.com/rstudio/rstudio/issues/16471)\
    ): Fixed an issue where Copilot status messages appeared below editor when Copilot was disabled\
*   ([#16423](https://github.com/rstudio/rstudio/issues/16423)\
    ): Fixed an issue where a Copilot warning appeared when closing a document it was told to ignore\
*   ([#16509](https://github.com/rstudio/rstudio/issues/16509)\
    ): Fixed an issue where a Copilot warning appeared when closing an unmodified empty new document\
*   ([#16516](https://github.com/rstudio/rstudio/issues/16516)\
    ): Removed extraneous whitespace for large objects in Environment pane\
*   ([#16542](https://github.com/rstudio/rstudio/issues/16542)\
    ): Improved accessibility of column splitters by adding accessible labels for screen readers\
*   ([#14683](https://github.com/rstudio/rstudio/issues/14683)\
    ): Changed RStudio Desktop on Linux to default to using native file and message dialog boxes\
*   ([#15340](https://github.com/rstudio/rstudio/issues/15340)\
    ): Fixed an issue where native file dialogs on RStudio Desktop on Linux wouldn’t show .Rproj files\
*   ([#16561](https://github.com/rstudio/rstudio/issues/16561)\
    ): Fixed issues with pane layout when resizing the RStudio window when one or more source columns are displayed\
*   ([#16519](https://github.com/rstudio/rstudio/issues/16519)\
    ): Fixed an issue where Copilot completions would degrade in quality if external edits were applied to an open document\
*   ([#16576](https://github.com/rstudio/rstudio/issues/16576)\
    ): Fixed an issue where column zoom state would lose synchronization when dragging splitters to leave zoomed state\
*   ([#16583](https://github.com/rstudio/rstudio/issues/16583)\
    ): Fixed an issue where a pane wouldn’t unzoom if no source files were open when it was zoomed\
*   ([#16595](https://github.com/rstudio/rstudio/issues/16596)\
    ): Fixed an issue where Open File dialog could malfunction in rare cases\
*   ([#16607](https://github.com/rstudio/rstudio/issues/16607)\
    ): Fixed an issue where warning hyperlinks were malformed in some cases\
*   ([#16329](https://github.com/rstudio/rstudio/issues/16329)\
    ): Fixed an issue where autosave could update a file’s modified time even if it had no changes\
*   ([#16355](https://github.com/rstudio/rstudio/issues/16355)\
    ): Improved rendering performance for large, nested tables in R Markdown / Quarto documents\
*   ([#16624](https://github.com/rstudio/rstudio/issues/16624)\
    ): Fixed an issue where links in a PDF document presented in the Viewer pane could cause navigation to occur in the main RStudio window\
*   ([#16322](https://github.com/rstudio/rstudio/issues/16332)\
    ): Fixed an issue where prefix text was removed by “Reflow comment”\
*   ([#16358](https://github.com/rstudio/rstudio/issues/16358)\
    ): Removed the extra border around the splash screen on macOS Tahoe\
*   ([#16555](https://github.com/rstudio/rstudio/issues/16555)\
    ): Fixed an issue where the Find in Files dialog could open with an empty “Search in:” directory\
*   ([#16521](https://github.com/rstudio/rstudio/issues/16521)\
    ): Fixed an issue where rsession logs would be emitted to the console when `log-message-format=json` is set\
*   ([#16483](https://github.com/rstudio/rstudio/issues/16483)\
    ): Changed R Markdown / Quarto documents to only use paged-table view for auto-printed data objects\
*   ([#16484](https://github.com/rstudio/rstudio/issues/16484)\
    ): Fixed an issue where the “..” entry in the Files pane would not navigate to the parent folder\
*   ([#16320](https://github.com/rstudio/rstudio/issues/16320)\
    ): Fixed an issue where the wrong error message was displayed when SSH key passwords do not match\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-32)\
\
*   (rstudio-pro#8918): Fixed an issue where home page failed to load when a user’s recent project list contains duplicate entries\
*   (rstudio-pro#8846): Improved contrast of check boxes on Workbench home page to meet 3:1 minimum contrast (AA)\
*   (rstudio-pro#8845): Fixed keyboard navigation to inactive sessions on the home page (AA)\
*   (rstudio-pro#9386): Fixed an issue when downloading server-side fonts in load-balanced Workbench configurations\
*   (rstudio-pro#9126): Fixed an issue locating `vscode-user-settings.json` and `positron-user-settings.json` when using `XDG_CONFIG_DIRS`\
*   (rstudio-pro#7638): Fixed an issue where the Workbench API was accessible with the wrong license tier\
*   (rstudio-pro#9279): Fixed an issue in Slurm clusters where R and Python versions were not detected in VS Code and Positron\
*   (rstudio-pro#9421): Fixed an issue with running Workbench Jobs from Positron and VS Code in Slurm clusters without Singularity\
*   (rstudio-pro#9178): Fixed an issue where session memory usage was displayed incorrectly in RStudio Memory Usage dialog when running in a Kubernetes pod\
*   (rstudio-pro#9685): Updated the Positron Pro logo to use a square icon\
*   (rstudio-pro#9494): Fixed an issue where no Workbenches appeared when opening the Resume Session dialog via URL\
*   (rstudio-pro#9278): Fixed an issue where VS Code and Positron could not send heartbeats to Workbench\
*   (rstudio-pro#9169): Fixed an issue where Snowflake Credentials were labeled as “Invalid” in the New Session Dialog after first authentication\
*   (rstudio-pro#8972): Fixed an issue in SAML authentication when request signing is enabled\
*   (rstudio-pro#8968): Fixed an issue that produced spurious “Cannot allocate memory” error in audited jobs\
*   (rstudio-pro#8872): Fixed an issue that changed the session name unexpectedly when switching Workbench type in the New Session dialog\
*   (rstudio-pro#8046): Fixed an issue where `rstudio-server` and `root` users were incorrectly added to Workbench’s internal database\
*   (rstudio-pro#6489): Fixed excessive logging when too many files are open in RStudio Pro\
*   (rstudio-pro#4901): Fixed an issue where sessions were not terminated when `rsession.conf` contained `session-timeout-minutes=0` and `session-timeout-kill-hours=1`\
*   (rstudio-pro#8840): Fixed an issue where RStudio Pro `.Rproj` files were not directly checked for existence, which caused errors when launching RStudio Pro sessions for nonexistent projects\
*   (rstudio-workbench-vscode-ext#289): Fixed links to User Guide documentation in Positron\
\
### Deprecated / Removed[](https://docs.posit.co/ide/news/#rstudio-2026.01.0-deprecated)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-27)\
\
*   ([#16485](https://github.com/rstudio/rstudio/issues/16485)\
    ): Removed inoperative min/max controls from Source Columns\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-33)\
\
*   ([#16218](https://github.com/rstudio/rstudio/issues/16218)\
    ) Removed Crashpad for collecting crash dumps\
\
### Dependencies[](https://docs.posit.co/ide/news/#rstudio-2026.01.0-dependencies)\
\
*   Copilot Language Server 1.399.0\
*   Electron 38.7.2\
*   Node.js 22.21.1 (Copilot completions)\
*   Node.js 22.20.0 (Code OSS server)\
*   Quarto 1.8.25\
*   Launcher 2.21.0\
*   rserver-saml 0.9.2\
*   Positron 2025.12.2-5\
*   Code OSS 1.105\
\
2025.09.2[](https://docs.posit.co/ide/news/#rstudio-2025.09.2)\
\
---------------------------------------------------------------\
\
**“Cucumberleaf Sunflower”** | Date: 2025-10-30\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2025.09.2-new)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-34)\
\
*   (rstudio-pro#9244): Improved log messages for product check failures\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2025.09.2-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-28)\
\
*   ([#16495](https://github.com/rstudio/rstudio/issues/16495)\
    ): Fixed issue with high GPU/CPU utilization on macOS Tahoe\
*   ([#16532](https://github.com/rstudio/rstudio/issues/16352)\
    ): Fixed an issue where ongoing R Markdown render output was lost when after a browser refresh\
*   (rstudio-pro#6377): Extend CSRF protection to the export endpoint\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-35)\
\
*   (rstudio-pro#9312): Fixed a regression that caused the image selection dropdown in the New Session dialog to fail to update when the cluster selection changed to a different cluster of the same type\
*   (rstudio-pro#9199): Fixed an issue where disabled session types were shown in the New Session dialog when creating a new session for an existing project\
*   (rstudio-pro#8055): Fixed an issue where VS Code sessions could crash due to the remote extension host terminating unexpectedly\
*   (rstudio-pro#9109): Fixed an issue where the user service was not logging full error details during user creation failures\
\
### Dependencies[](https://docs.posit.co/ide/news/#rstudio-2025.09.2-dependencies)\
\
*   ([#16492](https://github.com/rstudio/rstudio/issues/16492)\
    ): Copilot Language Server 1.381.0\
*   ([#16495](https://github.com/rstudio/rstudio/issues/16495)\
    ): Electron 37.6.1\
*   Positron Pro 2025.10.1\
\
2025.09.1[](https://docs.posit.co/ide/news/#rstudio-2025.09.1)\
\
---------------------------------------------------------------\
\
**“Cucumberleaf Sunflower”** | Date: 2025-10-01\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2025.09.1-new)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-36)\
\
*   Positron Pro sessions are now supported on RHEL 8\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2025.09.1-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-29)\
\
*   ([#16444](https://github.com/rstudio/rstudio/issues/16444)\
    ): Fixed an issue where the file extension of a new C++ source file was truncated to `.cp` on macOS\
*   ([#16455](https://github.com/rstudio/rstudio/issues/16455)\
    ): Fixed an issue where file extensions for newly saved files were always lowercase on macOS\
*   ([#16436](https://github.com/rstudio/rstudio/issues/16436)\
    ): Fixed an issue where certain ALTREP objects could cause RStudio to crash while populating the Environment pane. This fix also resolves duplicates [#16445](https://github.com/rstudio/rstudio/issues/16445)\
     and [#16465](https://github.com/rstudio/rstudio/issues/16465)\
    \
*   ([#16446](https://github.com/rstudio/rstudio/issues/16446)\
    ): Fixed a regression that could cause file downloads to fail on Windows\
*   ([#16449](https://github.com/rstudio/rstudio/issues/16449)\
    ): Fixed a regression that could cause package installation to fail when installing packages from local sources\
*   ([#16463](https://github.com/rstudio/rstudio/issues/16463)\
    ): Fixed an issue where syntax highlighting was broken in certain Quarto documents\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-37)\
\
*   (rstudio-pro#9163): Fixed the Open Project command to stop throwing an exception\
*   (rstudio-pro#9219): Fixed a regression that caused the image selection dropdown in the new session dialog to display the wrong image\
*   (rstudio-pro#9078): Fixed API error when username and posixuser do not match\
*   (rstudio-pro#9107): Fixed config out of range error\
\
2025.09.0[](https://docs.posit.co/ide/news/#rstudio-2025.09.0)\
\
---------------------------------------------------------------\
\
**“Cucumberleaf Sunflower”** | Date: 2025-09-12\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2025.09.0-new)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-30)\
\
*   ([#16293](https://github.com/rstudio/rstudio/issues/16293)\
    ): Added a Source column that displays a package’s origin (if known) in RStudio’s Packages pane\
*   ([#16294](https://github.com/rstudio/rstudio/issues/16294)\
    ): Provided an additional icon in RStudio’s Packages pane that links to a package’s external documentation (e.g., pkgdown website) when available\
*   ([#16295](https://github.com/rstudio/rstudio/issues/16295)\
    ): Added functionality in the RStudio UI for changing the current repository/snapshot when using Posit Package Manager\
*   ([#15841](https://github.com/rstudio/rstudio/issues/15841)\
    ): Added support for highlighing all SQL 2023 standard keywords in SQL documents in RStudio\
*   ([#16138](https://github.com/rstudio/rstudio/issues/16138)\
    ): Added support for version 17 of the R graphics engine in RStudio\
*   ([#16213](https://github.com/rstudio/rstudio/issues/16213)\
    ): Improved legibility of highlighted code when the RStudio debugger is active\
*   ([#15945](https://github.com/rstudio/rstudio/issues/15945)\
    ): Added a user preference in RStudio to disable showing the splash screen at startup\
*   ([#15614](https://github.com/rstudio/rstudio/issues/15614)\
    ): Added support for closing the RStudio splash screen when clicked with the mouse\
*   ([#16111](https://github.com/rstudio/rstudio/issues/16111)\
    ): Increased RStudio’s default console buffer size to 10,000 lines\
*   ([#11661](https://github.com/rstudio/rstudio/issues/11661)\
    ): Added functionality to bring an existing zoomed plot window to the foreground when clicking the Zoom button in the RStudio Desktop plots pane\
*   ([#16009](https://github.com/rstudio/rstudio/issues/16009)\
    ): Provided an option in RStudio to stop ignoring update prompts when manually checking for updates after previously ignoring them\
*   ([#15988](https://github.com/rstudio/rstudio/issues/15988)\
    ): Added Posit Product Documentation theme v7.0.0 with cookie consent, style updates, accessibility fixes, and dark theme improvements\
*   ([#16214](https://github.com/rstudio/rstudio/issues/16214)\
    ): Introduced a new structure for RStudio release note entries\
*   ([#16226](https://github.com/rstudio/rstudio/issues/16226)\
    ): Added an option (off by default) to zoom RStudio Desktop UI with Ctrl/Cmd + mouse wheel\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-38)\
\
*   ([#14083](https://github.com/rstudio/rstudio/issues/14083)\
    ): Added support for custom certificate bundles for GitHub Copilot in RStudio\
*   (rstudio-pro#8093): Redesigned the Workbench homepage to provide a more efficient and intuitive user experience focused on projects\
*   (rstudio-pro#6768): Added Positron Pro and VS Code projects alongside RStudio Pro projects on the Workbench homepage\
*   (rstudio-pro#8162): Added a custom “Metadata” column in the RStudio Packages pane for sessions using Posit Package Manager\
*   (rstudio-pro#5357): Added support for enforcing the user limit specified by the Posit Workbench product license strictly\
*   (rstudio-pro#7533): Released Posit Product Documentation theme v7.0.1 with cookie consent, style updates, accessibility fixes, and dark theme improvements\
*   (rstudio-pro#8186): Enabled Positron Pro sessions by default in Workbench\
*   (rstudio-pro#7599): Added a step to back-up existing Positron Pro configuration files and install defaults during upgrade\
*   (rstudio-pro#8072): Added support for importing VS Code settings into Positron Pro in Workbench\
*   (rstudio-pro#7466): Added support for setting the default Connect server for the Publisher extension in Positron settings via the `default-rsconnect-server` option in `rsession.conf`\
*   (rstudio-pro#8697): Added a product check request in Workbench that notifies a Posit server when the service is set up and actively using a license. Control this with the `server-product-check` configuration setting (enabled by default: `1`)\`.\
*   (rstudio-pro#8090): Improved integration between RStudio and Posit Package Manager, including repository discovery, authentication, and feature visibility\
*   (rstudio-pro#5068): Added support for just-in-time provisioning of local groups for Proxied Auth, OpenID Connect, and SAML Authentication in Workbench\
*   (rstudio-pro#7817): Added a Run Script in a Workbench Job action (and matching command) in the editor toolbar for R and Python scripts in Positron and VS Code\
*   (rstudio-pro#8463): Organized the Workbench Jobs pane in Positron Pro and VS Code by script, adopt familiar VS Code UI conventions, and open scripts or virtual Job Details documents when clicked\
*   (rstudio-pro#7862): Added support for dismissing completed jobs individually from the Workbench Jobs pane in Positron Pro and VS Code. Provided Dismiss Completed Jobs and Restore Completed Jobs actions to hide/unhide all completed jobs (not persistent across sessions).\
*   (rstudio-pro#8464): Added a preview setting in Workbench to launch jobs from Positron Pro and VS Code with managed credentials (disabled by default)\
*   (rstudio-pro#8148): Provided a new Audit Database and `get_historical_session` Workbench API endpoint to retrieve data about ended sessions\
*   (rstudio-pro#8124): Made Prometheus metrics generally available and removed Preview status\
*   (rstudio-pro#8289): Removed `pwb_session_duration`from Prometheus Metrics and provided session start/end times via the new Workbench API endpoint `get_historical_session`\
*   (rstudio-pro#8135): Added Prometheus metrics for the Launcher component of Workbench\
*   (rstudio-pro#8502): Added version information for Positron Pro and Posit Workbench Code Server to the diagnostic report output\
*   (rstudio-pro#8504): Added Positron Pro version information to Positron Pro session output\
*   (vscode-server#202): Added GitHub Device Login URL as a default trusted domain for VS Code and Positron Pro sessions\
*   (rstudio-pro#6867): Enhanced the image selection in the Workbench New Session dialog to more clearly display and classify available images\
*   (rstudio-pro#8776): Added a switch in both Workbench homepages to toggle between the new and legacy versions and remember the user’s choice locally (see deprecation notice)\
*   (rstudio-pro#9009): Added the kapa.ai website widget to Posit Workbench documentation to answer questions about deploying, configuring, and using Workbench, Posit Connect, and Posit Package Manager.\
*   (rstudio-pro#7247): Added support for SLURM 24 and 25\
*   (rstudio-pro#8025): Improved diagnostic messages for communication errors between Workbench components\
*   (rstudio-pro#8502): Added version information for Positron Pro and Posit Workbench Code Server in diagnostic report output\
*   (vscode-server#164): Added support for controlling the location of VS Code session logs with the `XDG_STATE_HOME` environment variable\
*   (vscode-server#202): Added GitHub Device Login URL as a default trusted domain for VS Code and Positron Pro sessions\
*   Improved Positron Pro Admin and User Guide documentation\
*   Added AWS Load Balanced Reference Architecture\
*   Added support for RHEL 10\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2025.09.0-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-31)\
\
*   ([#15482](https://github.com/rstudio/rstudio/issues/15482)\
    ): Fixed an issue where RStudio would display a “Cannot reinitialise DataTable” error in RStudio when viewing data sets\
*   ([#15133](https://github.com/rstudio/rstudio/issues/15133)\
    ): Fixed an issue where pkgdown websites built outside of the user directory could not be viewed from RStudio Server\
*   ([#14113](https://github.com/rstudio/rstudio/issues/14113)\
    ): Fixed an issue where factors with more than 64 levels were displayed as though they were character vectors in RStudio\
*   ([#15955](https://github.com/rstudio/rstudio/issues/15955)\
    ): Fixed an issue where the “Save As” dialog would not be visible when trying to save an older git revision of a file\
*   ([#15879](https://github.com/rstudio/rstudio/issues/15879)\
    ): Fixed an issue where code indentation stopped working following code chunks containing only Quarto comments\
*   ([#15979](https://github.com/rstudio/rstudio/issues/15979)\
    ): Fixed an issue where RStudio could hang when attempting to execute notebook chunks without a registered handler\
*   ([#12545](https://github.com/rstudio/rstudio/issues/12545)\
    ): (Windows) Fixed an issue where “Use default 32bit / 64bit version of R” did not always use the default version of R set in the registry\
*   ([#16249](https://github.com/rstudio/rstudio/issues/16249)\
    ): Fixed an issue where Copilot would hang by updating copilot-language-server\
*   ([#15923](https://github.com/rstudio/rstudio/issues/15923)\
    ): Fixed an issue where an error message was not shown when the GitHub Copilot language server was missing\
*   ([#15895](https://github.com/rstudio/rstudio/issues/15895)\
    ): Fixed an issue where GitHub Copilot was unaware of files already loaded in the source editor before Copilot starts\
*   ([#16133](https://github.com/rstudio/rstudio/issues/16133)\
    ): Fixed an issue where RStudio’s Update Packages dialog could report packages were out-of-date for packages installed into multiple library paths\
*   (rstudio-pro#8159): Fixed an issue where attempting to attach or detach a package using the Packages pane could cause UI to become out-of-sync with actual package state\
*   ([#16119](https://github.com/rstudio/rstudio/issues/16119)\
    ): Fixed an issue where GitHub Copilot’s status was incorrectly reported as an error in the Preferences dialog\
*   ([#16128](https://github.com/rstudio/rstudio/issues/16128)\
    ): Fixed an issue where GitHub Copilot would not index project files when Copilot was started while the project is open\
*   ([#15901](https://github.com/rstudio/rstudio/issues/15901)\
    ): Fixed an issue where the entire document was sent to GitHub Copilot after each edit instead of just the changes\
*   ([#16129](https://github.com/rstudio/rstudio/issues/16129)\
    ): Fixed an issue where RStudio would send multiple didOpen messages to GitHub Copilot for the same file\
*   ([#2900](https://github.com/rstudio/rstudio/issues/2900)\
    ): Fixed an issue where new R package projects did not inherit “Generate documentation with Roxygen” preference\
*   ([#15919](https://github.com/rstudio/rstudio/issues/15919)\
    ): Fixed an issue where large character vectors were shown with an NaN size in the environment pane\
*   ([#15444](https://github.com/rstudio/rstudio/issues/15444)\
    ): Fixed an issue where hitting the Escape key to close the “Update Available” dialog would exit RStudio\
*   ([#16191](https://github.com/rstudio/rstudio/issues/16191)\
    ): Fixed an issue where the splash screen would not close and the RStudio main window would not show when starting RStudio Desktop\
*   ([#16198](https://github.com/rstudio/rstudio/issues/16198)\
    ): Fixed an issue where the “Switch Focus between Source/Console” command would not work when the Visual Editor was active\
*   ([#12470](https://github.com/rstudio/rstudio/issues/12470)\
    ): Fixed an issue in RStudio Desktop on Windows where creating multiple cursors using Alt + the mouse would move focus to the menu bar\
*   ([#15797](https://github.com/rstudio/rstudio/issues/15797)\
    ): Fixed an issue where the label in readr-based text import dialog incorrectly showed “factors” instead of “factor levels”\
*   ([#16266](https://github.com/rstudio/rstudio/pull/16266)\
    ): Fixed an issue where RStudio was not resolving xdg-open on the PATH, and was instead assuming it was located at /usr/bin/xdg-open\
*   ([#16217](https://github.com/rstudio/rstudio/issues/16217)\
    ): Fixed an issue where error messages were not wrapped when presented in the Console\
*   ([#16225](https://github.com/rstudio/rstudio/issues/16225)\
    ): Fixed an issue where the RStudio memory panel showed shared memory resources for certain cgroup configurations\
*   ([#16326](https://github.com/rstudio/rstudio/issues/16326)\
    ): Fixed an issue where an error was shown when creating a new folder in the Choose Directory dialog\
*   ([#15919](https://github.com/rstudio/rstudio/issues/15919)\
    ): Fixed an issue where NaN might display for the object sizes of large character vectors by using lobstr in RStudio to compute the size\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-39)\
\
*   (rstudio-pro#8144): Fixed an issue where Positron State was not being loaded on login\
*   (rstudio-pro#7368): Fixed an issue where Shiny for Python and other applications would regularly experience websocket failures in VS Code and Positron sessions\
*   (rstudio-pro#7818): Fixed an issue where Workbench Jobs launched from Positron and VS Code did not set the working directory correctly for scripts outside of the current workspace\
*   (rstudio-pro#7605): Fixed an issue where setting `create-container-user=1` in `rserver.conf` option would not work when `pam-use-password=1` was also set\
*   (rstudio-pro#7861): Fixed an issue where completed jobs in the Workbench Jobs pane in Positron and VS Code had a non-functional `Stop Workbench Job` action\
*   (rstudio-pro#8088): Fixed an issue where Workbench Jobs launched from Positron and VS Code were ignoring queues, resource limits, or resource profiles\
*   (rstudio-pro#8251): Fixed an issue where `RS_SERVER_URL` was not set correctly in Positron and VS Code sessions launched through the Workbench API\
*   (rstudio-pro#8003): Fixed an issue where Positron user settings were not being copied to `user-data-dir`\
*   (rstudio-pro#8287): Fixed an issue where RStudio memory limits were applied to shared processes for certain cgroup configurations\
*   (rstudio-pro#8120): Fixed an issue where local launcher resource limits did not work with pam\_systemd\
*   (rstudio-pro#8319): Fixed an issue where a file descriptor would leak in RStudio Pro sessions when running on a system without cgroups v1 or v2\
*   (rstudio-pro#8246): Fixed an issue where rworkspaces would sometimes segfault when it exited (no user impact)\
*   (rstudio-pro#8462): Fixed an issue where VS Code/Positron Pro session browser state would not be loaded on sign in after being signed out due to inactivity\
*   (rstudio-pro#6867): Fixed an issue where image selection in the launcher UI was not behaving consistently\
*   (rstudio-pro#8690): Fixed an issue with locking users when using a license that has unlimited user count\
*   (rstudio-pro#7589) Fixed an issue where users were not gracefully returned to the homepage when clicking an invalid link\
*   (rstudio-pro#8080): Fixed an issue where the original CPU and Memory requests would not be remembered when resuming a session\
*   (rstudio-pro#8003): Fixed an issue where Positron user settings were not being copied to `user-data-dir`\
*   (rstudio-pro#8145): Fixed an issue where VS Code sessions were incorrectly labeled as `"rstudio-pro"` in the `pwb_sessions_launched_total` Prometheus metric\
*   (rstudio-pro#8563): Fixed an issue where the upload link in the Workbench diagnostics report was outdated\
*   (rstudio-pro#8580): Fixed an issue where sessions started in a Kubernetes cluster would fail to start if “.0000” was appended to the CPU request\
*   (rstudio-pro#8929): Fixed an issue that could cause spurious login failures in Workbench\
*   (rstudio-workbench-vscode-ext#268): Fixed an issue where the custom port warning for FastAPI application in VS Code and Positron Pro sessions would not be displayed in some cases\
*   (rstudio-workbench-vscode-ext#278): Fixed an issue where Python/R console activity in Positron Pro sessions was not detected when the browser was closed, which caused premature termination\
*   (rstudio-workbench-vscode-ext#310): Fixed an issue where disabling the extension marketplace in Positron Pro sessions would prevent built-in extensions from being installed\
*   (rstudio-workbench-vscode-ext#291): Fixed an issue where long-running Workbench Jobs launched from Positron and VS Code were displaying incorrect runtimes\
*   (rstudio-workbench-vscode-ext#345): Fixed an issue where the Workbench extension for VS Code and Positron had an overly noisy notification\
*   (vscode-server#171): Fixed an issue where VS Code and Positron Pro sessions would prompt the user when navigating to the Workbench homepage as though the Workbench URL were an external link\
\
### Upgrade Instructions[](https://docs.posit.co/ide/news/#rstudio-2025.09.0-upgrade)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-40)\
\
With this release, Positron Pro sessions are moving from preview to General Availability (GA). The upgrade process will automatically back up any existing Positron Pro configuration files to ensure production-ready defaults are properly installed.\
\
During package upgrade, the following files will be backed up if they exist:\
\
*   `/etc/rstudio/positron.conf` as `/etc/rstudio/positron.conf.bak`\
*   `/etc/rstudio/positron-user-settings.conf` as `/etc/rstudio/positron-user-settings.conf.bak`\
\
After completing the package upgrade, carefully review the backed up files and the new default configuration files and merge any customizations as needed.\
\
Since Positron Pro is now enabled by default, the following default configuration value has changed in the `positron.conf` configuration file:\
\
|     |     |     |     |\
| --- | --- | --- | --- |   \
| `enabled` | `0` (disabled) | `1` (enabled) | (rstudio-pro#9376) |\
\
### Dependencies[](https://docs.posit.co/ide/news/#rstudio-2025.09.0-dependencies)\
\
*   (rstudio-pro#9080): rserver-saml 0.9.1\
*   (rstudio-pro#8991): Nginx 1.29.1\
*   ([#15935](https://github.com/rstudio/rstudio/issues/15935)\
    ): Copilot Language Server 1.352.0\
*   ([#15933](https://github.com/rstudio/rstudio/issues/15933)\
    ): Electron 37.2.6\
*   ([#16062](https://github.com/rstudio/rstudio/issues/13924)\
    ): GWT 2.12.2\
*   ([#15934](https://github.com/rstudio/rstudio/issues/15934)\
    ): Quarto 1.7.32\
*   (vscode-server#177): Code OSS 1.102.0\
*   Node.js 22.15.1\
*   Positron Pro 2025.08.1\
\
### Deprecated / Removed[](https://docs.posit.co/ide/news/#rstudio-2025.09.0-deprecated)\
\
*   ([#15940](https://github.com/rstudio/rstudio/issues/15940)\
    ): Discontinuted support for Ubuntu Focal for RStudio Server and Posit Workbench\
*   ([#16104](https://github.com/rstudio/rstudio/issues/16104)\
    ): Removed the “Limit visible console output” feature\
*   ([#16233](https://github.com/rstudio/rstudio/issues/16233)\
    ): Removed the “Send automated crash reports” feature from RStudio Desktop\
*   (rstudio-pro#8257): Removed publishing to Posit Cloud\
*   (rstudio-pro#8776): Deprecated the legacy Workbench homepage\
*   (rstudio-pro#6251): Removed the deprecated Google Auth feature, including the associated documentation and server options\
\
2025.05.1[](https://docs.posit.co/ide/news/#rstudio-2025.05.1)\
\
---------------------------------------------------------------\
\
**“Mariposa Orchid”** | Date: 2025-06-05\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2025.05.1-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-32)\
\
*   Fixed an issue where GitHub Copilot suggestions could be missing some text (#16023)\
*   Fixed an issue where warnings were not treated as errors when options(warn = 2) was set (#16031)\
*   Fixed an issue where RStudio could hang when attempting to execute notebook chunks without a registered handler (#15979)\
*   Fixed an issue where RStudio continued executing code within R Markdown chunks after an error occurred (#16000, #16002)\
*   Fixed an issue where no more console output was produced after a ’ character input in some cases (#16038)\
*   Fixed an issue where console history could not be retrieved if an error occurred while executing a notebook chunk (#16006)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-41)\
\
*   Fixed an issue where resource profiles would be incorrectly added to Workbench Jobs (rstudio-pro#8127)\
*   Fixed an issue where audited jobs would fail if the user’s Workbench username differs from their posix username (rstudio-pro#8129)\
*   Fixed an issue where the session init container was being added to containerized sessions and jobs on clusters that did not support them (rstudio-pro#8009)\
*   Fixed an issue where Shiny for Python and other applications would reguarly experience websocket failures in VS Code and Positron sessions (rstudio-pro#7368)\
*   Fixed an issue where the positron-settings.json example in the Admin guide had an extra comma (rstudio-pro#8853)\
\
### Dependencies[](https://docs.posit.co/ide/news/#rstudio-2025.05.1-dependencies)\
\
*   Updated Positron Pro sessions to 2025.06 with Code OSS 1.100 (rstudio-pro#8239)\
\
2025.05.0[](https://docs.posit.co/ide/news/#rstudio-2025.05.0)\
\
---------------------------------------------------------------\
\
**“Mariposa Orchid”** | Date: 2025-05-05 | [Release Blog Post](https://posit.co/blog/rstudio-2025-05-0-whats-new/)\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2025.05.0-new)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-33)\
\
*   RStudio now uses an alternate display for R errors, warnings, and messages. In addition, output on stderr (e.g. R messages) are colored the same as regular output on stdout. (#2574)\
*   RStudio now displays a message when the GitHub Copilot completion limit has been reached (typically on a free Copilot account). (#15848)\
*   RStudio now uses the RStudio project folder as the GitHub Copilot workspace root, providing more relevant completions. (#15816)\
*   RStudio now supports being built without GitHub Copilot support via the `RSTUDIO_ENABLE_COPILOT` CMake option. (#15869)\
*   On macOS, RStudio now uses the project directory / home directory for new RStudio sessions opened via the Dock menu’s “Open in New Window” command. (#15409)\
*   RStudio Desktop now supports opening files via drag and drop. (#4037)\
*   RStudio installation on Windows now registers icons for many supported file types. (#12730)\
*   RStudio for Windows binaries now have digital signatures. (rstudio-pro#5772)\
*   RStudio now only writes the ProjectId field within a project’s `.Rproj` file when required. Currently, this is for users who have configured a custom `.Rproj.user` location.\
*   Added memory limit monitoring to RStudio (Linux only for now). If `ulimit -m` is set, this limit is displayed in the Memory Usage Report. As the limit is approached, a warning is displayed, then an error when the limit is reached. When the system is low on memory, the session can abort itself by shutting down in a controlled way with a dialog to the user. See the new `"allow-over-limit-sessions` option in rsession.conf. (rstudio-pro#5019).\
*   RStudio now supports configuring a Kerberos Service Principal for the GitHub Copilot Language Server proxy settings. (#15823)\
*   RStudio now supports installation of Rtools45 for the upcoming R 4.5.0 release on Windows.\
*   RStudio now sets the environment variable `SPARK_CONNECT_USER_AGENT = posit-rstudio` in R sessions. (rstudio-pro#7732)\
*   RStudio now sets the environment variable `SF_PARTNER = posit_rstudio` in R sessions. (rstudio-pro#7577)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-42)\
\
*   Changed memory limit enforcement of `/etc/rstudio/profiles` `max-memory-mb` setting from limiting virtual memory (`ulimit -v`) to resident memory (`ulimit -m`) for more accuracy. This allows a session to run quarto 1.6, which uses a lot of virtual memory due to its underlying virtual machine. Unfortunately, resident memory is only enforceable at the kernel level in Linux versions that support cgroups. To make up for the loss of kernel enforcement, RStudio warns the user and stops over limit sessions. For more robust kernel enforcement, configure memory limits in the Job Launcher using cgroups (rstudio-pro#5019).\
*   RStudio will now preserve unknown fields in `.Rproj` files that are added by future versions of RStudio. (#15524)\
*   RStudio now sends an interrupt git processes when stopped via “Stop” during a git commit, rather than just terminating the processes. (#6471)\
*   RStudio now properly displays R Markdown render errors with newer versions of the `rmarkdown` and `rlang` packages. (#15579)\
*   An SELinux policy module is now available, allowing Workbench to run when enforcement is enabled. (#4937, rstudio-pro/#4749)\
*   Migrated the Posit Workbench Admin Guide Hardening: Set Up SSL content into the Access and Security: Secure Sockets (SSL) topic to promote content discovery and single source of truth. (rstudio-pro#6098)\
*   Adds secure browser storage to VS Code and Positron Pro sessions (vscode-server#174)\
*   Implemented User and Group profiles for VS Code and Positron Pro sessions (rstudio-pro#7468)\
*   Introduced custom bootstrap extensions to Positron Pro session to improve the Admin pre-configured extensions experience (rstudio-pro#7423)\
*   Introduced a new admin configuration UI **in preview** to modify and deploy distributed workload (Launcher) settings (rstudio-pro#7401, rstudio-pro#7403, rstudio-pro#7481)\
*   Updated to Launcher 2.19.0, which now writes an active state file to the filesystem for each config file loaded on reload or restart (launcher#1172)\
*   Consolidated the Posit Workbench Administrator Guide and Posit Workbench User Guide into a single site that includes a Posit Workbench documentation landing page (rstudio-pro#6892)\
*   Introduced audited Workbench jobs to provide auditing information alongside Workbench job output. Enable audited Workbench jobs with the `audited-jobs` parameter in the `rserver.conf` file (rstudio-pro#7418, rstudio-pro#7569, rstudio-pro#7571, rstudio-pro#7581, rstudio-pro#7935)\
*   Sessions now set the environment variable `SPARK_CONNECT_USER_AGENT` to `posit-workbench-rstudio`, `posit-workbench-positron`, `posit-workbench-jupyter`, or `posit-workbench-vscode` depending on the session type (rstudio-pro#7970)\
*   Sessions now set the environment variable `SF_PARTNER` to `posit_workbench_rstudio`, `posit_workbench_positron`, `posit_workbench_jupyter`, or `posit_workbench_vscode` depending on the session type (rstudio-pro#7970)\
*   Updated dependencies for the JupyterLab extension to address security vulnerabilities (rstudio-pro#7621)\
*   Allow the option `launcher-sessions-use-pam-password=1` in environments where `launcher-ssl=0` if `launcher-address` points to the localhost. (rstudio-pro#2929).\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2025.05.0-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-34)\
\
*   Fixed an issue where execution of notebook chunks could fail if the `http_proxy` environment variable was set. (#15530)\
*   Fixed an issue where RStudio could hang when attempting to stage large folders from the Git pane on Windows. (#13222)\
*   Fixed an issue where RStudio could crash when attempting to clear plots while a new plot was being drawn. (#11856)\
*   Fixed an issuew here RStudio could crash if a project contained `.R` files with binary data. (#15801)\
*   Fixed an issue where the R startup banner was printed twice in rare cases. (#6907)\
*   Fixed an issue where RStudio Server could hang when navigating the Open File dialog to a directory with many (> 100,000) files. (#15441)\
*   Fixed an issue where the F1 shortcut would fail to retrieve documentation in packages. (#10869)\
*   Fixed an issue where some column names were not displayed following select() in pipe completions. (#12501)\
*   Fixed an issue where building with a newer version of Boost (e.g. Boost 1.86.0) would fail. (#15625)\
*   Fixed an issue where opening multiple copies of RStudio Desktop installed in different locations would cause RStudio to try to open itself as a script. (#15554)\
*   Fixed an issue where printing 0-row data.frames containing an ‘hms’ column from an R Markdown chunk could cause an unexpected error. (#15459)\
*   Fixed an issue where the Resources page in the Help pane was not legible with dark themes. (#10855)\
*   Fixed an issue where “Posit Workbench” was used instead of “RStudio Server” in a message shown when the user was signed out during a session. (#15698)\
*   Fixed an issue where the RStudio diagnostics system incorrectly inferred the scope for functions defined and passed as named arguments. (#15629)\
*   Fixed an issue where `locator()` and `grid.locator()` would produce incorrect coordinates with high DPI displays. (#10587)\
*   Fixed an issue where grid coordinates were not converted between different units correctly with high DPI displays. (#1908, #8559)\
*   Fixed an issue where locator points were not drawn on click. (#10025, #11103)\
*   Fixed an issue where RStudio would crash when using the MySQL ODBC Connector on Microsoft Windows. (#15674)\
*   Fixed an issue where autocompletion of R6 object names could fail with R6 2.6.0. (#15706)\
*   Fixed a WCAG 1.1.1 violation (unlabeled image in the Console toolbar) by marking it as cosmetic. \[Accessibility\] (#15757)\
*   Fixed Material theme’s colors for selected word or text highlighting so they are more visible. \[Accessibility\] (#15753)\
*   Fixed an issue where .bib files with extra commas could be treated as binary files on RHEL9. (rstudio-pro/7521)\
*   Update NO\_PROXY domain filter to be less restrictive and allow for expressions like `.local` and `.sub.example.local` (#15607)\
*   Fixed an issue where Copilot support on Apple Silicon Macs was running via Rosetta2 instead of natively. (#14156)\
*   Fixed an issue where the Copilot process was being started twice per RStudio session. (#15858))\
*   Fixed an issue where documents could open very slowly when many tabs were already open. (#15767)\
*   Fixed an issue where the download of Rtools44 could fail when using Posit Package Manager as the default R package repository. (#15803)\
*   Fixed an issue where messages produced by `rlang::inform()` were not separated by newlines.\
*   Fixed an issue where the `modifyRange` API function was not available, even though such a function was provided by `rstudioapi`.\
*   Fixed an issue where installing “required but not installed” packages could fail if those packages were available from an alternate (non-CRAN) package repository. (#10016)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-43)\
\
*   Fixed an issue where uploading a file to a directory containing an ‘&’ character could fail. (#6830)\
*   Fixed an issue where unopened VSCode and Positron sessions wouldn’t timeout when `session-timeout-kill-hours` was set and SSL was enabled. (rstudio-pro#7195)\
*   Fixed bug where collaborative editing would break unless `server-working-dir=/usr/lib/rstudio-server` was set in rserver.conf. (rstudio-pro#7300)\
*   Fixed a couple of bugs setting file permissions for project sharing. (rstudio-pro#7460)\
*   Fixed issue where PAM session could not use privileges in Local Job Launcher sessions (rstudio-pro#6885)\
*   Fixed issue with PAM sessions using CIFS PAM mounts (rstudio-pro#7198)\
\
### Dependencies[](https://docs.posit.co/ide/news/#rstudio-2025.05.0-dependencies)\
\
*   Update Electron to version 34.5.1. (#15450)\
*   Update Quarto to version 1.6.42. (#15460)\
*   Updated Positron Pro sessions to 2025.04 with Code OSS 1.98\
*   Updated Code OSS to 1.99 for VS Code sessions (rstudio-pro#7882)\
*   Copilot Language Server 1.300.0. (rstudio-pro#7450)\
*   Updated Node in VS Code and Positron Pro sessions to 20.18.2 (rstudio-pro#7612)\
\
### Deprecated / Removed[](https://docs.posit.co/ide/news/#rstudio-2025.05.0-deprecated)\
\
*   No longer building RStudio Desktop or Desktop Pro for OpenSUSE 15, Ubuntu Focal, or RedHat 8. (rstudio-pro/#7445)\
*   No longer bundling node.js with RStudio Desktop, Desktop Pro, or RStudio Server. (rstudio-pro#7450)\
\
2024.12.1[](https://docs.posit.co/ide/news/#rstudio-2024.12.1)\
\
---------------------------------------------------------------\
\
**“Kousa Dogwood”** | Date: 2025-02-13\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2024.12.1-new)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-35)\
\
*   The editor line height can now be customized (via Tools -> Global Options… -> Appearance) \[Accessibility\]. (#3372)\
*   Noto Sans is now used as a fallback proportional font (for RStudio UI elements) on Linux systems. (#15547)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-44)\
\
*   The secret key used to sign browser cookies can now be set via the `WORKBENCH_ENCRYPTION_KEY` environment variable. (rstudio-pro#7169)\
*   Added a warning when the server certificate is self-signed but the certificate authority root is not in the system’s CA store. (rstudio-pro#6813)\
*   Added an error when the Launcher port or SSL configuration does not match Workbench’s corresponding configuration. (rstudio-pro#6811)\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2024.12.1-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-36)\
\
*   Fixed an issue where executing Python code from an R Markdown chunk could cause a crash in rare cases. (#rstudio-pro/7322)\
*   Fixed an issue where reformatting a document with unsaved changes when using `styler` for formatting could lose unsaved changes. (#15568)\
*   Fixed an issue where double-clicking a source file to start RStudio didn’t always open the file after starting. (#15536, rstudio-pro#7259)\
*   Fixed an issue where double-clicking a file to open it in running RStudio didn’t work with zoomed plot windows. (#15457)\
*   Fixed an issue where the RStudio UI stopped working if publishing was disabled in Global Options. (#15561)\
*   Reverted support for `help.htmltoc` with R (>= 4.4); support will be re-evaluated in a future release. (#15531)\
*   Fixed an issue where Copilot completions were not provided in Quarto documents. (#15539)\
*   Fixed an issue where very large character vectors in the R global environment could make RStudio initialize more slowly. (rstudio-pro#7226)\
*   Fixed an issue where the `.Rproj.user` folder was not marked as hidden for new projects on Windows. (#15514)\
*   Fixed an issue where the Files pane could inadverently scroll back to top in some cases. (#15502)\
*   Fixed an issue with non-ASCII characters in qmd files showing as “unexpected token.” (#15316)\
*   Fixed an issue where chunk highlighting in Sweave documents was incorrect. (#15574)\
*   Fixed an issue where code diagnostics were incorrectly applied to un-evaluated R code chunks in visual mode. (#15592)\
*   Fixed an issue where RStudio could emit a warning when attempting to retrieve help for R objects without a help page. (rstudio-pro#7063)\
*   Fixed an issue where RStudio’s code formatter could produce invalid code in some cases. (#5425)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-45)\
\
*   Fixed images list in the launcher UI not updating immediately on cluster change for multi-cluster configurations with different image lists. (rstudio-pro#7169)\
*   Fixed a regression where editors configured with both a default cluster of “Local” and a default image cause a misconfiguration on session launch. (rstudio-pro#7172, rstudio-pro#7178)\
*   Fixed resource profile from a non-Local cluster remaining set for Local cluster when launcher is configured without cgroups support, leading to invalid session launch. (rstudio-pro#7253)\
*   Fixed issue with proxying websockets over ssl that could lead to intermittent VS Code session errors. (rstudio-pro#7264)\
*   Fixed problems using `rstudio-server reload` to reload configuration with load balancing enabled. (rstudio-pro#7166, rstudio-pro#5600)\
*   Fixed Workbench API support for launching Jupyter sessions. (rstudio-pro#7159)\
*   Fixed Workbench API get\_session call with a session-id filter. (rstudio-pro#7207)\
*   Fixed a regression in the behavior of the `auth-proxy-user-header-rewrite` setting which allowed conditional rewrites of usernames (rstudio-pro#7324)\
*   Fixed issue with using encrypted postgresql password when user provisioning is enabled. (rstudio-pro#7305, rstudio-pro#7248)\
*   Fixed an issue in VS Code sessions that caused Workbench to attempt to save massive entries to its database that could slow down servers by moving the `vscode-logs-store` out of browser storage (rstudio-pro#7369)\
*   Fixed an issue with the NO\_PROXY domain filter that caused a duplicate `.` character to appear in the rule (rstudio-pro#7265)\
\
### Upgrade Instructions[](https://docs.posit.co/ide/news/#rstudio-2024.12.1-upgrade)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-46)\
\
### Dependencies[](https://docs.posit.co/ide/news/#rstudio-2024.12.1-dependencies)\
\
*   Updated Electron to version 31.7.7 (#15634)\
\
### Deprecated / Removed[](https://docs.posit.co/ide/news/#rstudio-2024.12.1-deprecated)\
\
*   Added a warning about the deprecation of publishing to Posit Cloud. More information: https://pos.it/pc-publishing (rstudio-pro#7008)\
\
2024.12.0[](https://docs.posit.co/ide/news/#rstudio-2024.12.0)\
\
---------------------------------------------------------------\
\
**“Kousa Dogwood”** | Date: 2024-12-16 | [Release Blog Post](https://posit.co/blog/rstudio-2024-12-0-whats-new/)\
  \
\
### New[](https://docs.posit.co/ide/news/#rstudio-2024.12.0-new)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-37)\
\
*   RStudio now supports the inclusion of environment variables when publishing applications to Posit Connect. (#13032)\
*   Available environment variables are now provided as completion suggestions within `Sys.unsetenv()`. (#15215)\
*   RStudio now supports new features from the R graphics engine (groups, glyphs) when supported by the underlying device. (#14613)\
*   The `.Rproj.user` folder location can now be customized globally by both users and administrators. (#15098)\
*   RStudio now supports code formatting using the ‘styler’ R package, as well as other external applications. (#2563)\
*   The RStudio diagnostics system now supports destructuring assignments as implemented in the `dotty` package.\
*   The “Include all function arguments in the completion list” user preference can be used to control whether RStudio includes function arguments that appear to have already been used in the current context. (#13065)\
*   RStudio supports `usethis.description` option values when creating projects via the RStudio New Project wizard. (#15070)\
*   Rename in Scope now operates across chunks within R Markdown and Quarto documents. (#4961)\
*   RStudio now respects the chunk ‘dpi’ option when generating plots in R Markdown and Quarto documents. (#11649)\
*   RStudio now supports the display of an HTML table of contents for R help files when `options(help.htmltoc = TRUE)` is set. (#14523)\
*   RStudio now includes `.env` files in the fuzzy finder and displays these files in the Files pane.\
*   Quarto documents now have a gear icon for editing cell (chunk) options. (#11745)\
*   A “Copy RStudio Version” command has been added to the command palette for copying the RStudio version, commit, and build date to the clipboard.\
*   RStudio now supports syntax highlighting for Fortran source files. (#10403)\
*   The label “Publish” now appears next to the publish icon on the editor toolbar. (#13604)\
*   The font size used for the document outline can now be customized \[Accessibility\]. (#6887)\
*   The `www-socket` option has been added to rserver.conf to enable the server to listen on a Unix domain socket (#14938; Open-Source Server).\
*   The “Insert Chunk” button now acts as a menu in both Quarto and R Markdown documents. (#14785)\
*   Improved support for highlighting nested chunks in R Markdown and Quarto documents. (#10079)\
*   Improved support for variable-width chunk headers and footers in R Markdown and Quarto documents. (#15191)\
*   RStudio now provides executed chunk code as a single multi-line entry in the Console history. (#3520)\
*   RStudio now provides snippet completions within function calls and subset calls. (#13441)\
*   RStudio now supports zooming the IDE via Meta + NumpadAdd and Meta + NumpadSubtract. (#12242)\
*   RStudio now uses `lobstr::obj_size()` when computing object sizes for display in the Environment pane. (#15369)\
*   The RStudio IDE User Guide and the RStudio & Posit Workbench Release Notes have versioned URLs in the Guides drop-down menu in the navigation bar. Additionally, the navigation bar links to the Release Notes and Versions URLs have versioned URLs. (#15223)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-47)\
\
*   Added preview support for Positron Pro sessions on RHEL9 and Ubuntu 22/24. Positron Pro sessions must be manually configured by an admin. (rstudio-pro#6861)\
*   Added support for saving Positron Pro state across user logout. (rstudio-pro#6820)\
*   Added a feature that prevents Positron Pro and VS Code sessions from starting for insecure (non-SSL/TLS) contexts because they require SSL/TLS for full functionality. (rstudio-pro#3741)\
*   Added a `session-timeout-kill-hours` setting to VS Code and Positron Pro sessions, which terminates sessions after being idle for a set number of hours. There is a known issue that prevents this feature from working correctly with a custom www-root-path. (rstudio-pro#5746)\
*   Added the Quarto, Posit Shiny, and Posit Publisher extensions to the default `vscode.extensions.conf` file for fresh installs. These extensions will be installed automatically for users upon VS Code session launch. (rstudio-pro#6388)\
*   Added preview support for setting an active timeout, which logs out users after a period of time, regardless of activity. (rstudio-pro#5815)\
*   Added a new session init container that copies session components to the session container, allowing updates to components independent of the session image. The session init container can be enabled in Kubernetes sessions by setting `launcher-sessions-auto-update=1` in `rserver.conf`. Additionally, the init container uses a new multi-platform Linux session components package to support session images across different Linux distributions. (rstudio-pro#6821)\
*   Added the `auth-user-rewrite-rule` setting to `rserver.conf`. When this option is set in environments with Google OAuth, OpenID, SAML, or Proxied Authentication configured, Workbench will rewrite the username from the authentication provider using the provided regex. (rstudio-pro#2502)\
*   Added support for HTTP Proxy variables in rserver and rsession to enable managed credentials features in Workbench environments behind a proxy server. (rstudio-pro#5893)\
*   Set Posit Public Package Manager (P3M) as the default for R libraries in RStudio Pro sessions, if no other repository is specified. Package Manager will deliver pre-built binary packages when available, which are faster to install than source packages and don’t require most additional build dependencies. (rstudio-pro#5066)\
*   Added support to the Workbench API for registering shell scripts as session hooks that can run when a session starts and stops. (rstudio-pro#6428)\
*   Extended the Workbench API, adding support for launching jobs, resuming sessions, and retrieving user lists. Additionally, support for passing in environment variables, session hooks, and a file to open on session load has been added to the launch session endpoint. (rstudio-pro#5066)\
*   The Posit Workbench Administration Guide, the Posit Workbench User Guide, and the Posit Workbench Licenses Guide have versioned URLs in the Guides drop-down menu in the navigation bar. (rstudio-pro#6151)\
*   The Posit Workbench User Guide underwent a reorganization of how the individual IDE guides are presented. Each guide was migrated from the left-hand navigation to the upper (main) navigation bar. Now, when a guide is selected from the navigation bar, only that guide’s contents display in the left-hand navigation. Additionally, the Posit Workbench guide was renamed to “Workbench Setup” in the navigation bar to prevent confusion between the title of the guide and to create more distinction between the home page of the guide and the Posit Workbench Overview. Lastly, the links for the five IDEs were updated to navigate to the corresponding guide within the Posit Workbench User Guide (instead of the IDE’s external site) and are displayed as buttons. (rstudio-pro#6069)\
*   Added an FAQ page to the Reference Architectures section of the Posit Workbench Administration Guide. (rstudio-pro#6645)\
*   Re-designed the user experience for configuring managed credentials (rstudio-pro#6748)\
*   Added support for using Azure delegated credentials to access DevOps repositories (rstudio-pro#6734)\
*   Improved the database migration experience with additional feedback to the admin, logging, and potential error handling (rstudio-pro#6674)\
*   Improved diagnostics for the license manager (rstudio-pro#5932)\
*   Added support for reloading the Launcher through systemd (rstudio-pro#3749)\
*   Added support for a configurable auth (SAML/OpenID) username re-write rule (rstudio-pro#6987)\
*   Migrated Snowflake Native App documentation from Posit Workbench Administration Guide to the [Posit Partnerships](https://docs.posit.co/partnerships/snowflake/)\
     site.\
*   Made Workbench API generally available and removed Preview status\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2024.12.0-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-38)\
\
*   “Run All” now only executes R chunks when “Chunk Output in Console” is set. (#11995)\
*   Fixed an issue where the chunk options popup didn’t recognize chunk labels preceded by a comma. (#15156)\
*   Fixed an issue where the chunk options popup was confused by quoted strings containing spaces. (#6829)\
*   Fixed an issue where the chunk options popup was confused by spaces around equals signs. (#2673)\
*   Fixed the chunk options popup to work in Visual Mode for non-R chunks. (#15312)\
*   Fixed issue where collapsed raw chunks were displayed with an incorrect label in the Visual Editor. (#14594)\
*   Fixed an issue where an R Markdown chunk label containing dashes was truncated in Visual Editor. (#15162)\
*   Fixed issue with highlight of `tikz` code chunks in R Markdown documents. (#15019)\
*   Fixed an issue where ghost text could not be inserted in non-chunk parts of an R Markdown / Quarto document. (#14507)\
*   Fixed an issue where the R session could crash on connect while generating console output. (#15330)\
*   Fixed an issue where some output from `uv` could be rendered blurry in the RStudio Console. (#15282)\
*   Fixed an issue where right-clicking on the console history did not present Paste as an option. (#14538)\
*   RStudio no longer logs warning / error messages related to disabled R actions (e.g., ReadConsole) in forked sessions. (#15221)\
*   Fixed an issue where the Console header label was not properly layed out when other tabs (e.g., Terminal) were closed. (#15106)\
*   Fixed Windows Desktop Pro so it starts up after using the Choose R dialog. (rstudio-pro#6062)\
*   Fixed an issue with the splash screen appearing on top of the Desktop Pro Manage License. (rstudio-pro#6962)\
*   Fixed Mac Desktop Pro so it starts on an ARM (Mx) Mac that doesn’t have Rosetta2 installed. (rstudio-pro#3558)\
*   RStudio Desktop now forwards `LD_LIBRARY_PATH` when detecting available R installations. (#15044)\
*   Fixed an issue where attempts to publish to a collaborator’s application could fail to update that application. (#15065)\
*   Fixed an issue where the Rename File command did not write unsaved changes before performing the rename. (#15242)\
*   Fixed being unable to save file after cancelling the “Choose Encoding” window. (#14896)\
*   Fixed problems creating new files and projects on a UNC path. (#14963, #14964; Windows Desktop)\
*   Fixed an issue where RStudio could autosave files on blur even while a Save As… modal was active. (#15303)\
*   Fixed an issue where the IDE could hang when changing the file type of an R Markdown document. (#15313)\
*   Fixed an issue where autocompletion results within piped expressions were incorrect in some cases. (#13611)\
*   Fixed an issue where completion types for objects with a `.DollarNames` method were not properly displayed. (#15115)\
*   Fixed an issue where quoted variable names were not completed properly in dplyr pipes. (#15161)\
*   Fixed an issue with incorrect completions provided in `readline()` context. (#15238)\
*   Fixed issue where certain Python variable names were incorrectly quoted when inserted via autocompletion. (#14560)\
*   Fixed an issue where column names starting with numbers were not properly quoted when inserted as a completion. (#13290)\
*   Reformat Code no longer inserts whitespace around ‘^’ operator. (#14973)\
*   Auto-saves no longer trim trailing whitespace on the line containing the cursor. (#14829)\
*   Fixed an issue where pressing Tab would insert a literal tab instead of indenting a multi-line selection. (#15046)\
*   Fixed an issue where debugger breakpoints did not function correctly in some cases with R 4.4. (#15072)\
*   RStudio over-aggressively required packages to be rebuilt when setting breakpoints. (#15201)\
*   Clicking in the editor gutter to toggle a breakpoint no longer also selects the associated line. (#15226)\
*   Fixed a performance regression that occurred when requesting completions for very large R objects. (#15422)\
*   RStudio now uses current session repositories when installing package dependencies via background jobs. (#10016)\
*   RStudio now forward the current ‘repos’ option for actions taken in the Build pane. (#5793)\
*   Executing `options(warn = ...)` in an R code chunk now persists beyond chunk execution. (#15030)\
*   Prevent attempting to start Copilot on a non-main thread. (#14952)\
*   Fixed an issue where updating the Copilot agent on Windows could fail if Copilot was already in use. (#14850)\
*   Prompt for personal access token instead of password when using GitHub via HTTPS. (#14103)\
*   RStudio now includes Markdown headers without any label in the document outline. (#14552)\
*   Remove focus-visible polyfill and instead use native browser :focus-visible pseudoclass \[Accessibility\]. (#14352)\
*   Fixed an issue where RStudio could hang on startup with projects containing a very large number of files. (#15434)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-48)\
\
*   Fixed an issue with Workbench login not respecting “Stay signed in when browser closes” when using Single Sign-On (SSO). (rstudio-pro#5392)\
*   Fixed Slurm queue (partition) selection behavior in the launcher UI (**Slurm resource profiles that specify an invalid queue are now disabled in the UI**). (rstudio-pro#7025)\
*   Fixed several cross-reference links in the Posit Workbench Administration Guide and Posit Workbench User Guide - VS Code sections. (rstudio-pro#6678)\
*   Fixed heading anchor ID issue in Posit Administration Guide - VS Code PWB Code Server section. (rstudio-pro#6961)\
*   Fixed inconsistencies in naming throughout Reference Architecture sections. (rstudio-pro#6832)\
*   Fixed an issue where Workbench does not properly set the queue when starting a session (rstudio-pro#7025)\
*   Fixed an issue where the displayed contianer image does not match the used image when starting a Kubernetes session (rstudio-pro#6910)\
*   Fixed an issue where a user mismatch would return a 500 instead of a 401 (rstudio-pro#6579)\
*   Fixed an issue where Workbench Jobs in VS Code show NaN when there is no maximum memory value configured (rstudio-pro#6510)\
*   Fixed an issue when resuming RStudio Pro sessions where the version of unattached R packages is not prsevered (rstudio-pro#3074)\
\
### Upgrade Instructions[](https://docs.posit.co/ide/news/#rstudio-2024.12.0-upgrade)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-49)\
\
If running Workbench behind a proxy server, you may need to update your `NO_PROXY` configuration:\
\
*   HTTP Proxy variables are now supported in rserver and rsession, so it’s important to include local addresses to Job Launcher sessions and other internal services in your `NO_PROXY` list.\
*   See the [Outgoing Proxies](https://docs.posit.co/ide/server-pro/access_and_security/outgoing_proxies.html)\
     section of the Posit Workbench Administration Guide for more information. (rstudio-pro#5893)\
\
You may also want to update the following configuration entries, as the default values have changed:\
\
|     |     |     |     |\
| --- | --- | --- | --- |   \
| `rsession-proxy-max-wait-secs` | 10  | 30  | (rstudio-pro#6149) |\
| `www-thread-pool-size` | 2   | 6   | (rstudio-pro#6149) |\
\
### Dependencies[](https://docs.posit.co/ide/news/#rstudio-2024.12.0-dependencies)\
\
*   Updated GWT to version 2.10.1. (#15011)\
*   Updated Electron to version 31.7.6. (#14982; Desktop)\
\
### Deprecated / Removed[](https://docs.posit.co/ide/news/#rstudio-2024.12.0-deprecated)\
\
*   Removed user preference for turning off focus indicator rectangles. (#14352)\
*   Removed support for `rsconnect-jupyter`; publish Jupyter Notebooks to Connect using `rsconnect-python`. See the [Publishing Jupyter Notebooks to Connect](https://docs.posit.co/ide/server-pro/integration/jupyter-multiple-python-versions.html#publishing-jupyter-notebooks-to-connect)\
     section of the Posit Workbench Administration Guide for more information. (rstudio-pro#6989)\
\
2024.09.1[](https://docs.posit.co/ide/news/#rstudio-2024.09.1)\
\
---------------------------------------------------------------\
\
**“Cranberry Hibiscus”** | Date: 2024-11-04\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2024.09.1-new)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-39)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-50)\
\
*   Add support for conditional regex replacement strings in proxied auth. (rstudio-pro#6753)\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2024.09.1-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-40)\
\
*   Fixed an issue where the R session could crash on connect while generating console output. (#15330)\
*   Fixed Visual Editor losing raw HTML code blocks. (#15189)\
*   Fixed Visual Editor losing raw LaTeX code blocks. (#15253)\
*   Fixed opening and saving files on UNC paths. (Windows Desktop, #15280)\
*   Fixed package builds failing when set to generate documents on build. (#15236)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-51)\
\
*   Fixed OAuth failure for Snowflake roles that must be double-quoted. (rstudio-pro#6881)\
*   Fixed a bug in the Homepage launcher UI where limits and constraints could be copied to the Local cluster launch spec from a different cluster resulting in a launch failure. (rstudio-pro#6913)\
\
### Deprecated / Removed[](https://docs.posit.co/ide/news/#rstudio-2024.09.1-deprecated)\
\
*   Removed msys-ssh client from Windows Desktop install and stopped setting RSTUDIO\_MSYS\_SSH environment variable. (rstudio-pro#6880)\
\
2024.09.0[](https://docs.posit.co/ide/news/#rstudio-2024.09.0)\
\
---------------------------------------------------------------\
\
**“Cranberry Hibiscus”** | Date: 2024-09-23 | [Release Blog Post](https://posit.co/blog/rstudio-2024-09-0-whats-new/)\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2024.09.0-new)\
\
*   Posit Product Documentation theme v4.0.2; adds dark mode and several accessibility improvements. (rstudio-pro#6373)\
*   Added ability for RStudio and Workbench to use AES 256 encryption. (rstudio-pro#4011)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-41)\
\
*   You can now toggle between R and Python in the Console by clicking the language’s logo in the Console pane header. (#11613)\
*   Allow customization of the project scratch path location. (#14875)\
*   Restart commands are now run after restoring the search path + global environment by default. (#14636)\
*   The “Save as Image” dialog now includes a “Use device pixel ratio” check box, controlling whether plots are scaled according to the current display’s DPI. (#14727)\
*   The “Soft-wrap R source files” preference now applies to all source files, and has been relabelled appropriately. (#10940)\
*   RStudio now supports Electron flags set via `~/.config/rstudio/electron-flags.conf` or `~/.config/electron-flags.conf` on Linux / macOS. On Windows, the paths are `%LocalAppData%\RStudio\electron-flags.conf` and `%LocalAppData%\electron-flags.conf`. (#14641)\
*   RStudio now uses a glimpse-like display for data.frame list-column entries. (#14257)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-52)\
\
*   Quitting Jupyter and VS Code sessions from the home page no longer force quits them immediately; instead, they are given time to exit gracefully, as with RStudio Pro sessions. (rstudio-pro#5317)\
*   Workbench jobs launched on Kubernetes or on Slurm with Singularity support now default to using the same container image as the parent session. (rstudio-pro#5875)\
*   Workbench’s Prometheus metrics now track R and Python jobs launched, in addition to sessions. (rstudio-pro#6271)\
*   When launching sessions on Slurm, environment variables set by the Slurm scheduler itself should now be available to sessions. (rstudio-pro#5148, rstudio-pro#4692, rstudio-pro#3255)\
*   The `launcher-sessions-forward-container-environment` flag has been deprecated and will be removed in a future version. Use `launcher-sessions-forward-environment=0` to disable environment variable forwarding instead. (rstudio-pro#5895)\
*   The New Project dialog in RStudio Pro now defaults to the R version of the current session, rather than the system default. (rstudio-pro#4244)\
*   Workbench jobs launched from RStudio Pro now default to the R version of the current session, rather than the system default. (rstudio-pro#5903)\
*   Added support for Jupyter Notebook 7. (rstudio-pro#6266)\
*   Replaced code server binary with PWB Code Server. PWB Code Server is bundled with the PWB VS Code Extension, so a separate install is no longer required. It is a fork of VS Code 1.93.0. (rstudio-pro#6265)\
*   In VS Code sessions, Workbench now preserves the open directory or workspace on a per-session basis. (rstudio-pro#6491)\
*   Fixed an issue preventing potential data leakage between users in the same browser session. As a result, the minimum recommended version of Firefox is now `126.0`. See the [Browser requirements](https://docs.posit.co/ide/server-pro/2024.09.1/getting_started/requirements.html#browser-requirements)\
     section of the admin guide for more details. (vscode-server#17)\
*   Disabled Jupyter Notebooks by default on fresh installs of PWB. (rstudio-pro#6269)\
*   Workbench now respects the `SLURM_CONF` environment variable, which can be used to point to a non-standard location for the Slurm configuration file. (launcher#767)\
*   Workbench now does a better job of tracking which Slurm jobs it owns, allowing multiple independent Workbench servers to use the same Slurm cluster, or a single Workbench server to use the same backing Slurm cluster with different configurations. (launcher#908)\
*   Preview of the workbench api, using api-tokens for launching sessions and session status. See documentation for details.\
*   Added support for just-in-time provisioning of local user accounts for Proxied Auth, OpenID Connect, and SAML Authentication. Just-in-time provisioning creates users on first login, and can serve as an alternative to SCIM-based provisioning for Identity Providers that do not support the SCIM protocol. (rstudio-pro#5909)\
*   Workbench now has a native integration for Snowflake that includes support for managed Snowflake OAuth credentials, allowing end users to sign into a Snowflake account from the home page and, using their existing identity, be immediately granted access to data and warehouses. (rstudio-pro#6280)\
*   Added visual credential controls to the New Session dialog to quickly sign into and select credentials for new sessions. (rstudio-pro#6287)\
*   Added an Edit Credentials dialog to allow users to select and sign into Workbench-supported cloud providers, with a few additional controls over the selection widget. (rstudio-pro#6287)\
*   Updated Admin Guide with additional guidance for Kubernetes installations on [accessing license files from secrets](https://docs.posit.co/ide/server-pro/2024.09.0/getting_started/installation/kubernetes_installation.html#create-a-secret-containing-a-license-file)\
     and [specifying PostgreSQL database passwords as environment variables](https://docs.posit.co/ide/server-pro/2024.09.0/getting_started/installation/kubernetes_installation.html#create-a-secret-containing-a-postgresql-database-password)\
    . (rstudio-pro#5312)\
*   Improved performance of Workbench when automatic user provisioning is enabled by adding support for the Workbench NSS library to communicate over unix socket. (rstudio-pro#6591)\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2024.09.0-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-42)\
\
*   The RStudio diagnostics system no longer automatically loads packages when encountering calls of the form `dplyr::mutate()`. (#9692)\
*   Fixed an issue where breakpoints set within `observeEvent()` calls in Shiny applications did not behave correctly. (#14815)\
*   Fixed an issue where Build output from ‘Run Tests’ was not appropriately colored. (#13088)\
*   Fixed an issue where various editor commands (Reindent Lines; Run Chunks) could fail in a document containing Quarto callout blocks. (#14640)\
*   Fixed an issue where end fold markers were not rendered correctly in Quarto documents. (#14699)\
*   Fixed an issue where the context menu sometimes did not display when right-clicking a word in the editor. (#14575)\
*   Fixed an issue where the “Go to directory…” button brought up the wrong dialog (#14501; Desktop)\
*   Fixed an issue where “View plot after saving” in the Save Plot as Image dialog sometimes did not work. (#14702)\
*   Fixed an issue where the IDE could hang when navigating the Files pane to a directory containing a very large number of files. (#13426)\
*   Fixed an issue where RStudio could trigger active bindings in environments when requesting completions. (#14784)\
*   Fixed an issue where the editor scroll speed had inadvertently been decreased. (#14664)\
*   Fixed an issue where external links couldn’t be opened from a popped-out Help pane window. (#14801; Desktop)\
*   Fixed an issue where loaded package DLLs were not unloaded prior to attempting to build and install an under-development package from the Packages pane. (#13399)\
*   Fixed an issue where breakpoints could not be added to an already-sourced file in some cases. (#14682)\
*   Fixed an issue where autocompletion results did not display for datasets imported via `haven::read_sav()` in some scenarios. (#14672)\
*   Fixed an issue where paths were not tilde-aliased after selection in certain desktop dialogs. (#14851)\
*   Fixed an issue where the RStudio diagnostics system could emit spurious errors for documents using the R pipebind placeholder `_`. (#14713)\
*   Fixed an issue where RStudio incorrectly modified the PATH when “Automatically activate project-local Python environments” was selected. (#14659)\
*   Fixed an issue where column name completions could be very slow for SQL tables with dbplyr (>= 2.4.0). (#14864)\
*   Remove superfluous Uninstall shortcut and Start Menu folder (#1900; Desktop installer on Windows)\
*   Hide Refresh button while Replace All operation is running in the Find in Files pane. (#13873)\
*   Stop the File Pane’s “Copy To” operation from deleting the file when source and destination are the same. (#14525)\
*   Fix keyboard shortcuts acting on the wrong source file when using Visual Editor in source columns or separate windows. (#12581, #11684)\
*   Fix startup error due to invalid zoom setting triggering a config schema violation. (#14690)\
*   Removed extra spaces after package names in warning message about required packages. (#14608)\
*   Moved the “Sign commit” check box to Git/Svn global options panel. (##14559)\
*   RStudio’s editor highlighting no longer accepts embedded spaces in ‘#|’ comment prefixes. (#14592)\
*   RStudio now preserves a file’s existing line endings when performing a Find and Replace. (#14796)\
*   Fixed an issue with loading and saving files to folders whose path partially patches the user’s home folder. (#14764)\
*   Fixed an issue where headers without a label in R Markdown documents were not shown in the scope tree. (#13159)\
*   Fixed an issue where RStudio could launch with an incorrect initial working directory when using multiple sessions. (#14695)\
*   Fixed an issue where ggplot2 aesthetic completions were not provided for plots assigned to a variable. (#14566)\
*   Fixed an issue where attempting to inspect a list-column entry in a View()-ed data.frame with custom row names would fail. (#14509)\
*   Fixed an issue where the document outline in Quarto documents could incorrectly render in very long documents in some scenarios. (#14906)\
*   Fixed an issue with a once-in-a-long-while auto-save error dialog. (rstudio-pro#6468)\
*   Fixed an issue with linux PAM session error handling. (#12116)\
*   Fixed an issue where the RStudio debugger location could be incorrect when debugging a package’s S3 method. (#14499)\
*   Fixed an issue where RStudio could hang when clicking on a citation in the visual editor. (#10823)\
*   Fixed RStudio Desktop Pro crashing at startup on macOS 15 Sequoia. (rstudio-pro#6777)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-53)\
\
*   Workbench jobs now set resource profiles correctly. (rstudio-pro#5217)\
*   When launching a Workbench job from RStudio Pro, changing fields in the Options tab no longer resets the selected R version in the Environment tab. (rstudio-pro#5218)\
*   Fixed bug that prevented users from receiving the admin-configured default settings when launching VS Code sessions. (rstudio-pro#6207)\
*   RStudio Pro sessions running inside Singularity containers on Slurm now respect the `modules-bin-path` setting. (rstudio-pro#6319)\
*   When user provisioning is enabled, server logs no longer contain related debug messages unless debug logging is enabled. (rstudio-pro#6480)\
*   Trailing slashes in Databricks workspace URLs in the `databricks.conf` file no longer prevent users from signing in to Databricks from the home page. (rstudio-pro#6435)\
*   Resource profiles on Kubernetes and Slurm are now listed in the order in which they appear in the config file. (rstudio-pro#6485)\
*   Switching the selected IDE when launching a session from the home page no longer resets the image selection. (rstudio-pro#4079)\
*   Removed an error starting sessions in some docker containers about resetting keyrings, other unnecessary debug messages. (rstudio-pro#6444)\
*   Fixed a bug where users who attempted login before being provisioned could not log in after being provisioned. (rstudio-pro#6564)\
*   Fixed bug that prevented Workbench from respecting licenses with an unlimited named user limit when re-activating SCIM provisioned users. (rstudio-pro#6561)\
*   Fixed bug where user provisioning would not work properly if the homedir column in the database for any user was null. (rstudio-pro#6587)\
*   Fixed a pagination issue in the SCIM API that could prevent more than 100 users from being provisioned via Okta. (rstudio-pro#6608)\
*   Fixed various bugs that could cause NSS requests to fail when automatic user provisioning is enabled. (rstudio-pro#6676, rstudio-pro#6657)\
\
### Upgrade Instructions[](https://docs.posit.co/ide/news/#rstudio-2024.09.0-upgrade)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#upgrade-pwb-fr-2024.04.X)\
\
If upgrading from Workbench 2024.04.x with automatic user provisioning enabled, fix a performance and reliability issue:\
\
*   In the `workbench-nss.conf` file, update the `server-address` setting to:  \
    `unix:/var/run/rstudio-server/rstudio-rserver/user-service.socket`\
\
See the [User Provisioning Configuration](https://docs.posit.co/ide/server-pro/user_provisioning/configuration.html)\
 section in the Posit Workbench Administrator Guide for more information. (rstudio-pro#6591)\
\
### Dependencies[](https://docs.posit.co/ide/news/#rstudio-2024.09.0-dependencies)\
\
Updated the following dependencies to the listed version:\
\
|     |     |     |\
| --- | --- | --- |\
| MathJax | 2.7.9 | (#11535) |\
| node.js | 20.15.1 | (#14826) |\
| Electron | 30.4.0 | (#14582; Desktop) |\
| Quarto | 1.5.57 | (#14884, #15102) |\
| rserver-saml | 0.8.0 | (rstudio-pro#6529) |\
| rserver-openid | 0.7.0 | (rstudio-pro#6635) |\
| nginx | 1.26.0 | (rstudio-pro#6581) |\
\
2024.04.2[](https://docs.posit.co/ide/news/#rstudio-2024.04.2)\
\
---------------------------------------------------------------\
\
**“Chocolate Cosmos”** | Date: 2024-06-10\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2024.04.2-new)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-54)\
\
*   Added a Generic Architectures page to the Workbench Admin Guide\
*   Added an AWS Single Server reference architecture to the Workbench Admin Guide\
*   Added an AWS EKS reference architecture to the Workbench Admin Guide\
*   Added a Background Jobs vs Workbench jobs page to the Workbench Admin Guide\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2024.04.2-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-43)\
\
*   Fixed an issue where editor tools (e.g., Reindent Lines) did not work in Quarto documents with `:::` blocks. (#14652; #14640)\
*   Fixed an issue where insertion of braces in Sweave documents did not function as intended. (#14667; #14646)\
*   Fixed ability to build using system YAML (#14629)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-55)\
\
*   Fixed an issue introduced in 2024.04.0 with the create-container-user feature for job launcher plugins that reuse a container for more than one session (rstudio/rstudio-pro#6408)\
*   Improved some AWS documentation links in the reference architecture section\
\
### Dependencies[](https://docs.posit.co/ide/news/#rstudio-2024.04.2-dependencies)\
\
*   Updated node.js to version 18.20.3 (#14731)\
*   Updated Quarto to version 1.4.555 (#14779)\
*   Updated Electron to version 28.3.1 (#14732)\
\
2024.04.1[](https://docs.posit.co/ide/news/#rstudio-2024.04.1)\
\
---------------------------------------------------------------\
\
**“Chocolate Cosmos”** | Date: 2024-05-13\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2024.04.1-new)\
\
*   Added support for R 4.4.0\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-44)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-56)\
\
*   On the homepage, launcher errors will now show a “details” drop-down containing the raw error output if launcher does not recognize the error type. (rstudio/rstudio-pro#4717)\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2024.04.1-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-45)\
\
*   Fixed an issue where RStudio could crash when requesting completions within a ggplot2 aes() call, for datasets containing multi-byte variable names. (#14625)\
\
2024.04.0[](https://docs.posit.co/ide/news/#rstudio-2024.04.0)\
\
---------------------------------------------------------------\
\
**“Chocolate Cosmos”** | Date: 2024-04-29 | [Release Blog Post](https://posit.co/blog/rstudio-2024-04-0-whats-new/)\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2024.04.0-new)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-46)\
\
*   RStudio now requires R 3.6.0 or newer. (#14210)\
*   RStudio’s auto-completion system now supports ggplot2 aesthetic names and data columns. (#8444)\
*   RStudio’s auto-completion system now supports the display of the “label” attribute. (#14242)\
*   RStudio Desktop on Windows and Linux supports auto-hiding the menu bar. (#8932)\
*   RStudio Desktop on Windows and Linux supports full-screen mode via F11. (#3243)\
*   RStudio Desktop now supports pasting of file paths for files copied to the clipboard. (#14240)\
*   RStudio now reports a diagnostics warning when `=` (rather than `==`) is used in `if`, `for`, and `while` conditionals. (#14455)\
*   R projects can be given a custom display name in Project Options. (#1909)\
*   The automatic display of Copilot code completions can now be controlled via a user preference. (#14033)\
*   Copilot code suggestions can now be requested via the keyboard shortcut `Ctrl + \`.\
*   The next word in a Copilot code suggestion can now be accepted via `Ctrl + Right` (`Cmd + Right` on macOS). (#14395)\
*   RStudio now highlights and lints Quarto chunk options in Python code chunks.\
*   RStudio no longer highlights `\[ \]` and `\( \)` Mathjax equations; prefer `$$ $$` and `$ $` instead. (#12862)\
*   Added cmake option to build RStudio without the check for updates feature. (#13236)\
*   Allow choosing R from non-standard location at startup. (#14180; Windows Desktop)\
*   Add `EnvironmentFile` support to systemd service definitions. (#13819)\
*   RStudio’s GWT sources can now be built with JDKs > 11. (#11242)\
*   Show grey background instead of solid-white during Desktop startup. (#13768)\
*   The ‘restartSession()’ API method gains the ‘clean’ argument. (#2841)\
*   ‘dot’ chunks in R Markdown documents are now executable. (#14063)\
*   (rstudioapi) Fixed an issue where selectFile() did not parse filter strings in a cross-platform way. (#13994)\
*   Show Quarto version information in the About dialog. (#14263)\
*   RStudio now reports repository validation errors (if any) when adding secondary repositories in the Global Options -> Packages pane. (#13842)\
*   The working directory of a background job now defaults to the .Rproj location when a project is open. (#12600)\
*   Add search results copy button and search results breadcrumbs to RStudio User Guide. (#13618, #14069)\
*   RStudio now supports generation of a Copilot diagnostic report from the Copilot preferences pane. (#14358)\
*   The RStudio debugger is now better at matching debugged code to source documents. (#13925)\
*   RStudio no longer includes spurious chunk markers from Copilot completion results. (#13686)\
*   Added new commands which toggle the maximized state of Console, Source, and Tab Group quadrants \[Accessibility\]. (#7022)\
*   RStudio now prints a warning if an overly-long line of console input is truncated when sending to R. (#14420)\
*   Implemented Posit Product Documentation theme to RStudio & Posit Workbench Release Notes and RStudio IDE User Guide via Quarto extension. (#14513)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-57)\
\
*   Show custom project names on Workbench homepage. (rstudio-pro#5589)\
*   Added support for JupyterLab 4 through the Python extension [PWB JupyterLab](https://pypi.org/project/pwb-jupyterlab/)\
    . (rstudio-pro#5777)\
*   Added search results copy button and search results breadcrumbs to Workbench Administration Guide, Workbench User Guide, RStudio Desktop Pro Administration Guide. (#5088, #5603)\
*   Migrated Troubleshooting Launcher and Kubernetes guide from docs.posit.co site to Workbench Administration Guide: Job Launcher > Launcher Troubleshooting section. (#5720)\
*   Added search results copy button and search results breadcrumbs to Workbench Administration Guide, Workbench User Guide, RStudio Desktop Pro Administration Guide. (#5088, #5603)\
*   When launching sessions from the home page, memory is now shown in GB rather than MB. (rstudio-pro#2722)\
*   When running sessions on Kubernetes or Slurm with Singularity, the home page now remembers the container image used most recently and sets it as the default. This includes custom images, when permitted. (rstudio-pro#3601, rstudio-pro#4079)\
*   When launching a session from the home page on Kubernetes or Slurm, the dropdown for available container images is now better organized and manages long image names more gracefully. (rstudio-pro#5630)\
*   Opening the job summary for a session on the home page now shows much more detailed information, including the session’s host (if available), AWS role and/or Databricks Workspace (if any), queue (on Slurm), platform-native ID (on Slurm and Kubernetes) and resource profile (if applicable). (rstudio-pro#3690, rstudio-pro#5537)\
*   The Databricks pane is now enabled by default if there are Databricks workspaces configured in the `databricks.conf` file. There is no need to enable it separately. To disable the pane, set `databricks-enabled=0` in the `rserver.conf` file. (rstudio-pro#5556)\
*   A new icon on the RStudio Pro toolbar shows information on active AWS or Databricks credentials, if present. (rstudio-pro#5860)\
*   The PostgreSQL password can now be set via environment variable. (rstudio-pro#5332)\
*   Implemented Posit Product Documentation theme in Posit Workbench Administration Guide, Posit Workbench Licenses, Posit Workbench User Guide, and RStudio Desktop Administration Guide via Quarto extension. (rstudio-pro#5729)\
*   Performance improvement where nginx handles static files, configurable with nginx.static.conf file. (rstudio-pro#5671)\
*   VSCode: upgraded coder/code-server to 4.22.1 (VS Code version 1.87.2) on all operating systems except CentOS 7. Upgraded to coder/code-server 4.16.1 (VS Code version 1.80.2) on Centos 7.\
*   Added preview of Code OSS - with Posit Workbench, pwb-code-server version 2024.04-b31 (VS Code version 1.87.0). (rstudio-pro#3777)\
*   Robustness and scalability improvements for streaming connections. Close all streaming connections when tabs are invisible, and impose limits on “session output view”. Added options for tuning large-scale system performance: launcher-sessions-proxy-timeout-seconds, max-streams-per-user, streaming-connection-timeout-seconds rserver.conf option. . (rstudio-pro#5888, rstudio-pro#5616, rstudio-pro#5771, rstudio-pro#3417)\
*   Added support for debug, and strace session diagnostics for individual user sessions. Create a file with ‘strace’ or ‘debug’ in ~/.config/rsession-diagnostics or ~/.config/pwb/jupyter-diagnostics, vscode-diagnostics. Logs in ~/.local/share/{rstudio,pwb}/log. (rstudio-pro#5529)\
*   Posit Workbench no longer has a dependency on the `libuser` package. (rstudio-pro#4261)\
*   Container users that have special characters in their names, such as `@`, can now be created at session start. (rstudio-pro#2714)\
*   Prometheus metrics are now available as a Preview feature. (rstudio-pro#5793)\
*   Prometheus metrics can now be enabled or disabled with `metrics-enabled=[1|0]` in `rserver.conf`. (rstudio-pro#5792)\
*   Prometheus metrics can now be configured. For more details see [Promethes Metrics in the Workbench Admin Guide](https://docs.posit.co/ide/server-pro/2024.04.0/auditing_and_monitoring/prometheus_metrics.html)\
    . (rstudio-pro#5791)\
*   Added support for automatically provisioning users when using Okta or Microsoft Entra ID as an IdP. When using this feature, users can be assigned to Workbench from the IdP and do not need to be created as POSIX users. This feature also supports migrating from local, or ldap/sssd, users to IdP provisioned users. For more details see the [User Provisioning section of the Admin Guide](https://docs.posit.co/ide/server-pro/2024.04.0/user_provisioning/user_provisioning.html)\
    . (rstudio-pro#2784)\
*   Move the force-quit session option into the session info dialog. (rstudio-pro#3385)\
*   Added support for setting Posit Workbench envrionment variables at the service level in an EnvironmentFile: `/etc/default/rstudio-server`. (rstudio-pro#5337)\
*   Added support for Slurm with Singularity and Apptainer. (rstudio-pro#5236)\
*   Updated the Workbench JupyterLab 3 extension to v1.1.738 to upgrade NPM dependencies. (rstudio-pro#5900)\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2024.04.0-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-47)\
\
*   Fixed an issue where Stage chunk and Stage line in the Review Changes UI failed in some scenarios. (#5476)\
*   Fixed shortcut for inserting an assignment operator to work on non-US English keyboards. (#12457)\
*   Fixed an issue where the menubar would show on secondary windows if Alt key was pressed. (#13973)\
*   Fixed Windows installer to delete Start Menu shortcut during uninstall. (#13936)\
*   Fixed current Git branch not always showing correctly in external editor windows. (#14029)\
*   Fixed the tooltip to show the correct keyboard shortcut when hovering over URLs in the editor. (#12504)\
*   Fixed Save As dialog on Windows not showing Save As Type field when extensions are hidden. (#12965)\
*   Fixed GitHub Copilot project preferences not showing the correct status message. (#14064)\
*   Fixed an issue where Quarto chunk option completions were not displayed at the start of a comment. (#14074)\
*   Fixed an issue where pipes containing a large number of comments were not indented correctly. (#12674)\
*   Fixed an issue where RStudio would unnecessarily list directory contents when opening a file. (#14096)\
*   Localize Copilot-related user interface strings into French. (#14092)\
*   Improved highlighting of YAML chunk options for Quarto Documents. (#13836)\
*   Removed obsolete “Use Internet Explorer library/proxy” checkbox from Packages settings. (#13250)\
*   Improved error handling for Desktop Pro license handling. (rstudio-pro#4873)\
*   Fixed exception being logged when copying or cutting from the editor in a separate window. (#14140)\
*   Fixed an issue where RStudio’s R diagnostics warned about potentially missing arguments even when disabled via preferences. (#14046)\
*   Fixed an issue where the Visual Editor’s toolbar controls were duplicated on format change. (#12227)\
*   Fixed regression that caused extra whitespace at the bottom of some popups. (#14223)\
*   Fixed type dropdowns not working in dataset import when user-interface is in French. (#14224)\
*   Fixed an issue where RStudio failed to retrieve help for certain S3 methods. (#14232)\
*   Fixed a regression where the Data Viewer did not display ‘variable.labels’ for columns. (#14265)\
*   Fixed an issue where autocompletion help was not properly displayed for development help topics. (#14273)\
*   Fixed an issue where Shiny onSessionEnded callbacks could be interrupted when stopped in RStudio. (#13394)\
*   Fixed Copyright date ranges for Release Notes and RStudio IDE User Guide. (#14078)\
*   Fixed Copyright date ranges for Workbench Administrator and Workbench User Guide, and RStudio Desktop Pro Administration Guide. (#5614)\
*   Fixed misencoded Hunspell dictionaries. (#8147)\
*   Fixed an issue where the RStudio debugger failed to step through statements within a tryCatch() call. (#14306)\
*   Improved responsiveness of C / C++ editor intelligence features when switching Git branches. (#14320)\
*   If R is not found when starting RStudio Desktop on Linux and macOS, Rstudio Desktop shows an error dialog. (#14343)\
*   An empty `rstudio-prefs.json` no longer logs spurious JSON parsing errors. (rstudio-pro#4347)\
*   Fixed Help pane’s Next and Previous find-in-topic buttons to have meaningful accessible labels \[Accessibility\]. (#14347)\
*   Fixed an issue where the RStudio debugger would re-focus a debugged context over-aggressively. (#10664)\
*   Fixed handling of duplicated calls in debugger when source references not available. (#14276)\
*   Fixed issue where stepping through lines of code in tryCatch() would provide incorrect debug highlight. (#14306)\
*   Fixed an issue where PATH modifications in .Renviron / .Rprofile could be lost on macOS. (#9815)\
*   Fixed an issue where custom headers were not propagated to `available.packages()` when calling `install.packages()`. (#14282)\
*   Fixed an issue where code highlight in Sweave expressions was incorrectly handled. (#14382)\
*   Fixed an issue where the Edit button in the Viewer pane could fail for Quarto documents. (#14325)\
*   Fixed an issue where terminal history would show internal commands. (#9833)\
*   Fixed an issue where RStudio could fail to launch with Conda builds of R. (#13184)\
*   Fixed an issue where hovering over S4 class names in the Help pane could produce an R error. (#13344)\
*   Fixed an issue where defining a custom viewer method produced an R error when View was called. (#14439)\
*   Fixed an issue where Quarto dashboards could not be previewed if their file path contained a single quote. (#13900)\
*   Fixed an issue where language objects (calls, formulas) were not described in the Environment pane. (#14446)\
*   Improved some French translations of the UI.\
*   Fixed an issue where searches in the Help pane could fail for entries like `[<-`. (#10975)\
*   Fixed an issue where the “Save workspace on exit” preference was ignored in some cases. (#14258)\
*   Fixed an issue where the NEWS button in the Update Packages dialog could fail to find the package NEWS file in some cases. (#12648)\
*   Fixed an issue where Tensorflow object completions were not generated in some contexts. (#14524)\
*   Fixed an issue in Vim where bracket highlighting followed the bracket behind the cursor when in normal mode. (#4152)\
*   Fixed an issue where ELECTRON\_RUN\_AS\_NODE was set to true. Thanks to Mykola Grymalyuk of RIPEDA Consulting for reporting this.\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-58)\
\
*   Fixed an issue where Professional Driver installation could fail on macOS. (rstudio-pro#5168)\
*   Fixed Copyright date ranges for Workbench Administrator Guide and Workbench User Guide. (rstudio-pro#5865)\
*   Fixed low-contrast text on Workbench pages \[Accessibility\]. (rstudio-pro#4464)\
*   The terminal pane of JupyterLab sessions now respects the user’s default shell. (rstudio-pro#5484)\
*   The Databricks pane now respects the `databricks-enabled=1` setting in the `rserver.conf` file even when running in legacy RStudio Server Pro mode. (rstudio-pro#5695)\
*   Fixed an issue where pending or failed sessions that were launched on Slurm will no longer erroneously appear in the Workbench Jobs pane on the home page. (rstudio-pro#4846)\
*   VSCode sessions will now respect the `user-data-dir` option in `vscode.conf` when installing extensions in a user’s directory on vscode session startup. (rstudio-pro#6078)\
*   Fixed an issue where `rstudio-server license-manager deactivate` would emit an error indicating incorrect usage of the `kill` command when `rstudio-server` is already stopped. (rstudio-pro#5549)\
*   Fixed an error message in the Databricks pane of RStudio Pro sessions when Databricks authentication is not available. (rstudio-pro#5583)\
*   Fixed an issue where `rstudio-launcher` commands would not work when `RSTUDIO_CONFIG_DIR` or `XDG_CONFIG_DIRS` was set in systemctl overrides. (rstudio-pro#4122)\
*   Fixed an issue with the permissions on files uploaded from shared projects in RStudio Pro sessions. (rstudio-pro#3134)\
*   Fixed setting project sharing ACLs on parent directories for projects in subfolders. (rstudio-pro#5309)\
*   Fixed sporadic CPU usage and crash in rworkspaces. (rstudio-pro#5690)\
*   Fixed problem with `rstudio-server reload` changing permissions on nginx proxy/body dirs leading to user errors accessing the system. (rstudio-pro#5636)\
\
### Dependencies[](https://docs.posit.co/ide/news/#rstudio-2024.04.0-dependencies)\
\
*   Updated Ace to version 1.32.5. (#14227; Desktop + Server)\
*   Updated Electron to version 28.2.6. (#14055; Desktop)\
*   Updated GWT to version 2.10.0. (#11505; Desktop + Server)\
*   Updated NSIS to version 3.09. (#14123; Windows Desktop)\
*   Updated OpenSSL to version 3.1.4. (Windows Desktop)\
*   Updated nginx to 1.25.4. (rstudio-pro#5970)\
*   Updated node.js to version 18.19.1. (#14373, rstudio-pro#5935)\
*   Updated Quarto to version 1.4.553. (Desktop + Server)\
*   Updated zlib to 1.3.1. (rstudio-pro#5971)\
\
### Deprecated / Removed[](https://docs.posit.co/ide/news/#rstudio-2024.04.0-deprecated)\
\
*   Due to the upcoming [end of support for CentOS 7](https://posit.co/about/platform-support/)\
     in June 2024, CentOS 7 builds are no longer available for public download. If you have any questions, please contact Posit Support.\
\
2023.12.1[](https://docs.posit.co/ide/news/#rstudio-2023.12.1)\
\
---------------------------------------------------------------\
\
**“Ocean Storm”** | Date: 2024-01-29\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2023.12.1-new)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-48)\
\
*   Changed the failure message for server no-responses (http code 0) to be more helpful to the user (rstudio/rstudio-pro#5646)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-59)\
\
*   Added Reference Architectures (ParallelCluster) documentation to the Posit Workbench Administration Guide (rstudio-pro#6178)\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2023.12.1-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-49)\
\
*   Removed GitHub Copilot preview label and disclaimer in Copilot options panes (#14067)\
*   Fixed an issue where GitHub Copilot indexed binary files when project indexing enabled (#14106)\
*   Fixed regression that prevented opening help topics in separate window (#14097)\
*   Increased open files limit (#14148)\
*   Fixed an issue with saving pane layouts for Desktop Pro and Workbench (rstudio-pro#5612)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-60)\
\
*   Fixed join session when ready control not responding to mouse clicks in all areas (rstudio/rstudio-pro#5609)\
*   Fixed intermittent rserver crash when joining a session started with the job launcher that is not immediately available (rstudio-pro#5579)\
*   Fixed regression introduced in 2023.06 with `rstudio-server reload` where permission changed on nginx directories caused intermittent content loading errors (rstudio-pro#5636)\
*   Fixed intermittent rworkspaces performance problem where in unusual circumstances, it would make repeated get\_jobs requests (rstudio-pro#5690)\
*   Fixed rworkspaces crash with debug logging enabled when get\_jobs request returned an error (rstudio/rstudio-pro#5690)\
*   Fixed supported Slurm versions in Integrating with Slurm - Administration Guide (rstudio-pro#5857)\
*   Added missing Slurm dependency to Integrating with Slurm documentation (rstudio-pro#5876)\
*   Removal of Debian 10 due to end of support (rstudio-pro#5925)\
\
2023.12.0[](https://docs.posit.co/ide/news/#rstudio-2023.12.0)\
\
---------------------------------------------------------------\
\
**“Ocean Storm”** | Date: 2023-12-15 | [Release Blog Post](https://posit.co/blog/rstudio-2023-12-0-whats-new/)\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2023.12.0-new)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-50)\
\
*   Updated Ace to version 1.28. (#13708)\
*   Updated Boost to version 1.83.0. (#13577)\
*   Updated Electron to version 26.2.4. (#13577)\
*   Updated the default version of the GitHub Copilot agent to 1.10.3. (#13729)\
*   Updated openssl to 1.1.1w on Mac and Windows. (#13683)\
*   Updated Electron Forge to version 6.4.2 and Webpack to version 5.89.0. (rstudio-pro#5383)\
*   Updated Quarto to version 1.3.450. (#13914)\
*   RStudio now supports highlighting of inline YAML chunk options in R Markdown / Quarto documents. (#11663)\
*   RStudio now supports auto-completion following `@` via `.AtNames`. (#13451)\
*   RStudio now supports the execution and display of GraphViz (`dot`) graphs in R Markdown / Quarto chunks. (#13187)\
*   RStudio now supports the execution of chunks with the ‘file’ option set. (#13636)\
*   RStudio now supports `LuaLaTeX` to compile Sweave/Rnw documents. (#13812)\
*   RStudio now supports pasting of file paths for files copied to the clipboard. (#4572)\
*   RStudio now supports duplicate connection names for Posit drivers. (rstudio-pro#5437)\
*   Improved support for development documentation when a package has been loaded via `devtools::load_all()`. (#13526)\
*   Better error message when user preferences fail to save due to folder permissions. (#12974)\
*   With screen reader support enabled, hitting ESC key allows Tabbing away from editor. \[accessibility\] (#13593)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-61)\
\
*   Removed link for opening sessions in RStudio Desktop Pro from Session Info dialog. (rstudio-pro#5263)\
*   Restored database password encryption support removed in 2023.09.1 (rstudio-pro#5365)\
*   Added Licenses guide that includes open source software components and full copies of license agreements used by the components. (#5027)\
*   Added support for launching jobs via Singularity with Slurm (launcher#447)\
*   Added requestTime to nginx access logs when rserver.conf’s server-access-log=1. Format for rserver-http-access.log has changed to add a request time field useful for seeing how long it takes rserver to respond to requests. WARNING: if you have code that processes the log file, expect a new field.\
*   Increased the built-in nginx server’s max connection limit, enabled nginx error logging, and allow both to be configured (rstudio-pro#4652, rstudio-pro#4747, rstudio-pro#5452)\
*   Replaced Administration Guide section PRO markers with Workbench tags. (#5416)\
*   Improved Admin: The Logs tab allows viewing other server log files. A new Server tab provides real-time performance info and on-the-fly adjustment of the rserver log-level (rstudio-pro#5212)\
*   Added Databricks integration to RStudio Pro Sessions which allows users to seamlessly interact with Databricks clusters and resources (rstudio-pro#4927)\
*   Added Databricks integration to Workbench which enables pass-through auth with Databricks, AWS-Databricks, and Azure Databricks for IDE and VS Code (rstudio-pro#4927)\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2023.12.0-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-51)\
\
*   Fixed an issue preventing the object explorer from exploring httr request objects. (#13348)\
*   Fixed an issue where underscores in file names were incorrectly displayed in menu items. (#13662)\
*   Fixed an issue where previewed plots were not rendered at the correct DPI. (#13387)\
*   Fixed an issue where warnings could be emitted when parsing YAML options within R Markdown code chunks. (#13326)\
*   Fixed an issue where inline YAML chunk options were not properly parsed from SQL chunks. (#13240)\
*   Fixed an issue where help text in the autocompletion popup was not selectable. (#13674)\
*   Fixed an issue where a file could be opened twice when debugging functions sourced from other directories. (#13719)\
*   Fixed an issue preventing publishing standalone Quarto content from within larger Quarto projects. (#13637)\
*   Fixed an issue that prevented RStudio from opening PDF vignettes from the Help pane. (#13041)\
*   Inline chunk execution now respects YAML style plot options styled with hyphens. (#11708)\
*   Fixed a bug where project options updated in the Project Options pane were not properly persisted in RStudio 2023.09.0. (#13757)\
*   Fixed viewing or blaming files on GitHub for a newly created branch. (#9798)\
*   Fixed an issue on macOS where ‘-ne’ was erroneously printed to the console with certain versions of Bash. (#13809)\
*   Fixed an issue where attempts to open files containing non-ASCII characters from the Files pane could fail on Windows. (#13855, #12467)\
*   Fixed an issue where the color highlight for Console input could not be disabled. (#13118)\
*   Fixed an issue that could cause the RStudio IDE to crash if a large amount of Console output was serialized with a suspended session. (#13857)\
*   Fixed an issue where Find in Files results were not presented in rare cases. (#12657)\
*   Fixed an issue that could cause errors if an R Markdown document was saved while a chunk was running. (#13860)\
*   Fixed an issue where console output could be dropped when rendering large ANSI links. (#13869)\
*   Fixed an issue preventing users from copying code from the History pane. (#3219)\
*   Fixed WSL terminals not starting on RStudio Desktop for Windows. (#13918)\
*   Fixed an issue that prevented users from opening files and vignettes with non-ASCII characters in their paths. (#13886)\
*   Fixed an issue where large, heavily-nested objects could slow code execution in the R session. (#13965)\
*   Fixed performance problem locating RStudio projects that live under a large directory tree (rstudio-pro#5435)\
*   RStudio will no longer attempt to activate the default system installation of Python automatically. (#13497)\
*   RStudio now records the deployment target for newly published documents, even when deployment fails due to an error in the document. (#12707)\
*   Improved performance of R Markdown chunk execution for projects running on networked filesystems. (#8034)\
*   Improved screen reader support when navigating source files in the editor. \[accessibility\] (#7337)\
*   Session Protocol Debug in Tools -> Command Palette turns on log-level=debug when set (rstudio-pro#5095)\
*   Reduce overhead of session suspension checks and writes to the executing file (#13534, rstudio-pro#4922)\
*   Reset session keyring on Linux platforms to ensure credentials added in a session are isolated (rstudio-pro#5485)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-62)\
\
*   Fixed opening job details in new windows more than once for Workbench jobs on the homepage. (rstudio/rstudio-pro#5179)\
*   Fixed accessibility issues with empty Session and Project lists on the homepage. \[accessibility\] (rstudio/rstudio-pro#5214)\
*   Fixed accessibility issues with Project controls on the homepage when not using launcher sessions. \[accessibility\] (rstudio/rstudio-pro#5215)\
*   Fixed unlabeled input field in Rename Session modal dialog on the homepage. \[accessibility\] (rstudio/rstudio-pro#5178)\
*   Fixed mismatched label on “Join session when ready” check box in New Session dialog. \[accessibility\] (rstudio/rstudio-pro#5221)\
*   Fixed issue that caused start-up crash in environments with encrypted database passwords. (rstudio-pro#5228)\
*   Fixed an issue where Shift+Tab wouldn’t wrap focus in the New Session dialog. \[accessibility\] (rstudio-pro#4488)\
*   Fixed an issue where sessions couldn’t be started with a keyboard with Kubernetes or Slurm. \[accessibility\] (rstudio-pro#4360)\
*   Fixed label on the button for showing and hiding launcher details so it is available to screen reader. \[accessibility\] (rstudio-pro#5268)\
*   Fixed an issue where last sign in for user would be updated even if login fails due to license limits (rstudio-pro#5039)\
*   Fixed bug where vscode and jupyter websockets might be intermittently closed in some circumstances, especially when auth-timeout-minutes=0 (rstudio-pro#5220)\
*   Fixed routing problem with load balancing when not using a standard port (rstudio-pro#5367)\
*   Fixed intermittent problem with load balancing and local launcher sessions for some features like workbench jobs (rstudio-pro#5451)\
*   Fixed issue where the homepage did not display RStudio session’s ‘Executing’ status consistently (rstudio-pro#5141)\
*   Fixed bug in the Posit Workbench VS Code extension that prevented the extension from recognizing all Dash apps (rstudio-workbench-vscode-ext#239)\
*   Improved the accessible label on launcher job details buttons. \[accessibility\] (rstudio-pro#5270)\
*   Reduced the number of DB connections allocated in the pool when servers have many CPUs (rstudio-pro#5210)\
\
2023.09.1[](https://docs.posit.co/ide/news/#rstudio-2023.09.1)\
\
---------------------------------------------------------------\
\
**“Desert Sunflower”** | Date: 2023-10-17\
\
### Deprecated / Removed[](https://docs.posit.co/ide/news/#rstudio-2023.09.1-deprecated)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-63)\
\
*   We have removed support for decrypting or providing encrypted database passwords for the internal PostgreSQL database. Instead, we now strongly recommend a more robust authentication mechanism, such as SSL certificate-based authentication. When a password appears to be encrypted, Workbench will log a warning, and attempt to use it as an unencrypted password. For more information please see the [Posit Workbench admin guide section on PostgreSQL](https://docs.posit.co/ide/server-pro/2023.09.1/database/configuration.html#postgresql)\
    .\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2023.09.1-new)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-52)\
\
*   GitHub Copilot is available as an opt-in integration with RStudio. This feature is currently in public Preview, and has only been tested on RStudio Desktop. Copilot support is expected to be generally available in RStudio Desktop, RStudio Server and Posit Workbench in a future release.\
*   Update to Electron 26.2.4 (#13457)\
*   Upgrade Node to 16.20.2 (rstudio-pro#5275)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-64)\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2023.09.1-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-53)\
\
*   Fixed a bug where project options updated in the Project Options pane were not properly persisted in RStudio 2023.09.0 (#13757)\
*   Fixed issue preventing enabling screen reader mode (#13710)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-65)\
\
*   Exclude unused files from the Workbench VS Code Extension package\
*   Fixed issue that caused start up crash in environments with encrypted database passwords. (rstudio-pro#5228)\
\
2023.09.0[](https://docs.posit.co/ide/news/#rstudio-2023.09.0)\
\
---------------------------------------------------------------\
\
**“Desert Sunflower”** | Date: 2023-09-25 | [Release Blog Post](https://posit.co/blog/rstudio-2023-09-0-whats-new/)\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2023.09.0-new)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-54)\
\
*   Update to Electron 25.5.0 (#13457)\
*   Add support Quarto Manuscript projects, a new Quarto feature that will be released in Quarto 1.4.\
*   Added option to sign Git commits (#1865)\
*   Add section to theme generation that will use theme-specific color(s) to set colors of vim/emacs-mode cursor\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-66)\
\
*   An initial set of Prometheus metrics and grafana dashboard are available for the Workbench server (rstudio/rstudio-pro#3273)\
*   Additional support for publishing new content types to Posit Cloud (rstudio/rstudio-pro#4541)\
*   Update code-server to version 4.14.1 (VS Code version 1.79.2) bundled with node 16.20.2 (rstudio/rstudio-pro#4774, rstudio/rstudio-pro#5012)\
*   Update rserver-saml to 0.7.0 (rstudio/rstudio-pro#4903)\
*   Change the default behavior of the load-balancer configuration setting `launcher-balancing-enabled` to always be true. This has no effect on non load-balanced environments. (rstudio/rstudio-pro#4953)\
*   Auto-generate the `secure-cookie-key` and launcher key pair in load-balanced environments (rstudio/rstudio-pro#4985)\
*   Add the `secure-cookie-key` and launcher key pair to the node table of the database for load-balanced environments. (rstudio/rstudio-pro#4985)\
*   Multiple instances of the Slurm plugin can now point at the same backing cluster without interfering with one another, provided they have different names (rstudio/launcher#706)\
*   The Slurm plugin now has a `default-partition` setting that allows choosing a different partition than the cluster-wide default. The default partition is also put at the top of the list and highlighted in the UI when launching sessions (rstudio/launcher#551, rstudio/launcher#627, rstudio/rstudio-pro#4658)\
*   Resource profiles for the Slurm plugin now support setting the partition (rstudio/launcher#695, rstudio/rstudio-pro#4658)\
*   Resource profiles for the Kubernetes plugin now support setting placement constraints (rstudio/launcher#714, rstudio/rstudio-pro#4767)\
*   When launching sessions or Workbench jobs, available clusters are now shown only when there is more than one option (rstudio/rstudio-pro#4675)\
*   Non-shared projects on the home page no longer show a superfluous “Owner” field (rstudio/rstudio-pro#4984)\
*   Users can now opt to receive desktop notifications when their sessions are ready, which is especially useful on platforms like Slurm or Kubernetes where this may take more than a few seconds (rstudio/rstudio-pro#3432)\
*   While waiting to auto-join a session from the home page, the popup now shows additional status information on Kubernetes and Slurm and no longer warns about sessions that take more than 30 seconds to start (rstudio/rstudio-pro#4813)\
*   Projects that can’t be found by the server are no longer completely hidden on the home page; rather, they are flagged as potentially moved or deleted (rstudio/rstudio-pro#4958)\
*   Workbench now sets the `SPARK_CONNECT_USER_AGENT` environment variable for all sessions. This can help users of hosted Apache Spark clusters (including Databricks) identify when Workbench users are accessing Spark (rstudio/rstudio-pro#5015)\
*   Security audit and file size optimization for VS Code Workbench extension (rstudio/rstudio-workbench-vscode-ext#227)\
*   Added `delete-node-on-exit` option for load balancing to cleanup node table and fixed error caused by stale nodes (rstudio/rstudio-pro#4888)\
*   Added explicit load-balancing-enabled option to rserver.conf (rstudio/rstudio-pro#4836)\
*   Sticky sessions are no longer required to use OpenID Connect authentication (rstudio/rstudio-pro#2451)\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2023.09.0-fixed)\
\
#### RStudio[](https://docs.posit.co/ide/news/#rstudio-55)\
\
*   Fixed issue where `DYLD_FALLBACK_LIBRARY_PATH` was not properly forwarded on macOS (#13085)\
*   Fixed issue where ‘ggrepel’ plot annotations could disappear when a plot was redrawn in an R Markdown document (#4330)\
*   Fixed issue where whitespace in error messages was not properly preserved (#13239)\
*   Fixed issue where the Data Viewer could fail to render data.frames containing AsIs matrices (#13215)\
*   Fixed issue where error messages were not properly translated on Windows in some cases (#10308)\
*   Fixed issue where Electron menubar commands are not disabled when modals are displayed (#12972)\
*   Fixed bug causing invalid/empty `cacheKey` error when accessing a dataframe variable (#13188)\
*   Fixed bug preventing dataframe column navigation past the default number of display columns (#13220)\
*   Fixed bug preventing files from being saved when user `HOME` path includes trailing slashes on Windows (#13105)\
*   Fixed broken Help pane after navigating to code demo (#13263)\
*   Fixed bug preventing Update Available from displaying (#13347)\
*   Fixed bug causing dataframe help preview to fail for nested objects (#13291)\
*   Fixed issue where changes to binary files were not presented in Git History view (#13126)\
*   Fixed bug where clicking “Ignore Update” would fail to ignore the update (#13379)\
*   Fixed issue with alignment of R argument names in Help pane (#13474)\
*   Fixed issue where user was not warned of missing Rosetta installation on Apple silicon (#12791)\
*   Fixed bug with modals disabling copy/paste (#13365)\
*   Fixed issue with file opened twice when navigating `cli` package hyperlinks (#13134)\
*   Fixed issue where column names weren’t provided as completion candidates for DBI tables. (#12577)\
*   Fixed an issue where parameter name completions were not provided within `dplyr` joins. (#13415)\
*   Fixed issue where R sessions containing large ‘igraph’ objects could become slow (#13489)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-67)\
\
*   Fixed intermittent rsession crash when the linux nscd service was enabled (rstudio/rstudio-pro#4648)\
*   Fixed bug when resuming session not restoring current working directory for Terminal pane (rstudio/rstudio-pro#4027)\
*   Fixed bug preventing `HOME` from being modified in system init scripts (rstudio/rstudio-pro#4584)\
*   Removed unnecessary files from install packages (rstudio/rstudio-pro#4943)\
*   Updated Launcher go dependencies to latest versions (rstudio/rstudio-pro#5021)\
*   Workbench will no longer log a spurious error about ownership when the `r-versions` file is on an NFS mount with `root_squash` set (rstudio/rstudio-pro#4721)\
*   The `launcher-sessions-clusters`, `launcher-adhoc-clusters`, and `launcher-default-cluster` settings now apply to all IDEs. Individual settings for Jupyter and VS Code sessions are now marked as deprecated (rstudio/rstudio-pro#4651)\
*   Recent projects listed on the home page should no longer have an empty “Last Used” field (rstudio/rstudio-pro#4157)\
*   The Slurm plugin no longer warns that some legitimately-supported Slurm versions are not supported (rstudio/launcher#644)\
*   AWS roles can now be chosen when resuming a session as well as launching a new one (rstudio/rstudio-pro#5043)\
*   Fixed `rstudio-server active-sessions` command and added `node-status` (rstudio/rstudio-pro#4074)\
*   Fixed load balancing to count all types of sessions (rstudio/rstudio-pro#3016)\
*   Fixed bug preventing user’s last sign in date from updating on CentOS 7 and PostgreSQL (rstudio/rstudio-pro#5072)\
*   Limit logs collected in rstudio-diagnostics to reduce size\
\
### Performance[](https://docs.posit.co/ide/news/#performance)\
\
*   Improved performance of group membership tests (rstudio/rstudio-pro#4643)\
*   Increased read buffer size for rserver proxy (rstudio/rstudio-pro#4764)\
*   Various improvements to the responsiveness of the Workbench home page (rstudio/rstudio-pro#4736, rstudio/rstudio-pro#4750, rstudio/rstudio-pro#4762, rstudio/rstudio-pro#4085)\
*   Fixed rserver CPU bottleneck when session generates lots of output but never starts (rstudio/rstudio-pro#4865)\
*   Avoid username lookups when listing processes looking for sessions (rstudio/rstudio-pro#4800)\
*   Avoid load balancing node-status checks for Slurm and Kubernetes sessions (rstudio/rstudio-pro#4876)\
\
2023.06.2[](https://docs.posit.co/ide/news/#rstudio-2023.06.2)\
\
---------------------------------------------------------------\
\
**“Mountain Hydrangea”** | Date: 2023-08-24\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2023.06.2-fixed)\
\
#### RStudio IDE[](https://docs.posit.co/ide/news/#rstudio-ide)\
\
*   Fixed an issue causing data to be sorted incorrectly in the data viewer within paginated columns (#13328)\
*   Fixed bug preventing files from being saved when user `HOME` path includes trailing slashes on Windows (#13105)\
*   Fixed issue where Electron menubar commands are not disabled when modals are displayed (#12972)\
*   Fixed bug preventing Update Available from displaying (#13347)\
*   Fixed bug causing dataframe help preview to fail for nested objects (#13291)\
*   Fixed bug where clicking “Ignore Update” would fail to ignore the update (#13379)\
*   Fixed bug preventing `HOME` from being modified in system init scripts (rstudio-pro:#4584)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-68)\
\
*   Caching of passwd lookups for a few more api calls including the process info api used by load balancing (rstudio/rstudio-pro#4800)\
*   Avoid intermittent hanging `rserver` process when using 3rd party active directory (rstudio/rstudio-pro#4614)\
*   Fixed rserver CPU utilization bug when starting a session that emits lots of output without the expected “listening on port” pattern (rstudio/rstudio-pro#4865)\
*   Fixed bug when resuming session not restoring current working directory for Terminal pane (rstudio/rstudio-pro#4027)\
*   More efficient version of is user in groups feature and improved error handling for when get group fails (rstudio/rstudio-pro#4643)\
*   Fixed issue with Slurm and load balancing that could delay session starts or occasionally fail to start (rstudio/rstudio-pro#4971)\
*   Updated jupyterlab buildutils package to fix vulnerability (rstudio/rstudio-pro#4951)\
*   Updated the SAML helper program to fix problem found in vulnerability scan (rstudio/rstudio-pro#4903)\
*   Add support for newer Slurm v23 (rstudio/rstudio-pro#4766)\
\
### Deprecated / Removed[](https://docs.posit.co/ide/news/#rstudio-2023.06.2-deprecated)\
\
#### RStudio IDE[](https://docs.posit.co/ide/news/#rstudio-ide-1)\
\
*   Remote desktop sessions are no longer supported (rstudio-pro:#4832)\
\
2023.06.1[](https://docs.posit.co/ide/news/#rstudio-2023.06.1)\
\
---------------------------------------------------------------\
\
**“Mountain Hydrangea”** | Date: 2023-07-07\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2023.06.1-new)\
\
#### RStudio IDE[](https://docs.posit.co/ide/news/#rstudio-ide-2)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-69)\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2023.06.1-fixed)\
\
#### RStudio IDE[](https://docs.posit.co/ide/news/#rstudio-ide-3)\
\
*   Fixed bug causing invalid/empty `cacheKey` error when accessing a dataframe variable (#13188)\
*   Fixed bug preventing dataframe column navigation past the default number of display columns (#13220)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-70)\
\
2023.06.0[](https://docs.posit.co/ide/news/#rstudio-2023.06.0)\
\
---------------------------------------------------------------\
\
**“Mountain Hydrangea”** | Date: 2023-06-08\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2023.06.0-new)\
\
#### RStudio IDE[](https://docs.posit.co/ide/news/#rstudio-ide-4)\
\
*   Updated to Electron 23.3.0 (#13030)\
*   Moved Help panel font size setting to Appearance tab in Global Options (#12816)\
*   Updated openssl to 1.1.1t for Windows (rstudio/rstudio-pro#3675)\
*   Improved visibility of focus rectangles on Server / Workbench Sign In page \[Accessibility\] (#12846)\
*   Added ability to enable minidump generation for Electron crashes (#13025)\
*   Added Quarto for Linux arm64 (#12411)\
*   Updated zlib to 1.2.13 (rstudio/rstudio-pro#4531)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-71)\
\
*   Added the `session-connections-block-suspend` session option, controlling whether active connections can block the suspension of an R session\
*   Added the `session-external-pointers-block-suspend` session option, controlling whether R objects containing external pointers can block the suspension of an R session\
*   Added http server request processing statistics for the rserver, logged as info/debug messages, controlled by the option `www-stats-monitor-seconds` in rserver.conf (rstudio/rstudio-pro#4554)\
*   Updated code server to 4.12.0 to address security vulnerabilities\
*   Updated nginx to supported version 1.24.0 (rstudio/rstudio-pro#4532)\
*   Updated PCRE to PCRE2, version 10.42 (rstudio/rstudio-pro#4530)\
*   Added a new `session-port-range` option in `rsession.conf` that allows limiting the port range available to RStudio Pro sessions (rstudio/rstudio-pro#945)\
*   Added support for accessing delegated credentials through Azure Active Directory in RStudio Pro sessions (rstudio/rstudio-pro#4485)\
*   Support for setting per-user AWS credentials in RStudio Pro sessions is now generally available (rstudio/rstudio-pro#4246)\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2023.06.0-fixed)\
\
#### RStudio IDE[](https://docs.posit.co/ide/news/#rstudio-ide-5)\
\
*   Fixed display problems with Choose R dialog when UI language is French (#12717)\
*   Fixed focus switching to Help Pane search box after executing ? in the console \[Accessibility\] (#12741)\
*   Fixed initial focus placement in Help Pane \[Accessibility\] (#10600)\
*   Fixed invalid element role on session-suspended icon \[Accessibility\] (#12449)\
*   Improved screen-reader support for Console pane toolbar \[Accessibility\] (#12825)\
*   Background script jobs are now run using the global environment, which fixes the behavior of `source()` in backgrounds jobs (#11866)\
*   Fixed bug that caused Update Available dialog to show after the user selected to Ignore Update (rstudio/rstudio-pro#4179)\
*   Fixed bug that prevented updating to the latest release if version was previously ignored (#12874)\
*   RStudio no longer uses `reg.exe` when attempting to enumerate R versions in the Windows registry (#12599)\
*   Fixed file-type icons not displaying in Finder on Mac (#12252)\
*   Fixed saving and restoring window location when maximized or partially offscreen (#12463)\
*   Fixed display of macOS message dialogs (#12928)\
*   Set theme of menu bar, title bar, and dialogs (dark vs. light) based on RStudio theme (#12247)\
*   Fixed issues with mouse back / forward navigation in Source pane and Help pane (#12932)\
*   Fixed opening files from command-line with relative paths (#12495, #12563)\
*   Fixed issue with column preview with older versions of the ‘pillar’ package. (#12863)\
*   Fixed bug where the OK button was disabled in Choose R dialog when only one version of R installed (#12916)\
*   Improved robustness when chosing custom R version in Windows desktop (#12969)\
*   Fixed bug that prevented RStudio Desktop from starting on Linux if desktop.ini was unreadable (#12963)\
*   Improved RStudio Desktop startup behavior when the user state folder is inaccessible (#12988)\
*   Fixed saving files to UNC paths on Windows (#12652, #12935)\
*   Fixed window disappearing when restoring from maximized on macOS (#13010)\
*   Fixed Project Build Tools preferences pane showing &mdash text in French UI (#11134)\
*   Fixed inserting cross references in a Quarto document showing no references (#12882)\
*   Fixed keyboard shortcut help not displaying in Emacs or Sublime Text mode (#11376)\
*   Fixed issue with rendering development documentation with R 4.3.0 (#12945)\
*   Fixed issue with use of “Whole word” with Find in Files search (#13017)\
*   Fixed issue with diagnostics freezing session with documents containing pipebind operator (#13091)\
*   Fixed issue with stopping a Quarto Shiny doc render on Windows (#12546)\
*   Fixed issue causing sessions to fail to start if repos contained `NA` value (#12946)\
*   Fixed “Error Retrieving Help” bug when data preview column contains `NA` values (#12918)\
*   Fixed hang when restarting R or closing IDE after rendering a Quarto document (#12836)\
*   Fixed an issue where large R objects could adversely affect the performance of the IDE (#13103)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-72)\
\
*   Fixed unlabeled buttons for screen reader users when page is narrow \[Accessibility\] (rstudio/rstudio-pro#4340)\
*   Removed redundant mouse-only New Session widget from accessibility tree \[Accessibility\] (rstudio/rstudio-pro#4338)\
*   Fixed launcher error details not showing on the homepage when clicking “Error Details” (rstudio/rstudio-pro#4333)\
*   Fixed theme button’s semantics so it is meaningful to screen reader \[Accessibility\] (rstudio/rstudio-pro#4337)\
*   Fixed screen reader accessibility for the homepage theme dropdown menu \[Accessibility\] (rstudio/rstudio-pro#4339)\
*   Fixed hidden controls on Session Info dialog remaining active \[Accessibility\] (rstudio/rstudio-pro#4341)\
*   Added keyboard support to the “Show list” control in New Session dialog \[Accessibility\] (rstudio/rstudio-pro#4461)\
*   Fixed job details to be hidden from screen reader when visibly hidden \[Accessibility\] (rstudio/rstudio-pro#4466)\
*   Fixed sign-in pages to be more mobile and zoom friendly \[Accessibility\] (rstudio/rstudio-pro#4472)\
*   Cache results for user and group lookups (rstudio/rstudio-pro#4451)\
*   Increased timeout for stale messages error (rstudio/rstudio-pro#4325)\
*   Reduced database queries and remove locking around DB calls (rstudio/rstudio-pro#4492)\
*   Eliminated assertion failed error when reloading config with load balancing enabled (rstudio/rstudio-pro#4504)\
*   Fixed verify-installation failure when jupyter sessions were enabled but jupyter was not installed (rstudio/rstudio-pro#4390)\
*   AWS credentials now work correctly on Kubernetes, Slurm, and when PAM sessions are disabled (rstudio/rstudio-pro#4484, rstudio/rstudio-pro#4686)\
*   Add option to allow launcher sessions to return a non-zero exit code (rstudio/rstudio-pro#4719)\
*   Errors related to `/var/run/rserver-http.pid` when running in single-user (unprivileged) mode are now resolved (rstudio/rstudio-pro#4578, rstudio/rstudio-pro#4597)\
*   A blank `rstudio-prefs.json` file no longer causes `Failed to parse settings` errors (rstudio/rstudio-pro#4347)\
*   Kubernetes Service Accounts that contain only numeric characters will now work correctly with templates (rstudio/launcher#650)\
*   Resource profiles now work correctly when the Slurm plugin is configured with `enable-gpus=1` but `gpu-types` is empty (rstudio/launcher#639)\
*   Routine timeouts when watching Kubernetes resources are no longer logged as an error (rstudio/launcher#604)\
*   The Kubernetes plugin should now reload authorization tokens more reliably (rstudio/launcher#685)\
*   Fixed a memory leak and various crashes in the Kubernetes plugin (rstudio/launcher#584, rstudio/launcher#645, rstudio/launcher#660)\
*   The Kubernetes plugin now interprets the default number of AMD GPUs correctly (rstudio/launcher#688)\
*   Fixed the logic when manipulating ACLs for project sharing to not remove permissions on parent directories (rstudio/rstudio-pro#4258)\
\
2023.03.2[](https://docs.posit.co/ide/news/#rstudio-2023.03.2)\
\
---------------------------------------------------------------\
\
**“Cherry Blossom”** | Date: 2023-06-12\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2023.03.2-fixed)\
\
#### RStudio IDE[](https://docs.posit.co/ide/news/#rstudio-ide-6)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-73)\
\
*   Added option to allow launcher sessions to return a non-zero exit code (rstudio/rstudio-pro#4719)\
\
2023.03.1[](https://docs.posit.co/ide/news/#rstudio-2023.03.1)\
\
---------------------------------------------------------------\
\
**“Cherry Blossom”** | Date: 2023-05-12\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2023.03.1-new)\
\
#### RStudio IDE[](https://docs.posit.co/ide/news/#rstudio-ide-7)\
\
*   Upgrade Quarto to 1.2.475 (#12887)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-74)\
\
*   Cache results for user and group lookups (rstudio/rstudio-pro#4451)\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2023.03.1-fixed)\
\
#### RStudio IDE[](https://docs.posit.co/ide/news/#rstudio-ide-8)\
\
*   Fix no cross references when inserting (#12882)\
*   Fix Windows Choose R dialog error after selecting an R installation (#12984)\
*   Fix saving files to UNC paths on Windows (#12652)\
*   Fix RStudio freeze when copy/pasting on Windows (#12879)\
*   Fix inserting an empty citation (#12833)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-75)\
\
*   Increase timeout for stale messages error (rstudio/rstudio-pro#4325)\
*   Reduce database queries and remove locking around DB calls (rstudio/rstudio-pro#4492)\
*   Eliminate assertion failed error when reloading config with load balancing enabled (rstudio/rstudio-pro#4504)\
*   Fix a bug with starting JupyterLab and Jupyter Notebook sessions when ServerApp.token=’’ is present in the Jupyter settings (rstudio/rstudio-pro#4491)\
*   Routine timeouts when watching Job Launcher Kubernetes resources are no longer logged as an error (rstudio/launcher#604)\
*   Resolve an issue in the Job Launcher Kubernetes plugin with handling Kubernetes token rotation that would result in the Kubernetes plugin restarting (rstudio/launcher#584)\
*   Address a memory leak in the Job Launcher Kubernetes plugin related to the reloading of the Kubernetes API token (rstudio/launcher#645)\
*   Kubernetes Service Accounts that contain only numeric characters will now work correctly with templates (rstudio/launcher#650)\
*   Resource Profiles now work correctly when the Job Launcher Slurm plugin is configured with `enable-gpus=1` but `gpu-types` is empty (rstudio/launcher#639)\
*   Address a crash in the Job Launcher Kubernetes Plugin (rstudio/launcher#660)\
*   Fix a bug in Job Launcher Kubernetes Plugin Kubernetes Auth Token reload logic for streaming requests (rstudio/launcher#685)\
\
2023.03.0[](https://docs.posit.co/ide/news/#rstudio-2023.03.0)\
\
---------------------------------------------------------------\
\
**“Cherry Blossom”** | Date: 2023-03-16 | [Release Blog Post](https://posit.co/blog/rstudio-2023-03-0-whats-new/)\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2023.03.0-new)\
\
#### RStudio IDE[](https://docs.posit.co/ide/news/#rstudio-ide-9)\
\
*   Adopt panmirror (visual editor) migration to quarto-dev/quarto project (#12316)\
*   Upgrade Electron to 22.0.0 (#11734)\
*   Upgrade Quarto to 1.2.335 (#12697)\
*   roxygen2 completions show description and complete as a snippet (#11957)\
*   data frame and data frame columns completions show more information (#12308)\
*   Support more “complex” start of pipe chains in completions (#9612), #10538\
*   Revisit the order of completions, i.e., columns before search path secondary completions (#12292)\
*   Improved `[` and data.table related completions (#12289), 11202\
*   Support column completions for arrow objects (#11629)\
*   Support searching for roxygen specific information in fuzzy finder (Go to File/Function) (#12190)\
*   “Rainbow” fenced divs, controlled by Options > R Markdown > \[v\] Use rainbow fenced divs (#12115)\
*   Disable argument tooltips in the script editor for unknown functions (#12160)\
*   Add RTools 4.3 support (#12528)\
*   Add support for R 4.3 (#12751)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-76)\
\
*   Session components no longer link to libpq or its dependencies (rstudio/rstudio-pro#2138)\
*   Sessions now have lower CPU priority during suspension on macOS and Linux (#12623)\
*   Sessions run on Kubernetes or Slurm will no longer exit with nonzero codes under normal circumstances (rstudio/rstudio-pro#3375)\
*   Updated code-server to version 4.9.1 (VS Code version 1.73.1) (rstudio/rstudio-pro#4150)\
*   Preview support for setting per-user AWS credentials in RStudio Pro sessions (rstudio/rstudio-pro#4246)\
*   Sessions run on Kubernetes or Slurm can now greatly simplify the task of assigning CPU, memory, or GPU resources by using named Resource Profiles (rstudio/rstudio-pro#4249)\
*   Kubernetes Job and Service resources created by Workbench now set the `app.kubernetes.io/managed-by` label to `launcher` (rstudio/launcher#379)\
*   When the Job Launcher is enabled, the Local plugin can now be configured to use “external” load balancing, which removes the need for the `scratch-path` to be on shared storage (rstudio/launcher#42, rstudio/rstudio-pro#3770)\
*   A new `allowed-partitions` setting in the `launcher.slurm.profiles.conf` file can be used to limit visibility of Slurm partitions to specific users or groups (rstudio/launcher#309)\
*   All Job Launcher plugins now support fractional values for the `job-expiry-hours` setting (i.e., `0.5` for 30 minutes) (rstudio/launcher#372)\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2023.03.0-fixed)\
\
#### RStudio IDE[](https://docs.posit.co/ide/news/#rstudio-ide-10)\
\
*   Fixed an issue where Git / SVN actions requiring user input could fail in some situations. (#12390)\
*   Fixed an issue where the plots displayed in the inline preview were incorrectly scaled on devices with high DPI (#4521, #2098, #10825, #7028, #4913).\
*   Fixed background jobs not showing the entire output (#12389)\
*   Fixed mixed-case CSS colors (#12562)\
*   Fixed indentation of colored text (#12489)\
*   Fixed (and speedup) identification of the presence of external pointers (#12328)\
*   Fixed rendering of custom source markers (#12425)\
*   Fixed handling of backticks in data frame columns in auto-completion (#8675)\
*   Fixed group\_by() specific completions (#12356)\
*   Fixed auto-completions when named arguments already in use (#12326)\
*   Fixed column name completions when package name is specified (#9786)\
*   Fixed Excel import preview (#3955)\
*   Fixed indentation of raw strings (#12127)\
*   Removed empty spell check tooltips (#11306)\
*   Fixed package completion tooltips (#12147)\
*   Fixed setting rsession log level using command-line argument or logging.conf (#12557)\
*   Fixed issue that allowed users to overwrite their home directory in server mode (#12653)\
*   Fixed “Check for updates” incorrectly reports that there are no updates (rstudio/rstudio-pro#3388)\
*   Fixed default options for Choose R dialog on Windows (#12452)\
*   Fixed data viewer’s “Show in new window” results in an empty window (#12468)\
*   Fixed uncaught Shiny error breaks RStudio’s “Run in Window” feature (#12569)\
*   Fixed previewing rendered html\_document causes URLs to open in a browser (#12494)\
*   Fixed link opens in a browser after Render with .qml file when hypothes.is comments are turned on in `_quarto.yml` (#12413)\
*   Fixed Copy Plot to Clipboard - pasting bitfile option not working correctly in the latest build (#12466)\
*   Fixed Find in Files with git projects and older version of git (#11822)\
\
#### Posit Workbench[](https://docs.posit.co/ide/news/#posit-workbench-77)\
\
*   Fixed intermittent hanging logins in Workbench using ActiveDirectory (rstudio/rstudio-pro#4285)\
*   Fixed incorrect icons displayed in the sessions drop-down menu in RStudio Pro (rstudio/rstudio-pro#4257)\
*   Editor Selection widget in New Session dialog is now usable via keyboard \[Accessibility\] (rstudio/rstudio-pro#4205)\
*   Editor Selection widget in New Session dialog supports screen reader usage \[Accessibility\] (rstudio/rstudio-pro#4206)\
*   Editor icons in New Session dialog are marked as cosmetic for screen readers \[Accessibility\] (rstudio/rstudio-pro#4207)\
*   Homepage modal dialogs are now implemented correctly for keyboard and screen reader use \[Accessibility\] (rstudio/rstudio-pro#4208)\
*   Posit logo on the home page marked as cosmetic for screen readers \[Accessibility\] (rstudio/rstudio-pro#4209)\
*   Focus and keyboard-focus styles have been improved on the homepage \[Accessibility\]\
*   Keyboard support has been added to the job summary drop-down in session list items on the homepage \[Accessibility\]\
*   Improved alt-text and updated link to posit.co on sign-in page logo \[Accessibility\] (rstudio/rstudio-pro#4096)\
*   Help pane home page switches to single-column display at narrow widths \[Accessibility\] (#12643)\
*   RStudio Pro sessions drop-down panel icons marked with role=“presentation” \[Accessibility\] (rstudio/rstudio-pro#4257)\
*   Workbench will no longer write an unrelated `rserver-http.pid` file to the `server-data-dir` directory (rstudio/rstudio-pro#4279)\
*   Fixed the frequent `No such file or directory` errors logged by `rserver-monitor` when on a system with cgroups v2 (#10914, rstudio/rstudio-pro#2683)\
*   Support Kubernetes v1.24 (rstudio/rstudio-pro#4064)\
*   Security fix: User ID is now set by the server when running Workbench Jobs created by VS Code (rstudio/rstudio-pro#4255)\
*   Fixed connection issues with SSL-enabled sessions running on Slurm in a load-balanced cluster or after a Launcher restart (rstudio/rstudio-pro#4098)\
\
2022.12.0+353[](https://docs.posit.co/ide/news/#rstudio-2022.12.0353)\
\
----------------------------------------------------------------------\
\
**“Elsbeth Geranium”** | Date: 2022-12-15 | [Release Blog Post](https://posit.co/blog/rstudio-2022-12-0-update-whats-new/)\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2022.12.0353-new)\
\
*   RStudio now displays a splash screen on startup, while the R session is being initialized. (#11604)\
*   Updated RStudio Desktop installer on Windows to detect running RStudio by process name. (#10588)\
\
R\
\
*   Whether pending console input is discarded on error can now be controlled via a preference in the Console pane. (#10391)\
*   Improved handling of diagnostics within pipeline expressions. (#11780)\
*   Improved handling of diagnostics within glue() expressions.\
*   Completions within R Markdown documents now respect the `knitr` `root.dir` chunk option if set. (#12047)\
*   RStudio now provides autocompletion results for packages used but not loaded within a project.\
*   Improved handling of missing arguments for some functions in the diagnostics system.\
*   Code editor can show previews of color in strings (R named colors e.g. “tomato3” or of the forms “#rgb”, “#rrggbb”, “#rrggbbaa”) when `Options > Code > Display > [ ] enable preview of named and hexadecimal colors` is checked.\
*   Fixes the bug introduced with `rlang` >= 1.03 where Rmd documents show the error message `object 'partition_yaml_front_matter' not found` upon project startup. (#11552)\
*   Name autocompletion following a `$` now correctly quotes names that start with underscore followed by alphanumeric characters. (#11689)\
*   Suspended sessions will now default to using the project directory, rather than the user home directory, if the prior working directory is no longer accessible. (#11960)\
*   The fuzzy finder indexes C(++) macros. (#11981)\
*   Improved handling for large amounts of `message()` output in the Console pane. (#12059)\
*   Build output is now truncating when very large amounts of output are produced (e.g. from C++ compilation warnings).\
*   Memory usage in the environment pane now works correctly on Linux when using cgroups v2. (#11894)\
*   Fixed an issue where code execution could pause in RStudio Server after closing the browser tab even with active computations. (Pro #3943)\
*   Chunk output calls `format()` method on vctrs-based classes stored in a dataframe. (#6878)\
\
Python\
\
*   RStudio attempts to infer the appropriate version of Python when “Automatically activate project-local Python environments” is checked and the user has not requested a specific version of Python. This Python will be stored in the environment variable “RETICULATE\_PYTHON\_FALLBACK”, available from the R console, the Python REPL, and the RStudio Terminal (#9990)\
*   Shiny for Python apps now display a “Run App” button on the Source editor toolbar. (Requires `shiny` Python package v0.2.7 or later.)\
\
Quarto\
\
*   Support for v2 format of Quarto crossref index\
*   Support for RHEL7 and CentOS7 and fixes missing Pandoc for RMarkdown (rstudio-pro#3804)\
\
Posit Workbench\
\
*   Rebranded Workbench from RStudio Workbench to Posit Workbench to match Posit Software, PBC’s new branding terminology and iconography\
*   Adds `-l` (long) option to `rserver-url`. When `/usr/lib/rstudio-server/bin/rserver-url -l <port number>` is executed within a VS Code or Jupyter session, the full URL where a user can view a server proxied at that port is displayed (rstudio-pro#3620)\
*   Support `launcher-local-proxy` load balancing option to ensure that session requests are always proxied from the local workbench server in a cluster. Eliminates the need to open a range of ports in the firewall for sessions to be reached by other workbench servers (rstudio/rstudio-pro#3670)\
*   Redesigned the session launch dialog from the homepage to show all session types at once (rstudio-pro#3646)\
*   Enabled the Job Launcher with the Local Launcher by default in clean installations of Workbench (rstudio-pro#3571)\
*   Enabled all session types (Jupyter Lab, Jupyter Notebook, RStudio Pro, and VS Code) by default in clean installations of Workbench and added warnings to the Session Launch dialog and the Posit Workbench log when the components for a session type is not installed (rstudio-pro#3689)\
*   Add support for disabling RStudio Pro sessions (rstudio-pro#3642)\
\
Posit Workbench VS Code Sessions\
\
*   Install VS Code session support (code-server) with Posit Workbench instead of requiring a separate download (rstudio-pro#3643)\
*   Updated code-server to version 4.7.1 (VS Code version 1.71.2) (rstudio-pro#3643)\
*   Sets the `UVICORN_ROOT_PATH` environment variable to the proxied port URL for port 8000 in VS Code and Jupyter sessions, allowing FastAPI applications to run without additional configuration. (rstudio-pro#2660)\
*   Workbench now checks for the `code-server` binary in the `WORKBENCH_VSCODE_PATH` environment variable (if present) then the `vscode-exe` setting in `vscode.conf`, or falls back to the preinstalled version and finally the `PATH`. This allows more flexibility when launching sessions on Kubernetes or Slurm clusters. (rstudio/rstudio-pro#3942)\
*   Add support for launching Workbench Jobs through VS Code Sessions (rstudio-pro#3565)\
\
Posit Workbench VS Code Extension\
\
*   Install VS Code Extension with Posit Workbench instead of requiring a separate download (rstudio-pro#3643)\
*   Introduce Workbench Job management to VS Code Extension (rstudio/rstudio-pro#3784, rstudio/rstudio-pro#3565)\
*   Added a pop-up notification when working with certain relevant filetypes that makes it easier to find the Workbench Extension. This notification is a one-time view per user. It can be re-enabled in the user settings (vscode-ext#96).\
*   Rebranded the interface to match Posit Software, PBC’s new branding terminology and iconography\
*   Fixed extension servers appearing in Proxied Servers list (vscode-ext#116)\
*   Added support for Flask, including a help dialog and the Posit Workbench Flask Interface code snippet, for proxying Flask applications (rstudio-pro#2660)\
*   Added a FastAPI help dialog and the following code snippets for setting the root\_path in FastAPI applications (rstudio/rstudio-pro#3698):\
    *   Posit Workbench Uvicorn Root Path Snippet\
    *   Posit Workbench FastAPI Uvicorn Root Path Snippet\
*   Added a Warning notification that appears when a uvicorn process was started with a custom port, without the root-path argument. These processes will now appear in the Proxied Servers view with a warning icon (rstudio/rstudio-pro#3699)\
*   Fixed mislabelling of Shiny app in Proxied Servers list (#117)\
\
Posit Workbench Jupyter Sessions\
\
*   Workbench now checks for the `jupyter` binary in the `WORKBENCH_JUPYTER_PATH` environment variable (if present), then the `jupyter-exe` setting in `jupyter.conf`, and finally the `PATH`. This is allows more flexibility when launching sessions on Kubernetes or Slurm clusters. (rstudio/rstudio-pro#3942)\
*   Fixed an issue where Workbench would not install the `jupyter` extension automatically if the configured `jupyter` path was a symlink to the actual install location. We now follow the symlink. (rstudio/rstudio-pro#3942)\
*   Disabled `session-cull-timeout` in `jupyter.conf` by default for clean installations of Workbench to prevent possible data loss due to Jupyter storing all state in the browser (rstudio-pro#4010)\
\
Posit Workbench Jupyter Extension\
\
*   The Jupyter Notebook and JupyterLab extensions have been updated to match with the new Posit Software, PBC branding (rstudio-pro#3645)\
\
Experimental ARM64 and RedHat 9 support\
\
*   Experimental (preview) support for Linux `aarch64` platforms, such as the Raspberry Pi and AWS Graviton\
*   Experimental (preview) support for RedHat Enterprise Linux 9 and compatible platforms, such as Rocky Linux 9\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2022.12.0353-fixed)\
\
*   Fixed an issue where the console history scroll position was not preserved when switching focus to a separate application (#1638)\
*   Fixed an issue where Find in Files could omit matches in some cases on Windows (#11736)\
*   Fixed an issue where the Git History window inverted the display of merge diffs (#10150)\
*   Fixed an issue where Find in Files could fail to find results with certain versions of git (#11822)\
*   Fixed visual mode outline missing nested R code chunks (#11410)\
*   Fixed an issue where chunks containing multibyte characters was not executed correctly (#10632)\
*   Fixed bringing main window under active secondary window when executing background command (#11407)\
*   Fix for schema version comparison that breaks db in downgrade -> upgrade scenarios (rstudio-pro#3572)\
*   Fixed an issue in the Electron build of the IDE on Macs where users could not clone a git repository via password-protected SSH or HTTPS (#11693)\
*   Fixed scroll speed sensitivity for Mac and Linux and added a preference to adjust it (#11578)\
*   Fixed an issue in server environments where invoking `systemd` directly could lead to orphaned processes and undefined behavior. Processes are now cleaned up more consistently as a part of server or launcher shutdown. (rstudio/rstudio-pro#2585)\
*   RStudio sessions now shut down and suspend properly when they receive a `SIGTERM` signal, as they have for `SIGUSR2` (rstudio/rstudio-pro#2585)\
*   Fixed an issue where `ssl-hsts-include-subdomains=1` would render Workbench non-functional. The setting now works as expected. (rstudio/rstudio-pro#3010)\
*   Fixed an issue where the `suspend-session`, `suspend-all`, and `kill-all` subcommands of `rstudio-server` did not work when using the Launcher. (rstudio/rstudio-pro#4007)\
*   Fixed conflicting keyboard shortcut for toggling screen reader support on macOS (#12339)\
*   Fixed issue with session-ssl that prevented resuming some sessions in a load-balanced environment (rstudio/rstudio-pro#3759)\
*   Fixed intermittent problem where sessions in the Posit Workbench homepage would display incorrect status over NFS (rstudio/rstudio-pro#3979)\
*   Fixed an issue where Workbench Job output would somtimes fail to show (rstudio-pro#3972)\
*   Fixed an issue where reactivating a user could result in an erroneous warning that user license limit had been reached (rstudio-pro#3874)\
\
### Deprecated / Removed[](https://docs.posit.co/ide/news/#rstudio-2022.12.0353-deprecated)\
\
*   Removed the Tools / Shell command (#11253)\
*   Deprecated the vscode.conf “min-ext-version” option for specifying the minimum version of the Posit Workbench VS Code extension as the extension is now bundled with Workbench and Session packages rather than being downloaded (rstudio-pro#3643)\
*   Removed the “rstudio-server install-vs-code” admin command for downloading and configuring code-server; code-server is now installed with Workbench, use the “rstudio-server configure-vs-code” command for configuration (rstudio-pro#3643)\
*   It is highly recommended that you disable session culling in Jupyter sessions by done by setting `session-cull-minutes=0` in `jupyter.conf` to prevent potential data loss (rstudio-pro#3054)\
\
2022.07.2+576.pro12[](https://docs.posit.co/ide/news/#rstudio-2022.07.2576.pro12)\
\
----------------------------------------------------------------------------------\
\
**“Spotted Wakerobin”** | Date: 2022-09-19\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2022.07.2576.pro12-new)\
\
Quarto\
\
*   Support for v2 format of Quarto crossref index\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2022.07.2576.pro12-fixed)\
\
*   Fix for schema version comparison that breaks db in downgrade -> upgrade scenarios (rstudio-pro#3572)\
*   Fix for Quarto crossref indexing/completion not working with Quarto v1.0\
*   Fixed homepage session status problems (rstudio-pro#3644, #3671, and #3669)\
*   Fixed regression in spotted-wakerobin that prevented sessions from starting when launcher-sessions-use-password=1 (rstudio-pro#3664)\
*   Fixes the bug introduced with `rlang` >= 1.03 where Rmd documents show the error message `object 'partition_yaml_front_matter' not found` upon project startup (#11552)\
*   Fixed regression in spotted-wakerobin that prevents R sessions from starting when the crashhandler reports an error (#11717)\
*   Fixed problems with load balancing when database connections are timed out, and fail to restore (pro #3714)\
*   Fixed an issue where chunks containing multibyte characters was not executed correctly (#10632)\
*   Fixed an issue with signing the Ubuntu 22 package by switching the compression to a supported type\
*   Fixed visual mode outline missing nested R code chunks (#11410)\
*   Fixed `Cannot read property 'python'` error when creating new projects on some systems (#11769)\
\
2022.07.1+554.pro3[](https://docs.posit.co/ide/news/#rstudio-2022.07.1554.pro3)\
\
--------------------------------------------------------------------------------\
\
**“Spotted Wakerobin”** | Date: 2022-07-23\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2022.07.1554.pro3-new)\
\
*   Update Quarto to 1.0.36\
\
2022.07.0+548.pro5[](https://docs.posit.co/ide/news/#rstudio-2022.07.0548.pro5)\
\
--------------------------------------------------------------------------------\
\
**“Spotted Wakerobin”** | Date: 2022-07-07 | [Release Blog Post](https://posit.co/blog/rstudio-2022-07-0-what-s-new/)\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2022.07.0548.pro5-new)\
\
*   RStudio:\
    *   Linux: Support for Ubuntu 22.04, Fedora 35. (#10902, #9854)\
    *   Source marker `message` can contain ANSI SGR codes for setting style and color (#9010)\
    *   Linux/MacOS: Executing a code selection that encounters an error will stop execution of remaining code (#3014)\
    *   Added support for hyperlinks in the console and build pane (#1941)\
    *   Added support for blurred text (#11019)\
    *   “Clean and Rebuild” and “Install and Restart” have been merged into “Install Package”, the “Project Options > Build” gains a “clean before install” option to toggle the –preclean flag. The Build toolbar changes to “Install | Test | Check | More v” (#4289)\
    *   The source button uses `cpp11::source_cpp()` on C++ files that have `[[cpp11::register]]` decorations (#10387)\
    *   New \*Relative Line Numbers- preference for showing line numbers relative to the current line, rather than the first line (#1774)\
    *   Upgraded SOCI library dependency from version 4.0.0 to 4.0.3 (#10792)\
    *   (macOS only) RStudio now reads the PATH from the user’s default shell on startup (#10551)\
    *   (experimental) Option to display the user interface in French (#10455)\
    *   Label commit timestamps as being in UTC (#2544)\
    *   The choice of pipe operator (`magrittr` or native R 4.1+) inserted with the “Insert Pipe Operator” keyboard shortcut can now be configured at the project level as well as the global level (#9409)\
    *   The Git/SVN pane now supports creating ED25519-encrypted SSH keys by default. Newly created RSA SSH keys will now be 4096 bits instead of 2048 to increase security (#8255)\
    *   Read only R and C++ files (marked by “do not edit by hand”) are ignored by the fuzzy file finder (#10912)\
    *   Linux: For compatibility with newer versions of glibc (>= 2.34), the seccomp filter sandbox is disabled. See https://chromium.googlesource.com/chromium/src/+/0e94f26e8/docs/linux\_sandboxing.md#the-sandbox-1 for more details. (#9854)\
    *   Changed “Jobs” tab in IDE to “Background Jobs” (#11296)\
    *   The fuzzy finder shows `test_that()` calls when the search term starts with “t” (#11082)\
    *   Calls to test\_that() appear in the source file outline (#11082)\
    *   Windows: Update embedded libclang to 13.0.1 (#11186)\
    *   Added a warning when renv is actively overriding repository settings in Global Options (#9947)\
    *   Workbench now supports project sharing in single-session mode (i.e. when `server-multiple-sessions=0`) (rstudio-pro#1263)\
\
Find in Files\
\
*   Fixed Find in Files whole-word replace option, so that when “Whole word” is checked, only file matches containing the whole word are replaced, as displayed in the preview (#9813)\
*   Adds support for POSIX extended regular expressions with backreferences in Find in Files find and replace modes, so that special regex characters such as `+` and `?`, `|`, `(`, etc do not need to be escaped, and other ERE escape sequences such as `\b`, `\w`, and `\d` are now supported. This matches the behavior of R’s own `grep()` function, but note that backslashes do not need to be escaped (as they typically are in R strings) (#9344)\
*   The “Common R source files” option in Find in Files has been updated to “Common source files”, with support for searching Markdown (of any type, including .Rmd), JS, and YAML files (#10526)\
*   Updated support for searching paths and filenames with Unicode characters on Windows, including Chinese and non-Latin characters (#9881)\
*   Add a refresh button to the Find in Files pane to enable manual refresh of Find in Files search results (#3240)\
\
R\
\
*   Added support for the `_` placeholder as used by the R pipe-bind operator, to be introduced with R 4.2.0. (#10757)\
*   Added support for using the AGG renderer (as provided by the ragg package) as a graphics backend for inline plot execution; also added support for using the backend graphics device requested by the knitr `dev` chunk option (#9931)\
*   rstudioapi functions are now always evaluated in a clean environment, and will not be masked by objects in the global environment (#8031)\
*   Removed support for versions of R earlier than R 3.3.0. (rstudio-pro#2887)\
*   Chunk options in the body of a code chunk, prefaced by `#|` will be respected during inline code execution, and will take precedence over conflicting chunk options in the chunk header (#10645). Both YAML `tag: value` syntax and valid R expressions will be parsed.\
*   Fixed issue in R debugger that caused RStudio to lose focus out of source code when interacting with the console in certain ways, such as evaluating an expression (#10664)\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2022.07.0548.pro5-fixed)\
\
*   Fixed an issue where vignette content was illegible when viewed with a dark theme. (#11164)\
*   Fixed an issue where previewing a plot as PDF could fail after a session restart. (#1905)\
*   Fixed logging of `HRESULT` error values by logging them as hexadecimal instead of decimal (#10310)\
*   Fixed notebook execution handling of knitr `message=FALSE` chunk option to suppress messages if the option is set to FALSE (#9436)\
*   Fixed plot export to PDF options (#9185)\
*   `.rs.formatDataColumnDispatch()` iterates through classes of `x` (#10073)\
*   `.rs.api.navigateToFile()` is now synchronous and returns document id (#8938)\
*   The `Session > Load Workspace` menu option now explicitly namespaces `base::load` if the `load` function has been masked in the global environment (#10089)\
*   The data viewer truncates large list cells to 50 characters by default, this can be changed with the command palette or `rstudioapi::writeRStudioPreference("data_viewer_max_cell_size", 10L)` (#5100)\
*   The R version and logo displayed in the top left of the console will update to the current R version whenever the R session is restarted (#10458)\
*   Fixed issue where `core::system::userBelongsToGroup` errors under specific sssd configurations (`ignore_group_members = true`) (#10829)\
*   Fixed a security issue where shiny apps and vscode sessions remained active after signout (rstudio-pro#3287)\
*   Fixed an intermittent hang when invoking `rstudio-server verify-installation` which caused stale `rserver` processes to exist (rstudio-pro#3041)\
*   (Windows only) Fixed an issue where multiple instances of RStudio launched at the same time could bind to the same session. (#10488)\
*   Fixed unintended change of date/time formatting in the VCS commit history (#10810)\
*   Fixed an issue where code of the form ‘1:2:3’ was diagnosed incorrectly. (#10979)\
*   Add back link to the title of sessions so that users can easily open sessions in new tabs and copy session links (rstudio-pro#3290)\
*   (Linux Only) License-manager now works in a installer-less context (rstudio-pro#3150)\
*   Fixed an issue where R raw strings were not highlighted correctly in R Markdown documents. (#11087)\
*   Fixed issue with using RStudio server behind multi-level proxy servers (#11010)\
*   Fixed an issue with project sharing where other users’ actions could prevent a session’s auto suspend (rstudio-pro#3362)\
*   Fixed a regression in which the “(Use Default Version)” option was not present in some R version selector drop downs (rstudio-pro#3451)\
*   Fix opening a remote session via downloaded rdprsp file in Mac Desktop Pro when it (RDP) is already open (rstudio-pro#3291)\
*   Fixed several error marker issues in visual mode where they did not display (#10949 #10483)\
*   Allow Jupyter and VScode sessions to be renamed from the homepage (rstudio-pro#1686)\
*   Fixed a user-facing error and added logging when the a session fails to launch due to a misconfigured launcher (rstudio-pro#1684)\
\
RStudio Workbench\
\
*   Add a -G option to `rsandbox` to allow configuring the effective group of the process (#3214)\
*   When resuming a suspended session with the Kubernetes Launcher Plugin, the container image that was previously being used will now be selected by default (#1520)\
*   Upgrade the default version of `code-server` to 4.4.0 to resolve issue with the latest Python VS Code extension (Pro #3320)\
*   JupyterLab Sessions are now configured to be run with the `rsw_jupyterlab` extension. If not globally installed, this will be auto-installed for users on their first JupyterLab session launch (Pro #3429)\
*   Change the label of the “Jobs” section on the homepage to “Workbench Jobs” to disambiguate. Likewise, change the “Launcher” pane title in the IDE to “Workbench Jobs” (rstudio-pro#3138, rstudio-pro#3453)\
*   Session status information on the homepage has been upgraded! Additional information about a session’s processes is easily accessible with a drop-down. Visual updates and cues help improve the user experience. Back-end updates improve the stability and responsiveness of session operations and status changes (rstudio-pro#2443)\
*   Change the “Jobs” tab to “Launcher Diagnostics” in the session information pop-up to further distinguish it from various other references to “jobs.” Hide the “Job Name” field, as it was confusing where it was displayed in the session information details. (rstudio-pro#3453)\
*   Upgrade the default version of `code-server` to 4.4.0 to resolve issue with the latest Python VS Code extension (Pro #3320)\
*   JupyterLab Sessions are now configured to be run with the `workbench_jupyterlab` extension. If not globally installed, this will be auto-installed for users on their first JupyterLab session launch (Pro #3429)\
*   Added ability to configure a `vscode.extensions.conf` file allowing admins to create a list of VS Code extension that will be pre-installed for all users (Pro #3378)\
\
### Deprecated / Removed[](https://docs.posit.co/ide/news/#rstudio-2022.07.0548.pro5-deprecated)\
\
*   The minimum supported R version for the IDE has been increased from R 3.0.1 to R 3.3.0 (rstudio-pro#2887)\
*   **BREAKING:** Block port proxy requests at `/proxy/<port>` for Jupyter sessions - previously only available if [Jupyter Server Proxy](https://github.com/jupyterhub/jupyter-server-proxy)\
     was installed (Pro #3339)\
*   No longer support Debian 9 (“stretch”) for Desktop, Server, and Workbench (#10981)\
*   No longer support SLES 12 for Desktop, Server, and Workbench (#10583)\
\
2022.02.4+500.pro1[](https://docs.posit.co/ide/news/#rstudio-2022.02.4500.pro1)\
\
--------------------------------------------------------------------------------\
\
**“Prairie Trillium”** | Date: 2022-08-27\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2022.02.4500.pro1-fixed)\
\
R:\
\
*   Fixes the bug introduced with rlang >= 1.03 where Rmd documents show the error message object ‘partition\_yaml\_front\_matter’ not found upon project startup (#11552)\
\
Misc:\
\
*   Fixed for schema version comparison that breaks db in downgrade -> upgrade scenarios (rstudio-pro#3572)\
\
2022.02.3+492.pro3[](https://docs.posit.co/ide/news/#rstudio-2022.02.3492.pro3)\
\
--------------------------------------------------------------------------------\
\
**“Prairie Trillium”** | Date: 2022-05-17\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2022.02.3492.pro3-fixed)\
\
*   R:\
    *   Fixed issue in R debugger that caused RStudio to lose focus out of source code when interacting with the console in certain ways, such as evaluating an expression (#10664)\
    *   Fixed an issue where files would appear to be blank when opened in projects not using UTF-8 encoding on Windows with R 4.2.0. (#11206)\
*   Ubuntu 22.04 (“Jammy”) and Fedora 35 Compatibility:\
    *   Ubuntu Jammy builds of RStudio using libssl3 to enable installation on Ubuntu Jammy Jellyfish 22.04 LTS (#10902)\
        *   Fixed incompatibility between QtWebEngine and newer glibc by disabling Chromium sandbox, see disclaimer below (#9854)\
\
Noteglibc 2.34+ and Chromium Sandbox:\
\
For Ubuntu 22.04 (“Jammy”), Fedora 35, and other distros with with newer versions of glibc (>= 2.34) the RStudio Desktop application now disables the Chromium security sandbox in order to workaround a library conflict between the version of chromium used in Qt 5.12 and the platform libraries. The sandbox is a second level security mechanism that prevents untrusted Javascript code from exploiting unknown security problems from using a set of protected system services.\
\
While we will continue to support the Chromium security sandbox for other versions of Linux and in our upcoming Electron version on all platforms, we believe the product security for RStudio Desktop on Ubuntu 22.04 and Fedora 35 will not be significantly affected even with this security feature disabled. Software security is not a perfect science so we want to be clear about the implications so users can make informed choices.\
\
RStudio Desktop is a developer’s tool that is commonly runs custom code outside of the browser sandbox. Users already must take care to trust the code they run, and are protected by the language and library interfaces they use, as well as a trusted supply chain of package managers. RStudio Desktop either accesses all files on the local system, or connects through an explicit process to trusted servers.\
\
See https://chromium.googlesource.com/chromium/src/+/0e94f26e8/docs/linux\_sandboxing.md#the-sandbox-1 for more details.\
\
2022.02.2+485.pro2[](https://docs.posit.co/ide/news/#rstudio-2022.02.2485.pro2)\
\
--------------------------------------------------------------------------------\
\
**“Prairie Trillium”** | Date: 2022-04-27\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2022.02.2485.pro2-new)\
\
R\
\
*   Support for the enhanced R help system, introduced with R 4.2.0.\
*   Added editor support for the R pipe-bind placeholder (`_`). (#10757)\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2022.02.2485.pro2-fixed)\
\
*   Fixed an issue causing tooltips and menus to render incorrectly in Safari 15.4. (#10821)\
*   Fixed a security issue where shiny apps and vscode sessions remained active after signout (rstudio-pro#3287)\
*   Fixed various issues with incorrect escaping of citation brackets (#10075)\
*   Fixed issue with inability to insert Quarto crossrefs (#10918)\
*   (Windows only) Fixed an issue where multiple instances of RStudio launched at the same time could bind to the same session. (#10488)\
\
2022.02.1+461.pro1[](https://docs.posit.co/ide/news/#rstudio-2022.02.1461.pro1)\
\
--------------------------------------------------------------------------------\
\
**“Prairie Trillium”** | Date: 2022-03-23\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2022.02.1461.pro1-fixed)\
\
*   Fixed an issue preventing deployment of applications on Windows. (#10672)\
*   Fixed an issue where `list.files()` did not handle “globs” as expected. (#10679)\
*   Fixed incorrect label in Global Options for “Show full path to project in window title” (#10688)\
*   Fixed hang running Rmd chunks with launcher sessions and other problems the new session-ssl feature of RStudio Workbench (Pro #3301)\
*   Fixed failure to create log file for rserver-session-reaper (#3307)\
*   Fixed failure to create log file for rserver-acls (#3318)\
*   Fixed error refreshing the IDE when project sharing is enabled and a file is actively being shared (Pro #3321)\
*   Fixed restoring session containing invalid `RSTUDIO_PANDOC` value\
\
2022.02.0+443.pro2[](https://docs.posit.co/ide/news/#rstudio-2022.02.0443.pro2)\
\
--------------------------------------------------------------------------------\
\
**“Prairie Trillium”** | Date: 2022-02-23 | [Release Blog Post](https://posit.co/blog/rstudio-workbench-2022-02-0/)\
\
### New[](https://docs.posit.co/ide/news/#rstudio-2022.02.0443.pro2-new)\
\
Visual Mode\
\
*   Improved handling of table markdown in visual editor (#9830)\
*   Added option to show line numbers in visual mode code chunks (#9387)\
*   Made visual code chunks collapsible (#8613)\
*   Show source diagnostics in visual code chunks (#9874)\
*   Fixed code execution via selection in indented visual mode code chunks (#9108)\
*   Fixed detection of HTTP(S) URLs on Windows in the image resolver (#9837)\
*   Improved behavior of citekey removal in Insert Citation dialog (#9124)\
*   Fix issue with unicode characters in citation data (#9745)\
*   Fix issue with unicode characters in citekeys (#9754)\
*   Fix issue with delay showing newly added Zotero references when inserting citations (#9800)\
*   Add ability to insert citation for R Packages (#8921)\
*   Fixed BetterBibTeX detection on Linux (#10007)\
*   Fixed DT tables being squashed in the viewer pane (#10276)\
\
RStudio Workbench\
\
*   Added support for setting the `subPath` on Kubernetes sessions using `KubernetesPersistentVolumeClaim` mounts in `/etc/rstudio/launcher-mounts` (Pro #2976).\
*   Added support for Slurm 21.08 to the Slurm Launcher plugin\
*   Added `license-warning-days` setting to make it possible to adjust or disable the license warnings that appear two weeks prior to expiration (Pro #440)\
*   When an R version defined in `r-versions` uses an environment module, the name of the module is displayed in the version select menus instead of the system R version name. (Pro #2687)\
*   Clicking on a session entry in the RSW homepage will always attempt to launch it – the title is no longer a link. Clicking on “Info” will always show info. (Pro #3082)\
*   With the options `launcher-sessions-create-container-user`, and `launcher-sessions-container-forward-groups` enabled, RSW will now add a group to the user even if the group with a matching id exists but with a different name. (Pro #2971)\
*   Added SSL communication between RSW and remote sessions (using the job launcher). It’s enabled by default and can be disabled in rserver.conf by setting session-ssl-enabled=0. Certificates are generated for each job by default or can be manually configured. (Pro #3026)\
*   Disable session SSL for Code Server 3.9.3 and support auth changes in Code Server 3.11.0 (Pro #3111)\
*   Show user’s full name, or proxied auth display name, in Project Sharing presence indicator (Pro #3121)\
*   Allow users to specify R version in launcher jobs (Pro #1046)\
*   Show additional environment information in the IDE Job Launcher dialog (Pro #3110)\
*   Allow users to specify custom path to R\_HOME in the IDE Job Launcher when the target cluster or image do not match the current environment (Pro #3110)\
*   Removed some unnecessary warnings in the RStudio VS Code Extension when using Dash (Ext #98)\
*   Added a link to a help article about using VS Code Sessions in RStudio Workbench\
*   Blocked access to code-server’s `/absproxy/<port>` url (Pro #3275)\
*   Sessions that attempt to automatically suspend, but were blocked by some operation, will report what’s blocking suspension in the IDE in the R Console toolbar (Pro #2618)\
*   Added ability to disable the dependency checker by setting the `RSTUDIO_DISABLE_PACKAGE_INSTALL_PROMPT` environment variable. This increases the compatibility with older R versions.\
\
R\
\
*   RStudio now supports the experimental UTF-8 UCRT builds of R (#9824)\
*   Preliminary support for R graphics engine version 15 in R 4.2.0. (#10058)\
*   Default file download method in Windows for R 4.2 and above changed from `wininet` to `libcurl` (#10163)\
*   `list.files()` and `list.dirs()` now handle international characters on Windows (#10451)\
\
Misc\
\
*   Add commands to open selected files in columns or active editor (#7920)\
*   Add \*New Blank File- command to Files pane to create empty files of selected type in the directory (#1564)\
*   Add CSRF token header `X-RS-CSRF-Token` and cookie `rs-csrf-token`, to avoid clashing with similarly named headers and cookies in other services (#7319)\
*   Use double indent for function parameters to align with Tidyverse style (#9766)\
*   Recognize `id_ed25519` key file in Version Control options UI (#9991)\
*   Updated Files Pane buttons to resize and remain visible at smaller widths (#9870)\
*   Remove ‘Classic’ IDE theme (#9738)\
*   Added support for Amazon Linux 2 (Pro #2474)\
*   Treat Alt and Caption fields differently depending on file type (#9713)\
*   Fixed shortcut conflict on German keyboard (#9276)\
*   Updated shinymod snippet for Shiny modules (#10009)\
*   Fixed an issue where `conda install` could fail within a Git Bash terminal on Windows (#10283)\
*   Add hover text to ‘Go to project directory’ button in Files pane (#10092)\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2022.02.0443.pro2-fixed)\
\
*   Fixed an issue that could cause calls to `grid` functions to fail after restart (#2919)\
*   Fixed errors when uploading files/directory names with invalid characters (Pro #698)\
*   Added error when rsession may be running a different version of R than expected (Pro #2477)\
*   Fixed “No such file or directory” errors when auto-saving R Notebook chunks while running them (#9284)\
*   Fixed issue causing unnecessary document switching when evaluating statements in debugger (#9918)\
*   Fixed scrolling past long sub-content (like kables) in RMD files. User must interact with sub-content in order to scroll through it (#2202)\
*   Fixed custom shortcuts not appearing correctly in menus (#9915)\
*   Fixed custom shortcuts not appearing correctly in “Keyboard Shortcuts Help” and Electron menus. (#9953)\
*   Fixed header scrolling in data viewer tables not following table contents in unfocused windows (#8208)\
*   Fixed permissions on Mac Desktop application so all user accounts can launch it (#9945, #10267)\
*   Fixed logging directory permissions to be more restrictive (775 instead of 777) (#3099)\
*   Fixed errors when opening or saving Rmarkdown documents when R is busy (#9868)\
*   Fixed issue with SLES 12 builds using OpenSSL 1.1 instead of 1.0.2\
*   Fixed a bug where Slurm Launcher jobs that exited with a non-zero exit code would still have a zero exit code (Launcher #203)\
*   Fixed a bug where Slurm Launcher jobs with standard error would never be written to the output file (Launcher #203)\
*   Fixed a bug where Slurm Launcher jobs that exited due to a signal would not show the exit code as 128+signal (Launcher #203)\
*   Fixed a bug where Launcher log files could be stuck being owned by the root user (#9728)\
*   Fixed bug with customized display names and launcher sessions (Pro #3217)\
\
### Breaking[](https://docs.posit.co/ide/news/#breaking)\
\
*   **BREAKING:** Remove `session-collab-server` and `filebase-path` R Session options (pro #3181)\
\
2021.09.4+403.pro3[](https://docs.posit.co/ide/news/#rstudio-2021.09.4403.pro3)\
\
--------------------------------------------------------------------------------\
\
**“Ghost Orchid”** | Date: 2022-09-19\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2021.09.4403.pro3-fixed)\
\
*   Fixed schema version comparison that breaks db in downgrade -> upgrade scenarios (rstudio-pro#3572)\
\
2021.09.3+396.pro1[](https://docs.posit.co/ide/news/#rstudio-2021.09.3396.pro1)\
\
--------------------------------------------------------------------------------\
\
**“Ghost Orchid”** | Date: 2022-04-20\
\
RStudio Workbench\
\
*   Blocked access to code-server’s `/absproxy/<port>` url (Pro #3275)\
\
Features\
\
*   Support for syntax highlighting of the R 4.2.0 pipe-bind operator. (#10757)\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2021.09.3396.pro1-fixed)\
\
*   Reverted changes supporting UTF-8 code page with UCRT builds of R (>= 4.2.0). (#10507)\
*   Fixed a security issue where shiny apps and vscode sessions remained active after signout (rstudio-pro#3287) (Windows only) Fixed an issue where multiple instances of RStudio launched at the same time could bind to the same session. (#10488) (macOS only) Fixed an issue causing tooltips and menus to render incorrectly in Safari 15.4. (#10821)\
\
2021.09.2+382.pro1[](https://docs.posit.co/ide/news/#rstudio-2021.09.2382.pro1)\
\
--------------------------------------------------------------------------------\
\
**“Ghost Orchid”** | Date: 2022-01-04\
\
Features\
\
*   Support for the UTF-8 code page with UCRT builds of R (>= 4.2.0) (#9824)\
*   Support for R (>= 4.2.0) on Windows (#9792)\
*   Preliminary support for R graphics engine version 15 in R 4.2.0. (#10058)\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2021.09.2382.pro1-fixed)\
\
*   Fix issue causing backslashes to be added to citations in the visual editor (#10075)\
*   Fix issue preventing startup on multi-user macOS environments (#9945, #10267)\
\
2021.09.1+372.pro1[](https://docs.posit.co/ide/news/#rstudio-2021.09.1372.pro1)\
\
--------------------------------------------------------------------------------\
\
**“Ghost Orchid”** | Date: 2021-11-09\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2021.09.1372.pro1-fixed)\
\
*   Fixed issue causing verify-installation to hang in load balanced launcher environments (Pro #3036)\
*   Fixed bug that prevented publishing to Connect from a preview window (#9901)\
*   Fixed bug that prevented RStudio from correctly reporting new versions when running ‘Check for Updates’ (Pro #9911)\
*   Fixed bug that prevented disabling the “Automatically activate project-local Python environments” setting (#9952)\
*   Fixed bug preventing detection of Python environments when conda installed in typical location but not on path (#9975)\
*   Make Python detection less likely to override RETICULATE\_PYTHON (#9999)\
\
2021.09.0+351.pro6[](https://docs.posit.co/ide/news/#rstudio-2021.09.0351.pro6)\
\
--------------------------------------------------------------------------------\
\
**“Ghost Orchid”** | Date: 2021-09-01 | [Release Blog Post](https://posit.co/blog/rstudio-2021-09-0-update-whats-new/)\
\
*   Changed from semantic versioning to calendar based versioning (Pro #2652)\
\
Python\
\
*   Projects containing a Python environment are now automatically activated (#9489)\
\
Logging\
\
*   In an effort to help make the RStudio Team products more cohesive, logging has been changed significantly.\
*   By default, server logs will now be written to file instead of syslog. Warnings and errors will still log to syslog. This can be controlled by the `warn-syslog` parameter in `logging.conf`.\
*   By default, server logs will now be written under `/var/log/rstudio/rstudio-server`.\
*   Logs can now be written in JSON lines format.\
*   Reloading the logging.conf configuration by sending a SIGHUP to the `rserver` process will now cause all RStudio managed subprocesses to also refresh their logging configuration.\
*   Logging can now be partially configured using environment variables (`RS_LOGGER_TYPE`, `RS_LOG_LEVEL`, `RS_LOG_MESSAGE_FORMAT`, and `RS_LOG_DIR`).\
*   Log files will now rotate by time in addition to the existing rotation by file size. This can be controlled by the `rotate-days` parameter in `logging.conf`.\
*   For more information, see section 2 of the Admin Guide.\
\
RStudio Workbench\
\
*   Load-balancing configuration is now automatic, stored in the internal database, and doesn’t require editing config files. Added supporting `rstudio-server list-nodes` command to show users the node’s status according to the database. (Pro #2167)\
*   Use of the `[config]` or `[nodes]` headers, or the precense of nodes, in the load-balancing configuration file will lead to warning messages logged. (Pro #2167)\
*   Use of `[config]` or `[nodes]` headers, or the precense of nodes, in the load-balancing configuration file will lead to warning messages logged. (Pro #2167)\
*   Added `rstudio-server delete-node` command to allow users to remove a load-balancing node from the database (Pro #2800)\
*   Added AWS Cognito support to OpenID integration (Pro #2313)\
*   Add file uploads and downloads to session audit log (Pro #2226)\
*   RStudio Workbench can now run without root access in a single-user mode (Pro #9496)\
*   Updated embedded nginx in Server Pro to 1.20.1 (Pro #2676)\
*   Use separate database schema for open source RStudio Server instances (`rstudio-os`) and RStudio Workbench instances (`rstudio`) to avoid conflicts (Pro #2725)\
*   Prevent user preferences from setting CRAN repos when `allow-cran-repos-edit=0` (Pro #1301)\
*   Ensure that improperly configured `launcher-sessions-callback-address` values can’t hang user sessions (Pro #2532)\
*   Support username aliases, where two usernames map to the same uid (Pro #2736)\
\
### Fixed[](https://docs.posit.co/ide/news/#rstudio-2021.09.0351.pro6-fixed)\
\
*   Fixed issue where running Python chunk in notebook did not validate reticulate was installed (#9471)\
*   Fixed issue where .md, .py, .sql, and .stan files had duplicate event handlers (#9106)\
*   Fixed issue where output when running tests could be emitted in wrong order in Build pane (#5126)\
*   Fixed issue where RStudio could crash when viewing a malformed data.frame (#9364)\
*   Fixed issue where completion tooltip was erroneously shown in multi-line strings in some cases (#8677)\
*   Fixed issue with autocompletion of column names within native-piped R expressions (#9385)\
*   Fixed issue where help requests for Python objects would fail with reticulate 1.20 (#9311)\
*   Fixed issue where busy sessions can’t be interrupted and block basic file operations (#2038)\
*   Fixed issue where R Markdown error output was not properly formatted when displayed (#9390)\
*   Fixed issue where R Markdown template skeletons with a ‘.rmd’ extension were not discovered (Pro #1607)\
*   Fixed issue where autocompletion system could emit errors with R (< 3.3.0). (Pro #2680)\
*   Fixed issues causing multiple background jobs to be created when running Shiny applications in the background (#8746, #6904)\
*   Fixed issue causing an error when adding files to static content published to RStudio Connect (#9571)\
*   Fixed issue where R banner could be displayed twice on startup (#6907)\
*   Fixed issue where RStudio was unable to initialize a Git repository in UNC paths on Windows (#4137)\
*   Removed the breaking change introduced in Juliet Rose that changed the behavior of the X-Forwarded-Proto header when RSW is behind a proxy server (Pro #2657)\
*   Fixed issue where adjacent links in the Visual Editor could merge into a single link (#8471)\
*   Fixed Issue where items deleted from a local Zotero Collection would still appear in the Visual Editor’s Insert Citation dialog.\
*   Fixed issue where Console width was computed incorrectly with some custom fonts (#8696)\
*   Fixed two 502 errors with load balancing: quick session restart, and failover for non-launcher sessions (Pro #2696)\
*   Fixed problem with backspace in terminal causing incorrect display (#9249)\
\
Misc\
\
*   **BREAKING:** RStudio Desktop Pro only supports activation with license files (Pro #2300)\
*   **BREAKING:** The `session-env-var-save-blacklist` option has been renamed to `session-ephemeral-env-vars`.\
*   **BREAKING:** The `directory-view-whitelist` option has been renamed to `directory-view-allow-list`.\
*   Update bundled Pandoc to version 2.14.1\
*   Depend on new versions of `rmarkdown` (2.10) and `shiny` (1.6)\
*   Fixed an issue where scroll position in PDFs was not preserved on re-render (#9603)\
*   Support highlight of ‘css’ and ‘asis’ chunks in R Markdown documents (#4821)\
*   Improved ordering of completion results within `library()` calls (#9293)\
*   Syntax support for embedded knitr chunks (#9579)\
*   Add option to synchronize the Files pane with the current working directory in R (#4615)\
*   Add new \*Set Working Directory- command to context menu for source files (#6781)\
*   Local background jobs can now be replayed (#5548)\
*   Improved display of R stack traces in R functions invoked internally by RStudio (#9307)\
*   High DPI (“Retina”) plots are now supported on RStudio Server (#3896)\
*   The “auto-detect indentation” preference is now off by default (#9211)\
*   Make the _Use renv with this project_ option sticky, and allow setting by admins (Pro #2671)\
*   RStudio no longer treats R objects containing null external pointers specially when building Environment pane (#5546)\
*   Make Cmd+Shift+0 the shortcut for restarting session on MacOS (#7695)\
*   Update Plumber file template for Plumber 1.0 (#9402)\
*   Support creating supplemental groups when create-container-user=1 (Pro #2276)\
*   RStudio addins installed within `tools:::R_user_dir(<pkg>, "config")` are now discovered by RStudio. (#9648)\
\
1.4.1743-4[](https://docs.posit.co/ide/news/#rstudio-1.4.1743-4)\
\
-----------------------------------------------------------------\
\
**“Evergreen Rose”** | Date: 2022-04-28\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-3)\
\
*   Removed the breaking change introduced in Juliet Rose that changed the behavior of the X-Forwarded-Proto header when RSW is behind a proxy server (Pro #2657)\
*   Fixed an issue where RStudio Desktop Pro could fail when connecting to remote sessions via https (Pro #2651)\
*   Fixed a crash that can occur when opening a VS Code session behind a path-rewriting proxy (Pro #2699)\
*   Updated embedded nginx to 1.20.1 (Pro #2676)\
*   Blocked access to code-server’s `/absproxy/<port>` url (Pro #3275)\
*   Fixed a security issue where shiny apps and vscode sessions remained active after signout (rstudio-pro#3287)\
\
1.4.1717-3[](https://docs.posit.co/ide/news/#rstudio-1.4.1717-3)\
\
-----------------------------------------------------------------\
\
**“Juliet Rose”** | Date: 2021-06-01 | [Release Blog Post](https://posit.co/blog/rstudio-v1-4-update-whats-new/)\
\
This is a major update to RStudio 1.4 that includes the following enhancements and bugfixes:\
\
R\
\
*   Add native support for Apple Silicon (aarch64) builds of R on macOS (#8652)\
*   Show memory usage details in Environment pane (#4033)\
*   Added support for the `|>` pipe operator and the `=>` pipe-bind operator, proposed for R 4.1.0 (#8543)\
*   Added support for the `\(x)` function shorthand syntax, proposed for R 4.1.0 (#8543)\
*   Added preference toggle for inserting the `|>` pipe operator when the Insert Pipe Operator command is used (#8534)\
*   Compilation of Sweave documents now uses tinytex when requested (#2788)\
*   Preliminary support for R graphics engine version 14 in R 4.1.0. (#9251)\
\
Python\
\
*   The Python REPL can now be interrupted (#8763, #8785)\
*   Python installs within `/opt/python` and `/opt/local/python` are now discovered by RStudio (#8852)\
*   Improved handling of unicode input on Windows (#8549)\
*   Fixed issue where inspecting a null Python object would cause emit errors to console (#8185)\
*   Detect active Python version when publishing content (#8636)\
*   Use active Python version when knitting R Markdown files (#8854)\
*   The active version of Python is now placed on the PATH for new Terminal sessions (#9188)\
\
RStudio Workbench\
\
*   RStudio Server Pro has been renamed to RStudio Workbench to more accurately reflect its cross-language editing capabilities.\
*   **BREAKING:** RStudio Workbench’s Linux packages have new file names, `rstudio-workbench-*` instead of `rstudio-server-pro-*`. The operating system package name remains `rstudio-server`, so installs and upgrades will work correctly. Scripts which refer to the `.deb` or `.rpm` file names directly will need to be updated.\
*   Added support for JupyterLab 3 (Pro #2022)\
*   Add support for using OpenID and SAML authentication schemes when a proxy is required for outbound requests (Pro #2427)\
*   Updated product licensing engine (LimeLM) to TurboActivate and TurboFloat to v4.4.3.\
*   Licenses can now be applied and updated without a restart (Pro #2468)\
*   Improved R session diagnostic logging; now records all instances of a session (Pro #2268)\
*   Improved troubleshooting logging for PostgreSQL encrypted password configuration (Pro #2441)\
*   Improved `locktester` file locking diagnostic utility; now tries all lock types and recommends configuration (Pro #2400)\
*   Added new `rstudio-server reload` command to reload some server configuration settings without a restart (Pro #2139)\
*   Added `pool-size` option in `database.conf` to control size of database connection pool; avoid creating a large pool on systems with many CPUs (Pro #2494)\
*   Display hidden characters in filenames when logging config files with `run-diagnostics` (Pro #2509)\
*   Add support for SSL communication between nodes when using load balancing (Pro #2565)\
\
VS Code\
\
*   Visual Studio Code is fully supported on RStudio Workbench and no longer in beta\
*   Added support for Dash, Streamlit, and local web development servers in VS Code sessions\
*   Added RStudio Workbench navigation tools in VS Code sessions\
*   Added a new user settings template file for VSCode settings to allow administrators to specify a default user configuration for VSCode sessions (Pro #2014)\
*   Set environment variables `RS_URI_SCHEME`, `RS_SESSION_URL`, `SERVER_URL`, and `RS_HOME_URL` when VSCode is launched (Pro #2346, Pro #2373)\
*   Updated `rstudio-server install-vs-code` to install `code-server` 3.9.3 (Pro #2576)\
*   **BREAKING** `code-server` 3.3.0 moves the executable to a `bin` directory. After upgrading `code-server`, the `exe` setting in `vscode.conf` may need to be updated to include `bin` in the path. This happens if the upgrade is not done by `install-vs-code-ext` or if `vscode.conf` is being programatically managed. If not updated, VS Code sessions will launch with “wrong version number” message. [Related `code-server` change](https://github.com/cdr/code-server/releases/tag/v3.3.0)\
    \
*   Change the default behavior of `install-vs-code` to not configure a global extensions directory and allow users to manage their own extensions. If `install-vs-code` was run with a previous release and you’d like to change your configuration, the configuration can be manually removed from `vscode.conf` or the script can be rerun to regenerate `vscode.conf` (Pro #2516)\
*   Added `rstudio-server install-vs-code-ext` script to install the RStudio Workbench VS Code extension in a global directory and upgrade `code-server` to 3.9.3 (Pro #2456)\
*   When a global extensions directory isn’t configured, install the RStudio Workbench extension on the first VS Code session launch per user (Pro #2376)\
*   Disable the extensions marketplace in VS Code sessions when a global directory is configured that the user does not have write access to (Pro #2507)\
*   Improved error messaging for VS Code session errors from `verify-installation` (Pro #2442)\
\
RStudio Server Open Source\
\
*   **BREAKING:** RStudio when served via `http` erroneously reported its own address as `https` during redirects if the header `X-Forwarded-Proto` was defined by a proxy. That could lead to a confusing proxy setup. That has been fixed, but existing proxy installations with redirect rewite settings matching for `https` may have to be adjusted.\
*   **BREAKING:** RStudio Server no longer supports Internet Explorer 11.\
*   Added `session-suspend-on-incomplete-statement` option to enable more aggressive session suspension behavior (Pro #1934)\
*   New `env-vars` configuration file simplifies setting environment variables for the main RStudio server process. (Pro #2433)\
*   Refreshed style on sign-in page; sign-in page now has a dark mode that syncs with the operating system’s (#9092, #9093)\
\
Visual Editor\
\
*   Code chunks in the visual editor now respect the “Tab Key Always Moves Focus” accessibility setting (#8584)\
*   The commands “Execute Previous Chunks” and “Execute Subsequent Chunks” now work when the cursor is outside a code chunk in the visual editor (#8500)\
*   The commands “Go to Next Chunk” and “Go to Previous Chunk” now work in the visual editor (#9005)\
*   Fixed issue causing the document to scroll unpredictably when a code chunk inside a list item is executed in the visual editor (#8883)\
*   Cmd+U now toggles underlining in the visual editor on macOS (#8656)\
*   Improve YAML cursor position after omni-insert in the visual editor (#8670)\
*   Fix issues finding words with punctuation in visual mode (#8655)\
*   Fix spurious image insertion when pasting into visual mode from Excel (#8665)\
*   Fix issue causing spell check to stop identifying misspellings when switching between visual and source modes (#8473)\
*   Fixed issue importing dataset author data from DOIs in the visual editor (#9059)\
*   Fixed issue where the Insert Citation dialog in the visual editor would clear selected citation when typeahead searching (#8521)\
*   Fixed issue where the bibliography path is assumed to be document relative when inserting citations in the visual editor (#8847)\
*   Fixed error in visual mode spellcheck where underline would disappear when hitting backspace (#9187)\
\
Job Launcher\
\
*   Fixed an issue where the Kubernetes Launcher could hang in Azure Kubernetes Service (AKS) environments by lowering the watch-timeout-seconds parameter default down to 3 minutes instead of 5 (Pro #2312)\
*   Fixed issue preventing Kubernetes sessions from starting due to incorrect SSL certificate checking on websocket connections; make websocket connections support the `verify-ssl-certs` option (Pro #2463)\
*   Fixed an issue where the Kubernetes Launcher can sometimes get in a state where communication with Kubernetes hangs until a restart (Pro #2548)\
*   Fixed an issue where Kubernetes Launcher services could sometimes leak and never be cleaned up (Pro #2548)\
*   Fixed an issue causing Kubernetes plugin to fail to deserialize jobs from Kubernetes 1.19 (Pro #2605)\
*   Improved a Slurm Session Launch Delay that may occur due to buffering when using Slurm job steps (Pro #2331)\
*   Fixed an issue where Load Balanced Local Launcher instances could get into a state where they would no longer receive job updates from other nodes due to silent network drops (Pro #2281)\
\
Misc\
\
*   The mouse back / forward buttons can now be used to navigate within the Help pane (#8338)\
*   Right-click on document tab provides menu with close, close all, close others (#1664)\
*   Rename File added to document tab context menu (#8374)\
*   Copy Path command added to document tab context menu (#7289)\
*   Preliminary compatibility with UCRT builds of R-devel (#8461)\
*   Update Windows Desktop to openSSL 1.1.1i (#8574)\
*   Improve ordering of items in Command Palette list and search results (#7567, #7956)\
*   Update embedded Pandoc to v2.11.3.2\
*   Change default per-user install folder to `%LocalAppData%\Programs` on Windows (#8598)\
*   Detect newer plumber tags when enabling plumber integration (#8118)\
*   Option to restore RStudio 1.2 tab key behavior in editor find panel; search in Command Palette for “Tab key behavior in find panel matches RStudio 1.2 and earlier” (#7295)\
*   Show `.renvignore` in Files pane (#8658)\
*   Make the set of always-shown files and extensions in the Files pane configurable (#3221)\
*   Log location of addins that raise parse errors at startup (#8012)\
*   Support dual/charcell-spaced editor fonts (e.g., Fira Code) on Linux desktop environments (#6894)\
*   Improve logging of session RPC failures (Pro #2248)\
*   Add support for `rstudioapi` methods enabling callbacks for command execution (Pro #1846)\
*   Add support for non-CRAN repositories when installing R packages in the background (#8946)\
*   Add server homepage link and retry options to mitigate “Unable to connect to service” errors (Pro #2066)\
*   Add support for commenting and uncommenting code in C (`.c` and `.h`) files (#4109, thanks to @cm421)\
*   The R session binary (`rsession`) now has a `--version` option for reporting its version (Pro #2410)\
*   RStudio Desktop startup diagnostics now include the RStudio version/platform and an option to copy to plain text (#6628, #9117)\
*   Improved Spellcheck package to be compatible with all known Hunspell-compatible dictionaries, improved spellcheck initial loading and large file performance (#9161)\
*   Add ‘whole word’ filter to Find in Files. (#8594)\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-4)\
\
*   Fixed an issue that could cause RStudio to crash when generating plots on Windows (#9113)\
*   Fixed an issue causing slow session startup and “Unable to connect to service” errors on RStudio Server (#9152)\
*   Fix Windows Desktop installer to support running from path with characters from other codepages (#8421)\
*   Fixed issue where R code input could be executed in the wrong order in some cases (#8837)\
*   Fixed issue where debugger could hang when debugging functions called via `do.call()` (#5158)\
*   Fixed issue where rendering .tex document with tinytex would fail on Windows (#8725)\
*   Fixed issue where reinstalling an already-loaded package could cause errors (#8265)\
*   Fixed issue where RStudio would inappropriately autoload the ‘yaml’ and ‘tinytex’ packages (#8698)\
*   Fixed issue where right-assignment with multi-line strings gave false-positive diagnostic errors (#8307)\
*   Fixed issue where restoring R workspace could fail when project path contained non-ASCII characters (#8321)\
*   Fixed issue where forked R sessions could hang after a package was loaded or unloaded (#8361)\
*   Fixed issue where attempting to profile lines ending in comment would fail (#8407)\
*   Fixed issue where warnings + messages were mis-encoded in chunk outputs on Windows (#8565)\
*   Fixed issue where C++ compilation database was not invalidated when compiler was updated (#8588)\
*   Fixed issue where SQL chunks containing non-ASCII characters could fail to run on Windows (#8900)\
*   Fixed issue where ‘case:’ statements were not outdented when rainbow parentheses were active. (#8846)\
*   Fixed issue where Stan completion handlers were duplicated on save (#9106)\
*   Improved checks for non-writable R library paths on startup (Pro #2184)\
*   Fixed issue preventing R Notebook chunks from being queued for execution if they had never been previously run (#4238)\
*   Fix various issues when the “Limit Console Output” performance setting was enabled (#8544, #8504, #8529, #8552)\
*   Fix display of condition messages (errors and warnings) in some character encodings (#8546)\
*   Fix out-of-date tooltip when renaming files (#8490, #8491)\
*   Fix incorrect keyboard shortcuts shown in some places in the Command Palette (#8735)\
*   Fixed issue with formatting of closing braces when inserting newline in C++ code (#8770)\
*   Fixed issue where empty panes would remain open and pop open unexpectedly (#8460)\
*   Fixed issue where ‘continue comment on newline’ would treat Markdown headers as comments (#6421)\
*   Fixed issue where Set Working Directory command could fail if path contained quotes (#6004)\
*   Fixed issue where Pro database drivers will not install if `~/odbcinst.ini` is missing (Pro #2284)\
*   Fixed issue causing the mouse cursor to become too small in certain areas on Linux Desktop (#8781)\
*   Fixed issue causing Run Tests command to do nothing unless the Build tab was available (#8775)\
*   Fixed issue where paging in the DataViewer would throw errors and current columns wouldn’t update (#9078)\
*   Fixed issue causing RStudio Server to create `.local/share/rstudio` folder with incorrect permissions when `session-timeout-kill-hours` is set (Pro #2388)\
*   Fixed issue causing `verify-installation` to exit without showing the error that caused it to do so (Pro #2399)\
*   Fixed issue causing spurious “Failed to reset ACL permission mask” errors to be logged outside shared projects on some filesystems (Pro #2406)\
*   Fixed issue where sending code from Python History pane would switch Console to R mode (#8693)\
*   Fixed issue where Open File dialog would fail to open files whose names were explicitly typed (#4059)\
*   Fixed issue causing Project Sharing to fail to set Access Control Lists when using NFS v4 and `username@domain` security principals (Pro #2415)\
*   Fixed issue where dialog boxes \[e.g. Git commit, Installing Pro Database drivers\] could fail to show output with Limit Console Output turned on (Pro #2284)\
*   Fixed issue where uploading a .zip archive when unzip was not on PATH would cause a cryptic error (#9151)\
*   Fixed issue where RStudio occasionally reset the locale to the “default” locale on Windows (#9350)\
*   Errors that occur when R packages update the Connections pane are now better handled and reported (#9219)\
*   Fixed an issue where login page could fail intermittently with slow network connections (Pro #2551)\
\
1.4.1106-5[](https://docs.posit.co/ide/news/#rstudio-1.4.1106-5)\
\
-----------------------------------------------------------------\
\
**“Tiger Daylily”** | Date: 2021-02-22\
\
This is a minor update to RStudio 1.4 that contains fixes for a handful of important bugs.\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-5)\
\
*   Fixed issue where R code input could be executed in the wrong order in some cases (#8837)\
*   Fixed issue where default initial working directory was incorrectly set to a project directory (#8683)\
*   Fixed issue causing the second inline equation in a paragraph to fail to render in visual editing mode (#8810)\
*   Fixed issue where session source database sentinel file was not being written correctly when the session is suspended (#8903)\
\
Misc - Update Pandoc to 2.11.4 (#8848) - Update jQuery to 3.5.1 (Pro #2314)\
\
1.4.1103-4[](https://docs.posit.co/ide/news/#rstudio-1.4.1103-4)\
\
-----------------------------------------------------------------\
\
**“Wax Begonia”** | Date: 2021-01-20\
\
*   A new [visual editor](https://rstudio.github.io/visual-markdown-editing/)\
     for R Markdown documents\
*   Improved support for Python, including an environment pane for Python and visualization of Python objects\
*   Workbench productivity improvements, including a command palette and rainbow parentheses\
*   A more configurable workspace with additional source columns and improved accessibility\
*   Support for SAML and OpenID authentication, and experimental support for VS Code sessions, in RStudio Server Pro\
*   Dozens of small improvements and bugfixes\
\
Python\
\
*   The default version of Python used by `reticulate` can now be customized via the Global Options pane.\
*   Python indentation rules are now applied to Python code within R Markdown documents. (#5945)\
*   Pressing F1 when the Python completion list is shown now opens the relevant Help documentation. (#5982)\
*   Python objects are now shown in the Environment Pane when `reticulate` REPL is active. (#6862)\
*   Python objects can now be viewed using the Data Viewer and Object Explorer. (#6862)\
*   The `matplotlib.pyplot.show()` function now displays PNG plots within the Plots pane. (#4965)\
*   Plots generated via `matplotlib` are now shown with a higher DPI in the Plots pane when appropriate.\
*   The autocompletion system can now auto-complete virtual environment names in `reticulate::virtualenv()`.\
\
Plots\
\
*   The default renderer used for the RStudio graphics device can now be customized. (#2142)\
*   The AGG renderer (as provided by the ragg package) is now a supported backend. (#6539)\
*   Version 14 of the R Graphics Engine, which will be introduced in R 4.1, is now supported. (#8383)\
\
Workbench\
\
*   Any tab can be hidden from view through Global Options. (#6428)\
*   Accessibility preference to reduce focus rectangle display (#7242)\
*   Multiple source panes can be opened in the main window via Global Options. (#2854)\
*   Keyboard shortcut F6 added to navigate focus to the next pane. (#7408)\
*   Accessibility preference to show a highlight around focused panel (#7881)\
\
Configurable Paths\
\
*   The user data folder ~/.rstudio has been moved to ~/.local/share/rstudio, and its location can now be customized with XDG\_DATA\_HOME. (#1846)\
*   XDG\_CONFIG\_DIRS can be used to specify alternate directories for server configuration files. (Pro #1607)\
*   It is now possible to specify the exact folder for user data and configuration files using new environment variables RSTUDIO\_DATA\_HOME, RSTUDIO\_CONFIG\_DIR, etc. (#7792)\
\
Miscellaneous\
\
*   The Files pane now sorts file names naturally, so that e.g. step10.R comes after step9.R. (#5766)\
*   Added command to File pane’s “More” menu to copy path to clipboard (#6344)\
*   Table summaries are shown for tibble objects in R Notebooks. (#5970)\
*   RStudio now infers document type from shebang (e.g. #!/usr/bin/env sh) for R, Python and shell scripts (#5643)\
*   New option to configure soft wrapping for R Markdown files, and command to change the soft wrap mode of the editor on the fly (#2341)\
*   New Command Palette for searching and running build-in commands and add-ins (#5168)\
*   Colorize parentheses, braces, and brackets in assorted colors (#7027)\
*   Option to display Console error and message output in same color as regular output (#7029)\
*   Moved console options to a new pane in Global Options (#7047)\
*   The Data Viewer now uses the format() methods defined for columns entries when available (#7239)\
*   Add support for navigating source history with mouse forward/back buttons (#7272)\
*   Add ability to go directly to various Global Option panes via Command Palette (#7678)\
*   R6Class method definitions are now indexed and accessible by the fuzzy finder (Ctrl + .)\
*   The ‘Preview’ command for R documentation files now passes along RdMacros declared from the package DESCRIPTION file (#6871)\
*   Some panes didn’t have commands for making them visible, now they do (#5775)\
*   Show correct symbol for Return key in Mac menus (#6524)\
*   Added command and button for clearing Build pane output (#6636)\
*   Added option to disable clickable hyperlinks in the editor (#6689, thanks to Paul Kaefer)\
*   Added basic editor support for Dockerfiles (#5141)\
*   Markdown-style sub-sections are now rendered as nested sections in the document outline for R documents (#4124)\
*   Update to Pandoc 2.11 (#7696)\
*   Ctrl + D can now be used to send EOF when reading user input via readLines() (#3448)\
*   External files with spaces in their path or filename are now openable on Big Sur from Files pane (#8506)\
*   PDF files opened from Files pane on macOS will open in registered application, not always Preview.app (#8506)\
*   RStudio Server is no longer supported on RedHat Enterprise Linux 6 or CentOS 6, as these platforms have reached the vendors’ End of Life (EOL) dates (Pro #2203)\
\
RStudio Server\
\
*   The font used in the editor and console can now be customized on RStudio Server. (#2534)\
*   The new option www-same-site provides support for the SameSite attribute on cookies issued by RStudio. (#6608)\
*   New X-RStudio-Request header for specifying originating URL behind path-rewriting proxies (Pro #1579)\
*   New X-RStudio-Root-Path header or the new www-root-path for specifying the exact path prefixes added by a path-rewriting proxy (Pro #1410).\
*   The option www-url-path-prefix was deprecated and removed. Use www-root-path instead.\
*   Improved error logging of mistyped usernames when using PAM authentication (#7501)\
\
RStudio Server Pro\
\
Note\
\
*   RStudio Server Pro now requires a Postgres database when using its internal load balancer; this database must be set up prior to upgrade from earlier releases. If you have a multi-node RStudio Server Pro installation, consult the Administration Guide for instructions before upgrading.\
*   RStudio Server Pro uses a new location for user state; .rstudio is now .local/share/rstudio. This is a breaking change if you have symlinked .rstudio and can make downgrade more complicated. See the Administration Guide for more information, including instructions for using the old location if desired for compatibility with previous releases.\
\
*   SAML is now supported as an authentication mechanism (Pro #1194)\
*   OpenID Connect is now support as an authentication mechanism (Pro #1747)\
*   Visual Studio Code is now an available editor when using Launcher sessions (Pro #1423)\
*   New auth-proxy-sign-out-url option specified an endpoint to take the user to when “Sign Out” is clicked in the IDE user interface (Pro #1745)\
*   New user profile option session-limit allow limiting the maximum number of sessions a user can have (Pro #540)\
*   Project sharing is automatically disabled and a warning is issued when server-multiple-sessions=0. (Pro #1263)\
*   New load-balancer option timeout limits how long to wait for a response from a node, defaults to 10 seconds. (Pro #1642)\
*   New load-balancer option verify-ssl-certs for testing nodes with self-signed certificates when using SSL. (Pro #1504)\
*   New launcher-verify-ssl-certs and launcher-sessions-callback-verify-ssl-certs options for testing with self-signed certificates when using SSL. (Pro #1504)\
*   R sessions can now be renamed from within the session or the home page. (Pro #1572)\
*   Project Sharing now works on Launcher sessions.\
*   Remote session connections over HTTPS can now load certificates from the Apple Keychain. (Pro #1828)\
*   Improved session load balancing when using the Local Job Launcher plugin to evenly spread session load between Local plugin nodes. (Pro #1814)\
*   Update embedded nginx to v1.19.2 (Pro #1719)\
*   Changed the command to retrieve Slurm resource utilization to be run as the current user rather than the slurm-service-user (Pro #1527)\
*   Reduced supurflous log messages in the Slurm Launcher Plugin log file about non-RStudio jobs in Slurm (Pro #1528)\
*   Allow administrators to disable the ability to set resource requests on jobs launched through the Slurm Launcher Plugin (Pro #1948)\
*   Add support for setting GPU and GRES requests on jobs launched through the Slurm Launcher Plugin (Pro #1390)\
*   Allow administrators to enable Slurm job requeueing for jobs launched through the Slurm Launcher Plugin (Pro #2025)\
*   Update the version of Slurm supported by the Slurm Launcher Plugin to 20.02 (Pro #2192)\
*   Project Sharing can now use raw UIDs as security principals, for compatibility with nodes that cannot resolve domains (Pro #2104)\
*   RETIRED: The option auth-proxy-require-hmac is has been retired and it is no longer operational. RStudio will not start if enabled. See the documentation on \[Proxy Security Considerations\] for alternatives to secure RStudio. (Pro #2029)\
*   Fix GetPass not working in remote sessions from Rstudio Desktop Pro (Pro #2218)\
*   Fix issue with creating RSA key from remote sessions in RStudio Desktop Pro (Pro #2219)\
*   Ensure error messages occurring during installation are displayed in the terminal (Pro #2214)\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-6)\
\
*   Fixed issue where debugger contexts were not displayed correctly for byte-compiled functions. (#6922)\
*   UTF-8 character vectors are now properly displayed within the Environment pane. (#6877)\
*   Fixed issue where diagnostics system surface “Unknown or uninitialized column” warnings in some cases. (#7372)\
*   Fixed issue where hovering mouse cursor over C++ completion popup would steal focus. (#5941)\
*   Fixed issue where autocompletion could fail for functions masked by objects in global environments. (#6942)\
*   Fixed issue where autocompletion could fail to provide argument names for piped-to S3 generics. (#7060)\
*   Fixed issue where UTF-8 output from Python chunks was mis-encoded on Windows. (#6254)\
*   Git integration now works properly for project names containing the ‘!’ character. (#6160)\
*   Fixed issue where loading the Rfast package could lead to session hangs. (#6645)\
*   Fixed header resizing in Data Viewer (#1665)\
*   Fixed resizing last column in Data Viewer (#2642)\
*   Fixed inconsistencies in the resizing between a column and its header (#4361)\
*   Fixed submission of inconsistently indented Python blocks to reticulate (#5094)\
*   Fixed error when redirecting inside Plumber applications in RStudio Server Pro (Pro #1570)\
*   Fixed failure to open files after an attempt to open a very large file (#6637)\
*   Fixed Data Viewer getting out of sync with the underlying data when changing live viewer object (#1819)\
*   Fixed issue where attempts to plot could fail if R tempdir was deleted (#2214)\
*   Fixed issue that caused sessions to freeze due to slow I/O for monitor logs (Pro #1259)\
*   Added CSRF protection to sign-in pages (Pro #1469)\
*   Fixed issue that allowed multiple concurrent sign-in requests (#6502)\
*   Fixed issue where the admin logs page could sometimes crash due to a malformed log statement (Pro #1768)\
*   Fixed issue where the URL popped out by the Viewer pane was incorrect after navigation (#6967)\
*   Fixed issue where clicking the filter UI box would sort a data viewer column (#7299)\
*   Fixed issue where Windows shortcuts were not resolved correctly in file dialogs. (#7327)\
*   Fixed issue where failure to rotate a log file could cause a process crash (Pro #1779)\
*   Fixed issue where saving workspace could emit ‘package may not be available when loading’ warning (#7001)\
*   Fixed issue where indented Python chunks could not be run (#3731)\
*   Fixed disappearing commands and recent files/projects when RStudio Desktop opens new windows (#3968)\
*   Fixed issue where active repositories were not propagated to newly-created renv projects (#7136)\
*   Fixed issue where .DollarNames methods defined in global environment were not resolved (#7487)\
*   Reduced difference in font size and spacing between Terminal and Console (#6382)\
*   Fixed issue where path autocompletion in R Markdown documents did not respect Knit Directory preference (#5412)\
*   Fixed issue where Job Launcher streams could remain open longer than expected when viewing the job details page (Pro #1855)\
*   Fixed issue where rstudioapi::askForPassword() did not mask user input in some cases\
*   Fixed issue where Job Launcher admin users would have gid=0 in Slurm Launcher Sessions (Pro #1935)\
*   Fixed issue where Slurm Job Launcher jobs would not post updated resource utilization without browser refresh (Pro #2177)\
*   Fixed issue causing script errors when reloading Shiny applications from the editor toolbar (#7762)\
*   Fixed issue where saving a file or project located in a backed up directory (such as with Dropbox or Google Drive) would frequently fail and display an error prompt (#7131)\
*   Fixed issue causing C++ diagnostics to fail when Xcode developer tools were active (#7824)\
*   Added option for clickable links in Terminal pane (#6621)\
*   Fixed issue where R scripts containing non-ASCII characters in their path could not be sourced as a local job on Windows (#6701)\
*   Fixed issue where non-ASCII characters in Subversion commit comments were incorrect encoded on Windows (#7959)\
*   Prevent Discard button from being hidden in Subversion diff viewer (#6031)\
*   Fixed issue where French (AZERTY) keyboards inserted ‘/’ rather than ‘:’ in some cases (#7932)\
*   readline() and readLines() can now be interrupted, even when reading from stdin() (#3448)\
*   Fixed issue causing Knit button to show old formats after editing the YAML header (#7833)\
*   Fixed issue wherein the Python prompt would continue to be shown after an R restart (#8011)\
*   Fixed issue where searches in the console history could inappropriately preserve search position (#7682)\
*   Fixed issue where auth-pam-session-use-password would not work when multiple Server nodes are used behind an external load balancer (Pro #2158)\
*   Fixed issue where project sharing configured it server-project-sharing-root-dir would fail to share when the path contain mixed ACL support (Pro #2061)\
*   Fixed issue where project sharing would fail to share when the path contain mixed NFS ACL support (Pro #2103)\
*   Fixed issue where in sharing a project on some NFSv4 filesystems could result in damage to owner permissions (Pro #2188)\
*   Fixed issue where file permissions were not corrected after uploading a file to a shared project (Pro #2208)\
*   Fixed issue where the project sharing would not work behind a HTTPS proxy (Pro #2088)\
\
1.3.1093-1[](https://docs.posit.co/ide/news/#rstudio-1.3.1093-1)\
\
-----------------------------------------------------------------\
\
**“Apricot Nasturtium”** | Date: 2020-09-18\
\
This is a patch release of RStudio 1.3, consisting primarily of bugfixes and small improvements.\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-7)\
\
*   Fix an issue where a PAM session would be attempted for Launcher sessions when no password is available, potentially locking users out of their accounts (Pro #1831)\
*   Fix an issue causing logs to fail to load in the admin panel when using the local time zone (Pro #1766)\
*   Fix an issue where syslog and monitor log entries could contain newlines in them, preventing the admin logs page from properly displaying log entries (Pro #1782)\
*   Fix an issue where failing to open the Slurm job output file could result in hanging `tail -f` child processes (Pro #1856)\
*   Fix an issue where a delay in the creation of the Slurm job output file could result in a hanging “Determining session network” page when opening a session (Pro #1792)\
*   Fix an issue where `auth-none` would not load sessions (#7575)\
*   Fix session crashing on Windows desktop (#7637, #7652, #7665)\
*   Fix an issue where launching many sessions simultaneously could cause a segfault (#7670)\
*   Fix an issue where invalid logging statements were not properly skipped in the Admin log page, causing a crash of the rserver-admin process (#1766)\
*   Fix an issue where sharing a project would cause extra rserver processes to be spawned into a hanging state, requiring external cleanup (Pro #1736)\
*   Fix an issue where invalid logging statements were not properly skipped in the Admin log page, causing a crash of the rserver-admin process (Pro #1766)\
*   Fix an issue where sessions running on Slurm compute nodes with names longer than 20 characters could not be entered (Pro #1906)\
*   Fix an issue where users could not launch sessions via Kubernetes or Slurm if they belonged to a group that was innumerable (Pro #1895)\
*   Fix an issue where users could not be added to shared projects when `auth-required-user-group` was set in some configurations (Pro #1944)\
*   Fix an issue where global replace gave unexpected results outside of a project (#7736)\
*   Fix an issue with session detection that could cause a failure to sign in when the authentication does not complete immediately (Pro #1104)\
\
1.3.1073-1[](https://docs.posit.co/ide/news/#rstudio-1.3.1073-1)\
\
-----------------------------------------------------------------\
\
**“Giant Goldenrod”** | Date: 2020-08-11\
\
This is a patch release of RStudio 1.3, consisting primarily of bugfixes and small improvements to RStudio 1.3.\
\
Misc - Compatible with R graphics engine version 13 (R 4.1.0+) (#7253) - Add support for configurable `rsandbox` path in Server Pro (Pro #1777) - Add support for running Slurm plugin in unprivileged Docker containers (Pro #1744)\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-8)\
\
*   Fix issue where files could not be uploaded when using RStudio Server load balancing (Pro #1751)\
*   Fix issue where the Crash Handler notification prompt would never go away (#7243)\
*   Fix issue with slow shutdown on Windows (#7117)\
*   Fix issue where Launcher debug logs could contain user’s plain text password (Pro #1687)\
*   Fix issue where some log entries could not be displayed on the admin logs page (Pro #1783)\
*   Fix “TypeError” when sign-in using IE11 (#7359)\
*   Fix issue where users belonging to more than 101 groups could not launch Kubernetes sessions (Pro #1796)\
*   Fix problem with moving Console between left and right columns (#7246)\
*   Fix issue with `rstudioapi::setCursorPosition()` not scrolling cursor into view (#7317)\
*   Fix issue with `rmarkdown` and `packrat` packages being eagerly loaded on IDE launch (#7265)\
*   Fix issue with folded chunk outputs getting stuck at top of IDE (#7293)\
*   Fix issue where Slurm Launcher jobs could not be started on systems with root squash configured for the user home directory (Pro #1775)\
*   Fix issue where locking an account would cause an infinite redirect loop on the sign-in page (Pro #1785, Pro #1764)\
*   Fix issue where Jupyter sessions could not be started when the home directory was a root squash mount (Pro #1795)\
*   Fix issue where large R objects in the environment pane could not be expanded (Pro #1799)\
*   Fix issue where Session Server settings for a saved server could not be modified (Pro #1824)\
\
1.3.1056-1[](https://docs.posit.co/ide/news/#rstudio-1.3.1056-1)\
\
-----------------------------------------------------------------\
\
**“Water Lily”** | Date: 2020-07-15\
\
This is a patch release of RStudio 1.3, consisting primarily of bugfixes and small improvements from the initial 1.3 stable release.\
\
Misc\
\
*   R 4.0.0’s raw string literals are now handled properly by the diagnostics engine. (#6788)\
*   Allow projects to reopen after a crash (#3220)\
*   Added spellcheck blacklist item for preview Latvian dictionary (#6594)\
*   Allow multiple space-separated domains in `www-frame-origin` for Tutorial API (Pro)\
*   Update `rstudioapi` highlightUi call to accept a callback variable containing an R script to be executed after the highlight element has been selected (#67565)\
*   Adds class attributed to RMarkdown chunks, their control buttons, and their output based on their given labels. (#6787)\
*   Add option `www-url-path-prefix` to force a path on auth cookies (Pro #1608)\
*   Add additional keyboard shortcut (Ctrl+\`) for Focus Console Output accessibility command (#6850)\
*   Always set application role for screen readers and removed related accessibility preference checkbox (#6863)\
*   Update `NOTICE` for Ace editor license (#7102)\
*   Removed requirement of password forwarding for PAM sessions when using Launcher sessions (Pro #1638)\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-9)\
\
*   Announce text of warnings bar via screen reader (#6963)\
*   Fix issue where projects using renv sometimes failed to load (#7077)\
*   Fix issue where attempts to create clusters via parallel package failed on macOS (#6692)\
*   Fix display issue with keyboard shortcut in Modify Keyboard Shortcuts dialog (#7142)\
*   Fix ‘truncating string with embedded nuls’ warning being emitted when saving R Notebook (#6932)\
*   Fix Compare Results and other incompatibility with newer versions of the `shinytest` package (#6960)\
*   Fix Terminal to work with both Git-Bash and RTools4 MSYS2 installed on Windows (#6696, #6809)\
*   Fix auto-activation of JAWS screen reader virtual cursor in Console Output region (#6884)\
*   Fix dependency installation for untitled buffers (#6762)\
*   Fix failure to open source files when debugging some functions in R 4.0.0 (work around R bug in `deparse()`) (#6854)\
*   Fix failure to use the first project template and default open files (#6865)\
*   Fix issue where R\_LIBS\_SITE could be forcibly set empty, overriding the value in /etc/R/REnviron (#6982)\
*   Fix keybinding failure when global keybindings exists but user keybindings don’t (#6870)\
*   Fixed Chromium issue when using RStudio Desktop on Linux systems with newer glibc (#6379)\
*   Fixed install issue where service scripts would not be created if there was no /lib/systemd path (Pro #6710)\
*   Fixed issue where an attempt to create more sessions than the license limit would fail with a generic error (Pro #1680)\
*   Fixed issue where users could not save files in home directory if specified by UNC path (#6598)\
*   Fixed issue where file upload would fail when the file already existed (#7015)\
*   Fix sign out from the Admin Dashboard when behind a path-rewriting proxy (Pro #1709)\
*   Fix “Login as user” from the Admin Dashboard when using Launcher sessions (Pro #1710)\
*   Fix issue with first esc keypress being ignored (#7045)\
*   Fix issue with spellcheck not working with realtime turned off (#7068)\
*   Fix error when some HTML comments are included in R Markdown documents (#6997)\
*   Fix issue where toolbar buttons were missing on initialization (#7076)\
*   Fix error in Viewer pane when previewing Distill blogs (#6945)\
*   Fix misalignment of some number cells in the data viewer (#6975)\
*   Fix C++ autocompletion results missing on macOS in some contexts (#7097)\
*   Fix misleading errors report for `verify-installation` without Launcher (Pro #1718)\
*   Fix Global Options failure to launch when missing secondary repositories (#7116)\
*   Send keyboard focus to the Source pane when creating new files (#7103)\
*   Fix failure to open HTML widgets from the Viewer in an external web browser on Windows with R >= 4.0.0 (#6893)\
*   Fix “cannot access the file” error with rstan when Viewer is open (#7046)\
*   Fix launching jobs from working directories with spaces on their names (Pro #1708)\
*   Update editor toolbar when R Markdown documents are switched to/from Notebook mode in YAML header (#7051)\
*   Fix error when invoking spell check manually on some languages (#7018)\
*   Fix RStudio Desktop Pro Job Launcher connections and path mappings (Pro #1726 and Pro #1727)\
*   Fix painting of Appearance pane in Global Options on RStudio Desktop (#6268)\
*   Fix `Alt+-` shortcut to insert assignment operator in R Markdown documents (#7169)\
*   Fix issue with duplicated signature tooltips in R Markdown documents (#7154)\
*   Fix issue with chunk toolbars not showing up in some cases (#7067)\
*   Fix RStudio Server Pro issue where R version modules would sometimes not be able to modify the PATH environment variable (Pro #1737)\
*   Fix dealing with expired sessions due to inactivity or signed out when using multiple browser tabs (Pro #1731, #7205)\
*   Fix dropdowns not repopulating after being closed via keyboard shortcut (#7215)\
*   Fix errors occurring during verify-installation command (#7221)\
\
RStudio Server Pro\
\
*   New option `server-project-sharing-root-dir` allows project sharing outside user home directories (Pro #1340)\
*   Update embedded nginx to 1.17.10\
\
1.3.959-1[](https://docs.posit.co/ide/news/#rstudio-1.3.959-1)\
\
---------------------------------------------------------------\
\
**“Middlemist Red”** | Date: 2020-05-22\
\
This is a major new release of RStudio which includes the following enhancements:\
\
*   Dramatically improved accessibility support, including support for screen readers, keyboard navigation improvements, focus indicators and contrast improvements, and more.\
*   Real-time spellchecking with customizable dictionaries and inline correction suggestions.\
*   Dozens of other productivity improvements, including auto-save, global search and replace, and Shiny background jobs.\
*   All preferences and settings are now saved centrally in plain text files, and can be set by admins and backed up by users.\
*   Compatibility with iPad OS 13 for RStudio Server.\
*   RStudio Desktop Pro can now function as a client for RStudio Server Pro; access your server’s compute power and environments with the convenience of a windowed desktop application.\
\
Accessibility\
\
*   Dramatically improved accessibility for sight-impaired users, including:\
*   Keyboard focus management and visibility upgrades\
*   Improved keyboard navigation\
*   Compatibility with popular screen readers\
*   Compliant contrast ratios and other accessibility improvements\
*   User preference for disabling user-interface animations such as when zooming panes\
\
Spell Check\
\
*   Real-time spell-checking engine for checking while editing\
*   Customizable dictionaries and word ignore lists preloaded with common R terms\
*   Inline correction suggestions\
\
Preferences and Configuration\
\
*   All user preferences and settings can now be set using a plain JSON file\
*   All user preferences can now have global defaults set by a system administrator\
*   New diagnostics commands for editing the prefs file, resetting state, and viewing pref system data\
*   Editor themes, snippets, file templates, and keybindings are now portable and can be installed by admins\
*   The content of new file templates (New R Script, New R Markdown, etc.) can now be controlled by users or administrators\
\
renv\
\
*   New projects can be initialized with renv, giving them an isolated project environment\
\
Server Security\
\
*   New auth-timeout-minutes option signs users out after a defined period of inactivity (Pro #667)\
*   CSRF hardening improvements including optional validation of the HTTP Origin header (Pro #1214)\
*   Add option auth-cookies-force-secure to always mark auth cookies as secure when SSL is terminated upstream (Pro #995)\
*   Set HTTP header X-Content-Type-Options to discourage MIME type sniffing (Pro #1219)\
*   Authentication cookies are now revoked after signout (Pro #606)\
*   File-serving resource endpoints can now be made more restrictive; added new restrict-directory-view and directory-view-whitelist options (Pro #607)\
*   RStudio Server now uses 2048 bit RSA keys, for secure communication of encrypted credentials between server / session and client\
\
iPad OS 13\
\
*   Improved keyboard and touch support for iPadOS 13.1\
*   Support Ctrl+\[ as Esc key on iPadOS 13.1 keyboards lacking physical Esc key (#4663)\
*   Add ability to resize panes using keyboard arrow keys via View / Panes / Adjust Splitter\
\
Terminal Improvements\
\
*   User preference to configure initial working directory of new terminals (#1557)\
*   Command to open a new terminal at location of current editor file\
*   Command to insert the full path and filename of current editor file into terminal\
*   Command in File pane to open a new terminal at File pane’s current location\
*   Command in to change terminal to current RStudio working directory (#2363)\
*   PowerShell Core option in terminal (Windows-only)\
*   Custom terminal shell option for Windows desktop (previously only on Mac, Linux, and server)\
*   Change shortcuts for Next/Previous terminal to avoid clash with common Windows shortcuts (#4892)\
*   Suppress macOS Catalina message about switching to zsh in Terminal pane (#6182)\
*   Add ‘Close All Terminals’ command to Terminal menu (#3564)\
*   Zsh option in terminal for Mac and Linux desktop, and RStudio Server (#5587)\
\
Diagnostics and Recovery\
\
*   Add automated crash handling and reporting\
*   Show detailed logs and process output when R fails to start (#2097)\
*   Add “Safe Mode” for opening sessions without profile scripts or workspace restoration (#4338)\
\
Tutorials\
\
*   Support for tutorials with the learnr package in a new Tutorials pane\
\
Background Jobs\
\
*   Add support for running Shiny applications as background jobs (#5190)\
*   Install missing package dependencies in a background job (#5584)\
\
Auto Save\
\
*   Changes automatically (and optionally) saved to disk after a few seconds or when editor loses focus (#5263)\
*   Option to disable real-time backup of unsaved changes to avoid conflicts with Google Drive, Dropbox, etc. (#3837)\
*   Option to adjust idle interval for backup or saving changes\
\
Miscellaneous\
\
*   Add global replace with live preview and regular expression support (#2066)\
*   Enable large file uploads (over 4GB) in RStudio Server (#3299)\
*   Improved ‘Comment / Uncomment’ handling of empty lines around selection (#4163)\
*   Files with extension ‘.q’ are no longer indexed or parsed as R files (#4696)\
*   Add support for an API command to return the list of R packages RStudio depends on (#2332)\
*   Upgrade internal JSON parsing engine for speed improvements (#1830)\
*   Improved ergonomics for history prefix navigation (#2771)\
*   Make columns resizable in the Environment pane (#4020)\
*   Add Word Count command (#4237)\
*   Keyboard shortcuts for main menu items on RStudio Server (e.g. Ctrl+Alt+F for File menu)\
*   Show number of characters when entering version control commit messages (#5192)\
*   Update embedded Qt to 5.12.5 for Chromium update, stability and bugfixes (#5399)\
*   Add preference for changing font size on help pane (#3282)\
*   Warn when Xcode license has not been agreed to on macOS when command line tools required (#5481)\
*   Improved browser tab names (project name first, complete product name) (Pro #1172)\
*   The diagnostics system now understands referenced symbols in glue strings (#5270)\
*   Add preference for compiling .tex files with tinytex (#2788)\
*   Long menus and popups now scroll instead of overflowing (#1760, #1794, #2330)\
*   Sort package-installed R Markdown templates alphabetically (#4929)\
*   The ‘Reopen with Encoding’ command now saves unsaved changes before re-opening the document. (#5630)\
*   Autocomplete support for Plumber #\* comment keywords (#2220)\
*   Automatically continue Plumber #\* on successive lines (#2219)\
*   Comment / uncomment is now enabled for YAML documents (#3317)\
*   Reflow comment has been rebound to ‘Ctrl + Shift + /’ on macOS. (#2443)\
*   Allow fuzzy matches in help topic search (#3316)\
*   The diagnostics system better handles missing expressions (#5660)\
*   Keyboard shortcuts for debugging commands can be customized (#3539)\
*   Update Pandoc to 2.7.3 (#4512)\
*   Update SumatraPDF to version 3.1.2 (#3155)\
*   Allow previewing PDFs in fullscreen mode in Sumatra PDF (#4301)\
*   RStudio Server runtime files are stored in /var/run, or another configurable location, instead of /tmp (#4666)\
*   Errors encountered when attempting to find Rtools installations are handled more gracefully (#5720)\
*   Enable copying images to the clipboard from the Plots pane (#3142)\
*   Update minimum supported browser versions (#5593)\
*   Automatic refresh of the Git pane can now be enabled / disabled as required. (#4368)\
*   Target directory can be changed from within the ‘Upload Files’ dialog (RStudio Server)\
*   Zoom Left/Right Column commands for keyboard users (#5874)\
*   Increase maximum plot size for large, high-DPI displays (#4968; thanks to Jan Gleixner)\
*   Make maximum lines in R console configurable; was previously fixed at 1000 (#5919)\
*   Option to only show project name instead of full path in desktop window title (#1817)\
*   New rstudio –version command to return the version of RStudio Desktop (#3922)\
*   Scan R Markdown YAML header for R packages required to render document (#4779)\
*   Support use of F13 - F24 for custom keyboard shortcuts (full Mac keyboard has F13-F19, for example)\
*   Keyboard shortcuts for searching R help in Help pane, and next/previous help page (#5149)\
*   Keep keyboard focus in the console during debugging (#6039)\
*   Enable wrap-around for previous/next source tab by default (#6139)\
*   Provide full SHA in detail of Git commits (#6155)\
*   File monitor now ignores Packrat, renv library folders (#3267)\
*   Make global source control commands rebindable (#6503)\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-10)\
\
*   Fix issue where calling install.packages() without arguments would fail (#5154)\
*   Fix issue where C code in packages would incorrectly be diagnosed as C++ (#5418)\
*   Fix plot history when plot() called immediately after dev.off() (#3117)\
*   Fix debug stopping past breakpoint when source windows are open (#3683)\
*   Fix diagnostics error with multibyte characters in R Markdown documents on Windows (#1866)\
*   Fix stale processes when invoking child R processes with large command lines (#3414)\
*   Fix an issue where help tooltips could become corrupt when using prettycode (#5561)\
*   Fix an issue where signature tooltips were shown even when disabled by user preference (#5405)\
*   Fix an issue where Git did not work within projects whose paths contained multibyte characters (#2194)\
*   Fix an issue where RStudio would fail to preview self-contained bookdown books (#5371)\
*   Fix modal dialog boundaries extending out of the app window in certain cases (#1605)\
*   Fix issue where session restore could fail when using multiple user libraries\
*   Fix issue where library paths were not forwarded when building package documentation\
*   Restore ability to select and copy text in version control diffs (#4734)\
*   Fix incorrect column names when non-dataframes with a column named x were viewed (#3304)\
*   Fix inconsistent shading in R Markdown chunk backgrounds with folding (#2992)\
*   Fix list column display in columns past 50 with data viewer (#5851)\
*   Fix incorrect column type display when paging columns (#5479)\
*   Fix incorrect sorting in data viewer when paging columns (#4682)\
*   Fix carryover of light ANSI background colors (#6092)\
*   Fix issue where Shiny applications using reticulate on Windows could crash on run (#6140)\
*   Fix issue where pasting text into last chunk in document could occasionally cause hang (#6226)\
*   Fix blank Viewer Pane when displaying most HTML widgets with R 4.0.0 (#6737)\
\
RStudio Professional\
\
*   Logging improvements; log destinations and levels are more configurable and can be changed in real time\
*   RStudio Desktop Pro can now function as a client for RStudio Server Pro\
*   New tools for viewing and managing server users when using named user licensing\
*   Floating licensing can now pass through an HTTPS proxy\
*   The Launcher service now starts and runs automatically when the system starts\
*   New Kubernetes Launcher plugin feature to modify the generated job/pod specs (#1353)\
*   When containers are created when running RStudio Launcher sessions, user home directories are propagated to the container instead of requiring the home directories to be mounted at /home. This is a potentially breaking change, and will requiring updating the /etc/rstudio/laucher-mounts file to mount the home directory to the correct location (#1369)\
*   New Kubernetes Launcher plugin feature to allow the specification of a requests limit to allow for oversubscription of Kubernetes resources (#1360)\
*   Slurm Launcher plugin will now generate jobs with much shorter names (#1595)\
\
Acknowledgments\
\
*   Thanks to Dr Jonathan Godfrey (Massey University, New Zealand), and to JooYoung Seo (https://www.jooyoungseo.com/) for their valuable insights on improving screen reader support in RStudio 1.3.\
\
1.2.5042-1[](https://docs.posit.co/ide/news/#rstudio-1.2.5042-1)\
\
-----------------------------------------------------------------\
\
**“Double Marigold”** | Date: 2020-04-13 | [Release Blog Post](https://posit.co/blog/rstudio-1-2-release/)\
\
This is a maintenance release of RStudio containing small bugfixes and functionality enhancements.\
\
Misc\
\
*   Fix a crash when debugging with R 4.0+ (#5888)\
\
Server Pro\
\
*   Fix a crash in rserver that sometimes occurs when a port proxy request fails to connect (#1361)\
*   Fix a display issue for configured Launcher session limits (#1167)\
*   Fix inability to select R version in Global Options and elsewhere (#1470)\
*   Fix failure to start R sessions when multiple values are present in `www-frame-origin` (#1529)\
\
1.2.5033-1[](https://docs.posit.co/ide/news/#rstudio-1.2.5033-1)\
\
-----------------------------------------------------------------\
\
**“Orange Blossom”** | Date: 2019-12-17\
\
Misc\
\
*   Add compatibility with recent versions of the `shinytest` package (#5677, #5703)\
*   Eliminate warnings when using `_R_CHECK_LENGTH_1_CONDITION_` (#5268, #5363)\
*   Ensure compatibility with Boost 1.72.0 (#5742)\
*   Set Server Name Indication (SNI) on outbound HTTPS requests for compatibility with TLS 1.3 (#5757)\
*   Session configuration option to customize environment variables saved when session suspends (#5769)\
\
Server Pro\
\
*   Add ability to configure Slurm command line tools location for the Slurm Launcher Plugin (#1298)\
*   Fix an issue where the Slurm service user must have a home directory for the Slurm Launcher Plugin (#1286)\
*   Fix an issue where errors are ignored when validating the version of Slurm for the Slurm Launcher Plugin (#1287)\
*   Add documentation for load balancing limitations, module support, and support for multiple versions of R with the Slurm Launcher Plugin (#1296)\
\
1.2.5019-6[](https://docs.posit.co/ide/news/#rstudio-1.2.5019-6)\
\
-----------------------------------------------------------------\
\
**“Elderflower”** | Date: 2019-11-01\
\
Misc\
\
*   Fully reset Connections pane objects when refreshing (#2136)\
*   Fix incorrect `memory.limit()` result with R >= 3.6.0 (#4986)\
*   Unset `DYLD_INSERT_LIBRARIES` after launch on macOS to prevent spurious library load errors (#5313)\
*   Include R/RStudio version in HTTP user agent header when installing required packages (#5369)\
*   Eliminate warnings when using `_R_CHECK_LENGTH_1_LOGIC2_` (#5268, #5363)\
*   Truncate console output in notebooks to avoid hang with long outputs (#5518)\
*   Fix plain serif/sans-serif font rendering on macOS Catalina (#5525)\
*   Restore First Project Template feature (Pro #1267)\
\
Server Pro\
\
*   Include Job Launcher logs in diagnostics report (#1262)\
*   Add ability to specify multiple R versions with same path but differing labels (#1034)\
*   Include child processes and timing information in session diagnostic traces (#1192)\
*   Adds better Session UI/UX including sorting, label viewing, and creation visibility (#1215)\
*   Respect user profile resource limits for local launcher R sessions (#1269)\
\
1.2.5001-3[](https://docs.posit.co/ide/news/#rstudio-1.2.5001-3)\
\
-----------------------------------------------------------------\
\
> Date: 2019-09-19\
\
RStudio Server Pro\
\
*   New Slurm plugin for the Job Launcher enables running R sessions and jobs on Slurm clusters\
*   Support for starting and managing Jupyter sessions alongside R sessions\
*   Overhaul of user dashboard for managing R sessions, Jupyter sessions, and jobs\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-11)\
\
*   Restore capability to use 32-bit R on Windows (#3150)\
*   Fix pane configuration being reset after customization (#2101)\
*   Fix issue where middle click failed to close editor tabs (#4379)\
*   Fix incorrect application of C++ project compilation options to non-project files (#4404)\
*   Fix issues on MacOS with command line tool headers when ‘/usr/include’ is missing (#4405)\
*   Fix failure to start on R 3.6.0 when the error option is set in `.Rprofile` (#4441)\
*   Fix issue where attempts to run R debugger in `.Rprofile` could hang RStudio (#4443)\
*   Fix parsing multi-line expressions with single brackets inside strings (#4452)\
*   Improve detection of remote sessions on Windows (#4466)\
*   Fix issue where text in prompts would fail to display on macOS Mojave (#4497)\
*   Fix “Reload App” button for Shiny applications in Firefox on RStudio Server (#4552)\
*   Fix issue where themes without names would not use the file name as a name instead (#4553)\
*   Fix NULL in code preview on first attempt to import data (#4563)\
*   Prompt for permissions on macOS Mojave when R packages require them (#4579)\
*   Add explicit dependency on required `libxkbcommon` package on Linux (#4610)\
*   Fixed inability to execute editor commands from menu in RStudio Server (#4622)\
*   Remove unnecessary dependency on `rprojroot` package (#4628)\
*   Fix failure to launch RStudio Desktop when started as root user (#4631)\
*   Fixed an issue where the Files pane occasionally would fail to scroll to bottom (#4662)\
*   Fixed an issue where RStudio would always use the discrete GPU on macOS (#4672)\
*   Fix startup failure when using multiple CRAN repos (#4751)\
*   Fix console display issue with certain mixed color output patterns (#4777)\
\
Miscellaneous\
\
*   Improve detection of current working directory for terminals on macOS (#4570)\
*   Update to Pandoc 2.7.2 on Windows to address occasional segfaults (#4618)\
*   Qt support libraries for Wayland are now bundled on Linux (#4686)\
*   Set secure flag when clearing cookies for consistency (Pro #964)\
\
1.2.1335-1[](https://docs.posit.co/ide/news/#rstudio-1.2.1335-1)\
\
-----------------------------------------------------------------\
\
> Date: 2019-04-08\
\
Python and Notebooks\
\
*   Use a shared Python session to execute Python chunks via reticulate\
*   Simple bindings to access R objects from Python chunks and vice versa\
*   Show matplotlib plots emitted by Python chunks\
\
Keyring\
\
*   Store passwords and secrets securely with keyring by calling rstudioapi::askForSecret()\
*   Install keyring directly from dialog prompt\
\
D3\
\
*   Author D3 visualizations in RStudio and preview in the Viewer pane\
*   Use r2d3 D3 visualizations in R Notebook chunks\
\
Jobs\
\
*   Run any R script as a background job in a clean R session\
*   Monitor progress and see script output in real time\
*   Optionally give jobs your global environment when started, and export values back when complete\
\
SQL\
\
*   Author SQL queries in RStudio and preview in the SQL Results pane\
\
Testing\
\
*   Run Tests command in testthat R scripts for direct running\
*   testthat output in the Build pane with navigable issue list\
*   Integration with shinytest to record and run Shiny app tests\
\
PowerPoint\
\
*   Create PowerPoint presentations with R Markdown\
\
Package Management\
\
*   Specify a primary CRAN URL and secondary CRAN repos from the package preferences pane.\
*   Link to a package’s primary CRAN page from the packages pane.\
*   Configure CRAN repos with a repos.conf configuration file and the r-cran-repos-file option.\
*   Suggest additional secondary CRAN repos with the r-cran-repos-url option.\
\
Plumber\
\
*   Create Plumber APIs in RStudio\
*   Execute Plumber APIs within RStudio to view Swagger documentation and make test calls to the APIs\
*   Publish Plumber APIs to RStudio Connect\
\
Miscellaneous\
\
*   Git ‘Create Branch’ dialog defaults to remote associated w/current branch (if any)\
*   Added link to purrr cheatsheet (in Help) and link to browse all cheatsheets\
*   Added option to temporarily disable environment pane refreshing\
*   Improve NSE detection for dplyr (better understands S3 dispatch and idioms)\
*   Add ability to search for displayed database objects in Connections tab (#1549)\
*   Add button to open profiler output in an external browser (#1657)\
*   Add option to show the R Markdown render command used when knitting (#1658)\
*   Add option to show hidden files in the Files pane (#1769)\
*   Upgrade embedded Pandoc to 2.2.1 (#1807)\
*   Allow renames that change only file case on Windows (#1886)\
*   Remember scroll position when navigating in Help pane (#1947)\
*   Show warning when attempting to edit a generated file (#2082)\
*   Allow opening .ini files with file.edit (#2116)\
*   Add shinymod snippet for Shiny modules (#2078)\
*   Allow changing zoom level without reloading (#2125)\
*   New command ‘Pull with Rebase’ to pull and rebase a branch in a single step (#2151)\
*   Click on promises in the Environment pane now calls force on the promise\
*   Add Rename command to File menu for quick rename of current file (#2199)\
*   Numeric filtering in data viewer shows value distribution and supports user-entered values (#2230)\
*   Improved support for custom knitr engines in R Notebooks (#2401)\
*   Add support for viewing external web URLs in the Viewer pane (#2252)\
*   Add option to disable drag-and-drop for text in the editor (#2428)\
*   Add option to disable cursor save/load; improves performance on some Windows machines (#2778)\
*   R startup files (e.g. .Rprofile) are now always saved with trailing newlines (#3029)\
*   Update embedded libclang to 5.0.2 (Windows only)\
*   RStudio now a 64-bit application on Windows (Linux and Mac are already 64-bit)\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-12)\
\
*   Fix “Invalid byte sequence” when spell checking\
*   Fix incorrect Git status pane display when git detects that a file has been copied\
*   Fix hang when submitting empty passwords and password encryption is turned off (#1545)\
*   Fix HTTP 500 error when navigating to directories such as /js/ (#1561)\
*   Fix issue where Build pane would get ‘stuck’ on failed Rcpp::compileAttributes() call (#1601)\
*   Fix low/no-contrast colors with HTML widgets in notebooks with a dark theme (#1615)\
*   Fix invalid YAML in some cases when changing R Markdown output type via dialog (#1609)\
*   Fix error when quitting while a function named q() is present (#1647)\
*   Fix crash when executing multiple R Notebook chunks with a failing Rcpp chunk (#1668)\
*   Fix missing blank lines in code chunks in R Notebook preview (#1556)\
*   Fix selection in Files pane when files are modified while checked (#1715)\
*   Fix incorrect truncation of some R object descriptions in Environment pane (#1703)\
*   Fix duplicate prompts in each window when using RStudio API showPrompt (#1706)\
*   Fix proxy timeouts with the websocket used for the Terminal, via keepalive messages (#1860)\
*   Fix file.edit failures with Chinese filenames on Windows (#1868)\
*   Fix errors when importing non-ASCII filenames in base Import Dataset (#1910)\
*   Fix rserver crash that can occur when proxying websockets to Shiny apps (#2061)\
*   Fix hang on some Linux systems caused by X11 clipboard monitoring w/ option to disable monitoring (#2068)\
*   Fix empty column titles when viewing matrices without column names (#2086)\
*   Fix error when pressing F1 on non-function autocomplete results (#2127)\
*   Fix hang when autocompleting filenames in large directories (#2236)\
*   Fix inability to copy content from Viewer pane and data viewer in IE11 (#2351)\
*   Fix errant addition of msys-ssh to path on non-Windows platforms (#2352)\
*   Fix buggy behavior with when ANSI colors are present (#2387)\
*   Fix external process slowness (git, etc.) when open file limit RLIMIT\_NOFILE is high (#2470)\
*   Fix issue caused by resolving symlinks when choosing Git path (#2476)\
*   Fix display of consecutive spaces in the Data Viewer (#2499)\
*   Fix issue where ‘#’ in YAML strings would be highlighted as comments (#2591)\
*   Fix over-eager loading of yaml package when IDE starts up (#2602)\
*   Fix issue on Windows with R dialogs showing behind RStudio window (#2901)\
*   Fix incorrect insertion of mousewheel handler into HTML widget JavaScript (#2634)\
*   Fix unresponsive buttons in Connections pane when connection deletion is cancelled (#2644)\
*   Fix RStudio hang when installing packages (e.g. BH) in Packrat projects on Windows (#1864)\
\
RStudio Server Pro\
\
*   Overhauled R versions, allowing you to specify version labels, load environment modules, and execute a prelaunch script when loading specific versions.\
*   New rsession-diagnostics-enabled option for rserver.conf to enable session launch diagnostics mode to help diagnose session launch failures.\
*   Added support for auth-pam-sessions-use-password option in a load balanced setup.\
*   Added ability to suspend sessions from user home page.\
*   Added hmac signature verification for proxy auth mode with new auth-proxy-require-hmac option in rserver.conf.\
*   Add nodes to RStudio Server Pro load-balanced clusters without service interruptions.\
\
RStudio Pro Drivers\
\
*   Discover, install and uninstall RStudio Pro Drivers from the New Connection wizard.\
\
1.1.463[](https://docs.posit.co/ide/news/#rstudio-1.1.463)\
\
-----------------------------------------------------------\
\
> Date: 2018-10-18\
\
This is a maintenance release of RStudio which contains fixes for the following issues:\
\
*   Fix sign-out issue when “stay signed in” is checked in RStudio Server ([#1538](https://www.github.com/rstudio/rstudio/issues/1538)\
    )\
*   Fix hang when submitting empty passwords and password encryption is turned off ([#1545](https://www.github.com/rstudio/rstudio/issues/1545)\
    )\
*   Fix dark theme partial application in data viewer when upgrading from 1.0 ([#1573](https://www.github.com/rstudio/rstudio/issues/1573)\
    )\
*   Fix overlap between Refresh icon and plot title text ([#1585](https://www.github.com/rstudio/rstudio/issues/1585)\
    )\
*   Fix slow File Open dialog on RStudio Desktop for Linux ([#1587](https://www.github.com/rstudio/rstudio/issues/1587)\
    )\
*   Fix slow open of new files on Windows when using network drives ([#1592](https://www.github.com/rstudio/rstudio/issues/1592)\
    )\
*   Fix build pane freeze when Rcpp::compileAttributes results in parse errors ([#1601](https://www.github.com/rstudio/rstudio/issues/1601)\
    )\
*   Fix issue when migrating from RStudio 1.0 which could result in empty R files ([#1623](https://www.github.com/rstudio/rstudio/issues/1623)\
    )\
*   Fix incorrect output type when compiling R script to non-HTML report ([#1631](https://www.github.com/rstudio/rstudio/issues/1631)\
    )\
*   Improve spacing in account when username and servername are short ([#1637](https://www.github.com/rstudio/rstudio/issues/1637)\
    )\
*   Fix incorrect background highlighting after reindent ([#1643](https://www.github.com/rstudio/rstudio/issues/1643)\
    )\
*   Fix autocompletion of Rcpp C++ objects ([#1654](https://www.github.com/rstudio/rstudio/issues/1654)\
    )\
*   Better “hand” cursor position on RStudio Desktop for Linux ([#1659](https://www.github.com/rstudio/rstudio/issues/1659)\
    )\
*   Fix segfault that can occur when a notebook contains a Rcpp chunk with compilation failures ([#1668](https://www.github.com/rstudio/rstudio/issues/1668)\
    )\
*   Fix problems with Git for Windows installations into sub-directories of home directory ([#1679](https://www.github.com/rstudio/rstudio/issues/1679)\
    )\
*   Fix crashes when restarting R session while using a network drive ([#1690](https://www.github.com/rstudio/rstudio/issues/1690)\
    )\
*   Don’t suspend R sessions with active external pointer objects ([#1696](https://www.github.com/rstudio/rstudio/issues/1696)\
    )\
*   Allow new “Copy To” command in Files Pane to overwite its target ([#1722](https://www.github.com/rstudio/rstudio/issues/1722)\
    )\
*   Respect “Load All” command shortcut when the Terminal is open ([#1723](https://www.github.com/rstudio/rstudio/issues/1723)\
    )\
*   Detect full-screen mode correctly in Terminal pane ([#1725](https://www.github.com/rstudio/rstudio/issues/1725)\
    )\
*   Support Pandoc 2 in RSTUDIO\_PANDOC ([#1756](https://www.github.com/rstudio/rstudio/issues/1756)\
    )\
*   Allow installation of package dependencies from repos not named CRAN ([#1762](https://www.github.com/rstudio/rstudio/issues/1762)\
    )\
*   Fix password entry in Subversion and other shell dialogs ([#1810](https://www.github.com/rstudio/rstudio/issues/1810)\
    )\
*   Ensure R Markdown files are saved before publish ([#1821](https://www.github.com/rstudio/rstudio/issues/1821)\
    )\
*   Reconnect terminal when disconnected via proxy timeout ([#1844](https://www.github.com/rstudio/rstudio/issues/1844)\
    )\
*   Closing Shiny apps no longer can crash RStudio Server ([#2061](https://www.github.com/rstudio/rstudio/issues/2061)\
    )\
*   Avoid hang when .git folder own Windows is not hidden ([#2141](https://www.github.com/rstudio/rstudio/issues/2141)\
    )\
*   Setting non-default Knit Directory no longer breaks R Markdown websites ([#2158](https://www.github.com/rstudio/rstudio/issues/2158)\
    )\
*   Fix scrolling through database objects if there are more than 25 ([#2211](https://www.github.com/rstudio/rstudio/issues/2211)\
    )\
*   Pressing F1 on help autocompletions no longer raises an error ([#2261](https://www.github.com/rstudio/rstudio/issues/2261)\
    )\
*   RTools 3.5 compatibility ([#2636](https://www.github.com/rstudio/rstudio/issues/2636)\
    )\
*   R Notebook compatibility with R 3.5 ([#2748](https://www.github.com/rstudio/rstudio/issues/2748)\
    )\
*   Fix issues with RStudio bundled with Anaconda in Windows 10 build 1803+ ([#2802](https://github.com/rstudio/rstudio/issues/2802)\
    )\
*   Fix disconnects with latest version of Shiny, RStudio Server, and Firefox ([#2940](https://github.com/rstudio/rstudio/issues/2940)\
    )\
*   Fix paged table output R Notebooks with R 3.5.1 ([#3163](https://github.com/rstudio/rstudio/issues/3163)\
    )\
*   Fix republishing content from directories with very short names ([#3168](https://github.com/rstudio/rstudio/issues/3168)\
    )\
*   Server Pro: Update embedded nginx to 1.14.0\
*   Server Pro: Can now log in to load-balanced servers when password contains a space (Pro #338)\
\
1.1.383[](https://docs.posit.co/ide/news/#rstudio-1.1.383)\
\
-----------------------------------------------------------\
\
DATE: 2017-10-09 | [Release Blog Post](https://posit.co/blog/rstudio-v1-1-release/)\
\
Connections\
\
*   New Connections tab for working with a wide variety of data sources\
*   Connections to data sources are saved and can be easily reconnected and reused\
*   Objects inside data sources can be browsed and contents viewed inside RStudio\
*   Works with ODBC data sources and Spark, and can integrate with other R packages\
\
Terminal\
\
*   New Terminal tab for fluid shell interaction within the IDE\
*   Support for xterm emulation including color output and full-screen console apps\
*   Support for multiple terminals, each with persistent scrollback buffer\
*   Web links in terminal can be clicked and opened in default browser (new tab for server)\
*   Windows terminal supports multiple terminal shell types\
    *   Git Bash, if installed\
    *   Command Prompt (cmd.exe), 32-bit and 64-bit depending on OS support\
    *   PowerShell, 32-bit and 64-bit depending on OS support\
    *   Bash on Windows Subsystem for Linux, if installed on 64-bit Windows 10\
*   Default Windows terminal shell type set in new Global Options/Terminal preferences pane\
\
Object Explorer\
\
*   New view for the exploration of hierarchical / deeply-nested R objects\
*   Can recursively inspect R lists, environments, functions, S4 objects\
*   Integration with the xml2 package for exploration of XML documents\
*   Generate R code that can be used to access a particular item within object\
\
Themes\
\
*   New flat, modern UI theme\
*   New dark theme option\
*   Retina-quality icons throughout\
\
Data Import\
\
*   Add support for all file encodings supported by R\
*   Restore text import dialog from previous releases (uses only base R functions)\
*   Code generator in import dialog now creates a relative path to data file\
\
R Markdown\
\
*   Added option to specify the working directory when executing R Markdown chunks\
*   Added option to set preview mode (in viewer, window, etc.) in YAML header\
*   Added option to skip knitting before publishing in YAML header\
*   Multiline strings in YAML header are now properly highlighted\
\
R Notebooks\
\
*   Python chunks now respect virtualenv if present\
*   ‘Rename in Scope’ now works within R chunks\
*   Global chunk options (e.g. ‘echo’) now properly respected in Notebook mode\
*   Fixed an issue where non-R chunk output could become duplicated\
*   Added option to set notebook mode in the document’s YAML header\
*   Allow setting default chunk connection option to raw connection object\
*   Added an ‘Use paged tables’ checkbox under chunk options popup\
\
Git Integration\
\
*   Add support for creating new Git branches and setting upstream remotes\
*   Git branch list is now searchable\
*   RStudio warns when attempting to commit large files (>10 MB)\
*   Implemented ‘ignore whitespace’ option for Git Diff view\
*   Wait for index.lock file to clear before performing git operations (with recovery)\
*   Improve handling of paths containing special characters\
\
Miscellaneous\
\
*   ANSI escape code support in console for colored output\
*   Add support for custom, user-provided [project templates](https://rstudio.github.io/rstudio-extensions/rstudio_project_templates.html)\
    \
*   Add support for middle-click pasting using X11 global selection (Linux Desktop only)\
*   Document cursor position is now saved and restored between RStudio sessions\
*   Addins are now fully searchable in dropdown toolbar menu\
*   Add support for changing editor tabs with the mouse wheel\
*   Snippets can now be inserted in the R console\
*   Add option to knit in current working directory or project directory\
*   Cmd/Ctrl+Enter in Help pane now sends selected example code to console\
*   View(vignette(…)) now opens editor with vignette source\
*   Ctrl+P/Ctrl+N to visit previous/next console history line (like readline)\
*   Ctrl+R to search console history incrementally (like readline)\
*   New “Copy To” command in Files pane to copy and rename in one step\
*   Added UI for loading ‘.rds’ files when clicked in Files pane\
*   F2 in source editor opens data frame under cursor in a new tab\
*   Highlight markdown inside ROxygen comments\
*   Minor fixes to C++ syntax highlighting\
*   Added syntax highlighting for TOML files\
*   Provide autocompletion support for R6 ‘new()’ methods\
*   Improve performance of autocompletion for installed packages\
*   Add option to run multiple consecutive lines of R with Ctrl+Enter\
*   Add commands to run a line, statement, or consecutive lines\
*   Add Clear Console button to top of Console pane\
*   Add option to wrap around when navigating to previous or next editor tab\
*   Allow opening directories as projects (Server and macOS only)\
*   Vim: Use \]f and \[f to open adjacent files on the file system\
*   Show disambiguation in overflow list when two editor tabs have the same filename\
*   Respect control characters in error output; makes e.g. curl output correct\
*   Add new cheatsheet links to Help: Data Import, Interfacing Spark\
*   macOS: Always show project label on dock tiles\
*   Remove 100 column limit in data viewer\
*   Make columns in data viewer resizable\
*   Add option to kill child processes when session exits\
*   Upgrade to [pandoc](http://pandoc.org/)\
     1.19.2.1\
*   Remove Packrat package sync notifications; replace with Check Library Status command\
*   Add support for ligature coding fonts in RStudio Desktop for Windows and Linux\
*   Added page viewer (accessible via getOption(“page\_viewer”)) for viewing web content in an external window.\
*   Add editor theme Dracula (thanks to [Fabian Mundt](https://github.com/inventionate)\
    )\
*   Server Pro: Add option to disable file uploads\
*   Server Pro: Upgrade to TurboActivate 4.0; improves licensing\
*   Server Pro: Add support for floating (lease-based) licenses\
*   Server Pro: Show the size of suspended sessions\
*   Server Pro: Add user-defined session labels\
*   Server Pro: Upgrade to nginx 1.12.0\
*   Server Pro: Add support for NFSv4 Access Control Lists in Project Sharing\
*   Server Pro: Add support for user-initiated session quit and force-terminate\
*   Server Pro: Add support for admin-supplied notifications in R sessions\
*   Server Pro: New session-timeout-kill-hours option to expire and cleanly remove old R sessions\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-13)\
\
*   Fixed an issue where dragging tabs out multiple times could revert contents to older version\
*   macOS: fixed ‘crash on wake’ issue with late-2016 Macbooks\
*   Fixed mangling of YAML header string values containing backticks\
*   Fixed mangling of YAML indentation when re-indenting R Markdown documents\
*   File downloads from the internal browser are now saved correctly on Linux and Windows\
*   Rendering or running an R Markdown document no longer saves it unnecessarily\
*   ‘Insert assignment operator’ shortcut now works on Firefox\
*   Fixed issue where ‘execute current statement’ behaved poorly with unclosed statements\
*   Fixed issue where tibble warnings could be emitted by autocompletion engine\
*   Fixed issue where ‘Copy Plot to Clipboard’ from Viewer failed with macOS Sierra\
*   Fixed issue where keybinding changes were not reflected in popped-out windows\
*   Fix hang when replacing a misspelled word with word and punctuation\
*   Fixed issue where cursor would begin blinking even when ‘Blinking Cursor’ preference disabled\
*   Editor now responds correctly when renaming an open file using the Files pane\
*   Fixed an issue that could cause the data viewer cache to contain orphaned entries\
*   Fixed highlighting of Markdown text within Markdown blockquote\
*   Invoke R without –vanilla when building R Markdown websites\
*   Fixed an issue in which R Markdown documents could get stuck in notebook mode\
*   Fixed an issue preventing plain .md files from being published if not rendered\
*   Fixed runtime crashes in R packages that use Boost libraries\
*   Fixed startup crashes associated with Boost regular expressions\
*   Fixed an issue where scroll position in History pane could be lost when losing focus\
*   Fixed an issue where RStudio would fail to discover build tools if R was not on PATH\
*   Improve stability of crashed session recovery system\
*   Fixed issues arising from restoring a session suspended with a different R version\
*   Color errors in the R console correctly when resuming a session\
*   Fixed an issue in which notebook tables would not print data with lists of lists\
*   Fix session crash that can occur with certain malformed chunk headers\
*   Fix issue preventing New Session from working on Ubuntu 16+\
*   Server Pro: Fix issue with dirty indicator/saving after collaborative editing ends\
*   Server Pro: Fix issue with using multiple R versions feature when multi-session is off\
\
1.0.153[](https://docs.posit.co/ide/news/#rstudio-1.0.153)\
\
-----------------------------------------------------------\
\
> Date: 2017-07-20\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-14)\
\
*   Fix for crashes in Pandoc on Ubuntu 16\
*   Fix inability to open some text file types on macOS High Sierra beta\
*   Fix missing output/issues pillbox on Windows Compile PDF output\
*   Fix superflous warnings in install.packages\
*   Fix blank data viewer issue affecting some Windows users\
\
Miscellaneous - Show Python error stack traces (using reticulate) - Add .registration=TRUE to useDynLib when Rcpp >= 0.12.11 - New binary release for users running Ubuntu 16+ and Debian 9+\
\
1.0.143[](https://docs.posit.co/ide/news/#rstudio-1.0.143)\
\
-----------------------------------------------------------\
\
> Date: 2017-04-19\
\
R 3.4 Support\
\
*   Support for debugging code in R 3.4.0\
*   Support for graphical output in R 3.4.0\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-15)\
\
*   Fix bug in macOS 10.12.4 with input of extended characters\
*   Fix bug causing R Notebook chunk temporary folder errors\
*   Fix scroll jump when clicking on the Console pane in newer versions of Chrome\
*   Fix errors when printing data frames containing dates\
*   Server Pro: Fix issue with collaborative editing when owner’s session is suspended\
\
Miscellaneous\
\
*   Environment pane support for [reticulate](https://cran.r-project.org/web/packages/reticulate/index.html)\
     objects\
\
1.0.136[](https://docs.posit.co/ide/news/#rstudio-1.0.136)\
\
-----------------------------------------------------------\
\
> Date: 2016-12-21\
\
R Notebooks\
\
*   Improved sizing of htmlwidgets in R Notebooks\
*   Allow changing to R Notebook mode without closing and reopening the file\
*   Add support for knitr code chunks defined in external .R files\
*   Add support for raw relative paths such as “..” in knitr root.dir option\
*   Add support for ‘output.var’ chunk option for Stan chunks\
*   Improve scrolling past htmlwidgets in the editor\
*   Always show chunk output preferences (inline or console)\
*   Add support for variable height HTML widgets (non-knitr figures)\
*   Improve support for non-ASCII characters in chunk metadata and output\
*   Add support for JavaScript and CSS chunks\
\
Data Import\
\
*   Add support for all readr locale settings (date/time format, decimal, etc.)\
*   Prompt for a comma-separated list of factors instead of a collection\
\
Miscellaneous\
\
*   Add Ctrl+Tab / Ctrl+Shift+Tab shortcuts to navigate tabs (Desktop only)\
*   Include .scala files in fuzzy file finder (Ctrl + .)\
*   Add support for pre-rendered Shiny documents (shiny\_prerendered)\
*   Update Stan editor mode to support Stan 2.12.0\
*   Server Pro: Add new `www-frame-origin` option for specifying framing permissions\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-16)\
\
*   Improve resilience against malformed YAML header in R Markdown documents\
*   Avoid triggering active bindings in environments from the Environment pane\
*   Fix encoding of R\_HOME, R\_USER, and R\_LIBS\_USER on Windows\
*   Fix project-based file completion on Windows\
*   Respect loaded packages in R help topic completion\
*   Fix positioning of editor toolbar buttons in Safari and Mac OS client\
*   Fix incorrect height of R Notebook outputs when run above viewport\
*   Detect multi-line data.table chains properly\
*   Allow git staging for filenames containing a space on Windows\
*   Use Windows proxy settings to serve requests made by htmlwidgets\
*   Fix cross-domain error when opening a link to RStudio Server in a new window\
*   Fix comment toggling for ROxygen comments\
*   Fix notebook resource problems occurring in projects on mounted filesystems\
*   Server Pro: Allow server user to have group name differing from user name\
*   Server Pro: Don’t require LDAP to support user enumeration when `auth-required-user-group` is set\
\
1.0.44[](https://docs.posit.co/ide/news/#rstudio-1.0.44)\
\
---------------------------------------------------------\
\
> Date: 2016-11-01\
\
Highlights\
\
*   Authoring tools for [R Notebooks](https://rmarkdown.rstudio.com/r_notebooks.html)\
    .\
*   Integrated support for the [sparklyr](https://sparklyr.ai/)\
     package (R interface to Spark).\
*   Enhanced data import tools based on the [readr](https://readr.tidyverse.org/)\
    , [readxl](https://readxl.tidyverse.org/)\
     and [haven](https://haven.tidyverse.org/)\
     packages.\
*   Performance profiling via integration with the [profvis](https://rstudio.github.io/profvis/)\
     package.\
*   Authoring tools for R Markdown [websites](https://rmarkdown.rstudio.com/rmarkdown_websites.html)\
     and the [bookdown](https://bookdown.org/)\
     package.\
*   Many other miscellaneous enhancements and bug fixes.\
\
R Notebooks\
\
*   Authoring tools for [R Notebooks](http://rmarkdown.rstudio.com/r_notebooks.html)\
    \
*   Inline display for text, latex, tabular data, graphics, and htmlwidgets in source editor\
*   All code and output saved within a single notebook HTML file (.nb.html)\
*   Multiple language engines including Python, Bash, SQL, Rcpp, and Stan\
*   Tools for running various combinations of chunks (current, next, previous, remaining)\
\
Data Import\
\
*   Import dataset from text via [readr](https://readr.tidyverse.org/)\
    \
*   Import dataset from Excel via [readxl](https://readxl.tidyverse.org/)\
    \
*   Import dataset from SAS, SPSS, and Stata via [haven](https://haven.tidyverse.org/)\
    \
*   Preview data while importing datasets\
*   Explicitly set column types while importing datasets\
*   Preview and copy code while importing datasets\
\
Profiler\
\
*   Profiling features based on the [profvis](https://rstudio.github.io/profvis/)\
     package\
*   Visualize profiling results within the IDE\
*   Profile menu enables easy stop/start of profiling or profiling of selected lines.\
*   Save and load of previous profiling sessions\
\
RStudio Connect\
\
*   Publish reports, applications, and plots to [RStudio Connect](https://posit.co/products/enterprise/connect/)\
    \
*   One-click deployment of Shiny applications\
*   Publish and schedule periodic execution of R Markdown reports\
*   Set which users and/or groups have permission to view content\
\
Spark\
\
*   Integrated support for the [sparklyr](https://sparklyr.ai/)\
     package\
*   Create and manage connections to Spark clusters and local Spark instances\
*   Browse tables and columns of Spark DataFrames\
*   Preview the first 1,000 rows of Spark DataFrames\
\
Source Editor\
\
*   Ctrl+Enter now executes current R statement when selection is empty\
*   Use Shift+Click to open web links in source editor (Command+Click on OS X)\
*   Enabled auto-pairing of backticks in R documents\
*   Fixed regression re: folding of unnamed sections, e.g. ‘#####’\
*   Implemented folding for sub-sections in R documents\
*   Added option for display of ‘end’ fold markers\
*   Display function tooltip on mouse over of function name\
*   Added option to display function signature tooltip on cursor idle\
*   Autocompletion allows mismatch between ‘.’, ’\_’ in token\
*   Improvements to refactoring utility ‘Rename in Scope’\
*   Expand selection command learns how to expand to current statement\
*   Added (as unbound command) Sublime Text style ‘Quick Add Next’\
*   The various ‘yank’ commands are now rebindable (Ctrl + Y, Ctrl + K, Ctrl + U)\
*   Insert assignment operator (Alt+-, ‘<-’) is now rebindable\
*   Insert pipe operator (Cmd+Shift+M, ‘%>%’) is now rebindable\
*   Enable implementors of .DollarNames to provide custom types\
\
R Markdown\
\
*   Inline preview for MathJax equations\
*   Show custom formats in Knit menu\
*   Show options menu and Knit w/ Params for custom formats\
*   Use “Run Document” for custom formats with runtime: shiny\
*   Add option to suppress Knit preview entirely\
*   Add R Markdown pane to global options dialog\
*   Build tab and preview support for R Markdown websites\
*   Various enhancements for authoring with the bookdown package\
*   Add command to clear knitr cache\
*   Update pandoc to 1.17.2\
*   Update MathJax to 2.6.1\
\
C/C++\
\
*   Provide autocompletion of header paths\
*   Syntax highlighting of raw, wide, unicode string literals (e.g R”hello”)\
\
Server\
\
*   Added session-default-working-dir and session-default-new-project-dir options\
*   Added sudo, lsb-release, and libssl1.0.0 packages to Debian dependencies\
*   Server Pro: Auditing for authentication and session start/suspend/exit events\
*   Server Pro: Ability to configure per-user and per-group session timeouts\
*   Server Pro: Ability to include custom HTML within server sign-in page\
*   Server Pro: Update to Nginx 1.10.1\
\
Miscellaneous\
\
*   Improved performance of ‘Find in Files’ tool\
*   Attempting to cut or copy with an empty selection no longer clears the clipboard\
*   Files pane now has a fixed header row\
*   Attempting to check out remote git branch now checks out local copy tracking remote\
*   Published plots are larger and responsive to changes in browser size\
*   Implement gt/gT bindings in Vim mode to switch to next/previous tab\
*   Always provide file completions for top-level current directory\
*   Prevent wrapping of text in Files pane display\
*   Indicate when object details in environment pane have been truncated\
*   Improved keyboard navigation in browser file widgets\
*   Added option to limit length of lines in console history\
*   Improved performance when many lines of code sent to console\
*   ‘save()’ warnings no longer emitted when saving session state\
*   Update C++ unit testing library (catch) to v1.3.3 (fix gcc >=5 compilation errors)\
*   Change default max.print to 1000 (was 10000)\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-17)\
\
*   Fixed a hang on Windows + 64bit R when errors occurred while resizing Plots pane\
*   Fixed an issue where a user-defined git executable was sometimes not respected on OS X\
*   Data Viewer: fixed a crash that could occur when calling ‘View()’ on matrix\
*   R Markdown: hide chunk toolbar when chunk is hidden by folded Markdown section\
*   R Markdown: fixed highlighting with multiple Markdown links on one line\
*   R Markdown: improved highlighting for ’\*‘,’\_’\* text\
*   R Markdown: fixed issue where sections did not display in document outline when following empty bulleted list\
*   Reformat code: fixed an issue where\
    \
    ’\*\*’\
    \
    was not recognized as a single token\
*   SVN: avoid recursive revert when reverting changes to modified directory properties\
*   Autocompletion: fixed errors printed in console when ‘devtools::load\_all()’ active\
*   Autocompletion: fixed errors printed in console for functions ‘force’, ‘identity’\
*   Autocompletion: ensure .DollarNames method respected when discovered\
*   Autocompletion: avoid errors when retrieving completions in debugger\
*   Viewer: Fixed issue in ‘Export -> Copy to Clipboard’ when IDE not at default zoom level\
*   Fix hang caused by large, heavily-nested S4 objects\
*   Fix for ‘httpdPort’ detection error sometimes seen with R built from source\
*   Fixed a hang on Windows with 64-bit R when attempting to load a corrupted workspace\
*   Fixed an issue where non-interactive addins could not be executed in popped out windows\
*   Diagnostics: fix false positive errors with ‘{’ following function calls\
*   Diagnostics: engine better understands ‘data()’ calls (fixes ‘no symbol in scope’ false positive)\
*   Improved performance of document tokenization (fix laggy typing)\
*   Sweave: Fix block commenting of chunks\
*   Sweave: Fixed an issue where TOC headings weren’t displayed in document outline\
*   Fix highlighting of escaped ‘$’ in inline Mathjax expressions\
*   Fix editor preview vanishing on zoom level change\
*   Emacs mode: C-f now moves the cursor forward instead of opening Find dialog\
*   Emacs mode: C-r now performs a reverse isearch on Windows (rather than running code)\
*   Ensure that modal dialogs capture all input even in the presence of multiple modals\
*   Filter out “00LOCK” directories from package name completions\
*   Provide completions for ‘lazydata’ objects within namespaces\
*   Prevent warnings from leaking when accessing refClass elements for completions\
*   Fix inablity to get active frame for completions when package lfe was loaded\
*   Prevent completion popup from appearing offscreen for very long completion names\
*   Don’t pass encoding=“” to knitr for .Rpres files not in a project\
*   Avoid duplicating keydown handlers in image list boxes (e.g. New R Markdown template)\
*   Ensure editor completion popups are hidden when editor loses focus\
*   Cleanup R auto-indentation for plain () or \[\]\
    \
    (i.e., when not in a function call)\
    \
*   Suppress httpd warnings on invalid help queries\
*   Correct syntax highlighting for operator << in C++ mode\
*   Fix highlighting in R mode for numbers with only a trailing decimal (e.g. ‘1.’)\
*   Ensure that SparkR DataFrames appear as data in environment pane\
*   Avoid firing active bindings in completion system\
*   Fix copy, cut, paste handling when Emacs mode enabled\
*   Avoid perturbing RNG state when invoking View()\
*   Fix unlinked directories in Files pane when other users’ folders are browseable\
*   Fixed an issue where nested folds were not preserved correctly on save / load\
*   Prevent lines terminated by from entering editor (cause of many subtle problems)\
*   Fix error message when invoking View() on an object with no columns\
*   Fix blank screen on log-in when PAM username capitalization doesn’t match system\
*   Prompt to save untitled (never saved) documents when closing source windows\
*   Don’t depend on number of call frames when detecting install.packages call\
*   Fix failure to install packages with long install.packages commands after restart\
*   Server Pro: Fix issue causing sporadic session launch failures when using PAM sessions\
\
0.99.903[](https://docs.posit.co/ide/news/#rstudio-0.99.903)\
\
-------------------------------------------------------------\
\
> Date: 2016-07-18\
\
Highlights\
\
*   Support for multiple [source windows](https://support.posit.co/hc/en-us/articles/207126217)\
     (tear editor tabs off main window).\
*   Pane zooming for working distraction free within a single mode.\
*   Editor and IDE keyboard shortcuts can [now be customized](https://support.posit.co/hc/en-us/articles/206382178)\
    .\
*   New [Emacs keybindings](https://support.posit.co/hc/en-us/articles/210928128)\
     mode for the source editor.\
*   Support for registering custom [RStudio Addins](http://rstudio.github.io/rstudioaddins/)\
    .\
*   R Markdown editing improvements including outline view and inline UI for chunk execution.\
*   Support for [parameterized](http://rmarkdown.rstudio.com/developer_parameterized_reports.html)\
     R Markdown reports.\
*   Various improvements to RStudio Server Pro including [multiple concurrent R sessions](https://support.posit.co/hc/en-us/articles/211789298)\
    , -se of [multiple R versions](https://support.posit.co/hc/en-us/articles/212364537)\
    , and [shared projects](https://support.posit.co/hc/en-us/articles/211659737)\
     for collaboration.\
\
Source Editor\
\
*   New Emacs editing mode\
*   Editor and IDE keyboard shortcuts can now be customized\
*   Support for multiple source windows (tear editor tabs off main window)\
*   New global and per-project options for line feed conversion\
*   Snippets: pass parameters to snippet generating R functions\
*   Split into lines command for multiple cursors (Ctrl+Alt+A)\
*   New keyboard shortcuts to expand/contract current selection\
    *   Cmd+Alt+Shift+{Up/Down} OS X\
    *   Ctrl+Shift+{Up/Down} otherwise\
*   Enhanced display of sections in R scope navigator\
*   Added document outline display to R and C++ documents\
*   New Close All Except Current command\
*   Rename variable in scope (Cmd+Shift+Alt+M)\
*   More context-sensitive highlighting of R keywords\
*   Option to enable highlighting of R function calls\
*   F2 now navigates into files (e.g. within calls to source)\
*   Yank before/after (Ctrl+K, Ctrl+U) now use system clipboard on RStudio Desktop\
*   Yank after cursor (Ctrl+K) no longer eats end of line character\
*   Added option controlling ‘surround on text insertion’ behavior\
\
R Markdown\
\
*   New run chunk and options buttons overlaid at the top right of chunks\
*   New shortcut for run current chunk (Cmd+Shift+Enter)\
*   Outline view for quick navigation between sections/code chunks\
*   Ctrl+PageUp and Ctrl+PageDown navigate between sections within Rmd, Rpres\
*   Enabled comment/uncomment (Cmd+Shift+C) for Markdown documents\
*   Knit with Parameters command for previewing with varying parameters\
*   Run All now executes chunks in console (rather than calling e.g. knitr::purl)\
*   Reorganize toolbar commands/menu for improved discoverability\
*   Added Run Setup Chunk command\
*   Updated embedded pandoc to v1.15.2\
*   Update embedded pdf.js to v1.3\
*   Support additional options for MS Word (table of contents, keep markdown)\
\
Miscellaneous\
\
*   RStudio Addins:\
    *   Register R functions as addins that can interact with the IDE using the rstudioapi package.\
    *   Accessible from the Addins menu and can be bound to custom keyboard shortcuts\
*   New Session command (create new R session with same project or working directory)\
*   Open project in a new window from the projects recently used menu\
*   New Shiny App command for quick creation of Shiny applications\
*   Data Viewer: Filter factor columns by text or level\
*   Raise limit on shinyapps uploads to 1GB from 100MB\
*   ‘Edit -> Replace and Find’ opens Find toolbar if not already open (e.g. with Cmd+Shift+J)\
*   Improve performance of console for large and/or rapidly updating output\
*   Roxygen quick reference available from the Help menu\
*   Links to RStudio cheatsheets available on the Help menu\
*   Scan for Rtools in both HKCU and HKLM (for non-Admin installs of Rtools)\
*   Run app command and shortcut now works for running single file Shiny applications\
*   Move running Shiny apps between IDE panes and windows without restarting the app\
*   Add support for single-file, standalone Shiny applications\
*   Parse TeX magic comments that start with “%%” (ESS compatibility).\
*   Change default Rpres template to specify autosize: true\
*   Automatically create ~/.ssh directory if necessary on Windows\
*   Added Makefile mode (used for Makefile, Makevars)\
*   Always use LF for line endings in Unix Makefiles in R packages\
*   Return environment variables as completions within Sys.getenv(), Sys.setenv() calls\
*   Add ‘R Scripts’ preset filter to Find in Files dialog\
*   OS X: Support for executing commands via AppleScript via ‘cmd’ verb\
*   OS X: Enable WebKit WebGL by default\
*   OS X: Enable WebKit DeveloperExtras by default\
*   OS X: Enable creation of directories in folder picker dialog\
*   Windows: Update to SumatraPDF 3.1.1\
*   Added ability to zoom panes (e.g. Ctrl+Shift+1 to zoom source pane)\
*   Add Console on Left/Right commands for quick relocation of Console\
*   Add product and version metadata to Windows installer\
*   Add askForPassword function to rstudioapi\
*   Improved detection of Msysgit installation location on Windows\
\
Server\
\
*   Include active project in document title (caption of browser tab)\
*   Quit session command now accessible from global toolbar\
*   Added option to control how many days users stay signed in for\
*   Allow specification of multiple groups in auth-required-user-group option\
*   Suspend and resume running R sessions when server is restarted\
*   Add kill-session and kill-all admin commands\
*   Use SHA256 for signing cookies (previously used SHA1)\
*   Use more resilient file locking mechanism for compatibility with NFS volumes\
*   Attempt to close application window when quitting\
*   Track installed client version using git commit hash rather than timestamp\
*   Detect minimum user id from /etc/login.defs (can also be specified via option)\
*   Save user-specific .RData and .Rhistory if .Ruserdata directory exists\
*   Server Pro: Shared Projects (including concurrent multi-user editing)\
*   Server Pro: Support for multiple concurrent R sessions per-user\
*   Server Pro: Support for running against multiple versions of R\
*   Server Pro: Ability to record user console history for audit purposes\
*   Server Pro: Home page for navigating to active sessions and recent projects\
*   Server Pro: Don’t close PAM sessions by default (configurable via an option)\
*   Server Pro: Remove Google OpenID auth (deprecated by Google in favor of OAuth)\
*   Server Pro: Add option to specify client-id for Graphite metrics back end\
*   Server Pro: Supported SSL protocols is now configurable\
*   Server Pro: Add option to rewrite user header in proxied authentication\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-18)\
\
*   Diagnostics: Avoid linting symbols in R formulas\
*   Diagnostics: Resolve functions in correct namespace\
*   Diagnostics: Fix invalid diagnostics within formulas\
*   Diagnostics: Respect // \[\[Rcpp::export\]\] functions used in R code\
*   Fix grid metrics issues (e.g. text too small) by using res of 96 rather than 72\
*   Correct computation of getOption(“width”) on high DPI displays\
*   Rcpp: Parse attributes when generating diagnostics for header files\
*   Enable outdenting in Rhtml documents\
*   Find all now respects active search/replace options\
*   Fix issue with cursor disappearing in Rmd chunks for ambiance theme\
*   Publish button shows in the editor and viewer at the appropriate times\
*   Avoid spurious R warnings when autocompletions requested\
*   Allow completions in statements following infix operators\
*   Completions in Install Packages are now correct for the case of multiple active repositories\
*   Vim mode: prevent paste operation from entering visual mode via Ctrl+V cross-talk\
*   Fixed chunk highlighter issues that occurred when editing chunk label\
*   Correctly handle call to edit() with no arguments\
*   Fix inability to start up on OS X when multiple conflicting R versions are on the library search path\
*   Prevent crash when canceling out of q() prompt on Windows\
*   OS X: Fix crash which could occur when focusing text boxes with placeholders\
*   OS X: Viewer now correctly recognizes session temp dir even when prefixed by /private\
*   OS X: Word document preview now correctly reloads for newer versions of Office\
*   Fix issue with rstudioapi previewRd function when path included spaces\
*   R 3.3: Don’t call setInternet2 or use –internet2 flag for child R processes\
*   Linux, Windows: ensure native printer used (don’t default to PDF printing)\
*   Linux: Install on Debian Sid and Ubuntu 16.04 via addition of libgstreamer-0.10 dependencies\
*   Prevent spurious navigation when user cancels from the file upload dialog\
*   Don’t include H3 (and higher) headers when creating presentation slide preview navigation menu\
*   Don’t allow long file paths to overflow in message dialogs\
*   RPM: Set autreqprov to “no” for both desktop and server\
*   Prevent periods from being used in Rmd date field (caused LaTeX errors)\
\
0.99.902[](https://docs.posit.co/ide/news/#rstudio-0.99.902)\
\
-------------------------------------------------------------\
\
> Date: 2016-05-26\
\
Data Viewer\
\
*   Support for viewing large data sets (removed 1k row limit)\
*   Data can be filtered, searched, and sorted\
*   Viewer updates to reflect changes in data\
\
R Code Completion\
\
*   Completions provided automatically without an explicit gesture\
*   All objects visible from the current scope are now included in completions\
*   Completions in more contexts including S3 and S4 methods and dplyr pipelines\
*   Automatic insertion of closing parens when appropriate\
*   Inline help tooltip for signatures of completed functions\
*   Completion for statements spanning multiple lines\
*   Specialized autocompletions provided for library, data, vignette, ?\
*   For Shiny applications, autocompletions for ui.R + server.R pairs\
*   Completions for dimension names in \[, \[\[ calls\
*   Completions from packages in library, require calls automatically inferred and supplied even when not loaded\
*   Completions for knitr options, e.g. in opts\_chunk$get(), are now supplied\
*   Completions for dynamic symbols within .C, .Call, .Fortran, .External\
*   Completions for object names for ‘formula’ arguments, e.g. lm(.., data = mtcars)\
\
R Code Diagnostics\
\
*   Syntax errors are highlighted and displayed in red (e.g. missing commas, unmatched brackets)\
*   Function calls are checked and validated with e.g. match.call()\
*   Warn if variable is used but no definition is available in scope\
*   Warn if variable is defined but never subsequently used\
*   Whitespace diagnostics to help code conform to [http://adv-r.had.co.nz/Style.html](http://adv-r.had.co.nz/Style.html)\
    \
\
Source Editor\
\
*   Improvements in file/function navigation:\
    *   Fuzzy matching on search terms\
    *   Navigate to file posititions using file:line:col\
    *   Include parameters in function navigation menu\
*   Multiple cursors:\
*   Create a new cursor above / below the current cursor with CTRL + ALT + {up / down}\
*   Move the active cursor up / down with CTRL + SHIFT + ALT + {up / down}\
*   Create multiple cursors by pressing CTRL + ALT and clicking + dragging the mouse\
*   Improved Vim mode:\
    *   Various bug fixes\
    *   Visual block selection (CTRL + v)\
    *   Multiple-cursor aware\
    *   Macros (q)\
    *   Marks (m)\
    *   Quick find (/)\
    *   Support a subset of commands in :\
    *   Use :help for documentation on available commands\
*   Configurable snippets for fast insertion of common blocks of code\
*   Editor tabs in the source pane can now be rearranged\
*   Automatically save files prior to sourcing (controlled by option)\
*   Support for multiple cursors via Ctrl+Alt+Up/Down\
*   Alt+Enter to run code while retaining cursor position\
*   Ctrl+Shift+E to select within matching parens / braces\
*   Ctrl+Alt+Shift+E to expand selection to matching paren / brace\
*   Comment/uncomment respects indent level when appropriate\
*   New Reformat Code command for R scripts\
*   Shift+Enter now searches backwards in Find/Replace\
*   Find All option added in Find/Replace\
*   Ctrl+E now focuses the editor after finding from selection\
*   New option to control comment continuation on insertion of new lines\
*   Reflow text (comment) for markdown and plain text modes\
*   Updated to Ace (source editor component) v1.1.8\
*   Syntax highlighting for GraphViz and mermaid.js diagrams.\
*   Diagram previews using the DiagrammeR package (requires recent version from GitHub).\
*   Syntax highlighting modes for many new languages including Clojure, CoffeeScript, C#, Graphviz, Go, Groovy, Haskell, Java, Julia, Lisp, Lua, Matlab, Perl, Ruby, Rust, Scala, and Stan.\
*   Keyword and text based code completion for many languages including JavaScript, HTML, CSS, Python, and SQL.\
*   A wide variety of new editor themes (color schemes) are now available.\
*   Increase file size limit to 5MB (was previously 2MB)\
\
C/C++ Development\
\
*   Code completion\
*   Code diagnostics\
*   F2 code navigation (go to definition)\
*   Go to file/function for C/C++\
*   Find usages for C++ symbols\
*   Intelligent auto-indentation\
*   Scope tree for quick intra-file navigation\
\
Web Development (HTML/CSS/JavaScript)\
\
*   Code completion\
*   Inline diagnostics (JSHint) on syntax and other issues\
\
Workspace\
\
*   Improved handling of objects containing or consisting of NULL externalptr\
\
Debugging\
\
*   Allow ‘debugSource’ to be executed in user-specified environment\
*   Improved heuristics for locating the stack frame where errors originated\
*   Autocompletions now available when debugging\
*   Improved debug stepping through statements wrapped in tryCatch()\
*   Better call frame selection when using recover()\
*   Keyboard shortcuts for Step Into (Shift+F4) and Step Out (Shift+F6)\
\
Packages\
\
*   Improvements to New Package:\
*   Generate cleaner packages with no warnings\
*   Respect various devtools options\
*   Support for roxygen2 ‘vignette’ roclet\
*   Insert Roxygen Skeleton command (Ctrl+Alt+Shift+R)\
*   Default to roxygenize for Build and Reload\
*   Improved checking for supported protocol with packrat package\
*   Escape backslashes in library names when loading packages\
*   Call to library after Build and Reload respects –library argument\
*   Validate that required versions are available for prompted installs\
*   Set R\_BROWSER=false and R\_PDFVIEWER=false (as CRAN does) for R CMD check\
\
Plots\
\
*   Render plots using devicePixelRatio for retina and HDPI screens -Preserve last exported size in Save Plot as PDF dialog\
*   dev.new() now creates a new desktop graphics device (e.g. quartz) if the RStudio device is already active.\
\
R Markdown\
\
*   Updated to pandoc 1.13.1\
*   Support for parameterized R Markdown reports\
*   Ensure that .RData from Rmd directory isn’t loaded during Knit\
*   Improved handling of lists in editor\
*   Syntax highlighting for comments in markdown documents\
*   Make publishing UI easier to discover\
*   Require save before previewing Rmd file\
*   Handle encoding correctly for Run All Chunks on Windows\
*   Support for deploying single interactive documents (not just directories)\
*   Updated internal PDF viewer (PDF.js) to version 1.0.1040\
\
Miscellaneous\
\
*   Updated rendering engine to Qt 5.4 for improved performance\
*   Windows: updated to MSYS SSH 1000.18\
*   Windows: check HKCU in addition to HKLM when scanning for R versions\
*   Windows: Use Rtools 3.3 when running under R 3.2\
*   Use system.file() rather than .packages() to query for package availability.\
*   Bind Cmd+Shift+K shortcut to Compile PDF and Preview HTML\
*   When evaluating R strings ensure ‘try’ is called from base package\
*   Default to current working directory for New Project from existing directory\
*   Add Clear Recent Projects menu item to toolbar project menu\
*   Command to sync current working directory and Files pane to project directory\
*   Eliminated rstudio and manipulate packages (both now available on CRAN)\
*   Respect existing values for RSTUDIO\_PANDOC and RMARKDOWN\_MATHJAX\_PATH environment variables.\
*   Added global RStudio.Version function for getting basic version info\
*   Diagram previews using the DiagrammeR package (requires recent version from GitHub).\
*   Added Markers pane and sourceMarker API for externals tools (e.g. linters)\
*   Enable specification of Sweave driver in Rnw magic comment\
*   Re-map prev/next tab shortcuts to eliminate conflicts with window managers\
*   Run App command for single file Shiny applications\
*   Deprecated ‘source.with.encoding’ in favor of source(…, encoding = “…”)\
*   Make source code compatible with -std=c++11\
*   Allow specifying character encoding, row name source, and comment character when importing data\
*   Jump to the definition of a function by clicking it in the environment pane\
*   Increase shinyapps upload limit to 1GB (was previously 100MB).\
\
Server\
\
*   Use systemd to manage server processes on platforms where it is the default\
*   Add server-set-umask option to control whether the server sets its umask to 022 at startup\
*   Improved installation by reducing dependencies and providing additional platform-specific builds (e.g. SUSE, RHEL5 vs. RHEL6/7)\
*   Server Pro: Support for SPDY protocol\
*   Server Pro: Custom header name for proxied authentication\
*   Server Pro: Option to eliminate “stay signed in” option for PAM authentication.\
*   Server Pro: Update to Nginx 1.8.0\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-19)\
\
*   Prevent error dialog when getOption(“repos”) is an unnamed vector\
*   Fix for regex Find/Replace lockup with empty strings\
*   Fix for console text unselectable in Firefox\
*   Find in Files now always activates result pane\
*   Correctly reflow comments in Rmd C++ code chunks\
*   Don’t warn when saving C/C++ file with .hpp extension on OS X\
*   Ensure that rmarkdown documents render within input directory\
*   Eliminate race condition that could cause crash when polling child processes\
*   Correct handling for breakpoints in files with non-ascii filenames on Windows\
*   Next/previous word behavior in Rmd is now consistent with behavior in R scripts\
*   Don’t parse YAML front matter if not preceded by whitespace\
*   Eliminate some UI problems on Windows HDPI systems\
*   Prevent null reference exception in packages pane with active filter + packrat\
*   Allow JSON as text file type in the editor\
*   Only hide object files (e.g. _.o)_ in Files pane when in package src directory\
*   Ensure cursor is always visible after source navigation\
*   Server: Ensure that LANG is populated from system default when not inherited\
*   Server: Provide required domain socket permissions during startup\
*   IE 11: Strip unprintable unicode characters in Rmd front matter dates\
*   Only filter object file listings in ‘src’ directory\
*   Fix crash in R tokenizer when source files have binary 0xFFF\
*   Correctly navigate to package inst/include directory for template errors\
*   Fix visual debugging issues when code isn’t saved in system encoding\
*   Fix compilation errors that occurred as a result of GCC concept checks\
*   Persist last size setting in Save Plot as PDF dialog\
*   R 3.2: Specify .Platform$pkgType when installing binary package archives\
\
0.98.1103[](https://docs.posit.co/ide/news/#rstudio-0.98.1103)\
\
---------------------------------------------------------------\
\
> Date: 2015-03-06\
\
R Markdown\
\
*   Next generation of R Markdown based on [pandoc](https://pandoc.org/)\
    *   Create HTML, PDF, and MS Word documents as well as [Beamer](https://bitbucket.org/rivanvx/beamer/wiki/Home)\
         and [ioslides](https://code.google.com/p/io-2012-slides/)\
         presentations\
    *   New markdown syntax including expanded support for tables, definition lists, and bibliographies\
    *   A responsive (multi-device friendly) and themeable HTML template based on [Bootstrap](http://getbootstrap.com/2.3.2/)\
        \
    *   Include raw LaTeX within markdown for advanced customization of PDF output\
    *   Use Shiny with R Markdown to create interactive documents\
    *   Compile HTML, PDF, or MS Word notebooks from R scripts\
    *   See the [rmarkdown website](http://rmarkdown.rstudio.com/)\
         package for more details\
*   Option to preview R Markdown HTML in Viewer Pane\
*   Enhancements to HTML previewing for presentation authoring\
*   Previewing for MS Word and PDF output\
*   Added Run Previous Chunks command (Ctrl+Alt+P)\
*   Keyboard shortcut for Knit is now Ctrl+Shift+K\
\
Debugging Tools\
\
*   Support for R 3.1 advanced stepping commands (step into and finish loop)\
*   Allow viewing and stepping through functions that don’t have source-refs (via deparse)\
*   Improved support for debugging outside of functions including stepping inside loops\
\
Packages\
\
*   Integrated support for [packrat](http://rstudio.github.io/packrat/)\
    \
*   New devtools mode for package development (uses devtools for check, document, test, etc.)\
*   Keyboard shortcuts for Test (Ctrl+Shift+T) and Document (Ctrl+Shift+D)\
*   Package listing is now grouped by library\
*   Pick default save location for files based on type (e.g. R, src, man, etc.)\
*   Don’t write HTML output when previewing package Rmd or md documentation\
\
Shiny Development\
\
*   Run and debug Shiny applications directly within the IDE\
*   Launch applications and reload changes on the fly using Run/Reload command (Ctrl+Enter)\
*   Automatically close Shiny application windows on interrupt/exit\
*   Integrated support for publishing applications to shinyapps.io\
\
Source Editor\
\
*   Keyboard shortcut (Ctrl+Shift+M) for magrittr pipe operator (%>%)\
*   Find from selection keyboard shortcut (Mac: Cmd+E, Windows/Linux: Ctrl+F3)\
*   Execute Current Section command (Mac: Cmd+Option+T, Windows/Linux: Ctrl+Alt+T)\
*   Syntax highlighting modes for XML, YAML, SQL, Python, and shell scripts.\
*   Command to execute Python and shell scripts (Ctrl+Shift+Enter)\
*   New Extract Variable code refactoring (thanks to Dirk Schumacher)\
*   Miscellaneous improvements to R and C++ syntax highlighting (thanks to Kevin Ushley)\
*   Execute R code from the Source Viewer using Ctrl+Enter\
*   Option to automatically strip whitespace at the end of lines\
*   Option to ensure that R source files always end with newline\
*   Always use tabs for indentation in Makefile and Makevars\
*   Enable save command immediately for new documents\
\
RStudio Server\
\
*   Support for Internet Explorer 10 and 11\
*   Improved satellite window reactivation (e.g. version control, preview, etc.)\
*   Improved location and refresh header re-writing for localhost proxy\
*   r-cran-repos option now works consistently and overrides user CRAN option\
*   Fix completion window dismissal issue in Ubuntu Chrome\
*   Compatibility with RHEL/CentOS 7\
*   Pro: Load balancing for increased capacity and high availability\
*   Pro: Allocate cores and set scheduler priority and resource limits per user or group\
*   Pro: Run a different version of R per user or group\
*   Pro: Optionally forward credentials to PAM sessions (e.g. for issuing Kerberos tickets)\
*   Pro: New config options to disable access to various features\
*   Pro: Migrate Google Accounts support to OAuth 2.0 interface\
*   Pro: Login as user link now works correctly when running behind proxies\
*   Pro: Updated embedded nginx to 1.6.2\
*   Pro: Prevent use of SSLv3 protocol\
*   Pro: Compatibility with SLES 11 (SP1, SP2, and SP3)\
\
Miscellaneous\
\
*   Viewer: History, Zoom, and Export commands for static HTML widgets\
*   Publish to RPubs from Plots and Viewer panes\
*   Keyboard shortcut quick reference (Mac: Option+Shift+K, Windows/Linux: Alt+Shift+K)\
*   Mac: Overlay project name on RStudio Dock icon when multiple projects are open\
*   Mac: Added New Window command to RStudio Dock icon\
*   Mac: Show help PDFs in Preview rather than in an internal window\
*   Mac: Correct handling of file downloads from help pane\
*   Mac: Direct /usr/bin/gnutar to /usr/bin/tar if necessary on Mavericks\
*   Mac: Updated code signing method for OS X 10.10 Yosemite\
*   Mac: Remove duplicated PATH entries on OS X 10.10 Yosemite\
*   Mac: Eliminate checkbox animation in dialog boxes on OS X 10.10 Yosemite\
*   Windows: Automatically adapt typefaces for for high-dpi displays\
*   Linux: Improved Ubuntu font rendering (spacing for monospace, font face for proportional)\
*   Linux: Don’t link to R BLAS and LAPACK on RedHat/Fedora (R 3.1 compatibility)\
*   Git/SVN menu on global toolbar with commands for active file and project\
*   Added history, zoom, and export for static HTML widgets in Viewer pane\
*   View/Blame on GitHub commands for GitHub projects (file or selection driven)\
*   Display current Git branch in main window title\
*   Added stringsAsFactors and string.na options to Import Dataset\
*   Restore previously entered input to console after executing commands\
*   Increase limit on active plots from 30 to 100\
*   Added documentation on which version rstudio package functions were introduced\
*   Updated GWT library to version 2.6.0\
*   Updated pdf.js for improved performance and fidelity of PDF preview\
*   R 3.2: Use new API for accessing tools::httpdPort\
*   R 3.2: Support for Rtools 3.2\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-20)\
\
*   Disable spell checking and auto-correction in text entry fields\
*   Fix debugger line highlighting for functions invoked with :: at the console\
*   Fix for package breakpoints set after library() sometimes missing srcrefs\
*   Fix cursor positioning on OS X when CJK characters are present\
*   Handle Windows junctions (soft links) in the Files Pane\
*   Correctly scale satellite windows in Windows high DPI mode\
*   Prevent slowdown in scrolling and editing for large Rmd and Sweave files\
*   Preserve working directory when restarting R while not in a project\
*   Fix for intermittent R Pubs upload failures\
*   Environment: prevent view of large data frames from collapsing on update\
*   Packages: Don’t check dependency status when repos = NULL\
*   Packages: Respect repository option already set from .Rprofile\
*   Packages: Don’t use –with-keep.source for R < 2.14\
*   Plots: fix issues with copy plot to clipboard on OS X\
*   Plots: prevent spurious warnings when rendering plots from already closed device\
*   Help: handle internal redirects from R help correctly on Windows & Linux\
*   Server: Fix issue which caused extra bytes at end of some file uploads\
*   Server: Prevent freeze when concurrently reading both ends of proxied websocket\
*   Server: Enable loading of IDE within an iframe in Firefox\
*   Server: Don’t remove /usr/\[s\]bin soft links during upgrades\
*   Server: Fix python egg cache issue with metrics script\
*   Server: Ensure helper processes run as server user and terminate with parent\
*   Server: Fix completion window dismissal issue in Ubuntu Chrome\
*   Mac: Correctly detect OS X command line tools on OS X Yosemite\
*   Mac: Prevent extra line from being copied in Safari 8\
*   Prevent loading of videos in HTML Preview (caused crashes in some configurations)\
*   Respect ‘whole word’ option in source editor replace operations\
*   Eliminate compiler errors when building on Ubuntu 14.04\
*   Correctly recognize application/xml as a text file type in the source editor\
*   Prevent crash which occurred after opening a QtWebKit web inspector\
*   Prevent error messages during session termination\
*   Fix for Windows crash when ESC key pressed at startup\
*   Fix for installing packages when repos option is an unnamed vector\
\
0.98.507[](https://docs.posit.co/ide/news/#rstudio-0.98.507)\
\
-------------------------------------------------------------\
\
> Date: 2015-04-25\
\
Debugging Tools\
\
*   Set breakpoints within the source editor, both inside and outside functions\
*   View object values and call stack during debugging\
*   Step through code line by line\
*   Error inspector for quick access to tracebacks and debugger after runtime errors\
*   Integration with traditional R debugging tools, such as `browser()` and `debug()`\
*   For more information see [Debugging with RStudio](https://support.posit.co/hc/en-us/articles/200713843-Debugging-with-RStudio)\
    \
\
Environment Pane\
\
*   Browse any environment on the search path\
*   Filtering by name/value\
*   Expand lists, data frames, and S4 objects inline\
*   Use `str()` for displaying object values\
*   Optional grid view sortable by various attributes\
*   Many other small correctness and robustness enhancements\
\
R Presentations\
\
*   Easy authoring of HTML5 presentations based on [R Markdown](https://rmarkdown.rstudio.com/)\
    \
*   Extensive support for authoring and previewing inside the IDE\
*   Many options for customizing layout and appearance\
*   Easily published as either a standalone HTML file or to [RPubs](http://rpubs.com/)\
    \
*   For more information see [Authoring R Presentations](https://support.posit.co/hc/en-us/articles/200486468-Authoring-R-Presentations)\
    \
\
Source Editor\
\
*   Use Rcpp template by default for new C++ files\
*   Add code folding for markdown headings/sections\
*   Option to not restore source documents when re-opening projects\
*   Preserve open source documents when underlying project directory is moved\
*   Ability to execute roxygen example code via Cmd/Ctrl+Enter\
*   Change fold/unfold all keyboard shortcut to use ‘O’ rather than ‘0’\
*   Automatically insert a newline at the end of R scripts when executing the last line in the file\
*   Don’t advance cursor after execute code if there is a selection\
*   Detect and provide notification when editing readonly files (Linux and OSX only)\
*   TeX syntax highlighting for .dtx and .ins files\
*   Allow opening application/postscript files in the editor\
*   Scroll to cursor when reactivating the source pane via the keyboard shortcut\
*   Improve clarity of error message for moved or deleted source files\
*   R code automatic indentation now adapts to alternate indentations on subsequent lines\
*   Execute multi-line statements even when line delimiter is plain\
\
Console\
\
*   Control+Enter can now execute commands in the console\
*   Allow Esc key to interrupt the console even if used when focus is in the source editor\
*   Scroll to cursor when reactivating the console via the keyboard shortcut\
\
Packages\
\
*   User option to disable the Packages pane (useful if there are hundreds of packages installed)\
*   Environment variable (RSTUDIO\_DISABLE\_PACKAGES) that can be used to entirely disable the Packages pane.\
*   Build packages using –with-keep-source by default\
*   Correctly set LC\_COLLATE for roxygenize (now works the same as devtools)\
*   Automatically focus console after devtools Load All command\
\
Sweave/knitr\
\
*   knitr 1.2 is now the minimum required version\
*   Higher fidelity parsing of knitr error messages\
*   MathJax compatability mode for IE 10\
*   Correctly base64 encode images with special characters in their paths\
*   Read the Sweave template from the filesystem (resources/templates/sweave.Rnw)\
*   Update Windows PDF viewer to Sumatra PDF v2.4\
\
Viewer Pane\
\
*   New Viewer pane for viewing local web content within RStudio\
*   Works with files written to the R session temporary directory or arbitrary localhost URLs\
*   For more information see [Extending RStudio with the Viewer Pane](https://support.posit.co/hc/en-us/articles/202133558-Extending-RStudio-with-the-Viewer-Pane)\
    \
\
Miscellaneous\
\
*   Replaced Qt with native Cocoa implementation for Mac desktop to improve performance\
*   RStudio can now build on OS X Mavericks with the latest version of XCode\
*   Support the AppNap API on OS X Mavericks to prevent CPU throttling when R is busy\
*   Use domain sockets (Linux/OS X) and named pipes (Windows) for R session communication rather than TCP/IP\
*   Allow R help http server to handle custom URLs directly\
*   Significantly more robust detection of user home paths on Windows\
*   Detect R on OS X even if /usr/bin/R has been deleted\
*   Add option to create projects in a new window\
*   Abilty to create Shiny applications directly from the New Project dialog\
*   Display row.names in data viewer\
*   Compatiblity with Rtools 3.1 (R-devel)\
*   Added previewRd function to RStudio package\
*   Keyboard shortcut (Ctrl+Shift+F10) for restarting R session\
*   Don’t add commands to history when Browser> context is active\
*   Limit size of history database file to approximately 1 MB\
*   Move History button to main toolbar for Git VCS\
*   Always use code-search dialog for Go To Function\
*   Treat objects of type data.table and cast\_df as data in the environment pane\
*   New RSTUDIO\_HTTP\_REFERER environment variable for detecting the full client URL in server mode\
*   User option to disable automatic checking for updates to RStudio\
*   Environment variable (RSTUDIO\_DISABLE\_CHECK\_FOR\_UPDATES) that can be used to disable automatic checking for updates to RStudio\
*   Improved error message for failure to start due to version mismatch between libR and loaded packages\
*   Disable spell-checking in VCS commit message widget\
*   Add .travis.yml to the whitelist of hidden files displayed in the Files pane\
*   Fix inability to change default working directory on Ubuntu 13.10\
*   Block iframes with remote URLs rather than showing them in a new window\
\
RStudio Server\
\
*   Localhost URLs (e.g. for Shiny, Rook, or OpenCPU applications) are now automatically proxied back to remote clients on the main server port.\
*   Add upstart script for RedHat/CentOS 6\
*   No longer specify unlimited core size in upstart script\
*   More permissive AA profile during startup (ability to auto-detect R in more locations)\
*   Enhance fidelity of callstacks for client-side errors\
*   Respect X-Forwarded-Proto header required for redirects when running behind SSL proxies\
*   Deprecated rsesssion ulimit options: rsession-memory-limit-mb, rsession-stack-limit-mb, and rsession-process-limit\
*   Changed Chrome close document shortcut to Cmd+Alt+W\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-21)\
\
*   Avoid evaluating promises for objects in the workspace\
*   Recognize more object types as datasets (any object of class data.frame)\
*   Fix for browseVignettes function not working in server mode\
*   Prevent spurious console warnings when long vectors appear in the workspace\
*   Recover gracefully from plot export default directory being removed during a session\
*   Track multiple changes within a session to default export plot directory\
*   Ignore YAML front-matter that contains multi-line lists in R Markdown documents\
*   Prevent mis-detection of embedded R chunks in C++ files (space required before R on first line)\
*   Don’t serve http content (javascript:false) when running behind an https proxy\
*   Fix for cursor positioning bug when using Safari 7.0\
*   Clear busy indicator after cancelling update packages\
*   Serve woff fonts with correct mime type (avoids warnings in javascript console)\
*   Ensure that the user’s own group is checked when verifying that a user belongs to a group\
*   Fix for console interrupt button sometimes remaining active even when session is idle\
*   Enable copying of prompt text from within the console\
*   Navigate to help topics based on mouse selection (formerly requried keyboard selection)\
*   Ensure that Git revert requests with no valid files don’t revert all unstaged changes\
*   Prevent RPM upgrade from removing rstudio-server script from /usr/sbin\
*   Fix for some text file types being incorrectly detected as binary on RedHat 5\
*   Detect R location within cmake configuration even when warnings or other spurious output are generated during R startup.\
*   Eliminate warnings which sometimes occurred when initializing default user package library\
*   Eliminate warnings which sometimes occurred when resizing graphics devices\
*   R 3.02 plots now correctly restore during session resume and build and reload\
*   R 3.02 plots that occur in rapid sequence without rendering in the UI now work correctly\
*   Prevent “parameter type mismatch” error when using manipulate\
*   Prevent error messages which could occur when restarting R from an already suspended session\
\
0.97.551[](https://docs.posit.co/ide/news/#rstudio-0.97.551)\
\
-------------------------------------------------------------\
\
> Date: 2013-05-11\
\
Package Development\
\
This release includes a variety of tools to support R package development, including:\
\
*   A new Build tab with various package development commands and a view of build output and errors\
*   Build and Reload command that rebuilds the package and reloads it in a fresh R session\
*   Incremental reload is very fast and preserves the state of the previous R session, providing quick turnarounds and much more interactive workflow for package development\
*   Additional commands for checking packages and building source and binary packages\
*   Ability to create a new package based on existing R source files\
\
There are also a number of features aimed at making it easier to write R documentation:\
\
*   Preview and optional automatic preview on save for Rd files\
*   Spell-checking for Rd files\
*   Syntax highlighting, code-completion, and re-flowing for [Roxygen](https://roxygen2.r-lib.org/)\
     comments\
*   Ability to automatically invoke Roxygen prior to package builds\
\
There is also integration with the [devtools](https://devtools.r-lib.org/)\
 package, including:\
\
*   Load All command and keyboard shortcut (Ctrl+Shift+L) that calls `devtools::load_all`\
*   All package installations respect the development library established by `devtools::dev_mode`\
*   Automatic restoration of `devtools::dev_mode` when reloading and restarting R sessions\
\
Rcpp\
\
This release includes many new features to support seamless R and C++ integration using [Rcpp](http://dirk.eddelbuettel.com/code/rcpp.html)\
, including:\
\
*   Syntax highlighting for C/C++\
*   Quick navigation to gcc errors and warnings\
*   Support for [Rcpp Attributes](http://dirk.eddelbuettel.com/code/rcpp/Rcpp-attributes.pdf)\
    :\
    *   Command w/ keyboard shortcut for `Rcpp::sourceCpp`\
    *   Editor support for embedded R code chunks in C++ source files\
    *   Automatic calls to `Rcpp::compileAttributes` for package builds\
*   New project option to create “Package w/Rcpp”\
*   Automatic unloading of Windows dynamic libraries before package builds\
*   Editor support for Rcpp code chunks in R Markdown\
\
Source Editor\
\
*   Find and Replace improvements:\
    *   Incremental search\
    *   Find/Replace in selection\
    *   Backwards find\
    *   Options for whole word and wrap\
*   Automatic indentation improvements:\
    *   Full support for auto-indent in Sweave/knitr code chunks\
    *   More intelligent handling of closing braces\
    *   Recognize operators (e.g. ‘+’ for ggplot) as expression continuations\
    *   Option to control whether function arguments are vertically aligned\
    *   Option to disable auto-indent after pasting code into editor\
*   [Vim](http://en.wikipedia.org/wiki/Vim_(text_editor))\
     editing mode\
*   [Tomorrow](https://github.com/chriskempson/tomorrow-theme#readme)\
     suite of editor themes\
*   Surround selected text with quote/brace/paren/etc. on key input\
*   Jump to matching brace/param (Ctrl+P)\
*   New options: show whitespace, show indent guides, non-blinking cursor\
*   Advance to next line after executing a selection from the editor\
*   Significantly improved file-type detection (automatically open all files detected as text)\
\
Console\
\
*   More intelligent history navigation with up/down arrow keys\
*   Confirm if attempting to quit while R console is busy\
*   Improved auto-scroll behavior in the console\
*   Option to focus console after executing code from editor\
*   Send interrupt for ESC key even if server doesn’t appear to be busy\
*   Display error output in distinct color for TextMate theme (and some others)\
\
Plots\
\
*   Plot zoom window improvements:\
    *   Automatically refreshes with plots pane\
    *   Remembers and restores it’s size (within each session)\
*   Use bg=transparent option for plots to RStudio device\
*   Always use native R png device with cairo bitmapType on Linux\
*   Default plot export dialogs to current size of plots pane\
*   Option to use cairo\_pdf for PDF plot export on platforms where it is available\
*   Set useDingbats = FALSE for PDF plot export (for compatibility with broader set of PDF viewers)\
*   Compatibility with R Graphics Engine version 10 (R-devel)\
\
Packages\
\
*   Install Packages dialog can now install both source and binary packages\
*   Warn and offer optional restart when updating packages that are currently loaded\
*   Display package version and tooltip indicating which library they are installed in\
*   Option to use RStudio CRAN mirror (Amazon S3/CloudFront)\
*   Install rstudio and manipulate packages in default user library (R 3.0)\
\
Workspace\
\
*   New option to control whether hidden objects are removed in Clear All\
*   Confirm prior to editing large (length >= 100) workspace objects\
*   Call read.csv directly when possible in import dataset (compatibility with spreadsheets exported as CSV from LibreOffice)\
*   Custom workspace display for ore.frame objects\
*   Treat objects of type data.table and cast\_df as data\
\
Sweave/knitr\
\
*   Added a Log button to the HTML preview window for reviewing the compilation log\
*   Changed insert chunk keyboard shortcut to Cmd+Alt+I\
*   Enable syntax highlighting inside of Markdown lists\
*   Add docs on inline R code to markdown quick reference\
*   Markdown rendering no longer performs a hard wrap for newlines\
*   Ignore Pandoc title blocks and YAML front-matter when rendering markdown\
*   Don’t use new window to open links from Markdown generated HTML documents\
*   Parse new knitr error message format for enhanced R error diagnostics\
*   Removed stitch notebook option\
*   Append rather than prepend /opt/local/bin to path (prefer MacTeX over MacPorts Tex)\
*   Explicitly pass file encoding to Sweave and knitr\
\
Miscellaneous\
\
*   Compatibility with R 3.0\
*   Ability to specify a global UI zoom-level\
*   Improved keyboard navigation for the Help pane (Ctrl+F, incremental search)\
*   Show directory disambiguater when multiple projects in the MRU share the same name\
*   Support for OS X Lion full screen mode\
*   Add Ctrl+Q shortcut for quit on Windows on Linux\
*   Change replace and find keyboard shortcut to Cmd+Shift+J\
*   Change Chrome close window shortcut to Cmd+Shift+Z\
*   Preface Alt keyboard shortcuts on the Mac with Cmd (international keyboard compatibility)\
*   Preference to control whether –internet2 is enabled on Windows\
*   Find in files search pattern defaults to current selection\
*   Remember find in files search scope (per-project) across sessions\
*   RSTUDIO environment variable is set at startup (for detecting RStudio within .Rprofile)\
*   New ‘rstudio’ package with versionInfo and diagnosticsReport functions\
*   Change Windows stack size to 20MB (was 10MB in v0.96)\
*   Sign Windows installer using Authenticode\
*   Use DYLD\_FALLBACK\_LIBRARY\_PATH rather than DYLD\_LIBRARY\_PATH to bind to libR on OS X\
*   More robust handling of errors that occur during quit\
*   Reduce error option related overhead of calls from C++ to R\
*   Remove legacy 32MB minimum memory limit\
\
Robustness/Diagnostics\
\
*   New Restart R and Terminate R commands\
*   More graceful recovery if the underlying R session crashes or is unable to start\
*   Diagnostic tools for troubleshooting startup and configuration problems\
*   Prohibit opening binary files in the source editor\
*   Improved detection of invalid or too-large source files at startup\
*   Prevent OS X freeze which occurs when more than one modal dialog shows at startup.\
*   Use Recycle Bin for file deletion on Windows and OS X\
\
RStudio Server\
\
*   Suspend now saves and restores .libPaths and environment variables\
*   Suspend now correctly handles packages loaded from a custom lib.loc\
*   Option to automatically re-execute .Rprofile on session resume\
*   Automatic installation of dependencies on Debian/Ubuntu using gdebi\
*   Fix execute rule conflict with AppArmor base abstraction\
*   Ability to discover R in non-standard filesystem locations\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-22)\
\
*   Don’t allow console width to be set to an invalid value\
*   Correct default project file name for project directories containing a period\
*   Remove files from MRU list if an error occurs while opening them\
*   Recognize .q and .s files as R source files\
*   Show forward and back buttons for Rmd and Rnw source documents\
*   Enable shell escape option for LaTeX now works correctly on Windows\
*   Fix for execute current/next chunk not working in certain cursor states\
*   Code folding keyboard shortcuts now work for non-top level code blocks\
*   Correctly display next/previous tab shortcuts on Linux\
*   Advance to empty line after executing last line in the document\
*   Yank (Ctrl+U) shortcut now works as intended on all platforms\
*   Prevent selection of user-interface elements (only text can be selected)\
*   Ensure that serialization progress always appears above global toolbar\
*   Restore focus to editor after switching file types\
*   Restore focus to main window after open/save dialogs are dismissed\
*   Ensure that Git/SVN and document preview windows correctly reactivate in Chrome\
*   Use correct SVN directory even when working directory changes\
*   Set locale correctly on OS X (including respecting R.app locale preferences)\
*   Set R\_ARCH in multi-arch builds of R for OS X\
*   Print warning when running against MacPorts R that is compiled without aqua/quartz\
*   When scanning for R script don’t treat /usr/bin/R as a script if it’s actually a directory\
*   Fix OS X crashes that occurred sporadically for some list boxes in the options dialog\
*   Don’t prevent application exit when errors occur while reverting source documents\
*   Don’t show plot preview if it’s larger than available screen space\
*   Prevent simultaneous display of message box and update dialog\
*   Ctrl+W can now closes the plot zoom window\
*   Use correct parameters to ensure a valid EPS file is exported\
*   Show correct number of variables in data viewer\
*   Automatically hide history popup panel when clicking away from it\
*   Correctly handle package status when multiple versions of packages are installed\
*   Update status of packages even when they are hidden by a filter\
*   Don’t call packageVersion for compatibility with R 2.11.1\
*   RShowDoc type=html now works correctly on Windows\
*   browseURL can now open HTML documents now prefaced by the file:// protocol\
*   browseURL in desktop mode no longer performs additional URL encoding\
*   Ensure that PDF preview works even when concordance isn’t available\
*   Display search results when looking up help term with more than one matching symbol\
*   PDF links now open correctly from the Help pane\
*   Always use bundled gnu grep on windows (rather than other versions of grep that might be in the path)\
*   Eliminate upstart and AppArmor mis-detection on Debian testing\
*   Prevent freeze when loading large line-wrapped source files on Chrome for Linux\
\
0.96.331[](https://docs.posit.co/ide/news/#rstudio-0.96.331)\
\
-------------------------------------------------------------\
\
> Date: 2012-08-27\
\
Sweave / knitr\
\
*   Spell checking for Sweave and TeX documents.\
*   Integrated PDF previewer that supports two-way synchronization ([SyncTeX](http://itexmac.sourceforge.net/SyncTeX.html)\
    ) between the editor and PDF view.\
*   Support for weaving Rnw files using the [knitr](http://yihui.name/knitr/)\
     package (requires knitr version 0.5 or higher).\
*   Parsing of TeX error logs to extract errors, warnings, and bad boxes and present them in a navigable list.\
\
Web Publishing\
\
*   Editing and previewing R Markdown and R HTML files (like Sweave except for web pages).\
*   Creation of easy to distribute standalone HTML files (with embedded images).\
*   Support for including LaTeX and MathML equations in web pages using [MathJax](http://www.mathjax.org/)\
    .\
\
Source Editing\
\
*   Find in files with regular expressions.\
*   Code folding (expanding and collapsing regions of code).\
\
**0.96.331 — August 27th, 2012**\
\
Miscellaneous\
\
*   Fix issue with git console flashing on windows\
\
**0.96.330 — August 6th, 2012**\
\
Miscellaneous\
\
*   Retina display font rendering for new MacBook Pro\
*   Add Ctrl+R as a shortcut for Run Code on Windows\
*   Improved window restoration behavior (especially for multi-monitor configurations)\
*   Prevent console from flickering after it has been cleared\
*   Always initialize projects even while the underlying filesystem doesn’t support locking\
*   Never overwrite exiting project file when creating a new project\
*   Ensure that source-on-save setting is always respected\
*   Source documents no longer marked as dirty if they are changed while RStudio is closed\
*   Find in Files updated to work correctly with OS X 10.8 grep\
*   RStudio Server compatibility with Safari 6\
\
**0.96.316 — June 29th, 2012**\
\
Markdown\
\
*   Ability to define custom markdown rendering function to override default handling\
*   HTML preview improvements: set focus on load, preserve anchor when refreshing\
*   New notebook types based on calling knitr::stitch and knitr::silk\
*   No longer require \\ escape for MathJax native equations\
\
Miscellaneous\
\
*   Syntax highlighting mode for C/C++\
*   Use current project directory as default for save as dialog\
*   Fix for narrowing of console width after external PDF preview\
\
**0.96.304 — June 8th, 2012**\
\
Markdown\
\
*   Added Create Notebook for quick reports from R scripts\
\
MathJax\
\
*   Support for wider variety of equation delimiters\
\
**0.96.233 — June 7th, 2012**\
\
Miscellaneous\
\
*   Rebuild from correct v0.96 branch\
\
**0.96.231 — June 5th, 2012**\
\
Markdown\
\
*   Fix publish to RPubs on Windows\
\
**0.96.230 — June 4th, 2012**\
\
Markdown\
\
*   Support for publishing markdown documents to RPubs\
\
**0.96.228 — May 26th, 2012**\
\
Miscellaneous\
\
*   Fix symbol lookup incompatibility with R-devel\
\
**0.96.227 — May 25th, 2012**\
\
MathJax\
\
*   Introduce more explicit syntax for equation embedding to eliminate parsing ambiguities\
*   Update docs to reflect no current support for ASCIIMath equations\
\
**0.96.225 — May 23rd, 2012**\
\
Sweave/LaTeX\
\
*   Comment/Uncomment for LaTeX and Sweave files\
*   Call Sweave/knitr with –no-save and –no-restore (rather than –vanilla)\
*   Default to calling pdflatex or xelatex directly (rather than using texi2dvi)\
*   Don’t spell-check cite\* or bibitem commands\
\
Markdown\
\
*   Create new documents using a basic template that documents R Markdown syntax\
*   Eliminate table borders in Markdown CSS\
*   Improved document title detection\
*   Added documentation on R code blocks to Markdown quick reference\
\
MathJax\
\
*   Use a local version of MathJax for previews (enabling MathJax preview even when offline)\
*   Use SVG for local MathJax previews on the Mac (but still publish as HTML/CSS)\
*   Allow embedding multiple inline equations on a single line\
*   Allow inline equation definitions to span across multiple lines\
*   Only include HTML-CSS options in local preview mode\
*   Link to the https version of the MathJax scripts in generated HTML file\
\
Source Editing\
\
*   Changed Comment/Uncomment shortcut to Ctrl+Shift+C\
*   Fixed issue with clipboard shortcuts on Japanese keyboard layouts\
*   Fixed inability to enter braces in international keyboard layouts on the Mac\
*   Execute current function now works (fixed regression)\
\
Miscellaneous\
\
*   Developer ID code signing for Mac\
*   Add libjpeg62 dependency for Ubuntu 12.04\
*   Fix symbol lookup incompatibility with R-devel\
*   Prevent console access by forked child processes\
\
**0.96.122 — May 14th, 2012**\
\
Sweave / knitr\
\
*   Spell checking for Sweave and TeX documents.\
*   Integrated PDF previewer that supports two-way synchronization ([SyncTeX](http://itexmac.sourceforge.net/SyncTeX.html)\
    ) between the editor and PDF view.\
*   Support for weaving Rnw files using the [knitr](http://yihui.name/knitr/)\
     package (requires knitr version 0.5 or higher).\
*   Parsing of TeX error logs to extract errors, warnings, and bad boxes and present them in a navigable list.\
*   Chunk option auto-complete, chunk folding, jump to chunk, and iterative execution of chunks.\
*   Compilation based on multiple input files (support for specifying a root TeX document) .\
*   TeX formatting commands, block comment/uncomment, and various new compilation options.\
\
Web Publishing\
\
*   Editing and previewing R Markdown and R HTML files (like Sweave except for web pages).\
*   Creation of easy to distribute standalone HTML files (with embedded images).\
*   Support for including LaTeX and MathML equations in web pages using [MathJax](http://www.mathjax.org/)\
    .\
\
Source Editing\
\
*   Find in files with regular expressions.\
*   Code folding (expanding and collapsing regions of code).\
*   Automatic comment reflowing (Cmd+Shift+/).\
*   Smart editing of Roxygen comments.\
*   Syntax highlighting for Markdown, HTML, Javascript, and CSS files.\
*   New font customization options.\
\
Miscellaneous\
\
*   Fixed incompatibility with Winbind for PAM authentication.\
*   Fixed editor cursor off by one line problem that occurred after rapid scrolling.\
*   Updated to Qt 4.8: required for PDF viewer and to fix OS X Lion trackpad scrolling issue (however as a result 32-bit Mac systems and OS X 10.5 are no longer supported).\
\
0.95.265[](https://docs.posit.co/ide/news/#rstudio-0.95.265)\
\
-------------------------------------------------------------\
\
> Date: 2012-04-05\
\
Miscellaneous\
\
*   Fix R 2.15 startup problem when libraries with missing dependencies are loaded in .Rprofile\
\
**0.95.263 — March 15th, 2012**\
\
Miscellaneous\
\
*   Shortcuts no longer disabled after showing SVN commit dialog\
\
**0.95.262 — February 28th, 2012**\
\
Plots\
\
*   Fix JPEG, TIFF, and BMP plot exporting for R 2.14 on OS X\
\
**0.95.261 — February 15th, 2012**\
\
Source Editor\
\
*   Bypass corrupt source documents on startup\
\
**0.95.258 — January 31st, 2012**\
\
Version Control\
\
*   Git https authentication now works on Mac OS X\
*   Fix for startup problems when a pane layout includes only a (hidden) Git or SVN panel\
\
Miscellaneous\
\
*   Fixed various issues with project paths containing non-Ascii characters on Windows\
*   Eliminate spurious display of scrollbars for History pane with Ubuntu Mono typeface\
*   Correctly launch Chrome on Windows for external URLs (when it is the default system browser)\
\
**0.95.256 — January 25th, 2012**\
\
Projects\
\
*   Create projects that enable easy switching between working directories\
*   Each project has its own RStudio context:\
    *   R session\
    *   Open source documents\
    *   Arrangement of panes\
    *   History\
    *   Saved workspace (.RData)\
*   All R code within a project is indexed for quick navigation by filename or function\
*   Projects can be bound to version control repositories (Git or Subversion)\
*   File-association for .Rproj files to open projects from the shell\
*   Open multiple instances of RStudio with different projects concurrently\
\
Code Navigation\
\
*   Quickly navigate to any file or function within a project using typeahead search\
*   Go To Function Definition:\
    *   Go to the definition of function currently at the cursor (F2 or Ctrl+Click)\
    *   Works for both indexed source code as well as functions defined within packages\
    *   Special handling for S3/S4 methods with multiple definitions\
*   Back and Forward commands for quickly traversing navigation contexts (including tab switches)\
\
Version Control\
\
*   Integrated support for binding projects to Git and Subversion repositories\
*   Git/SVN pane:\
    *   View current changelist\
    *   Stage or revert changes\
    *   Push/pull/update\
    *   Switch branches\
*   Review changes window:\
    *   Diff pending changes\
    *   Incremental stage/discard of chunks (Git)\
    *   All functions from Git/Svn pane also available\
*   History window:\
    *   View the history of all changelists (and their associated diffs) for a project\
    *   View changelists that affect only a specific file or directory\
    *   Filter changelists by subject (Git)\
\
Other New Features\
\
*   Support for multiple concurrent instances of RStudio\
*   Global toolbar for accessing common file/navigational commands\
*   Source editor improvements:\
    *   Jump to Line\
    *   Reindent Lines\
    *   Automatically re-indent lines on paste\
    *   Save All and Close All commands\
    *   Immediate refresh of documents changed in external editors\
*   Manipulate package:\
    *   Button control\
    *   Function to capture mouse coordinates (`manipulatorMouseClick`)\
*   Shell command:\
    *   Desktop: open system terminal in current directory\
    *   Web: open web-based terminal in current directory\
*   Use native Ubuntu monospace and proportional fonts on newer Ubuntu systems (11.10+)\
*   Support for \\1..\\99 and , n regex search & replace\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-23)\
\
*   Correctly highlight variables which include dot (.) in their names\
*   Prevent unmapped command keys on OSX from inserting characters in the editor\
*   Correctly handle context-sensitive help requests for functions which include underscore (\_) in their names.\
*   Remove syntax highlighting for strings within LaTeX.\
*   Improve precision of click-selection on variables in the editor\
*   F1-help now works properly for Google Chrome browsers\
*   Don’t auto-insert matching quotes for string-terminating quotes\
*   Disable quote-matching in Roxygen comments\
*   Fix cursor-position issues in soft-wrapped documents\
*   Run function definition now works correctly on Windows\
*   Preserve scroll position for History pane across activations\
*   Fix re-rendering of R 2.14 lattice plots after server suspend/resume\
*   data.css is now correctly served when running behind a reverse proxy\
\
0.94.110[](https://docs.posit.co/ide/news/#rstudio-0.94.110)\
\
-------------------------------------------------------------\
\
> Date: 2011-10-03\
\
Installation\
\
*   Fix Ubuntu 64-bit packaging issue that was introduced in 0.94.109\
\
**0.94.110 — October 3rd, 2011**\
\
Source Editor\
\
*   Fix Ubuntu 64-bit packaging issue that was introduced in 0.94.109\
\
**0.94.109 — October 3rd, 2011**\
\
Source Editor\
\
*   Fix intermittent problems with autoindent\
\
**0.94.106 — September 22nd, 2011**\
\
R 2.14\
\
*   Temporarily disable support for dev.hold / dev.flush (need to buffer flushes to reduce http round trips)\
\
**0.94.105 — September 12th, 2011**\
\
R 2.14\
\
*   Support for Graphics Engine v9 (dev.hold, dev.flush, and dev.capabilities)\
*   Parallel package compatibility (corrected problem with child process signal handling)\
*   Eliminate readLines warning (for incomplete last line) from startup and after source of active document\
\
**0.94.102 — August 22nd, 2011**\
\
Miscellaneous\
\
*   Enforce editor file size limits (1MB warning, 5MB absolute limit) in desktop mode\
*   Improved track-pad responsiveness for scrolling on OSX Lion\
*   Use short file name variant for R.home() on Windows\
*   Use privileged mode for PAM authentication on Ubuntu\
*   Correct escaping of apostrophes in settings files\
*   Enable select none button in package update dialog\
\
**0.94.92 — July 11th, 2011**\
\
Source Editor and Console\
\
*   Added Source with Echo command (Ctrl-Shift-Enter)\
*   Editor toolbar menu for specifying default source echo behavior\
*   Sourcing of saved files uses file’s path rather than temporary file\
*   Change Run All shortcut to Ctrl-Shift+R and remove from toolbar\
*   All commands from multiline input are recalled by up-arrow\
*   Correctly handle spacing for ampersands within quotes\
*   Fix for misalignment of text with embedded tabs\
*   Correct indentation behavior when in hard tab mode\
\
Sweave\
\
*   Improved detection of TeX installation on OS X\
*   Prevent activation of external console window on Windows\
\
Miscellaneous\
\
*   Correct state for dev.interactive even when graphics device not yet loaded\
*   Delegate to shell for unknown file types in desktop mode\
*   Eliminate warning messages resulting from display of bquote assignments in workspace\
*   Skip reading of .DS\_Store files in source database directory\
*   Prevent crash when timestamp is called from .Rprofile on Windows\
\
**0.94.82 — June 15th, 2011**\
\
Source Editor and Console\
\
*   Run code:\
    *   Run all lines in source file\
    *   Run to current line\
    *   Run from current line\
    *   Redefine current function\
    *   Re-run previous region\
    *   Code is now run line-by-line in the console\
*   Brace, paren, and quote matching\
*   Improved cursor placement after newlines\
*   Support for regex find and replace\
*   Optional syntax highlighting for console input\
*   Press F1 for help on current selection\
*   Function navigation / jump to function\
*   Column and line number display\
*   Manually set/switch document type\
*   New themes: Solarized and Solarized Dark\
\
Plots\
\
*   Improved image export:\
    *   Formats: PNG, JPEG, TIFF, SVG, BMP, Metafile, and Postscript\
    *   Dynamic resize with preview\
    *   Option to maintain aspect ratio when resizing\
    *   Copy to clipboard as bitmap or metafile\
*   Improved PDF export:\
    *   Specify custom sizes\
    *   Preview before exporting\
*   Remove individual plots from history\
*   Resizable plot zoom window\
\
History\
\
*   History tab synced to loaded .Rhistory file\
*   New commands:\
    *   Load and save history\
    *   Remove individual items from history\
    *   Clear all history\
*   New options:\
    *   Load history from working directory or global history file\
    *   Save history always or only when saving .RData\
    *   Remove duplicate entries in history\
*   Shortcut keys for inserting into console or source\
\
Packages\
\
*   Check for package updates\
*   Filter displayed packages\
*   Install multiple packages\
*   Remove packages\
*   New options:\
    *   Install from repository or local archive file\
    *   Target library\
    *   Install dependencies\
\
Miscellaneous\
\
*   Find text within help topic\
*   Sort file listing by name, type, size, or modified\
*   Set working directory based on source file, files pane, or browsed for directory.\
*   Console titlebar button to view current working directory in files pane\
*   Source file menu command\
*   Replace space and dash with dot (.) in import dataset generated variable names\
*   Add decimal separator preference for import dataset\
*   Added .tar.gz (Linux) and .zip (Windows) distributions for non-admin installs\
*   Read /etc/paths.d on OS X to ensure RStudio has the same path as terminal sessions do\
*   Added manifest to rsession.exe to prevent unwanted program files and registry virtualization\
\
Server\
\
*   Break PAM auth into its own binary for improved compatibility with 3rd party PAM authorization modules.\
*   Ensure that AppArmor profile is enforced even after reboot\
*   Ability to add custom LD library path for all sessions\
*   Improved R discovery:\
    *   Use which R then fallback to scanning for R script\
    *   Run R discovery unconfined then switch into restricted profile\
*   Default to uncompressed save.image output if the administrator or user hasn’t specified their own options (improved suspend/resume performance)\
*   Ensure all running sessions are automatically updated during server version upgrade\
*   Added verify-installation command to rstudio-server utility for easily capturing configuration and startup related errors\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-24)\
\
*   Undo to unedited state clears now dirty bit\
*   Extract function now captures free variables used on lhs\
*   Selected variable highlight now visible in all themes\
*   Syncing to source file updates made outside of RStudio now happens immediately at startup and does not cause a scroll to the bottom of the document.\
*   Fixed various issues related to copying and pasting into word processors\
*   Fixed incorrect syntax highlighting issues in .Rd files\
*   Make sure font size for printed source files matches current editor setting\
*   Eliminate conflict with Ctrl+F shortcut key on OS X\
*   Zoomed Google Chrome browser no longer causes cursor position to be off\
*   Don’t prevent opening of unknown file types in the editor\
*   Fixed sporadic missing underscores (and other bottom clipping of text) in console\
*   Make sure console history is never displayed offscreen\
*   Page Up and Page Down now work properly in the console\
*   Substantially improved console performance for both rapid output and large quantities of output\
*   Install successfully on Windows with special characters in home directory name\
*   make install more tolerant of configurations where it can’t write into /usr/share\
*   Eliminate spurious stderr output in forked children of multicore package\
*   Ensure that file modified times always update in the files pane after a save\
*   Always default to installing packages into first writeable path of .libPaths()\
*   Ensure that LaTeX log files are always preserved after compilePdf\
*   Fix conflicts with zap function from epicalc package\
*   Eliminate shortcut key conflicts with Ubuntu desktop workspace switching shortcuts\
*   Always prompt when attempting to save files of the same name\
*   Maximized main window now properly restored when reopening RStudio\
*   PAM authorization works correctly even if account has password expiration warning\
*   Correct display of manipulate panel when Plots pane is on the left\
\
0.93.73[](https://docs.posit.co/ide/news/#rstudio-0.93.73)\
\
-----------------------------------------------------------\
\
> Date: 2011-04-11\
\
### New[](https://docs.posit.co/ide/news/#new-2)\
\
Source editor enhancements\
\
We’ve added some new features & options to the source editor. We’ve also received lots of feedback on more advanced capabilities users want in the editor and we will definitely address this in upcoming releases. New stuff in the editor includes:\
\
*   Highlight all instances of selected text\
*   Insert spaces for tabs (soft-tabs)\
*   Customizable print margin line\
*   Selected line highlight\
*   Toggle line numbers on/off\
*   Optional soft-wrapping for R source files\
\
The docs on [source code editing options](https://support.posit.co/hc/en-us/articles/200549016-Customizing-RStudio#editing)\
 include more details.\
\
Customizable layout and appearance\
\
One of the most frequently requested features we’ve have is the ability to put the Console and Source views side-by-side. This configuration (and others) are now possible. New appearance and layout options include:\
\
*   Customize locations of panes and tabs\
*   Change default font size for code views\
*   Select from various editor themes including TextMate, Eclipse, and others.\
\
For more details see the docs on [appearance and layout options](https://support.posit.co/hc/en-us/articles/200549016-Customizing-RStudio#appearance)\
.\
\
Interactive plotting (manipulate)\
\
This release includes a package called manipulate that can be use to create interactive plots within RStudio. Manipulate is very flexible and includes the following capabilities:\
\
*   Generate plots with inputs bound to custom controls (rather than being hard-coded to a single value)\
*   Variety of control types including slider, picker, and checkbox.\
*   Controls appear next to the plot and can be easily shown and hidden\
\
More details as well as screenshots with examples can be found in the [manipulate documentation](https://support.posit.co/hc/en-us/articles/200551906-Interactive-Plotting-with-Manipulate)\
.\
\
Works with R installed from source\
\
The first beta of RStudio was compatible with the binary version of R distributed from CRAN. The current release works with any version of R, including:\
\
*   R built and installed from source using make install\
*   MacPorts or Homebrew versions of R on MacOS X\
\
The docs on [using different versions of R](https://support.posit.co/hc/en-us/articles/200486138-Using-Different-Versions-of-R)\
 describe how RStudio determines which R to run against on each platform.\
\
Character encoding\
\
In this release we’ve significantly improved handling of non-ASCII characters, this includes:\
\
*   Unicode characters can be used for input and output in the console.\
*   The source editor supports Unicode characters and can open/save files using any character encoding.\
*   A product-wide default encoding can be set, and can be overridden on a per-document basis.\
\
See the [character encoding](https://support.posit.co/hc/en-us/articles/200532197-Character-Encoding)\
 documentation for more details.\
\
Improved management of working directories\
\
We’ve added a number of new features to make it easier to switch between working contexts located in different directories. These include:\
\
*   Option to specify a default initial working directory\
*   Tools - Change Working Dir menu command to change both the working directory and Files pane.\
*   Optional file associations for .RData and .R that initialize RStudio within the opened file’s directory\
*   Windows: Startup in working directory specified for shortcuts\
*   Mac: Startup in folder dragged and dropped on RStudio Dock icon\
*   Linux: Startup in terminal working directory when run from the command line\
\
The docs on [working directories and workspaces](https://support.posit.co/hc/en-us/articles/200711843-Working-Directories-and-Workspaces)\
 go into more depth on these features.\
\
Other Enhancements\
\
Console\
\
*   Recognize haracter in console so that txtProgressBar works as expected\
*   Lift restrictions on size of console input which can be sent to R (was 4K total, is now 4K per line)\
*   Jump to next non-blank line in source after executing via Ctrl-Enter\
\
Source Editing\
\
*   Improved size and legibility of default fonts on Windows & Linux\
*   New keyboard shortcuts:\
    *   Alt- for inserting assignment (“<-”) operator.\
    *   Ctrl+Shift+Home/End for select to start/end\
    *   Ctrl+Shift+P for Compile PDF\
*   Add “return” to list of symbols syntax highlighted as a keyword\
\
Compatibility\
\
*   Compatible with R 2.11.1 on Mac (previously required R 2.12)\
*   Added CFBundleSignature to Mac version\
*   Correctly initialize memory.limit to available physical memory on 64-bit Windows\
*   Ensure that R uses Internet2 on Windows for interoperability with proxy servers.\
*   Compatibility with changes to the R 2.13 internal web server (pass headers to custom handlers).\
*   Allow RStudio desktop to run under root account\
*   Improved support for openSUSE (still requires install from source):\
    *   Added install-dependencies-zypper script\
    *   Added init.d script for daemon management\
\
Packaging and Installation\
\
*   Added RStudio.version function to show current version of RStudio\
*   Changed name of RStudio binary from rdesktop to rstudio (avoid conflict with existing rdesktop binary)\
*   Added /usr/bin/rstudio soft-link\
*   Change DEB and RPM dependency on base R package to “recommends” rather than “depends”\
*   Made it more straightforward to install from source:\
    *   Eliminated git pull requirement (can now build directly from tarball)\
    *   Optionally use system package manager installed versions of Qt4 & Boost\
\
Miscellaneous\
\
*   Added Tools menu with Interrupt R, Change Working Dir, and Options commands.\
*   Add support for loading .rda files into Workspace.\
*   Improved file icons including new custom icons for Rnw and Rd files.\
*   Respect both R\_USER and HOME environment variables for determining location of R home directory\
*   Render plot changes on calls to Sys.sleep (enables animated plots)\
*   Workaround Ubuntu TeX ~ substitution bug by using pdflatex rather than texi2dvi\
\
### Fixed[](https://docs.posit.co/ide/news/#fixed-25)\
\
Console\
\
*   Workspace restored message prints at startup even if no workspace was restored\
*   Numeric keypad Enter and navigation keys not correctly interpreted by console\
*   Esc key not always correctly interpreted when attempting to exit from incomplete command.\
\
Source Editing\
\
*   Source pane can become fully selected and impossible to unselect.\
*   Control-Enter to execute sometimes results in selection not updating properly\
*   Jump to Word (Ctrl+Right) doesn’t navigate past ‘\[’ character.\
*   Ctrl+Backspace doesn’t delete previous word on Windows\
*   Characters illegible when Lucida Grande is installed on Mac systems\
*   Active tab in source mode sometimes hidden or partially obscured\
*   Control+S repeats last Undo/Redo on Firefox 3.6\
*   Print from source view not working in Firefox 4\
*   Eliminate key binding conflicts for international keyboard layouts\
*   Incorrect shortcut key displayed in tooltip for Run from source commands\
*   Variables with dots (“.”) in their names not highlighting on double-click.\
\
Plotting\
\
*   Graphics device not reselected after closing other device (e.g. pdf or png device)\
*   X11 device and rgl package not working properly on on Mac.\
*   Save as PNG command not working on Linux\
*   Re-entrant plot rendering routine causes crash for plots which take a long time to be rendered.\
*   plotmath expressions not rendered correctly\
*   Plot history can grow arbitrarily large and cause disk/memory problems.\
\
Compatibility\
\
*   rJava package not working on Linux due to incomplete LD\_LIBRARY\_PATH\
*   Not always correctly detecting whether TeX is installed\
*   Dependency on psmisc package not specified for RStudio Server\
*   Incorrect file association for download of RPM on Fedora\
\
Miscellaneous\
\
*   Failed to start when running behind some proxy server configurations.\
*   Unable to initialize from .Rhistory file that is owned by root\
*   Exit delay of 2-3 seconds in Mac version\
*   Crash when custom gtk theme contains missing or invalid images for standard icons\
*   Unresponsiveness when viewing extremely large data frames\
*   Conflicting RStudio instances running in parallel if launched from different executable paths\
\
Back to top