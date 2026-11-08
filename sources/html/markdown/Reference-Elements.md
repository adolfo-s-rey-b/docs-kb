*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#mdn-search)
    

HTML elements reference
=======================

This page lists all the [HTML](https://developer.mozilla.org/en-US/docs/Glossary/HTML)
 [elements](https://developer.mozilla.org/en-US/docs/Glossary/Element)
, which are created using [tags](https://developer.mozilla.org/en-US/docs/Glossary/Tag)
.

They are grouped by function to help you find what you have in mind easily. An alphabetical list of all elements is provided in the sidebar on every element's page as well as this one.

**Note:** For more information about the basics of HTML elements and attributes, see [Anatomy of an HTML element](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax#anatomy_of_an_html_element)
.

[Main root](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#main_root)

--------------------------------------------------------------------------------------------

| Element | Description |
| --- | --- |
| [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html) | Represents the root (top-level element) of an HTML document, so it is also referred to as the _root element_. All other elements must be descendants of this element. |

[Document metadata](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#document_metadata)

------------------------------------------------------------------------------------------------------------

Metadata contains information about the page. This includes information about styles, scripts and data to help software ([search engines](https://developer.mozilla.org/en-US/docs/Glossary/Search_engine)
, [browsers](https://developer.mozilla.org/en-US/docs/Glossary/Browser)
, etc.) use and render the page. Metadata for styles and scripts may be defined in the page or linked to another file that has the information.

| Element | Description |
| --- | --- |
| [`<base>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base) | Specifies the base URL to use for all relative URLs in a document. There can be only one such element in a document. |
| [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head) | Contains machine-readable information (metadata) about the document, like its [title](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title)<br>, [scripts](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)<br>, and [style sheets](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style)<br>. |
| [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link) | Specifies relationships between the current document and an external resource. This element is most commonly used to link to CSS but is also used to establish site icons (both "favicon" style icons and icons for the home screen and apps on mobile devices) among other things. |
| [`<meta>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta) | Represents [metadata](https://developer.mozilla.org/en-US/docs/Glossary/Metadata)<br> that cannot be represented by other HTML meta-related elements, like [`<base>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/base)<br>, [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)<br>, [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)<br>, [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style)<br> and [`<title>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title)<br>. |
| [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style) | Contains style information for a document or part of a document. It contains CSS, which is applied to the contents of the document containing this element. |
| [`<title>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title) | Defines the document's title that is shown in a [browser](https://developer.mozilla.org/en-US/docs/Glossary/Browser)<br>'s title bar or a page's tab. It only contains text; HTML tags within the element, if any, are also treated as plain text. |

[Sectioning root](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#sectioning_root)

--------------------------------------------------------------------------------------------------------

| Element | Description |
| --- | --- |
| [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body) | Represents the content of an HTML document. There can be only one such element in a document. |

[Content sectioning](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#content_sectioning)

--------------------------------------------------------------------------------------------------------------

Content sectioning elements allow you to organize the document content into logical pieces. Use the sectioning elements to create a broad outline for your page content, including header and footer navigation, and heading elements to identify sections of content.

| Element | Description |
| --- | --- |
| [`<address>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address) | Indicates that the enclosed HTML provides contact information for a person or people, or for an organization. |
| [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article) | Represents a self-contained composition in a document, page, application, or site, which is intended to be independently distributable or reusable (e.g., in syndication). Examples include a forum post, a magazine or newspaper article, a blog entry, a product card, a user-submitted comment, an interactive widget or gadget, or any other independent item of content. |
| [`<aside>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/aside) | Represents a portion of a document whose content is only indirectly related to the document's main content. Asides are frequently presented as sidebars or call-out boxes. |
| [`<footer>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer) | Represents a footer for its nearest ancestor [sectioning content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#sectioning_content)<br> or [sectioning root](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br> element. A `<footer>` typically contains information about the author of the section, copyright data, or links to related documents. |
| [`<header>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header) | Represents introductory content, typically a group of introductory or navigational aids. It may contain some heading elements but also a logo, a search form, an author name, and other elements. |
| [`<h1>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br>, [`<h2>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br>, [`<h3>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br>, [`<h4>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br>, [`<h5>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br>, [`<h6>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements) | Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest. |
| [`<hgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hgroup) | Represents a heading grouped with any secondary content, such as subheadings, an alternative title, or a tagline. |
| [`<main>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main) | Represents the dominant content of the body of a document. The main content area consists of content that is directly related to or expands upon the central topic of a document, or the central functionality of an application. |
| [`<nav>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav) | Represents a section of a page whose purpose is to provide navigation links, either within the current document or to other documents. Common examples of navigation sections are menus, tables of contents, and indexes. |
| [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section) | Represents a generic standalone section of a document, which doesn't have a more specific semantic element to represent it. Sections should always have a heading, with very few exceptions. |
| [`<search>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/search) | Represents a part that contains a set of form controls or other content related to performing a search or filtering operation. |

[Text content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#text_content)

--------------------------------------------------------------------------------------------------

Use HTML text content elements to organize blocks or sections of content placed between the opening [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 and closing `</body>` tags. Important for [accessibility](https://developer.mozilla.org/en-US/docs/Glossary/Accessibility)
 and [SEO](https://developer.mozilla.org/en-US/docs/Glossary/SEO)
, these elements identify the purpose or structure of that content.

| Element | Description |
| --- | --- |
| [`<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote) | Indicates that the enclosed text is an extended quotation. Usually, this is rendered visually by indentation. A URL for the source of the quotation may be given using the `cite` attribute, while a text representation of the source can be given using the [`<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite)<br> element. |
| [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dd) | Provides the description, definition, or value for the preceding term ([`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt)<br>) in a description list ([`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl)<br>). |
| [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div) | The generic container for flow content. It has no effect on the content or layout until styled in some way using CSS (e.g., styling is directly applied to it, or some kind of layout model like [flexbox](https://developer.mozilla.org/en-US/docs/Glossary/Flexbox)<br> is applied to its parent element). |
| [`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl) | Represents a description list. The element encloses a list of groups of terms (specified using the [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt)<br> element) and descriptions (provided by [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dd)<br> elements). Common uses for this element are to implement a glossary or to display metadata (a list of key-value pairs). |
| [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt) | Specifies a term in a description or definition list, and as such must be used inside a [`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl)<br> element. It is usually followed by a [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dd)<br> element; however, multiple `<dt>` elements in a row indicate several terms that are all defined by the immediate next [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dd)<br> element. |
| [`<figcaption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figcaption) | Represents a caption or legend describing the rest of the contents of its parent [`<figure>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure)<br> element. |
| [`<figure>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure) | Represents self-contained content, potentially with an optional caption, which is specified using the [`<figcaption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figcaption)<br> element. The figure, its caption, and its contents are referenced as a single unit. |
| [`<hr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr) | Represents a thematic break between paragraph-level elements: for example, a change of scene in a story, or a shift of topic within a section. |
| [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li) | Represents an item in a list. It must be contained in a parent element: an ordered list ([`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)<br>), an unordered list ([`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)<br>), or a menu ([`<menu>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu)<br>). In menus and unordered lists, list items are usually displayed using bullet points. In ordered lists, they are usually displayed with an ascending counter on the left, such as a number or letter. |
| [`<menu>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu) | A semantic alternative to [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)<br>, but treated by browsers (and exposed through the accessibility tree) as no different than [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)<br>. It represents an unordered list of items (which are represented by [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)<br> elements). |
| [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol) | Represents an ordered list of items — typically rendered as a numbered list. |
| [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p) | Represents a paragraph. Paragraphs are usually represented in visual media as blocks of text separated from adjacent blocks by blank lines and/or first-line indentation, but HTML paragraphs can be any structural grouping of related content, such as images or form fields. |
| [`<pre>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre) | Represents preformatted text which is to be presented exactly as written in the HTML file. The text is typically rendered using a non-proportional, or [monospaced](https://en.wikipedia.org/wiki/Monospaced_font "External link (opens in new tab)")<br>, font. Whitespace inside this element is displayed as written. |
| [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul) | Represents an unordered list of items, typically rendered as a bulleted list. |

[Inline text semantics](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#inline_text_semantics)

--------------------------------------------------------------------------------------------------------------------

Use the HTML inline text semantic to define the meaning, structure, or style of a word, line, or any arbitrary piece of text.

| Element | Description |
| --- | --- |
| [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a) | Together with its `href` attribute, creates a hyperlink to web pages, files, email addresses, locations within the current page, or anything else a URL can address. |
| [`<abbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr) | Represents an abbreviation or acronym. |
| [`<b>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b) | Used to draw the reader's attention to the element's contents, which are not otherwise granted special importance. This was formerly known as the Boldface element, and most browsers still draw the text in boldface. However, you should not use `<b>` for styling text or granting importance. If you wish to create boldface text, you should use the CSS [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)<br> property. If you wish to indicate an element is of special importance, you should use the [`<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong)<br> element. |
| [`<bdi>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi) | Tells the browser's bidirectional algorithm to treat the text it contains in isolation from its surrounding text. It's particularly useful when a website dynamically inserts some text and doesn't know the directionality of the text being inserted. |
| [`<bdo>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdo) | Overrides the current directionality of text, so that the text within is rendered in a different direction. |
| [`<br>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br) | Produces a line break in text (carriage-return). It is useful for writing a poem or an address, where the division of lines is significant. |
| [`<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite) | Used to mark up the title of a creative work. The reference may be in an abbreviated form according to context-appropriate conventions related to citation metadata. |
| [`<code>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/code) | Displays its contents styled in a fashion intended to indicate that the text is a short fragment of computer code. By default, the content text is displayed using the user agent's default monospace font. |
| [`<data>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/data) | Links a given piece of content with a machine-readable translation. If the content is time- or date-related, the `<time>` element must be used. |
| [`<dfn>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn) | Used to indicate the term being defined within the context of a definition phrase or sentence. The ancestor [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)<br> element, the [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt)<br>/[`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dd)<br> pairing, or the nearest section ancestor of the `<dfn>` element, is considered to be the definition of the term. |
| [`<em>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/em) | Marks text that has stress emphasis. The `<em>` element can be nested, with each nesting level indicating a greater degree of emphasis. |
| [`<i>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i) | Represents a range of text that is set off from the normal text for some reason, such as idiomatic text, technical terms, and taxonomical designations, among others. Historically, these have been presented using italicized type, which is the original source of the `<i>` naming of this element. |
| [`<kbd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd) | Represents a span of inline text denoting textual user input from a keyboard, voice input, or any other text entry device. By convention, the user agent defaults to rendering the contents of a `<kbd>` element using its default monospace font, although this is not mandated by the HTML standard. |
| [`<mark>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/mark) | Represents text which is marked or highlighted for reference or notation purposes due to the marked passage's relevance in the enclosing context. |
| [`<q>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/q) | Indicates that the enclosed text is a short inline quotation. Most modern browsers implement this by surrounding the text in quotation marks. This element is intended for short quotations that don't require paragraph breaks; for long quotations use the [`<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote)<br> element. |
| [`<rp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rp) | Used to provide fall-back parentheses for browsers that do not support the display of ruby annotations using the [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)<br> element. One `<rp>` element should enclose each of the opening and closing parentheses that wrap the [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)<br> element that contains the annotation's text. |
| [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt) | Specifies the ruby text component of a ruby annotation, which is used to provide pronunciation, translation, or transliteration information for East Asian typography. The `<rt>` element must always be contained within a [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)<br> element. |
| [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby) | Represents small annotations that are rendered above, below, or next to base text, usually used for showing the pronunciation of East Asian characters. It can also be used for annotating other kinds of text, but this usage is less common. |
| [`<s>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/s) | Renders text with a strikethrough, or a line through it. Use the `<s>` element to represent things that are no longer relevant or no longer accurate. However, `<s>` is not appropriate when indicating document edits; for that, use the [`<del>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del)<br> and [`<ins>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins)<br> elements, as appropriate. |
| [`<samp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/samp) | Used to enclose inline text which represents sample (or quoted) output from a computer program. Its contents are typically rendered using the browser's default monospaced font (such as [Courier](https://en.wikipedia.org/wiki/Courier_(typeface) "External link (opens in new tab)")<br> or Lucida Console). |
| [`<small>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/small) | Represents side-comments and small print, like copyright and legal text, independent of its styled presentation. By default, it renders text within it one font size smaller, such as from `small` to `x-small`. |
| [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span) | A generic inline container for phrasing content, which does not inherently represent anything. It can be used to group elements for styling purposes (using the `class` or `id` attributes), or because they share attribute values, such as `lang`. It should be used only when no other semantic element is appropriate. `<span>` is very much like a div element, but div is a [block-level element](https://developer.mozilla.org/en-US/docs/Glossary/Block-level_content)<br> whereas a `<span>` is an [inline-level element](https://developer.mozilla.org/en-US/docs/Glossary/Inline-level_content)<br>. |
| [`<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong) | Indicates that its contents have strong importance, seriousness, or urgency. Browsers typically render the contents in bold type. |
| [`<sub>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub) | Specifies inline text which should be displayed as subscript for solely typographical reasons. Subscripts are typically rendered with a lowered baseline using smaller text. |
| [`<sup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup) | Specifies inline text which is to be displayed as superscript for solely typographical reasons. Superscripts are usually rendered with a raised baseline using smaller text. |
| [`<time>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time) | Represents a specific period in time. It may include the `datetime` attribute to translate dates into machine-readable format, allowing for better search engine results or custom features such as reminders. |
| [`<u>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/u) | Represents a span of inline text which should be rendered in a way that indicates that it has a non-textual annotation. This is rendered by default as a single solid underline but may be altered using CSS. |
| [`<var>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/var) | Represents the name of a variable in a mathematical expression or a programming context. It's typically presented using an italicized version of the current typeface, although that behavior is browser-dependent. |
| [`<wbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr) | Represents a word break opportunity—a position within text where the browser may optionally break a line, though its line-breaking rules would not otherwise create a break at that location. |

[Image and multimedia](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#image_and_multimedia)

------------------------------------------------------------------------------------------------------------------

HTML supports various multimedia resources such as images, audio, and video.

| Element | Description |
| --- | --- |
| [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area) | Defines an area inside an image map that has predefined clickable areas. An _image map_ allows geometric areas on an image to be associated with [hyperlink](https://developer.mozilla.org/en-US/docs/Glossary/Hyperlink)<br>. |
| [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio) | Used to embed sound content in documents. It may contain one or more audio sources, represented using the `src` attribute or the source element: the browser will choose the most suitable one. It can also be the destination for streamed media, using a [`MediaStream`](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream)<br>. |
| [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img) | Embeds an image into the document. |
| [`<map>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map) | Used with [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)<br> elements to define an image map (a clickable link area). |
| [`<track>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track) | Used as a child of the media elements, audio and video. It lets you specify timed text tracks (or time-based data), for example to automatically handle subtitles. The tracks are formatted in [WebVTT format](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)<br> (`.vtt` files)—Web Video Text Tracks. |
| [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video) | Embeds a media player which supports video playback into the document. You can also use `<video>` for audio content, but the audio element may provide a more appropriate user experience. |

[Embedded content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#embedded_content)

----------------------------------------------------------------------------------------------------------

In addition to regular multimedia content, HTML can include a variety of other content, even if it's not always easy to interact with.

| Element | Description |
| --- | --- |
| [`<embed>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/embed) | Embeds external content at the specified point in the document. This content is handled by the browser or an external application. |
| [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe) | Represents a nested browsing context, embedding another document into the current one. |
| [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object) | Represents an external resource, which can be treated as an image, a nested browsing context, or a resource to be handled by a plugin. |
| [`<picture>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/picture) | Contains zero or more [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source)<br> elements and one [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)<br> element to offer alternative versions of an image for different display/device scenarios. |
| [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/source) | Specifies multiple media resources for the picture, the audio element, or the video element. It is a void element, meaning that it has no content and does not have a closing tag. It is commonly used to offer the same media content in multiple file formats in order to provide compatibility with a broad range of browsers given their differing support for [image file formats](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Image_types)<br> and [media file formats](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats)<br>. |

[SVG and MathML](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#svg_and_mathml)

------------------------------------------------------------------------------------------------------

You can embed [SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)
 and [MathML](https://developer.mozilla.org/en-US/docs/Web/MathML)
 content directly into HTML documents, using the [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
 and [`<math>`](https://developer.mozilla.org/en-US/docs/Web/MathML/Reference/Element/math "<math>")
 elements.

| Element | Description |
| --- | --- |
| [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg) | Container defining a new coordinate system and [viewport](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/viewBox)<br>. It is used as the outermost element of SVG documents, but it can also be used to embed an SVG fragment inside an SVG or HTML document. |
| [`<math>`](https://developer.mozilla.org/en-US/docs/Web/MathML/Reference/Element/math "<math>") | The top-level element in MathML. Every valid MathML instance must be wrapped in it. In addition, you must not nest a second `<math>` element in another, but you can have an arbitrary number of other child elements in it. |

[Scripting](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#scripting)

--------------------------------------------------------------------------------------------

To create dynamic content and Web applications, HTML supports the use of scripting languages, most prominently JavaScript. Certain elements support this capability.

| Element | Description |
| --- | --- |
| [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas) | Container element to use with either the [canvas scripting API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)<br> or the [WebGL API](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API)<br> to draw graphics and animations. |
| [`<noscript>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noscript) | Defines a section of HTML to be inserted if a script type on the page is unsupported or if scripting is currently turned off in the browser. |
| [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script) | Used to embed executable code or data; this is typically used to embed or refer to JavaScript code. The `<script>` element can also be used with other languages, such as [WebGL](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API)<br>'s GLSL shader programming language and [JSON](https://developer.mozilla.org/en-US/docs/Glossary/JSON)<br>. |

[Demarcating edits](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#demarcating_edits)

------------------------------------------------------------------------------------------------------------

These elements let you provide indications that specific parts of the text have been altered.

| Element | Description |
| --- | --- |
| [`<del>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del) | Represents a range of text that has been deleted from a document. This can be used when rendering "track changes" or source code diff information, for example. The `<ins>` element can be used for the opposite purpose: to indicate text that has been added to the document. |
| [`<ins>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins) | Represents a range of text that has been added to a document. You can use the `<del>` element to similarly represent a range of text that has been deleted from the document. |

[Table content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#table_content)

----------------------------------------------------------------------------------------------------

The elements here are used to create and handle tabular data.

| Element | Description |
| --- | --- |
| [`<caption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/caption) | Specifies the caption (or title) of a table. |
| [`<col>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col) | Defines one or more columns in a column group represented by its implicit or explicit parent [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup)<br> element. The `<col>` element is only valid as a child of a [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup)<br> element that has no [`span`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#span)<br> attribute defined. |
| [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup) | Defines a group of columns within a table. |
| [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table) | Represents tabular data—that is, information presented in a two-dimensional table comprised of rows and columns of cells containing data. |
| [`<tbody>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tbody) | Encapsulates a set of table rows ([`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)<br> elements), indicating that they comprise the body of a table's (main) data. |
| [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td) | A child of the [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)<br> element, it defines a cell of a table that contains data. |
| [`<tfoot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tfoot) | Encapsulates a set of table rows ([`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)<br> elements), indicating that they comprise the foot of a table with information about the table's columns. This is usually a summary of the columns, e.g., a sum of the given numbers in a column. |
| [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th) | A child of the [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)<br> element, it defines a cell as the header of a group of table cells. The nature of this group can be explicitly defined by the [`scope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#scope)<br> and [`headers`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th#headers)<br> attributes. |
| [`<thead>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/thead) | Encapsulates a set of table rows ([`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr)<br> elements), indicating that they comprise the head of a table with information about the table's columns. This is usually in the form of column headers ([`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)<br> elements). |
| [`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tr) | Defines a row of cells in a table. The row's cells can then be established using a mix of [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/td)<br> (data cell) and [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)<br> (header cell) elements. |

[Forms](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#forms)

------------------------------------------------------------------------------------

HTML provides several elements that can be used together to create forms that the user can fill out and submit to the website or application. Further information about this available in the [HTML forms guide](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms)
.

| Element | Description |
| --- | --- |
| [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button) | An interactive element activated by a user with a mouse, keyboard, finger, voice command, or other assistive technology. Once activated, it performs an action, such as submitting a [form](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms)<br> or opening a dialog. |
| [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist) | Contains a set of [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)<br> elements that represent the permissible or recommended options available to choose from within other controls. |
| [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset) | Used to group several controls as well as labels ([`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)<br>) within a web form. |
| [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form) | Represents a document section containing interactive controls for submitting information. |
| [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input) | Used to create interactive controls for web-based forms to accept data from the user; a wide variety of types of input data and control widgets are available, depending on the device and user agent. The `<input>` element is one of the most powerful and complex in all of HTML due to the sheer number of combinations of input types and attributes. |
| [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label) | Represents a caption for an item in a user interface. |
| [`<legend>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/legend) | Represents a caption for the content of its parent [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)<br>. |
| [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter) | Represents either a scalar value within a known range or a fractional value. |
| [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup) | Creates a grouping of options within a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)<br> element. |
| [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option) | Used to define an item contained in a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)<br>, an [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup)<br>, or a [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)<br> element. As such, `<option>` can represent menu items in popups and other lists of items in an HTML document. |
| [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output) | Container element into which a site or app can inject the results of a calculation or the outcome of a user action. |
| [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress) | Displays an indicator showing the completion progress of a task, typically displayed as a progress bar. |
| [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select) | Represents a control that provides a menu of options. |
| [`<selectedcontent>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/selectedcontent) | Displays the content of the currently selected `<option>` inside a closed `<select>` element. |
| [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea) | Represents a multi-line plain-text editing control, useful when you want to allow users to enter a sizeable amount of free-form text, for example, a comment on a review or feedback form. |

[Interactive elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#interactive_elements)

------------------------------------------------------------------------------------------------------------------

HTML offers a selection of elements that help to create interactive user interface objects.

| Element | Description |
| --- | --- |
| [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details) | Creates a disclosure widget in which information is visible only when the widget is toggled into an "open" state. A summary or label must be provided using the [`<summary>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary)<br> element. |
| [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog) | Represents a dialog box or other interactive component, such as a dismissible alert, inspector, or subwindow. |
| [`<geolocation>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/geolocation) | Creates an interactive control for the user to share their geolocation data with the page. |
| [`<summary>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary) | Specifies a summary, caption, or legend for a details element's disclosure box. Clicking the `<summary>` element toggles the state of the parent [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)<br> element open and closed. |

[Web Components](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#web_components)

------------------------------------------------------------------------------------------------------

Web Components is an HTML-related technology that makes it possible to, essentially, create and use custom elements as if it were regular HTML. In addition, you can create custom versions of standard HTML elements.

| Element | Description |
| --- | --- |
| [`<slot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot) | Part of the [Web Components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components)<br> technology suite, this element is a placeholder inside a web component that you can fill with your own markup, which lets you create separate DOM trees and present them together. |
| [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template) | A mechanism for holding HTML that is not to be rendered immediately when a page is loaded but may be instantiated subsequently during runtime using JavaScript. |

[Obsolete and deprecated elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#obsolete_and_deprecated_elements)

------------------------------------------------------------------------------------------------------------------------------------------

**Warning:** These are old HTML elements that are deprecated and should not be used. **You should never use them in new projects, and you should replace them in old projects as soon as you can.** They are listed here for completeness only.

| Element | Description |
| --- | --- |
| [`<acronym>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/acronym) | Allows authors to clearly indicate a sequence of characters that compose an acronym or abbreviation for a word. |
| [`<big>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/big) | Renders the enclosed text at a font size one level larger than the surrounding text (`medium` becomes `large`, for example). The size is capped at the browser's maximum permitted font size. |
| [`<center>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/center) | Displays its block-level or inline contents centered horizontally within its containing element. |
| `<content>` | An obsolete part of the [Web Components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components)<br> suite of technologies—was used inside of [Shadow DOM](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM)<br> as an insertion point, and wasn't meant to be used in ordinary HTML. It has now been replaced by the [`<slot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot)<br> element, which creates a point in the DOM at which a shadow DOM can be inserted. Consider using [`<slot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot)<br> instead. |
| [`<dir>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dir) | Container for a directory of files and/or folders, potentially with styles and icons applied by the user agent. Do not use this obsolete element; instead, you should use the [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)<br> element for lists, including lists of files. |
| [`<fencedframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fencedframe) | Represents a nested browsing context, like `<iframe>` but with more native privacy features built in. |
| [`<font>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/font) | Defines the font size, color and face for its content. |
| [`<frame>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame) | Defines a particular area in which another HTML document can be displayed. A frame should be used within a [`<frameset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frameset)<br>. |
| [`<frameset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frameset) | Used to contain [`<frame>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame)<br> elements. |
| `<image>` | An ancient and poorly supported precursor to the [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)<br> element. It should not be used. |
| [`<marquee>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/marquee) | Used to insert a scrolling area of text. You can control what happens when the text reaches the edges of its content area using its attributes. |
| `<menuitem>` | Represents a command that a user is able to invoke through a popup menu. This includes context menus, as well as menus that might be attached to a menu button. |
| [`<nobr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nobr) | Prevents the text it contains from automatically wrapping across multiple lines, potentially resulting in the user having to scroll horizontally to see the entire width of the text. |
| [`<noembed>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noembed) | An obsolete, non-standard way to provide alternative, or "fallback", content for browsers that do not support the embed element or do not support the type of [embedded content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#embedded_content)<br> an author wishes to use. This element was deprecated in HTML 4.01 and above in favor of placing fallback content between the opening and closing tags of an [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object)<br> element. |
| [`<noframes>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noframes) | Provides content to be presented in browsers that don't support (or have disabled support for) the [`<frame>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frame)<br> element. Although most commonly-used browsers support frames, there are exceptions, including certain special-use browsers including some mobile browsers, as well as text-mode browsers. |
| [`<param>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/param) | Defines parameters for an [`<object>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/object)<br> element. |
| [`<plaintext>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/plaintext) | Renders everything following the start tag as raw text, ignoring any following HTML. There is no closing tag, since everything after it is considered raw text. |
| [`<rb>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rb) | Used to delimit the base text component of a ruby annotation, i.e., the text that is being annotated. One `<rb>` element should wrap each separate atomic segment of the base text. |
| [`<rtc>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rtc) | Embraces semantic annotations of characters presented in a ruby of [`<rb>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rb)<br> elements used inside of [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)<br> element. [`<rb>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rb)<br> elements can have both pronunciation ([`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)<br>) and semantic ([`<rtc>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rtc)<br>) annotations. |
| `<shadow>` | An obsolete part of the [Web Components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components)<br> technology suite that was intended to be used as a shadow DOM insertion point. You might have used it if you have created multiple shadow roots under a shadow host. Consider using [`<slot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot)<br> instead. |
| [`<strike>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strike) | Places a strikethrough (horizontal line) over text. |
| [`<tt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tt) | Creates inline text which is presented using the user agent default monospace font face. This element was created for the purpose of rendering text as it would be displayed on a fixed-width display such as a teletype, text-only screen, or line printer. |
| [`<xmp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/xmp) | Renders text between the start and end tags without interpreting the HTML in between and using a monospaced font. The HTML2 specification recommended that it should be rendered wide enough to allow 80 characters per line. |

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#see_also)

------------------------------------------------------------------------------------------

*   [`Element`](https://developer.mozilla.org/en-US/docs/Web/API/Element)
     interface

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/index.md?plain=1 "Folder: en-us/web/html/reference/elements (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F456c370394c0cd8869feb60c4e9926f35422beaf%0A*+Document+last+modified%3A+2026-09-16T03%3A52%3A25.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")