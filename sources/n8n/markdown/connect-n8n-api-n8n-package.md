For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/n8n-package.md)
.

Copy

On this page

Beta — breaking changes may still occur without major version bump.

### Beta: Import an n8n package into a project[](https://docs.n8n.io/connect/n8n-api/n8n-package#post-n8n-packages-import)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/n8n-packages/import

**Beta** — breaking changes may still occur without major version bump.

Imports a gzip-compressed tar package (`.n8np`) into the target project. Send the archive as the multipart field `package`. Optional routing uses form fields `projectId` and `folderId` (omit or send empty for defaults). Every optional mode/policy field (credential, workflow, project, folder, data table, variable, and tag) takes its default when omitted; the one non-fixed default is `folderConflictPolicy`, which follows `projectConflictPolicy` on a project package. The required `workflowConflictPolicy` field controls what happens when a package workflow matches an existing workflow by source id in the target project. Maximum upload size is `N8N_ENDPOINTS_PAYLOAD_SIZE_MAX` MB (default 16).

The package must declare its manifest at `manifest.json` and include every file the manifest references.

Credential references are resolved before any workflow is written.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

multipart/form-data

packagestring · binaryRequired

Gzip-compressed tar package (`.n8np`).

projectIdstringOptional

Target project id. Omit or send empty to import into the caller's personal project.

folderIdstringOptional

Optional folder within the target project. Omit or send empty for project root.

credentialMatchingModestring · enumOptional

How credential references in `requirements.credentials` are matched on the target instance. `id-only` (default) matches by id. `name-and-type` matches credentials with the exact same name and type. `type-only` matches any credential of the same type. For `name-and-type` and `type-only`, candidates are ranked by scope — a credential owned by the target project wins over one merely shared into it, which in turn wins over a global credential; if several candidates remain in the winning scope, the most recently updated one is chosen.

Default: `id-only`Possible values: `id-only``name-and-type``type-only`

credentialMissingModestring · enumOptional

What to do when a credential reference cannot be resolved. `create-stub` (default) creates empty credential placeholders in the target project for missing references. `create-with-values` also creates them, seeded from the expression data bundled in the package (see the export option `credentialExportPolicy`); a reference the package carries no data for falls back to an empty stub. A credential created with package data is listed under `credentials.seeded` when the package confirms that all source data was retained. Otherwise, also when the package has no completeness flag, it is listed under `credentials.incomplete` and blocks workflow publishing with `incomplete-credential`. `create-with-values` requires the `credential:create` scope when the import creates a credential. `must-preexist` requires every referenced credential to already exist.

Default: `create-stub`Possible values: `must-preexist``create-stub``create-with-values`

bindingsstringOptional

Optional JSON object of explicit source→target id bindings, keyed by entity type. Only `credentials` is supported today: send `{"credentials":{"<packageCredentialId>":"<targetCredentialId>"}}` to map credential ids from the package to credential ids on the target instance. These explicit bindings are validated on type and applied before `credentialMatchingMode` resolution runs.

Default: `{}`

workflowConflictPolicystring · enumRequired

`new-version` updates matching workflows and creates a new version; the archived state follows the package, so a matching workflow is archived or unarchived to match it. `fail` rejects the import when any matching workflow exists, and `skip` leaves matching workflows unchanged. Archived workflows in the target project match like any other. An archive state change also needs the `workflow:delete` scope.

Possible values: `new-version``fail``skip`

workflowPublishingPolicystring · enumOptional

Controls whether imported workflows are published after content is written. `preserve-published-state` (default) keeps new workflows inactive, and republishes an updated workflow only when it was already published and the package carries the version the source publishes — so drafts are never published. `match-source` publishes the version the package carries when the source publishes it, and unpublishes when the source publishes nothing; when the source publishes a version the package does not carry, the target keeps its published version. `publish-all` publishes every imported workflow. `unpublish-all` leaves new workflows inactive and unpublishes updated workflows that were published.

Default: `preserve-published-state`Possible values: `preserve-published-state``match-source``publish-all``unpublish-all`

workflowIdPolicystring · enumOptional

