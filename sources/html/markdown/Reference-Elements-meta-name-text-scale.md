*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/text-scale#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/text-scale#mdn-search)
    

<meta name="text-scale">
========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/517)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/text-scale#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/text-scale#browser_compatibility)
 carefully before using this in production.

The **`text-scale`** value for the [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name)
 attribute of a [`<meta>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta)
 element enables opting the page in to having the [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)
 root element's initial [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 scale in proportion to OS and browser-level text scale settings.

**Warning:** If you include `<meta name="text-scale" content="scale" />` on your website to opt in to this text scaling behavior, you must test that it supports text sizes up to the maximum text-scaling factor for your target platforms. This typically ranges from 200% to over 300% on mobile platforms, with some accessibility features enabling even larger text scaling. Make sure your website does not look broken for users setting larger or smaller operating system font-size preferences.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/text-scale#usage_notes)

---------------------------------------------------------------------------------------------------------------------

A `<meta name="text-scale">` element has the following additional attributes:

[`content`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#content)

Specifies the [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 scale opt-in behavior. Its value is a keyword, which can be one of the following:

[`scale`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/text-scale#scale)

Opts the page in to having the [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)
 root element's initial [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 scale in proportion to OS and browser-level text scale settings. It also causes the browser to disable existing browser-based mechanisms and heuristics (for example, text auto-sizing on mobile).

[`legacy`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/text-scale#legacy)

The default value. The page is not opted in to the root element's `font-size` scaling in proportion to OS and browser-level text scale settings. This has the same effect as not including the `<meta>` element at all (OS-level font preferences are ignored.)

[Description](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/text-scale#description)

---------------------------------------------------------------------------------------------------------------------

The `<meta name="text-scale" content="scale" />` element can be included in a document's [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head)
 to signal to the browser that the page is sized in a way that will scale well across various user-selected font size preferences; it also disables existing browser-based mechanisms and heuristics.

Specifically, it defines the value of the [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)
 root element's initial `font-size` to scale in proportion to user-defined OS and browser-level font size settings. The [`initial`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial)
 value of the root [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 is `medium`, which defines the [`rem`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#rem)
 unit's value. Provided you set or allow the root `font-size` to default to a [local or root font-relative `<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Numeric_data_types#local_font-relative_lengths)
 unit, any subsequent keyword (like `medium`) or font-relative length (such as `em` and `rem`) will be scaled in proportion to OS or browser font size settings.

For example, with `<meta name="text-scale" content="scale">` included on the page, the following rule:

css

    p {
      font-size: medium;
    }
    

would result in all [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 elements receiving a scaled font size. You could also set `font-size` to `initial` to get the same effect.

On mobile platforms, this is not the case by default. `<meta name="text-scale" content="scale" />` enables this scaling. On desktop platforms, the effect is that the [`env(preferred-text-scale)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/env#preferred-text-scale)
 environment variable is made to reflect the multiplier that corresponds to browser font size settings, but other than that, it has no discernable advantage.

### [Usage summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/text-scale#usage_summary)

To summarize, set `scale` only if your app is designed to support font scaling. Recommended usage is to:

1.  Include `<meta name="text-scale" content="scale" />` in the `<head>` of your page.
2.  Don't override the initial [`:root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:root)
     `font-size` with an [absolute length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#absolute_length_units)
     value (like `16px`).
3.  Use only [font-relative units](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#relative_length_units_based_on_font)
     such as `em`/`rem` or keywords such as `small`, `x-large`, etc. to size content.

### [`<meta name="text-scale">` versus `env(preferred-text-scale)`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/text-scale#meta_nametext-scale_versus_envpreferred-text-scale)

Using `<meta name="text-scale" />` to size dimensions relative to OS text scale settings is recommended over the [`env(preferred-text-scale)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/env#preferred-text-scale)
 environment variable. They have similar effects on mobile, but `<meta>` also provides improvements for desktop browsers (and is easier to use).

Avoid using both features together, as text scaling may be applied twice, making small font-relative dimensions smaller and large font-relative dimensions larger.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/text-scale#examples)

---------------------------------------------------------------------------------------------------------------

### [Meta viewport text-scale demonstration](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/text-scale#meta_viewport_text-scale_demonstration)

This example demonstrates the effect of `<meta name="text-scale" content="scale">`.

#### HTML

We include the `<meta name="text-scale" content="scale">` element in the document `<head>`, plus a [`<meta name="viewport">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport)
 element to ensure correct display on mobile devices. We also include some text content inside [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 elements with different `class` attributes set on them to allow us to target them with different styles.

html

    <!doctype html>
    <html lang="en-US">
      <head>
        <meta name="text-scale" content="scale" />
        <meta name="viewport" content="width=device-width" />
      </head>
      <body>
        <p class="text-scale">
          This font size obeys the user's font preferences, whether those
          preferences are specified at the operating system level or the user agent
          level.
        </p>
        <p class="fixed">
          This font size does NOT respect the user's font preferences, even with
          text-scale set.
          <span class="text-scale">But this font size does!</span>
        </p>
      </body>
    </html>
    

    <!doctype html>
    <html lang="en-US">
      <head>
        <meta name="viewport" content="width=device-width" />
      </head>
      <body>
        <p class="text-scale">
          This font size does not obey the user's font preferences, whether those
          preferences are specified at the operating system level or the user agent
          level.
        </p>
        <p class="fixed">
          This font size does NOT respect the user's font preferences.
          <span class="text-scale">Neither does this!</span>
        </p>
      </body>
    </html>
    

#### CSS

Text containers with a `class` of `text-scale` are given a [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 of `1rem`, which means that in browsers that support `<meta name="text-scale" content="scale">`, that text will scale as the OS/browser font settings are changed. Text containers with a `class` of `fixed` are given a `font-size` of `20px`, which means that this text will remain at a fixed size as the OS/browser font settings are changed.

css

    .text-scale {
      font-size: 1rem;
    }
    
    .fixed {
      font-size: 20px;
    }
    

#### Result

This version has the `<meta name="text-scale">` element included:

This version does NOT have the `<meta name="text-scale">` element included:

Test these examples in a mobile browser. Change the preferred font size in the mobile device's display or accessibility settings. Note how, in the first example, when `<meta name="text-scale">` is included, the top and bottom lines of text scale in proportion to the OS settings, whereas the middle line, with the `font-size` set using absolute units, doesn't change size. Without the `<meta name="text-scale">` element, text does not scale proportionally with OS settings.

To make testing easier, you can open both versions full screen in a separate tab using the links below:

*   [Example with `<meta name="text-scale">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/text-scale#livesample_fullscreen=text-scale)
    
*   [Example without `<meta name="text-scale">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/text-scale#livesample_fullscreen=no-text-scale)
    

### [A text-scale-responsive layout](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/text-scale#a_text-scale-responsive_layout)

This example demonstrates that with `<meta name="text-scale">` applied to a page, font-relative sizes can be used inside [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
 queries to cause mobile browsers to automatically adjust breakpoints as the OS text size is changed.

#### HTML

Like the previous example, our markup again includes the `<meta name="text-scale">` and `<meta name="viewport">` elements in the `<head>`. In this demo, the body content contains two elements — [`<main>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main)
 and [`<aside>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/aside)
 — to represent a main content column and a sidebar.

html

    <!doctype html>
    <html lang="en-US">
      <head>
        <meta name="text-scale" content="scale" />
        <meta name="viewport" content="width=device-width" />
      </head>
      <body>
        <main>Main content</main>
        <aside>Aside content</aside>
      </body>
    </html>
    

#### CSS

By default, the main content and sidebar are laid out one below the other. We include a [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
 query that lays the elements out side-by-side using [CSS Grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 when the viewport becomes wider than `35rem`.

    body {
      margin: 0;
    }
    
    main,
    aside {
      background-color: silver;
      padding: 24px;
      font-size: 1.5rem;
    }
    

css

    @media (width > 35rem) {
      body {
        display: grid;
        gap: 24px;
        grid-template-columns: 1fr 18.75rem;
      }
    }
    

#### Result

Test this in a mobile browser. You'll see that, as the OS font size is increased, the breakpoint size increases in proportion to it. At larger OS font sizes, the main and aside will start to appear on top of each other whereas previously they appeared side-by-side. You may have to look at it in landscape orientation to see the effect.

You can open the demo in a separate tab using the link below to make testing easier:

[Responsive layout example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/text-scale#livesample_fullscreen=text-scale-layout)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/text-scale#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 5  <br>\# text-scale-meta](https://drafts.csswg.org/css-fonts-5/#text-scale-meta) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/text-scale#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/text-scale#see_also)

---------------------------------------------------------------------------------------------------------------

*   [`env(preferred-text-scale)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/env#preferred-text-scale)
    
*   [\[meta text-scale\] Support for WebView](https://chromium.googlesource.com/chromium/src/+/b29d63222d10f4c7e620d057578d737969eb7ae3 "External link (opens in new tab)")
     on chromium.googlesource.com (2026)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 4, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/text-scale/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/meta/name/text-scale/index.md?plain=1 "Folder: en-us/web/html/reference/elements/meta/name/text-scale (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmeta%2Fname%2Ftext-scale&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmeta%2Fname%2Ftext-scale%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmeta%2Fname%2Ftext-scale%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmeta%2Fname%2Ftext-scale%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4c58f4735f986a91bee1b77e336143630df727a2%0A*+Document+last+modified%3A+2026-09-04T04%3A21%3A12.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")