*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:scope#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:scope#mdn-search)
    

`:scope` CSS pseudo-class
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:scope#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:scope`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 represents elements that are a reference point, or scope, for selectors to match against.

css

    /* Selects a scoped element */
    :scope {
      background-color: lime;
    }
    

Which element(s) `:scope` matches depends on the context in which it is used:

*   When used at the root level of a stylesheet, `:scope` is equivalent to [`:root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:root)
    , which in a regular HTML document matches the [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)
     element.
*   When used inside a [`@scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@scope)
     block, `:scope` matches the block's defined scope root. It provides a way to apply styles to the root of the scope from inside the `@scope` block itself.
*   When used within a DOM API call — such as [`querySelector()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelector "querySelector()")
    , [`querySelectorAll()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelectorAll "querySelectorAll()")
    , [`matches()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/matches "matches()")
    , or [`Element.closest()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/closest)
     — `:scope` matches the element on which the method was called.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:scope#syntax)

---------------------------------------------------------------------------------------------

css

    :scope {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:scope#examples)

-------------------------------------------------------------------------------------------------

### [Using `:scope` as an alternative to `:root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:scope#using_scope_as_an_alternative_to_root)

This example shows that `:scope` is equivalent to `:root` when used at the root level of a stylesheet. In this case, the provided CSS colors the background of the `<html>` element orange.

css

    :scope {
      background-color: orange;
    }
    

### [Using `:scope` to style the scope root in a `@scope` block](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:scope#using_scope_to_style_the_scope_root_in_a_scope_block)

In this example, we use two separate `@scope` blocks to match links inside elements with a `.light-scheme` and `.dark-scheme` class respectively. Note how `:scope` is used to select and provide styling to the scope roots themselves. In this example, the scope roots are the [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements that have the classes applied to them.

#### HTML

html

    <div class="light-scheme">
      <p>
        MDN contains lots of information about
        <a href="/en-US/docs/Web/HTML">HTML</a>,
        <a href="/en-US/docs/Web/CSS">CSS</a>, and
        <a href="/en-US/docs/Web/JavaScript">JavaScript</a>.
      </p>
    </div>
    
    <div class="dark-scheme">
      <p>
        MDN contains lots of information about
        <a href="/en-US/docs/Web/HTML">HTML</a>,
        <a href="/en-US/docs/Web/CSS">CSS</a>, and
        <a href="/en-US/docs/Web/JavaScript">JavaScript</a>.
      </p>
    </div>
    

#### CSS

    div {
      padding: 10px;
    }
    

css

    @scope (.light-scheme) {
      :scope {
        background-color: plum;
      }
    
      a {
        color: indigo;
      }
    }
    
    @scope (.dark-scheme) {
      :scope {
        background-color: indigo;
        color: antiquewhite;
      }
    
      a {
        color: plum;
      }
    }
    

#### Result

### [Using `:scope` in JavaScript](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:scope#using_scope_in_javascript)

This example demonstrates using the `:scope` pseudo-class in JavaScript. This can be useful if you need to get a direct descendant of an already retrieved [`Element`](https://developer.mozilla.org/en-US/docs/Web/API/Element)
.

#### HTML

html

    <div id="context">
      <div id="element-1">
        <div id="element-1-1"></div>
        <div id="element-1-2"></div>
      </div>
      <div id="element-2">
        <div id="element-2-1"></div>
      </div>
    </div>
    <p>
      Selected element ids :
      <span id="results"></span>
    </p>
    

#### JavaScript

js

    const context = document.getElementById("context");
    const selected = context.querySelectorAll(":scope > div");
    
    document.getElementById("results").textContent = [...selected]
      .map((element) => `#${element.id}`)
      .join(", ");
    

#### Result

The scope of `context` is the element with the [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 of `context`. The selected elements are the `<div>` elements that are direct children of that context — `element-1` and `element-2` — but not their descendants.

### [Sibling combinators to the right of `:scope` never match](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:scope#sibling_combinators_to_the_right_of_scope_never_match)

The relationship defined by `:scope` is always ancestor-to-descendant from the scope root. Because of that, putting a sibling combinator to the right of `:scope` creates a selector that can never match, because no element can both be within the selector scope and also be a sibling of `:scope`.

css

    :scope + p {
      color: red;
    }
    
    :scope ~ * {
      color: red;
    }
    

Selectors that never match may trigger a warning in browser DevTools.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:scope#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# the-scope-pseudo](https://drafts.csswg.org/selectors/#the-scope-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:scope#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:scope#see_also)

-------------------------------------------------------------------------------------------------

*   The [`@scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@scope)
     [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
    
*   The [`:root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:root)
     [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
    
*   [Selection and traversal on the DOM tree](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Selection_and_traversal_on_the_DOM_tree)
    
*   [`Element.querySelector()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelector)
     and [`Element.querySelectorAll()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelectorAll)
    
*   [`Document.querySelector()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)
     and [`Document.querySelectorAll()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll)
    
*   [`DocumentFragment.querySelector()`](https://developer.mozilla.org/en-US/docs/Web/API/DocumentFragment/querySelector)
     and [`DocumentFragment.querySelectorAll()`](https://developer.mozilla.org/en-US/docs/Web/API/DocumentFragment/querySelectorAll)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:scope/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_scope/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_scope (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Ascope&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_scope%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Ascope%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_scope%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe8310a9d2806a4aebf457f75eec4671e14e47e44%0A*+Document+last+modified%3A+2026-08-11T23%3A47%3A04.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")