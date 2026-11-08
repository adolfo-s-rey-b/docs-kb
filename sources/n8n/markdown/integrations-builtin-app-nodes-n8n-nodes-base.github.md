For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.github.md)
.

Use the GitHub node to automate work in GitHub, and integrate GitHub with other applications. n8n has built-in support for a wide range of GitHub features, including creating, updating, deleting, and editing files, repositories, issues, pull requests, releases, and users.

On this page, you'll find a list of operations the GitHub node supports and links to more resources.

**Credentials**

Refer to [GitHub credentials](https://docs.n8n.io/integrations/builtin/credentials/github)
 for guidance on setting up authentication.

**This node can be used as an AI tool**

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.github#operations)

--------------------------------------------------------------------------------------------------

*   File
    
    *   Create
        
    *   Delete
        
    *   Edit
        
    *   Get
        
    *   List
        
    
*   Issue
    
    *   Create
        
    *   Create Comment
        
    *   Edit
        
    *   Get
        
    *   Lock
        
    
*   Organization
    
    *   Get Repositories
        
    
*   Pull Request
    
    *   Close
        
    *   Create
        
    *   Create Comment
        
    *   Edit Comment
        
    *   Get
        
    *   Get Diff
        
    *   Get Patch
        
    *   Merge
        
    *   Reopen
        
    *   Update
        
    
*   Release
    
    *   Create
        
    *   Delete
        
    *   Get
        
    *   Get Many
        
    *   Update
        
    
*   Repository
    
    *   Get
        
    *   Get Issues
        
    *   Get License
        
    *   Get Profile
        
    *   Get Pull Requests
        
    *   List Popular Paths
        
    *   List Referrers
        
    
*   Review
    
    *   Create
        
    *   Get
        
    *   Get Many
        
    *   Update
        
    
*   User
    
    *   Get Repositories
        
    *   Invite
        
    
*   Workflow
    
    *   Disable
        
    *   Dispatch
        
    *   Enable
        
    *   Get
        
    *   Get Usage
        
    *   List
        
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.github#templates-and-examples)

--------------------------------------------------------------------------------------------------------------------------

[Browse GitHub node documentation integration templates](https://n8n.io/integrations/github)
 or [search all templates](https://n8n.io/workflows/)

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.github#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

[PreviousGhost](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.ghost)
[NextGitLab](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gitlab)

Last updated 10 days ago

Was this helpful?