*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Sticky_footers#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Sticky_footers#mdn-search)
    

Sticky footers
==============

A sticky footer pattern is one where the footer of your page "sticks" to the bottom of the viewport in cases where the content is shorter than the viewport height. We'll look at a couple of techniques for creating one in this recipe.

[Requirements](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Sticky_footers#requirements)

--------------------------------------------------------------------------------------------------------------------

The sticky footer pattern needs to meet the following requirements:

*   Footer sticks to the bottom of the viewport when content is short.
*   If the content of the page extends past the viewport bottom, the footer gets pushed down, always sitting below the content as normal.

[The recipe](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Sticky_footers#the_recipe)

----------------------------------------------------------------------------------------------------------------

Click "Play" in the code blocks below to edit the example in the MDN Playground:

html

    <div class="wrapper">
      <header class="page-header">This is the header</header>
      <main class="page-body">
        <p contenteditable>
          The footer sticks to the bottom even though this paragraph is short. Add
          content to this editable area to see the footer push down when needed to
          fit the content.
        </p>
      </main>
      <footer class="page-footer">Sticky footer</footer>
    </div>
    

css

    * {
      box-sizing: inherit;
    }
    
    html {
      height: 100%;
      box-sizing: border-box;
    }
    
    body {
      height: 100%;
      font: 1.2em sans-serif;
    }
    
    .wrapper {
      min-height: 100%;
      display: grid;
      grid-template-rows: auto 1fr auto;
    }
    
    .page-header,
    .page-footer {
      background-color: rgb(75 70 74);
      color: white;
      padding: 20px;
    }
    
    .page-body {
      padding: 20px;
    }
    
    .page-body p {
      border: 1px solid grey;
    }
    

**Note:** In this example and the following one we are using a wrapper set to `min-height: 100%`. You can also achieve this for a full page by setting a [`min-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-height)
 of `100vh` on the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 and then using it as your grid container.

[Choices made](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Sticky_footers#choices_made)

--------------------------------------------------------------------------------------------------------------------

In the above example we achieve the sticky footer using [CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
. The `.wrapper` has a minimum height of `100%` which means it is as tall as the container it is in. We then create a single column grid layout with three rows, one row for each part of our layout.

[Grid auto-placement](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Auto-placement)
 will place our items in source order and so the header goes into the first auto sized track, the main content into the `1fr` track and the footer into the final auto sized track. The `1fr` track will take up all available space and so grows to fill the gap.

[Alternate method](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Sticky_footers#alternate_method)

----------------------------------------------------------------------------------------------------------------------------

You can also use [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
 to create a sticky footer.

html

    <div class="wrapper">
      <header class="page-header">This is the header</header>
      <main class="page-body">
        <p contenteditable>
          The footer sticks to the bottom even though this paragraph is short. Add
          content to this editable area to see the footer push down when needed to
          fit the content.
        </p>
      </main>
      <footer class="page-footer">Sticky footer</footer>
    </div>
    

css

    * {
      box-sizing: border-box;
    }
    
    html,
    body {
      box-sizing: border-box;
      height: 100%;
      padding: 0;
      margin: 0;
      font: 1.2em sans-serif;
    }
    
    .wrapper {
      box-sizing: border-box;
      min-height: 100%;
    
      display: flex;
      flex-direction: column;
    }
    
    .page-header,
    .page-footer {
      background-color: rgb(75 70 74);
      color: white;
      padding: 20px;
    
      flex-grow: 0;
      flex-shrink: 0;
    }
    
    .page-body {
      padding: 20px;
    
      flex-grow: 1;
    }
    
    .page-body p {
      border: 1px solid grey;
    }
    

The flexbox example starts out in the same way, but we use `display:flex` rather than `display:grid` on the `.wrapper`; we also set [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
 to `column`. Then we set our main content to [`flex-grow: 1`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)
 and the other two elements to [`flex-shrink: 0`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink)
 — this prevents them from shrinking smaller when content fills the main area.

[Resources on MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Sticky_footers#resources_on_mdn)

----------------------------------------------------------------------------------------------------------------------------

*   CSS properties: [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
    , [`min-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-height)
    , [`grid-template-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-rows)
    , [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
    , [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)
    , [`flex-shrink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink)
    
*   [Basic concepts of grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Basic_concepts)
    
*   [CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
     module
*   [Basic concepts of flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
    
*   [CSS flexible box layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Sticky_footers/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/how_to/layout_cookbook/sticky_footers/index.md?plain=1 "Folder: en-us/web/css/how_to/layout_cookbook/sticky_footers (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FHow_to%2FLayout_cookbook%2FSticky_footers&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fhow_to%2Flayout_cookbook%2Fsticky_footers%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FHow_to%2FLayout_cookbook%2FSticky_footers%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fhow_to%2Flayout_cookbook%2Fsticky_footers%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")