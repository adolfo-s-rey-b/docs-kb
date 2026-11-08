For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gitlab.md)
.

Use the GitLab node to automate work in GitLab, and integrate GitLab with other applications. n8n has built-in support for a wide range of GitLab features, including creating, updating, deleting, and editing issues, repositories, releases and users.

On this page, you'll find a list of operations the GitLab node supports and links to more resources.

**Credentials**

Refer to [GitLab credentials](https://docs.n8n.io/integrations/builtin/credentials/gitlab)
 for guidance on setting up authentication.

**This node can be used as an AI tool**

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gitlab#operations)

--------------------------------------------------------------------------------------------------

*   File
    
    *   Create
        
    *   Delete
        
    *   Edit
        
    *   Get
        
    *   List
        
    
*   Issue
    
    *   Create a new issue
        
    *   Create a new comment on an issue
        
    *   Edit an issue
        
    *   Get the data of a single issue
        
    *   Lock an issue
        
    
*   Release
    
    *   Create a new release
        
    *   Delete a new release
        
    *   Get a new release
        
    *   Get all releases
        
    *   Update a new release
        
    
*   Repository
    
    *   Get the data of a single repository
        
    *   Returns issues of a repository
        
    
*   User
    
    *   Returns the repositories of a user
        
    

Working with subgroups and nested repositories[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gitlab#working-with-subgroups-and-nested-repositories)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If your repository is located within nested GitLab groups or subgroups (for example, `https://gitlab.com/org/subgroup1/subgroup2/my-repo`), GitLab's API requires you to URL-encode the namespace path.

To configure the node for nested subgroups:

1.  **Project Owner**: Enter the full subgroup hierarchy up to the repository, replacing all forward slashes (`/`) with `%2F`. Example: `org%2Fsubgroup1%2Fsubgroup2`
    
2.  **Project Name**: Enter the project's repository slug. Example: `my-repo`
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gitlab#templates-and-examples)

--------------------------------------------------------------------------------------------------------------------------

[Browse GitLab node documentation integration templates](https://n8n.io/integrations/gitlab)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gitlab#related-resources)

----------------------------------------------------------------------------------------------------------------

Refer to [GitLab's documentation](https://docs.gitlab.com/ee/api/rest/)
 for more information about the service.

n8n provides a trigger node for GitLab. Refer to the [GitLab Trigger node documentation](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gitlabtrigger)
 for more information.

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gitlab#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

[PreviousGitHub](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.github)
[NextGmail](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail)

Last updated 10 days ago

Was this helpful?