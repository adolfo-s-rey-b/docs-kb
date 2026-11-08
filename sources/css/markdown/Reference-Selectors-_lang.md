*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang#mdn-search)
    

`:lang()` CSS pseudo-class
==========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:lang()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 matches elements based on the language they are determined to be in.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang#try_it)

--------------------------------------------------------------------------------------------

    *:lang(en-US) {
      outline: 2px solid deeppink;
    }
    

    <p lang="en-US">
      Music during road trips and long commutes aren't a problem, but using
      headphones isn't the best thing to do while driving in your car.
    </p>
    
    <p lang="pl-PL">
      Gdy widzimy znak z narysowaną czaszką i napisem
      <strong lang="en-US">DANGER</strong> to lepiej nie wchodzić do środka.
    </p>
    

**Note:** In HTML, the language is determined by a combination of the [`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang)
 attribute, the [`<meta>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta)
 element, and possibly by information from the protocol (such as HTTP headers). For other document types there may be other document methods for determining the language.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang#syntax)

--------------------------------------------------------------------------------------------

:lang(<language-code> \[,<language-code> \]\*) {
  /\* ... \*/
}

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang#parameters)

[`<language-code>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang#language-code)

A comma-separated list of one or more [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
s that target elements based on the [BCP 47 language tags](https://developer.mozilla.org/en-US/docs/Glossary/BCP_47_language_tag)
 set in their [`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang)
 attributes. Matching by language range is case-insensitive.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang#description)

------------------------------------------------------------------------------------------------------

When selecting languages, there is implicit wildcard matching, so `:lang(de-DE)` will match `de-DE`, `de-DE-1996`, `de-Latn-DE`, `de-Latf-DE`, and `de-Latn-DE-1996`. Explicitly using wildcards must include a full match of a language subtag, so `:lang("*-F*")` is invalid but `:lang("*-Fr")` is valid.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang#examples)

------------------------------------------------------------------------------------------------

### [Matching children of a given language](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang#matching_children_of_a_given_language)

In this example, the `:lang()` pseudo-class is used to match the parents of quote elements ([`<q>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/q)
) using [child combinators](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Child_combinator)
. Note that this doesn't illustrate the only way to do this, and that the best method to use depends on the type of document. Also note that [Unicode](https://developer.mozilla.org/en-US/docs/Glossary/Unicode)
 values are used to specify some of the special quote characters.

#### HTML

html

    <div lang="en">
      <q>This English quote has a <q>nested</q> quote inside.</q>
    </div>
    <div lang="fr">
      <q>This French quote has a <q>nested</q> quote inside.</q>
    </div>
    <div lang="de">
      <q>This German quote has a <q>nested</q> quote inside.</q>
    </div>
    

#### CSS

css

    :lang(en) > q {
      quotes: "\201C" "\201D" "\2018" "\2019";
    }
    :lang(fr) > q {
      quotes: "« " " »";
    }
    :lang(de) > q {
      quotes: "»" "«" "\2039" "\203A";
    }
    

#### Result

### [Matching multiple languages](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang#matching_multiple_languages)

The following example shows how to match multiple languages by providing a comma-separated list of language codes. It's also possible to use a wildcard to match languages in a given language range.

    p {
      margin: 0;
    }
    

#### CSS

css

    /* Matches nl and de */
    :lang("nl", "de") {
      color: green;
    }
    
    /* Omitting quotes & case-insensitive matching */
    :lang(EN, FR) {
      color: blue;
    }
    
    /* Wildcard matching a language range */
    :lang("*-Latn") {
      color: red;
    }
    

#### HTML

html

    <p lang="nl">Dit is een Nederlandse paragraaf.</p>
    <p lang="de">Dies ist ein deutscher Satz.</p>
    <p lang="en">This is an English sentence.</p>
    <p lang="en-GB">Matching the language range of English.</p>
    <p lang="fr">Ceci est un paragraphe français.</p>
    <p lang="fr-Latn-FR">Ceci est un paragraphe français en latin.</p>
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# lang-pseudo](https://drafts.csswg.org/selectors/#lang-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang#see_also)

------------------------------------------------------------------------------------------------

*   The [`:dir`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:dir)
     pseudo-class that matches by directionality of text
*   HTML [`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang)
     attribute
*   HTML [`translate`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/translate)
     attribute
*   [BCP 47 language tag](https://developer.mozilla.org/en-US/docs/Glossary/BCP_47_language_tag)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_lang/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_lang (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Alang&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_lang%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Alang%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_lang%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")