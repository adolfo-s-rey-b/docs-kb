For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-a-custom-workflow-templates-library.md)
.

n8n provides a library of workflow templates. When self-hosting n8n, you can:

*   Continue to use n8n's workflow templates library (this is the default behavior)
    
*   Disable workflow templates
    
*   Create your own workflow templates library
    

Disable workflow templates[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-a-custom-workflow-templates-library#disable-workflow-templates)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In your environment variables, set `N8N_TEMPLATES_ENABLED` to false.

Use your own workflow templates library[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-a-custom-workflow-templates-library#use-your-own-workflow-templates-library)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In your environment variables, set `N8N_TEMPLATES_HOST` to the base URL of your API.

#### Endpoints[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-a-custom-workflow-templates-library#endpoints)

Your API must provide the same endpoints and data structure as n8n's.

The endpoints are:

Method

Path

Purpose

GET

`/templates/workflows/<id>`

Fetch template metadata for preview/browsing

GET

`/workflows/templates/<id>`

Fetch workflow data to import onto canvas

GET

`/templates/search`

Search for workflow templates

GET

`/templates/collections/<id>`

Get a specific template collection

GET

`/templates/collections`

List all template collections

GET

`/templates/categories`

List all template categories

GET

`/health`

Health check endpoint

**Critical: Two different response formats required**

The two workflow endpoints require **different response formats**:

*   `**/templates/workflows/{id}**`: Returns the template itself, which includes the workflow in the `workflow` key
    
*   `**/workflows/templates/{id}**`: Returns the workflow the template contains
    

See Schemas below for details.

#### Query parameters[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-a-custom-workflow-templates-library#query-parameters)

The `/templates/search` endpoint accepts the following query parameters:

Parameter

Type

Description

`page`

integer

The page of results to return

`rows`

integer

The maximum number of results to return per page

`category`

comma-separated list of strings (categories)

The categories to search within

`search`

string

The search query

The `/templates/collections` endpoint accepts the following query parameters:

Parameter

Type

Description

`category`

comma-separated list of strings (categories)

The categories to search within

`search`

string

The search query

#### Schemas[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-a-custom-workflow-templates-library#schemas)

The key difference between the two workflow endpoints:

Copy

    // GET /templates/workflows/{id} returns (wrapped):
    {
      "workflow": {
        "id": 123,
        "name": "...",
        "totalViews": 1000,
        // ... see full workflow item schema below
        "workflow": {    // actual workflow definition
          "nodes": [...],
          "connections": {}
        }
      }
    }
    
    // GET /workflows/templates/{id} returns (flat):
    {
      "id": 123,
      "name": "...",
      "workflow": {      // actual workflow definition
        "nodes": [...],
        "connections": {}
      }
    }

Detailed schemas for response objects:

Show `workflow` item data schema[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-a-custom-workflow-templates-library#show-workflow-item-data-schema)

Used by `/templates/workflows/{id}` endpoint (wrapped in a `workflow` key).

This schema describes the template metadata used for displaying templates in search/browse UI. It includes a nested `workflow` property that contains the actual importable workflow definition.

Copy

    {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "title": "Generated schema for Root",
      "type": "object",
      "properties": {
        "id": {
          "type": "number"
        },
        "name": {
          "type": "string"
        },
        "totalViews": {
          "type": "number"
        },
        "price": {},
        "purchaseUrl": {},
        "recentViews": {
          "type": "number"
        },
        "createdAt": {
          "type": "string"
        },
        "user": {
          "type": "object",
          "properties": {
            "username": {
              "type": "string"
            },
            "verified": {
              "type": "boolean"
            }
          },
          "required": [\
            "username",\
            "verified"\
          ]
        },
        "nodes": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "number"
              },
              "icon": {
                "type": "string"
              },
              "name": {
                "type": "string"
              },
              "codex": {
                "type": "object",
                "properties": {
                  "data": {
                    "type": "object",
                    "properties": {
                      "details": {
                        "type": "string"
                      },
                      "resources": {
                        "type": "object",
                        "properties": {
                          "generic": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "string"
                                },
                                "icon": {
                                  "type": "string"
                                },
                                "label": {
                                  "type": "string"
                                }
                              },
                              "required": [\
                                "url",\
                                "label"\
                              ]
                            }
                          },
                          "primaryDocumentation": {
                            "type": "array",
                            "items": {
                              "type": "object",
                              "properties": {
                                "url": {
                                  "type": "string"
                                }
                              },
                              "required": [\
                                "url"\
                              ]
                            }
                          }
                        },
                        "required": [\
                          "primaryDocumentation"\
                        ]
                      },
                      "categories": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "nodeVersion": {
                        "type": "string"
                      },
                      "codexVersion": {
                        "type": "string"
                      }
                    },
                    "required": [\
                      "categories"\
                    ]
                  }
                }
              },
              "group": {
                "type": "string"
              },
              "defaults": {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string"
                  },
                  "color": {
                    "type": "string"
                  }
                },
                "required": [\
                  "name"\
                ]
              },
              "iconData": {
                "type": "object",
                "properties": {
                  "icon": {
                    "type": "string"
                  },
                  "type": {
                    "type": "string"
                  },
                  "fileBuffer": {
                    "type": "string"
                  }
                },
                "required": [\
                  "type"\
                ]
              },
              "displayName": {
                "type": "string"
              },
              "typeVersion": {
                "type": "number"
              },
              "nodeCategories": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "number"
                    },
                    "name": {
                      "type": "string"
                    }
                  },
                  "required": [\
                    "id",\
                    "name"\
                  ]
                }
              }
            },
            "required": [\
              "id",\
              "icon",\
              "name",\
              "codex",\
              "group",\
              "defaults",\
              "iconData",\
              "displayName",\
              "typeVersion"\
            ]
          }
        },
        "description": {
          "type": "string"
        },
        "image": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "number"
              },
              "url": {
                "type": "string"
              }
            }
          }
        },
        "categories": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "number"
              },
              "name": {
                "type": "string"
              }
            }
          }
        },
        "workflowInfo": {
          "type": "object",
          "properties": {
            "nodeCount": {
              "type": "number"
            },
            "nodeTypes": {
              "type": "object"
            }
          }
        },
        "workflow": {
          "type": "object",
          "properties": {
            "nodes": {
              "type": "array"
            },
            "connections": {
              "type": "object"
            },
            "settings": {
              "type": "object"
            },
            "pinData": {
              "type": "object"
            }
          },
          "required": [\
            "nodes",\
            "connections"\
          ]
        }
      },
      "required": [\
        "id",\
        "name",\
        "totalViews",\
        "createdAt",\
        "user",\
        "nodes",\
        "workflow"\
      ]
    }

