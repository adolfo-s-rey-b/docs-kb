*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/aspect-ratio#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/aspect-ratio#mdn-search)
    

`aspect-ratio` CSS media feature
================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/aspect-ratio#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`aspect-ratio`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 can be used to test the [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
 of the [viewport](https://developer.mozilla.org/en-US/docs/Glossary/Viewport)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/aspect-ratio#syntax)

---------------------------------------------------------------------------------------------------------

The `aspect-ratio` feature is specified as a [`<ratio>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio)
 value representing the width-to-height aspect ratio of the viewport. It is a range feature, meaning you can also use the prefixed **`min-aspect-ratio`** and **`max-aspect-ratio`** variants to query minimum and maximum values, respectively.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/aspect-ratio#examples)

-------------------------------------------------------------------------------------------------------------

In the example below, a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element is contained in an [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
. The iframe creates its own viewport. Resize the `<iframe>` to see `aspect-ratio` in action.

Note that, when none of the media query conditions are true, the background will turn white because none of the below rules will be applied to the `<div>` inside the `<iframe>`. See if you can find which width and height values trigger this!

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/aspect-ratio#html)

html

    <iframe
      id="outer"
      srcdoc="<div id='inner'>Watch this element as you resize iframe viewport's width and height.</div>">
    </iframe>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/aspect-ratio#css)

css

    /* Minimum allowed aspect ratio */
    /* Select aspect ratios 8/5 = 1.6 and above */
    @media (min-aspect-ratio: 8/5) {
      div {
        background: #9999ff; /* blue */
      }
    }
    
    /* Maximum allowed aspect ratio */
    /* Select aspect ratios 3/2 = 1.5 and below */
    @media (max-aspect-ratio: 3/2) {
      div {
        background: #99ff99; /* green */
      }
    }
    
    /* Exact aspect ratio, put it at the bottom to avoid override */
    @media (aspect-ratio: 1/1) {
      div {
        background: #ff9999; /* red */
      }
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/aspect-ratio#result)

    <label id="wf" for="w">width:165</label>
    <input id="w" name="w" type="range" min="100" max="250" step="5" value="165" />
    <label id="hf" for="w">height:165</label>
    <input id="h" name="h" type="range" min="100" max="250" step="5" value="165" />
    <label id="ratio">aspect-ratio: 165/165 = 1</label>
    
    <iframe
      id="outer"
      srcdoc="<style> @media (min-aspect-ratio: 8/5) { div { background: #9999ff; } } @media (max-aspect-ratio: 3/2) { div { background: #99ff99; } } @media (aspect-ratio: 1/1) { div { background: #ff9999; } }</style><div id='inner'> Watch this element as you resize iframe viewport's width and height.</div>">
    </iframe>
    

    iframe {
      display: block;
      border: 1px dashed black;
    }
    

    outer.style.width = outer.style.height = "165px";
    
    const updateRatio = () => {
      ratio.textContent = `aspect-ratio: ${w.value}/${h.value} = ${(w.value / h.value).toFixed(2)}`;
    };
    
    w.onchange = w.oninput = () => {
      outer.style.width = `${w.value}px`;
      wf.textContent = `width: ${w.value}`;
      updateRatio();
    };
    
    h.onchange = h.oninput = () => {
      outer.style.height = `${h.value}px`;
      hf.textContent = `height: ${h.value}`;
      updateRatio();
    };
    

Note the `min-aspect-ratio: 8/5` sets the _lower_ bound to 1.6, so this media query selects elements with aspect ratios 1.6 and above. The `max-aspect-ratio: 3/2` sets the _upper_ bound, so this media query selects elements with aspect ratios 1.5 and below. The `aspect-ratio: 1/1` overrides the max aspect ratio rule because it has been declared after and selects elements with aspect ratios exactly `1`.

From the initial state, as you reduce height, the aspect ratio starts increasing from one. So the div's background color goes from red(1) < green(1.5) < white < blue(1.6).

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/aspect-ratio#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Media Queries Level 4  <br>\# aspect-ratio](https://drafts.csswg.org/mediaqueries/#aspect-ratio) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/aspect-ratio#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/aspect-ratio#see_also)

-------------------------------------------------------------------------------------------------------------

*   [Understanding `aspect-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios)
    
*   [Using Media Queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
    
*   [@media](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/aspect-ratio/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/aspect-ratio/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@media/aspect-ratio (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Faspect-ratio&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Faspect-ratio%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2Faspect-ratio%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2Faspect-ratio%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F67d40334c8b90e4623f3b0d3aea466b9882d8236%0A*+Document+last+modified%3A+2026-04-20T16%3A07%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")