Controls the id each newly created workflow receives. `source` (default) reuses the package's own workflow id on the target instance, which best fits promotion use cases where the same workflow moves between environments. `new` mints a fresh id and records the package id as `sourceWorkflowId`, so the same package can be imported repeatedly without id collisions — best suited to marketplace imports. Workflows matched to an existing workflow in the target project (status `updated` or `skipped`) always keep that workflow's current id, regardless of policy.

Default: `source`Possible values: `new``source`

missingNodeTypeModestring · enumOptional

What to do when a workflow in the package uses a node type — or a version of a node type — this instance does not have. `fail` (default) rejects the import before anything is written, listing every missing `(nodeType, typeVersion)` pair and the workflows that use it. `import-anyway` imports the package; workflows containing missing node types are never published by this import, regardless of `workflowPublishingPolicy`.

Default: `fail`Possible values: `fail``import-anyway`

projectConflictPolicystring · enumOptional

What to do when a project the package defines already exists here (matched by id), and — unless `folderConflictPolicy` overrides it — how its contents are treated. `merge` (default) leaves the existing project's name, description, icon and custom span attributes untouched and adds the package's contents alongside. `overwrite` replaces those details with the package's; a detail the package omits is left as it is, not cleared. `fail` rejects the import before anything is written, with one `project-conflict` issue per existing project. A package project id belonging to a personal project, or to a team project the caller cannot update, always rejects the import. Ignored for workflow packages.

Default: `merge`Possible values: `merge``fail``overwrite`

folderConflictPolicystring · enumOptional

What to do when a package folder already exists at the same position in the target project. Defaults to whatever `projectConflictPolicy` is, so the intent is stated once; a workflow package defines no projects, so it defaults to `merge` there. `merge` reuses the existing folder and merges the package's children into it. `fail` rejects the import. `overwrite` reuses folders as `merge` does and additionally removes workflows the package does not contain — at a project's root and in folders the package defines, leaving target-only folders and their contents alone. Folders it does not define are then removed too, but only once nothing is left inside them. Removals are listed under `removedWorkflows` and `removedFolders`; see `overwriteDeletionPolicy`. A folder whose id sits under a different parent, or belongs to another project, always blocks the import. `overwrite` is project-packages-only, needs the `workflow:delete` and `folder:delete` scopes, is rejected against a `projectConflictPolicy` other than `overwrite`, and blocks up front if the caller cannot delete something it would remove. Folders need the `folder:create` scope and a folders-enabled licence.

Possible values: `merge``fail``overwrite`

overwriteDeletionPolicystring · enumOptional

How `folderConflictPolicy=overwrite` removes a workflow the package does not contain. `archive` (default) archives it, so it stays recoverable along with its execution history. `hard-delete` archives it — the step that unpublishes it, which a delete will not do on its own — and then deletes the workflow and its executions permanently. Each entry in `removedWorkflows` reports what actually happened in its `deletion` field: a `hard-delete` whose row cannot be dropped yet, because unpublishing defers trigger teardown, is left `archived` rather than failing an import whose content is already written. Ignored unless `folderConflictPolicy` is `overwrite`.

Default: `archive`Possible values: `archive``hard-delete`

dataTableMatchingModestring · enumOptional

How data tables referenced by the package's workflows are matched against the target project. `by-id` matches the target-project table with the same id (imported tables keep their source id) and never falls back to name matching, so a match survives a rename on the target. Currently the only mode.

Default: `by-id`Possible values: `by-id`

dataTableMissingModestring · enumOptional

Controls what happens when a referenced data table has no match in the target project. `create` (default) creates it from the package schema, keeping the source id, with no rows; requires the `dataTable:create` scope. `must-preexist` rejects the import. `do-nothing` skips creation of missing tables. Under the `keep-existing`, `fail`, and `overwrite-non-destructive` schema conflict policies, matched tables are still validated for schema compatibility and can still block the import. The import never imports table rows. Matched tables change only under `dataTableSchemaConflictPolicy=overwrite` or `overwrite-non-destructive`, which keep their rows.

Default: `create`Possible values: `create``must-preexist``do-nothing`