Show `category` item data schema[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-a-custom-workflow-templates-library#show-category-item-data-schema)

Copy

    {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "id": {
          "type": "number"
        },
        "name": {
          "type": "string"
        }
      },
      "required": [\
        "id",\
        "name"\
      ]
    }

Show `collection` item data schema[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-a-custom-workflow-templates-library#show-collection-item-data-schema)

Copy

    {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "id": {
          "type": "number"
        },
        "rank": {
          "type": "number"
        },
        "name": {
          "type": "string"
        },
        "totalViews": {},
        "createdAt": {
          "type": "string"
        },
        "workflows": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "number"
              }
            },
            "required": [\
              "id"\
            ]
          }
        },
        "nodes": {
          "type": "array",
          "items": {}
        }
      },
      "required": [\
        "id",\
        "rank",\
        "name",\
        "totalViews",\
        "createdAt",\
        "workflows",\
        "nodes"\
      ]
    }

You can also interactively explore n8n's API endpoints:

[https://api.n8n.io/templates/categories](https://api.n8n.io/templates/categories)
 [https://api.n8n.io/templates/collections](https://api.n8n.io/templates/collections)
 [https://api.n8n.io/templates/search](https://api.n8n.io/templates/search)
 [https://api.n8n.io/health](https://api.n8n.io/health)

You can [contact us](mailto:help@n8n.io)
 for more support.

Add your workflows to the n8n library[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-a-custom-workflow-templates-library#add-your-workflows-to-the-n8n-library)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can submit your workflows to n8n's template library.

n8n is working on a creator program, and developing a marketplace of templates. This is an ongoing project, and details are likely to change.

Refer to [n8n Creator hub](https://www.notion.so/n8n/n8n-Creator-hub-7bd2cbe0fce0449198ecb23ff4a2f76f)
 for information on how to submit templates and become a creator.

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-a-custom-workflow-templates-library#related-resources)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Configuration examples](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples)
    

[PreviousPre-configure Microsoft OAuth credentials](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/pre-configure-microsoft-oauth-credentials)
[NextChoose n8n's database](https://docs.n8n.io/deploy/host-n8n/configure-n8n/choose-n8ns-database)

Last updated 10 days ago

Was this helpful?