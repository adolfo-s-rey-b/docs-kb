*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Cheatsheet#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Cheatsheet#mdn-search)
    

HTML cheatsheet for syntax and common tasks
===========================================

While using [HTML](https://developer.mozilla.org/en-US/docs/Glossary/HTML)
 it can be very handy to have an easy way to remember how to use HTML tags properly and how to apply them. MDN provides you with extended [HTML reference documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements)
 as well as a deep instructional [set of HTML guides](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content)
. However, in many cases we just need some quick hints as we go. That's the whole purpose of the cheat sheet, to give you some quick accurate ready to use code snippets for common usages.

**Note:** HTML tags must be used for their semantic value, not their appearance. It's always possible to totally change the look and feel of a given tag using [CSS](https://developer.mozilla.org/en-US/docs/Glossary/CSS)
 so, when using HTML, take the time to focus on the meaning rather than the appearance.

[Inline elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Cheatsheet#inline_elements)

-------------------------------------------------------------------------------------------------------

An "element" is a single part of a webpage. Some elements are large and hold smaller elements like containers. Some elements are small and are "nested" inside larger ones. By default, "inline elements" appear next to one another in a webpage. They take up only as much width as they need in a page and fit together horizontally like words in a sentence or books shelved side-by-side in a row. All inline elements can be placed within the `<body>` element.

|     |     |     |
| --- | --- | --- |Inline elements: usage and examples
| Usage | Element | Example |
| --- | --- | --- |
| A link | [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a) |     |
| An image | [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img) | html<br><br>    <img src="beast.png" width="50" /> |
| An inline container | [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span) | html<br><br>    Used to group elements: for example,<br>    to <span style="color:blue">style<br>    them</span>. |
| Emphasize text | [`<em>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/em) | html<br><br>    <em>I'm posh</em>. |
| Italic text | [`<i>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i) | html<br><br>    Mark a phrase in <i>italics</i>. |
| Bold text | [`<b>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b) | html<br><br>    Bold <b>a word or phrase</b>. |
| Important text | [`<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong) | html<br><br>    <strong>I'm important!</strong> |
| Highlight text | [`<mark>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/mark) | html<br><br>    <mark>Notice me!</mark> |
| Strikethrough text | [`<s>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/s) | html<br><br>    <s>I'm irrelevant.</s> |
| Subscript | [`<sub>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub) | html<br><br>    H<sub>2</sub>O |
| Small text | [`<small>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/small) | html<br><br>    Used to represent the <small>small<br>    print </small>of a document. |
| Address | [`<address>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address) | html<br><br>    <address>Main street 67</address> |
| Textual citation | [`<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite) | html<br><br>    For more monsters,<br>    see <cite>The Monster Book of Monsters</cite>. |
| Superscript | [`<sup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup) | html<br><br>    x<sup>2</sup> |
| Inline quotation | [`<q>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/q) | html<br><br>    <q>Me?</q>, she said. |
| A line break | [`<br>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br) | html<br><br>    Line 1<br />Line 2 |
| A possible line break | [`<wbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr) | html<br><br>    <div style="width: 200px"><br>      Llanfair<wbr />pwllgwyngyll<wbr />gogerychwyrndrobwllllantysiliogogogoch.<br>    </div> |
| Date | [`<time>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time) | html<br><br>    Used to format the date. For example:<br>    <time datetime="2020-05-24"><br>    published on 23-05-2020</time>. |
| Code format | [`<code>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/code) | html<br><br>    This text is in normal format,<br>    but <code>this text is in code<br>    format</code>. |
| Audio | [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio) | html<br><br>    <audio controls><br>      <source src="/shared-assets/audio/t-rex-roar.mp3" type="audio/mpeg" /><br>    </audio> |
| Video | [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video) | html<br><br>    <video controls width="250"<br>      src="/shared-assets/videos/flower.webm" ><br>      <a href="/shared-assets/videos/flower.webm">Download WebM video</a><br>    </video> |

[Block elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Cheatsheet#block_elements)

-----------------------------------------------------------------------------------------------------

"Block elements," on the other hand, take up the entire width of a webpage. They also take up a full line of a webpage; they do not fit together side-by-side. Instead, they stack like paragraphs in an essay or toy blocks in a tower.

**Note:** Because this cheat sheet is limited to a few elements representing specific structures or having special semantics, the [`div`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element is intentionally not included — because the `div` element doesn't represent anything and doesn't have any special semantics.

| Usage | Element | Example |
| --- | --- | --- |
| A simple paragraph | [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p) | html<br><br>    <p>I'm a paragraph</p><br>    <p>I'm another paragraph</p> |
| An extended quotation | [`<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote) | html<br><br>    They said:<br>    <blockquote>The blockquote element indicates<br>    an extended quotation.</blockquote> |
| Additional information | [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details) | html<br><br>    <details><br>      <summary>HTML Cheat Sheet</summary><br>      <p>Inline elements</p><br>      <p>Block elements</p><br>    </details> |
| An unordered list | [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul) | html<br><br>    <ul><br>      <li>I'm an item</li><br>      <li>I'm another item</li><br>    </ul> |
| An ordered list | [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol) | html<br><br>    <ol><br>      <li>I'm the first item</li><br>      <li>I'm the second item</li><br>    </ol> |
| A definition list | [`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl) | html<br><br>    <dl><br>      <dt>A Term</dt><br>      <dd>Definition of a term</dd><br>      <dt>Another Term</dt><br>      <dd>Definition of another term</dd><br>    </dl> |
| A horizontal rule | [`<hr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr) | html<br><br>    before<hr />after |
| Text Heading | [<h1>-<h6>](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements) | html<br><br>    <h1> This is Heading 1 </h1><br>    <h2> This is Heading 2 </h2><br>    <h3> This is Heading 3 </h3><br>    <h4> This is Heading 4 </h4><br>    <h5> This is Heading 5 </h5><br>    <h6> This is Heading 6 </h6> |

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 3, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Cheatsheet/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/guides/cheatsheet/index.md?plain=1 "Folder: en-us/web/html/guides/cheatsheet (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FGuides%2FCheatsheet&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Fguides%2Fcheatsheet%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FGuides%2FCheatsheet%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Fguides%2Fcheatsheet%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Faff319cd81d10cfda31b13adb3263deafb284b20%0A*+Document+last+modified%3A+2025-11-03T18%3A07%3A59.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")