dataTableSchemaConflictPolicystring · enumOptional

How strictly a matched data table's schema is compared. `keep-existing` (default) accepts a target table that has every package column with the same name and type. The target table can have extra columns. `fail` rejects any difference, including target-only columns. Under `keep-existing` and `fail`, a missing package column or a type mismatch rejects the import, and the target table does not change.

`overwrite` changes the matched target table to match the package. It can remove or retype columns. The values in those columns are removed. Rows and other columns are kept. When the package has column ids, a column that is only renamed keeps its values. The changes apply to all workflows that use the table. A blocked `keep-existing`, `fail`, or `overwrite-non-destructive` import lists them in `overwriteChanges`. Requires the `dataTable:update` scope only when a matched table changes.

`overwrite-non-destructive` makes the same changes as `overwrite`, but rejects the import and writes nothing when a change removes or retypes a column. A target-only column counts as removed.

Default: `keep-existing`Possible values: `keep-existing``fail``overwrite``overwrite-non-destructive`

variableMissingModestring · enumOptional

Controls what happens when a variable referenced by the package's workflows is absent from the target project and the global scope (lookup order: project, then global). `create-with-value` (default) creates the variable with its package value and lists its name under `variables.created`. When the package carries no value for it — values were excluded at export, or the exported value was itself empty — it creates an empty stub listed under `variables.stubbed`. `do-nothing` imports without creating the variable and lists its name under `variables.missing`. `must-preexist` rejects the import unless every referenced variable already resolves. `create-stub` creates each missing variable with an empty value at the placement scope (see `variableParentPolicy`) and lists the created names under `variables.stubbed`. An import that actually creates a variable requires a license that permits variables and, for API key callers, the `variable:create` scope; a package whose variables all already resolve creates nothing and needs neither.

Default: `create-with-value`Possible values: `do-nothing``must-preexist``create-stub``create-with-value`

variableConflictPolicystring · enumOptional

What to do when a referenced variable resolves in the target project or global scope but the package bundles a _different_ value for it. `keep-existing` (default) leaves the target value untouched and reports the name under `variables.matched`. `overwrite` silently replaces the value of the existing variable at whichever scope it was found — the target project or the global scope, so a global variable other projects also read can be rewritten by this import — and reports the name under `variables.updated`; it needs a license that permits variables, the `variable:update` / `projectVariable:update` permission on that scope, and, for API key callers, the `variable:update` scope. `fail` rejects the import with a 409 instead. Every policy leaves a resolved variable alone when there is nothing to change — either the package bundles no value for it (values were excluded at export, or the exported value was itself empty), or the value it bundles already matches the target's. The reverse does not hold: a resolved variable holding an empty value — a stub an earlier import created, say — still counts as a value, so `overwrite` fills it and `fail` rejects it. Under `overwrite`, a project package whose projects hold _different_ values for a name they all resolve to one row — a global none of them shadows, typically — is rejected with a 409: one row cannot carry both values, and the import will not pick for you. Give the projects their own variables in the target, or import them separately.

Default: `keep-existing`Possible values: `keep-existing``overwrite``fail`

variableParentPolicystring · enumOptional

