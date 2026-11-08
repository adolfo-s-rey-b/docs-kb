*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::search-text#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::search-text#mdn-search)
    

`::search-text` CSS pseudo-element
==================================

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::search-text#browser_compatibility)
 carefully before using this in production.

The **`::search-text`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 applies styles to search results identified by the user agent's "Find" or "Find in page" text search feature.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::search-text#try_it)

----------------------------------------------------------------------------------------------------

    p::search-text {
      color: crimson;
      background-color: wheat;
    }
    

    <p>
      Using your browser's "Find in page" functionality, find a word or phrase that
      appears in this sentence, and note how, in supporting browsers, each result is
      highlighted using the specified custom styles.
    </p>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::search-text#syntax)

----------------------------------------------------------------------------------------------------

css

    ::search-text {
      /* ... */
    }
    

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::search-text#description)

--------------------------------------------------------------------------------------------------------------

Most browsers include some kind of in-page text search functionality, usually labeled "Find" or "Find in page". The `::search-text` pseudo-element, one of the [highlight pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements#highlight_pseudo-elements)
, allows you to apply a [limited set of styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::search-text#allowable_properties)
 to the text results highlighted by the browser search functionality.

Not all browsers and browser versions highlight search results using in-page highlights that are stylable with CSS. In such cases, `::search-text` may be unimplemented or just ignored.

Using `::search-text` as a selector on its own will style browser search results appearing _anywhere_ on a page. If you want to only style browser search results appearing inside certain elements, you can combine `::search-text` with other selectors, for example `section::search-text`.

Additionally, `::search-text` can be combined with the [`:current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:current)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 to provide specific styles to the currently-focused search result, for example:

css

    p::search-text {
      color: white;
      background-color: purple;
    }
    
    p::search-text:current {
      background-color: crimson;
    }
    

### [Inheritance model](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::search-text#inheritance_model)

The `::search-text` pseudo-element follows a special inheritance model common to all highlight pseudo-elements, wherein styles are inherited from both their parent elements and the pseudo-elements of their parents. For more details on how this inheritance works, see the [Highlight pseudo-elements inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements#highlight_pseudo-elements_inheritance)
 section.

### [Allowable properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::search-text#allowable_properties)

A limited subset of CSS properties can be used with `::search-text`:

*   [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
    
*   [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    
*   The [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
     shorthand and associated longhand properties:
    *   [`text-decoration-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line)
        : the `grammar-error`, `spelling-error`, `line-through`, `none`, and `underline` values only.
    *   [`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)
        
    *   [`text-decoration-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-style)
        
    *   [`text-decoration-thickness`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness)
        
    *   [`text-decoration-skip-ink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip-ink)
        
*   [`text-underline-offset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset)
    
*   [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
    

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::search-text#accessibility)

------------------------------------------------------------------------------------------------------------------

**Override text search result styles sparingly**, especially when doing so for purely aesthetic reasons. For people experiencing cognitive concerns or who are less technologically literate, unexpected changes to these styles may hurt their understanding of the functionality.

A primary use case of `::search-text` is to increase color contrast compared to the default browser styling. When customizing highlighted text, it is important to ensure that the [contrast ratio between the foreground and background colors](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
 is great enough for people to be able to perceive the content of the highlighted text.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::search-text#examples)

--------------------------------------------------------------------------------------------------------

### [Custom styles for text search results](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::search-text#custom_styles_for_text_search_results)

This example shows how to use `::search-text` and `:current` to create custom styles for your browser's "Find in page" search results.

#### HTML

The HTML consists of a basic paragraph of text. We won't show the HTML source, both for brevity, and so that it is easier to navigate the search results in the rendered example.

    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec finibus est
      eget eros congue pellentesque. Etiam a augue accumsan, scelerisque nisl sit
      amet, lobortis nulla. Aliquam condimentum eu orci eu elementum. Donec
      porttitor quam et posuere commodo. Mauris rhoncus diam a scelerisque molestie.
      Integer sollicitudin risus dui, ut sagittis lorem laoreet eget. Duis eget
      pretium enim. Morbi tristique, diam sit amet gravida finibus, metus ex
      tincidunt nibh, ac volutpat urna purus et arcu. Donec risus risus, semper vel
      purus sit amet, gravida vestibulum est. Sed et tristique urna. Nam vel mi eget
      nisi consectetur elementum. Aenean faucibus aliquam cursus. Morbi posuere
      tincidunt velit, et sagittis quam sagittis in. Nam eget ante ultrices, auctor
      dui vel, euismod lacus. Vivamus tincidunt, sem ac sodales aliquet, tortor
      tortor consequat diam, nec tempor mi dui vel eros. Aliquam ac erat et metus
      egestas scelerisque.
    </p>
    

#### CSS

In our CSS, we start by styling the `::search-text` pseudo-element. We give it custom [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
, [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
, and [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
 styles.

    html {
      font-family: "Helvetica", "Arial";
    }
    
    p {
      font-size: 1.5rem;
      line-height: 1.5;
      width: 90%;
      margin: 0 auto;
    }
    @layer no-support {
      body::before {
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1em 0;
      }
      @supports not selector(:current) {
        body::before {
          content: "Your browser doesn't support the :current pseudo-class.";
        }
      }
      @supports not selector(::search-text) {
        body::before {
          content: "Your browser doesn't support the ::search-text pseudo-element.";
        }
      }
    }
    

css

    ::search-text {
      background-color: purple;
      color: white;
      text-shadow: 1px 1px 1px black;
    }
    

Finally, we style the currently-focused search result via `::search-text:current`, providing it with a different `background-color` and some [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
 styles so that it is distinguishable from the rest of the results.

css

    ::search-text:current {
      background-color: crimson;
      text-decoration-line: underline;
      text-decoration-color: yellow;
      text-decoration-thickness: 3px;
    }
    

#### Result

The example renders as follows:

Try using the browser's find in page interface to find a word that appears multiple times in the example text, such as "aliquam", "amet", or "tortor". Move between the previous and next results to check out the `:current` styling.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::search-text#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Pseudo-Elements Module Level 4  <br>\# selectordef-search-text](https://drafts.csswg.org/css-pseudo-4/#selectordef-search-text) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::search-text#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::search-text#see_also)

--------------------------------------------------------------------------------------------------------

*   [`:current`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:current)
    
*   [Highlight pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements#highlight_pseudo-elements)
    
*   [CSS pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Pseudo-elements)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::search-text/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_search-text/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_search-text (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Asearch-text&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_search-text%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Asearch-text%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_search-text%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb3cd597b58940518a7712487ce94efc0881cb549%0A*+Document+last+modified%3A+2026-08-27T07%3A38%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")