*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre#mdn-search)
    

`<pre>` HTML preformatted text element
======================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<pre>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents preformatted text which is to be presented exactly as written in the HTML file. The text is typically rendered using a non-proportional, or [monospaced](https://en.wikipedia.org/wiki/Monospaced_font "External link (opens in new tab)")
 font.

Whitespace inside this element is displayed as written, with one exception. If one or more leading newline characters are included immediately following the opening `<pre>` tag, the _first_ newline character is stripped. This transformation is done by the HTML parser and does not apply when using [XHTML](https://developer.mozilla.org/en-US/docs/Glossary/XHTML)
.

`<pre>` elements' text content is parsed as HTML, so if you want to ensure that your text content stays as plain text, some syntax characters, such as `<`, may need to be escaped using their respective [character references](https://developer.mozilla.org/en-US/docs/Glossary/Character_reference)
. See [escaping ambiguous characters](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre#escaping_ambiguous_characters)
 for more information.

`<pre>` elements commonly contain [`<code>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/code)
, [`<samp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/samp)
, and [`<kbd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd)
 elements, to represent computer code, computer output, and user input, respectively.

By default, `<pre>` is a [block-level](https://developer.mozilla.org/en-US/docs/Glossary/Block-level_content)
 element, i.e., its default [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 value is `block`.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre#try_it)

------------------------------------------------------------------------------------------

    <pre>
                 S
                 A
                LUT
                 M
                O N
                D  E
                DONT
              JE SUIS
              LA  LAN
              G U E  É
             L O Q U E N
            TE      QUESA
           B  O  U  C  H  E
          O        P A R I S
         T I R E   ET   TIRERA
        T O U             JOURS
       AUX                  A  L
     LEM                      ANDS   - Apollinaire
    </pre>
    

    pre {
      font-size: 0.7rem;
      margin: 0;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre#attributes)

--------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`width`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre#width)

Contains the _preferred_ count of characters that a line should have. Though technically still implemented, this attribute has no visual effect; to achieve such an effect, use CSS [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 instead.

[`wrap`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre#wrap)

Is a _hint_ indicating how the overflow must happen. In modern browser this hint is ignored and no visual effect results in its present; to achieve such an effect, use CSS [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
 instead.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre#accessibility)

--------------------------------------------------------------------------------------------------------

It is important to provide an alternate description for any images or diagrams created using preformatted text. The alternate description should clearly and concisely describe the image or diagram's content.

People experiencing low vision conditions and browsing with the aid of assistive technology such as a screen reader may not understand what the preformatted text characters are representing when they are read out in sequence.

A combination of the [`<figure>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure)
 and [`<figcaption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figcaption)
 elements, supplemented by the [ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)
 `role` and [`aria-label`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-label)
 attributes on the `pre` element allow the preformatted [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
 art to be announced as an image with alternative text, and the `figcaption` serving as the image's caption.

### [Example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre#example)

html

    <figure>
      <pre role="img" aria-label="ASCII COW">
          ___________________________
      &lt; I'm an expert in my field. &gt;
          ---------------------------
              \   ^__^
               \  (oo)\_______
                  (__)\       )\/\
                      ||----w |
                      ||     ||
      </pre>
      <figcaption id="cow-caption">
        A cow saying, "I'm an expert in my field." The cow is illustrated using
        preformatted text characters.
      </figcaption>
    </figure>
    

*   [MDN Understanding WCAG, Guideline 1.1 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.1_%E2%80%94_providing_text_alternatives_for_non-text_content)
    
*   [H86: Providing text alternatives for ASCII art, emoticons, and leetspeak | W3C Techniques for WCAG 2.0](https://www.w3.org/TR/WCAG20-TECHS/H86.html "External link (opens in new tab)")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre#examples)

----------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre#basic_example)

#### HTML

html

    <p>Using CSS to change the font color is easy.</p>
    <pre><code>
    body {
      color: red;
    }
    </code></pre>
    

#### Result

### [Escaping ambiguous characters](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre#escaping_ambiguous_characters)

Suppose you want to demonstrate HTML code in a `<pre>` element. The character sequences that define valid HTML tags (starting with `<` and ending with `>`) will not be displayed. To display the tag characters as text, you need to escape (at least) the `<` character using its character reference, so that the sequences no longer define valid tags.

In reality, the HTML parser treats most characters as plain text unless in specific contexts. For example, `< code` is fine, but `<code` would be misparsed; `&am;` is fine, but `&amp;` is not. However, it's a good practice to escape all ambiguous characters to avoid any confusion, especially if you are programmatically generating HTML and injecting the `<pre>` content. In this case, here's a good rule of thumb for how to escape characters:

1.  First, write the content out, as you would like it to appear in the HTML document.
2.  Replace any ampersands (`&`) with `&amp;`. Do this step first, so that new `&` characters generated in the next step don't get escaped.
3.  Replace any `<` characters with `&lt;`.

This should result in the content being displayed as you intended. The replacement of other HTML syntax characters is optional (like `>` to `&gt;`, `"` to `&quot;`, and `'` to `&apos;`), but will do no harm.

#### HTML

html

    <pre><code>
    let i = 5;
    
    if (i &lt; 10 &amp;&amp; i &gt; 0)
      return &quot;Single Digit Number&quot;
    </code></pre>
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre#technical_summary)

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, palpable content. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Implicit ARIA role | `[generic](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/generic_role) ` |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLPreElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLPreElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-pre-element](https://html.spec.whatwg.org/multipage/grouping-content.html#the-pre-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre#see_also)

----------------------------------------------------------------------------------------------

*   CSS: [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
    , [`word-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break)
    
*   [Character reference](https://developer.mozilla.org/en-US/docs/Glossary/Character_reference)
    
*   Related element: [`<code>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/code)
    , [`<samp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/samp)
    , [`<kbd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/pre/index.md?plain=1 "Folder: en-us/web/html/reference/elements/pre (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fpre&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fpre%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fpre%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fpre%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")