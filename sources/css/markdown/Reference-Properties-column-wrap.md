*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap#mdn-search)
    

`column-wrap` CSS property
==========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/960)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap#browser_compatibility)
 carefully before using this in production.

The **`column-wrap`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the wrapping behavior of overflow columns in a [CSS multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap#syntax)

---------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    column-wrap: auto;
    column-wrap: nowrap;
    column-wrap: wrap;
    
    /* Global values */
    column-wrap: inherit;
    column-wrap: initial;
    column-wrap: revert;
    column-wrap: revert-layer;
    column-wrap: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap#auto)

The initial value. If the content container's [`column-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height)
 is set to a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
, `auto` resolves to `wrap`, otherwise it resolves to `nowrap`.

[`nowrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap#nowrap)

Columns overflow in the inline direction.

[`wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap#wrap)

Overflow columns are placed in a new row in the block direction.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap#description)

-------------------------------------------------------------------------------------------------------------

The `column-wrap` property can be used to set the columns of a [CSS multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
 to wrap onto a new row when they start to overflow the column width. This is useful for creating more readable layouts when using the [`column-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)
 or [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
 property to set multiple columns.

Without `column-wrap`, excess columns will overflow to the side, and readers will have to scroll in the inline direction to read all the content. The [`column-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height)
 property, along with `column-wrap`, allows you to set a specific height for the columns and wrap them onto a new row of columns when the container edge is reached.

The default value of `column-wrap` is `auto`, which resolves to `wrap` when `column-height` is set to a `<length>` value; `wrap` allows the fixed-height columns to wrap onto multiple rows. When `column-height` is equal to `auto`, `column-wrap: auto` resolves to `nowrap`, allowing the columns to overflow horizontally if a fixed container height is set.

As a result of this default behavior, generally you don't need to explicitly set the `column-wrap` property.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | multicol elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

column-wrap =   
  auto    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  nowrap  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  wrap      

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap#examples)

-------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap#basic_usage)

This example demonstrates basic usage of the `column-wrap` property to create a wrapped multi-col layout via setting a `column-height` property.

#### HTML

We include a poem by Dr. Seuss using an [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)
 containing 28 [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
s, followed by the author's name in a [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
.

html

    <ol>
      <li>One fish</li>
      <li>Two fish</li>
      <li>Red fish</li>
      <li>Blue fish</li>
      ...
    </ol>
    <p>-- Dr. Seuss</p>
    

    <ol>
      <li>One fish</li>
      <li>Two fish</li>
      <li>Red fish</li>
      <li>Blue fish</li>
      <li>Black fish</li>
      <li>Blue fish</li>
      <li>Old fish</li>
      <li>New fish.</li>
      <li>This one has a little star.</li>
      <li>This one has a little car.</li>
      <li>Say! What a lot</li>
      <li>Of fish there are.</li>
      <li>Yes. Some are red. And some are blue.</li>
      <li>Some are old. And some are new.</li>
      <li>Some are sad.</li>
      <li>And some are glad.</li>
      <li>And some are very, very bad.</li>
      <li>Why are they</li>
      <li>Sad and glad and bad?</li>
      <li>I do not know.</li>
      <li>Go ask your dad.</li>
      <li>Some are thin.</li>
      <li>And some are fat.</li>
      <li>The fat one has</li>
      <li>A yellow hat.</li>
      <li>From there to here, from here to there,</li>
      <li>Funny things</li>
      <li>Are everywhere.</li>
    </ol>
    <p>--Dr. Seuss</p>
    

#### CSS

We define the `<ol>` to be a multi-column container by setting the [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
 property to `150px`, meaning the container will contain as many columns as possible with each being at least `150px` wide. The [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 property sets a horizontal gap between columns and a vertical gap between rows of columns. We then set the `column-height` to `3em`, causing the `column-wrap` property's default `auto` value to resolve to `wrap` to create wrapped rows of columns.

css

    ol {
      column-width: 150px;
      gap: 2em;
      column-height: 3em;
    }
    

#### Result

### [Comparing `wrap` and `nowrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap#comparing_wrap_and_nowrap)

This example features a multi-column layout that demonstrates the difference between the `wrap` and `nowrap` values by allowing you to toggle the column container's `column-wrap` value between the two. The result is a layout that dynamically changes between horizontal and vertical scrolling.

#### HTML and JavaScript

The markup for this example contains multiple paragraphs of content, taken from MDN's HTML, CSS, and JavaScript home pages, and a JavaScript-powered [`<input type="checkbox">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox)
 element to toggle the container's `column-wrap` property value between `nowrap` and `wrap`. The HTML and JavaScript have been hidden for brevity.

    <form>
      <label for="set-wrap"
        >Set <code>column-wrap</code> to <code>wrap</code></label
      >
      <input type="checkbox" id="set-wrap" />
    </form>
    <h1>HTML, CSS, and JavaScript summaries</h1>
    <p>
      <strong>HTML</strong> (HyperText Markup Language) is the most basic building
      block of the Web. It defines the meaning and structure of web content. Other
      technologies besides HTML are generally used to describe a web page's
      appearance (CSS) or behavior (JavaScript).
    </p>
    <p>
      "Hypertext" refers to text containing links that connect web pages to one
      another, either within a single website or between websites. Links are a
      fundamental aspect of the Web. By uploading content to the Internet and
      linking it to pages created by other people, you become an active participant
      in the World Wide Web.
    </p>
    <p>
      HTML uses "markup" to annotate text, images, and other content for display in
      a Web browser. HTML markup includes special "elements" such as
      <a href="/en-US/docs/Web/HTML/Reference/Elements/head"
        ><code>&lt;head&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/title"
        ><code>&lt;title&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/body"
        ><code>&lt;body&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/header"
        ><code>&lt;header&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/footer"
        ><code>&lt;footer&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/article"
        ><code>&lt;article&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/section"
        ><code>&lt;section&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/p"><code>&lt;p&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/div"
        ><code>&lt;div&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/span"
        ><code>&lt;span&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/img"
        ><code>&lt;img&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/aside"
        ><code>&lt;aside&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/audio"
        ><code>&lt;audio&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/canvas"
        ><code>&lt;canvas&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/datalist"
        ><code>&lt;datalist&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/details"
        ><code>&lt;details&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/embed"
        ><code>&lt;embed&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/nav"
        ><code>&lt;nav&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/search"
        ><code>&lt;search&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/output"
        ><code>&lt;output&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/progress"
        ><code>&lt;progress&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/video"
        ><code>&lt;video&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/ul"
        ><code>&lt;ul&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/ol"
        ><code>&lt;ol&gt;</code></a
      >,
      <a href="/en-US/docs/Web/HTML/Reference/Elements/li"
        ><code>&lt;li&gt;</code></a
      >
      and many others.
    </p>
    <p>
      An HTML element is set off from other text in a document by "tags", which
      consist of the element name surrounded by <code>&lt;</code> and
      <code>&gt;</code>. The name of an element inside a tag is case-insensitive.
      That is, it can be written in uppercase, lowercase, or a mixture. For example,
      the <code>&lt;title&gt;</code> tag can be written as
      <code>&lt;Title&gt;</code>, <code>&lt;TITLE&gt;</code>, or in any other way.
      However, the convention and recommended practice is to write tags in
      lowercase.
    </p>
    
    <hr />
    
    <p>
      <strong>Cascading Style Sheets</strong> (<strong>CSS</strong>) is a
      <a href="/en-US/docs/Web/API/StyleSheet">stylesheet</a> language used to
      describe the presentation of a document written in
      <a href="/en-US/docs/Web/HTML">HTML</a> or
      <a href="/en-US/docs/Web/XML/Guides/XML_introduction">XML</a> (including XML
      dialects such as <a href="/en-US/docs/Web/SVG">SVG</a>,
      <a href="/en-US/docs/Web/MathML">MathML</a> or
      <a href="/en-US/docs/Glossary/XHTML">XHTML</a>). CSS describes how elements
      should be rendered on screen, on paper, in speech, or on other media.
    </p>
    <p>
      CSS is among the core languages of the <strong>open web</strong> and is
      standardized across web browsers according to
      <a href="https://www.w3.org/Style/CSS/#specs" class="external" target="_blank"
        >W3C specifications</a
      >. Previously, the development of various parts of CSS specification was done
      synchronously, which allowed the versioning of the latest recommendations. You
      might have heard about CSS1, CSS2.1, or even CSS3. There will never be a CSS3
      or a CSS4; rather, everything is now just "CSS" with individual CSS modules
      having version numbers.
    </p>
    <p>
      After CSS 2.1, the scope of the specification increased significantly and the
      progress on different CSS modules started to differ so much, that it became
      more effective to
      <a
        href="https://www.w3.org/Style/CSS/current-work"
        class="external"
        target="_blank"
        >develop and release recommendations separately per module</a
      >. Instead of versioning the CSS specification, W3C now periodically takes a
      snapshot of
      <a href="https://www.w3.org/TR/css/" class="external" target="_blank"
        >the latest stable state of the CSS specification</a
      >
      and individual modules progress. CSS modules now have version numbers, or
      levels, such as
      <a
        href="https://drafts.csswg.org/css-color-5/"
        class="external"
        target="_blank"
        >CSS Color Module Level 5</a
      >.
    </p>
    
    <hr />
    
    <p>
      <strong>JavaScript</strong> (<strong>JS</strong>) is a lightweight interpreted
      (or
      <a href="/en-US/docs/Glossary/Just_In_Time_Compilation"
        >just-in-time compiled</a
      >) programming language with
      <a href="/en-US/docs/Glossary/First-class_Function">first-class functions</a>.
      While it is most well-known as the scripting language for Web pages,
      <a
        href="https://en.wikipedia.org/wiki/JavaScript#Other_usage"
        class="external"
        target="_blank"
        >many non-browser environments</a
      >
      also use it, such as <a href="/en-US/docs/Glossary/Node.js">Node.js</a>,
      <a href="https://couchdb.apache.org/" class="external" target="_blank"
        >Apache CouchDB</a
      >
      and
      <a
        href="https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/"
        class="external"
        target="_blank"
        >Adobe Acrobat</a
      >. JavaScript is a
      <a href="/en-US/docs/Glossary/Prototype-based_programming">prototype-based</a
      >, <a href="/en-US/docs/Glossary/Garbage_collection">garbage-collected</a>,
      <a href="/en-US/docs/Glossary/Dynamic_typing">dynamic</a> language, supporting
      multiple paradigms such as imperative, functional, and object-oriented.
    </p>
    <p>
      JavaScript's dynamic capabilities include runtime object construction,
      variable parameter lists, function variables, dynamic script creation (via
      <a href="/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval"
        ><code>eval</code></a
      >), object introspection (via
      <a href="/en-US/docs/Web/JavaScript/Reference/Statements/for...in"
        ><code>for...in</code></a
      >
      and
      <a
        href="/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object#static_methods"
        ><code>Object</code> utilities</a
      >), and source-code recovery (JavaScript functions store their source text and
      can be retrieved through
      <a
        href="/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/toString"
        ><code>toString()</code></a
      >).
    </p>
    <p>
      This section is dedicated to the JavaScript language itself, and not the parts
      that are specific to Web pages or other host environments. For information
      about <a href="/en-US/docs/Glossary/API">APIs</a> that are specific to Web
      pages, please see <a href="/en-US/docs/Web/API">Web APIs</a> and
      <a href="/en-US/docs/Glossary/DOM">DOM</a>.
    </p>
    <p>
      The standards for JavaScript are the
      <a href="https://tc39.es/ecma262/" class="external" target="_blank"
        >ECMAScript Language Specification</a
      >
      (ECMA-262) and the
      <a href="https://tc39.es/ecma402/" class="external" target="_blank"
        >ECMAScript Internationalization API specification</a
      >
      (ECMA-402). As soon as one browser implements a feature, we try to document
      it. This means that cases where some
      <a href="https://github.com/tc39/proposals" class="external" target="_blank"
        >proposals for new ECMAScript features</a
      >
      have already been implemented in browsers, documentation and examples in MDN
      articles may use some of those new features. Most of the time, this happens
      between the
      <a href="https://tc39.es/process-document/" class="external" target="_blank"
        >stages</a
      >
      3 and 4, and is usually before the spec is officially published.
    </p>
    <p>
      Do not confuse JavaScript with the
      <a
        href="https://en.wikipedia.org/wiki/Java_(programming_language)"
        class="external"
        target="_blank"
        >Java programming language</a
      >
      — <strong>JavaScript is <em>not</em> "Interpreted Java"</strong>. Both "Java"
      and "JavaScript" are trademarks or registered trademarks of Oracle in the U.S.
      and other countries. However, the two programming languages have very
      different syntax, semantics, and use.
    </p>
    <p>
      JavaScript documentation of core language features (pure
      <a
        href="/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview"
        >ECMAScript</a
      >, for the most part) includes the following:
    </p>
    

    const checkbox = document.getElementById("set-wrap");
    checkbox.addEventListener("change", () => {
      if (checkbox.checked) {
        document.body.style.columnWrap = "wrap";
      } else {
        document.body.style.columnWrap = "nowrap";
      }
    });
    

#### CSS

We make the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 element a multi-col container by setting the [`column-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)
 to `3`. We then set a [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 of `3em 2em`, resulting in a `3em` gap between rows and a `2em` gap between columns.

We then set a `column-height` of `90vh`, making the columns nearly as tall as the viewport. We also set `column-wrap` to `nowrap`, causing excess content columns to overflow horizontally. This is required because the initial `column-wrap` value is `auto`, which resolves to `wrap` when `column-height` is set to a `<length>` value.

The checkbox toggles the `column-wrap` property between `nowrap` and `wrap`. When set to `wrap`, the excess content columns overflow vertically into new rows of columns, creating the vertical layout. The `column-height` value causes each row of columns to fill the viewport.

css

    body {
      column-count: 3;
      gap: 3em 2em;
      padding: 0 2em;
      column-height: 90vh;
      column-wrap: nowrap;
    }
    

Next, we set the [`<h1>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
 element's [`column-span`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-span)
 property to `all`, to make the heading span across all the columns, and set the [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
 property of the first [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 to `0` so that it lines up with the top of the columns.

css

    h1 {
      column-span: all;
    }
    
    p:first-of-type {
      margin-top: 0;
    }
    

    * {
      box-sizing: border-box;
    }
    
    html {
      font-family: "Arial", sans-serif;
    }
    
    p {
      line-height: 1.5;
    }
    
    @supports not (column-wrap: wrap) {
      body::before {
        content: "Your browser does not support the 'column-wrap' property.";
        background-color: wheat;
        position: fixed;
        inset: 40% 0;
        height: fit-content;
        text-align: center;
        padding: 1rem 0;
      }
    }
    
    form {
      position: fixed;
      top: 0;
      right: 0;
      background-color: white;
      padding: 5px;
      border: 1px solid black;
    }
    

#### Result

Toggle the checkbox to change the value of the `column-wrap` property and switch the layout between horizontal and vertical scrolling. When `column-wrap` is set to `nowrap`, the columns overflow horizontally; when `column-wrap` is set to `wrap`, new rows of columns are added vertically.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Multi-column Layout Module Level 2  <br>\# propdef-column-wrap](https://drafts.csswg.org/css-multicol-2/#propdef-column-wrap) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap#see_also)

-------------------------------------------------------------------------------------------------------

*   [`column-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)
    
*   [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
    
*   [`columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns)
     shorthand
*   [`column-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height)
    
*   [CSS multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/column-wrap/index.md?plain=1 "Folder: en-us/web/css/reference/properties/column-wrap (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-wrap&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-wrap%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-wrap%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-wrap%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")