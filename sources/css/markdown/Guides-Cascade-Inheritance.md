*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance#mdn-search)
    

Inheritance
===========

In CSS, **inheritance** controls what happens when no value is specified for a property on an element.

CSS properties can be categorized in two types:

*   **inherited properties**, which by default are set to the [computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
     of the parent element
*   **non-inherited properties**, which by default are set to [initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
     of the property

Refer to [any CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#index)
 definition to see whether a specific property inherits by default ("Inherited: yes") or not ("Inherited: no").

[Inherited properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance#inherited_properties)

-------------------------------------------------------------------------------------------------------------------------

When no value for an **inherited property** has been specified on an element, the element gets the [computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
 of that property on its parent element. Only the root element of the document gets the [initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
 given in the property's summary.

A typical example of an inherited property is the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 property. Consider the following style rules and the markup:

css

    p {
      color: green;
    }
    

html

    <p>This paragraph has <em>emphasized text</em> in it.</p>
    

The words "emphasized text" will appear green, since the `em` element has inherited the value of the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 property from the `p` element. It does _not_ get the initial value of the property (which is the color that is used for the root element when the page specifies no color).

[Non-inherited properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance#non-inherited_properties)

---------------------------------------------------------------------------------------------------------------------------------

When no value for a **non-inherited property** has been specified on an element, the element gets the [initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
 of that property (as specified in the property's summary).

A typical example of a non-inherited property is the [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
 property. Consider the following style rules and the markup:

css

    p {
      border: medium solid;
    }
    

html

    <p>This paragraph has <em>emphasized text</em> in it.</p>
    

The words "emphasized text" will not have another border (since the initial value of [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
 is `none`).

[Notes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance#notes)

-------------------------------------------------------------------------------------------

The [`inherit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit)
 keyword allows authors to explicitly specify inheritance. It works on both inherited and non-inherited properties.

You can control inheritance for all properties at once using the [`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all)
 shorthand property, which applies its value to all properties. For example:

css

    p {
      all: revert;
      font-size: 200%;
      font-weight: bold;
    }
    

This reverts the style of the paragraphs' [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
 property to the user agent's default unless a user stylesheet exists, in which case that is used instead. Then it doubles the font size and applies a [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
 of `"bold"`.

### [Overriding inheritance, an example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance#overriding_inheritance_an_example)

Using our previous example with [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
, if we explicitly set the inheritance with `inherit`, we get the following:

css

    p {
      border: medium solid;
    }
    
    em {
      border: inherit;
    }
    

html

    <p>This paragraph has <em>emphasized text</em> in it.</p>
    

We can see here another border around the word "emphasized text".

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Cascading and Inheritance Level 5  <br>\# css-inheritance](https://drafts.csswg.org/css-cascade-5/#css-inheritance) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance#see_also)

-------------------------------------------------------------------------------------------------

*   CSS values for controlling inheritance: [`inherit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit)
    , [`initial`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial)
    , [`revert`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert)
    , [`revert-layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer)
    , and [`unset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset)
    
*   [CSS cascading and inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade)
     module
*   [CSS error handling](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Error_handling)
    
*   [Introduction to the CSS cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction)
    
*   [Learn: Handling conflicts](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Handling_conflicts)
    
*   [Learn: Cascade layers](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Cascade_layers)
    
*   [Introduction to CSS syntax: declarations, rulesets, and statements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction)
    
*   [At-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
    
*   Values: [initial](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
    , [computed](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
    , [used](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#used_value)
    , and [actual](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#actual_value)
    
*   [Value definition syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax)
    
*   [CSS nesting](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 16, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/cascade/inheritance/index.md?plain=1 "Folder: en-us/web/css/guides/cascade/inheritance (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FCascade%2FInheritance&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fcascade%2Finheritance%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FCascade%2FInheritance%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fcascade%2Finheritance%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F33094d735e90b4dcae5733331b79c51fee997410%0A*+Document+last+modified%3A+2025-12-16T15%3A14%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")