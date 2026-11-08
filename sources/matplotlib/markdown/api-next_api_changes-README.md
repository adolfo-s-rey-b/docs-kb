[Skip to main content](https://matplotlib.org/stable/api/next_api_changes/README.html#main-content)

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
    

Adding API change notes[#](https://matplotlib.org/stable/api/next_api_changes/README.html#adding-api-change-notes "Link to this heading")

==========================================================================================================================================

API change notes for future releases are collected in `doc/api/next_api_changes/`. They are divided into four subdirectories:

*   **Deprecations**: Announcements of future changes. Typically, these will raise a deprecation warning and users of this API should change their code to stay compatible with future releases of Matplotlib. If possible, state what should be used instead.
    
*   **Removals**: Parts of the API that got removed. If possible, state what should be used instead.
    
*   **Behaviour changes**: API that stays valid but will yield a different result.
    
*   **Development changes**: Changes to the build process, dependencies, etc.
    

Please place new entries in these directories with a new file named `99999-ABC.rst`, where `99999` would be the PR number, and `ABC` the author's initials. Typically, each change will get its own file, but you may also amend existing files when suitable. The overall goal is a comprehensible documentation of the changes.

A typical entry could look like this:

Locators
~~~~~~~~
The unused \`Locator.autoscale()\` method is deprecated (pass the axis
limits to \`Locator.view\_limits()\` instead).

Please avoid using references in section titles, as it causes links to be confusing in the table of contents. Instead, ensure that a reference is included in the descriptive text. Use inline literals (double backticks) to denote code objects in the title.