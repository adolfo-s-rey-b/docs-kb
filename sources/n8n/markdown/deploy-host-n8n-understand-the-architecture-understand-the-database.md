For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database.md)
.

This page describes the purpose of each table in the n8n database.

Database and query technology[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#database-and-query-technology)

-------------------------------------------------------------------------------------------------------------------------------------------------------

By default, n8n uses SQLite as the database. If you are using another database the structure will be similar, but the data-types may be different depending on the database.

n8n uses [TypeORM](https://github.com/typeorm/typeorm)
 for queries and migrations.

To inspect the n8n database, you can use [DBeaver](https://dbeaver.io/)
, which is an open-source universal database tool.

Tables[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#tables)

---------------------------------------------------------------------------------------------------------

These are the tables n8n creates during setup.

### auth\_identity[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#authidentity)

Stores details of external authentication providers when using [SAML](https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/use-saml)
.

### auth\_provider\_sync\_history[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#authprovidersynchistory)

Stores the history of a SAML connection.

### credentials\_entity[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#credentialsentity)

Stores the credentials used to authenticate with integrations.

### event\_destinations[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#eventdestinations)

Contains the destination configurations for [Log streaming](https://docs.n8n.io/administer/observe-and-log/stream-logs-to-external-systems)
.

### execution\_data[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#executiondata)

Contains the workflow at time of running, and the execution data.

### execution\_entity[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#executionentity)

Stores all saved workflow executions. Workflow settings can affect which executions n8n saves.

### execution\_metadata[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#executionmetadata)

Stores [Custom executions data](https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data)
.

### installed\_nodes[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#installednodes)

Lists the [community nodes](https://docs.n8n.io/integrations/community-nodes/installation-and-management)
 installed in your n8n instance.

### installed\_packages[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#installedpackages)

Details of npm community nodes packages installed in your n8n instance. [`installed_nodes`](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#installednodes)
 lists each individual node. `installed_packages` lists npm packages, which may contain more than one node.

### migrations[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#migrations)

A log of all database migrations. Read more about [Migrations](https://typeorm.io/docs/advanced-topics/migrations/)
 in TypeORM's documentation.

### project[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#project)

Lists the [projects](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects)
 in your instance.

### project\_relation[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#projectrelation)

Describes the relationship between a user and a [project](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects)
, including the user's [role type](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/see-available-roles)
.

### role[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#role)

Not currently used. For use in future work on custom roles.

### settings[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#settings)

Records custom instance settings. These are settings that you can't control using environment variables. They include:

*   Whether the instance owner is set up
    
*   Whether the user chose to skip owner and user management setup
    
*   Whether certain types of authentication, including SAML and LDAP, are on
    
*   License key
    

### shared\_credentials[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#sharedcredentials)

Maps credentials to users.

### shared\_workflow[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#sharedworkflow)

Maps workflows to users.

### tag\_entity[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#tagentity)

All workflow tags created in the n8n instance. This table lists the tags. [`workflows_tags`](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#workflowstags)
 records which workflows have which tags.

### user[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#user)

Contains user data.

### variables[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#variables)

Store [variables](https://docs.n8n.io/build/code-in-n8n/define-custom-variables)
.

### webhook\_entity[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#webhookentity)

Records the active webhooks in your n8n instance's workflows. This isn't just webhooks uses in the Webhook node. It includes all active webhooks used by any trigger node.

### workflow\_entity[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#workflowentity)

Your n8n instance's saved workflows.

### workflow\_history[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#workflowhistory)

Store previous versions of workflows.

### workflow\_statistics[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#workflowstatistics)

Counts workflow IDs and their status.

### workflows\_tags[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#workflowstags)

Maps tags to workflows. [`tag_entity`](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#tagentity)
 contains tag details.

Entity Relationship Diagram (ERD)[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#entity-relationship-diagram-erd)

-------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2773773108-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fjm0ZYRpZIPWge2ZSiDYO%252Fuploads%252Fgit-blob-609f5ea22a39df9891e515216fff6a37caf65861%252Fn8n-database-diagram.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=1c50199369321ce2e954636da127f667&sv=3)

Entity relationship diagram showing foreign-key connections between n8n's database tables, including user, workflow\_entity, execution\_entity, and credentials\_entity

Related resources[](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database#related-resources)

-------------------------------------------------------------------------------------------------------------------------------

*   [Understand the architecture](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture)
    
*   [How n8n works](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/how-n8n-works)
    

[PreviousHow n8n works](https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/how-n8n-works)
[NextDeploy as an OEM integration](https://docs.n8n.io/deploy/host-n8n/deploy-as-an-oem-integration)

Last updated 10 days ago

Was this helpful?