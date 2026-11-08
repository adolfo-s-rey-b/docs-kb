*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme#mdn-search)
    

`prefers-color-scheme` CSS media feature
========================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`prefers-color-scheme`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using#targeting_media_features)
 is used to detect if a user has requested light or dark color themes. A user indicates their preference through an operating system setting (e.g., light or dark mode) or a user agent setting.

[Embedded elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme#embedded_elements)

---------------------------------------------------------------------------------------------------------------------------------------

For SVG and iframes, `prefers-color-scheme` lets you set a CSS style for the SVG or iframe based on the [`color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme)
 of the parent element in the web page. SVGs must be used embedded (i.e., `<img src="circle.svg" alt="circle" />`) as opposed to [inlined in HTML](https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/SVG_in_HTML#basic_example)
. An example of using `prefers-color-scheme` in SVGs can be found in the ["Inherited color scheme in embedded elements"](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme#inherited_color_scheme_in_embedded_elements)
 section.

Using `prefers-color-scheme` is allowed in [cross-origin](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy#cross-origin_network_access)
 `<svg>` and `<iframe>` elements. Cross-origin elements are elements retrieved from a different host than the page that is referencing them. To learn more about SVGs, see the [SVG documentation](https://developer.mozilla.org/en-US/docs/Web/SVG)
 and for more information about iframes, see the [iframe documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme#syntax)

-----------------------------------------------------------------------------------------------------------------

[`light`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme#light)

Indicates that user has notified that they prefer an interface that has a light theme, or has not expressed an active preference.

[`dark`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme#dark)

Indicates that user has notified that they prefer an interface that has a dark theme.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme#examples)

---------------------------------------------------------------------------------------------------------------------

### [Detecting a dark or light theme](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme#detecting_a_dark_or_light_theme)

A common usage is to use a light color scheme by default, and then use `prefers-color-scheme: dark` to override the colors to a darker variant. It is also possible to do it the other way around.

This example shows both options: Theme A uses light colors, but can be overridden to dark colors. Theme B uses dark colors, but can be overridden to light colors. In the end, if the browser supports `prefers-color-scheme`, both themes will be light or dark.

#### HTML

html

    <div class="box theme-a">Theme A (initial)</div>
    <div class="box theme-a adaptive">Theme A (changed if dark preferred)</div>
    <br />
    
    <div class="box theme-b">Theme B (initial)</div>
    <div class="box theme-b adaptive">Theme B (changed if light preferred)</div>
    

#### CSS

    div.box {
      display: inline-block;
      padding: 1em;
      margin: 6px;
      outline: 2px solid black;
      width: 12em;
      height: 2em;
      vertical-align: middle;
    }
    

Theme A (brown) uses a light color scheme by default, but will switch to a dark scheme based on the media query:

css

    .theme-a {
      background: #ddccaa;
      color: #773311;
    }
    @media (prefers-color-scheme: dark) {
      .theme-a.adaptive {
        background: #775533;
        color: #ddccbb;
        outline: 5px dashed black;
      }
    }
    

Theme B (blue) uses a dark color scheme by default, but will switch to a light scheme based on the media query:

css

    .theme-b {
      background: #444477;
      color: #bbbbdd;
    }
    @media (prefers-color-scheme: light) {
      .theme-b.adaptive {
        background: #bbccdd;
        color: #333344;
        outline: 5px dotted black;
      }
    }
    

#### Result

The left boxes shows Theme A and Theme B as they would appear without the `prefers-color-scheme` media query. The right boxes show the same themes, but one of them will be changed to a darker or lighter variant based on the user's active color scheme. The outline of one box will be dashed or dotted if it was changed based on your browser or operating systems settings.

### [Inherited color scheme in embedded elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme#inherited_color_scheme_in_embedded_elements)

The following example shows how to use the `prefers-color-scheme` media feature in an embedded element to inherit a color scheme from a parent element. A script is used to set the source of the `<img>` elements and their `alt` attributes. This would normally be done in HTML as `<img src="circle.svg" alt="circle" />`.

You should see three circles, with one drawn in a different color. The first circle inherits the `color-scheme` from the OS and can be toggled using the system OS's theme switcher.

The second and third circles inherit the `color-scheme` from the embedding element; the `@media` query allows setting styles of the SVG content based on the parent element's `color-scheme`. In this case, the parent element with a `color-scheme` CSS property is a `<div>`.

html

    <div>
      <img alt="circle" src="" />
    </div>
    <div class="light">
      <img alt="circle" src="" />
    </div>
    <div class="dark">
      <img alt="circle" src="" />
    </div>
    

css

    .light {
      color-scheme: light;
    }
    
    .dark {
      color-scheme: dark;
    }
    

js

    // Embed an SVG for all <img> elements
    for (const img of document.querySelectorAll("img")) {
      img.src = `data:image/svg+xml;base64,${window.btoa(`
        <svg width="32" height="32" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
          <style>
            :root { color: blue }
            @media (prefers-color-scheme: dark) {
              :root { color: purple }
            }
          </style>
          <circle fill="currentColor" cx="16" cy="16" r="16"/>
        </svg>
      `)}`;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme#specifications)

---------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Media Queries Level 5  <br>\# prefers-color-scheme](https://drafts.csswg.org/mediaqueries-5/#prefers-color-scheme) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [`color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme)
     property
*   [`<meta name="color-scheme">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/color-scheme)
    
*   [`Sec-CH-Prefers-Color-Scheme`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-CH-Prefers-Color-Scheme)
     HTTP Header [User Agent Client Hint](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Client_hints#user_agent_client_hints)
    
*   [Simulate prefers-color-scheme in Firefox](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/how_to/examine_and_edit_css/index.html#view-media-rules-for-prefers-color-scheme "External link (opens in new tab)")
    
*   [Video: Coding a Dark Mode for your Website](https://www.youtube.com/watch?v=jmepqJ5UbuM "External link (opens in new tab)")
    
*   [Redesigning your product and website for dark mode](https://stuffandnonsense.co.uk/blog/redesigning-your-product-and-website-for-dark-mode/ "External link (opens in new tab)")
    
*   Changing color schemes in [Windows](https://blogs.windows.com/windowsexperience/2019/04/01/windows-10-tip-dark-theme-in-file-explorer/ "External link (opens in new tab)")
    , [macOS](https://developer.apple.com/design/human-interface-guidelines/dark-mode "External link (opens in new tab)")
    , [Android](https://www.theverge.com/2019/5/7/18530599/google-android-q-features-hands-on-dark-mode-gestures-accessibility-io-2019 "External link (opens in new tab)")
    , or [other platforms](https://support.mozilla.org/en-US/questions/1271928 "External link (opens in new tab)")
    .

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 4, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/prefers-color-scheme/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@media/prefers-color-scheme (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fprefers-color-scheme&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fprefers-color-scheme%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Fprefers-color-scheme%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Fprefers-color-scheme%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc655f38c10ba17b853b0e66b43cf4cf2b176e424%0A*+Document+last+modified%3A+2026-08-04T23%3A29%3A57.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")