For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop.md)
.

Use the Airtop node to automate work in Airtop, and integrate Airtop with other applications. n8n has built-in support for a wide range of Airtop features, enabling you to control a cloud-based web browser for tasks like querying, scraping, and interacting with web pages.

On this page, you'll find a list of operations the Airtop node supports, and links to more resources.

**Credentials**

Refer to [Airtop credentials](https://docs.n8n.io/integrations/builtin/credentials/airtop)
 for guidance on setting up authentication.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop#operations)

--------------------------------------------------------------------------------------------------

*   Agent
    
    *   Run an agent
        
    
*   Session
    
    *   Create session
        
    *   Save profile on termination
        
    *   Terminate session
        
    *   Wait for download
        
    
*   Window
    
    *   Create a new browser window
        
    *   Load URL
        
    *   Take screenshot
        
    *   Get live view
        
    *   List windows
        
    *   Close window
        
    
*   Extraction
    
    *   Query page
        
    *   Query page with pagination
        
    *   Smart scrape page
        
    
*   Interaction
    
    *   Click an element
        
    *   Fill form
        
    *   Hover on an element
        
    *   Scroll
        
    *   Type
        
    
*   File
    
    *   Upload a file
        
    *   Get a file
        
    *   Get many files
        
    *   Load a file
        
    *   Delete a file
        
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop#templates-and-examples)

--------------------------------------------------------------------------------------------------------------------------

[Browse Airtop node documentation integration templates](https://n8n.io/integrations/airtop)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop#related-resources)

----------------------------------------------------------------------------------------------------------------

Refer to [Airtop's documentation](https://docs.airtop.ai/api-reference/airtop-api)
 for more information about the service.

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

Contact [Airtop's Support](https://docs.airtop.ai/guides/misc/support)
 for assistance or to create a feature request.

Node reference[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop#node-reference)

----------------------------------------------------------------------------------------------------------

### Run an agent[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop#run-an-agent)

Run a published Airtop agent. In the **Agent** field, select the agent to run, then map its input parameters. To run the agent against a specific browser profile, enter its ID in the optional **Browser Profile ID** field. Leave it empty to use the agent's default profile.

### Create a session and window[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop#create-a-session-and-window)

Create an Airtop browser session to get a **Session ID**, then use it to create a new browser window. After this, you can use any extraction or interaction operation.

### Manage windows[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop#manage-windows)

Work with the browser windows in a session:

*   **Load URL**: Navigate a window to a page.
    
*   **Get live view**: Get a Live View URL to watch and control a window in real time.
    
*   **Take screenshot**: Capture an image of a window.
    
*   **List windows**: List the windows open in a session.
    
*   **Close window**: Close a specific window.
    

### Extract content[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop#extract-content)

Extract content from a web browser using these operations:

*   **Query page**: Extract information from the current window.
    
*   **Query page with pagination**: Extract information from pages with pagination or infinite scrolling.
    
*   **Smart scrape page**: Get the window content as markdown.
    

Get JSON responses by using the **JSON Output Schema** parameter in query operations.

### Interacting with pages[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop#interacting-with-pages)

Interact with a page in a session by describing the element you want to act on in natural language:

*   **Click an element**, **Hover on an element**, or **Type** text.
    
*   **Fill form**: Fill several fields at once from a plain-language description of the values.
    
*   **Scroll**: Scroll to a described element, or by a set amount toward a page edge.
    

### Work with files[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop#work-with-files)

Upload files to Airtop and use them in your browser automations:

*   **Upload a file**: Upload a file from a URL or binary data, and optionally attach it to a page's file input in a session.
    
*   **Load a file**: Attach a previously uploaded file to a page's file input in an existing session.
    
*   **Get a file** and **Get many files**: Retrieve file details, or download a ready file as binary data.
    
*   **Delete a file**: Permanently remove an uploaded file by its **File ID**.
    

### Wait for a download[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop#wait-for-a-download)

After you trigger a download in a session, use **Wait for download** to wait until the file is ready, then get its file ID and download URL.

### Terminate a session[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop#terminate-a-session)

End your session to save resources. Sessions are automatically terminated based on the **Idle Timeout** set in the **Create Session** operation or can be manually terminated using the **Terminate Session** operation.

[PreviousCommon issues](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/common-issues)
[NextQwen Cloud](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.alibabacloud)

Last updated 10 days ago

Was this helpful?