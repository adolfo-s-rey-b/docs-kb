*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/paint#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/paint#mdn-search)
    

`paint()` CSS function
======================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/80)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/paint#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`paint()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 defines an [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 value generated with a PaintWorklet.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/paint#syntax)

-----------------------------------------------------------------------------------------------

css

    paint(workletName, ...parameters)
    

where:

[_workletName_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/paint#workletname)

The name of the registered worklet.

[_parameters_ Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/paint#parameters)

Optional additional parameters to pass to the paintWorklet

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/paint#formal_syntax)

-------------------------------------------------------------------------------------------------------------

<paint()> =   
  paint( [<ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
 , <declaration-value>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/paint#examples)

---------------------------------------------------------------------------------------------------

### [Basic CSS paint() usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/paint#basic_css_paint_usage)

Given the following HTML:

html

    <ul>
      <li>item 1</li>
      <li>item 2</li>
      <li>item 3</li>
      <li>item 4</li>
      <li>item 5</li>
      <li>item 6</li>
      <li>item 7</li>
      <li>item 8</li>
      <li>item 9</li>
      <li>item 10</li>
      <li>item N</li>
    </ul>
    

In JavaScript, we register the [paint worklet](https://developer.mozilla.org/en-US/docs/Web/API/PaintWorkletGlobalScope)
:

js

    CSS.paintWorklet.addModule(
      "https://mdn.github.io/houdini-examples/cssPaint/intro/worklets/boxbg.js",
    );
    

In the CSS, we define the `background-image` as a `paint()` type with the worklet name, `boxbg`, along with any variables (ex. `--box-color` and `--width-subtractor`) the worklet will use:

css

    body {
      font: 1.2em / 1.2 sans-serif;
    }
    li {
      background-image: paint(boxbg);
      --box-color: hsl(55 90% 60%);
    }
    
    li:nth-of-type(3n) {
      --box-color: hsl(155 90% 60%);
      --width-subtractor: 20;
    }
    
    li:nth-of-type(3n + 1) {
      --box-color: hsl(255 90% 60%);
      --width-subtractor: 40;
    }
    

### [CSS paint() with parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/paint#css_paint_with_parameters)

You can pass optional arguments in the CSS `paint()` function. In this example, we passed two arguments that control whether the `background-image` on a group of list items is `filled` or has a `stroke` outline, and the `width` of that outline:

    <ul>
      <li>item 1</li>
      <li>item 2</li>
      <li>item 3</li>
      <li>item 4</li>
      <li>item 5</li>
      <li>item 6</li>
      <li>item 7</li>
      <li>item 8</li>
      <li>item 9</li>
      <li>item 10</li>
      <li>item N</li>
    </ul>
    

    CSS.paintWorklet.addModule(
      "https://mdn.github.io/houdini-examples/cssPaint/intro/worklets/hilite.js",
    );
    

css

    body {
      font: 1.2em / 1.2 sans-serif;
    }
    
    li {
      --box-color: hsl(55 90% 60% / 100%);
      background-image: paint(hollow-highlights, stroke, 2px);
    }
    
    li:nth-of-type(3n) {
      --box-color: hsl(155 90% 60% / 100%);
      background-image: paint(hollow-highlights, filled, 3px);
    }
    
    li:nth-of-type(3n + 1) {
      --box-color: hsl(255 90% 60% / 100%);
      background-image: paint(hollow-highlights, stroke, 1px);
    }
    

We've included a custom property in the selector block defining a boxColor. Custom properties are accessible to the PaintWorklet.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/paint#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Painting API Level 1  <br>\# paint-notation](https://drafts.css-houdini.org/css-paint-api/#paint-notation) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/paint#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/paint#see_also)

---------------------------------------------------------------------------------------------------

*   [`PaintWorkletGlobalScope`](https://developer.mozilla.org/en-US/docs/Web/API/PaintWorkletGlobalScope)
    
*   [CSS Painting API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Painting_API)
    
*   [Using the CSS Painting API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Painting_API/Guide)
    
*   [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
    
*   [Canvas API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/paint/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/image/paint/index.md?plain=1 "Folder: en-us/web/css/reference/values/image/paint (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fimage%2Fpaint&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fimage%2Fpaint%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fimage%2Fpaint%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fimage%2Fpaint%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")