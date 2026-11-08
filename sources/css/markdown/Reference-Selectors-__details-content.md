*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::details-content#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::details-content#mdn-search)
    

`::details-content` CSS pseudo-element
======================================

Baseline 2025

Newly available

Since September 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::details-content#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`::details-content`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 represents the expandable/collapsible contents of a [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)
 element.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::details-content#try_it)

--------------------------------------------------------------------------------------------------------

    details[open]::details-content {
      color: dodgerblue;
      padding: 0.5em;
      border: thin solid grey;
    }
    

    <details open>
      <summary>Example summary</summary>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
      <p>
        Architecto cupiditate ea optio modi quas sequi, esse libero asperiores
        debitis eveniet commodi hic ad.
      </p>
    </details>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::details-content#syntax)

--------------------------------------------------------------------------------------------------------

css

    selector::details-content
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::details-content#examples)

------------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::details-content#basic_example)

This example demonstrates basic usage of the `::details-content` pseudo-element to style the content of a [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)
 element.

#### HTML

Our `<details>` element includes a [`<summary>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary)
 element, whose contents will always be visible. The details content includes a [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 element.

html

    <details>
      <summary>Click me</summary>
      <p>Here is some content</p>
    </details>
    

#### CSS

We set a [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 on the `::details-content` pseudo-element:

css

    details::details-content {
      background-color: #a29bfe;
    }
    

#### Result

Click on the summary to view the detail contents.

### [Transition example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::details-content#transition_example)

In this example the `::details-content` pseudo-element is used to set a transition on the content of the [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)
 element so that it smoothly fades into view when expanded, and fades out again when collapsed.

#### HTML

The HTML is the same as in the previous example.

html

    <details>
      <summary>Click me</summary>
      <p>Here is some content</p>
    </details>
    

#### CSS

To achieve our transition, we specify two separate transitions inside the [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
 shorthand property:

*   The [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
     property is given a basic transition over `600ms` to create the fade-in/fade-out effect.
*   The [`content-visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility)
     property (which is toggled between `hidden` and `visible` when the `<details>` content is expanded/collapsed) is given a `600ms` transition with the [`transition-behavior`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior)
     value `allow-discrete` specified. This opts the browser into having a transition started on `content-visibility`, the animation behavior of which is [discrete](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties#discrete)
    . The effect is that the content is visible for the entire duration of the transition, allowing other transitions to be seen. If this transition was not included, the content would immediately disappear when the `<details>` content was collapsed — you wouldn't see the smooth fade-out.

css

    details::details-content {
      opacity: 0;
      transition:
        opacity 600ms,
        content-visibility 600ms allow-discrete;
    }
    
    details[open]::details-content {
      opacity: 1;
    }
    

#### Result

To see the animation, toggle the visibility of the detail contents by clicking on the summary.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::details-content#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Pseudo-Elements Module Level 4  <br>\# details-content-pseudo](https://drafts.csswg.org/css-pseudo-4/#details-content-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::details-content#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::details-content#see_also)

------------------------------------------------------------------------------------------------------------

*   [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)
    
*   [`<summary>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::details-content/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_details-content/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_details-content (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Adetails-content&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_details-content%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Adetails-content%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_details-content%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6cf697a8965ecdc4967258cc0282fe789b60318e%0A*+Document+last+modified%3A+2026-04-17T06%3A04%3A50.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")