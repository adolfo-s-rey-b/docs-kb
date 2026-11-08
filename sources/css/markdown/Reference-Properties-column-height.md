*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height#mdn-search)
    

`column-height` CSS property
============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/960)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height#browser_compatibility)
 carefully before using this in production.

The **`column-height`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the height of the columns in a [CSS multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height#syntax)

-----------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    column-height: auto;
    
    /* <length> value */
    column-height: 300px;
    column-height: 25em;
    column-height: 70vh;
    
    /* Global values */
    column-height: inherit;
    column-height: initial;
    column-height: revert;
    column-height: revert-layer;
    column-height: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height#values)

This property is specified as a single value from the following list:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height#auto)

The initial value. If the content container has a set height, the content columns will grow to that height, overflowing to the side if the content doesn't fit inside the container. If the content container does not have a set height, the content will be equally distributed between the columns generated inside the container.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

The height of the columns. Must be non-negative.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height#description)

---------------------------------------------------------------------------------------------------------------

The `column-height` property sets the height of the columns in a [multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
. This is useful for constraining the column height for readability when setting multiple columns using the [`column-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)
 or [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
 property.

Without `column-height`, if the height of the multi-col content exceeds the viewport height, readers will need to scroll down to the end of a column and then back up to the top of the next column. One possible fix would be to set a fixed height on the content container, however, excess columns will then overflow to the side, and readers will have to scroll in the inline direction to read all the content.

The `column-height` property, along with [`column-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap)
, allows you to set a specific height for the columns and wrap them onto a new row of columns when the container edge is reached.

The default value of `column-wrap` is `auto`, which resolves to `wrap` when `column-height` is set to a `<length>` value; `wrap` allows the fixed-height columns to wrap onto multiple rows. When `column-height` is equal to `auto`, `column-wrap: auto` resolves to `nowrap`, allowing the columns to overflow horizontally if a fixed container height is set. As a result of this default behavior, generally you don't need to explicitly set the `column-wrap` property.

The `column-height` property, along with the [`column-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)
 and [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
 properties, can also be set by using the [`columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns)
 shorthand.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | Block containers except table wrapper boxes |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | `auto` if specified as `auto`, otherwise for [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)<br> the absolute value specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

column-height =   
  auto            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<length \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height#examples)

---------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height#basic_usage)

This example demonstrates basic usage of the `column-height` property to create a wrapped multi-col layout.

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
 property of `2em` sets a horizontal gap between columns and a vertical gap between rows of columns. We then set the `column-height` to `2em`, causing the `column-wrap` property's default `auto` value to resolve to `wrap` to create wrapped rows of columns.

css

    ol {
      column-width: 150px;
      gap: 2em;
      column-height: 3em;
    }
    

#### Result

### [Scroll-snapped columns](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height#scroll-snapped_columns)

This example combines a wrapped multi-column layout with [CSS scroll snapping](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
, creating a usable experience where each scrolling action snaps a new row of columns neatly inside the full height of the viewport for comfortable reading.

#### HTML

The HTML, which contains multiple paragraphs of content from the MDN HTML, CSS, and JavaScript home pages, has been hidden for brevity.

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
    

#### CSS

We start by setting [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
 on the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 element to define the preferred width for the columns. A [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 of `3em 2em` results in a `3em` gap between rows and a `2em` gap between columns. The [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
 adds a line in the center of the gap between the columns. The `column-height` of `95vh` makes the columns nearly as tall as the viewport.

We explicitly set [`column-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap)
 to `wrap` as a reminder of the applied wrapping behavior. We could have set the value to `auto` or omitted the property altogether, as, by default, `column-wrap` resolves to `wrap` when the `column-height` is set to a `<length>` value.

css

    body {
      column-width: 150px;
      column-rule: 2px solid red;
      gap: 3em 2em;
      padding: 0 2em;
      column-height: 95vh;
      column-wrap: wrap;
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
    

Finally, we add scroll snapping by setting [`scroll-snap-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type)
 to `y mandatory` on the [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)
 element, and [`scroll-snap-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align)
 to `start` on the [`::column`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::column)
 pseudo-elements that represent each generated column. This causes the content to snap to the top of a new column each time it is scrolled.

css

    html {
      scroll-snap-type: y mandatory;
    }
    
    ::column {
      scroll-snap-align: start;
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
    

    @supports not (column-height: 15em) {
      body::before {
        content: "Your browser does not support the 'column-height' property.";
        background-color: wheat;
        position: fixed;
        inset: 40% 0;
        height: fit-content;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

#### Result

Try scrolling the content. Note how each new row of columns fills the viewport, and how the content snaps neatly to the top of a new row with each scroll.

### [`column-height` and `column-count` playground](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height#column-height_and_column-count_playground)

This example builds upon the previous one by including two range sliders that allow you to adjust the multiple-column layout's column count and column height.

#### HTML and JavaScript

The HTML is the same as the previous example, with the addition of a form containing two [`<input="range">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range)
 elements that update the `column-count` and `column-height` values via JavaScript. The HTML and JavaScript are hidden for brevity.

    <form>
      <div>
        <label for="columns">
          <code>column-count <output id="columns-output">3</output></code>
        </label>
        <input type="range" min="3" max="6" value="3" id="columns" />
      </div>
      <div>
        <label for="column-height">
          <code>column-height <output id="column-height-output">20em</output></code>
        </label>
        <input type="range" min="10" max="30" value="20" id="column-height" />
      </div>
    </form>
    

    const columnsRange = document.getElementById("columns");
    const columnsOutput = document.getElementById("columns-output");
    const columnHeightRange = document.getElementById("column-height");
    const columnHeightOutput = document.getElementById("column-height-output");
    
    columnsRange.addEventListener("input", () => {
      document.body.style.columnCount = columnsRange.value;
      columnsOutput.textContent = columnsRange.value;
    });
    
    columnHeightRange.addEventListener("input", () => {
      document.body.style.columnHeight = `${columnHeightRange.value}em`;
      columnHeightOutput.textContent = `${columnHeightRange.value}em`;
    });
    

#### CSS

We specify the [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
 and [`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
 with the same values as the previous example. We don't specify a `column-width`; instead, we create a multi-column layout using the [`column-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)
 property, interactively setting the number of columns and the height of the column rows using JavaScript. Scroll snapping is not included in this example.

css

    body {
      column-count: 3;
      column-height: 20em;
      column-rule: 2px solid red;
      gap: 3em 2em;
      padding: 0 2em;
    }
    

    form {
      border: 1px solid black;
      background-color: white;
      padding: 10px;
      position: fixed;
      bottom: 1px;
      right: 1px;
    }
    
    form div {
      display: flex;
      gap: 1em;
      align-items: center;
      justify-content: space-between;
    }
    

#### Result

Adjust the number of columns and the column height to see the effect of these properties.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Multi-column Layout Module Level 2  <br>\# propdef-column-height](https://drafts.csswg.org/css-multicol-2/#propdef-column-height) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height#see_also)

---------------------------------------------------------------------------------------------------------

*   [`column-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)
    
*   [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
    
*   [`columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns)
     shorthand
*   [`column-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap)
    
*   [CSS multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 1, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/column-height/index.md?plain=1 "Folder: en-us/web/css/reference/properties/column-height (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-height&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-height%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolumn-height%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolumn-height%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F25e50f8d5b36eb86d40916f6f06051671333f3a7%0A*+Document+last+modified%3A+2026-10-01T19%3A24%3A46.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")