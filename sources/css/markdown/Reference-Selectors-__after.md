*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after#mdn-search)
    

`::after` CSS pseudo-element
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

In CSS, **`::after`** creates a [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 that is the last child of the selected element. It is often used to add cosmetic content to an element with the [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 property. It is inline by default.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after#try_it)

----------------------------------------------------------------------------------------------

    a::after {
      content: " (" attr(href) ")";
    }
    
    .dead-link {
      text-decoration: line-through;
    }
    
    .dead-link::after {
      content: url("/shared-assets/images/examples/warning.svg");
      display: inline-block;
      width: 12px;
      height: 12px;
    }
    

    <p>
      The sailfish is named for its sail-like dorsal fin and is widely considered
      the fastest fish in the ocean.
      <a href="https://en.wikipedia.org/wiki/Sailfish"
        >You can read more about it here</a
      >.
    </p>
    
    <p>
      The red lionfish is a predatory scorpionfish that lives on coral reefs of the
      Indo-Pacific Ocean and more recently in the western Atlantic.
      <a href="" class="dead-link">You can read more about it here</a>.
    </p>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after#syntax)

----------------------------------------------------------------------------------------------

css

    ::after {
      content: /* value */;
      /* properties */
    }
    

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after#description)

--------------------------------------------------------------------------------------------------------

The `::after` pseudo-element is an inline box generated as an immediate child of the element it is associated with, or the "originating element". It is often used to add cosmetic content to an element via the [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 property, such as icons, quote marks, or other decoration.

`::after` pseudo-elements can't be applied to _[replaced elements](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
_ such as [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
, whose contents are determined by external resources and not affected by the current document's styles.

An `::after` pseudo-element with a [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 value of `list-item` behaves like a list item, and can therefore generate a [`::marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)
 pseudo-element just like an [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 element.

If the [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 property is not specified, has an invalid value, or has `normal` or `none` as a value, then the `::after` pseudo-element is not rendered. It behaves as if `display: none` is set.

**Note:** The [Selectors Level 3](https://drafts.csswg.org/selectors-3/#gen-content "External link (opens in new tab)")
 specification introduced the double-colon notation `::after` to distinguish [pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 from [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
. Browsers also accept single-colon notation `:after`, introduced in CSS2.

By default, the `::before` and `::after` pseudo-elements share the same stacking context as their parent. If no [`z-index`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index)
 is explicitly set, the `::after` pseudo-element's generated content will appear above the `::before` pseudo-element's generated content because `::after` is rendered later in the DOM flow.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after#accessibility)

------------------------------------------------------------------------------------------------------------

Using an `::after` pseudo-element to add content is discouraged, as it is not reliably accessible to screen readers.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after#examples)

--------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after#basic_usage)

Let's create two classes: one for boring paragraphs and one for exciting ones. We can use these classes to add pseudo-elements to the end of paragraphs.

#### HTML

html

    <p class="boring-text">Here is some plain old boring text.</p>
    <p>Here is some normal text that is neither boring nor exciting.</p>
    <p class="exciting-text">Contributing to MDN is fun.</p>
    

#### CSS

css

    .exciting-text::after {
      content: " <- EXCITING!";
      color: darkgreen;
      font-weight: bolder;
    }
    
    .boring-text::after {
      content: " <- BORING";
      color: darkviolet;
      font-weight: bolder;
    }
    

#### Result

### [Decorative example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after#decorative_example)

We can style text or images in the [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 property almost any way we want.

#### HTML

html

    <span class="ribbon">Look at the orange box after this text. </span>
    

#### CSS

css

    .ribbon {
      background-color: #5bc8f7;
    }
    
    .ribbon::after {
      content: "This is a fancy orange box.";
      background-color: #ffba10;
      border-color: black;
      border-style: dotted;
    }
    

#### Result

### [Tooltips](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after#tooltips)

This example uses `::after`, in conjunction with the [`attr()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr)
 CSS expression and a `data-description` [custom data attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/data-*)
, to create tooltips. No JavaScript is required!

We can also support keyboard users with this technique, by adding a `tabindex` of `0` to make each `span` keyboard focusable, and using a CSS `:focus` selector. This shows how flexible `::before` and `::after` can be, though for the most accessible experience a semantic disclosure widget created in some other way (such as with [details and summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)
 elements) is likely to be more appropriate.

#### HTML

html

    <p>
      Here we have some
      <span tabindex="0" data-description="collection of words and punctuation">
        text
      </span>
      with a few
      <span tabindex="0" data-description="small popups that appear when hovering">
        tooltips</span
      >.
    </p>
    

#### CSS

css

    span[data-description] {
      position: relative;
      text-decoration: underline;
      color: blue;
      cursor: help;
    }
    
    span[data-description]:hover::after,
    span[data-description]:focus::after {
      content: attr(data-description);
      position: absolute;
      left: 0;
      top: 24px;
      min-width: 200px;
      border: 1px #aaaaaa solid;
      border-radius: 10px;
      background-color: #ffffcc;
      padding: 12px;
      color: black;
      font-size: 14px;
      z-index: 1;
    }
    

#### Result

### [`::after::marker` nested pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after#aftermarker_nested_pseudo-elements)

The `::after::marker` [nested pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements#nesting_pseudo-elements)
 selects the list [`::marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)
 of an `::after` pseudo-element that is itself a list item, that is, it has its [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 property set to `list-item`.

In this demo, we generate extra list items before and after a list navigation menu using `::before` and `::after` (setting them to `display: list-item` so they behave like list items). We then use `ul::before::marker` and `ul::after::marker` to give their list markers a different color.

#### HTML

html

    <ul>
      <li><a href="#">Introduction</a></li>
      <li><a href="#">Getting started</a></li>
      <li><a href="#">Understanding the basics</a></li>
    </ul>
    

#### CSS

css

    ul {
      font-size: 1.5rem;
      font-family: "Helvetica", "Arial", sans-serif;
    }
    
    ul::before,
    ul::after {
      display: list-item;
      color: orange;
    }
    
    ul::before {
      content: "Start";
    }
    
    ul::after {
      content: "End";
    }
    
    ul::before::marker,
    ul::after::marker {
      color: red;
    }
    

#### Result

While the list bullets of the three navigation items are generated because they are `<li>` elements, "Start" and "End" have been inserted via pseudo-elements and `::marker` is used to style their bullets.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Pseudo-Elements Module Level 4  <br>\# selectordef-after](https://www.w3.org/TR/css-pseudo-4/#selectordef-after) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after#see_also)

--------------------------------------------------------------------------------------------------

*   [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)
    
*   [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_after/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_after (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Aafter&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_after%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Aafter%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_after%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6cf697a8965ecdc4967258cc0282fe789b60318e%0A*+Document+last+modified%3A+2026-04-17T06%3A04%3A50.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")