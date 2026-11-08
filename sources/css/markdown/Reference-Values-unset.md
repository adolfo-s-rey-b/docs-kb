*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset#mdn-search)
    

`unset` CSS keyword
===================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2016.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`unset`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 keyword resets a property to its inherited value if the property naturally inherits from its parent, and to its [initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
 if not. In other words, it behaves like the [`inherit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit)
 keyword in the first case, when the property is an [inherited property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance#inherited_properties)
, and like the [`initial`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial)
 keyword in the second case, when the property is a [non-inherited property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance#non-inherited_properties)
.

**`unset`** can be applied to any CSS property, including the CSS shorthand property [`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset#examples)

---------------------------------------------------------------------------------------------

### [Color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset#color)

[`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color#formal_definition)
 is an inherited property.

#### HTML

html

    <p>This text is red.</p>
    <div class="foo">
      <p>This text is also red.</p>
    </div>
    <div class="bar">
      <p>This text is green (default inherited value).</p>
    </div>
    

#### CSS

css

    .foo {
      color: blue;
    }
    
    .bar {
      color: green;
    }
    
    p {
      color: red;
    }
    
    .bar p {
      color: unset;
    }
    

#### Result

### [Border](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset#border)

[`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border#formal_definition)
 is a non-inherited property.

#### HTML

html

    <p>This text has a red border.</p>
    <div>
      <p>This text has a red border.</p>
    </div>
    <div class="bar">
      <p>This text has a black border (initial default, not inherited).</p>
    </div>
    

#### CSS

css

    div {
      border: 1px solid green;
    }
    
    p {
      border: 1px solid red;
    }
    
    .bar p {
      border-color: unset;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Cascading and Inheritance Level 4  <br>\# inherit-initial](https://drafts.csswg.org/css-cascade/#inherit-initial) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset#see_also)

---------------------------------------------------------------------------------------------

*   Use the [`initial`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial)
     keyword to set a property to its initial value.
*   Use the [`inherit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit)
     keyword to make an element's property the same as its parent.
*   Use the [`revert`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert)
     keyword to reset a property to the value established by the user-agent stylesheet (or by user styles, if any exist).
*   Use the [`revert-layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer)
     keyword to reset a property to the value established in a previous cascade layer.
*   Use the [`revert-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-rule)
     keyword to reset a property to the value of an earlier matching style rule.
*   The [`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all)
     property lets you reset all properties to their initial, inherited, reverted, or unset state at once.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/unset/index.md?plain=1 "Folder: en-us/web/css/reference/values/unset (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Funset&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Funset%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Funset%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Funset%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0aa8517faf9d7d15c745ac94db7014d3a2d2085f%0A*+Document+last+modified%3A+2026-04-20T12%3A06%3A36.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")