*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists/Indenting#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists/Indenting#mdn-search)
    

Consistent list indentation
===========================

One of the most common style changes made to lists is a change in the indentation distance—that is, how far the list items are pushed over to the right. This article will help you understand indenting list items so that list item markers are visible.

To understand why this is the case, and more importantly how to avoid the problem altogether, it's necessary to examine the details of list construction.

[Creating a list](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists/Indenting#creating_a_list)

-----------------------------------------------------------------------------------------------------------

### [Stand-alone list item](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists/Indenting#stand-alone_list_item)

First, we consider the pure list item, not nested in a list of items. When using the HTML [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 element, the browser sets the [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 value to `list-item`. Whether list items not nested in a list are provided a marker (otherwise known as a "bullet") depends on the browser. We can remove that bullet with [`list-style-type: none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
.

css

    li {
      border: 1px dashed red;
    }
    li:nth-of-type(n + 4) {
      list-style-type: none;
    }
    

    li {
      width: 15em;
    }
    

    <p>Default bullets depend on the browser:</p>
    <li>A list item</li>
    <li>A list item</li>
    <li>A list item</li>
    <p>These list items have their bullets removed:</p>
    <li>A list item</li>
    <li>A list item</li>
    <li>A list item</li>
    

That dotted red border represents the outer edges of the content area of each list item. At this point, the list items have no padding or borders.

### [Nested list items](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists/Indenting#nested_list_items)

Now we wrap these in a parent element; in this case, we'll wrap them in an unordered list (i.e., `<ul>`). According to the CSS box model, the list items' boxes must be displayed within the parent element's content area.

css

    ul {
      border: 1px dashed blue;
    }
    li {
      border: 1px dashed red;
      list-style-type: none;
    }
    

    body {
      width: 15em;
    }
    

    <ul>
      <li>A list item</li>
      <li>A list item</li>
      <li>A list item</li>
    </ul>
    

The dotted blue border shows us the edges of the `<ul>` element's content area. That parent comes with both margin and padding. Browsers set the following default styles on unordered lists:

css

    ul {
      /* user-agent styles */
      display: block;
      list-style-type: disc;
      margin-block-start: 1em;
      margin-block-end: 1em;
      padding-inline-start: 40px;
    }
    

### [Default bullet position](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists/Indenting#default_bullet_position)

Now we put the list item markers back in. Since this is an unordered list, the list items inherit `list-style-type: disc;` browser styles, which are filled-circle "bullets," from their `<ul>` parent.

css

    li {
      border: 1px dashed red;
    }
    ul {
      border: 1px dotted blue;
    }
    ul:last-of-type {
      list-style-position: inside;
    }
    

    ul {
      width: 15em;
    }
    

    <p>These default to <code>list-style-position: outside</code>.</p>
    <ul>
      <li>A list item</li>
      <li>A list item</li>
      <li>A list item</li>
    </ul>
    <p>These have <code>list-style-position: inside</code> set.</p>
    <ul>
      <li>A list item</li>
      <li>A list item</li>
      <li>A list item</li>
    </ul>
    

Visually, the markers are _outside_ the content area of the `<ul>`, but that's not the important part here. What's key is that the markers are placed outside the "principal box" of the `<li>` elements, not the `<ul>`. They're sort of like appendages to the list items, hanging outside the content-area of the `<li>` but still attached to the `<li>`.

This is why, in every modern browser, markers are placed outside any border set for an `<li>` element when the value of [`list-style-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position)
 defaults to or is explicitly set to `outside`. When we changed it to `inside`, the markers were brought inside the `<li>`'s content, as though they're an inline box placed at the very beginning of the `<li>`.

[Default indentation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists/Indenting#default_indentation)

-------------------------------------------------------------------------------------------------------------------

As noted above, all browsers provide the `<ul>` parent both margin and padding. While user agents CSS differ somewhat, they all include:

css

    ul,
    ol {
      /* user-agent styles */
      display: block;
      list-style-type: disc;
      margin-block-start: 1em;
      margin-block-end: 1em;
      padding-inline-start: 40px;
    }
    ol {
      list-style-type: decimal;
    }
    li {
      display: list-item;
      text-align: match-parent;
    }
    ::marker {
      unicode-bidi: isolate;
      font-variant-numeric: tabular-nums;
      text-transform: none;
    }
    

All browsers set [`padding-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-inline-start)
 to 40 pixels for the `<ul>` element by default. In left-to-right languages, like English, this is the left _padding_. Any padding set in the author style sheets (that's your stylesheet) takes precedence.

If you want to be explicit, set the following in your style sheets to ensure, unless otherwise overridden, the list items in the main content area of your document, contained in the [`<main>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main)
 section, are properly indented:

css

    :where(main ol, main ul) {
      margin-inline-start: 0;
      padding-inline-start: 40px;
    }
    

And always nest your `<li>` elements in a `<ul>` or `<ol>`.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists/Indenting/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/lists/indenting/index.md?plain=1 "Folder: en-us/web/css/guides/lists/indenting (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FLists%2FIndenting&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Flists%2Findenting%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FLists%2FIndenting%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Flists%2Findenting%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")