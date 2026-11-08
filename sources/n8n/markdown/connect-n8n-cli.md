For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-cli.md)
.

**n8n CLI** is a lightweight command-line client that communicates with a running n8n instance through the [n8n API](https://docs.n8n.io/connect/n8n-api)
. It can run from any machine with network access and authenticates using an API key.

Use the API CLI to:

*   List and inspect workflows
    
*   Create a workflow from JSON
    
*   Check recent executions
    
*   Create a credential
    
*   Manage projects
    

All operations respect the permissions of the user and the scope of the API key.

n8n CLI versus server CLI[](https://docs.n8n.io/connect/n8n-cli#n8n-cli-versus-server-cli)

-------------------------------------------------------------------------------------------

If you need to manage your n8n instance (backups, license management, emergency resets), see the [Server CLI](https://docs.n8n.io/deploy/host-n8n/configure-n8n/use-the-command-line)
, a built-in tool that runs on the same machine as n8n.

Aspect

n8n CLI

Server CLI

**Runs from**

Any machine with network access

Same machine as n8n

**Authentication**

API key

Direct database access

**Requires n8n running**

Yes

No (not required for most operations)

**Best for**

Developers, integrations, AI agents

Instance operators, backups, emergencies

**Permissions**

Respects user roles and API key scopes

Bypasses access control

Install n8n-cli[](https://docs.n8n.io/connect/n8n-cli#install-n8n-cli)

-----------------------------------------------------------------------

Copy

    # Use directly with npx (zero install) <a href="#use-directly-with-npx-zero-install" id="use-directly-with-npx-zero-install"></a>
    npx @n8n/cli workflow list
    
    # Or install globally <a href="#or-install-globally" id="or-install-globally"></a>
    npm install -g @n8n/cli

Connect to your instance[](https://docs.n8n.io/connect/n8n-cli#connect-to-your-instance)

-----------------------------------------------------------------------------------------

Copy

    n8n-cli config set-url https://your-instance.n8n.cloud
    n8n-cli config set-api-key YOUR_API_KEY
    n8n-cli config show

*   The configuration is saved to `~/.n8n-cli/config.json` with restricted file permissions (`0600`).
    
*   Get your API key from **n8n > Settings > n8n API**
    

Alternatively, skip the configuration file and use environment variables:

Copy

    export N8N_URL=https://your-instance.n8n.cloud
    export N8N_API_KEY=your_api_key

Inline flags[](https://docs.n8n.io/connect/n8n-cli#inline-flags)

-----------------------------------------------------------------

Copy

    n8n-cli --url=https://my-n8n.app.n8n.cloud --api-key=n8n_api_xxxxx workflow list

### Resolution order[](https://docs.n8n.io/connect/n8n-cli#resolution-order)

1.  Command-line flags (`--url`, `--api-key`)
    
2.  Environment variables (`N8N_URL`, `N8N_API_KEY`)
    
3.  Config file (`~/.n8n-cli/config.json`)
    

Commands[](https://docs.n8n.io/connect/n8n-cli#commands)

---------------------------------------------------------

Every command supports `--help` for detailed usage.

Topic

Commands

`workflow`

`list`, `get`, `create`, `update`, `delete`, `activate`, `deactivate`, `tags`, `transfer`

`execution`

`list`, `get`, `retry`, `stop`, `delete`

`credential`

`list`, `get`, `schema`, `create`, `delete`, `transfer`

`project`

`list`, `get`, `create`, `update`, `delete`, `members`, `add-member`, `remove-member`

`tag`

`list`, `create`, `update`, `delete`

`variable`

`list`, `create`, `update`, `delete`

`data-table`

`list`, `get`, `create`, `delete`, `rows`, `add-rows`, `update-rows`, `upsert-rows`, `delete-rows`

`user`

`list`, `get`

`config`

`set-url`, `set-api-key`, `show`

`source-control`

`pull`

`package (preview)`

`export`, `import`

`skill`

`install`

`audit`

(top-level)

`login` / `logout`

(top-level)

Output formats[](https://docs.n8n.io/connect/n8n-cli#output-formats)

---------------------------------------------------------------------

All commands support three output formats via `--format`:

Format

Flag

Use when

Table

\-`-format=table` (default)

You want human-readable terminal output

JSON

`--format=json`

Piping to jq, programmatic use

ID-only

`--format=id-only`

Piping to xargs, scripting

### Examples[](https://docs.n8n.io/connect/n8n-cli#examples)

*   Human-readable table
    
    Copy
    
        n8n-cli workflow list
    
*   JSON for scripts
    
    Copy
    
        n8n-cli workflow list --format=json | jq '.[] | select(.active) | .id'
    
*   Pipe IDs into another command
    
    Copy
    
        n8n-cli workflow list --format=id-only | xargs -I{} n8n-cli workflow deactivate {}
    

Use as skill with Claude Code[](https://docs.n8n.io/connect/n8n-cli#use-as-skill-with-claude-code)

---------------------------------------------------------------------------------------------------

Install the skill so Claude always knows how to use n8n-cli:

Copy

    n8n-cli skill install --global

Then in Claude Code, type `/n8n-cli` to load it. Claude can now create, update, and manage workflows on your behalf without requiring an MCP.

Examples[](https://docs.n8n.io/connect/n8n-cli#examples-1)

-----------------------------------------------------------

### List and inspect workflows[](https://docs.n8n.io/connect/n8n-cli#list-and-inspect-workflows)

Copy

    n8n-cli workflow list
    n8n-cli workflow get <id>

### Create a workflow from JSON[](https://docs.n8n.io/connect/n8n-cli#create-a-workflow-from-json)

Copy

    cat workflow.json | n8n-cli workflow create --stdin

### Check recent executions[](https://docs.n8n.io/connect/n8n-cli#check-recent-executions)

Copy

    n8n-cli execution list --status=error --limit=10

### Create a credential[](https://docs.n8n.io/connect/n8n-cli#create-a-credential)

Copy

    n8n-cli credential schema gmailOAuth2  # see required fields first
    n8n-cli credential create --type=gmailOAuth2 --name='My Gmail' --file=cred.json

### Manage projects[](https://docs.n8n.io/connect/n8n-cli#manage-projects)

Copy

    n8n-cli project create --name="My Project"
    n8n-cli workflow transfer <id> --project=<projectId>

### Export and import packages[](https://docs.n8n.io/connect/n8n-cli#export-and-import-packages)

**Preview status**

The `package` command is in Preview and may change in future releases.

Copy

    n8n-cli package export --workflow-id=<workflow-id> --output=export.n8np
    n8n-cli package export --project-id=<project-id> --output=project.n8np
    n8n-cli package import --file=export.n8np --workflow-conflict-policy=fail
    n8n-cli package import --file=export.n8np --project-id=<project-id> --workflow-conflict-policy=skip
    n8n-cli package import --file=export.n8np --project-id=<project-id> --data-table-schema-conflict-policy=overwrite-non-destructive

See [n8n packages](https://docs.n8n.io/build/manage-workflows/n8n-packages)
 for what makes up a package, and [Import a package](https://docs.n8n.io/build/manage-workflows/n8n-packages/import-a-package)
 for every available flag.

Related resources[](https://docs.n8n.io/connect/n8n-cli#related-resources)

---------------------------------------------------------------------------

*   [Connect](https://docs.n8n.io/connect)
    
*   [n8n API](https://docs.n8n.io/connect/n8n-api)
    
*   [Connect to n8n MCP server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server)
    
*   [Connect to the n8n docs MCP server](https://docs.n8n.io/connect/connect-to-n8n-docs-mcp-server)
    
*   [Create nodes](https://docs.n8n.io/connect/create-nodes)
    

[PreviousModels](https://docs.n8n.io/connect/n8n-api/models)
[NextConnect to n8n MCP server](https://docs.n8n.io/connect/connect-to-n8n-mcp-server)

Last updated 10 days ago

Was this helpful?