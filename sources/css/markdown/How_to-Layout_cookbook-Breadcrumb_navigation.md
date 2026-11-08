*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Breadcrumb_navigation#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Breadcrumb_navigation#mdn-search)
    

Breadcrumb navigation
=====================

Breadcrumb navigation helps the user to understand their location in the website by providing a [breadcrumb](https://developer.mozilla.org/en-US/docs/Glossary/Breadcrumb)
 trail back to the start page. The items typically display inline, with a separator between each item, indicating the hierarchy between individual pages.

![Links displayed inline with separators](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Breadcrumb_navigation/breadcrumb-navigation.png)

[Requirements](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Breadcrumb_navigation#requirements)

---------------------------------------------------------------------------------------------------------------------------

Display the hierarchy of the site by displaying inline links, with a separator between the items, indicating the hierarchy between individual pages, with the current page appearing last.

[Recipe](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Breadcrumb_navigation#recipe)

---------------------------------------------------------------------------------------------------------------

Click "Play" in the code blocks below to edit the example in the MDN Playground:

html

    <nav aria-label="Breadcrumb" class="breadcrumb">
      <ol>
        <li><a href="#">Home</a></li>
        <li><a href="#">Category</a></li>
        <li><a href="#">Sub Category</a></li>
        <li><a href="#">Type</a></li>
        <li><span aria-current="page">Product</span></li>
      </ol>
    </nav>
    

css

    body {
      font: 1.2em sans-serif;
    }
    
    .breadcrumb {
      padding: 0 0.5rem;
    }
    
    .breadcrumb ol {
      display: flex;
      flex-wrap: wrap;
      list-style: none;
      margin: 0;
      padding: 0;
      align-items: end;
    }
    
    .breadcrumb li:not(:last-child)::after {
      display: inline-block;
      margin: 0 0.25rem;
      content: "→";
    }
    

**Note:** The example above uses a complex selector to insert content before every `li` except the last one. This could also be achieved using a complex selector targeting all `li` elements except the first:

css

    .breadcrumb li:not(:first-child)::before {
      content: "→";
    }
    

Feel free to choose the solution that you prefer.

[Choices made](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Breadcrumb_navigation#choices_made)

---------------------------------------------------------------------------------------------------------------------------

To display list items inline, we use [flexbox layout](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Flexbox)
, thus demonstrating how a line of CSS can give us our navigation. The separators are added using [CSS generated content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Generated_content)
. You could change these to any separator that you like.

[Accessibility concerns](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Breadcrumb_navigation#accessibility_concerns)

-----------------------------------------------------------------------------------------------------------------------------------------------

We used the [`aria-label`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-label)
 and [`aria-current`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-current)
 attributes to help assistive technology users understand what this navigation is and where the current page is in the structure. See the related links for more information.

Be aware that the separator arrows `→` added via the [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 CSS property in the example above are exposed to assistive technologies (AT), including screen readers and braille displays. For a quieter solution, use a decorative [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 in your HTML with an empty `alt` attribute. An ARIA [`role`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles)
 set to [`none`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/none_role)
 or [`presentation`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/presentation_role)
 will also prevent the image from being exposed to AT.

Alternatively, silence the [CSS generated content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Generated_content)
 by including an empty string as alternative text, preceded by a slash (`/`); for example, `content: url("arrow.png") / "";`.

If including generated separators that will be exposed to AT, opt for creating the generated content using the [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)
 pseudo-element selector instead of [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)
, so the separator content is announced after the HTML content instead of before it.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Breadcrumb_navigation#see_also)

-------------------------------------------------------------------------------------------------------------------

*   [CSS flexible box layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
    
*   [Providing a breadcrumb trail](https://www.w3.org/TR/WCAG20-TECHS/G65.html "External link (opens in new tab)")
    
*   [Using the `aria-current` attribute](https://tink.uk/using-the-aria-current-attribute/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Breadcrumb_navigation/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/how_to/layout_cookbook/breadcrumb_navigation/index.md?plain=1 "Folder: en-us/web/css/how_to/layout_cookbook/breadcrumb_navigation (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FHow_to%2FLayout_cookbook%2FBreadcrumb_navigation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fhow_to%2Flayout_cookbook%2Fbreadcrumb_navigation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FHow_to%2FLayout_cookbook%2FBreadcrumb_navigation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fhow_to%2Flayout_cookbook%2Fbreadcrumb_navigation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")