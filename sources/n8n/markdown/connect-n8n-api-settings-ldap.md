For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/n8n-api/settings-ldap.md)
.

Copy

On this page

Operations about LDAP settings

### Retrieve the LDAP configuration[](https://docs.n8n.io/connect/n8n-api/settings-ldap#get-settings-ldap)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/settings/ldap

Retrieve the current LDAP configuration, including every field exposed in the UI. The binding admin password is redacted on read. Requires the `ldap:manage` scope and the LDAP feature to be licensed.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Responses

200

Operation successful.

application/json

Full LDAP configuration. Every field is returned by GET; send the full object back as PUT body.

loginEnabledbooleanRequired

Whether LDAP login is enabled.

Example: `false`

loginLabelstringRequired

Label shown on the LDAP login button.

Example: `LDAP`

connectionUrlstringRequired

LDAP server URL.

Example: `ldap://ldap.example.com`

allowUnauthorizedCertsbooleanRequired

Whether to allow unauthorized (self-signed) certificates.

Example: `false`

connectionSecuritystring · enumRequired

TLS/SSL security mode for the LDAP connection.

Example: `none`Possible values: `none``tls``startTls`

connectionPortnumberRequired

LDAP server port.

Example: `389`

baseDnstringRequired

Base DN for LDAP search queries.

Example: `dc=example,dc=com`

bindingAdminDnstringRequired

DN of the LDAP admin user for binding.

Example: `cn=admin,dc=example,dc=com`

bindingAdminPasswordstringRequired

Password for the LDAP admin user. Redacted on GET; returns the blanking placeholder when a password is stored, empty string when unset. Send the blanking placeholder from a prior GET to keep the stored password unchanged.

firstNameAttributestringRequired

LDAP attribute mapped to the user's first name.

Example: `givenName`

lastNameAttributestringRequired

LDAP attribute mapped to the user's last name.

Example: `sn`

emailAttributestringRequired

LDAP attribute mapped to the user's email.

Example: `mail`

loginIdAttributestringRequired

LDAP attribute used for login (usually the same as emailAttribute).

Example: `mail`

ldapIdAttributestringRequired

LDAP attribute that uniquely identifies a user.

Example: `uid`

userFilterstringRequired

Additional LDAP filter to apply when searching for users. Use an empty string for no additional filter.

Example: `(objectClass=inetOrgPerson)`

synchronizationEnabledbooleanRequired

Whether automatic LDAP synchronization is enabled.

Example: `false`

synchronizationIntervalnumberRequired

Interval in minutes between automatic synchronizations. Ignored if synchronizationEnabled is false.

Example: `60`

searchPageSizenumberRequired

Number of LDAP entries to fetch per search page.

Example: `1000`

searchTimeoutnumberRequired

LDAP search timeout in seconds.

Example: `60`

enforceEmailUniquenessbooleanRequired

Whether to enforce that email addresses are unique across LDAP users. When true, if two users have the same email, only the first will be imported.

Example: `true`

linkExistingAccountsByEmailbooleanRequired

Whether an LDAP user may be linked to an existing n8n account that has the same email. When false, login and synchronization skip such users. Optional on PUT; the stored value is kept when omitted.

Example: `true`

401

Unauthorized

403

Forbidden

get/settings/ldap

HTTP

Copy

    GET /api/v1/settings/ldap HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "loginEnabled": false,
      "loginLabel": "LDAP",
      "connectionUrl": "ldap://ldap.example.com",
      "allowUnauthorizedCerts": false,
      "connectionSecurity": "none",
      "connectionPort": 389,
      "baseDn": "dc=example,dc=com",
      "bindingAdminDn": "cn=admin,dc=example,dc=com",
      "bindingAdminPassword": "text",
      "firstNameAttribute": "givenName",
      "lastNameAttribute": "sn",
      "emailAttribute": "mail",
      "loginIdAttribute": "mail",
      "ldapIdAttribute": "uid",
      "userFilter": "(objectClass=inetOrgPerson)",
      "synchronizationEnabled": false,
      "synchronizationInterval": 60,
      "searchPageSize": 1000,
      "searchTimeout": 60,
      "enforceEmailUniqueness": true,
      "linkExistingAccountsByEmail": true
    }

