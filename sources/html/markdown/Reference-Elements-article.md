*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article#mdn-search)
    

`<article>` HTML article contents element
=========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<article>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents a self-contained composition in a document, page, application, or site, which is intended to be independently distributable or reusable (e.g., in syndication). Examples include: a forum post, a magazine or newspaper article, or a blog entry, a product card, a user-submitted comment, an interactive widget or gadget, or any other independent item of content.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article#try_it)

----------------------------------------------------------------------------------------------

    <article class="forecast">
      <h1>Weather forecast for Seattle</h1>
      <article class="day-forecast">
        <h2>03 March 2018</h2>
        <p>Rain.</p>
      </article>
      <article class="day-forecast">
        <h2>04 March 2018</h2>
        <p>Periods of rain.</p>
      </article>
      <article class="day-forecast">
        <h2>05 March 2018</h2>
        <p>Heavy rain.</p>
      </article>
    </article>
    

    .forecast {
      margin: 0;
      padding: 0.3rem;
      background-color: #eeeeee;
    }
    
    .forecast > h1,
    .day-forecast {
      margin: 0.5rem;
      padding: 0.3rem;
      font-size: 1.2rem;
    }
    
    .day-forecast {
      background: right/contain content-box border-box no-repeat
        url("/shared-assets/images/examples/rain.svg") white;
    }
    
    .day-forecast > h2,
    .day-forecast > p {
      margin: 0.2rem;
      font-size: 1rem;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article#attributes)

------------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article#usage_notes)

--------------------------------------------------------------------------------------------------------

A given document can have multiple articles in it; for example, on a blog that shows the text of each article one after another as the reader scrolls, each post would be contained in an `<article>` element, possibly with one or more `<section>`s within.

*   Each `<article>` should be identified, typically by including a heading ([`<h1>` - `<h6>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
     element) as a child of the `<article>` element.
*   When an `<article>` element is nested, the inner element represents an article related to the outer element. For example, the comments of a blog post can be `<article>` elements nested in the `<article>` representing the blog post.
*   Author information of an `<article>` element can be provided through the [`<address>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address)
     element, but it doesn't apply to nested `<article>` elements.
*   The publication date and time of an `<article>` element can be described using the [`datetime`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time#datetime)
     attribute of a [`<time>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/time)
     element.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article#examples)

--------------------------------------------------------------------------------------------------

html

    <article class="film_review">
      <h2>Jurassic Park</h2>
      <section class="main_review">
        <h3>Review</h3>
        <p>Dinos were great!</p>
      </section>
      <section class="user_reviews">
        <h3>User reviews</h3>
        <article class="user_review">
          <h4>Too scary!</h4>
          <p>Way too scary for me.</p>
          <footer>
            <p>
              Posted on
              <time datetime="2015-05-16 19:00">May 16</time>
              by Lisa.
            </p>
          </footer>
        </article>
        <article class="user_review">
          <h4>Love the dinos!</h4>
          <p>I agree, dinos are my favorite.</p>
          <footer>
            <p>
              Posted on
              <time datetime="2015-05-17 19:00">May 17</time>
              by Tom.
            </p>
          </footer>
        </article>
      </section>
      <footer>
        <p>
          Posted on
          <time datetime="2015-05-15 19:00">May 15</time>
          by Staff.
        </p>
      </footer>
    </article>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article#result)

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article#technical_summary)

--------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [sectioning content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#sectioning_content)<br>, [palpable content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#palpable_content) |
| Permitted content | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. Note that an `<article>` element must not be a descendant of an [`<address>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address)<br> element. |
| Implicit ARIA role | `[article](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/article_role) ` |
| Permitted ARIA roles | [`application`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/application_role)<br>, [`document`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/document_role)<br>, [`feed`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/feed_role)<br>, [`main`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/main_role)<br>, [`none`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/none_role)<br>, [`presentation`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/presentation_role)<br>, [`region`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/region_role) |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-article-element](https://html.spec.whatwg.org/multipage/sections.html#the-article-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article#see_also)

--------------------------------------------------------------------------------------------------

*   Other section-related elements: [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
    , [`<nav>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav)
    , [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
    , [`<aside>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/aside)
    , [h1](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [h2](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [h3](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [h4](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [h5](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [h6](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    , [`<hgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hgroup)
    , [`<header>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header)
    , [`<footer>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer)
    , [`<address>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address)
    
*   [Using HTML sections and outlines](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/article/index.md?plain=1 "Folder: en-us/web/html/reference/elements/article (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Farticle&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Farticle%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Farticle%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Farticle%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F100cf25d92d3953f3c70ecaa2af637d5e42179d8%0A*+Document+last+modified%3A+2026-09-10T17%3A31%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")