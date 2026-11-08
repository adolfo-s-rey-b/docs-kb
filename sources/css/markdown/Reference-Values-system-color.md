*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/system-color#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/system-color#mdn-search)
    

`<system-color>` CSS type
=========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/system-color#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<system-color>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 usually reflects the default color choices used for the different parts of a web page.

However, user agents can provide an accessibility feature called _forced colors mode_, in which colors are restricted into a user- and user agent-defined palette, overriding the author's choice of colors in certain properties. In forced colors mode, `<system-color>` exposes the chosen colors, so that the rest of the page can integrate with them. An example of forced colors mode is [high contrast mode on Windows](https://blogs.windows.com/msedgedev/2020/09/17/styling-for-windows-high-contrast-with-new-standards-for-forced-colors/ "External link (opens in new tab)")
.

In forced colors mode, authors should use colors from the `<system-color>` type for all properties that are _not_ in the set of properties whose colors are overridden. This ensures that the page consistently uses the same color palette across all properties.

Authors can detect forced colors mode using the [`forced-colors`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors)
 media feature.

A `<system-color>` value can be used anywhere a [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 can be used.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/system-color#syntax)

------------------------------------------------------------------------------------------------

Note that these keywords are _case insensitive_, but are listed here with mixed case for readability.

Depending on your settings, the sample colors displayed in the table may change. You can also view this page with different browsers, operating systems, and system settings, to check the differences.

| Keyword | Description | Sample |
| --- | --- | --- |
| `AccentColor` | Background of accented user interface controls. |     |
| `AccentColorText` | Text of accented user interface controls. |     |
| `ActiveText` | Text of active links. |     |
| `ButtonBorder` | Base border color of controls. |     |
| `ButtonFace` | Background color of controls. |     |
| `ButtonText` | Text color of controls. |     |
| `Canvas` | Background of application content or documents. |     |
| `CanvasText` | Text color in application content or documents. |     |
| `Field` | Background of input fields. |     |
| `FieldText` | Text in input fields. |     |
| `GrayText` | Text color for disabled items (for example, a disabled control). |     |
| `Highlight` | Background of selected items. |     |
| `HighlightText` | Text color of selected items. |     |
| `LinkText` | Text of non-active, non-visited links. |     |
| `Mark` | Background of text that has been specially marked (such as by the HTML `mark` element). |     |
| `MarkText` | Text that has been specially marked (such as by the HTML `mark` element). |     |
| `SelectedItem` | Background of selected items, for example, a selected checkbox. |     |
| `SelectedItemText` | Text of selected items. |     |
| `VisitedText` | Text of visited links. |     |

**Note:** To reduce the risk of [fingerprinting](https://developer.mozilla.org/en-US/docs/Glossary/Fingerprinting)
, some browsers return a fixed value for `AccentColor` and `AccentColorText` unless they are used in certain restricted circumstances. See [browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/system-color#browser_compatibility)
 for details.

### [Deprecated system color keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/system-color#deprecated_system_color_keywords)

The following keywords were defined in earlier versions of the CSS Color Module. They are now deprecated for use on public web pages.

| Keyword | Description | Replacement | Sample |
| --- | --- | --- | --- |
| `ActiveBorder` | Active window border | `ButtonBorder` |     |
| `ActiveCaption` | Active window caption. Should be used with `CaptionText` as foreground color. | `Canvas` |     |
| `AppWorkspace` | Background color of multiple document interface. | `Canvas` |     |
| `Background` | Desktop background. | `Canvas` |     |
| `ButtonHighlight` | The color of the border facing the light source for 3-D elements that appear 3-D due to that layer of surrounding border. | `ButtonFace` |     |
| `ButtonShadow` | The color of the border away from the light source for 3-D elements that appear 3-D due to that layer of surrounding border. | `ButtonFace` |     |
| `CaptionText` | Text in caption, size box, and scrollbar arrow box. Should be used with the `ActiveCaption` background color. | `CanvasText` |     |
| `InactiveBorder` | Inactive window border. | `ButtonBorder` |     |
| `InactiveCaption` | Inactive window caption. Should be used with the `InactiveCaptionText` foreground color. | `Canvas` |     |
| `InactiveCaptionText` | Color of text in an inactive caption. Should be used with the `InactiveCaption` background color. | `GrayText` |     |
| `InfoBackground` | Background color for tooltip controls. Should be used with the `InfoText` foreground color. | `Canvas` |     |
| `InfoText` | Text color for tooltip controls. Should be used with the `InfoBackground` background color. | `CanvasText` |     |
| `Menu` | Menu background. Should be used with the `MenuText` or `-moz-MenuBarText` foreground color. | `Canvas` |     |
| `MenuText` | Text in menus. Should be used with the `Menu` background color. | `CanvasText` |     |
| `Scrollbar` | Background color of scroll bars. | `Canvas` |     |
| `ThreeDDarkShadow` | The color of the darker (generally outer) of the two borders away from the light source for 3-D elements that appear 3-D due to two concentric layers of surrounding border. | `ButtonBorder` |     |
| `ThreeDFace` | The face background color for 3-D elements that appear 3-D due to two concentric layers of surrounding border. Should be used with the `ButtonText` foreground color. | `ButtonFace` |     |
| `ThreeDHighlight` | The color of the lighter (generally outer) of the two borders facing the light source for 3-D elements that appear 3-D due to two concentric layers of surrounding border. | `ButtonBorder` |     |
| `ThreeDLightShadow` | The color of the darker (generally inner) of the two borders facing the light source for 3-D elements that appear 3-D due to two concentric layers of surrounding border. | `ButtonBorder` |     |
| `ThreeDShadow` | The color of the lighter (generally inner) of the two borders away from the light source for 3-D elements that appear 3-D due to two concentric layers of surrounding border. | `ButtonBorder` |     |
| `Window` | Window background. Should be used with the `WindowText` foreground color. | `Canvas` |     |
| `WindowFrame` | Window frame. | `ButtonBorder` |     |
| `WindowText` | Text in windows. Should be used with the `Window` background color. | `CanvasText` |     |

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/system-color#examples)

----------------------------------------------------------------------------------------------------

### [Using system colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/system-color#using_system_colors)

In this example we have a button that normally gets its contrast using the [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
 property. In forced colors mode, `box-shadow` is forced to `none`, so the example uses the `forced-colors` media feature to ensure there is a border of the appropriate color (`ButtonBorder` in this case).

#### HTML

#### CSS

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/system-color#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Color Module Level 4  <br>\# css-system-colors](https://drafts.csswg.org/css-color/#css-system-colors) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/system-color#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/system-color#see_also)

----------------------------------------------------------------------------------------------------

*   [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
    : the data type these keywords belong to

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/system-color/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/system-color/index.md?plain=1 "Folder: en-us/web/css/reference/values/system-color (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fsystem-color&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fsystem-color%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fsystem-color%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fsystem-color%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4d49c28381a2b736e205215b75388945e44a028c%0A*+Document+last+modified%3A+2026-08-12T01%3A33%3A12.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")