### Set the LDAP configuration[](https://docs.n8n.io/connect/n8n-api/settings-ldap#put-settings-ldap)

put

/api/v1Current n8n instance (self-hosted built-in playground)

/settings/ldap

Replace the LDAP configuration with the provided full object (partial updates are not supported). For bindingAdminPassword, submit the blanking placeholder from a prior GET to keep the stored password unchanged. Requires the `ldap:manage` scope and the LDAP feature to be licensed. Setting loginEnabled to false is destructive and it deletes all stored LDAP user identities and disables synchronization.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Body

application/json

Full LDAP configuration. Use empty strings for unset fields.

loginEnabledbooleanRequired

Whether LDAP login is enabled. Setting this to false is destructive — it deletes all stored LDAP user identities and disables synchronization.

Example: `false`

loginLabelstringRequired

Label shown on the LDAP login button.

Example: `LDAP`

connectionUrlstringRequired

LDAP server URL.

Example: `ldap://ldap.example.com`

allowUnauthorizedCertsbooleanRequired

Whether to allow unauthorized (self-signed) certificates.

Example: `false`

connectionSecuritystring · enumRequired

TLS/SSL security mode for the LDAP connection.

Example: `none`Possible values: `none``tls``startTls`

connectionPortintegerRequired

LDAP server port.

Example: `389`

baseDnstringRequired

Base DN for LDAP search queries.

Example: `dc=example,dc=com`

bindingAdminDnstringRequired

DN of the LDAP admin user for binding.

Example: `cn=admin,dc=example,dc=com`

bindingAdminPasswordstringRequired

Password for the LDAP admin user. To keep an existing password unchanged, submit the blanking placeholder from a prior GET response. Use an empty string to clear the password.

firstNameAttributestringRequired

LDAP attribute mapped to the user's first name.

Example: `givenName`

lastNameAttributestringRequired

LDAP attribute mapped to the user's last name.

Example: `sn`

emailAttributestringRequired

LDAP attribute mapped to the user's email.

Example: `mail`

loginIdAttributestringRequired

LDAP attribute used for login (usually the same as emailAttribute).

Example: `mail`

ldapIdAttributestringRequired

LDAP attribute that uniquely identifies a user.

Example: `uid`

userFilterstringRequired

Additional LDAP filter to apply when searching for users. Use an empty string for no additional filter.

Example: `(objectClass=inetOrgPerson)`

synchronizationEnabledbooleanRequired

Whether automatic LDAP synchronization is enabled.

Example: `false`

synchronizationIntervalintegerRequired

Interval in minutes between automatic synchronizations. Ignored if synchronizationEnabled is false.

Example: `60`

searchPageSizeintegerRequired

Number of LDAP entries to fetch per search page.

Example: `1000`

searchTimeoutintegerRequired

LDAP search timeout in seconds.

Example: `60`

enforceEmailUniquenessbooleanRequired

Whether to enforce that email addresses are unique across LDAP users. When true, if two users have the same email, only the first will be imported.

Example: `true`

linkExistingAccountsByEmailbooleanOptional

Whether an LDAP user may be linked to an existing n8n account that has the same email. When false, login and synchronization skip such users. Optional on PUT; the stored value is kept when omitted.

Example: `true`

Responses

200

Operation successful.

application/json

Full LDAP configuration. Every field is returned by GET; send the full object back as PUT body.

loginEnabledbooleanRequired

Whether LDAP login is enabled.

Example: `false`

loginLabelstringRequired

Label shown on the LDAP login button.

Example: `LDAP`

connectionUrlstringRequired

LDAP server URL.

Example: `ldap://ldap.example.com`

allowUnauthorizedCertsbooleanRequired

Whether to allow unauthorized (self-signed) certificates.

Example: `false`

connectionSecuritystring · enumRequired

TLS/SSL security mode for the LDAP connection.

Example: `none`Possible values: `none``tls``startTls`

connectionPortnumberRequired

LDAP server port.

Example: `389`

baseDnstringRequired

Base DN for LDAP search queries.

Example: `dc=example,dc=com`

bindingAdminDnstringRequired

DN of the LDAP admin user for binding.

