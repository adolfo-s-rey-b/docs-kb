For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi.md)
.

**Feature availability**

The SerpApi (Google Search) node is deprecated from n8n 2.35.0. Use the verified **SerpApi Official** community node instead. Refer to [Deprecated and versioned nodes](https://docs.n8n.io/integrations/builtin/deprecated-nodes)
 for more information.

The SerpAPI node allows an agent in your workflow to call Google's Search API.

On this page, you'll find the node parameters for the SerpAPI node, and links to more resources.

**Credentials**

Refer to the [Serp credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/serp)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi#node-options)

------------------------------------------------------------------------------------------------------------------------------

*   **Country**: Enter the country code you'd like to use. Refer to [Google GL Parameter: Supported Google Countries](https://serpapi.com/google-countries)
     for supported countries and country codes.
    
*   **Device**: Select the device to use to get the search results.
    
*   **Explicit Array**: Choose whether to force SerpApi to fetch the Google results even if a cached version is already present (turned on) or not (turned off).
    
*   **Google Domain**: Enter the Google Domain to use. Refer to [Supported Google Domains](https://serpapi.com/google-domains)
     for supported domains.
    
*   **Language**: Enter the language code you'd like to use. Refer to [Google HL Parameter: Supported Google Languages](https://serpapi.com/google-languages)
     for supported languages and language codes.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi#templates-and-examples)

--------------------------------------------------------------------------------------------------------------------------------------------------

[Browse SerpApi (Google Search) node documentation integration templates](https://n8n.io/integrations/serpapi)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi#related-resources)

----------------------------------------------------------------------------------------------------------------------------------------

Refer to [Serp's documentation](https://serpapi.com/search-api)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousSearXNG Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolsearxng)
[NextThink Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolthink)

Last updated 10 days ago

Was this helpful?