Where `create-with-value` and `create-stub` create missing variables for workflow/folder packages. `project` — also the behaviour when the field is omitted — creates them in the import target project (`projectId`, else the caller's personal project). `global` creates them at the global scope. The license and `variable:create` requirements described under `variableMissingMode` apply to both placements. Must be omitted for project packages, which reject it with a 400: their placement follows the package layout, where a variable bundled under a project is created in that project and one bundled at the top level is created globally.

Possible values: `project``global`

tagMissingModestring · enumOptional

What to do when a tag referenced by the package's workflows has no tag with the same id on the target instance (tags are matched by source id, never by name). `create` (default) creates the tag globally with its package (source) id and name; when the import would create a tag this needs an API key carrying the `tag:create` scope. `do-nothing` imports the workflows without the missing tags — nothing is created and the dropped names are listed under `tags.skipped`.

Default: `create`Possible values: `create``do-nothing`

tagConflictPolicystring · enumOptional

What to do when a referenced tag conflicts on the target instance — either the same-id target tag carries a different name (rename drift), or the tag's name is already held by a different tag (name collision). `skip` (default) drops the conflicted tags from the import (not created, not renamed, not attached anywhere; the import proceeds and lists them under `tags.skipped`). `fail` rejects the import with a 409. `rename` renames a drifted target tag to the package name, and reconciles a name collision by re-keying the existing tag to the package (source) id — its name, workflow and folder taggings follow; both need an API key carrying the `tag:update` scope when the import would rename or reconcile a tag. A drifted tag whose package name is held by another tag still rejects the import (rename degrades to fail).

Default: `skip`Possible values: `skip``fail``rename`

Responses

200

Operation successful.

application/json

packageobjectRequired

Show properties

workflowsobject\[\]Required

Show properties

removedWorkflowsobject\[\]Required

Workflows removed from the target during this import.

Show properties

removedFoldersobject\[\]Required

Folders the package does not define that reconciliation left empty, removed by `folderConflictPolicy=overwrite`. A folder still holding anything survives, so target-only content is never swept up. Empty under every other policy.

Show properties

foldersobject\[\]Required

Folder shells created or skipped in the target project.

Show properties

projectsobject\[\]Required

Project shells created, or matched and then updated or left as-is (see `projectConflictPolicy`). Present for project packages; empty when importing loose workflows/folders.

Show properties

bindingsobjectRequired

Source id → target id mappings produced during import, one map per entity type. Each value maps an id as it appeared in the package to the id on the target instance.

Show properties

credentialsobjectRequired

Source credential ids grouped by whether they matched an existing credential or were created as empty stubs, seeded credentials, or incomplete credentials. Full source→target id mapping is in `bindings.credentials`.

Show properties

dataTablesobjectRequired

Show properties

variablesobjectRequired

Resolution of the package's variable requirements. Names only — values never travel in the response. For project packages these arrays are package-level unions of per-destination outcomes and may overlap (for example, a name may be created with a value in one project and stubbed in another); classification under concurrent external writes is best-effort.

Show properties

tagsobjectRequired

Resolution of the tags referenced by the imported workflows, matched by source id. Tag names only.

Show properties

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

409

Import blocked by at least one conflict among the issues — a workflow source-id conflict, a folder conflict, a tag conflict (rename drift or name collision), a data table conflict (id owned by another project, or a name that another table in the project has), a variable whose bundled value differs from the resolved target, or a selected destination also named for deletion.

application/json

413

Content too large.

415

Unsupported media type.

422

Import blocked by non-conflict issues only — for example unresolved credentials or variables, node types this instance does not have, a delete the caller may not perform, or variable stubs whose creation would exceed the instance variable quota.

application/json

500

Internal server error.

post/n8n-packages/import

HTTP

Copy

    POST /api/v1/n8n-packages/import HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: multipart/form-data
    Accept: */*
    Content-Length: 676
    
    {
      "package": "binary",
      "projectId": "text",
      "folderId": "text",
      "credentialMatchingMode": "id-only",
      "credentialMissingMode": "create-stub",
      "bindings": "{}",
      "workflowConflictPolicy": "new-version",
      "workflowPublishingPolicy": "preserve-published-state",
      "workflowIdPolicy": "source",
      "missingNodeTypeMode": "fail",
      "projectConflictPolicy": "merge",
      "folderConflictPolicy": "merge",
      "overwriteDeletionPolicy": "archive",
      "dataTableMatchingMode": "by-id",
      "dataTableMissingMode": "create",
      "dataTableSchemaConflictPolicy": "keep-existing",
      "variableMissingMode": "create-with-value",
      "variableConflictPolicy": "keep-existing",
      "variableParentPolicy": "project",
      "tagMissingMode": "create",
      "tagConflictPolicy": "skip"
    }

Test it

200

Operation successful.

Copy

    {
      "package": {
        "sourceN8nVersion": "text",
        "sourceId": "text",
        "exportedAt": "2026-01-01T00:00:00.000Z"
      },
      "workflows": [\
        {\
          "sourceWorkflowId": "text",\
          "localId": "text",\
          "name": "text",\
          "projectId": "text",\
          "parentFolderId": "text",\
          "activeVersionId": "text",\
          "isArchived": true,\
          "publishing": {\
            "state": "published",\
            "error": "text",\
            "blockedReason": "stub-credential",\
            "skippedPublishReason": "stub-credential"\
          },\
          "status": "created"\
        }\
      ],
      "removedWorkflows": [\
        {\
          "workflowId": "text",\
          "name": "text",\
          "projectId": "text",\
          "parentFolderId": "text",\
          "deletion": "archived"\
        }\
      ],
      "removedFolders": [\
        {\
          "folderId": "text",\
          "name": "text",\
          "projectId": "text",\
          "parentFolderId": "text"\
        }\
      ],
      "folders": [\
        {\
          "sourceFolderId": "text",\
          "localId": "text",\
          "name": "text",\
          "parentFolderId": "text",\
          "status": "created"\
        }\
      ],
      "projects": [\
        {\
          "sourceProjectId": "text",\
          "localId": "text",\
          "name": "text",\
          "status": "created"\
        }\
      ],
      "bindings": {
        "workflows": {
          "ANY_ADDITIONAL_PROPERTY": "text"
        },
        "credentials": {
          "ANY_ADDITIONAL_PROPERTY": "text"
        }
      },
      "credentials": {
        "matched": [\
          "text"\
        ],
        "stubbed": [\
          "text"\
        ],
        "seeded": [\
          "text"\
        ],
        "incomplete": [\
          "text"\
        ]
      },
      "dataTables": {
        "matched": 1,
        "created": 1,
        "updated": 1
      },
      "variables": {
        "matched": [\
          "text"\
        ],
        "missing": [\
          "text"\
        ],
        "created": [\
          "text"\
        ],
        "stubbed": [\
          "text"\
        ],
        "updated": [\
          "text"\
        ]
      },
      "tags": {
        "matched": [\
          "text"\
        ],
        "created": [\
          "text"\
        ],
        "renamed": [\
          "text"\
        ],
        "reconciled": [\
          "text"\
        ],
        "skipped": [\
          "text"\
        ]
      }
    }

### Beta: Import a selected subset of workflows from an n8n package[](https://docs.n8n.io/connect/n8n-api/n8n-package#post-n8n-packages-import-selection)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/n8n-packages/import-selection

**Beta** — breaking changes may still occur without major version bump.

Imports a chosen subset of workflows from one source project of a gzip-compressed tar package (`.n8np`), instead of the whole package. Send the archive as the multipart field `package`. The import is **additive** (cherry-pick): it never removes a workflow the selection omits. It creates or updates only the workflows named in `selectedWorkflowIds`, and deletes only the destination workflows named in `deletedWorkflowIds`.

`selectedProjectId` names the single source project the selection is scoped to (its id as it appears in the package). The selected workflows are written into the instance project whose id matches that source project, which is created if it does not yet exist; there is no separate target-project field. `selectedWorkflowIds` are source ids within that project; ids that belong to another project are dropped. `deletedWorkflowIds` are destination ids in the same project; an absent id is a tolerated no-op, and a delete needs the `workflow:delete` scope. A delete id must not match the destination id of a selected workflow, including when `workflowConflictPolicy=skip`. This overlap returns a 409 before any writes.

The package must be a project package (a workflow package is rejected with a 400). The cherry-pick conflict policies (folder, tag, and project) are fixed and are not accepted here; only `workflowConflictPolicy`, `workflowIdPolicy`, and `overwriteDeletionPolicy` are configurable. Maximum upload size is `N8N_ENDPOINTS_PAYLOAD_SIZE_MAX` MB (default 16). The caller is authorised through the `workflow:import` scope.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

multipart/form-data

packagestring · binaryRequired

Gzip-compressed tar package (`.n8np`).

selectedProjectIdstring · min: 1Required

Id of the single source project the selection is scoped to, as it appears in the package.

selectedWorkflowIdsstringRequired

JSON-encoded array of source workflow ids to import from `selectedProjectId`, e.g. `["wf-1","wf-2"]`. An empty array (`[]`) is allowed — useful for a delete-only request. Ids outside the scoped project are dropped.

deletedWorkflowIdsstringOptional

Optional JSON-encoded array of destination workflow ids to remove from the scoped project, e.g. `["wf-3"]`. Removal happens even under the additive profile, and the manner of removal follows `overwriteDeletionPolicy` (archive by default). An absent id is a no-op unless it is also a selected destination. Must not contain a selected workflow's destination id. Needs the `workflow:delete` scope.

workflowConflictPolicystring · enumOptional

What happens when a selected workflow matches an existing workflow by source id in the target project. `new-version` (default) updates it and creates a new version; `fail` rejects the import when any matching workflow exists; `skip` leaves matching workflows unchanged. An archive state change also needs the `workflow:delete` scope.

Default: `new-version`Possible values: `new-version``fail``skip`

workflowIdPolicystring · enumOptional

Controls the id each newly created workflow receives. `source` (default) reuses the package's own workflow id on the target instance; `new` mints a fresh id and records the package id as `sourceWorkflowId`. Workflows matched to an existing workflow keep that workflow's current id, regardless of policy.

Default: `source`Possible values: `new``source`

overwriteDeletionPolicystring · enumOptional

How the ids in `deletedWorkflowIds` are removed. `archive` (default) archives each one, so it stays recoverable along with its execution history. `hard-delete` archives it — the step that unpublishes it, which a delete will not do on its own — and then deletes the workflow and its executions permanently. Each entry in `removedWorkflows` reports what actually happened in its `deletion` field: a `hard-delete` whose row cannot be dropped yet, because unpublishing defers trigger teardown, is left `archived` rather than failing an import whose content is already written.

Default: `archive`Possible values: `archive``hard-delete`

Responses

200

Operation successful.

application/json

packageobjectRequired

Show properties

workflowsobject\[\]Required

Show properties

removedWorkflowsobject\[\]Required

Workflows removed from the target during this import.

Show properties

removedFoldersobject\[\]Required

Folders the package does not define that reconciliation left empty, removed by `folderConflictPolicy=overwrite`. A folder still holding anything survives, so target-only content is never swept up. Empty under every other policy.

Show properties

foldersobject\[\]Required

Folder shells created or skipped in the target project.

Show properties

projectsobject\[\]Required

Project shells created, or matched and then updated or left as-is (see `projectConflictPolicy`). Present for project packages; empty when importing loose workflows/folders.

Show properties

bindingsobjectRequired

Source id → target id mappings produced during import, one map per entity type. Each value maps an id as it appeared in the package to the id on the target instance.

Show properties

credentialsobjectRequired

Source credential ids grouped by whether they matched an existing credential or were created as empty stubs, seeded credentials, or incomplete credentials. Full source→target id mapping is in `bindings.credentials`.

Show properties

dataTablesobjectRequired

Show properties

variablesobjectRequired

Resolution of the package's variable requirements. Names only — values never travel in the response. For project packages these arrays are package-level unions of per-destination outcomes and may overlap (for example, a name may be created with a value in one project and stubbed in another); classification under concurrent external writes is best-effort.

Show properties

tagsobjectRequired

Resolution of the tags referenced by the imported workflows, matched by source id. Tag names only.

Show properties

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

409

Import blocked by at least one conflict among the issues — for example a workflow source-id conflict under `workflowConflictPolicy=fail`, or a selected destination also named for deletion (`workflow-removal-conflict`).

application/json

413

Content too large.

415

Unsupported media type.

422

Import blocked by non-conflict issues only — for example a delete the caller may not perform (`workflow-removal-forbidden`), unresolved credentials, or node types this instance does not have.

application/json

500

Internal server error.

post/n8n-packages/import-selection

HTTP

Copy

    POST /api/v1/n8n-packages/import-selection HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: multipart/form-data
    Accept: */*
    Content-Length: 207
    
    {
      "package": "binary",
      "selectedProjectId": "text",
      "selectedWorkflowIds": "text",
      "deletedWorkflowIds": "text",
      "workflowConflictPolicy": "new-version",
      "workflowIdPolicy": "source",
      "overwriteDeletionPolicy": "archive"
    }

Test it

200

Operation successful.

Copy

    {
      "package": {
        "sourceN8nVersion": "text",
        "sourceId": "text",
        "exportedAt": "2026-01-01T00:00:00.000Z"
      },
      "workflows": [\
        {\
          "sourceWorkflowId": "text",\
          "localId": "text",\
          "name": "text",\
          "projectId": "text",\
          "parentFolderId": "text",\
          "activeVersionId": "text",\
          "isArchived": true,\
          "publishing": {\
            "state": "published",\
            "error": "text",\
            "blockedReason": "stub-credential",\
            "skippedPublishReason": "stub-credential"\
          },\
          "status": "created"\
        }\
      ],
      "removedWorkflows": [\
        {\
          "workflowId": "text",\
          "name": "text",\
          "projectId": "text",\
          "parentFolderId": "text",\
          "deletion": "archived"\
        }\
      ],
      "removedFolders": [\
        {\
          "folderId": "text",\
          "name": "text",\
          "projectId": "text",\
          "parentFolderId": "text"\
        }\
      ],
      "folders": [\
        {\
          "sourceFolderId": "text",\
          "localId": "text",\
          "name": "text",\
          "parentFolderId": "text",\
          "status": "created"\
        }\
      ],
      "projects": [\
        {\
          "sourceProjectId": "text",\
          "localId": "text",\
          "name": "text",\
          "status": "created"\
        }\
      ],
      "bindings": {
        "workflows": {
          "ANY_ADDITIONAL_PROPERTY": "text"
        },
        "credentials": {
          "ANY_ADDITIONAL_PROPERTY": "text"
        }
      },
      "credentials": {
        "matched": [\
          "text"\
        ],
        "stubbed": [\
          "text"\
        ],
        "seeded": [\
          "text"\
        ],
        "incomplete": [\
          "text"\
        ]
      },
      "dataTables": {
        "matched": 1,
        "created": 1,
        "updated": 1
      },
      "variables": {
        "matched": [\
          "text"\
        ],
        "missing": [\
          "text"\
        ],
        "created": [\
          "text"\
        ],
        "stubbed": [\
          "text"\
        ],
        "updated": [\
          "text"\
        ]
      },
      "tags": {
        "matched": [\
          "text"\
        ],
        "created": [\
          "text"\
        ],
        "renamed": [\
          "text"\
        ],
        "reconciled": [\
          "text"\
        ],
        "skipped": [\
          "text"\
        ]
      }
    }

### Beta: Export agents, workflows, folders, or projects as an n8n package[](https://docs.n8n.io/connect/n8n-api/n8n-package#post-n8n-packages-export)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/n8n-packages/export

**Beta** — breaking changes may still occur without major version bump.

Export agents, workflows, and folders, or whole projects, as a gzipped tar archive (.n8np). Provide `agentIds`/`workflowIds`/`folderIds`, or `projectIds`. Do not combine these two groups. Each exported folder includes its nested folders. Whole projects include their agents when the agents module is enabled. Explicit agent selections require the agents module. Empty projects export project metadata only. `versionPolicy` selects the version for both agents and workflows and defaults to `latest`. `dependencyPolicy` applies to both entity types and defaults to `fail` when a required definition is absent from the package. The response is streamed as `application/gzip` with a `Content-Disposition` attachment header. Requires the n8n Packages feature to be licensed.

API key scopes: `agent:export` is required for explicitly selected agents. `workflow:export` is required for explicitly selected workflows or folders. `project:export` is sufficient for whole-project exports, including their agents and workflows. Included dependencies need no additional API key scope. The caller's project permissions apply to all included entities. When `includeVariableValues` is true (the default) and exported entities reference variables, `variable:list` is also required. Exports that reference no variables do not need it.

Agent definitions include referenced skills, custom tools, and schedules. Knowledge base files and runtime data are excluded. Agent package imports remain unavailable.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

agentIdsstring\[\] · min: 1 · max: 300Optional

IDs of the agents to include. Requires the agents module.

Example: `["uT9LdQx7rK2MvB4f"]`

workflowIdsstring\[\] · min: 1 · max: 300Optional

IDs of the workflows to include in the exported package.

Example: `["2tUt1wbLX592XDdX"]`

folderIdsstring\[\] · min: 1 · max: 300Optional

IDs of the folders to include in the exported package. Each folder is exported with its nested folders.

Example: `["9xKp2mNqRzAbCdEf"]`

projectIdsstring\[\] · min: 1 · max: 300Optional

IDs of the projects to include in the exported package. Includes their agents when the agents module is enabled.

Example: `["Ox8O54VQrmBrb4qL"]`

includeVariableValuesbooleanOptional

Whether values of variables referenced by the exported entities are bundled into the package. When `false`, variables still travel as name/type files and are listed in the package requirements, but no values travel with the package.

Default: `true`

includeTagsbooleanOptional

Whether tags assigned to the exported workflows are bundled into the package. When `false`, no tag files, tag references, or tag requirements travel with the package.

Default: `true`

dependencyPolicystring · enumOptional

Policy for workflow and agent dependencies outside the selected package contents. Includes static workflow references and disabled agent references. `fail` aborts when a required workflow or agent is absent from the package. `include-in-package` adds accessible dependencies recursively. `reference-only` records external requirements without including those definitions. The same policy applies to workflows and agents.

Default: `fail`Example: `fail`Possible values: `fail``reference-only``include-in-package`

versionPolicystring · enumOptional

Which version of each workflow and agent travels in the package. `latest` exports the current draft. `published-strict` requires a published version. `prefer-published` uses the published version when available and the draft otherwise. `ignore-unpublished` skips unpublished selections. Dependencies that cannot be included cause the export to fail only when `dependencyPolicy` is `fail` or `include-in-package`. With `reference-only`, the export records them as external requirements. The selected version supplies the definition and its references. Workflow names, settings, and tags always use their current values. Agent IDs, names, and MCP availability always use their current values.

Default: `latest`Example: `latest`Possible values: `published-strict``prefer-published``ignore-unpublished``latest`

credentialExportPolicystring · enumOptional

Whether expression values from credential data are bundled into the package. `expression-values-only` includes credential fields whose value is an n8n expression (for example `={{ $secrets.apiKey }}`); literal values never travel either way. `no-values` keeps credential data out of the package entirely, so each credential file carries only its id, name and type.

Default: `expression-values-only`Example: `expression-values-only`Possible values: `expression-values-only``no-values`

includeArchivedWorkflowsbooleanOptional

Whether folder and project exports include their archived workflows. When `false` (default) they are left out. When `true` they travel with `isArchived: true` and are archived on import. Workflows listed in `workflowIds` always export, also when archived.

Default: `false`Example: `false`

Responses

200

A gzipped tar archive containing the exported package contents.

application/gzip

Headersobject

Show Header

Responsestring · binary

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

404

The specified resource was not found.

409

Conflict

415

Unsupported media type.

422

Unprocessable Entity

post/n8n-packages/export

HTTP

Copy

    POST /api/v1/n8n-packages/export HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 317
    
    {
      "agentIds": [\
        "uT9LdQx7rK2MvB4f"\
      ],
      "workflowIds": [\
        "2tUt1wbLX592XDdX"\
      ],
      "folderIds": [\
        "9xKp2mNqRzAbCdEf"\
      ],
      "projectIds": [\
        "Ox8O54VQrmBrb4qL"\
      ],
      "includeVariableValues": true,
      "includeTags": true,
      "dependencyPolicy": "fail",
      "versionPolicy": "latest",
      "credentialExportPolicy": "expression-values-only",
      "includeArchivedWorkflows": false
    }

Test it

200

A gzipped tar archive containing the exported package contents.

Copy

    binary

[PreviousLog Streaming](https://docs.n8n.io/connect/n8n-api/log-streaming)
[NextNode Type Policy](https://docs.n8n.io/connect/n8n-api/node-type-policy)

Last updated 9 days ago

Was this helpful?