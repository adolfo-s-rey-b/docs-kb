For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/understand-workflows/create-and-edit-credentials.md)
.

Credentials are securely stored authentication information used to connect n8n workflows to external services such as APIs, or databases.

On n8n Cloud, supported AI models and services don't need a credential at all: select **Use Gateway credits** on the node to run it with [Gateway credits](https://docs.n8n.io/build/understand-workflows/use-gateway-credits)
 instead of your own API key.

Create a credential[](https://docs.n8n.io/build/understand-workflows/create-and-edit-credentials#create-a-credential)

----------------------------------------------------------------------------------------------------------------------

1.  Select the ![universal create resource icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-67e6f1d372835116e41a7e6ddd39acae384e5e29%252Funiversal-resource-button.png%3Falt%3Dmedia&width=39&dpr=3&quality=100&sign=04157a32047d49328e59f9a393beab01&sv=3) **Create** button in the upper-left corner of the side menu. Select credential.
    
2.  If your n8n instance supports projects, you'll also need to choose whether to create the credential inside your personal space or a specific project you have access to. If you're using the community version, you'll create the credential inside your personal space.
    
3.  Select the app or service you wish to connect to.
    

Or:

1.  Using the ![universal create resource icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-67e6f1d372835116e41a7e6ddd39acae384e5e29%252Funiversal-resource-button.png%3Falt%3Dmedia&width=39&dpr=3&quality=100&sign=04157a32047d49328e59f9a393beab01&sv=3) **Create** button in the upper-right corner from either the **Overview** page or a specific project. Select Credential.
    
2.  If you're doing this from the **Overview** page, you'll create the credential inside your personal space. If you're doing this from inside a project, you'll create the credential inside that specific project.
    
3.  Select the app or service you wish to connect to.
    

You can also create new credential in the credential drop down when editing a node on the workflow editor.

Once in the credential modal, enter the details required by your service. Refer to your service's page in the [credentials library](https://docs.n8n.io/integrations/builtin/credentials)
 for guidance.

When you save a credential, n8n tests it to confirm it works.

**Credentials naming**

n8n names new credentials "_node name_ account" by default. You can rename the credentials by clicking on the name, similarly to renaming nodes. It's good practice to give them names that identify the app or service, type, and purpose of the credential. A naming convention makes it easier to keep track of and identify your credentials.

Choose a credential type[](https://docs.n8n.io/build/understand-workflows/create-and-edit-credentials#choose-a-credential-type)

--------------------------------------------------------------------------------------------------------------------------------

When you create or edit an OAuth credential, you choose a **Credential type**:

*   **Fixed credential**: the same credential is used regardless of who runs the workflow. This is the default credential behaviour.
    
*   **End-user credential**: each user's credential is used at runtime, and can only be seen and used by that user.
    

End-user credentials let a workflow run with the credentials of the person who triggers it, and keep each user's data private to them. The choice between **Fixed credential** and **End-user credential** types appears for OAuth credentials on n8n Cloud Enterprise and self-hosted Enterprise. To learn how to set them up, see [End-user credentials](https://docs.n8n.io/administer/manage-credentials/end-user-credentials)
.

Allowed HTTP request domains[](https://docs.n8n.io/build/understand-workflows/create-and-edit-credentials#allowed-http-request-domains)

----------------------------------------------------------------------------------------------------------------------------------------

The **Allowed HTTP Request Domains** field appears on many n8n credentials for web-based APIs and services. It controls which domains the credential is permitted to be used against when the credential is selected in an **HTTP Request** node. It has no effect when the credential is used in its own dedicated node.

The field has three options:

*   **All**: The credential can be used against any URL.
    
*   **Specific Domains**: Restrict to specific domains (provide a comma-separated list like `httpbin.org, api.github.com`)
    
*   **None**: The credential is blocked entirely from use in the **HTTP Request** node.
    

This field prevents credential misuse, for example sending the credential to URLs outside the intended domain.

Expressions in credentials[](https://docs.n8n.io/build/understand-workflows/create-and-edit-credentials#expressions-in-credentials)

------------------------------------------------------------------------------------------------------------------------------------

You can use expressions to set credentials dynamically as your workflow runs:

1.  In your workflow, find the data path containing the credential. This varies depending on the exact parameter names in your data. Make sure that the data containing the credential is available in the workflow when you get to the node that needs it.
    
2.  When creating your credential, hover over the field where you want to use an expression.
    
3.  Toggle **Expression** on.
    
4.  Enter your expression.
    

### Example workflow[](https://docs.n8n.io/build/understand-workflows/create-and-edit-credentials#example-workflow)

spinner

#### Using the example[](https://docs.n8n.io/build/understand-workflows/create-and-edit-credentials#using-the-example)

To load the template into your n8n instance:

1.  Download the workflow JSON file.
    
2.  Open a new workflow in your n8n instance.
    
3.  Copy in the JSON, or select **Workflow menu** ![Workflow menu icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2738857267-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FGixZThfitWP21x2gQFpD%252Fuploads%252Fgit-blob-513566d28f893c602d89d96c0a06037329725e61%252Fthree-dots-horizontal.png%3Falt%3Dmedia&width=54&dpr=3&quality=100&sign=0d48cb7a502e001d3f9694f0a8b239bf&sv=3) > **Import from file...**.
    

The example workflows use Sticky Notes to guide you:

*   Yellow: notes and information.
    
*   Green: instructions to run the workflow.
    
*   Orange: you need to change something to make the workflow work.
    
*   Blue: draws attention to a key feature of the example.
    

Related resources[](https://docs.n8n.io/build/understand-workflows/create-and-edit-credentials#related-resources)

------------------------------------------------------------------------------------------------------------------

*   [Understand workflows](https://docs.n8n.io/build/understand-workflows)
    
*   [Create and run workflows](https://docs.n8n.io/build/understand-workflows/create-and-run-workflows)
    
*   [Save and publish workflows](https://docs.n8n.io/build/understand-workflows/save-and-publish-workflows)
    
*   [Use Gateway credits](https://docs.n8n.io/build/understand-workflows/use-gateway-credits)
    
*   [Workflow components](https://docs.n8n.io/build/understand-workflows/workflow-components)
    
*   [Understand executions](https://docs.n8n.io/build/understand-workflows/understand-executions)
    

[PreviousSave and publish workflows](https://docs.n8n.io/build/understand-workflows/save-and-publish-workflows)
[NextUse Gateway credits](https://docs.n8n.io/build/understand-workflows/use-gateway-credits)

Last updated 10 days ago

Was this helpful?