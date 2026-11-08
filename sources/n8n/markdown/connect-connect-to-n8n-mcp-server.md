For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/connect-to-n8n-mcp-server.md)
.

n8n's built-in MCP server lets supported clients, such as Lovable or Claude Desktop, connect securely to your n8n instance. Once connected, these clients can:

*   Search for your workflows
    
*   Interact with workflows marked as available in MCP
    
*   Trigger and test exposed workflows
    
*   Create and edit workflows and data tables
    

In this section[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#in-this-section)

-----------------------------------------------------------------------------------------

*   [MCP client connection examples](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-client-examples)
    : exact commands and configuration for specific MCP clients.
    
*   [MCP server tools reference](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference)
    : the complete list of available tools and their parameters.
    

**Connecting a chat client such as Claude Desktop?**

1.  [Enable MCP access](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#enabling-mcp-access)
     on your instance.
    
2.  Copy the **Server URL** from **Settings > Instance-level MCP > Connect a client**. It ends in `/mcp-server/http`.
    
3.  Paste it into your client. For the exact steps per client, see [MCP client connection examples](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-client-examples)
    .
    

The rest of this page covers the settings, permissions, and troubleshooting behind those steps.

Difference between instance-level MCP access and MCP Server Trigger node[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#difference-between-instance-level-mcp-access-and-mcp-server-trigger-node)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Instance-level MCP access lets you create one connection per n8n instance, use centralized authentication, and choose which workflows to enable for access. Enabled workflows are easy to find and run without extra setup for each workflow.

In comparison, you configure an MCP Server Trigger node inside a single workflow. This node exposes tools only from that workflow, a useful approach when you want to craft a specific MCP server behavior within one workflow.

### Key considerations when using instance-level MCP access[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#key-considerations-when-using-instance-level-mcp-access)

*   MCP supports two types of workflow interactions: running existing workflows with the workflow execution tools, and building or editing workflows (available from n8n 2.13.0).
    
*   It doesn't provide blanket exposure to all workflows in your instance. You must enable MCP at the instance level and then enable each workflow individually. The only exception is `search_workflows`, which can access every workflow the current user has permission to view, but only returns previews, not full workflow data.
    
*   It's not scoped to each MCP client. All clients you connect (for example, Claude Desktop and ChatGPT) can see all workflows you've enabled for MCP access. You can't restrict specific workflows to specific clients. On a user level, visibility remains user-scoped: users can only see MCP-enabled workflows they have access to.
    
*   Most MCP tools work on unpublished workflows. The exception is `execute_workflow`, which defaults to production mode and runs the published version of a workflow. It also supports a `manual` execution mode to run the current (unpublished) version.
    

Enabling MCP access[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#enabling-mcp-access)

-------------------------------------------------------------------------------------------------

**Feature availability**

The settings layout described below (**Connection details**, **Access**, **Connected clients**), the **Connect a client** dialog, and **Allowed callback URLs** are available from n8n 2.33.0. These replace the previous single-page MCP settings screen. On older versions, this page shows a simpler layout without per-client setup steps.

### For Cloud and self-hosted instances[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#for-cloud-and-self-hosted-instances)

1.  Navigate to **Settings > Instance-level MCP**.
    
2.  Select **Enable MCP access** (requires instance owner or admin permissions).
    

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-c36e53b427edbf48c2d00f96409ad096304c750f%252Fmcp-enable-screen.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=c5821f56fe4a7f10e2e262297d536769&sv=3)

The Instance-level MCP page before you enable MCP access, showing the Enable MCP access button

Once enabled, the page groups settings into three sections:

*   **Connection details**: shows the **MCP status** and a **Connect** button that opens setup steps for your MCP client.
    
*   **Access**: shows how many workflows (and, if your instance has the agents feature, agents) are exposed to MCP clients, see [Exposing workflows to MCP clients](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#exposing-workflows-to-mcp-clients)
     and [Exposing agents to MCP clients](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#exposing-agents-to-mcp-clients)
    . Instance owners and admins also see **Allowed callback URLs** here, see [Restricting OAuth callback URLs](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#restricting-oauth-callback-urls)
    .
    
*   **Connected clients**: previews up to three of your own connected clients and their permissions, and shows how many clients currently have access. Select a client to open its details, or **Revoke access** to disconnect it. Select **View all** to [review or revoke access for individual clients](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#revoking-client-access)
    .
    

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-f75b4905a145e90d09a3c8ef3249b498d383ed51%252Fmcp-enabled-screen.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=9476565befe44c5f039a515df8f9cd95&sv=3)

The Instance-level MCP page after you enable MCP access, showing Connection details, Access, and Connected clients

**To disable:** In **Connection details**, select the **MCP status** control and choose **Disable**. n8n asks you to confirm, since disabling disconnects every connected client and revokes its access. You can turn MCP access back on later.

**Environment variables (self-hosted only)**

On self-hosted instances, you can also manage MCP settings using environment variables. See [Manage instance settings using environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-settings-using-environment-variables#mcp)
.

### For self-hosted: Complete disablement[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#for-self-hosted-complete-disablement)

To remove the feature entirely, set the environment variable:

`N8N_DISABLED_MODULES=mcp`

This action removes MCP endpoints and hides all related UI elements.

Connecting MCP clients[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#setting-up-mcp-authentication)

--------------------------------------------------------------------------------------------------------------

**Feature availability**

Per-client connection setup steps are available from n8n 2.33.0. Earlier versions don't show these steps. Use the manual instructions in [MCP client connection examples](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-client-examples)
 to configure your client instead.

In **Connection details**, select **Connect** to open the **Connect a client** dialog, then choose an authentication method: [OAuth (recommended)](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#using-oauth2)
 or [API key](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#using-access-token)
.

### Using OAuth (recommended)[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#using-oauth2)

1.  Navigate to **Settings > Instance-level MCP**.
    
2.  In **Connection details**, select **Connect** to open the **Connect a client** dialog.
    
3.  Confirm you're on the **OAuth (recommended)** tab.
    
4.  In the **Your client** dropdown, pick your AI assistant, IDE, or CLI. n8n groups clients into **CLI** (Claude Code, Codex, Gemini CLI), **Web** (Claude.ai, ChatGPT, Mistral Vibe), and **IDE** (Cursor, VS Code, Windsurf), and shows setup steps tailored to your choice.
    
5.  Follow the steps shown for your client type:
    
    *   **Web clients**: select **One-click setup** to add n8n to the client directly, or copy the **Server URL** and paste it into the client's own connector settings yourself.
        
    *   **CLI clients**: run the install command shown, or add the manual configuration snippet to the client's configuration file instead. Either way, finish with the **Authenticate** step to complete the OAuth sign-in (see the [Claude Code](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-client-examples#connecting-claude-code-to-n8n-mcp-server)
         and [Codex](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-client-examples#connecting-codex-cli-to-n8n-mcp-server)
         examples for the exact commands).
        
    *   **IDE clients**: select the one-click install link (where the editor supports one), or copy the **Server URL** and add the manual configuration snippet to the editor yourself.
        
    
6.  When the client redirects you to n8n, approve access to finish connecting it.
    

#### Reviewing and revoking client access[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#revoking-client-access)

Each connected client only has the permissions you granted it when it connected, for example reading workflows without being able to create or run them. To review or revoke a client's access:

1.  Navigate to **Settings > Instance-level MCP**.
    
2.  In **Connected clients**, select a previewed client to open its details, or **Revoke access** to disconnect it. Select **View all** for clients not previewed. Switch to the all-users view for other users' clients. This shows a table of connected OAuth clients, their access level, and when they connected. Clients using an API key don't appear here, since they authenticate with a bearer token rather than an OAuth connection.
    
3.  Select a client's row to open its details and see every permission you granted it, or select **Revoke access** directly on the row to skip straight to revoking.
    
4.  Confirm the revocation. n8n disconnects the client at once; it must reconnect and sign in again to regain access.
    

### Using API key[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#using-access-token)

1.  Navigate to **Settings > Instance-level MCP**.
    
2.  In **Connection details**, select **Connect** to open the **Connect a client** dialog.
    
3.  Switch to the **API key** tab. n8n automatically generates a personal access token tied to your user account the first time you open it.
    
4.  Copy what you need: the **Configuration JSON** block, already filled in with your server URL and an `Authorization: Bearer` header carrying your token, or the individual **Server URL** and access token values if your client doesn't use that JSON format (for example, Codex's TOML configuration). Once you leave this tab, n8n only shows a redacted token value, and you won't be able to copy it again unless you [rotate it](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#rotating-your-token)
    .
    
5.  Paste what you copied into your MCP client's configuration: drop the **Configuration JSON** straight in for clients that accept an `mcpServers` JSON snippet, or use the individual **Server URL** and token for clients that need a different format. This tab isn't client-specific, so the same values work no matter which client you're setting up (see [MCP client connection examples](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-client-examples)
     for client-specific formats).
    

#### Rotating your access token[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#rotating-your-token)

If you lose your token or need to rotate it:

1.  Navigate to **Settings > Instance-level MCP**.
    
2.  In **Connection details**, select **Connect** to open the **Connect a client** dialog.
    
3.  Switch to the **API key** tab.
    
4.  Generate a new token using the button next to the redacted value.
    
    n8n revokes the previous token when you generate a new one.
    
5.  Update all connected MCP clients with the new value.
    

Exposing workflows to MCP clients[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#exposing-workflows-to-mcp-clients)

-----------------------------------------------------------------------------------------------------------------------------

MCP clients can discover previews of all workflows the current user has access to using `search_workflows`. Clients can't access full workflow data, execute, or modify a workflow unless you explicitly enable MCP access for that workflow.

### Enabling access for individual workflows[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#enabling-access-for-individual-workflows)

#### Option 1: From the Workflows enabled page[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#option-1-from-mcp-settings-page-available-from-n8n-v220)

From the **Workflows enabled** page (available from n8n 2.2.0; renamed from **Workflows exposed** in n8n 2.42.0), you can enable access for individual workflows:

1.  Navigate to **Settings > Instance-level MCP**.
    
2.  Select **Workflows enabled**.
    
3.  Click the **Enable workflows** button (in the workflows table header or in the table's empty state).
    
4.  Search for the desired workflow (by name or description) and select it from the list.
    
5.  Click **Enable** to confirm.
    

#### Option 2: From the workflow editor[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#option-2-from-the-workflow-editor)

1.  Open the workflow.
    
2.  Click the main **Workflow menu** (`...`) in the top-right corner.
    
3.  Select **Settings**.
    
4.  Toggle **Available in MCP**.
    

#### Option 3: From the workflows list[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#option-3-from-the-workflows-list)

1.  Go to **Workflows**.
    
2.  Open the menu on a workflow card.
    
3.  Select **Enable MCP access**.
    

### Enabling access for projects/folders[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#enabling-access-for-projectsfolders)

**Feature availability**

Project and folder-level MCP access control is available from n8n 2.24.0.

You can use the **Options** menu ![Options menu](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-f19a4d097d364587b73864eaed77b12bfd8f516b%252Fthree-dot-options-menu.png%3Falt%3Dmedia&width=19&dpr=3&quality=100&sign=7087b2fc8e73a32eba840e7c4d1630a9&sv=3) in the workflow list to toggle MCP access for all workflows in the current project or folder:

1.  Navigate to the desired project and select **Workflows** from the top menu, then open a subfolder if required.
    
2.  Select the **Options** menu ![Options icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-f19a4d097d364587b73864eaed77b12bfd8f516b%252Fthree-dot-options-menu.png%3Falt%3Dmedia&width=19&dpr=3&quality=100&sign=7087b2fc8e73a32eba840e7c4d1630a9&sv=3) next to the name of the project or folder.
    
3.  Select **Manage MCP access**, then either **Enable MCP** or **Disable MCP**.
    

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-692ea5f307bd29f0c5e7dcf5c902d8027c9fc816%252Fmcp_bulk_toggle.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=2d1305e5968b02670bcf55943ba4ccdb&sv=3)

Options menu with Manage MCP access expanded, showing Enable MCP access and Disable MCP access

**Note**

This will toggle MCP access for all workflows that are **currently** in the selected project or folder (skipping ones that are already in the selected state). To expose workflows you create later without toggling each one, use [Auto-expose new workflows](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#auto-exposing-new-workflows)
.

### Auto-exposing new workflows[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#auto-exposing-new-workflows)

**Feature availability**

Auto-exposing new workflows is rolling out gradually from n8n 2.36.0. The setting may not be visible on every instance yet.

Instead of enabling MCP access for each workflow individually, you can expose every newly created workflow automatically:

1.  Navigate to **Settings > Instance-level MCP**.
    
2.  Turn on **Auto-expose new workflows**.
    

This setting is off by default. Turning it on only affects workflows created afterward. Workflows that already exist keep their current setting, so use [Enabling access for individual workflows](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#enabling-access-for-individual-workflows)
 or [Enabling access for projects/folders](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#enabling-access-for-projectsfolders)
 to expose those.

Only instance owners and admins can change this setting. It's read-only on instances that manage MCP access through environment variables.

**Note**

Turning this setting on doesn't expose anything while MCP access is disabled for the instance.

### Managing access[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#managing-access)

The **Workflows enabled** page (**Access > Workflows enabled**) lists every workflow that MCP clients can access and operate on. From this list you can:

*   Open a workflow, its home project or parent folder directly
    
*   Revoke access using the action menu (or use **Disable MCP access** from the workflow card menu)
    
*   Update workflow description using the action menu (or use the menu in the workflow editor)
    
*   Enable access for more workflows using the **Enable workflows** button (available from n8n 2.2.0)
    

### Workflow descriptions[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#workflow-descriptions)

To help MCP clients identify workflows, you can add free-text descriptions as follows:

1.  Option 1: From the **Workflows enabled** page
    
    1.  Navigate to **Settings > Instance-level MCP**.
        
    2.  Select **Workflows enabled**.
        
    3.  Use the action menu in the desired workflow's row and select the **Edit description** action.
        
    4.  Alternatively, click the description text directly to open the edit dialog.
        
    
2.  Option 2: From the workflow editor
    
    1.  Open the workflow.
        
    2.  Click the main **Workflow menu** (`...`) in the top-right corner.
        
    3.  Select **Edit description**.
        
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-d96978986e0cb3ec7b6bbe88251371ea1252aafb%252Fmcp_workflow_description.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=2dd464c399d3d3d5ea057685c0f9ad09&sv=3)
    
    Workflow's main menu open, with Edit description highlighted
    

Exposing agents to MCP clients[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#exposing-agents-to-mcp-clients)

-----------------------------------------------------------------------------------------------------------------------

**Feature availability**

Agents are a separate feature from workflows. See [Build and manage agents](https://docs.n8n.io/build/build-and-manage-agents)
 for details. MCP clients can manage agents from n8n 2.34.0. On n8n Cloud, agents are on by default for accounts on the latest stable version. On self-hosted, this section only applies if you've enabled the `agents` module.

**Preview status**

Agents are in Preview and may change in future releases. Avoid relying on them in production workflows.

If your instance has the agents feature, the **Access** section also shows **Agents exposed**. As with workflows, MCP clients can't read or manage an agent unless you explicitly enable MCP access for it.

### Enabling access for individual agents[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#enabling-access-for-individual-agents)

#### Option 1: From the MCP settings page[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#option-1-from-the-mcp-settings-page-agents)

1.  Navigate to **Settings > Instance-level MCP**.
    
2.  Select **Agents exposed**.
    
3.  Select **Enable agents**.
    
4.  Search for the desired agent by name and select it from the list.
    
5.  Select **Enable** to confirm.
    

#### Option 2: From the agent builder[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#option-2-from-the-agent-builder)

1.  Open the agent in the agent builder.
    
2.  Open its MCP settings.
    
3.  Toggle **Available in MCP**.
    

### Managing agent access[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#managing-agent-access)

The **Agents exposed** page shows every agent enabled for MCP clients to access, with its name and its project or folder location. From this list you can:

*   Open an agent or its project directly.
    
*   Remove access for a single agent from its row, or select multiple agents and remove access for all at once.
    
*   Enable access for more agents using the **Enable agents** button.
    

Restricting OAuth callback URLs[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#restricting-oauth-callback-urls)

-------------------------------------------------------------------------------------------------------------------------

Instance owners and admins can restrict which URLs an OAuth client can redirect to after it signs in. By default, n8n allows any callback URL, which is less secure.

1.  Navigate to **Settings > Instance-level MCP**.
    
2.  In **Access**, select **Allowed callback URLs**.
    
3.  Choose a mode:
    
    *   **All callback URLs**: any URL can complete an OAuth sign-in.
        
    *   **Only trusted URLs**: only the URLs you list can complete an OAuth sign-in.
        
    
4.  If you chose **Only trusted URLs**, add each URL you trust, then select **Save**.
    

Tools and resources[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#tools-and-resources)

-------------------------------------------------------------------------------------------------

Consider using coding agents (such as Claude Code or Google ADK agents) instead of chat clients as your MCP clients. Coding agents specialize in generating and validating TypeScript code, making them ideal for building workflows programmatically.

The n8n MCP server exposes tools for workflow management, workflow building, agent management, user preferences, and data tables. For a complete list of available tools and their parameters, refer to the [MCP server tools reference](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference)
.

n8n Skills for coding agents[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#n8n-skills-for-coding-agents)

-------------------------------------------------------------------------------------------------------------------

When you connect a coding agent to the n8n MCP server, the agent can build and edit workflows, but it doesn't automatically know n8n's conventions for expressions, node configuration, error handling, and other patterns. n8n Skills give the agent that knowledge so it gets workflows right the first time.

n8n Skills are a set of capability modules published in the [n8n-io/skills](https://github.com/n8n-io/skills)
 repository. They pair with the instance-level MCP server and include:

*   **13 capability skills** covering workflow best practices, including sub-workflows, expressions, loops, AI agents, error handling, credentials, data tables, and debugging.
    
*   **50+ reference documents and examples** with per-node guidance, decision trees, and copy-paste workflow snippets.
    
*   **Hooks** that load the right guidance automatically, so the agent reads the relevant skill before it makes high-impact MCP calls.
    

A 14th meta-skill, `using-n8n-skills-official`, routes the agent to the matching capability skill for each task.

### Why use skills[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#why-use-skills)

Skills load guidance at the moment the agent needs it, rather than relying on the model's general knowledge. This helps the agent:

*   Follow n8n best practices for the node or feature it's working with.
    
*   Avoid common mistakes, such as incorrect expression syntax or missing error handling.
    
*   Produce workflows that need less back-and-forth to fix.
    

The skills are plain Markdown, so you can read, fork, and modify them for your own conventions.

### Installing skills[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#installing-skills)

The [n8n-io/skills](https://github.com/n8n-io/skills)
 repository has up-to-date install instructions for Claude Code, Codex, and other coding agents. Follow the steps in the repository README to add the skills to your agent.

Examples[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#examples)

---------------------------------------------------------------------------

For exact commands and configuration to connect specific clients, including Lovable, Claude Desktop, Claude Code, Codex, Gemini CLI, Cursor, VS Code, Windsurf, and Google ADK agents, see [MCP client connection examples](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-client-examples)
.

Troubleshooting[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#troubleshooting)

-----------------------------------------------------------------------------------------

If you encounter issues connecting MCP clients to your n8n instance, consider the following:

*   Ensure that your n8n instance is publicly accessible if you are using cloud-based MCP clients.
    
*   Verify that the MCP access is enabled in n8n settings.
    
*   Check that the workflows you want to execute or modify are marked as **Available in MCP**.
    
*   Confirm that the authentication method (OAuth or API key) is configured correctly in your MCP client.
    
*   If your instance runs behind a reverse proxy, load balancer, or web application firewall, make sure it doesn't strip the MCP request headers. See [MCP request headers](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#mcp-request-headers)
    .
    
*   Review n8n server logs for any error messages related to MCP connections.
    

### Insufficient permissions when authorizing a client[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#insufficient-permissions-when-authorizing-a-client)

Your client sends you to n8n to approve access, and you land on a page reading **You do not have sufficient permissions to authorize this request**.

For the instance MCP server, this means MCP access isn't on for your instance. The message doesn't say so, but there's no other cause. While the server runs, any signed-in user can approve a client. While it's off, n8n refuses everyone.

Ask an instance owner or admin to turn it on, see [Enabling MCP access](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#enabling-mcp-access)
, then connect the client again.

### MCP request headers[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#mcp-request-headers)

**Feature availability**

n8n allows these routing headers in its CORS policy from n8n 2.36.0.

MCP clients send the following headers to the n8n MCP endpoint:

*   `MCP-Protocol-Version`
    
*   `Mcp-Method`
    
*   `Mcp-Name`
    

If you place n8n behind a reverse proxy, load balancer, or web application firewall that removes unknown headers or only forwards an allowlist, add these three headers to that allowlist. Otherwise clients may fail to connect or fall back to an older protocol version.

Related resources[](https://docs.n8n.io/connect/connect-to-n8n-mcp-server#related-resources)

---------------------------------------------------------------------------------------------

*   [Connect](https://docs.n8n.io/connect)
    
*   [n8n API](https://docs.n8n.io/connect/n8n-api)
    
*   [n8n CLI](https://docs.n8n.io/connect/n8n-cli)
    
*   [Connect to the n8n docs MCP server](https://docs.n8n.io/connect/connect-to-n8n-docs-mcp-server)
    
*   [Create nodes](https://docs.n8n.io/connect/create-nodes)
    

[Previousn8n CLI](https://docs.n8n.io/connect/n8n-cli)
[NextMCP client connection examples](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-client-examples)

Last updated 26 days ago

Was this helpful?