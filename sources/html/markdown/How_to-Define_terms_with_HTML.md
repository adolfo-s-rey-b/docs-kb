*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Define_terms_with_HTML#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Define_terms_with_HTML#mdn-search)
    

Define terms with HTML
======================

HTML provides several ways to convey description semantics, whether inline or as structured glossaries. In this article, we'll cover how to properly mark up keywords when you're defining them.

|     |     |
| --- | --- |
| Prerequisites: | You need to be familiar with how to [create a basic HTML document](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website)<br>. |
| Objective: | Learn how to introduce new keywords and how to build description lists. |

When you need a term defined, you probably go straight to a dictionary or glossary. Dictionaries and glossaries _formally_ associate keywords with one or more descriptions, as in this case:

> [Blue (_Adjective_)](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Define_terms_with_HTML#blue_adjective)
> 
> Of a color like the sky in a sunny day. _"The clear blue sky"_

But we're constantly defining keywords informally, as here:

> **Firefox** is the web browser created by the Mozilla Foundation.

To deal with these use cases, [HTML](https://developer.mozilla.org/en-US/docs/Glossary/HTML)
 provides [tags](https://developer.mozilla.org/en-US/docs/Glossary/Tag)
 to mark descriptions and words described, so that your meaning gets across properly to your readers.

[How to mark informal description](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Define_terms_with_HTML#how_to_mark_informal_description)

-----------------------------------------------------------------------------------------------------------------------------------------------------

In textbooks, the first time a keyword occurs, it's common to put the keyword in bold and define it right away.

We do that in HTML too, except HTML is not a visual medium and so we don't use bold. We use [`<dfn>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn)
, which is a special element just for marking the first occurrence of keywords. Note that `<dfn>` tags go around the _word to be defined,_ not the definition (the definition consists of the entire paragraph):

html

    <p><dfn>Firefox</dfn> is the web browser created by the Mozilla Foundation.</p>
    

**Note:** Another use for bold is to emphasize content. Bold itself is a concept foreign to HTML, but there are [tags for indicating emphasis.](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Emphasis_and_importance)

### [Special case: Abbreviations](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Define_terms_with_HTML#special_case_abbreviations)

It's best to [mark abbreviations specially](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Advanced_text_features#abbreviations)
 with [`<abbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr)
, so that screen readers read them appropriately and so that you can operate on all abbreviations uniformly. Just as with any new keyword, you should define your abbreviations the first time they occur.

html

    <p>
      <dfn><abbr>HTML</abbr> (hypertext markup language)</dfn>
      is a description language used to structure documents on the web.
    </p>
    

**Note:** The HTML spec does indeed [set aside the `title` attribute](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-abbr-element "External link (opens in new tab)")
 for expanding the abbreviation. However, this is not an acceptable alternative for providing an inline expansion. The contents of `title` are completely hidden from your users, unless they're using a mouse and they happen to hover over the abbreviation. The spec duly [acknowledges this as well.](https://html.spec.whatwg.org/multipage/dom.html#attr-title "External link (opens in new tab)")

### [Improve accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Define_terms_with_HTML#improve_accessibility)

[`<dfn>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn)
 marks the keyword defined, and indicates that the current paragraph defines the keyword. In other words, there's an implicit relationship between the `<dfn>` element and its container. If you want a more formal relationship, or your definition consists of only one sentence rather than the whole paragraph, you can use the [`aria-describedby`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-describedby)
 attribute to associate a term more formally with its definition:

html

    <p>
      <span id="ff">
        <dfn aria-describedby="ff">Firefox</dfn>
        is the web browser created by the Mozilla Foundation.
      </span>
      You can download it at <a href="https://www.mozilla.org">mozilla.org</a>
    </p>
    

Assistive technology can often use this attribute to find a text alternative to a given term. You can use `aria-describedby` on any tag enclosing a keyword to be defined (not just the `<dfn>` element). `aria-describedby` references the [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 of the element containing the description.

[How to build a description list](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Define_terms_with_HTML#how_to_build_a_description_list)

---------------------------------------------------------------------------------------------------------------------------------------------------

Description lists are just what they claim to be: a list of terms and their matching descriptions (e.g., definition lists, dictionary entries, FAQs, and key-value pairs).

**Note:** Description lists are [not suitable for marking up dialog,](https://html.spec.whatwg.org/multipage/grouping-content.html#the-dl-element "External link (opens in new tab)")
 because conversation does not directly describe the speakers. Here are [recommendations for marking up dialog](https://html.spec.whatwg.org/multipage/semantics-other.html#conversations "External link (opens in new tab)")
.

The terms described go inside [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt)
 elements. The matching description follows immediately, contained within one or more [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dd)
 elements. Enclose the whole description list with a [`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl)
 element.

### [A simple example](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Define_terms_with_HTML#a_simple_example)

Here's an example describing kinds of food and drink:

html

    <dl>
      <dt>jambalaya</dt>
      <dd>
        rice-based entree typically containing chicken, sausage, seafood, and spices
      </dd>
    
      <dt>sukiyaki</dt>
      <dd>
        Japanese specialty consisting of thinly sliced meat, vegetables, and
        noodles, cooked in sake and soy sauce
      </dd>
    
      <dt>chianti</dt>
      <dd>dry Italian red wine originating in Tuscany</dd>
    </dl>
    

**Note:** The basic pattern, as you can see, is to alternate `<dt>` terms with `<dd>` descriptions. If two or more terms occur in a row, the following description applies to all of them. If two or more descriptions occur in a row, they all apply to the last given term.

### [Improving the visual output](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Define_terms_with_HTML#improving_the_visual_output)

Here's how a graphical browser displays the foregoing list:

If you want the keywords to stand out better, you could try bolding them. Remember, HTML is not a visual medium; we need [CSS](https://developer.mozilla.org/en-US/docs/Glossary/CSS)
 for all visual effects. The CSS [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
 property is what you need here:

css

    dt {
      font-weight: bold;
    }
    

This produces the slightly more readable result below:

[Learn more](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Define_terms_with_HTML#learn_more)

---------------------------------------------------------------------------------------------------------

*   [`<dfn>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn)
    
*   [`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl)
    
*   [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt)
    
*   [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dd)
    
*   [How to use the aria-describedby attribute](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-describedby)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 9, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Define_terms_with_HTML/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/how_to/define_terms_with_html/index.md?plain=1 "Folder: en-us/web/html/how_to/define_terms_with_html (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FHow_to%2FDefine_terms_with_HTML&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Fhow_to%2Fdefine_terms_with_html%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FHow_to%2FDefine_terms_with_HTML%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Fhow_to%2Fdefine_terms_with_html%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0754cd805a8e010d2e3a2a065f634a3bcf358252%0A*+Document+last+modified%3A+2025-07-09T21%3A49%3A04.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")