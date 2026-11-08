*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-index#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-index#mdn-search)
    

`sibling-index()` CSS function
==============================

Baseline 2026

Newly available

Since August 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-index#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`sibling-index()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 returns an integer representing the position of the current element in the DOM tree relative to all its sibling elements. The returned value is the index number of the contextual child's position among all the sibling elements within a parent element, with the first child returning `1` and the last child, returning the `length` of [`Element.children`](https://developer.mozilla.org/en-US/docs/Web/API/Element/children)
.

**Note:** Like the [`:nth-child()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-child)
 pseudo-class, `sibling-index()` starts from 1, not 0.

**Note:** The [`counter()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)
 function provides a similar result but it returns a `<string>` (which is more suitable for [generated content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Generated_content)
, while `sibling-index()` returns an `<integer>` (which can be used for calculations).

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-index#try_it)

-------------------------------------------------------------------------------------------------

    --width: calc(sibling-index() * 30px);
    

    --width: calc(sibling-index() * 20px);
    

    --width: calc(sibling-index() * 10px);
    

    --width: 100px;
    

    <ul id="example-element">
      <li>1</li>
      <li>2</li>
      <li>3</li>
      <li>4</li>
      <li>5</li>
      <li>6</li>
      <li>7</li>
      <li>8</li>
      <li>9</li>
      <li>10</li>
    </ul>
    

    #example-element {
      list-style-type: none;
      padding: 0;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
    }
    
    #example-element > li {
      text-align: center;
      padding: 2px;
      border-radius: 8px;
      width: var(--width, calc(sibling-index() * 30px));
      color: white;
      background-color: hsl(
        calc(360deg / sibling-count() * sibling-index()) 50% 50%
      );
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-index#syntax)

-------------------------------------------------------------------------------------------------

css

    sibling-index()
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-index#parameters)

The `sibling-index()` function doesn't accept parameters.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-index#return_value)

An integer; the position of the current element in the DOM tree's sibling order.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-index#examples)

-----------------------------------------------------------------------------------------------------

### [Dynamic list width](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-index#dynamic_list_width)

This example demonstrates how to dynamically increase the width of each [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 item in the [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
 by `50px`.

#### HTML

html

    <ul>
      <li>One</li>
      <li>Two</li>
      <li>Three</li>
      <li>Four</li>
    </ul>
    

#### CSS

css

    li {
      width: calc(sibling-index() * 50px);
      background-color: #ffaaaa;
    }
    

#### Results

### [Sequential animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-index#sequential_animations)

Combining `sibling-index()` with CSS animations opens new possibilities. In this example, the opacity of elements in sequential order by setting an [`animation-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay)
 based on their order in the DOM.

#### HTML

We include a container element with four children:

html

    <ul>
      <li>One</li>
      <li>Two</li>
      <li>Three</li>
      <li>Four</li>
    </ul>
    

#### CSS

We apply the `fade-in` animation to each element. We use the `sibling-index()` function within a [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
 function to set the duration of the `animation-delay` based on the source element's position in the source order. The [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
 applies the animation's `0%` keyframe until the `animation-duration` expires.

css

    ul {
      list-style-type: none;
      padding: 0;
      margin: 0;
    }
    
    li {
      animation-name: fade-in;
      animation-duration: 1s;
      animation-iteration-count: 1;
      animation-timing-function: linear;
      animation-fill-mode: backwards;
      animation-delay: calc(1s * sibling-index());
    }
    
    @keyframes fade-in {
      from {
        opacity: 0;
      }
      to {
        opacity: 1;
      }
    }
    

#### Results

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-index#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 5  <br>\# funcdef-sibling-index](https://drafts.csswg.org/css-values-5/#funcdef-sibling-index) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-index#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-index#see_also)

-----------------------------------------------------------------------------------------------------

*   [`sibling-count()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-count)
    
*   [`counter()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-index/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/sibling-index/index.md?plain=1 "Folder: en-us/web/css/reference/values/sibling-index (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fsibling-index&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fsibling-index%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fsibling-index%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fsibling-index%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")