Example: `cn=admin,dc=example,dc=com`

bindingAdminPasswordstringRequired

Password for the LDAP admin user. Redacted on GET; returns the blanking placeholder when a password is stored, empty string when unset. Send the blanking placeholder from a prior GET to keep the stored password unchanged.

firstNameAttributestringRequired

LDAP attribute mapped to the user's first name.

Example: `givenName`

lastNameAttributestringRequired

LDAP attribute mapped to the user's last name.

Example: `sn`

emailAttributestringRequired

LDAP attribute mapped to the user's email.

Example: `mail`

loginIdAttributestringRequired

LDAP attribute used for login (usually the same as emailAttribute).

Example: `mail`

ldapIdAttributestringRequired

LDAP attribute that uniquely identifies a user.

Example: `uid`

userFilterstringRequired

Additional LDAP filter to apply when searching for users. Use an empty string for no additional filter.

Example: `(objectClass=inetOrgPerson)`

synchronizationEnabledbooleanRequired

Whether automatic LDAP synchronization is enabled.

Example: `false`

synchronizationIntervalnumberRequired

Interval in minutes between automatic synchronizations. Ignored if synchronizationEnabled is false.

Example: `60`

searchPageSizenumberRequired

Number of LDAP entries to fetch per search page.

Example: `1000`

searchTimeoutnumberRequired

LDAP search timeout in seconds.

Example: `60`

enforceEmailUniquenessbooleanRequired

Whether to enforce that email addresses are unique across LDAP users. When true, if two users have the same email, only the first will be imported.

Example: `true`

linkExistingAccountsByEmailbooleanRequired

Whether an LDAP user may be linked to an existing n8n account that has the same email. When false, login and synchronization skip such users. Optional on PUT; the stored value is kept when omitted.

Example: `true`

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

415

Unsupported media type.

put/settings/ldap

HTTP

Copy

    PUT /api/v1/settings/ldap HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 610
    
    {
      "loginEnabled": false,
      "loginLabel": "LDAP",
      "connectionUrl": "ldap://ldap.example.com",
      "allowUnauthorizedCerts": false,
      "connectionSecurity": "none",
      "connectionPort": 389,
      "baseDn": "dc=example,dc=com",
      "bindingAdminDn": "cn=admin,dc=example,dc=com",
      "bindingAdminPassword": "text",
      "firstNameAttribute": "givenName",
      "lastNameAttribute": "sn",
      "emailAttribute": "mail",
      "loginIdAttribute": "mail",
      "ldapIdAttribute": "uid",
      "userFilter": "(objectClass=inetOrgPerson)",
      "synchronizationEnabled": false,
      "synchronizationInterval": 60,
      "searchPageSize": 1000,
      "searchTimeout": 60,
      "enforceEmailUniqueness": true,
      "linkExistingAccountsByEmail": true
    }

Test it

200

Operation successful.

Copy

    {
      "loginEnabled": false,
      "loginLabel": "LDAP",
      "connectionUrl": "ldap://ldap.example.com",
      "allowUnauthorizedCerts": false,
      "connectionSecurity": "none",
      "connectionPort": 389,
      "baseDn": "dc=example,dc=com",
      "bindingAdminDn": "cn=admin,dc=example,dc=com",
      "bindingAdminPassword": "text",
      "firstNameAttribute": "givenName",
      "lastNameAttribute": "sn",
      "emailAttribute": "mail",
      "loginIdAttribute": "mail",
      "ldapIdAttribute": "uid",
      "userFilter": "(objectClass=inetOrgPerson)",
      "synchronizationEnabled": false,
      "synchronizationInterval": 60,
      "searchPageSize": 1000,
      "searchTimeout": 60,
      "enforceEmailUniqueness": true,
      "linkExistingAccountsByEmail": true
    }

### Retrieve LDAP synchronization history[](https://docs.n8n.io/connect/n8n-api/settings-ldap#get-settings-ldap-sync)

get

/api/v1Current n8n instance (self-hosted built-in playground)

/settings/ldap/sync

Retrieve the history of LDAP synchronizations, most recent first. Requires the `ldap:sync` scope and the LDAP feature to be licensed.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Query parameters

