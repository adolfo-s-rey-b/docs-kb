*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert#mdn-search)
    

`revert` CSS keyword
====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`revert`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 keyword reverts the cascaded value of the property from its current value to the value the property would have had if no changes had been made by the current **[style origin](https://developer.mozilla.org/en-US/docs/Glossary/Style_origin)
** to the current element. Thus, it resets the property either to user agent set value, to user set value, to its inherited value (if it is inheritable), or to initial value. It can be applied to any CSS property, including the CSS shorthand property [`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all)
.

This keyword removes from the cascade all of the styles that have been overridden until the style being rolled back to is reached.

*   If used by a site's own styles (the author origin), `revert` rolls back the property's cascaded value to the user's custom style, if one exists; otherwise, it rolls the style back to the user agent's default style.
*   If used in a user's custom stylesheet, or if the style was applied by the user (the user origin), `revert` rolls back the cascaded value to the user agent's default style.
*   If used within the user agent's default styles, this keyword is functionally equivalent to [`unset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset)
    .

The `revert` keyword works exactly the same as [`unset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset)
 in many cases. The only difference is for properties that have values set by the browser or by custom stylesheets created by users (set on the browser side).

Revert will not affect rules applied to children of an element you reset (but will remove effects of a parent rule on a child). So if you have a `color: green` for all sections and `all: revert` on a specific section, the color of the section will be black. But if you have a rule to make all paragraphs red, then all paragraphs will still be red in all sections.

**Note:** Revert is just a value. It is still possible to override the `revert` value using [specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
.

**Note:** The `revert` keyword is different from and should not be confused with the [`initial`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial)
 keyword, which uses the [initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
 defined on a per-property basis by the CSS specifications. In contrast, user-agent stylesheets set default values on the basis of CSS selectors.

For example, the [initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
 for the [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display#formal_definition)
 property is `inline`, whereas a normal user-agent stylesheet sets the default [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 value of [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
s to `block`, of [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)
s to `table`, etc.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert#examples)

----------------------------------------------------------------------------------------------

### [Revert vs. unset](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert#revert_vs._unset)

Although `revert` and `unset` are similar, they differ for some properties for some elements.

So in the below example, we set custom [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight#formal_definition)
, but then try to `revert` and `unset` it inline in the HTML document. The `revert` keyword will revert the text to bold because that is the default value for headers in most browsers. The `unset` keyword will keep the text normal because, as an inherited property, the `font-weight` would then inherit its value from the body.

#### HTML

html

    <h3 style="font-weight: revert; color: revert;">
      This should have its original font-weight (bold) and color: black
    </h3>
    <p>Just some text</p>
    <h3 style="font-weight: unset; color: unset;">
      This will still have font-weight: normal, but color: black
    </h3>
    <p>Just some text</p>
    

#### CSS

css

    h3 {
      font-weight: normal;
      color: blue;
    }
    

#### Result

### [Revert all](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert#revert_all)

Reverting all values is useful in a situation where you've made several style changes and then you want to revert to the browser default values. So in the above example, instead of reverting `font-weight` and `color` separately, you could just revert all of them at once - by applying the `revert` keyword on `all`.

#### HTML

html

    <h3>This will have custom styles</h3>
    <p>Just some text</p>
    <h3 style="all: revert">This should be reverted to browser/user defaults.</h3>
    <p>Just some text</p>
    

#### CSS

css

    h3 {
      font-weight: normal;
      color: blue;
      border-bottom: 1px solid grey;
    }
    

#### Result

### [Revert on a parent](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert#revert_on_a_parent)

Reverting effectively removes the value for the element you select with some rule and this happens only for that element. To illustrate this, we will set a green color on a section and red color on a paragraph.

#### HTML

html

    <main>
      <section>
        <h3>This h3 will be dark green</h3>
        <p>Text in paragraph will be red.</p>
        This stray text will also be dark green.
      </section>
      <section class="with-revert">
        <h3>This h3 will be steelblue</h3>
        <p>Text in paragraph will be red.</p>
        This stray text will also be steelblue.
      </section>
    </main>
    

#### CSS

    main {
      border: 3px solid steelblue;
    }
    
    section {
      margin: 0.5rem;
      border: 2px dashed darkgreen;
    }
    

css

    main {
      color: steelblue;
    }
    section {
      color: darkgreen;
    }
    p {
      color: red;
    }
    section.with-revert {
      color: revert;
    }
    

#### Result

Notice how the paragraph is still red even though a `color` property for the section was reverted. Also, note that both the header and plain text node are `steelblue`. The result of reverting makes it as if `section { color: darkgreen; }` did not exist for the section with `color: revert` applied.

Also, if neither the user agent nor the user override the `<h3>` or `<section>` color values, then the `steelblue` color is inherited from `<main>`, as the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 property is an inherited property.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Cascading and Inheritance Level 4  <br>\# default](https://drafts.csswg.org/css-cascade/#default) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert#see_also)

----------------------------------------------------------------------------------------------

*   Use the [`initial`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial)
     keyword to set a property to its initial value.
*   Use the [`inherit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit)
     keyword to make an element's property the same as its parent.
*   Use the [`revert-layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer)
     keyword to reset a property to the value established in a previous cascade layer.
*   Use the [`revert-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-rule)
     keyword to reset a property to the value of an earlier matching style rule.
*   Use the [`unset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset)
     keyword to set a property to its inherited value if it inherits or to its initial value if not.
*   The [`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all)
     property lets you reset all properties to their initial, inherited, reverted, or unset state at once.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/revert/index.md?plain=1 "Folder: en-us/web/css/reference/values/revert (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Frevert&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Frevert%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Frevert%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Frevert%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0aa8517faf9d7d15c745ac94db7014d3a2d2085f%0A*+Document+last+modified%3A+2026-04-20T12%3A06%3A36.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")