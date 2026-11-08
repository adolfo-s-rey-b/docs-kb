*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit#mdn-search)
    

`inherit` CSS keyword
=====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`inherit`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 keyword causes the element to take the [computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
 of the property from its parent element. It can be applied to any CSS property, including the CSS shorthand property [`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all)
.

For [inherited properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance#inherited_properties)
, this reinforces the default behavior, and is only needed to override another rule.

**Note:** Inheritance is always from the parent element in the document tree, even when the parent element is not the containing block.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit#examples)

-----------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit#basic_usage)

In this example, we demonstrate the effect of the `inherit` keyword by comparing two paragraphs with nested elements: the inline elements in one use their browser default styles, while those in the other inherit individual property values from their parent.

#### HTML

We include two identical paragraphs with several inline elements.

html

    <p>
      This paragraph has <em>emphasized text</em>, <strong>strong text</strong>, and
      <a href="#">a link to top</a>.
    </p>
    <p>
      This paragraph has <em>emphasized text</em>, <strong>strong text</strong>, and
      <a href="#">a link to top</a>.
    </p>
    

#### CSS

We don't style the inline elements in the first paragraph, so they use their default browser styles. In the second paragraph, we set properties on each inline element to `inherit`, so they get the computed styles from the parent [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 element.

css

    p:nth-of-type(2) {
      a {
        text-decoration: inherit;
        color: inherit;
      }
      em {
        font-style: inherit;
      }
      strong {
        font-weight: inherit;
      }
    }
    

#### Result

### [Inheriting all property values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit#inheriting_all_property_values)

In this example, we use the same HTML as in the previous example to demonstrate the issues that can occur when the `inherit` keyword is applied to all properties.

    <p>
      This paragraph has <em>emphasized text</em>, <strong>strong text</strong>, and
      <a href="#">a link to top</a>.
    </p>
    <p>
      This paragraph has <em>emphasized text</em>, <strong>strong text</strong>, and
      <a href="#">a link to top</a>.
    </p>
    

#### CSS

In the second paragraph, instead of setting individual properties to `inherit`, we set the [`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all)
 property on all inline elements to `inherit`, so they all get computed styles from their parent [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
.

css

    p:nth-of-type(2) > * {
      all: inherit;
    }
    

#### Result

Notice how the inline element inherit all the properties of the parent `<p>`, including the paragraph's block-level [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 value. This is likely not the effect you would want.

### [Excluding selected elements from a rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit#excluding_selected_elements_from_a_rule)

This example demonstrates how the `inherit` keyword can be used to exclude selected elements from a color rule, allowing them to use their parent's color instead.

#### HTML

We include some semantically structured content.

html

    <header>
      <h1>This is my blog</h1>
      <h2>This is the subtitle of my blog in the HEADER</h2>
      <p>My blog is not very interesting</p>
    </header>
    <main>
      <h2>This first blog post in MAIN</h2>
      <p>I really have nothing to say.</p>
      <section>
        <h2>This second blog post is in a SECTION within MAIN</h2>
        <p>
          It is in a section because it is important even though it isn't the least
          bit interesting.
        </p>
      </section>
    </main>
    <footer>
      <h2>Contact in FOOTER</h2>
      <p>Find me on Mastodon</p>
      <section>
        <h2>Copyright in SECTION within FOOTER</h2>
        <p>1996</p>
      </section>
    </footer>
    

#### CSS

We set the text color of the `<main>` element to `blue` and all `<h2>` elements to `green` in `monospace` font. The `<h2>` elements inside a `<section>` are set to `inherit` their parent's text color.

css

    main {
      color: blue;
    }
    
    h2 {
      color: green;
      font-family: monospace;
    }
    
    section h2 {
      color: inherit;
    }
    

#### Result

The `<h2>` elements are all `green`. However, if they are nested in a [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 element, they inherit their color from their parent, which is `blue` within [`<main>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main)
. The default text color is black otherwise.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Cascading and Inheritance Level 4  <br>\# inherit](https://drafts.csswg.org/css-cascade/#inherit) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit#see_also)

-----------------------------------------------------------------------------------------------

*   [`initial`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial)
    , [`revert`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert)
    , [`revert-layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer)
    , [`revert-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-rule)
    , and [`unset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset)
     keywords
*   [Inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/inherit/index.md?plain=1 "Folder: en-us/web/css/reference/values/inherit (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Finherit&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Finherit%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Finherit%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Finherit%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0aa8517faf9d7d15c745ac94db7014d3a2d2085f%0A*+Document+last+modified%3A+2026-04-20T12%3A06%3A36.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")