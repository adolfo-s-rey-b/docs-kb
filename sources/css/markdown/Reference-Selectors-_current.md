*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:current#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:current#mdn-search)
    

`:current` CSS pseudo-class
===========================

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:current#browser_compatibility)
 carefully before using this in production.

The **`:current`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 selector represents an element or the ancestor of an element that is currently being displayed or highlighted.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:current#syntax)

-----------------------------------------------------------------------------------------------

css

    :current {
      /* ... */
    }
    
    :current(<compound-selector-list>) {
      /* ... */
    }
    

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:current#description)

---------------------------------------------------------------------------------------------------------

The `:current` pseudo-class is used to represent the "currently displayed" element out of a series of elements.

This can mean "current" in terms of time: `:current` can be used to target the currently displayed captions or subtitles (represented using [WebVTT](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)
) that are associated with a playing video.

It can also refer to the currently highlighted element in a series. For example, `:current` can be combined with the `::search-text` [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 to provide specific styles to the currently-focused search result from the browser's "Find in page" text search feature.

For example:

css

    p::search-text {
      color: white;
      background-color: purple;
    }
    
    p::search-text:current {
      background-color: crimson;
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:current#examples)

---------------------------------------------------------------------------------------------------

### [Custom styles for text search results](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:current#custom_styles_for_text_search_results)

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
      @supports not selector(::search-text) {
        body::before {
          content: "Your browser doesn't support the ::search-text pseudo-element.";
        }
      }
      @supports not selector(:current) {
        body::before {
          content: "Your browser doesn't support the :current pseudo-class.";
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

### [Styling currently-shown WebVTT subtitles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:current#styling_currently-shown_webvtt_subtitles)

#### CSS

css

    :current(p, span) {
      background-color: yellow;
    }
    

#### HTML

html

    <video controls preload="metadata">
      <source src="video.mp4" type="video/mp4" />
      <source src="video.webm" type="video/webm" />
      <track
        label="English"
        kind="subtitles"
        srclang="en"
        src="subtitles.vtt"
        default />
    </video>
    

#### WebVTT

WEBVTT FILE

1
00:00:03.500 --> 00:00:05.000
This is the first caption

2
00:00:06.000 --> 00:00:09.000
This is the second caption

3
00:00:11.000 --> 00:00:19.000
This is the third caption

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:current#specifications)

---------------------------------------------------------------------------------------------------------------

This feature does not appear to be defined in any specification.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:current#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:current#see_also)

---------------------------------------------------------------------------------------------------

*   [Web Video Text Tracks Format (WebVTT)](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)
    
*   [`:past`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:past)
    
*   [`:future`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:future)
    
*   [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:current/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_current/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_current (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Acurrent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_current%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Acurrent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_current%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")