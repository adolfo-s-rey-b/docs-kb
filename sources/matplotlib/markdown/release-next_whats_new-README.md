[Skip to main content](https://matplotlib.org/stable/release/next_whats_new/README.html#main-content)

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
    

Instructions for writing "What's new" entries[#](https://matplotlib.org/stable/release/next_whats_new/README.html#instructions-for-writing-what-s-new-entries "Link to this heading")

======================================================================================================================================================================================

Each new feature (e.g. function, parameter, rcParam, config value, behavior, ...) must be described through a "What's new" entry.

Each entry is written into a separate file in the `doc/release/next_whats_new/` directory. They are sorted and merged into `whats_new.rst` during the release process.

When adding an entry please look at the currently existing files to see if you can extend any of them. If you create a file, name it something like `cool_new_feature.rst` if you have added a brand new feature or something like `updated_feature.rst` for extensions of existing features.

Include contents of the form:

Section title for feature
\-------------------------

A description of the feature from the user perspective. This should include
what the feature allows users to do and how the feature is used. Technical
details should be left out when they do not impact usage, for example
implementation details.

The description may include a short instructive example, if it helps to
understand the feature.

Please avoid using references in section titles, as it causes links to be confusing in the table of contents. Instead, ensure that a reference is included in the descriptive text. Use inline literals (double backticks) to denote code objects in the title.