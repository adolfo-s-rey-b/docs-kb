*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text/Wrapping_breaking_text#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text/Wrapping_breaking_text#mdn-search)
    

Wrapping and breaking text
==========================

This guide explains the various ways in which overflowing text can be managed in CSS.

[What is overflowing text?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text/Wrapping_breaking_text#what_is_overflowing_text)

------------------------------------------------------------------------------------------------------------------------------------------

In CSS, if you have an unbreakable string such as a very long word, by default it will overflow any container that is too small for it in the inline direction. We can see this happening in the example below: the long word is extending past the boundary of the box it is contained in.

CSS will display overflow in this way, because doing something else could cause data loss. In CSS data loss means that some of your content vanishes. So the initial value of [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
 is `visible`, and we can see the overflowing text. It is generally better to be able to see overflow, even if it is messy. If things were to disappear or be cropped as would happen if `overflow` was set to `hidden` you might not spot it when previewing your site. Messy overflow is at least noticeable, and in the worst case, your visitor will be able to see and read the content even if it looks a bit strange.

In this next example, you can see what happens if `overflow` is set to `hidden`.

html

    <div class="box">
      Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch
    </div>
    

css

    .box {
      border: 4px solid #f76707;
      border-radius: 5px;
      padding: 10px;
      inline-size: 150px;
      overflow: hidden;
    }
    

[Finding the min-content size](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text/Wrapping_breaking_text#finding_the_min-content_size)

-------------------------------------------------------------------------------------------------------------------------------------------------

To find the minimum size of the box that will contain its contents with no overflows, set the [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 or [`inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inline-size)
 property of the box to [`min-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content)
.

html

    <div class="box">
      Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch
    </div>
    

css

    .box {
      border: 4px solid #f76707;
      border-radius: 5px;
      padding: 10px;
      inline-size: min-content;
    }
    

Using `min-content` is therefore one possibility for overflowing boxes. If it is possible to allow the box to grow to be the minimum size required for the content, but no bigger, using this keyword will give you that size.

[Breaking long words](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text/Wrapping_breaking_text#breaking_long_words)

-------------------------------------------------------------------------------------------------------------------------------

If the box needs to be a fixed size, or you are keen to ensure that long words can't overflow, then the [`overflow-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap)
 property can help. This property will break a word once it is too long to fit on a line by itself.

html

    <div class="box">
      Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch
    </div>
    

css

    .box {
      border: 4px solid #f76707;
      border-radius: 5px;
      padding: 10px;
      inline-size: 150px;
      overflow-wrap: break-word;
    }
    

**Note:** The `overflow-wrap` property acts in the same way as the non-standard property `word-wrap`. The `word-wrap` property is now treated by browsers as an alias of the standard property.

An alternative property to try is [`word-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break)
. This property will break the word at the point it overflows. It will cause a break-even if placing the word onto a new line would allow it to display without breaking.

In this next example, you can compare the difference between the two properties on the same string of text.

html

    <div class="box box1">A Very LongWordThatHasNoBreakingPossibilities</div>
    
    <div class="box box2">A Very LongWordThatHasNoBreakingPossibilities</div>
    

css

    .box {
      border: 4px solid #f76707;
      border-radius: 5px;
      padding: 10px;
      inline-size: 30ch;
      margin-block-end: 1em;
    }
    .box1 {
      word-break: break-all;
    }
    
    .box2 {
      overflow-wrap: break-word;
    }
    

This might be useful if you want to prevent a large gap from appearing if there is just enough space for the string. Or, where there is another element that you would not want the break to happen immediately after.

In the example below there is a checkbox and label. Let's say, you want the label to break should it be too long for the box. However, you don't want it to break directly after the checkbox.

html

    <div class="field">
      <input id="one" type="checkbox" /><label for="one">
        LongWordThatHasNoBreakingPossibilities
      </label>
    </div>
    
    <div class="field field-br">
      <input id="two" type="checkbox" /><label for="two">
        LongWordThatHasNoBreakingPossibilities
      </label>
    </div>
    

css

    .field {
      inline-size: 150px;
      border: 1px solid #cccccc;
      margin-block-end: 1em;
      padding: 10px;
    }
    
    .field-br {
      word-break: break-all;
    }
    

[Adding hyphens](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text/Wrapping_breaking_text#adding_hyphens)

---------------------------------------------------------------------------------------------------------------------

To add hyphens when words are broken, use the CSS [`hyphens`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens)
 property. Using a value of `auto`, the browser is free to automatically break words at appropriate hyphenation points, following whatever rules it chooses. To have some control over the process, use a value of `manual`, then insert a hard (U+2010) or soft break character (U+00AD) into the string. A hard break character can be added using `‐` or `&#x2010;`, and a soft break character can be added using the `&shy;`, `&#173;`, or `&#xad;` HTML character codes. A hard break will always break, even if it is not necessary to do so. A soft break only breaks if breaking is needed.

html

    <div class="box">
      Llanfair&shy;pwllgwyngyll&shy;gogerychwyrndrobwllllantysiliogogogoch
    </div>
    

css

    .box {
      inline-size: 150px;
      overflow-wrap: break-word;
      hyphens: manual;
      border: 4px solid #f76707;
      border-radius: 5px;
      padding: 10px;
    }
    

You can also use the [`hyphenate-character`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-character)
 property to use the string of your choice instead of the default hyphenation character at the end of the line (before the hyphenation line break) for the language. The `auto` value selects the correct value to mark a mid-word line break according to the typographic conventions of the current content language.

CSS provides additional hyphenation control: the [`hyphenate-limit-chars`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-limit-chars)
 property can be used to set the minimum word length that allows for hyphenation as well as the minimum number of characters before and after the hyphen.

[The `<wbr>` element](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text/Wrapping_breaking_text#the_wbr_element)

---------------------------------------------------------------------------------------------------------------------------

If you know where you want a long string to be allowed to break, you can also use the HTML [`<wbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr)
 element. The `<wbr>` element introduces a line break opportunity—if the word overflows, it will wrap at this position. This allows you to preserve meaningful segments in the string, such as long URLs.

In the example below, the browser may break the text at the location of the [`<wbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr)
.

html

    <div class="box">
      Llanfair<wbr />pwllgwyngyll<wbr />gogerychwyrndrobwllllantysiliogogogoch
    </div>
    

css

    .box {
      border: 4px solid #f76707;
      border-radius: 5px;
      padding: 10px;
      inline-size: 150px;
    }
    

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text/Wrapping_breaking_text#see_also)

---------------------------------------------------------------------------------------------------------

*   The HTML [`<wbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr)
     element
*   The CSS [`word-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break)
     property
*   The CSS [`overflow-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap)
     property
*   The CSS [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
     property
*   The CSS [`text-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap)
     property
*   The CSS [`hyphens`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens)
     property
*   The CSS [`hyphenate-character`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-character)
     property
*   The CSS [`hyphenate-limit-chars`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-limit-chars)
     property
*   [Overflow and Data Loss in CSS](https://www.smashingmagazine.com/2019/09/overflow-data-loss-css/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text/Wrapping_breaking_text/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/text/wrapping_breaking_text/index.md?plain=1 "Folder: en-us/web/css/guides/text/wrapping_breaking_text (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FText%2FWrapping_breaking_text&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Ftext%2Fwrapping_breaking_text%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FText%2FWrapping_breaking_text%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Ftext%2Fwrapping_breaking_text%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd4569d185ccab9b722eb849c033ef69f8f44d107%0A*+Document+last+modified%3A+2026-08-12T16%3A46%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")