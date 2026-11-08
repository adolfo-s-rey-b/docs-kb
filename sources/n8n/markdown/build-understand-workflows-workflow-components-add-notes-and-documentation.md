For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/understand-workflows/workflow-components/add-notes-and-documentation.md)
.

Sticky notes let you annotate and comment on your workflows.

n8n recommends using sticky notes on template workflows to help other users understand your workflow.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-1174cf5b27d0f69013117849481d1cf658c45b72%252Fexample-sticky-note.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a655f4c4d2db3d8729fbda0cfcea998b&sv=3)

A basic workflow with a sticky note attached

Create a sticky note[](https://docs.n8n.io/build/understand-workflows/workflow-components/add-notes-and-documentation#create-a-sticky-note)

--------------------------------------------------------------------------------------------------------------------------------------------

Sticky notes are a core node. To add a new sticky note:

1.  Open the nodes panel.
    
2.  Search for `note`.
    
3.  Click the **Sticky Note** node. n8n adds a new sticky note to the canvas.
    

Edit a sticky note[](https://docs.n8n.io/build/understand-workflows/workflow-components/add-notes-and-documentation#edit-a-sticky-note)

----------------------------------------------------------------------------------------------------------------------------------------

1.  Double-click the sticky note you want to edit.
    
2.  Write your note. [This guide](https://commonmark.org/help/)
     explains how to format your text with Markdown. n8n uses [markdown-it](https://github.com/markdown-it/markdown-it)
    , which implements the CommonMark specification.
    
3.  Click away from the note, or press `Esc`, to stop editing.
    

Change the color[](https://docs.n8n.io/build/understand-workflows/workflow-components/add-notes-and-documentation#change-the-color)

------------------------------------------------------------------------------------------------------------------------------------

To change the sticky note color:

1.  Hover over the sticky note.
    
2.  Select **Change color** ![Change Sticky Note color icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-0c2f798a7a9e9832907e37118970b112c847b5d4%252Fchange-color.png%3Falt%3Dmedia&width=41&dpr=3&quality=100&sign=a2716768be2ae250e59e7185453cb6c2&sv=3).
    
3.  Choose from seven preset colors, or click the rainbow gradient button to select a custom color.
    

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-8cbff715ed67fd48572b14b9572d9f7ecda6c978%252Fcolor-picker-popover.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=89f07dd15a2f78c0f53c54538c16c99f&sv=3)

Color selector showing preset colors and custom color button

### Custom colors[](https://docs.n8n.io/build/understand-workflows/workflow-components/add-notes-and-documentation#custom-colors)

Besides the seven preset colors, you can select any custom color for your sticky notes:

1.  Click the button with the rainbow gradient and plus icon.
    
2.  Use the color picker to select your desired color, or enter a hex color code (for example, `#FF5733`).
    
3.  Click **Apply** to set the color.
    

n8n automatically saves your last-used custom colors (up to eight) and displays them in the color picker for quick access.

Custom colors feature theme-aware borders that automatically adjust for optimal visibility in both light and dark modes.

Sticky note positioning[](https://docs.n8n.io/build/understand-workflows/workflow-components/add-notes-and-documentation#sticky-note-positioning)

--------------------------------------------------------------------------------------------------------------------------------------------------

You can:

*   Drag a sticky note anywhere on the canvas.
    
*   Drag sticky notes behind nodes. You can use this to visually group nodes.
    
*   Resize sticky notes by hovering over the edge of the note and dragging to resize.
    
*   Change the color: select the **Options** menu ![Options icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-f19a4d097d364587b73864eaed77b12bfd8f516b%252Fthree-dot-options-menu.png%3Falt%3Dmedia&width=19&dpr=3&quality=100&sign=71816d7d4b7eec8ac467fd97f3d76f22&sv=3) to open the color selector.
    

Writing in Markdown[](https://docs.n8n.io/build/understand-workflows/workflow-components/add-notes-and-documentation#writing-in-markdown)

------------------------------------------------------------------------------------------------------------------------------------------

Sticky Notes support Markdown formatting. This section describes some common options.

Copy

    The text in double asterisks will be **bold**
    
    The text in single asterisks will be *italic*
    
    Use # to indicate headings:
    # This is a top-level heading <a href="#this-is-a-top-level-heading" id="this-is-a-top-level-heading"></a>
    ## This is a sub-heading <a href="#this-is-a-sub-heading" id="this-is-a-sub-heading"></a>
    ### This is a smaller sub-heading <a href="#this-is-a-smaller-sub-heading" id="this-is-a-smaller-sub-heading"></a>
    
    You can add links:
    [Example](https://example.com/)
    
    Create lists with asterisks:
    
    * Item one
    * Item two
    
    Or created ordered lists with numbers:
    
    1. Item one
    2. Item two

For a more detailed guide, refer to [CommonMark's help](https://commonmark.org/help/)
. n8n uses [markdown-it](https://github.com/markdown-it/markdown-it)
, which implements the CommonMark specification.

Make images full width[](https://docs.n8n.io/build/understand-workflows/workflow-components/add-notes-and-documentation#make-images-full-width)

------------------------------------------------------------------------------------------------------------------------------------------------

You can force images to be 100% width of the sticky note by appending `#full-width` to the filename:

Copy

    ![Source example](https://<IMAGE-URL>/<IMAGE-NAME>.png#full-width)

Embed a YouTube video[](https://docs.n8n.io/build/understand-workflows/workflow-components/add-notes-and-documentation#embed-a-youtube-video)

----------------------------------------------------------------------------------------------------------------------------------------------

To display a YouTube video in a note, use the `@[youtube](<video-id>)` directive with the video's ID. For this to work, the video's creator must allow embedding.

For example:

Copy

    @[youtube](ZCuL2e4zC_4)

To embed your own video, copy the above syntax, replacing `ZCuL2e4zC_4` with your video ID. The YouTube video ID is the string that follows `v=` in the YouTube URL.

See [Workflow components](https://docs.n8n.io/build/understand-workflows/workflow-components)
 for other elements you can add to a workflow.

Related resources[](https://docs.n8n.io/build/understand-workflows/workflow-components/add-notes-and-documentation#related-resources)

--------------------------------------------------------------------------------------------------------------------------------------

*   [Workflow components](https://docs.n8n.io/build/understand-workflows/workflow-components)
    
*   [Work with nodes](https://docs.n8n.io/build/understand-workflows/workflow-components/work-with-nodes)
    
*   [Connect nodes together](https://docs.n8n.io/build/understand-workflows/workflow-components/connect-nodes-together)
    
*   [Canvas Groups](https://docs.n8n.io/build/understand-workflows/workflow-components/canvas-groups)
    
*   [Find your workflow ID](https://docs.n8n.io/build/understand-workflows/workflow-components/find-your-workflow-id)
    

[PreviousCanvas Groups](https://docs.n8n.io/build/understand-workflows/workflow-components/canvas-groups)
[NextFind your workflow ID](https://docs.n8n.io/build/understand-workflows/workflow-components/find-your-workflow-id)

Last updated 10 days ago

Was this helpful?