limitnumber · max: 250Optional

The maximum number of items to return.

Default: `100`Example: `100`

cursorstringOptional

Paginate by setting the cursor parameter to the nextCursor attribute returned by the previous request's response. Default value fetches the first "page" of the collection. See pagination for more detail.

Responses

200

Operation successful.

application/json

dataobject\[\]Required

LDAP synchronization history record.

Show properties

nextCursorstring · nullableRequired

Paginate through the synchronization history by setting the cursor parameter to the nextCursor attribute returned by the previous request. A null value means there are no more records.

Example: `MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA`

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

get/settings/ldap/sync

HTTP

Copy

    GET /api/v1/settings/ldap/sync HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Accept: */*
    

Test it

200

Operation successful.

Copy

    {
      "data": [\
        {\
          "id": 1,\
          "runMode": "live",\
          "status": "success",\
          "startedAt": "2025-07-21T10:30:00Z",\
          "endedAt": "2025-07-21T10:35:00Z",\
          "scanned": 42,\
          "created": 5,\
          "updated": 3,\
          "disabled": 0,\
          "error": ""\
        }\
      ],
      "nextCursor": "MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA"
    }

### Trigger an LDAP synchronization[](https://docs.n8n.io/connect/n8n-api/settings-ldap#post-settings-ldap-sync)

post

/api/v1Current n8n instance (self-hosted built-in playground)

/settings/ldap/sync

Manually trigger an LDAP synchronization. The response returns the new sync history record. Requires the `ldap:sync` scope and the LDAP feature to be licensed.

Authorizations

ApiKeyAuth

X-N8N-API-KEYstringRequired

Header parameters

Idempotency-Keystring · min: 1 · max: 128Optional

Safe retry key for this POST. Use 1 to 128 visible ASCII characters. The same key and the same request return the first successful response. A different request with this key returns 422. A retry while the first request is in progress returns 409.

Pattern: `^[\x21-\x7E]+$`

Body

application/json

Request body for triggering an LDAP synchronization.

typestring · enumRequired

Type of synchronization. 'live' applies changes to the database. 'dry' performs a test run and does not persist changes.

Example: `live`Possible values: `live``dry`

Responses

200

Operation successful.

application/json

LDAP synchronization history record.

idintegerRequired

Unique identifier for this sync run.

Example: `1`

runModestring · enumRequired

Whether the sync was a dry run or applied live.

Example: `live`Possible values: `dry``live`

statusstringRequired

Status of the synchronization (for example, success or error).

Example: `success`

startedAtstring · date-timeRequired

Timestamp when the synchronization started.

Example: `2025-07-21T10:30:00Z`

endedAtstring · date-timeRequired

Timestamp when the synchronization completed.

Example: `2025-07-21T10:35:00Z`

scannedintegerRequired

Number of LDAP entries scanned during synchronization.

Example: `42`

createdintegerRequired

Number of new users created during synchronization.

Example: `5`

updatedintegerRequired

Number of existing users updated during synchronization.

Example: `3`

disabledintegerRequired

Number of users disabled during synchronization.

Example: `0`

errorstringRequired

Error message if the synchronization failed. Empty string if successful.

400

The request is invalid or provides malformed data.

401

Unauthorized

403

Forbidden

409

Conflict

415

Unsupported media type.

422

Unprocessable Entity

post/settings/ldap/sync

HTTP

Copy

    POST /api/v1/settings/ldap/sync HTTP/1.1
    X-N8N-API-KEY: YOUR_API_KEY
    Content-Type: application/json
    Accept: */*
    Content-Length: 15
    
    {
      "type": "live"
    }

Test it

200

Operation successful.

Copy

    {
      "id": 1,
      "runMode": "live",
      "status": "success",
      "startedAt": "2025-07-21T10:30:00Z",
      "endedAt": "2025-07-21T10:35:00Z",
      "scanned": 42,
      "created": 5,
      "updated": 3,
      "disabled": 0,
      "error": ""
    }

[PreviousSecurity Policy](https://docs.n8n.io/connect/n8n-api/security-policy)
[NextSettings Otel](https://docs.n8n.io/connect/n8n-api/settings-otel)

Last updated 9 days ago

Was this helpful?