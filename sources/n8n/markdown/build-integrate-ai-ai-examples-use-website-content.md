For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/integrate-ai/ai-examples/use-website-content.md)
.

Use n8n to scrape a website, load the data into Pinecone, then query it using a chat workflow. This workflow uses the [HTTP node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to get website data, extracts the relevant content using the [HTML node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.html)
, then uses the [Pinecone Vector Store node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone)
 to send it to Pinecone.

spinner

Key features[](https://docs.n8n.io/build/integrate-ai/ai-examples/use-website-content#key-features)

----------------------------------------------------------------------------------------------------

This workflow uses:

*   [HTTP node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
    : fetches website data.
    
*   [HTML node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.html)
    : simplifies the data by extracting the main content from the page.
    
*   [Pinecone Vector Store node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone)
     and [Embeddings OpenAI](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai)
    : transform the data into vectors and store it in Pinecone.
    
*   [Chat Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger)
     and [Question and Answer Chain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa)
     to query the vector database.
    

Using the example[](https://docs.n8n.io/build/integrate-ai/ai-examples/use-website-content#using-the-example)

--------------------------------------------------------------------------------------------------------------

To load the template into your n8n instance:

1.  Download the workflow JSON file.
    
2.  Open a new workflow in your n8n instance.
    
3.  Copy in the JSON, or select **Workflow menu** ![Workflow menu icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2738857267-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FGixZThfitWP21x2gQFpD%252Fuploads%252Fgit-blob-513566d28f893c602d89d96c0a06037329725e61%252Fthree-dots-horizontal.png%3Falt%3Dmedia&width=54&dpr=3&quality=100&sign=0d48cb7a502e001d3f9694f0a8b239bf&sv=3) > **Import from file...**.
    

The example workflows use Sticky Notes to guide you:

*   Yellow: notes and information.
    
*   Green: instructions to run the workflow.
    
*   Orange: you need to change something to make the workflow work.
    
*   Blue: draws attention to a key feature of the example.
    

Related resources[](https://docs.n8n.io/build/integrate-ai/ai-examples/use-website-content#related-resources)

--------------------------------------------------------------------------------------------------------------

*   [AI examples](https://docs.n8n.io/build/integrate-ai/ai-examples)
    
*   [Use Google Sheets as a data source](https://docs.n8n.io/build/integrate-ai/ai-examples/use-google-sheets-as-a-data-source)
    
*   [Call APIs](https://docs.n8n.io/build/integrate-ai/ai-examples/call-apis)
    
*   [Human-in-the-loop for tools](https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools)
    
*   [Set a human fallback for AI workflows](https://docs.n8n.io/build/integrate-ai/ai-examples/set-a-human-fallback-for-ai-workflows)
    
*   [Use AI for parameters](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
    

[PreviousCall APIs](https://docs.n8n.io/build/integrate-ai/ai-examples/call-apis)
[NextHuman-in-the-loop for tools](https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools)

Last updated 10 days ago

Was this helpful?