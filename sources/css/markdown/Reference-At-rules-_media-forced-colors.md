*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors#mdn-search)
    

`forced-colors` CSS media feature
=================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`forced-colors`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 is used to detect if the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 has enabled a forced colors mode where it enforces a user-chosen limited color palette on the page. An example of a forced colors mode is Windows High Contrast mode.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors#syntax)

----------------------------------------------------------------------------------------------------------

The `forced-colors` media feature indicates whether or not the browser is currently in forced-colors mode.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors#values)

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors#none)

Forced colors mode is not active; the page's colors are not being forced into a limited palette.

[`active`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors#active)

Indicates that forced colors mode is active. The browser provides the color palette to authors through the [CSS system color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/system-color)
 keywords and, if appropriate, triggers the appropriate value of [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme)
 so that authors can adapt the page. The browser selects the value for `prefers-color-scheme` based on the lightness of the `Canvas` system color (see the [color adjust spec](https://drafts.csswg.org/css-color-adjust-1/#forced "External link (opens in new tab)")
 for more details).

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors#usage_notes)

--------------------------------------------------------------------------------------------------------------------

### [Properties affected by forced-color mode](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors#properties_affected_by_forced-color_mode)

In forced colors mode, the values of the following properties are treated as if they have no author-level values specified. That is, browser-specified values are used instead. The browser-specified values do not affect the style cascade; the values are instead forced by the browser at paint time.

These browser-specified values are selected from the set of system colors — this ensures a consistent contrast for common UI elements for users that have forced colors enabled.

*   [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
    
*   [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    
*   [`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)
    
*   [`text-emphasis-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-color)
    
*   [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
    
*   [`outline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color)
    
*   [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
    
*   [`-webkit-tap-highlight-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-tap-highlight-color)
    
*   [SVG fill attribute](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill)
    
*   [SVG stroke attribute](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke)
    

Additionally the following properties have special behavior in forced colors mode:

*   [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
     is forced to 'none'
*   [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
     is forced to 'none'
*   [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
     is forced to 'none' for values that are not url-based
*   [`color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme)
     is forced to 'light dark'
*   [`scrollbar-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color)
     is forced to 'auto'

The system colors that are forced for the above properties depend on the context of the element. For example the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 property on button element will be forced to `ButtonText`. On normal text it will be forced to `CanvasText`. See the [list of system colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/system-color)
 for additional details of when each might be appropriate in various UI contexts.

**Note:** User agents choose system colors based on native element semantics, _not_ on added ARIA roles. As an example, adding `role="button"` to a `div` will **not** cause an element's color to be forced to `ButtonText`

In addition to these adjustments, browsers will help ensure text legibility by drawing "backplates" behind text. This is particularly important for preserving contrast when text is placed on top of images.

There are some cases where the user agent does not force the values for the above properties:

When [`forced-color-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/forced-color-adjust)
 is set to `none` on an element, none of the forced color values will apply, and author styles will be applied as normal. Additionally, the backplate for text will be disabled.

When [`forced-color-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/forced-color-adjust)
 is set to `preserve-parent-color` on an element, and the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 value on the element does not inherit from its parent, then the element will behave the same as setting `preserve-parent-color` to `none`.

When a [system color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/system-color)
 is specified, it will be used instead of the value that would otherwise have been forced.

You can also use system colors with any property _other_ than those listed above, to ensure that the rest of the page integrates with the restricted color palette available in forced colors mode.

### [Accessibility concerns](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors#accessibility_concerns)

In general, web authors should **not** be using the `forced-colors` media feature to create a separate design for users with this feature enabled. Instead, its intended usage is to make small tweaks to improve usability or legibility when the default application of forced colors does not work well for a given portion of a page.

The high contrast provided by forced colors mode's reduced palette and text backplates is often essential for some users to be able to read or use a given website, so adjustments that affect content should be chosen carefully and targeted to content that is otherwise not legible.

### [User preferences](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors#user_preferences)

This media feature is active only if the user has enabled color scheme preferences in their operating system. One example of such a feature is High Contrast mode on Windows.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors#examples)

--------------------------------------------------------------------------------------------------------------

**Note:** The below example will only work when using a browser that supports this media feature, and with a preference such as High Contrast mode enabled in your OS.

This example is a button that normally gets its contrast via [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
. Under forced colors mode, box-shadow is forced to none, so the example uses the forced-colors media feature to ensure there is a border of the appropriate color (ButtonText in this case)

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors#html)

html

    <button class="button">Press me!</button>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors#css)

css

    .button {
      border: 0;
      padding: 10px;
      box-shadow:
        -2px -2px 5px gray,
        2px 2px 5px gray;
    }
    
    @media (forced-colors: active) {
      .button {
        /* Use a border instead, since box-shadow is forced to 'none' in forced-colors mode */
        border: 2px ButtonText solid;
      }
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Media Queries Level 5  <br>\# forced-colors](https://drafts.csswg.org/mediaqueries-5/#forced-colors) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors#see_also)

--------------------------------------------------------------------------------------------------------------

*   [@media](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
    
*   [Styling for Windows high contrast with standards for forced colors.](https://blogs.windows.com/msedgedev/2020/09/17/styling-for-windows-high-contrast-with-new-standards-for-forced-colors/ "External link (opens in new tab)")
    
*   [`forced-color-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/forced-color-adjust)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/forced-colors/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@media/forced-colors (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fforced-colors&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fforced-colors%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fforced-colors%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fforced-colors%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F67d40334c8b90e4623f3b0d3aea466b9882d8236%0A*+Document+last+modified%3A+2026-04-20T16%3A07%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")