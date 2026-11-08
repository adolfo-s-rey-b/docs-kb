*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar#mdn-search)
    

`::-webkit-scrollbar` CSS pseudo-element
========================================

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The `::-webkit-scrollbar` CSS pseudo-element affects the style of an element's scrollbar when it has scrollable overflow.

The [`scrollbar-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color)
 and [`scrollbar-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width)
 standard properties may be used as alternatives for browsers that do not support this pseudo-element and the related `::-webkit-scrollbar-*` pseudo-elements (see [Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar#browser_compatibility)
).

**Note:** If an element's computed [`scrollbar-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color)
 and [`scrollbar-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width)
 values are anything other than `auto`, they will override `::-webkit-scrollbar-*` styling. Because `scrollbar-color` is inherited, an element is affected when an ancestor sets it, even if the element itself doesn't. Setting `scrollbar-color: auto` on the element restores its `::-webkit-scrollbar-*` styling if it was previously removed by a `scrollbar-color` setting on an ancestor. See [Adding a fallback for scrollbar styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar#adding_a_fallback_for_scrollbar_styles)
 for more details.

[CSS Scrollbar Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar#css_scrollbar_selectors)

--------------------------------------------------------------------------------------------------------------------------------------------

You can use the following pseudo-elements to customize various parts of the scrollbar for WebKit browsers:

*   `::-webkit-scrollbar` — the entire scrollbar.
*   `::-webkit-scrollbar-button` — the buttons on the scrollbar (arrows pointing upwards and downwards that scroll one line at a time).
*   `::-webkit-scrollbar:horizontal` — the horizontal scrollbar.
*   `::-webkit-scrollbar-thumb` — the draggable scrolling handle.
*   `::-webkit-scrollbar-track` — the track (progress bar) of the scrollbar, where there is a gray bar on top of a white bar.
*   `::-webkit-scrollbar-track-piece` — the part of the track (progress bar) not covered by the handle.
*   `::-webkit-scrollbar:vertical` — the vertical scrollbar.
*   `::-webkit-scrollbar-corner` — the bottom corner of the scrollbar, where both horizontal and vertical scrollbars meet. This is often the bottom-right corner of the browser window.
*   `::-webkit-resizer` — the draggable resizing handle that appears at the bottom corner of some elements.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar#accessibility)

------------------------------------------------------------------------------------------------------------------------

Authors should avoid styling scrollbars, as changing the appearance of scrollbars away from the default [breaks external consistency](https://inclusivedesignprinciples.info/#be-consistent "External link (opens in new tab)")
 which negatively impacts usability. If styling scrollbars, ensure there is enough color contrast and touch targets are at least 44px wide and tall. See [Techniques for WCAG 2.0: G183: Using a contrast ratio of 3:1](https://www.w3.org/TR/WCAG20-TECHS/G183.html "External link (opens in new tab)")
 and [Understanding WCAG 2.1 : Target Size](https://www.w3.org/WAI/WCAG21/Understanding/target-size.html "External link (opens in new tab)")
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar#examples)

--------------------------------------------------------------------------------------------------------------

### [Styling scrollbars using `-webkit-scrollbar`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar#styling_scrollbars_using_-webkit-scrollbar)

#### CSS

css

    .visible-scrollbar,
    .invisible-scrollbar,
    .mostly-customized-scrollbar {
      display: block;
      width: 10em;
      overflow: auto;
      height: 2em;
      padding: 1em;
      margin: 1em auto;
      outline: 2px dashed cornflowerblue;
    }
    
    .invisible-scrollbar::-webkit-scrollbar {
      display: none;
    }
    
    /* Demonstrate a "mostly customized" scrollbar
     * (won't be visible otherwise if width/height is specified) */
    .mostly-customized-scrollbar::-webkit-scrollbar {
      width: 5px;
      height: 8px;
      background-color: #aaaaaa; /* or add it to the track */
    }
    
    /* Add a thumb */
    .mostly-customized-scrollbar::-webkit-scrollbar-thumb {
      background: black;
    }
    

#### HTML

html

    <div class="visible-scrollbar">
      <h3>Visible scrollbar</h3>
      <p>
        Etiam sagittis sem sed lacus laoreet, eu fermentum eros auctor. Proin at
        nulla elementum, consectetur ex eget, commodo ante. Sed eros mi, bibendum ut
        dignissim et, maximus eget nibh. Phasellus blandit quam turpis, at mollis
        velit pretium ut. Nunc consequat efficitur ultrices. Nullam hendrerit
        posuere est. Nulla libero sapien, egestas ac felis porta, cursus ultricies
        quam. Vestibulum tincidunt accumsan sapien, a fringilla dui semper in.
        Vivamus consectetur ipsum a ornare blandit. Aenean tempus at lorem sit amet
        faucibus. Curabitur nibh justo, faucibus sed velit cursus, mattis cursus
        dolor. Pellentesque id pretium est. Quisque convallis nisi a diam malesuada
        mollis. Aliquam at enim ligula.
      </p>
    </div>
    
    <div class="invisible-scrollbar">
      <h3>Invisible scrollbar</h3>
      <p>
        Thisisaveeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeerylongword
      </p>
    </div>
    
    <div class="mostly-customized-scrollbar">
      <h3>Custom scrollbar</h3>
      <p>
        Thisisaveeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeerylongword<br />
        And pretty tall<br />
        thing with weird scrollbars.<br />
        Who thought scrollbars could be made weird?
      </p>
    </div>
    

#### Result

### [Adding a fallback for scrollbar styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar#adding_a_fallback_for_scrollbar_styles)

You can use a [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
 at-rule to detect if a browser supports the standard [`scrollbar-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color)
 and [`scrollbar-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width)
 properties, and otherwise use a fallback with `::-webkit-scrollbar-*` pseudo-elements. The following example shows how to apply colors to scrollbars using [`scrollbar-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color)
 if supported and `::-webkit-scrollbar-*` pseudo-elements if not.

#### HTML

html

    <div class="scroll-box">
      <h1>Yoshi</h1>
      <p>
        Yoshi is a fictional dinosaur who appears in video games published by
        Nintendo. Yoshi debuted in Super Mario World (1990) on the SNES as Mario and
        Luigi's sidekick.
      </p>
      <p>
        Throughout the mainline Super Mario series, Yoshi typically serves as
        Mario's trusted steed.
      </p>
      <p>
        With a gluttonous appetite, Yoshi can gobble enemies with his long tongue,
        and lay eggs that doubly function as projectiles.
      </p>
    </div>
    

#### CSS

    .scroll-box {
      overflow: auto;
      width: 20rem;
      height: 5rem;
      border: 2px solid cornflowerblue;
      margin: 2rem auto;
      font-family: monospace;
    }
    

css

    /* For browsers that support `scrollbar-*` properties */
    @supports (scrollbar-color: auto) {
      .scroll-box {
        scrollbar-color: aquamarine cornflowerblue;
      }
    }
    
    /* Otherwise, use `::-webkit-scrollbar-*` pseudo-elements */
    @supports selector(::-webkit-scrollbar) {
      .scroll-box::-webkit-scrollbar {
        background: aquamarine;
      }
      .scroll-box::-webkit-scrollbar-thumb {
        background: cornflowerblue;
      }
    }
    

#### Result

In the example below, you can scroll the bordered box vertically to see the effect of styling the scrollbar.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar#specifications)

--------------------------------------------------------------------------------------------------------------------------

Not part of any standard.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

### [css.selectors.-webkit-scrollbar](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar#css.selectors.-webkit-scrollbar)

### [css.selectors.-webkit-scrollbar-button](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar#css.selectors.-webkit-scrollbar-button)

### [css.selectors.-webkit-scrollbar-thumb](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar#css.selectors.-webkit-scrollbar-thumb)

### [css.selectors.-webkit-scrollbar-track](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar#css.selectors.-webkit-scrollbar-track)

### [css.selectors.-webkit-scrollbar-track-piece](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar#css.selectors.-webkit-scrollbar-track-piece)

### [css.selectors.-webkit-scrollbar-corner](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar#css.selectors.-webkit-scrollbar-corner)

### [css.selectors.-webkit-resizer](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar#css.selectors.-webkit-resizer)

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar#see_also)

--------------------------------------------------------------------------------------------------------------

*   [`scrollbar-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width)
    
*   [`scrollbar-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color)
    
*   [Don't use custom scrollbars](https://ericwbailey.website/published/dont-use-custom-css-scrollbars/ "External link (opens in new tab)")
     (2023)
*   [Scrollbar styling](https://developer.chrome.com/docs/css-ui/scrollbar-styling "External link (opens in new tab)")
     on developer.chrome.com (2024)
*   [Styling Scrollbars](https://webkit.org/blog/363/styling-scrollbars/ "External link (opens in new tab)")
     on WebKit.org (2009)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_-webkit-scrollbar/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_-webkit-scrollbar (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3A-webkit-scrollbar&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_-webkit-scrollbar%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3A-webkit-scrollbar%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_-webkit-scrollbar%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb2a7378d76136b568fe9414f46abda899b2bf700%0A*+Document+last+modified%3A+2026-08-27T11%3A11%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")