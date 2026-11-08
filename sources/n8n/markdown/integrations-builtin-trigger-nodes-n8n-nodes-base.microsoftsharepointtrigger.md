For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftsharepointtrigger.md)
.

Use the Microsoft SharePoint Trigger node to start a workflow when a file or a list item changes in [Microsoft SharePoint](https://www.microsoft.com/en-us/microsoft-365/sharepoint/collaboration)
.

The node watches one document library or one list on one site. It checks for changes on a schedule you set. Each check starts the workflow at most once. If more than one item changed since the last check, they arrive together in that execution, one item for each entry the check read. If nothing changed, the node starts no execution.

On this page, you'll find what the node watches, the events it produces, and the common issues to know about before you build on it.

**Credentials**

The node supports the [Microsoft OAuth2 credential](https://docs.n8n.io/integrations/builtin/credentials/microsoft)
 and the [Microsoft Entra Service Principal credential](https://docs.n8n.io/integrations/builtin/credentials/microsoftentraserviceprincipal)
. It doesn't support the Microsoft SharePoint credential.

For the OAuth2 credential, enter `openid offline_access Sites.Read.All` in the **Scope** field. For the Service Principal credential, grant the app registration the `Sites.Read.All` [application permission](https://docs.n8n.io/integrations/builtin/credentials/microsoftentraserviceprincipal#required-application-permissions-by-node)
. If your organization grants access site by site, use `Sites.Selected` instead, and an administrator must [grant the app access to each site](https://docs.n8n.io/integrations/builtin/credentials/microsoftentraserviceprincipal#grant-access-per-site)
.

Triggers keep checking when nobody is signed in, so use the Service Principal credential in production. A user credential stops working when that user's session is revoked.

**Government cloud support**

If you're using a government cloud tenant (US Government, US Government DOD, or China), select the appropriate **Microsoft Graph API Base URL** in your Microsoft credentials configuration.

What the node watches[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftsharepointtrigger#what-the-node-watches)

------------------------------------------------------------------------------------------------------------------------------------------------

Choose a **Site**, then set **Resource** to what you want to watch on it:

*   **Document Library**: watches the files in one library. Choose the library in **Document Library**.
    
*   **List**: watches the items in one list. Choose the list in **List**.
    

Each field offers a picker and a typed value. Use the picker unless it can't reach what you need, for example when your organization grants access site by site. The **Site** field also accepts a site address in **By URL** mode.

The node watches the whole library or the whole list. You can't narrow it to one folder. Microsoft Graph's change feed can't be filtered on the server, and it doesn't report the folder path of a changed file, so there's nothing reliable to filter on.

Events[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftsharepointtrigger#events)

------------------------------------------------------------------------------------------------------------------

Select the events in **Events**. Both are on by default.

*   **Changed**: a file or item was added, edited, renamed, or moved, or its metadata changed.
    
*   **Deleted**: a file or item was deleted.
    

Folders produce no events, on either resource.

### Why there's no separate Created event[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftsharepointtrigger#why-theres-no-separate-created-event)

Microsoft Graph's change feed reports the latest state of each item, not each change. An item that was created and an item that was edited arrive looking the same, so the node reports both as **Changed** rather than guessing.

If you need to tell new items from edited ones, compare `createdDateTime` with `lastModifiedDateTime` in your workflow, and treat the result as a hint rather than a fact. An item created and then edited between two checks arrives once, with the two timestamps different.

How often the node checks[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftsharepointtrigger#how-often-the-node-checks)

--------------------------------------------------------------------------------------------------------------------------------------------------------

**Poll Times** sets how often the node checks for changes. It defaults to every minute.

The preset choices go down to once a minute. A **Custom** cron expression can go finer, down to seconds, but Microsoft throttles requests well before that frequency is useful.

A change is picked up on the next check. One check reads about 40 pages of changes at default settings, and stops early if it runs out of time. If more changes are waiting, the node saves its position and carries on at the next check. A large burst of changes therefore arrives over multiple executions, and can take longer to clear than one interval.

Output[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftsharepointtrigger#output)

------------------------------------------------------------------------------------------------------------------

The node outputs each changed entry exactly as Microsoft Graph returns it, with no reshaping. The fields depend on which resource you're watching and on what happened to the item.

An entry with a `deleted` property is a deletion. An entry without one is a change.

When watching a list, an entry carries the item's identity. The node reads Microsoft Graph's default payload and doesn't expand the item's `fields`, so don't rely on an entry carrying column values. To read a column, add a Microsoft SharePoint node after the trigger and get the item by `id`.

A deletion entry carries much less than a change entry, because Microsoft Graph drops most fields from it. Expect the item's `id` and the `deleted` property, and don't rely on anything else being present. If your workflow needs a deleted item's name, keep your own record of the items you've seen, keyed by `id`.

When watching a document library, don't rely on the entry carrying `parentReference.path`. Use `webUrl` to find where the file is.

Common issues[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftsharepointtrigger#common-issues)

--------------------------------------------------------------------------------------------------------------------------------

### Existing files and items don't trigger the workflow[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftsharepointtrigger#existing-files-and-items-dont-trigger-the-workflow)

When you publish the workflow, the node starts watching from that moment. Files and items that already exist raise no event. To process a library's existing contents, use the [Microsoft SharePoint node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftsharepoint)
 instead.

### Changes are missing after I edited the node[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftsharepointtrigger#changes-are-missing-after-i-edited-the-node)

Changing the **Authentication** method, **Site**, **Resource**, **Document Library**, or **List** resets the saved position. The node starts watching from that moment and doesn't report earlier changes. Choosing a different credential of the same type keeps the position.

### Changes are missing after the workflow was inactive[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftsharepointtrigger#changes-are-missing-after-the-workflow-was-inactive)

If the node doesn't run for a long time, its saved position can expire on Microsoft's side. The node then starts watching from that moment and logs a warning. Changes made while the position was expired aren't reported.

### The same item arrives more than once[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftsharepointtrigger#the-same-item-arrives-more-than-once)

Within one check, the node combines repeated changes to the same item. Across checks, the same item can arrive more than once while a large burst of changes is processed. Design your workflow so repeats for the same item are harmless.

### The test shows items, but not my change[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftsharepointtrigger#the-test-shows-items-but-not-my-change)

Testing the node in the editor doesn't move the saved position, so a test never consumes real events. A test lists items that already exist in the library or list, up to one page of them. It doesn't wait for a change, and it never shows a deletion. Use it to see the shape of an entry, not to check your event selection.

### The node reports that the library or list can't be found[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftsharepointtrigger#the-node-reports-that-the-library-or-list-cant-be-found)

If the watched library or list can no longer be reached, for example after someone deleted it, the node reports an error that names the library or list and the site it looked on. It keeps its saved position, so it resumes if the target comes back. A rename doesn't break the node, because it watches by ID. If you entered a list title in **By ID or Title** mode, a rename does break it.

### A permission error doesn't name the library or list[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftsharepointtrigger#a-permission-error-doesnt-name-the-library-or-list)

If the credential loses access, Microsoft Graph usually answers with a permission error. The node reports that error as it came back, so it doesn't name the library or list. Check the credential's scopes and the signed-in account's access to the site.

### The same error doesn't appear on every check[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftsharepointtrigger#the-same-error-doesnt-appear-on-every-check)

When a check fails, the node reports the failure. While the same failure repeats, it reports it again at most once an hour and writes a warning to the log in between, so a lasting problem doesn't fill your execution list. A different failure reports at once, and a successful check clears the record. A test in the editor always reports the failure.

Related resources[](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftsharepointtrigger#related-resources)

----------------------------------------------------------------------------------------------------------------------------------------

n8n provides an app node for Microsoft SharePoint. Refer to the [Microsoft SharePoint node documentation](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftsharepoint)
 for more information.

Refer to [Microsoft's driveItem delta documentation](https://learn.microsoft.com/en-us/graph/api/driveitem-delta)
 and [listItem delta documentation](https://learn.microsoft.com/en-us/graph/api/listitem-delta)
 for details about the change feeds this node reads.

[PreviousMicrosoft Outlook Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftoutlooktrigger)
[NextMicrosoft Teams Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftteamstrigger)

Last updated 26 days ago

Was this helpful?