*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/u#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/u#mdn-search)
    

`<u>` HTML unarticulated annotation (underline) element
=======================================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/u#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<u>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents a span of inline text which should be rendered in a way that indicates that it has a non-textual annotation. This is rendered by default as a single solid underline, but may be altered using CSS.

**Warning:** This element used to be called the "Underline" element in older versions of HTML, and is still sometimes misused in this way. To underline text, you should instead apply a style that includes the CSS [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
 property set to `underline`.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/u#try_it)

----------------------------------------------------------------------------------------

    <p>
      You could use this element to highlight <u>speling</u> mistakes, so the writer
      can <u>corect</u> them.
    </p>
    

    p {
      margin: 0;
    }
    
    u {
      text-decoration: red wavy underline;
    }
    

See the [Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/u#usage_notes)
 section for further details on when it's appropriate to use `<u>` and when it isn't.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/u#attributes)

------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/u#usage_notes)

--------------------------------------------------------------------------------------------------

Along with other pure styling elements, the original HTML Underline (`<u>`) element was deprecated in HTML 4; however, `<u>` was restored in HTML 5 with a new, semantic, meaning: to mark text as having some form of non-textual annotation applied.

**Note:** Avoid using the `<u>` element with its default styling (of underlined text) in such a way as to be confused with a hyperlink, which is also underlined by default.

### [Use cases](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/u#use_cases)

Valid use cases for the `<u>` element include annotating spelling errors, applying a [proper name mark](https://en.wikipedia.org/wiki/Proper_name_mark "External link (opens in new tab)")
 to denote proper names in Chinese text, and other forms of annotation.

You should _not_ use `<u>` to underline text for presentation purposes, or to denote titles of books.

### [Other elements to consider using](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/u#other_elements_to_consider_using)

In most cases, you should use an element other than `<u>`, such as:

*   [`<em>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/em)
     to denote stress emphasis
*   [`<b>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b)
     to draw attention to text
*   [`<mark>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/mark)
     to mark key words or phrases
*   [`<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong)
     to indicate that text has strong importance
*   [`<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite)
     to mark the titles of books or other publications
*   [`<i>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i)
     to denote technical terms, transliterations, thoughts, or names of vessels in Western texts

To provide textual annotations (as opposed to the non-textual annotations created with `<u>`), use the [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)
 element.

To apply an underlined appearance without any semantic meaning, use the [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
 property's value `underline`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/u#examples)

--------------------------------------------------------------------------------------------

### [Indicating a spelling error](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/u#indicating_a_spelling_error)

This example uses the `<u>` element and some CSS to display a paragraph which includes a misspelled error, with the error indicated in the red wavy underline style which is fairly commonly used for this purpose.

#### HTML

html

    <p>This paragraph includes a <u class="spelling">wrnogly</u> spelled word.</p>
    

In the HTML, we see the use of `<u>` with a class, `spelling`, which is used to indicate the misspelling of the word "wrongly".

#### CSS

css

    u.spelling {
      text-decoration: red wavy underline;
    }
    

This CSS indicates that when the `<u>` element is styled with the class `spelling`, it should have a red wavy underline underneath its text. This is a common styling for spelling errors. Another common style can be presented using `red dashed underline`.

#### Result

The result should be familiar to anyone who has used any of the more popular word processors available today.

### [Avoiding <u>](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/u#avoiding_u)

Most of the time, you actually don't want to use `<u>`. Here are some examples that show what you should do instead in several cases.

#### Non-semantic underlines

To underline text without implying any semantic meaning, use a [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
 element with the [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
 property set to `"underline"`, as shown below.

##### HTML

html

    <span class="underline">Today's Special</span>
    <br />
    Chicken Noodle Soup With Carrots
    

##### CSS

css

    .underline {
      text-decoration: underline;
    }
    

##### Result

#### Presenting a book title

Book titles should be presented using the [`<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite)
 element instead of `<u>` or even `<i>`.

##### Using the cite element

html

    <p>The class read <cite>Moby-Dick</cite> in the first term.</p>
    

##### Styling the cite element

The default styling for the `<cite>` element renders the text in italics. You can override that using CSS:

html

    <p>The class read <cite>Moby-Dick</cite> in the first term.</p>
    

css

    cite {
      font-style: normal;
      text-decoration: underline;
    }
    

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/u#technical_summary)

--------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, palpable content. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | `[generic](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/generic_role) ` |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/u#specifications)

--------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-u-element](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-u-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/u#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/u#see_also)

--------------------------------------------------------------------------------------------

*   The [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
    , [`<i>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i)
    , [`<em>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/em)
    , [`<b>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b)
    , and [`<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite)
     elements should usually be used instead.
*   The CSS [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
     property should be used for non-semantic underlining.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/u/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/u/index.md?plain=1 "Folder: en-us/web/html/reference/elements/u (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fu&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fu%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fu%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fu%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")