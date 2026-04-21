# Onshape Developer Documentation — Local Reference

Source: <https://onshape-public.github.io/docs/>  
Crawled: 2026-04-21  
Pages included: 36  

> Auto-generated from a Cloudflare Browser Rendering crawl.
> Page navigation stripped; per-page headings demoted two levels
> so original H2→H4, H3→H5 under each page section.

---

## Table of Contents

- [Overview](#sec-overview)
  - [Welcome to the Onshape Developer Documentation](#pg-docs)
- [API Introduction](#sec-api-introduction)
  - [Introduction to the Onshape REST API](#pg-docs-api-intro)
  - [Architecture](#pg-docs-api-intro-architecture)
  - [API Explorer](#pg-docs-api-intro-explorer)
  - [Quick Start](#pg-docs-api-intro-quickstart)
  - [Why Onshape?](#pg-docs-api-intro-whyonshape)
- [Authentication](#sec-authentication)
  - [Authentication](#pg-docs-auth)
  - [API Keys](#pg-docs-auth-apikeys)
  - [API Limits](#pg-docs-auth-limits)
  - [OAuth](#pg-docs-auth-oauth)
- [API Guides (Advanced)](#sec-api-guides-advanced)
  - [API Guides](#pg-docs-api-adv)
  - [Associativity](#pg-docs-api-adv-associativity)
  - [Billing](#pg-docs-api-adv-billing)
  - [Configurations](#pg-docs-api-adv-configs)
  - [Documents](#pg-docs-api-adv-documents)
  - [Drawings](#pg-docs-api-adv-drawings)
  - [Response Codes](#pg-docs-api-adv-errors)
  - [Features](#pg-docs-api-adv-featureaccess)
  - [Evaluating FeatureScript](#pg-docs-api-adv-fs)
  - [Metadata](#pg-docs-api-adv-metadata)
  - [Release Management](#pg-docs-api-adv-relmgmt)
  - [Import & Export](#pg-docs-api-adv-translation)
- [App Development](#sec-app-development)
  - [App Development](#pg-docs-app-dev)
  - [Client Messaging](#pg-docs-app-dev-clientmessaging)
  - [Extensions](#pg-docs-app-dev-extensions)
  - [Structured Storage](#pg-docs-app-dev-structuredstorage)
  - [Webhooks](#pg-docs-app-dev-webhook)
- [App Store](#sec-app-store)
  - [Onshape App Store](#pg-docs-app-store)
  - [Launch Checklist](#pg-docs-app-store-checklist)
  - [Quality Considerations](#pg-docs-app-store-quality)
  - [Testing Guidelines](#pg-docs-app-store-testingguidelines)
- [Tutorials](#sec-tutorials)
  - [Sample Apps](#pg-docs-tutorials)
  - [Create an Extension](#pg-docs-tutorials-createextension)
  - [glTF Viewer](#pg-docs-tutorials-gltf)
- [Help](#sec-help)
  - [Get Help](#pg-docs-help)
- [Changelog](#sec-changelog)
  - [Changelog](#pg-docs-changelog)

---

<a id="sec-overview"></a>
## Overview

<a id="pg-docs"></a>
### Welcome to the Onshape Developer Documentation

_Source: <https://onshape-public.github.io/docs/>_

Welcome to the Onshape Developer Documentation. You can find resources here for developing applications that integrate with Onshape. Use the navigation bar on the left to navigate through the documentation.

* New to Onshape? See the [Onshape Architecture guide](https://onshape-public.github.io/docs/docs/api-intro/architecture).
* New to REST APIs? Continue to the [API Introduction](https://onshape-public.github.io/docs/docs/api-intro/) page.
* Ready to develop your first Onshape app? Start with our [Quick Start](https://onshape-public.github.io/docs/docs/api-intro/quickstart) section.
* Already a pro? Head right over to the [Onshape API Explorer](https://cad.onshape.com/glassworks/explorer/#/).  
   * Use `https://companyName.onshape.com/glassworks/explorer` for Enterprise accounts.
* Looking to share your app with others? Check out our [App Store](https://onshape-public.github.io/docs/docs/app-store) documentation.
* Stuck? Check out our [Get Help](https://onshape-public.github.io/docs/docs/help) section.

---

###### [Introduction to the Onshape REST API](https://onshape-public.github.io/docs/docs/api-intro/)

###### [Authentication](https://onshape-public.github.io/docs/docs/auth/)

###### [API Guides](https://onshape-public.github.io/docs/docs/api-adv/)

###### [App Development](https://onshape-public.github.io/docs/docs/app-dev/)

###### [Onshape App Store](https://onshape-public.github.io/docs/docs/app-store/)

###### [Sample Apps](https://onshape-public.github.io/docs/docs/tutorials/)

###### [Get Help](https://onshape-public.github.io/docs/docs/help/)

###### [Changelog](https://onshape-public.github.io/docs/docs/changelog/)

---

<a id="sec-api-introduction"></a>
## API Introduction

<a id="pg-docs-api-intro"></a>
### Introduction to the Onshape REST API

_Source: <https://onshape-public.github.io/docs/api-intro/>_

This page explains the basics of using the Onshape REST API. If you are brand new to using APIs, we suggest you spend some time learning the basics from these free resources:

* <https://docs.github.com/en/rest/guides/getting-started-with-the-rest-api>
* <https://www.freecodecamp.org/news/apis-for-beginners/>

#### Videos & Courses

In addition to following along with the instructions on this page, you can also watch our _Intro to the Onshape API_ videos below, or view the full course content in the [Onshape Learning Center](https://learn.onshape.com/learn/course/intro-to-the-onshape-api/intro-to-the-onshape-api/what-is-an-api?page=1).

---

##### What is an API?

**Video Key Takeaways**

* _Onshape is cloud-native; no files._
* _You can access your Onshape data through the Onshape product interface, or using an API._
* _APIs are common tools for cloud-based systems to communicate._
* _Using the Onshape API can streamline many types of processes._

---

##### The Onshape Document Model

**Video Key Takeaways**

* _Onshape documents are data containers._
* _Onshape documents can contain parts, assemblies, subassemblies, drawings, and more._
* _Work within an Onshape document is organized into branches; each branch contains a workspace and may contain versions._
* _Onshape documents are organized into elements, such as Part Studios and assemblies._
* _An Onshape document URL can point to a specific document, workspace, version, or element._
* _Data security is Onshape’s highest priority._

---

#### REST APIs

Onshape uses REST APIs to communicate with clients and third-party systems. Onshape lives in your browser, which means you call REST APIs like you would any other web page. The API call returns information instead of a web page, and the response is formatted in JSON (JavaScript Object Notation).

You can use our REST APIs to access the Onshape engine and data in real time. We currently support three REST API requests (following the HTTP standards):

* `GET`: Retrieve (read) information from the server (i.e., your Onshape documents). Any arguments included in the URL are sent to the server.
* `POST`: Update (write) the server with new information. Required data is included in the request body.
* `DELETE`: Delete information from the server.

A typical REST API call in Onshape includes five major components:

* Method:  
   * `GET`, `POST`, or `DELETE`  
   * Every Onshape API endpoint is labeled with its method type.
* URL:  
   * Specifies the API endpoint and part of the document that the API is calling  
   * Uses the following format: `{base_url}/{fixed_url}`.  
         * `{base_url}`: Onshape URL (i.e., `https://cad.onshape.com/api` or `https://companyName.onshape.com/api` for Enterprise accounts).  
         * `{fixed_url}`: the URL of the API endpoint (more about this later)
* Query parameters:  
   * Optional parameters for the API call  
   * Described in the drop-down content of every endpoint in the API Explorer (you’ll learn about using our API Explorer in a later section).
* Headers:  
   * Defines the associated metadata, which is used by the server to process the request.  
   * Usually contains `Content-Type` and `Accept`.  
         * `Content-Type`:  
                  * Usually `application/json`  
                  * If the application downloads a file, `Content-Type` will be `application/octet-stream`  
         * `Accept`: found under `Media type` in the API response section on in the API Explorer.
* Payload body:  
   * Only applicable for `POST` requests  
   * Required for some `POST` requests; optional for others.  
   * Body template is available in the API drop-down in the API Explorer.  
   * Typically obtained and modified from the response of a related GET request (rather than manually)

##### Onshape API Request

Since Onshape is a web-based solution, it uses a URL to define what is loaded in the browser.

Example Onshape URL:`https://cad.onshape.com/api/` `documents/e60c4803eaf2ac8be492c18e/` `w/d2558da712764516cc9fec62/` `e/6bed6b43463f6a46a37b4a22`

* `https://cad.onshape.com/api` is the base URL of the document.  
   * Every Enterprise account has a custom base URL: `https://companyName.onshape.com/api`
* documents/ or d/ is followed by a 24-character document ID. The document ID uniquely identifies an Onshape document.
* Next, w/ is followed by a 24-character workspace ID. The workspace ID uniquely identifies a workspace within the document. By default, a document is started with the Main workspace.  
   * To refer to a specific document version, replace w/ with v/, followed by the 24-character version ID.  
   * With every edit made in the document, a microversion of every document is automatically created with every edit. To refer to a specific microversion, replace w/ with m/, followed by the 24-character microversion ID.  
   * **Note**: `POST` requests are always made to a workspace, since versions and microversions are immutable.
* e/ is followed by a 24-character element ID. The element ID uniquely identifies an element (e.g., a tab that we see and access through the user interface).

In this documentation, we often refer to the URL template as: `{base_URL}/{endpoint}/d/{did}/{wvm}/{wvmid}/e/{eid}` or sometimes `/{endpoint}/DWVME/` for short.

When your application is instantiated in a document, it is called with a URL like this:

```
https://_your-server.your-domain.com_?documentId=e60c4803eaf2ac8be492c18e&workspaceId=d2558da712764516cc9fec62&elementId=6bed6b43463f6a46a37b4a22&server=https%3A%2F%2Fcad.onshape.com&userId=53da35fbe4b0412c60b5e3b7&access=edit&debug=true

```

The query parameters passed from Onshape to your application are:

| Parameter                              | Description                                                                                                                                                                                              |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| documentId                             | Current document ID                                                                                                                                                                                      |
| workspaceId, versionId, microversionId | Current workspace ID OR version ID OR microversion ID                                                                                                                                                    |
| elementId                              | Current (application) element ID                                                                                                                                                                         |
| server                                 | The address of the current Onshape server. The server parameter is informational; REST requests should always be sent to cad.onshape.com. Enterprise accounts should be sent to companyName.onshape.com. |
| userId                                 | Current user ID, which can be found by calling /api/users/current and obtaining the user ID from the id field.                                                                                           |
| access                                 | Set to edit if the document should open with edit capabilities.                                                                                                                                          |

##### Onshape API Response

The REST API in Onshape communicates data in JSON format. If you are new to working with JSON, we recommend the following resources:

* <https://www.w3schools.com/js/js%5Fjson%5Fintro.asp>
* <https://www.freecodecamp.org/news/what-is-json-a-json-file-example/>

The example below is the response from calling the `getDocument` API for [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/6bed6b43463f6a46a37b4a22). A lot of information is returned, so we’ve truncated the middle of the response below, but if we look at the very end of the resulting JSON, we can see that the response has correctly returned `Onshape API Guide` as the document `name`.

`  {
    "jsonType": "document",
    "documentThumbnailElementId": "",
    "isUpgradedToLatestVersion": true,
    "public": false,
    "permission": "FULL",
    "isOrphaned": false,
    "recentVersion": null,
    // ...
    "isEnterpriseOwned": false,
    "resourceType": "document",
    "name": "Onshape API Guide",
    "id": "e60c4803eaf2ac8be492c18e",
    "href": "https://cad.onshape.com/api/v6/documents/e60c4803eaf2ac8be492c18e"
}
`

The Onshape API response also contains the following information:

* `X-Rate-Limit-Remaining` header: The number of times you are allowed to call this particular endpoint within an Onshape-defined time period.  
   * See [Response Codes: 429](https://onshape-public.github.io/docs/api-intro/docs/api-adv/errors#429-too-many-requests) for information on handling rate limits.  
   * See [API Limits](https://onshape-public.github.io/docs/api-intro/docs/auth/limits) for more information on plan-level limits.
* `X-Deprecated` header: Indicates the API has been deprecated. See the [Changelog](https://onshape-public.github.io/docs/api-intro/docs/changelog) for recommended alternatives.

#### API Conventions

The Onshape API generally uses the following conventions:

* Onshape generally supports only 3 methods: `GET` for read-only operations, `POST` for write operations, and `DELETE` for deletions. Onshape does not currently support other methods, such as `PUT`.
* Strings should be UTF-8 encoded.
* Query parameters are used for optional parameters. All required parameters are included in the path. For brevity, we use the following upper case letters in path definitions in this document:  
   * `D` Document ID (24-characters)  
   * `W` Workspace ID (24-characters)  
   * `V` Version ID (24-characters)  
   * `M` Microversion ID (24-characters)  
   * `E` Element ID (24-characters)
* The general form of a path is `/resource/context/subresource`. When present, the context identifies the document (D), the workspace, version or microversion (WVM), and the element (E). See the [Onshape Architecture](https://onshape-public.github.io/docs/api-intro/docs/api-intro/architecture) page for more information on Onshape’s basic API structure.
* Our intention is to provide `Workspace`, `Version`, and `Microversion` forms for all appropriate `GET` operations. `POST` will always be to a `Workspace`, as `Versions` and `Microversions` are immutable. Not all forms of all interfaces are implemented at this time.
* As of this writing, some API calls return information that is of use only for Onshape clients. You should generally only use the fields that are documented for external use. The internal data may be changed or removed without notice.

##### Versioning

All endpoint calls are versioned. The version string is inserted directly after the `/api/` path component. For instance, `https://cad.onshape.com/api/v6/documents/e60c4803eaf2ac8be492c18e` indicates a `version 6` request to the Onshape `getDocument` endpoint.

Calls within a version are compatible with one another; typically this means that a GET request can be fed back in as a POST at the same version. Versions are incremented whenever Onshape introduces a non-backwards-compatible change. Onshape users should always refer to the latest version in their calls. If no version is specified, the oldest version (`v0`) will be used.

##### Unit Designators

The following strings are valid unit designators:

For length measures:

* `meter`, `meters`, `m`
* `millimeter`, `millimeters`, `mm`
* `centimeter`, `centimeters`, `cm`
* `inch`, `inches`, `in`
* `foot`, `feet`, `ft`
* `yard`, `yards`, `yd`

For angular measures:

* `degree`, `degrees`, `deg`
* `radian`, `radians`, `rad`

#### What Now?

Continue on to our [API Explorer](https://onshape-public.github.io/docs/api-intro/docs/api-intro/explorer) page to learn about about navigating the Onshape APIs in our Glassworks API Explorer.

---

###### [API Explorer](https://onshape-public.github.io/docs/api-intro/docs/api-intro/explorer/)

###### [Quick Start](https://onshape-public.github.io/docs/api-intro/docs/api-intro/quickstart/)

###### [Architecture](https://onshape-public.github.io/docs/api-intro/docs/api-intro/architecture/)

###### [Why Onshape?](https://onshape-public.github.io/docs/api-intro/docs/api-intro/whyonshape/)

---

<a id="pg-docs-api-intro-architecture"></a>
### Architecture

_Source: <https://onshape-public.github.io/docs/api-intro/architecture/>_

Design in Onshape typically beings with a document, which is the container that includes all content related to a specific design. All data in an Onshape document is stored in Elements. Part Studios and Assemblies are two of the most common element types in a design. Throughout the design process, creating versions can be useful for product development management while working on the “Main” workspace. See also:

* The [API Introduction](https://onshape-public.github.io/docs/api-intro/architecture/docs/api-intro/) page for information on how documents, workspaces, and elements are assembled into a URL.
* The [Associativity](https://onshape-public.github.io/docs/api-intro/architecture/docs/api-adv/associativity) page for information on how Parts, Assemblies, and Elements relate to each other.

#### Elements

All data in an Onshape document are stored in Elements (represented as tabs in the user interface). Onshape documents contain five kinds of elements:

* **Part Studio**: Contains zero or more parts
* **Assembly**: Contains zero or more parts or assemblies
* **Blob** (Binary Large OBject): Can be provided by a partner or by the end user. For example, the user can upload a PDF file, an image, or a text file. Partner applications can store arbitrary data, but we recommend using the [structured storage](https://onshape-public.github.io/docs/api-intro/architecture/docs/app-dev/structuredstorage) available in an element for better integration.
* **Application**: Presents an iframe to the user. The user interface is managed by a server that can be provided by a third-party. Onshape Drawings are a special case of an application element.
* **Feature Studio**: Contains the definition for Onshape Features, which are defined in FeatureScript.

#### Workspaces, Versions, and Microversions

A document is stored in Onshape as a collection of changes.

* You can think of a **workspace** as a branch of the document, similar to a branch in a source control system. Documents can be branched to create new workspaces.
* Each individual change to the document creates a new document **microversion**. As the document is edited, changes are applied to the active workspace, creating new microversions.
* Periodically, the user may designate versions of the document. A **version** is a named snapshot of the entire document at some point in time (that is, at some microversion).

You cannot change a version or microversion of a document; all changes are applied to a workspace (and create a new microversion). Thus, while in general the `GET` methods of the API can read from a version, microversion, or workspace, the `POST` methods generally require a workspace, and create a new microversion when data is written to the document. (An exception is that it is possible to set metadata within a version; this does not create a new microversion).

The following IDs are used by many of the APIs. Each ID (except for Geometry IDs such as Part, Face and Edge) is a 24-character string that is used internally by Onshape to uniquely identify the resource. The Geometry IDs are variable-length strings used to resolve to a specific geometric entity within a model.

| ID                        | Description                                                                                                                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **User ID**               | Identifies a single user.                                                                                                                                                            |
| **Document ID**           | Identifies a document. The logged-in user must have access to the requested document for the API to succeed.                                                                         |
| **Workspace ID**          | The Workspace ID identifies a workspace within the document. Workspaces are used to distinguish between different branches of the document.                                          |
| **Version ID**            | The Version ID identifies a specific named version.                                                                                                                                  |
| **Microversion ID**       | The Microversion ID identifies an internal revision of the document.                                                                                                                 |
| **Element ID**            | The Element ID identifies an element within the document.                                                                                                                            |
| **Part IDFace IDEdge ID** | The Part ID identifies a part within a part studio. The Part ID should generally not be stored for long-term use, as it is only expected to be valid during the course of a session. |

Note that a Part ID may reference a part that no longer exists if the model is changed, so it is best to specify a Version or Microversion to pick the context for the Part ID. Note that even with the Version or Microversion, internal changes to the Onshape system may also change the Part ID. Onshape provides mechanisms for maintaining persistent references. See the [Associativity](https://onshape-public.github.io/docs/api-intro/architecture/docs/api-adv/associativity) page for more information. Face and Edge IDs are used in similar ways.

The following table identifies Onshape concepts and the corresponding Git concepts. Note that this is not a direct mapping, and the implementation of the concepts is very different.

| Onshape concept | Git concept |
| --------------- | ----------- |
| Document        | Repository  |
| Element         | File        |
| Workspace       | Branch      |
| Version         | Tag         |
| Microversion    | Commit      |

#### Linked Documents

Although a document can contain a complex model tree involving many Part Studio and Assembly elements, it is often more efficient to split the content into multiple documents. Connections between documents always refer to a specific version of the target document. _Once a version is used as the target of a linked document, that document version is preserved as long as any document references it, even if the containing document is deleted._ Additionally, any user that has access to the referring document will have limited read access to the target document, regardless of what permissions are currently on the target document.

#### Configurations

Onshape Part Studios can be constructed to be configurable using Onshape Configurations. API calls that reference Part Studios (primarily within the [Parts](https://cad.onshape.com/glassworks/explorer/#/Part) and [Part Studios](https://cad.onshape.com/glassworks/explorer/#/PartStudio) APIs) often accept a `configuration` parameter that identifies what specific configuration of the Part Studios is being referenced. When not specified, the API implementation typically uses the configuration that is currently selected within the Part Studio. An interactive ad-hoc API call might not behave consistently in an application, so be sure to specify the configuration parameter where applicable.

#### Onshape Data Model

Onshape data is stored in replicated databases in the cloud. The Onshape data model is influenced by the Git data model and similar source code repositories.

Documents contain **elements**. Elements are presented as tabs in the user interface. With some exceptions, all data in a document is stored within an element. The following table describes what data stored in each Element type:

| Element Type    | Description                                                                                                                                                                                                                                                                                                          |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Part Studio** | Each Part Studio contains exactly one Feature list. The Feature list contains Features such as sketches, planes, extrudes, etc. Each Feature contains one or parameters. Whenever the Feature list changes, the parametric history is evaluated, and the model is regenerated.                                       |
| **Assembly**    | Each Assembly contains an assembly tree, which contains parts and/or other assemblies (sub-assemblies), along with mate information. Onshape provides an API call to retrieve the assembly tree definition.                                                                                                          |
| **Blob**        | Each Blob element contains an uninterpreted binary object that has been uploaded to Onshape, typically from a file. Onshape depends on the browser client to display some blob data (e.g., PDF and image data), but does not interpret the data. A blob element can be updated with new data.                        |
| **Application** | Each Application element contains zero or more sub-elements, providing a structured set of transactional data that is defined and managed by an application. Application data can be displayed in the Onshape tab in an iframe; the application is responsible for rendering the data in the iframe from its server. |

Note that Onshape Drawing elements are Application elements managed by Onshape.

Tessellated data is not stored persistently in Onshape; it is generated on demand for display by the Onshape clients, or in response to application REST API requests. This data may be cached for performance.

##### Document data

All elements, including Assemblies, Part Studios, Drawings, or even apps, are history based. Each change to an element or set of elements represents a unique record in the document’s history, known as a microversion. The document can be restored to that particular state any time in the future.

##### Part Studio data

The Part Studio element is defined by a list of features, some of which (e.g., a sketch), may have a complex internal structure composed of entities. Part Studio features and entities are referenced by unique persistent identifiers. Part Studio features and entities can appear, disappear, and reappear depending on the current microversion of the model.

##### Assembly data

The Assembly element is defined as a list of assembly features and a tree of subassemblies/part instances. Occurrence ID is a unique persistent identifier of an occurrence of a part in the assembly structure.

##### External application data

An external application has complete control over how it manages/stores documents, however, to take advantage of the Onshape data model, there is a set of endpoints they should use to store state. These are collectively known as the AppElement API.

##### Model presentation data

A valid model definition usually corresponds to a real-world manufacturable topology, represented internally as a set of parts, faces, edges, and vertices and the set of relations between them. Each of these has a unique identifier in every state of the model. The identifier represents an encoded index in the model’s history, and its value depends on the structure of the model’s history. The value is not guaranteed to be preserved across model changes, and will almost always change if the model changes in significant ways. The model can be tessellated into a set of geometric primitives, which approximate the shape of the model. Tessellated data can be used for visual representation of the model or other processing related to the shape of the model.

The following changes in the topological representation can occur between two microversions of the model:

* New topological entities appear
* Id of existing topology change
* Topological entities disappear
* Existing topological entities are merged into a single entity
* Existing topological entity are split into multiple entities

The model microversion and topology ID can be used to identify topological entities across the model changes. Topology ID defined in a specific microversion can be translated into a set of topology IDs in the current microversion of the model. (The Topology ID is sometimes referred to as a Deterministic ID within Onshape, and is exposed in specific API calls as partId, faceId, etc.). See the [PartStudio APIs](https://cad.onshape.com/glassworks/explorer/#/PartStudio) to see what topology IDs are exposed.

---

<a id="pg-docs-api-intro-explorer"></a>
### API Explorer

_Source: <https://onshape-public.github.io/docs/api-intro/explorer/>_

We document all available Onshape REST API endpoints in our Glassworks API Explorer:

**<https://cad.onshape.com/glassworks/explorer/>**

#### Videos & Courses

You can also watch our API Explorer instructional video below, or view the full course content in the [Onshape Learning Center](https://learn.onshape.com/learn/course/intro-to-the-onshape-api/executing-a-get-request/glassworks-api-explorer?page=1). Additional example videos are embedded throughout this page.

---

##### Glassworks API Explorer

**Video Key Takeaways**

* _Onshape API endpoints are accessible through the [Glassworks API Explorer](https://cad.onshape.com/glassworks/explorer/#%5Fga=2.42102053.182342821.1729623970-505580682.1727441539)._
* _Glassworks endpoints are organized into sections._
* _Glassworks allows GET, POST, and DELETE requests._

---

#### Authenticate

You can authenticate in the API Explorer in one of three ways:

1. **Onshape**:  
   1. Open Onshape in a new tab in your browser.  
   2. Sign in with your Onshape credentials. Onshape will pass your credentials to the API Explorer.
2. **API Keys**:  
   1. Click **Authorize** in the top-right of the API Explorer page and scroll to the bottom of the dialog.  
   ![Glassworks Authorize button](https://onshape-public.github.io/docs/api-intro/explorer/images/glassworks-auth-button.png)  
   2. Provide your API access key in the Username field and your secret key in the Password field. See [API Keys](https://onshape-public.github.io/docs/api-intro/explorer/docs/auth/apikeys) for help creating your API Keys. Do NOT enter your Onshape credentials.  
   ![drawing](https://onshape-public.github.io/docs/api-intro/explorer/images/ApiExplorerBasicAuth.png)  
   3. Click **Authorize**, and then click **Close**.
3. **Oauth**:  
   1. Click **Authorize** in the top-right of the API Explorer page.  
   ![Glassworks Authorize button](https://onshape-public.github.io/docs/api-intro/explorer/images/glassworks-auth-button.png)  
   2. Fill out the OAuth fields. See [OAuth](https://onshape-public.github.io/docs/api-intro/explorer/docs/auth/oauth) for more information on authenticating with OAuth2.  
   3. Click **Authorize**, and then click **Close**.

#### Make a GET request

This API Explorer site enables you to run API requests directly within its interface and provides the output from the API call. To try an endpoint in the API Explorer, follow these steps or follow along with the video below:

1. Open this public Onshape document in your browser:<https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/6bed6b43463f6a46a37b4a22>
2. Open the API Explorer in a new browser tab: <https://cad.onshape.com/glassworks/explorer/>  
   * Note: For Enterprise accounts, substitute `cad` in this URL with your company name.
3. Scroll down to [Document](https://cad.onshape.com/glassworks/explorer/#/Document).
4. Click to expand the [getDocument](https://cad.onshape.com/glassworks/explorer/#/Document/getDocument) endpoint. (Hint: it appears in the API Ref as `GET /documents/{did}`).
5. Go back to the public document you opened in Step 2, and copy the document ID from the Onshape URL (`e60c4803eaf2ac8be492c18e`).![image](https://onshape-public.github.io/docs/api-intro/explorer/images/OnshapeAPIGuidePublicDoc.png)
6. Paste the document ID into the `did` field in the API Explorer.  
   * Note: If you can’t edit the `did` field, click the **Try it out** button. This will toggle to a **Cancel** button when the fields are editable.
7. Scroll down and click **Execute**.  
   * Note: If you receive a `403` error, see the [Authenticate](#authenticate) section for help.
8. Scroll to the bottom of the 200 response body. We have correctly returned `Onshape API Guide` as the document name.

> **IMPORTANT NOTE**: The documentation in the API Explorer reflects the supported interface. Some API calls may, for historical reasons, return additional undocumented fields. Unless the return fields are documented in the API Explorer, you should NOT use them, as they may be removed without warning. Your application should always ignore unexpected or undocumented return data. Onshape reserves the right to add, remove or change any undocumented fields.

---

##### Video example: GET Request

**Video Key Takeaways**

* _A GET request to the `/documents/{did}` will contain a lot of information about the particular document._
* _The thumbnail section contains thumbnail images of the document in several different sizes._
* _Document ID for this example: `7f718ac6ad66ac140097429b`_

---

#### Make a POST request

1. Make a copy of [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/6bed6b43463f6a46a37b4a22), and make a note of the copied document and workspace IDs in the URL.
2. In the Glassworks API Explorer, expand the [createAssembly](https://cad.onshape.com/glassworks/explorer/#/Assembly/createAssembly) endpoint. Note that in addition to URL parameters, this endpoint takes a request body. Like in the GET request, the URL parameters tell Onshape which document you’re working with. But instead of returning information about the document in the response, we will POST the data in the request body to the document.  
   1. Enter the document ID from your copied document into the `did` field.  
   2. Enter the workspace ID from your copied document into the `wid` field.  
   3. In the request body, specify a name for your Assembly by supplying a string in the `name` field. In this example, we’ll call it `myNewAssembly`.  
   ```  
   {  
       "name": "myNewAssembly"  
   }  
   ```
3. Click **Execute**.  
   * Note: If you receive a `403` error, see the [Authenticate](#authenticate) section for help.
4. Return to your copied document and observe that the new assembly tab has been added.  
![new assembly tab in the copied api guide document](https://onshape-public.github.io/docs/api-intro/explorer/images/assemblies-createAssemblyTab-01.png)

---

##### Video example: POST Request

**Video Key Takeaways**

* _POST requests send data to the Onshape servers with the intent of updating information._
* _POST requests usually include data in JSON format, sent in the request body._

---

#### Use the Auto-fill feature

1. Copy the URL of this drawing:<https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/15b07287508246ccd038e31e>
2. Expand the [getDrawingTranslatorFormats](https://cad.onshape.com/glassworks/explorer/#/Drawing/getDrawingTranslatorFormats) endpoint in the API Explorer.
3. Paste the URL into the `Onshape URL` field.
4. Click **Auto-fill**. The document ID, workspace ID, and element ID are pushed from the URL into the correct fields.
5. Confirm all fields are filled out as expected. Not every parameter can be extracted from an Onshape URL, so there may be more fields to fill out.  
![the autofill button copies document ids into their respective parameter fields in glassworks](https://onshape-public.github.io/docs/api-intro/explorer/images/explorer-autofill.png)

#### View response body docs

1. Expand the endpoint you want to use the in API Explorer.
2. Scroll down to the Responses section.
3. Click Schema.
4. Click the `[...]` symbols to expand the docs for the response JSON.

![glassworks api explorer response json docs](https://onshape-public.github.io/docs/api-intro/explorer/images/APIExplorerResponseJSON.png)

#### View request body docs

1. Expand the endpoint you want to use the in API Explorer.
2. **Click the _Cancel_ button to make the schema viewable.**
3. Click Schema.
4. Click the `[...]` symbols to expand the docs for the response JSON.

![glassworks api explorer response json docs](https://onshape-public.github.io/docs/api-intro/explorer/images/APIExplorerRequestJSON.png)

#### Copy a cURL

1. Expand the endpoint you want to use in the API Explorer.
2. Fill out the parameter fields.
3. Click Execute in the API Explorer.
4. Copy the curl from the Curl field.

![api explorer curl copy](https://onshape-public.github.io/docs/api-intro/explorer/images/APIExplorerCopyCurl.png)

#### Upload a file

1. In the endpoint’s **Request body** section, click the **Choose file** button.
2. Navigate to the location of the file to upload and select it. The filename appears in the field.![file has been uploaded to glassworks and filename appear in request body field](https://onshape-public.github.io/docs/api-intro/explorer/images/glassworks-file-upload-01.png)
3. Optionally, to remove the file, double-click the filename and choose **Cancel** in the dialog. The filename is removed from the field, and the **Send empty value** option is selected.![file has been removed from request body field](https://onshape-public.github.io/docs/api-intro/explorer/images/glassworks-file-empty-01.png)

#### Troubleshooting

* If the parameter fields in the API Explorer are grayed out, click the **Try it Out!** button to toggle it to a **Cancel** button. The parameter fields should become editable.
* If you can’t see the request body JSON docs, click the **Cancel** button to toggle it back to the **Try it Out!** button.
* If you see authentication issues, review the [Authenticate](#authenticate) section above.

---

<a id="pg-docs-api-intro-quickstart"></a>
### Quick Start

_Source: <https://onshape-public.github.io/docs/api-intro/quickstart/>_

In this example, we will call an Onshape REST API endpoint to send a document name to our console. We highly recommend completing the Learning Center’s [Intro to the Onshape API](https://learn.onshape.com/learn/course/intro-to-the-onshape-api/intro-to-the-onshape-api/what-is-an-api?page=1) course and mastering using Onshape APIs within the Glassworks Explorer before moving on to creating scripts and apps. Please note that the sample shown on this page is only designed to be used as a quick start guide and does not represent a full Onshape application.

---

#### Code Snippets

* python
* cURL
* Javascript
* C++

`` import requests 
import json

### Assemble the URL for the API call 
api_url = "https://cad.onshape.com/api/v10/documents/e60c4803eaf2ac8be492c18e"

### Optional query parameters can be assigned 
params = {}

### Use the keys from the developer portal
access_key = "ACCESS_KEY"
secret_key = "SECRET_KEY"

### Define the header for the request 
headers = {'Accept': 'application/json;charset=UTF-8;qs=0.09',
           'Content-Type': 'application/json'}

### Putting everything together to make the API request 
response = requests.get(api_url, 
                        params=params, 
                        auth=(access_key, secret_key),
                        headers=headers)

### Convert the response to formatted JSON and print the `name` property
print(json.dumps(response.json()["name"], indent=4))
 ``

`curl -X 'GET' \
https://cad.onshape.com/api/v10/documents/e60c4803eaf2ac8be492c18e \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \
  -H 'Authorization: Basic CREDENTIALS' 
`

`` import fetch from 'node-fetch'; 

async function getDocument(url='') {
    const response = await fetch(url, {
      method: 'GET', 
      headers: {
        'Content-Type': 'application/json', 
        Accept: 'application/json;charset=UTF-8;qs=0.09', 
        Authorization: `Basic ${btoa('CREDENTIALS')}`
      }
    });
    return response.json(); 
}

getDocument('https://cad.onshape.com/api/v10/documents/e60c4803eaf2ac8be492c18e'
).then((data) => {
    console.log(data.name); 
});
 ``

`#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int main() {
    string url = "curl ";

    url += "-X 'GET' "; 
    url += "'https://cad.onshape.com/api/v10/documents/e60c4803eaf2ac8be492c18e'"; 
    url += "-H 'accept: application/json;charset=UTF-8; qs=0.09' "; 
    url += "-H 'Authorization: Basic CREDENTIALS'"; 
    
    system(url.c_str());
    return 0; 
}
`

---

#### Quick Start Video

Watch the Onshape Quick Start video as you follow along with the steps on this page.

---

#### Quick Start Steps

##### System Requirements

* You must be signed in to your Onshape account at <https://cad.onshape.com> (or <https://companyName.onshape.com> for Enterprise accounts).
* This example is coded in Python. The equivalent code is provided in other languages at the end of the example. To follow along with this tutorial, you can download and install Python here: <https://www.python.org/downloads/>.

##### 1\. Review the API Endpoint

1. Go to the [API Explorer](https://cad.onshape.com/glassworks/explorer) and scroll to `Document`.
2. Expand the `GET /documents/{did}` endpoint. Note that in the URL, the name of this API is `getDocument`.
3. Make a note of the URL structure and the parameters required to make this request. This will become the fixed URL part of our API call.  
![image](https://onshape-public.github.io/docs/api-intro/quickstart/images/Glassworks_getDocument.png)  
For this endpoint, we only need to get the document ID from the document URL.
4. Scroll down and make a note of the `Media Type` that we’ll need to include in our header.  
![image](https://onshape-public.github.io/docs/api-intro/quickstart/images/Glassworks_MediaType.png)

##### 2\. Review the Document

Navigate to [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/6bed6b43463f6a46a37b4a22), and make a note of the document ID in the URL (`e60c4803eaf2ac8be492c18e`).  
![image](https://onshape-public.github.io/docs/api-intro/quickstart/images/OnshapeAPIGuidePublicDoc.png)

##### 3\. Create your API Keys

1. Go to <https://cad.onshape.com/appstore/dev-portal>.
2. In the left pane, click `API keys`.
3. Click the `Create new API key` button.
4. Select the following permissions for your app:  
   * `Application can read your documents.`  
   * `Application can write to your documents.`
5. Click the `Create API key` button.  
    
![image](https://onshape-public.github.io/docs/api-intro/quickstart/images/CreateNewAPIKey.png)
6. Copy both the **access key** and **secret key** from the pop-up window, save them somewhere, then click the `Close` button.  
**IMPORTANT NOTE: You will not be able to find the secret key again, so save it somewhere safe!**  
    
![image](https://onshape-public.github.io/docs/api-intro/quickstart/images/APIKeySecretKey.png)
7. The details for your application appear. We’ll refer to these strings as `ACCESS_KEY` and `SECRET_KEY` in this example.  
    
![image](https://onshape-public.github.io/docs/api-intro/quickstart/images/DevPortalKeys.png)
8. Some scripts might require that you base-64-encode your API keys. You’ll see either `ACCESS_KEY` and `SECRET_KEY` in the code examples below, or you’ll see `CREDENTIALS` to specify that the keys must be encoded before use. See [API Guide: API Keys](https://onshape-public.github.io/docs/api-intro/quickstart/docs/auth/apikeys#basic-authorization) for details.

##### 4\. Write Your Code

Follow along with the steps in this section to create the final code. This example uses python, but you can refer to the [code snippets](#code-snippets) at the top of this page for other languages.

1. Create a new file called `getDocInfo.py`.
2. Start your file by importing the necessary libraries.  
`import requests  
import json  
`
3. Next, define the URL for the API call:  
`# Assemble the URL for the API call  
api_url = "ASSEMBLED_URL"  
`
4. Replace `ASSEMBLED_URL` with the fully formed API. This is where we’ll put together everything we’ve learned so far:  
   1. The base URL:  
         * `https://cad.onshape.com/api`  
         * `https://companyName.onshape.com/api` for Enterprise accounts  
   2. The fixed URL is specified in the [getDocument](https://cad.onshape.com/glassworks/explorer/#/Document/getDocument) API in Glassworks: `/documents/{did}`  
   3. The document ID parameter from the public document URL to include in the fixed URL: `{did}: e60c4803eaf2ac8be492c18e`  
   4. Together, this makes the URL for our API request:`https://cad.onshape.com/api/v10/documents/e60c4803eaf2ac8be492c18e`
5. We don’t need to send any optional parameters with our request, so we can define them as an empty object:  
`# Optional query parameters can be assigned  
params = {}  
`
6. Now let’s add variables to represent our access and secret keys. Make sure to replace `ACCESS_KEY` and `SECRET_KEY` with your strings from the dev portal.  
`# Use the keys from the developer portal  
access_key = "ACCESS_KEY"  
secret_key = "SECRET_KEY"  
`
7. Next, define your headers:  
`# Define the header for the request  
headers = { 'Accept': 'MEDIA_TYPE',  
            'Content-Type': 'application/json'  
        }  
`
8. Replace `MEDIA_TYPE` with the Media type we obtained from the API Explorer during the Review the API section above:  
`'Accept': 'application/json;charset=UTF-8;qs=0.09',  
`
9. Put all the variables you just defined together into the request. The requests library implements Basic Authorization using the supplied API keys.  
`# Put everything together to make the API request  
response = requests.get(api_url,  
                    params=params,  
                    auth=(access_key, secret_key),  
                    headers=headers)  
`
10. And finally, print the name value from the response:  
`` # Convert the response to formatted JSON and print the `name` property  
print(json.dumps(response.json()["name"], indent=4))  
 ``
11. Make sure your file matches the full example shown at the beginning of this section.

##### 5\. Run Your Code

1. Open your terminal/command prompt and navigate into the folder where you saved your `getDocInfo.py` file:  
   * MacOS  
   * Windows  
`cd ~/<your-path>  
`  
`cd \<your-path>  
`
2. Install the necessary modules. If you have `pip` installed on your machine, you can run `pip install requests` instead.  
   * MacOS  
   * Windows  
`python3 -m pip install requests  
`  
`py -m pip install requests  
`
3. Run your code:  
   * MacOS  
   * Windows  
`python3 getDocInfo.py  
`  
`py getDocInfo.py  
`
4. Confirm that your console displays:  
`"Onshape API Guide"  
`

---

<a id="pg-docs-api-intro-whyonshape"></a>
### Why Onshape?

_Source: <https://onshape-public.github.io/docs/api-intro/whyonshape/>_

#### Why Onshape?

As long as there have been applications that manage organizational data into a database, there has been a need to share that data between different departments and therefore, usually, different systems. In a typical design/manufacturing organization, there could be at least four or five mission-critical databases that manage the data for different departments and for different stages in the product’s lifecycle.

Initially, these systems provide the capabilities required by their consumers (i.e., the departments that use these systems). For instance, the Finance might use QuickBooks, Manufacturing might use a manufacturing planning and execution system (MES), Engineering might use a Product Data management System (PDM), and so on for each group in the organization.

This often leads to disparate silos of data and knowledge. The departments in an organization do not work in a vacuum; each is dependent on information generated by other groups. For instance, Manufacturing can’t produce accurate assembly instructions without input from engineering on the designs and the bill of materials. Finance can’t price the product without understanding its contents and which parts are manufactured in-house or purchased.

Therefore, the need to integrate these systems becomes critical for the organization to function optimally. Initially, connecting one system to another can be a straightforward process. This usually involves some services to get the systems to talk to each other, however it isn’t too painful as long as the requirements are clearly defined.

Anyone who has implemented integrations between PLM (Product Lifecycle Management) systems or ERP (Enterprise Resource Planning) systems will tell you of the nightmare scenarios they encountered. Often this is the result of poorly scoped and defined requirements, conflicting requirements coming from multiple departments, and the many integration points required between systems. The result is that the organization is not getting what it wants or needs, the customer is paying for services that do not provide the promised solution, and usually the project is long overdue. All this equals an unhappy customer and often the software vendor’s solutions are blamed for the disaster.

Over the years, many technologies have appeared (and some of them, just as quickly disappeared) to enable integration without the need to write thousands of lines of custom code that needs to be re-written for every software upgrade. Several technologies provide “codeless” integration between SaaS products ([Zapier](https://zapier.com/), for example). These solutions are particularly good for generic use cases for data exchange between systems, but can be limited when it comes to custom modifications to the data being sent that might be required by a specific customer. In addition, they have the overhead of requiring a subscription to their service. Sending corporate IP through another third-party can also cause data security issues.

Therefore, we can understand that in most organizations integration between systems is a necessary evil that must be tackled, either with an out-of-the-box solution or through some custom coding.

Early on, Onshape understood that as an engineering system, it cannot exist in a vacuum; it must be able to communicate with other systems. For this reason, the REST API was developed.

An API, or _application programming interface_, is a set of rules that define how applications or devices can connect to and communicate with each other. A REST API is an API that conforms to the design principles of the REST, or _representational state transfer architectural style. For this reason, REST APIs are sometimes referred to RESTful APIs._

#### Onshape SaaS

Onshape was built from the ground up as a true SaaS-based system; Onshape had no investment in legacy code and was able to develop an application that truly runs as a multi-tenant SaaS solution from the first line of code. Many companies claim to run cloud-based solutions, but since they have such a large investment in their legacy code, that they can’t just discard and start again from scratch. Instead, they tend to try and port that code to the web.

More often than not, porting existing code to the web and calling it a SaaS solution is no more than a marketing ploy; it isn’t a true SaaS solution if it wasn’t written as one. These are generally known as cloud-hosted solutions. This means that a typical three-tier data management solution (which could have previously been installed on a set of servers), has now been modified to be hosted on the web.

##### Traditional three-tier architecture

Traditional PLM systems typically use a three-tier architecture, mainly consisting of an application server, a database server, and a client (either a web client or a thick client installed on the client hardware).

![The 3-tier architecture | Download Scientific Diagram](https://onshape-public.github.io/docs/api-intro/whyonshape/images/integrationguideimage10.png)

_Typical three-tier architecture_

To connect to and integrate with this architecture, APIs are usually exposed on the application or web server. If this architecture is ported to the web, it cannot make customizations through the API, since it would modify the behavior of the program for everyone connected to that application server.

##### Single- vs multiple-tenant architectures

The three-tier architecture is typical of most PLM solutions on the market today, which is fine if you want the solution to be installed on company servers and be accessible to people within the company only.

When this type of solution is ported to the web, software vendors typically must create a single-tenant application where an application server and a database server are provisioned for each new customer.

![Enterprise SaaS Architecture - The Why | Frontegg](https://onshape-public.github.io/docs/api-intro/whyonshape/images/integrationguideimage11.png)

_Single-tenant architecture_

In this case, the vendor must use expensive hardware to host more customers, which is not a sustainable model.

Modern 21st century software solutions use multi-tenant solutions that can be hosted on services such as Amazon cloud, Azure, etc. There are many benefits to this architecture, including that servers can be provisioned and decommissioned on the fly to provide ultimate performance whenever required. Since servers cost money, decommissioning servers when they are not required is a key benefit to a true SaaS solution.

![Saas Solutions - Multi-tenant vs multi-instance architectures](https://onshape-public.github.io/docs/api-intro/whyonshape/images/integrationguideimage12.png)

_Multi-tenant architecture_

Since each application is separate in this architecture, we can enable customizations that can’t be implemented in a single-tenant architecture. For example, we can provide access to the REST APIs that are required for Onshape integration. In the single-tenant architecture, if you provide API access to the application server, one customer will be modifying that application for all customers who are registered on that tenant.

#### The Onshape Difference

Onshape does not work like other legacy CAD systems. Onshape was built from scratch for the cloud and as a modern CAD system, so many of the failings of legacy CAD systems were excluded.

There are many differences and benefits to Onshape, which are well-documented in the Onshape Help and training materials.

The information in this section is specific to integrations, since Onshape does not behave like a traditional file-based systems. When writing an integration for Onshape, it is critical to understand the nuances in Onshape’s design practices and how data is organized in Onshape.

##### Data-driven/fileless

Most traditional PDM/PLM systems integrated with CAD systems enable this integration on a per-file basis. This means that you have an object in the PDM/PLM system that corresponds directly to a file in the CAD system. In this way, the PDM/PLM system can manage access to the files, build assemblies from the files, view the CAD data, and much more.

Onshape, however, does not work this way.

Being data-driven means that Onshape has no files, just data, so an integration into Onshape is going to look different from any integration to a CAD system that you might have done previously.

In traditional CAD, a single file represents a snapshot of what the design looked like at a specific moment in time. Unless it’s changed, it will remain in that state forever. PDM systems manage these files, and once a designer decides to make a revision or a release, the file is locked, and a new file can be created to represent any further updated versions or releases of the design. PDM/PLM systems are very good at managing this data in an up-to-date structure, but it does have the drawbacks. They generate many file copies of a specific design, and once a file is taken out from the system (for instance, to share with a supplier), it is no longer managed and tracked.

Onshape uses data instead of files. The data is always up-to-date and can be collaborated on in real-time without the need to send file copies back and forth. This means that Onshape views versions and releases differently than those traditional systems do. When integrating with Onshape, we must design for data rather than files.

Files can be generated from the Onshape data. For example, you can generate a PDF of a drawing upon release or of a STEP file that can be used by other downstream systems.

A key benefit of a data-driven system is the ability to retrieve detailed, real-time analytics. Onshape has comprehensive analytics; including who can view or edit a design, when and exactly what edits are made, which commands were used, and how long was spent modifying the design.

##### Built in PDM

Up until now, CAD was one software program, and PDM/PLM was another program that had to be integrated with the CAD. In many cases, both programs could be sold by the same software vendor (even though there are many PLM systems available that are sold by independent vendors who have no CAD system). Regardless, a PDM/PLM system always had to be an added solution to the CAD system.

No matter how deep the integration between a CAD system and a PLM system, there is always the need to sync data between the two. This is usually a weak point in any solution that is prone to errors.

Being data-driven, Onshape already has PDM built in as part of the CAD system. This is unique in the industry: CAD and PDM as part of the same solution with no additional piece of software required.

![A picture containing graphical user interface Description automatically generated](https://onshape-public.github.io/docs/api-intro/whyonshape/images/integrationguideimage14.png)

_Onshape’s revision and part number schema definition interface_

For instance:

* Since the **data is always up-to-date**, the correct state of any design is always represented in real-time with no delay for syncing between systems.
* Unlike file-based systems, **the data is never locked**; it is always available and always changing.
* PDM system **data management aspects are fully integrated** into every aspect of the CAD system.
* True **real-time collaboration/co-design** on both design and data is enabled.

So, what does this mean when it comes to integrating Onshape with another PLM system? First and foremost, we must understand that there are many things that a PLM system does that Onshape’s PDM capabilities can’t do. Integrating Onshape to a PLM system should augment the powerful capabilities already available inside Onshape, not necessarily replace them. Similarly, Onshape does not replace PLM-native capabilities. Instead, depending on the business case, we can use the best-in-class capabilities of each system to augment the other.

The Onshape release process is an example of the augmentation of each system’s capabilities. Onshape has a specific way of managing the release of data that is different from traditional PDM systems. This capability is inherently suited to a data-driven approach and provides a lot of value to the update of design data in Onshape. At the same time, PLM systems provide enterprise release processes that may include many people and different departments that extend beyond the engineering domain. Such PLM processes can be highly customized and suited to the organizations established business processes.

In this scenario, it doesn’t make sense to avoid the enterprise release processes in the PLM system. However, also omitting Onshape’s release capabilities could put data between Onshape and the PLM system out of sync and prevent Onshape from updating data (e.g., watermarks and title blocks on drawings, icons related the visualizing the state of data, etc.).

In this case, we want to use the best-in-class features of each software solution without compromising the capability provided by each solution. If we plan our integration correctly, this can be achieved by initiating the release of the data in Onshape, transferring the release data to the PLM system where the release process will be triggered, and finally automating the release in Onshape once the process has been completed in the PLM system.

##### Multi-part Part Studios

In traditional CAD systems, one file typically equals one part. While design-in-context is available in most CAD systems, and multiple solid bodies can be created, each part is self-contained in a separate file. For PLM systems, this makes it easy to associate an object in the PDM/PLM database with a specific CAD file. _This is not the case in Onshape._

In Onshape, parts are designed in what’s called a _Part Studio._ Within a Part Studio, the designer is free to create as many parts as they want. The general rule is that the parts should be related to each other in a system, thereby making it easier to design one part from another, however there is a lot of flexibility in how the designer wishes to work.

![A picture containing text Description automatically generated](https://onshape-public.github.io/docs/api-intro/whyonshape/images/integrationguideimage15.png)

_An example of a multi-part Part Studio in Onshape_

The structure of the Onshape document is discussed in detail in the [Onshape Architecture](https://onshape-public.github.io/docs/api-intro/whyonshape/docs/api-intro/architecture) page. The Part Studio is included in an Onshape document.

We can already begin to understand that the traditional CAD/PDM paradigm of “one file per object” will not work with Onshape; the designer would be forced by the PDM/PLM system to only create one part per Part Studio. This would therefore limit the designer’s freedom for creativity in Onshape and seriously reduce the powerful functionality available for the designer to use.

Therefore, we need to re-think how we integrate with Onshape versus how we integrate with traditional CAD systems. Fortunately, Onshape’s REST API supports the multi-part Part Studio scenario. Instead of associating a file with an object in the PDM/PLM database, we now use the REST API to associate a Part with its corresponding object.

##### Versions and releases

Traditional PDM/PLM systems provide design release support by locking a CAD file for access. The access controls are defined in the database and the definition of a part/assembly/drawing as released is controlled by the database. When a new revision of the part is required, a file copy is made, and the database provides access to the new copy. Generally, the old copy representing the previous release persists in the file store and can be referenced by the database. _This is not how Onshape works._

![](https://onshape-public.github.io/docs/api-intro/whyonshape/images/integrationguideimage16.png)Since there are no files in Onshape (just data) no file locking or copy mechanisms are available. Instead, Onshape looks at the data as a continuous timeline that is always moving forward and always changing as the design evolves. The data is never locked; it is always available.

In place of file copies that represent versions and releases of the design, Onshape provides the ability to create _versions_ as bookmarks in the timeline. When creating a version, Onshape places a bookmark in the timeline that represents the state of the design at that specific moment in time. Releases work in a similar way, but they are defined as official, company-approved processes and have special meaning.

In addition to creating versions and releases, Onshape can create _branches_, which can be defined as alternative timelines. A designer might want to experiment with alternate design ideas without modifying the existing design that others are working on. By creating a branch from any point in the timeline, the designer is free to experiment with alternate ideas. If the ideas work, they can be merged into the current timeline at any point.

From an integration perspective, we need to take into consideration how Onshape works with versions and releases. Since a release represents a company-approved design, Onshape provides processes for the approval of a release and the change of state of a design. Onshape also provides APIs and triggers (events) that enable integration points throughout the release process. It is through the triggers and the APIs that integration of any third-party system that wishes to manage the release process is enabled.

##### Workflows

Release and obsoletion workflows are included with Onshape and can be customized to meet company standards.

For details on how to implement and customize Onshape’s workflows, please review these online help topics:

* [How to design release management processes](https://cad.onshape.com/help/Content/relmgmt%5Fcustom.htm)
* [How to create a customized release workflow](https://cad.onshape.com/help/Content/custom%5Fworkflow.htm)

Most PDM/PLM systems can model a company’s business processes in a workflow. These can be highly automated processes that move data and file references through a process of reviews and approvals. Onshape also has this capability, which is currently used for release and obsoletion processes.

There are no files or file references in Onshape that are moved through the process. Onshape only has data. Therefore, it is the data that is referenced at each stage of the process. Traditional PDM systems might make file copies and lock files as they move through a release process. If the process is rejected at any stage, those files must be discarded, the previous version of the files unlocked and all states updated. In short, it system must rewind back to the state of the files and the data when the workflow was initiated. This is a lot of complex actions that must occur when a process is rejected for any reason. _Onshape doesn’t work this way._

A release process can be started on data (such as assemblies, parts, drawings, etc.). For example, if the state of a referenced part is updated to “Pending,” and the process is rejected at any stage, there is no rewinding of files and data; the data just reverts to the original “In Progress” state, and the workflow is discarded. Since the workflow didn’t complete, nothing related to the data has actually changed. When you are used to traditional PDM systems, this feels like an anti-climax, and we often receive the question, “But where’s my process? Where’s the data that was attached to the process?”. Well, the answer is: nothing changed. Until the process is completed, nothing actually changes, so the data is in the same state it was prior to the initialization of the release process.

![A picture containing chart Description automatically generated](https://onshape-public.github.io/docs/api-intro/whyonshape/images/integrationguideimage17.png)

_A custom release process in Onshape_

---

<a id="sec-authentication"></a>
## Authentication

<a id="pg-docs-auth"></a>
### Authentication

_Source: <https://onshape-public.github.io/docs/auth/>_

> 📘 **Note**
> 
> All applications submitted to the Onshape App Store (Onshape Apps) must follow the instructions on the [OAuth2](https://onshape-public.github.io/docs/auth/docs/auth/oauth) page and use OAuth2 for authorization. Automation scripts (or applications not meant for the Onshape App Store) may use either OAuth2 or [API Keys](https://onshape-public.github.io/docs/auth/docs/auth/apikeys) for authentication. OAuth2 allows applications to call Onshape APIs on behalf of the users of the application; API keys will only perform operations on behalf of the Onshape user who generated the API keys.

We’ve structured API keys to work very similarly to OAuth in the operation of your app. You must build your Authorization header differently (and set up redirects and sign-ins), but the API calls themselves work the same in both versions, provided that the API key and the OAuth app have the same scopes. An API key with the `OAuth2Read` and `OAuth2Write` scopes have the same access to the same API endpoints as an OAuth application with the `OAuth2Read` and `OAuth2Write` scopes. The only differences are when calling API endpoints in relation to the OAuth application itself, since an API key request does not come from an OAuth application.

Please select an option for authentication:

* [API Keys](https://onshape-public.github.io/docs/auth/docs/auth/apikeys) \- API keys are used to authenticate an application, NOT its users.
* [OAuth2](https://onshape-public.github.io/docs/auth/docs/auth/oauth) \- OAuth2 authenticates an application AND users of the application by ensuring the users are authorized to access Onshape.

---

###### [OAuth](https://onshape-public.github.io/docs/auth/docs/auth/oauth/)

###### [API Keys](https://onshape-public.github.io/docs/auth/docs/auth/apikeys/)

###### [API Limits](https://onshape-public.github.io/docs/auth/docs/auth/limits/)

---

<a id="pg-docs-auth-apikeys"></a>
### API Keys

_Source: <https://onshape-public.github.io/docs/auth/apikeys/>_

> 📘 **Note**
> 
> All applications submitted to the Onshape App Store (Onshape Apps) must follow the instructions on the [OAuth2](https://onshape-public.github.io/docs/auth/apikeys/docs/auth/oauth) page and use OAuth2 for authorization. Automation scripts (or applications not meant for the Onshape App Store) may use either OAuth2 or API Keys for authentication. OAuth2 allows applications to call Onshape APIs on behalf of the users of the application; API keys will only perform operations on behalf of the Onshape user who generated the API keys.

API keys are useful for small applications meant for personal use, allowing developers to avoid the overhead of the OAuth workflow. Creating an app is very easy with API keys: create an API key with the Developer Portal, set up a function to build your API key header as in the samples, and make your API calls.

Keep in mind:

* API keys are used to authenticate an application, NOT its users.
* [OAuth2](https://onshape-public.github.io/docs/auth/apikeys/docs/auth/oauth) authenticates an application AND users of the application by ensuring the users are authorized to access Onshape.

We use API keys for authenticating requests instead of cookies for several reasons:

* **Security**: Each request is signed with unique headers so that we can be sure it’s coming from the right place.
* **Scope**: API keys can be scoped to specific actions. See [Permission Scopes](https://cad.onshape.com/help/Content/Plans/my%5Faccount%5Fdeveloper.htm#scopes).
* **Revocation**: API keys are revokable. If a server with API secret keys is compromised, you can revoke the API key so it can no longer be used. Cookies require a password reset that must be updated everywhere.
* **OAuth**: The API key system we’re now using for HTTP requests is the same process developers follow when building full-blown OAuth applications; there’s no longer a disconnect between the two.

Once you create an API key, it will only be valid in the stack on which it was created. An API key created on your company stack (i.e., companyName.onshape.com) will not function on the production stack (cad.onshape.com).

#### Manage API keys

> ⚠️ **API keys are now managed in your Onshape settings.**
> 
> * To manage your own API keys, see: [My Account - Developer](https://cad.onshape.com/help/Content/Plans/developer-myaccount.htm)
> * To manage API keys for a company, classroom, or enterprise, see: [Company/Classroom/Enterprise Settings - Developer](https://cad.onshape.com/help/Content/Plans/developer.htm)

Your API key and secret are like a username and password pair. They are tied directly to your Onshape account. Avoid sharing them, and do not place them directly in the code for your application. Several of the samples provided on this site use a separate configuration file to contain this information, but there are other ways to keep the access key and secret safe, such as setting them as environment variables.

#### Authenticate with API keys

Please select an option for authentication:

* [Basic Authorization](#local-authorization): Lowest security. For local testing only.
* [Request Signature](#request-signature): Medium security. For testing and internal use.
* [OAuth2](https://onshape-public.github.io/docs/auth/apikeys/docs/auth/oauth): Highest security. Required for all Onshape Apps.

##### Basic authorization

For local testing, you can provide a basic authentication via your API Keys. Depending on your library of choice, you may need to encode your keys for basic authorization.

To base-64-encode your keys:

1. Open your terminal/command prompt and run the following command, replacing `ACCESS_KEY` and `SECRET_KEY` with the **access key** and **secret key** you created earlier. Remember to include the colon (`:`) between the keys. _You will receive a long, base-64-encoded string as output._  
   * **MacOS**:  
   ```  
   printf ACCESS_KEY:SECRET_KEY | base64  
   ```  
   * **Windows**:  
   ```  
   powershell "[convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes(\"ACCESS_KEY:SECRET_KEY\"))"  
   ```  
   * For example, given an access key of `abcdefghi0123456789jkl` and secret key of `abcdefghijklmnopqrstuvwxzy0123456789abcdefghijkl`, the corresponding command would be:  
         * **MacOS**  
         ```  
         printf abcdefghi0123456789jkl:abcdefghijklmnopqrstuvwxzy0123456789abcdefghijkl | base64  
         ```  
         * **Windows**  
         ```  
         powershell "[convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes(\"abcdefghijklmnopqrstuvwxzy0123456789abcdefghijkl:abcdefghijklmnopqrstuvwxzy0123456789abcdefghijkl\"))"  
         ```
2. Make note of the output string; these are your credentials.
3. Add the authorization header to your code, replacing `CREDENTIALS` with the string you received in Step 2:  
```  
-H 'Authorization: Basic CREDENTIALS' \  
```  
For example:  
```  
-H 'Authorization: Basic ZnBpZnE1cm92d2VjeHZRU0k0MmxHbn0m4r5ydXNXczRPRUJLWTduS1NObVhoMzlrN2dzVE5QWEdqb0gzSUU4dFVnTlREdDZaYQ==' \  
```

See our [Quick Start Guide](https://onshape-public.github.io/docs/auth/apikeys/docs/api-intro/quickstart) for an example of using Basic Authorization in an app.

##### Request signature

For additional security, you can include your API Keys as part of a request signature. This provides more security than the Basic Authorization above, but less security than OAuth2.

To ensure that a request is coming from you, we have a process for signing requests that you must follow for API calls to work. Everything is done via HTTP headers that you’ll need to set:

1. _Date_: A standard date header giving the time of the request; must be accurate within **5 minutes** of request. Example: `Mon, 11 Apr 2016 20:08:56 GMT`
2. _On-Nonce_: A string that satisfies the following requirements:  
   * At least 16 characters  
   * Alphanumeric  
   * Unique for each request
3. _Authorization_: This is where the API keys come into play. You’ll sign the request by implementing this algorithm:  
   * **Input**: Method, URL, On-Nonce, Date, Content-Type, AccessKey, SecretKey  
   * **Output**: String of the form: `On <AccessKey>:HmacSHA256:<Signature>`  
   * **Steps to generate the signature portion**:  
         1. Parse the URL and get the following:  
                  1. The path, e.g. `/api/documents` (no query params!)  
                  2. The query string, e.g. `a=1&b=2`  
                              * NOTE: If no query parameters are present, use an empty string  
         2. Create a string by appending the following information in order. Each field should be separated by a newline (`\n`) character, and the string must be converted to lowercase:  
                  1. HTTP method  
                  2. On-Nonce header value  
                  3. Date header value  
                  4. Content-Type header value  
                  5. URL pathname  
                  6. URL query string  
         3. Using SHA-256, generate an [HMAC digest](https://en.wikipedia.org/wiki/Hash-based%5Fmessage%5Fauthentication%5Fcode), using the API secret key first and then the above string, then encode it in Base64.  
         4. Create the `On <AccessKey>:HmacSHA256:<Signature>` string and use that in the Authorization header in your request.

Below is an example function to generate the authorization header, using Node.js’s standard `crypto` and `url` libraries:

`// ...at top of file
var u = require('url');
var crypto = require('crypto');

/**
* Generates the "Authorization" HTTP header for using the Onshape API
*
* @param {string} method - Request method; GET, POST, etc.
* @param {string} url - The full request URL
* @param {string} nonce - 25-character nonce (generated by you)
* @param {string} authDate - UTC-formatted date string (generated by you)
* @param {string} contentType - Value of the "Content-Type" header; generally "application/json"
* @param {string} accessKey - API access key
* @param {string} secretKey - API secret key
*
* @return {string} Value for the "Authorization" header
*/
function createSignature(method, url, nonce, authDate, contentType, accessKey, secretKey) {
    var urlObj = u.parse(url);
    var urlPath = urlObj.pathname;
    var urlQuery = urlObj.query ? urlObj.query : ''; // if no query, use empty string

    var str = (method + '\n' + nonce + '\n' + authDate + '\n' + contentType + '\n' +
        urlPath + '\n' + urlQuery + '\n').toLowerCase();

    var hmac = crypto.createHmac('sha256', secretKey)
        .update(str)
        .digest('base64');

    var signature = 'On ' + accessKey + ':HmacSHA256:' + hmac;
    return signature;
}
`

##### Redirects

Some API endpoints return 307 redirects. You must generate an Authorization header for the redirect as well, but please note that the server portion of the URL might be different, the redirect URL may contain query parameters that must be encoded in the Authorization header, etc.

#### Delete API keys

1. Click the **Delete API Key** button next to the key pair you wish to delete.
2. Confirm that you are deleting the correct set of API keys. This cannot be undone. Click **Delete** to confirm.

#### Get help

If you need information or have a question unanswered in this documentation, email [api-support@onshape.com](mailto:api-support@onshape.com) or check out the [forums](https://forum.onshape.com).

---

<a id="pg-docs-auth-limits"></a>
### API Limits

_Source: <https://onshape-public.github.io/docs/auth/limits/>_

When using the Onshape REST API, it is important to understand the usage limits in place to ensure reliable and consistent performance for all users. These limits help safeguard the platform and ensure equitable access to Onshape services.

#### Rate Limits

Onshape limits the number of API calls that can be made within a given time period to maintain optimal platform stability and performance. Specific rate limit values vary by endpoint, but exceeding the threshold results in an HTTP response status code `429 (Too Many Requests)`.

To minimize disruptions:

* Follow the guidance at [Response Codes: 429](https://onshape-public.github.io/docs/auth/limits/docs/api-adv/errors/#429-too-many-requests) to handle 429 responses gracefully.
* Optimize your application’s API call patterns to reduce unnecessary or redundant requests.
* Monitor your application’s request rate proactively to remain within acceptable usage levels.

#### Annual API Call Limits

In addition to per-endpoint rate limits, Onshape enforces annual limits on API usage, varying by account type:

| Onshape Subscription      | Annual Calls                    |
| ------------------------- | ------------------------------- |
| EnterpriseEnterprise GOV  | 10,000 per Full User in Company |
| Professional              | 5,000 per User in Company       |
| EDU StudentFreeStandard   | 2,500 per User                  |
| EDU Enterprise            | 10,000 per Enterprise           |
| EDU EducatorPro Discovery | 2,500 per Company               |

You can view your API usage directly in Onshape.

* See [Company/Classroom/Enterprise Settings - Developer](https://cad.onshape.com/help/Content/Plans/developer.htm?) for information on viewing company-wide usage.
* See [My Account - Developer](https://cad.onshape.com/help/Content/Plans/developer-myaccount.htm) for information on viewing your personal API usage.
![api usage in onshape enterprise settings](https://onshape-public.github.io/docs/auth/limits/images/api-usage-02.png)

#### Call limit details

**Calls that count toward API limits:**

_Calls from the following sources are only counted if they return 2xx or 3xx [Response Codes](https://onshape-public.github.io/docs/auth/limits/docs/api-adv/errors)._

* Calls made with [API keys](https://onshape-public.github.io/docs/auth/limits/docs/auth/apikeys)
* Calls made with [OAuth2](https://onshape-public.github.io/docs/auth/limits/docs/auth/oauth) via private applications (any applications that are NOT publicly available in the Onshape App Store)
* Calls made from the [Onshape API Explorer](https://cad.onshape.com/glassworks/explorer/) when [authenticated via API keys or OAuth2](https://onshape-public.github.io/docs/auth/limits/docs/api-intro/explorer/#authenticate)

**Calls that do NOT count toward API limits:**

* Calls made with [OAuth2](https://onshape-public.github.io/docs/auth/limits/docs/auth/oauth) via applications that are publicly available in the Onshape App Store
* Calls made from the Onshape browser, mobile clients, or the [Onshape API Explorer](https://cad.onshape.com/glassworks/explorer/) (when authenticated via an Onshape session)
* Webhook notifications sent by Onshape
* Calls that return 4xx or 5xx [Response Codes](https://onshape-public.github.io/docs/auth/limits/docs/api-adv/errors)

Limits are applied at the company level, and additional users increase allocation by a pro-rated amount. For example, if an Enterprise adds 1 seat when they have half of their API allocation period remaining, that allocation will increase by 5,000 API calls in their current cycle. It will then increase by 10,000 API calls in the next full cycle.

Once the annual API call limit is reached, subsequent API requests are rejected with a [402 Response Code](https://onshape-public.github.io/docs/auth/limits/docs/api-adv/errors#402-payment-required). To avoid service disruption, manage and monitor your API consumption carefully throughout the year.

Additional API calls are available for purchase upon request. Reach out to your Onshape representative or [api‑support@onshape.com](mailto:api-support@onshape.com) for more information.

See also: [Transfer app ownership](https://onshape-public.github.io/docs/auth/limits/docs/auth/oauth#transfer-ownership).

#### Terms of Use

Your usage of the Onshape API is governed by the Onshape Terms of Use and the Onshape API Terms of Use. You must comply fully with these terms when using the API. Specifically, it is critical to note:

* **Prohibited Usage**: The API may not be used by any robot, spider, scraper or other automated means for data mining, data gathering or extraction method from the Onshape Public Documents. Such activity constitutes a violation of the API Terms of Use and may result in suspension or termination of your API access.
* **Acceptable Use**: The API should be used exclusively to develop applications or tools that enhance productivity for you or other Onshape users by interacting responsibly with user content and resources provided by the Onshape platform.

Refer directly to the Onshape Terms of Use and the API Terms of Use for comprehensive information regarding permissible activities and usage restrictions. Reach out to your Onshape representative for the latest version of the agreements.

---

<a id="pg-docs-auth-oauth"></a>
### OAuth

_Source: <https://onshape-public.github.io/docs/auth/oauth/>_

**See the [gltf-viewer-app](https://github.com/onshape-public/app-gltf-viewer) for a working example of OAuth2.**

> 📘 **Note**
> 
> All applications submitted to the Onshape App Store (Onshape Apps) must use OAuth2 for authorization. Automation scripts (or applications not meant for the Onshape App Store) may use either OAuth2 or [API Keys](https://onshape-public.github.io/docs/auth/oauth/docs/auth/apikeys) for authentication. OAuth2 allows applications to call Onshape APIs on behalf of the users of the application; API keys will only perform operations on behalf of the Onshape user who generated the API keys.

#### What is OAuth2?

The OAuth (Open authorization) protocol was developed by the Internet Engineering Task Force, an open standards organization that develops and promotes voluntary Internet standards (particularly the technical standards that comprise the Internet protocol suite) to enable secure, delegated access to an application’s resources.

The OAuth2 protocol enables an application to access a resource that is under the control of someone else. In order to access that resource, a _token_ is required. The token represent the delegated rights of access (that is, what rights this application has, such as read/write/update, scope, rights to different resources, and more).

_This means the application can be accessed by a third-party system without that system impersonating the user that controls the resource._

A good analogy is the hotel check-in process. When you arrive at the front desk of a hotel, you provide an ID and a form of payment. Then, you are given a key card that opens a specific door. When you reach that door, you swipe your key card and are granted access. The door itself doesn’t know who you are or anything about you, it just knows that the key card was encoded correctly, and it allows you access. At some point, the key card expires, and the door no longer lets you into the room. This is the same for access tokens in the OAuth2 flow.

With the OAuth2 protocol, you register your application with the third party, and you are given a set of keys. These keys get exchanged for an access token that grants you access to resources in the third-party application. The token expires regularly; you must get a new token to access the application again. For this, you are provided with a _refresh token_. Sending the refresh token to the authentication server updates your access token and gives you a new refresh token.

![api token request diagram](https://onshape-public.github.io/docs/auth/oauth/images/APITokenRequestDiagram.png)

Keep in mind:

* [API keys](https://onshape-public.github.io/docs/auth/oauth/docs/auth/apikeys) are used to authenticate an application, NOT its users.
* OAuth2 authenticates an application AND users of the application by ensuring the users are authorized to access Onshape.

##### OAuth2 & Onshape

The first step in the OAuth flow is for the Onshape user to request that Onshape let the third-party application access Onshape.

Once the user has authorized the application, they are redirected to a predefined URL (called a _redirect URL_) with a code that will requests an access token from Onshape. Therefore, the redirect URL should contain a script that can capture the authorization code.

You will use the access token to authenticate requests to the Onshape API. The token expires after preset amount of time. To get a new valid access token after one has expired, you must use the refresh token to request a new access token. Refreshing the access token also provides you with an updated refresh token to use in the next refresh access token request. Make sure to store both the the access token and the refresh token, and update them with each refresh of the token. The authorization token must accompany any call to the API, this is done by adding the token to an Authorization field in the header of each request:

`Authorization: Bearer <accessToken>
`

If correctly authenticated, most responses from the REST API call return JSON data (though some return binary data), with an HTTP response code of `200 Success`, `204 - No Content`, or `301 - Permanent Redirect`. `301` responses will include a redirect for you to follow.

In the event that the authorization code is incorrect (for instance, if it expired), you will receive an **HTTP 401** response. This response means that the client request has not been completed, since it lacks valid authentication credentials for the requested resource. In this event, your code for each call to the REST API should include a catch clause for a 401 exception. Once caught, you can refresh the token and make the request again. Pay close attention to the `Content-Type` header for what data to parse and expect.

When integrating with Onshape, OAuth tokens give third-party applications (such as desktop applications or web services) access to users’ data as defined by the permissions scope (such as users’ documents or profile information). Using OAuth terminology, Onshape acts as both the authorization and resource server, while the desktop or web-based application is the client. Resource owners have the option of granting or denying access to applications.

Once obtained, an OAuth token will work for third-party APIs under `/api`. Do NOT attempt to use an OAuth token to fetch the URLs typically displayed in a web browsers location bar.

##### More resources

* [Digital Ocean](https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2) \- A good resource for learning more about OAuth2.
* [RFC 6749](http://tools.ietf.org/html/rfc6749) \- The reference for the OAuth framework as a whole. Most of this document describes how to implement the OAuth exchanges described by the reference within the context of Onshape and client applications.
* [RFC 6750](http://tools.ietf.org/html/rfc6750) \- Describes the exchange of OAuth access tokens between clients and OAuth servers.

#### Implement OAuth2

This OAuth tutorial demonstrates how to recreate the authentication process in Node.js found in the [gltf-viewer-app](https://github.com/onshape-public/app-gltf-viewer) sample code. The [final code](#final-code) in Node.js and other languages can be found at the end of this page.

> 📘 **Note**
> 
> Enterprise/Company administrators should create and manage OAuth applications from within their [Onshape Developer Settings](https://cad.onshape.com/help/Content/Plans/developer.htm). **Apps created within the dev portal are owned by the individual, not the company/enterprise.**

##### 1: Register the app

1. Navigate to <https://cad.onshape.com/appstore/dev-portal> and sign in.
2. In the left sidebar, click **OAuth applications**.
3. Click the **Create new OAuth application** button.
4. Fill out the form as follows:  
   * Name: `gltf-viewer-yourname`  
         * The application name to display to users.  
         * Should include the name of your company to differentiate it from other possibly similar applications.  
   * Primary format: `com.yourname.gltf-viewer`  
         * String that uniquely identifies your application and is a marker for the data it might store on Onshape servers.  
         * Cannot be changed after the application is registered.  
   * Summary: `Onshape OAuth tutorial`  
         * Description of your application.  
         * Displayed to the user when they’re asked to grant the application permission to access their data.  
   * Redirect URLs: `http://localhost:5000/token`  
         * Your application must specify at least one URL used in the OAuth protocol exchanges.  
         * This URL must also use SSL (a URL that begins with https), with two exceptions applicable for installed desktop applications: `http://localhost:<port>` and `urn:ietf:wg:oauth:2.0:oob`.  
         * e.g., `https://app-gltf-viewer-yourname-c11f263794bc.herokuapp.com/oauthRedirect`  
   * Admin team: `No Team`  
         * Optional.  
         * If defined, members of the team can make changes to the definition of this OAuth application.  
         * See the [Help Docs: Teams](https://cad.onshape.com/help/Content/teams-enterprise.htm) page for more information on creating teams in Onshape.  
   * OAuth URL: `none`  
         * Should contain the URL of your deployed application.  
         * This is the first URL called from the Onshape Applications page.  
         * The page hosted at this URL should handle the OAuth authentication. Once your application’s server has been authenticated on behalf of the user, that user should be redirected to your applications content.  
         * If you have not deployed your app yet, you can leave this field blank (as shown in this example) for local work and update it later.  
         * e.g., `https://app-gltf-viewer-yourname-c11f263794bc.herokuapp.com/oauthSignin`  
   * Settings: check **Supports collaboration**  
   * Permissions: This is also called application scope, and it defines what access rights your application has to the user’s data.  
         * **Application can read your profile information** (`OAuth2ReadPII`) - Enable your application to access the Onshape user profile. Check this option.  
         * **Application can read your documents** (`OAuth2Read`) - Onshape documents created by this user can be accessed with read privileges only. This means the documents and associated data can be viewed, but not updated or modified in any way, which can be a useful way to interact with data without risk of accidentally making unwanted changes. Check this option.  
         * **Application can write to your documents** (`OAuth2Write`) - The user-owned Onshape documents can be modified by this application. Check this option.  
         * **Application can delete documents and workspaces** (`OAuth2Delete`) - Your application will be able to delete content, including documents, workspaces, teams, comments, etc. Do not check this option for this example.  
         * **Application can request Purchases on Your behalf** (`OAuth2Purchase`) - The application will have access to make purchases if required. Do not check this option for this example.  
         * **Application can share and unshare documents on your behalf** (`OAuth2Share`) - Onshape’s document sharing capabilities are very powerful; they enable other parties to access your shared documents with predefined rights. If this option is checked, the application can automatically share a document with other people. Do not check this option for this example.
5. Click **Create application**.
6. **COPY THE OAUTH SECRET FROM THE POP-UP WINDOW.**  
   * You will not be able to access this secret again.  
   * This secret is unique to you and your app and should be protected like any sensitive password. For example, it should _NOT_ be checked in to source code control systems.
7. Click **Close**.
8. Copy the **OAuth client identifier** from the app Details page that opens.  
   * These OAuth secret and client ID keys will be used in your code for requesting a one-time user authorization code from Onshape.

Your application is now registered with Onshape and you have options to modify the application definition through this portal.

  
![the gltf-viewer app in the onshape dev portal app details screen](https://onshape-public.github.io/docs/auth/oauth/images/dev-portal-app-details-02.png)

##### 2: Get the user authorization code

We’ll start by loading the basic libraries required to run this sample. We’ll use Passport to authenticate requests through plugins known as strategies. In this example, we’ll use an Onshape-developed plugin called `passport-onshape`, but you can define your own strategy to use with Passport, if you prefer. You can find more information on [Passport here](https://www.npmjs.com/package/passport).

1. Create a directory for your app, and then install Passport and passport-onshape:

`npm install passport
npm install passport-onshape
`

1. Next, create a file calls `app.js` and add the following definitions to the top of the file:

`// App definitions 
const path = require('path');
const uuid = require('uuid');

const express = require('express');
const session = require('express-session');
const bodyParser = require('body-parser');

const passport = require('passport');
const OnshapeStrategy = require('passport-onshape');

const config = require('./config');
`

1. Next, tell Express to use Passport and initialize it. Note: you can replace the Express code with code for the web server of your choice.

`// Tell Express to use Passport, and initialize it.
const app = express();

app.use(express.static(path.join(__dirname, 'public')));
app.use(express.static(path.join(__dirname, 'dist')));
app.use(bodyParser.json());

app.set('trust proxy', 1); // To allow to run correctly behind Heroku when deployed

app.use(session({
    secret: config.sessionSecret,
    saveUninitialized: false,
    resave: false,
    cookie: {
        name: 'app-gltf-viewer',
        sameSite: 'none',
        secure: true,
        httpOnly: true,
        path: '/',
        maxAge: 1000 * 60 * 60 * 24 // 1 day
    }
}));
app.use(passport.initialize());
app.use(passport.session());
`

1. Next, we’ll store the Onshape user information so it can be retrieved from `req.user` in each call. Passport uses the `serializeUser` function to persist user data (after successful authentication) into the session. The function `deserializeUser` is used to retrieve user data from session.

`//Store the Onshape user information
passport.serializeUser((user, done) => done(null, user));
passport.deserializeUser((obj, done) => done(null, obj));
`

1. Initialize Passport with the Onshape Strategy:

`` //Initialize Passport with the Onshape Strategy
passport.use(new OnshapeStrategy({
        clientID: config.oauthClientId,
        clientSecret: config.oauthClientSecret,
        callbackURL: config.oauthCallbackUrl,
        authorizationURL: `${config.oauthUrl}/oauth/authorize`,
        tokenURL: `${config.oauthUrl}/oauth/token`,
        userProfileURL: `${config.oauthUrl}/api/users/sessioninfo`
    },
    (accessToken, refreshToken, profile, done) => {
        profile.accessToken = accessToken;
        profile.refreshToken = refreshToken;
        return done(null, profile);
    }
));
 ``

1. Open your environment variables file (e.g.,`.env`, `.bashrc`, `.bash_profile`, `.zshrc,` etc.) and add the following environment variables, then save and close the file.

`authorizationURL : https://oauth.onshape.com/oauth/authorize
tokenURL : https://oauth.onshape.com/oauth/token
userProfileURL : https://cad.onshape.com/api/users/sessioninfo
`

The callback function will provide us with the `accessToken`, the `refreshToken`, and the user’s Onshape profile once authentication has been successfully passed. We can now use this to update our database with user-specific information.

Note that if you store the `accessToken` and `refreshToken` in the database along with the user record, you must update it each time that the access codes are refreshed.

1. Next, we define our endpoint where the authorization flow starts (in this case, `/oauthSignin`). This is the endpoint that we previously defined in the Onshape application setup. This will redirect to an Onshape page in order for the user to confirm (or deny) the applications access to theOnshape resources.

`//Define the Onshape API endpoint
app.use('/oauthSignin', (req, res) => {
    /* These 5 lines are specific to the glTF Viewer sample app. You can replace them with the input for whatever Onshape endpoints you are using in your app */
    const state = {
        docId: req.query.documentId,
        workId: req.query.workspaceId,
        elId: req.query.elementId
    };
    req.session.state = state;
    return passport.authenticate('onshape', { state: uuid.v4(state) })(req, res);
}, (req, res) => {    

 });
`

##### 3: Exchange the code for an access token

Fortunately, if you are using Passport, there isn’t much to do once the user grants authorization. The return URL will contain the one-time authorization token, which Passport will extract and exchange for an access token and a refresh token, which are available in Passport callback function.

1. Add the following code to `app.js`:

`` //Exchange the code for an access token
app.use('/oauthRedirect', passport.authenticate('onshape', { failureRedirect: '/grantDenied' }), (req, res) => {
    /* This code is specific to the glTF Viewer sample app. You can replace it with the input for whatever Onshape endpoints you are using in your app. */
    res.redirect(`/?documentId=${req.session.state.docId}
&workspaceId=${req.session.state.workId}&elementId=
    ${req.session.state.elId}`);
});
 ``

1. If the user clicks **Deny** instead of **Authorize Application**, they are taken to a page that notifies them that access to the application was denied. We can see that in the `failureRedirect` argument. Add the following to `app.js`:

`//Handle denied access
app.get('/grantDenied', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'html', 'grantDenied.html'));
})
`

Now we have received the access token, and it can be accessed from `res.user.accessToken` on this page or from `req.user.accessToken` from any other page you redirect to from here.

##### 4: Use the access token

1. Add the following to the bottom of `app.js`. You can see that the access token is used as an Authorization header:

`` //Use the access token as an Authorization header
makeOnshapeAPICall: async (req, res) => {
        try {
            const apiUrl = "https://cad.onshape.com/api/documents?ownerType=1&sortColumn=createdAt&sortOrder=desc&offset=0&limit=20"; //You can replace this with any Onshape API endpoint URL.
            const resp = await fetch(normalizedUrl, { headers: { Authorization: `Bearer ${req.user.accessToken}` }});
            const data = await resp.text();
            const contentType = resp.headers.get('Content-Type');
            res.status(resp.status).contentType(contentType).send(data);
        } catch (err) {
            res.status(500).json({ error: err });
        }
    }
 ``

Note: in the glTF Viewer sample app, this code appears in `utils.js` instead of `app.js`.

##### 5: Refresh the token

When the access token expires, it must be refreshed by making another `POST` request to `https://oauth.onshape.com/oauth/token` with the following URL-encoded form body (with `Content-Type application/x-www-form-urlencoded`):

`grant_type=refresh_token&refresh_token=\<refresh_token\>&client_id=\<client_id\>&client_secret=\<client_secret\>
`

As with the authorization code data, the parameters in the form body must be URL-encoded. The response to this `POST` request will be a JSON-encoded structure with a new `access_token` value that can be used for the next 60 minutes.

Refresh tokens are valid for the lifetime of the user’s grant. If a user who previously granted access to your application decides to revoke the grant, the refresh token is invalidated. If the user decides to re-grant application access, a new refresh token is generated and returned along with the access token.

1. Add the following to `app.js`:

`` /** After landing on the home page, we check if a user had already signed in. If no user has signed in, we redirect the request to the OAuth sign-in page. If a user had signed in previously, we will attempt to refresh the access token of the user. After successfully refreshing the access token, we will simply take the user to the landing page of the app. If the refresh token request fails, we will redirect the user to the OAuth sign-in page again. */
app.get('/', (req, res) => {
    if (!req.user) {
        return res.redirect(`/oauthSignin${req._parsedUrl.search ? req._parsedUrl.search : ""}`);
    } else {
        refreshAccessToken(req.user).then((tokenJson) => {
            // Dereference the user object and update the access token and refresh token in the in-memory object.
            let usrObj = JSON.parse(JSON.stringify(req.user));
            usrObj.accessToken = tokenJson.access_token;
            usrObj.refreshToken = tokenJson.refresh_token;
            // Update the user object in PassportJS. No redirections will happen here, this is a purely internal operation.
            req.login(usrObj, () => {
                return res.sendFile(path.join(__dirname, 'public', 'html', 'index.html'));
            });
        }).catch(() => {
            // Refresh token failed, take the user to OAuth sign in page.
            return res.redirect(`/oauthSignin${req._parsedUrl.search ? req._parsedUrl.search : ""}`);
        });
    }
});

//Refresh the access token
const refreshAccessToken = async (user) => {
    const body = 'grant_type=refresh_token&refresh_token=' + user.refreshToken + '&client_id=' + config.oauthClientId + '&client_secret=' + config.oauthClientSecret;
    let res = await fetch(config.oauthUrl + "/oauth/token", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: body
    });
    if (res.ok) {
        return await res.json();
    } else {
        throw new Error("Could not refresh access token, please sign in again.");
    }
}

app.use('/api', require('./api'));
module.exports = app;
 ``

1. Save the file.
2. To see the authentication working in practice, you can follow the instructions in the [glTF Viewer README](https://github.com/onshape-public/app-gltf-viewer#readme) to deploy the glTF Viewer app.

##### 6: Grant authorization

For apps published in the Onshape App Store, the Onshape user must grant authorization to your application to access the Onshape data. This must be done by each user of your app.

To grant the application access to a user’s data in Onshape, the _Onshape user_ must follow the steps below:

1. Sign in to `cad.onshape.com`.  
   * Note: Use `https://companyName.onshape.com` for Enterprise accounts. See [Enterprise users](#enterprise-users) below for more information.
2. Click their name in the top-right corner of the Onshape window, and then click **My account** in the dropdown menu.  
![drawing](https://onshape-public.github.io/docs/auth/oauth/images/myaccountdropdown.png)
3. Click **Applications** in the left sidebar.  
   * Note that the gltf-viewer app will not appear in this list until it has been deployed and subscribed to as described in the [glTF Viewer README](https://github.com/onshape-public/app-gltf-viewer#readme).
4. Click **Grant** next to your app name to grant it access to their Onshape data. The Onshape user can click **Revoke** at any time to prevent your app from accessing their Onshape data.
5. The user will see the Authorize application screen shown below and will need to confirm their authorization grant by clicking **Authorize application**. The user is then redirected to the Redirect URL you specified in your code. Your app can now access the user’s Onshape resources and profile.

#### Notes

##### Transfer ownership

To transfer the app to a new owner:

1. Navigate to <https://cad.onshape.com/appstore/dev-portal> and sign in.
2. In the left sidebar, click **OAuth applications**.
3. Click the application to transfer.
4. Click the **Transfer ownership** button on the Details tab.  
![](https://onshape-public.github.io/docs/auth/oauth/images/dev-portal-transfer-02.png)
5. Select an option to transfer the app to an individual, company, or enterprise.
6. To transfer to an individual, enter the name or email of the new owner in the search field. To transfer ownership to a company or enterprise, select an option from the dropdown.
7. Click **Transfer Ownership**. The application is removed from your dev portal.  
   * If the app was transferred to an individual, it appears in their dev portal.  
   * If the app was transferred to a company or enterprise, it appears in their [Onshape Developer Settings](https://cad.onshape.com/help/Content/Plans/developer.htm).

Future API call consumption and billing will be attributed to the new owner. See [API Limits](https://onshape-public.github.io/docs/auth/oauth/docs/auth/limits) for details.

##### Installed desktop applications

OAuth is designed for interactions between two servers using a browser. However, it can also be used by an installed desktop (or mobile) application. The application must perform a similar role to that of a third party server: it must exchange the code for an access token structure.

To enable this, Onshape allows two special forms of redirect URI to be registered:

* `http://localhost:<port>` Causes the browser to attempt to load a page from the host upon which it is running. The code parameter will be supplied exactly the same as outlined above. If the application can listen on the registered port and behave as a simple web server for the redirect URL, it can retrieve the code in the same way as a deployed web server.
* `urn:ietf:wg:oauth:2.0:oob` Causes the browser to display a simple page after a request has been granted instead of going to a new URL. The page contains simple instructions to copy and paste code into an application field. The browser will also update the title of the window to contain the code. An application could also look for browsers with window titles containing the string `Success code=<code>` and automatically grab the code from the browser window title. If an error occurs (e.g., the grant is denied), the browser window title will contain `Error description=<error string>`.

##### Enterprise users

When a user authorizes an OAuth app to access Onshape on their behalf, they get a bearer token that corresponds to their session and the allowed scopes.

However, if the user has a seat in the Enterprise, additional information is needed to determine whether to allow the bearer token to access enterprise data for the user or simply return non-enterprise data. We use the `company_id` field for this distinction.

There are two ways of setting the `company_id` correctly to access enterprise data:

* During the authorization process, select the name and URL of the enterprise instead of `cad.onshape.com`. This will correctly associate your bearer token with the `company_id`.
* If you have an integrated app, call the [Company/findCompany](https://cad.onshape.com/glassworks/explorer/#/Company/findCompany) endpoint to obtain the `id` from the `company` object. Append this `company_id` as a query parameter to the `/authorize` URL while initiating the OAuth workflow. (Note: you may be asked to authenticate yourself again.)

##### 3rd-party cookies

3rd-party cookies must be enabled in the browser for Onshape apps to work correctly.

##### Debugging

Debugging OAuth can be a little tricky. Some tips are below:

1. Make sure you are correctly URL encoding the values supplied to the oauth/authorize and oauth/token endpoints.
2. Use a `GET /oauth/authorize` but a `POST /oauth/token` and make sure that the GET uses query parameters but that the `POST` uses a URL-encoded form body.
3. If you supply a `redirect_uri` to `/oauth/authorize`, you must also supply it as an additional parameter in the `POST` to `/oauth/token`
4. Use a tool such as [Burp](https://portswigger.net/burp) or [Charles](http://charlesproxy.com) to deliberately ‘man-in-the-middle’ the connection requests between your server and Onshape, and verify that you are performing the correct REST operations (GET vs. POST) and correctly URL-encoding the parameter values.

#### Final Code

The above example uses Node.js to authenticate an Onshape app. This section includes the code for using OAuth2 with other coding languages.

##### Node.js

**Prerequisites**

`npm install passport
npm install passport-onshape
`

**Environment variables**

`authorizationURL : <https://oauth.onshape.com/oauth/authorize>
tokenURL : <https://oauth.onshape.com/oauth/token>
userProfileURL : <https://cad.onshape.com/api/users/sessioninfo>
`

**app.js**

`` //App definitions
const path = require('path');
const uuid = require('uuid');

const express = require('express');
const session = require('express-session');
const bodyParser = require('body-parser');

const passport = require('passport');
const OnshapeStrategy = require('passport-onshape');

const config = require('./config');

//Tell Express to use Passport, and initialize it.
const app = express();

app.use(express.static(path.join(__dirname, 'public')));
app.use(express.static(path.join(__dirname, 'dist')));
app.use(bodyParser.json());

app.set('trust proxy', 1); // To allow to run correctly behind Heroku when deployed.

app.use(session({
    secret: config.sessionSecret,
    saveUninitialized: false,
    resave: false,
    cookie: {
        name: 'app-gltf-viewer',
        sameSite: 'none',
        secure: true,
        httpOnly: true,
        path: '/',
        maxAge: 1000 * 60 * 60 * 24 // 1 day
    }
}));
app.use(passport.initialize());
app.use(passport.session());

//Store the Onshape user information
passport.serializeUser((user, done) => done(null, user));
passport.deserializeUser((obj, done) => done(null, obj));

//Initialize Passport with the Onshape Strategy
passport.use(new OnshapeStrategy({
        clientID: config.oauthClientId,
        clientSecret: config.oauthClientSecret,
        callbackURL: config.oauthCallbackUrl,
        authorizationURL: `${config.oauthUrl}/oauth/authorize`,
        tokenURL: `${config.oauthUrl}/oauth/token`,
        userProfileURL: `${config.oauthUrl}/api/users/sessioninfo`
    },
    (accessToken, refreshToken, profile, done) => {
        profile.accessToken = accessToken;
        profile.refreshToken = refreshToken;
        return done(null, profile);
    }
));

//Define the Onshape API endpoint
app.use('/oauthSignin', (req, res) => {
    /* These 5 lines are specific to the glTF Viewer sample app. You can replace them with the input for whatever Onshape endpoints you are using in your app. */
    const state = {
        docId: req.query.documentId,
        workId: req.query.workspaceId,
        elId: req.query.elementId
    };
    req.session.state = state;
    return passport.authenticate('onshape', { state: uuid.v4(state) })(req, res);
}, (req, res) => {    

});

app.use('/oauthRedirect', passport.authenticate('onshape', { failureRedirect: '/grantDenied' }), (req, res) => {
    /* This code is specific to the glTF Viewer sample app. You can replace it with the input for whatever Onshape endpoints you are using in your app. */
    res.redirect(`/?documentId=${req.session.state.docId}&workspaceId=${req.session.state.workId}&elementId=${req.session.state.elId}`);
});

//Handle denied access
app.get('/grantDenied', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'html', 'grantDenied.html'));
})

/** After landing on the home page, we check if a user had already signed in. If no user has signed in, we redirect the request to the OAuth sign-in page. If a user had signed in previously, we will attempt to refresh the access token of the user. After successfully refreshing the access token, we will simply take the user to the landing page of the app. If the refresh token request fails, we will redirect the user to the OAuth sign-in page again. */
app.get('/', (req, res) => {
    if (!req.user) {
        return res.redirect(`/oauthSignin${req._parsedUrl.search ? req._parsedUrl.search : ""}`);
    } else {
        refreshAccessToken(req.user).then((tokenJson) => {
            // Dereference the user object, and update the access token and refresh token in the in-memory object.
            let usrObj = JSON.parse(JSON.stringify(req.user));
            usrObj.accessToken = tokenJson.access_token;
            usrObj.refreshToken = tokenJson.refresh_token;
            // Update the user object in PassportJS. No redirections will happen here, this is a purely internal operation.
            req.login(usrObj, () => {
                return res.sendFile(path.join(__dirname, 'public', 'html', 'index.html'));
            });
        }).catch(() => {
            // Refresh token failed, take the user to OAuth sign in page.
            return res.redirect(`/oauthSignin${req._parsedUrl.search ? req._parsedUrl.search : ""}`);
        });
    }
});

//Refresh the access token
const refreshAccessToken = async (user) => {
    const body = 'grant_type=refresh_token&refresh_token=' + user.refreshToken + '&client_id=' + config.oauthClientId + '&client_secret=' + config.oauthClientSecret;
    let res = await fetch(config.oauthUrl + "/oauth/token", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: body
    });
    if (res.ok) {
        return await res.json();
    } else {
        throw new Error("Could not refresh access token, please sign in again.");
    }
}

app.use('/api', require('./api'));
module.exports = app;

//Use the access token in an Authorization header.
makeOnshapeAPICall: async (req, res) => {
        try {
            const apiUrl = "https://cad.onshape.com/glassworks/explorer/#/Document/getDocuments"; //You can replace this with any Onshape API endpoint URL.
            const resp = await fetch(normalizedUrl, { headers: { Authorization: `Bearer ${req.user.accessToken}` }});
            const data = await resp.text();
            const contentType = resp.headers.get('Content-Type');
            res.status(resp.status).contentType(contentType).send(data);
        } catch (err) {
            res.status(500).json({ error: err });
        }
    }
 ``

##### Python

This Python code only works on a local machine. To deploy the code, you can replace the Flask code with the web server of your choice.

**Prerequisites**

`pip3 install flask
pip3 install requests_oauthlib
`

**app.py**

`from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify
from requests_oauthlib import OAuth2Session
import os

app = Flask(__name__)
app.secret_key = b'F\xf5\xe5\xc0\xbe\tg\x7f\xac\x89\x87e\xc24\xe8m\x1c\xd9\xda\x96G,\x90i'

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"

client_id = <Client ID of your application>
client_secret = <Client Secret of your application>
authorization_base_url = "https://oauth.onshape.com/oauth/authorize"
token_url = "https://oauth.onshape.com/oauth/token"
redirect_url = "http://localhost:5000/token"

@app.route('/')
def home():
  onshape = OAuth2Session(client_id, redirect_uri=redirect_url)
  auth_url, state = onshape.authorization_url(authorization_base_url)
  session['oauth_state'] = state
  return redirect(auth_url)

@app.route('/token', methods=["GET"])
def token():
  onshape = OAuth2Session(client_id, state=session['oauth_state'], redirect_uri=redirect_url)
  token = onshape.fetch_token(token_url, client_secret=client_secret, authorization_response=request.url)
  session['oauth_token'] = token
  return redirect(url_for('.documents'))

@app.route('/documents', methods=["GET"])
def documents():
  extra = {
    'client_id': client_id,
    'client_secret': client_secret,
  }
  onshape = OAuth2Session(client_id, token=session['oauth_token'], redirect_uri=redirect_url)
  session['oauth_token'] = onshape.refresh_token(token_url, **extra)
  return jsonify(onshape.get('https://cad.onshape.com/api/v6/documents?q=Untitled&ownerType=1&sortColumn=createdAt&sortOrder=desc&offset=0&limit=20').json())

if __name__ == "__main__":
  app.run()
  
`

---

<a id="sec-api-guides-advanced"></a>
## API Guides (Advanced)

<a id="pg-docs-api-adv"></a>
### API Guides

_Source: <https://onshape-public.github.io/docs/api-adv/>_

Please refer to the pages in this section for more information on working with Onshape APIs.

---

###### [Assemblies](https://onshape-public.github.io/docs/api-adv/docs/api-adv/assemblies/)

###### [Associativity](https://onshape-public.github.io/docs/api-adv/docs/api-adv/associativity/)

###### [Billing](https://onshape-public.github.io/docs/api-adv/docs/api-adv/billing/)

###### [Configurations](https://onshape-public.github.io/docs/api-adv/docs/api-adv/configs/)

###### [Documents](https://onshape-public.github.io/docs/api-adv/docs/api-adv/documents/)

###### [Drawings](https://onshape-public.github.io/docs/api-adv/docs/api-adv/drawings/)

###### [Features](https://onshape-public.github.io/docs/api-adv/docs/api-adv/featureaccess/)

###### [Evaluating FeatureScript](https://onshape-public.github.io/docs/api-adv/docs/api-adv/fs/)

###### [Import & Export](https://onshape-public.github.io/docs/api-adv/docs/api-adv/translation/)

###### [Metadata](https://onshape-public.github.io/docs/api-adv/docs/api-adv/metadata/)

###### [Part Studios](https://onshape-public.github.io/docs/api-adv/docs/api-adv/partstudios/)

###### [Release Management](https://onshape-public.github.io/docs/api-adv/docs/api-adv/relmgmt/)

###### [Response Codes](https://onshape-public.github.io/docs/api-adv/docs/api-adv/errors/)

---

<a id="pg-docs-api-adv-associativity"></a>
### Associativity

_Source: <https://onshape-public.github.io/docs/api-adv/associativity/>_

Onshape does not expose a persistent ID for any of these entities. When the model changes, the ID may change. Therefore, Onshape provides an API to enable mapping IDs from a previous microversion to the current microversion. Assuming a simple case of maintaining associativity for a face, an abstract workflow might be:

1. Read the tessellated model data.
2. Select the face of interest.
3. Store the Face ID and Document Microversion ID for the face.
4. \[ user changes model \]
5. Call the REST API to translate from the known Face ID to an ID in the new model.
6. Re-apply application-specific data to the face(s) in the new model. Note that a face may become zero, one or multiple faces in the new model, depending on what changes the user made.

#### Associativity Example

1. Create a cube in Onshape:  
![image alt text](https://onshape-public.github.io/docs/api-adv/associativity/images/associativityimage03.png)
2. Get the document microversion ID from the URL: `https://cad.onshape.com/api/d/<docid>/w/<wid>/microversionId`.
3. Use the appropriate REST API to get the tessellated faces (`getPartStudioFaces`) and edges (`getPartStudioEdges`}. Note the ids:  
   * Part ID: `JHD`  
   * Front face ID: `JHO`  
   * Top edge of the front face ID: `JHd`  
   * Right edge of the top face ID: `JHt`
4. Split cube with the Front plane and translate the IDs:

![image alt text](https://onshape-public.github.io/docs/api-adv/associativity/images/associativityimage00.png)

**POST**

```
https://cad.onshape.com/api/partstudios/d/<docid>/w/<wid>/e/<eid>/idtranslations

```

**Body**:

`{
  "sourceDocumentMicroversion" : "47e75ab2ee8b4356a76ebd47",
  "ids" : ["JHD", "JHO", "JHd", "JHt"  ]
}
`

**Response**:

`{
    "documentId": "748d6e850c9248328189922b",
    "elementId": "042a6fa54e79451e8076463d",
    "sourceDocumentMicroversion": "47e75ab2ee8b4356a76ebd47",
    "ids": [
        { "source": "JHD", "status": "SPLIT", "target": ["JID", "JIH"] },
        { "source": "JHO", "status": "OK", "target": ["JHO"] },
        { "source": "JHd", "status": "OK", "target": ["JHd"] },
        { "source": "JHt", "status": "SPLIT", "target": ["JI5", "JI9"] }
    ],
    "targetDocumentMicroversion": "78bc7f3fcf82475085c2f3ab"
}
`

1. Delete one of the parts, and translate the IDs:

![image alt text](https://onshape-public.github.io/docs/api-adv/associativity/images/associativityimage01.png)

**POST**

```
https://cad.onshape.com/api/partstudios/d/<docid>/w/<wid>/e/<eid>/idtranslations

```

**Body**:

`{
  "sourceDocumentMicroversion" : "47e75ab2ee8b4356a76ebd47",
  "ids" : ["JHD", "JHO", "JHd", "JHt"]
}
`

**Response**:

`{
    "documentId": "748d6e850c9248328189922b",
    "elementId": "042a6fa54e79451e8076463d",
    "sourceDocumentMicroversion": "47e75ab2ee8b4356a76ebd47",
    "ids": [
        { "source": "JHD", "status": "OK", "target": ["JID"] },
        { "source": "JHO", "status": "FAILED_TO_RESOLVE", "target": [] },
        { "source": "JHd", "status": "FAILED_TO_RESOLVE", "target": [] },
        { "source": "JHt", "status": "OK", "target": ["JI5"] }
    ],
    "targetDocumentMicroversion": "52aa74d34b624f3aaef33204"
}
`

1. Roll back the delete and the split, and translate the IDs:

![image alt text](https://onshape-public.github.io/docs/api-adv/associativity/images/associativityimage02.png)

**POST**

```
https://cad.onshape.com/api/partstudios/d/<docid>/w/<wid>/e/<eid>/idtranslations

```

**Body**:

`{
  "sourceDocumentMicroversion" : "47e75ab2ee8b4356a76ebd47",
  "ids" : ["JHD", "JHO", "JHd", "JHt"]
}
`

**Response**:

`{
    "documentId": "748d6e850c9248328189922b",
    "elementId": "042a6fa54e79451e8076463d",
    "sourceDocumentMicroversion": "47e75ab2ee8b4356a76ebd47",
    "ids": [
        { "source": "JHD", "status": "OK", "target": ["JID"] },
        { "source": "JHO", "status": "OK", "target": ["JHO"] },
        { "source": "JHd", "status": "OK", "target": ["JHd"] },
        { "source": "JHt", "status": "OK", "target": ["JHt"] }
    ],
    "targetDocumentMicroversion": "52aa74d34b624f3aaef33204"
}
`

---

<a id="pg-docs-api-adv-billing"></a>
### Billing

_Source: <https://onshape-public.github.io/docs/api-adv/billing/>_

This document describes APIs that will allow partners to interact with the Onshape billing system.

#### Overview

All billing is done through “plans” that are created in the Developer Portal. A “plan” has the following attributes:

| Name (also called SKU) | A unique (within your company) plan name                                   |
| ---------------------- | -------------------------------------------------------------------------- |
| Description            | A user-visible description of the plan                                     |
| Amount                 | The cost of the plan (may be one-time or recurring, depending on the type) |
| Type                   | Monthly, One-time or Consumable                                            |

Onshape defines three kinds of plans:

| Plan type                        | Description                                                                                                                                                                                                                                                 |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Recurring (Monthly Subscription) | A plan that is renewed monthly at a fixed cost. All Apps in the app store must have a Free monthly plan (which is created by default), and may have additional paid plans.                                                                                  |
| One-time                         | A plan that is purchased once (not renewed monthly). A user may purchase these multiple times.                                                                                                                                                              |
| Consumable                       | A plan that represents a consumable unit, such as "hours of rendering" or “simulation runs”. Consumable plans are not fully implemented at this time, but the consumable functionality can be implemented using One-time Purchase plans as described below. |

Users may purchase plans through the App Store interface. In addition, if your application has the OAuth Purchase Scope, your application can initiate “in-app” purchases by calling Onshape to request a purchase.

The basic steps for interacting with Onshape Billing:

1. Define one or more plans using the Developer Portal interface
2. Use the Onshape API to determine the current user’s plan
3. Provide features and/or limits based on the current plan

#### Using the Onshape Billing API

`GET /api/accounts/purchases`

Returns a list of purchase made by the current user for plans owned by the current application. Use this information to determine what capabilities or features the user is entitled to use.

`DELETE /api/accounts/purchases/<purchase id>`

Cancel a recurring purchase.

`POST /api/accounts/purchases/<purchase id>/consume`

Indicate the use of a consumable. (Not fully implemented at this time)

`GET /api/billing/plans/client/<client id>`

Get a list of the billing plans defined for this client.

#### Initiating a purchase from an application (in-app purchases)

To initiate a purchase of a subscription or one time item you must set the browser’s location to particular URL within the Onshape stack:

`https://cad.onshape.com/billing/purchase?redirectUri=RRRR&clientId=CCCC&sku=SSSS&userId=UUUU`

Each of the query parameters should be URL encoded. The clientId is your application’s OAuth Client ID, the sku is the name/sku field for an item (you can find this in the developer portal or it’s retrievable through the /api/billing/plans REST endpoints). The user Id should be the Onshape user Id for the current user and is available through the /api/users/session REST endpoint. The redirectUri is the URI the user will be returned to within your website when the purchase is finished.

When the browser’s location is changed to this pattern the Onshape stack will serve content to confirm the users identity, confirm the details of what is being purchased (or obtained if the item is free) and then after the user agrees to the purchase will confirm the transaction (with our payment processor if the item is not free) and then redirect the user back to the supplied redirectUri (the browser location will be changed to the redirectUri). Additionally Onshape will add a `success=true` or `success=false` query parameter to the redirectURI indicating whether the user completed successfully (payment was taken if required etc.) or failed, either due to cancelling the purchase or an issue with payment.

When the browser fetches the redirectUri your application must call back through the `/api/account/purchases` API to get confirmation of the purchase - do NOT assume that a fetch of the redirectUri with a `success=true` query parameter actually indicates a purchase has occurred. Query the Onshape stack with the `/api/account/purchases` API to ensure that the required item has actually been bought.

#### Consumable Items

A detailed description of the interface for managing consumable purchases will be provided shortly. You can use one-time plans to achieve similar results:

1. Define a one-time purchase plan with a description indicating the nature of the purchase, for example:  
RENDER-10 Ten rendering hours $100
2. Keep track of the number of hours that the user has consumed. You can store and retrieve this information in Onshape using the following APIs. These APIs allow you to store and retrieve arbitrary information on a per-user basis.  
POST /applications/clients/:cid/settings/users/:uid GET /applications/clients/:cid/settings/users/:uid
3. Check the number of available “units” by getting the purchases and the record of consumables. Be sure to include UI in your application that the user can use to see their remaining quantity.
4. Alternately, you can store the consumption data in your own system; you do not need to use the Onshape API to manage that data.

Onshape intends to provide a richer set of APIs that help track the purchase and consumption of consumables in the near future.

#### Other billing models

You can use these mechanisms to implement other models. For example, a time-limited trial could be implemented by scanning purchases for the first “purchase” and denying service if it is more than a defined number of days in the past. A “fixed number of uses per month” could be implemented as a monthly subscription, string usage data with the settings API, and denying service after a fixed number of uses.

#### Samples

Onshape will provide sample code for both desktop and integrated applications demonstrating the use of the billing APIs and workflow. If you are subscribed to the Onshape Github Partner group, you will have access to those samples as soon as they are posted.

#### Testing

Please contact [support](mailto:api-support@onshape.com) to discuss details of testing billing & subscriptions.

---

<a id="pg-docs-api-adv-configs"></a>
### Configurations

_Source: <https://onshape-public.github.io/docs/api-adv/configs/>_

This page describes the APIs Onshape provides for working with [configurations](https://cad.onshape.com/help/Content/configurations.htm).

You can use configurations to create variations of entire Part Studios, assemblies, specific parts and more. You can configure feature and parameter values, part properties, custom part properties, face and part appearances, and sketch text. Each Part Studio can have only one configuration, but it can contain multiple configuration inputs. The configuration inputs you define for a Part Studio become options when inserting that Part Studio into an assembly or drawing. You can also create configurations for an assembly, regardless of any existing Part Studio configurations. Assembly configurations work the same way as Part Studio configurations, but are limited to configuring mates (_not_ mate connectors), instances, and patterns.

| PrerequisitesAll Onshape API calls must be properly authenticated.See the [API Keys](https://onshape-public.github.io/docs/api-adv/configs/docs/auth/apikeys) page for instructions and the [Quick Start](https://onshape-public.github.io/docs/api-adv/configs/docs/api-intro/quickstart) for an example.All applications submitted to the Onshape App Store _must_ authenticate with [OAuth2](https://onshape-public.github.io/docs/api-adv/configs/docs/auth/oauth).For Standard accounts, replace {baseUrl} with cad in all endpoints. For Enterprise accounts, replace it with your company domain. Add /api and the version number, and then provide the endpoint.https://{baseUrl}.onshape.com/api/v10/documentshttps://cad.onshape.com/api/v10/documentshttps://companySubDomain.onshape.com/api/v10/documentsOnshape IDs are written as: {did}, {wvmid}, {eid}, {pid}, {otherId}.These represent document, workspace (or version or microversion), element, part, and other IDs, respectively.See [API Guide: API Intro](https://onshape-public.github.io/docs/api-adv/configs/docs/api-intro/#onshape-api-request) for information on what these IDs mean and how to obtain them from your documents.Variables are written as: {variableId1} or <variableIdTwo>.These represent variables that must be replaced in the code before it is usable.Never include the braces {} or angle brackets <> with your IDs/variables.This page provides sample code in cURL and python.For additional instruction and video content, visit the Learning Center’s [Intro to the Onshape API](https://learn.onshape.com/learn/course/intro-to-the-onshape-api/intro-to-the-onshape-api/what-is-an-api?page=1) course. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

#### Endpoints

* [getConfiguration](https://cad.onshape.com/glassworks/explorer/#/Element/getConfiguration): Get the configuration data for a Part Studio or Assembly.  
```  
curl -X 'GET' \  
    'https://cad.onshape.com/api/v6/elements/d/{did}/wvm/{wvmid}/e/{eid}/configuration' \  
    -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS'\  
    -H 'Content-Type: application/json;charset=UTF-8; qs=0.09'  
```
* [updateConfiguration](https://cad.onshape.com/glassworks/explorer/#/Element/updateConfiguration): Update the configuration data for a Part Studio or Assembly.  
```  
curl -X 'POST' \  
    'https://cad.onshape.com/api/v6/elements/d/{did}/wvm/{wvmid}/e/{eid}/configuration' \  
    -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS'\  
    -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
    -d '{ }'  
```
* [decodeConfiguration](https://cad.onshape.com/glassworks/explorer/#/Element/decodeConfiguration): Process an encoded configuration file.  
```  
curl -X 'GET' \  
    'https://cad.onshape.com/api/v6/elements/d/{did}/wvm/{wvmid}/e/{eid}/configurationencodings/{encodingId}' \  
    -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS'  
```
* [encodeConfigurationMap](https://cad.onshape.com/glassworks/explorer/#/Element/encodeConfigurationMap): Create an encoded map of configurations.  
```  
curl -X 'POST' \  
    'https://cad.onshape.com/api/v6/elements/d/{did}/e/{eid}/configurationencodings' \  
    -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS'\  
    -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
    -d '{  
        "parameters": [  
        {  
            "parameterId": "{parameterId}",  
            "parameterValue": "{configValue}"  
        }  
        ]  
    }'  
```

##### Encoded configurations

The [encodeConfigurationMap](https://cad.onshape.com/glassworks/explorer/#/Element/encodeConfigurationMap) and [decodeConfiguration](https://cad.onshape.com/glassworks/explorer/#/Element/decodeConfiguration) APIs convert parameters from JSON to URL-encoded strings.

For example,

`{
    "parameters": [
        {
        "parameterId": "List_izOjbm5HCRXEld",
        "parameterValue": "_500_mm"
        }
    ]
}
`

encodes to:

`{
    "encodedId": "List_sCW2T7xBCmN6an=_500_mm",
    "queryParam": "configuration=List_izOjbm5HCRXEld%3D_500_mm"
}
`

* You can use the `encodedId` in request bodies. See [Export a configured assembly](#export-a-configured-assembly-asynchronous) for an example.
* You can use the `queryParam` as a query parameter. See [Export a configured part](#export-a-configured-part-synchronous) for an example.  
   * Note that the value includes the parameter name within it for convenience. Be careful when copy and pasting. It might be helpful to think of these values as: `{queryParam} = "configuration={encodedString}"`.  
   * When using the Onshape [API Explorer](https://cad.onshape.com/glassworks/explorer/), use only the `{encodedString}` in any `configuration` query parameter fields.

##### Configured parts

> **IMPORTANT NOTE**
> 
> Configured parts each have a unique part ID. Changing the configuration for a part changes the part ID.

##### Configuration visibility conditions

You can adjust the conditions under which a configuration input is visible. See [Help: Setting visibility conditions](https://cad.onshape.com/help/Content/configurations.htm#config%5Fvisibility) for details.

When working with visibility conditions in the API, note that:

* The configuration endpoints include a `visibilityCondition` attribute for every configuration input.
* The GET configuration endpoints include an `isVisible` attribute for every configuration input.

**Visibility condition errors**

* Configuration endpoints in v1 through v9 of the Onshape API will silently repair any bad visibility conditions.
* Configuration endpoints in v10 or later will return a 400 error when bad visibility conditions are detected.

#### Sample Workflows

These sample workflows all build off one another. Completing all of the workflows will take you step-by-step through the process of getting Configuration information, encoding the information for use, and using the encoded configuration to create a configured export. You can also watch the [video](#workflow-video) to see the entire workflow in the Glassworks API Explorer.

The general workflow for working with configurations is:

1. Call [getConfiguration](https://cad.onshape.com/glassworks/explorer/#/Element/getConfiguration) to get the configuration details.
2. Call [encodeConfigurationMap](https://cad.onshape.com/glassworks/explorer/#/Element/encodeConfigurationMap) to encode the configuration string.
3. Use the encoded configuration string in other Onshape API calls, like exporting a configured Part Studio or Assembly.

##### Get a configuration

In this example, we’ll use the [getConfiguration](https://cad.onshape.com/glassworks/explorer/#/Element/getConfiguration) endpoint to get the Configuration information from a Part Studio.

1. Make a copy of [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/958bceb5a2511b572dbbe851). Make a note of the new document’s document ID, workspace ID, and element ID.
2. Click the Configurations dropdown in the Features list, and observe that there are two options for the drillbit length, `250 mm` and `500 mm`.  
    
![ ](https://onshape-public.github.io/docs/api-adv/configs/images/configs-example-ui.png)
3. Set up a call to the [getConfiguration](https://cad.onshape.com/glassworks/explorer/#/Element/getConfiguration) endpoint to get the Configuration for the Part Studio. Don’t forget to replace the URL parameters with the IDs from your copy of the document, and replace `CREDENTIALS` with your authorization credentials.  
```  
curl -X 'GET' \  
    'https://cad.onshape.com/api/v6/elements/d/{did}/w/{wid}/e/{eid}/configuration' \  
    -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS' \  
```
4. Review the Configuration information detailed in the response. You can see that the Part Studio contains one configuration (`Drill_Bit_Length`) with two options (`250 mm` and `500 mm`).  
```  
{  
"btType": "BTConfigurationResponse-2019",  
"currentConfiguration": [  
    {  
    "btType": "BTMParameterEnum-145",  
    "namespace": "",  
    "nodeId": "{nodeId1}",  
    "enumName": "{enumName}",  
    "value": "Default",  
    "parameterId": "{paramId}"  
    }  
],  
"configurationParameters": [  
    {  
    "btType": "BTMConfigurationParameterEnum-105",  
    "enumName": "{enumName}",  
    "namespace": "",  
    "defaultValue": "Default",  
    "options": [  
        {  
        "btType": "BTMEnumOption-592",  
        "optionName": "250 mm",  
        "option": "Default",  
        "nodeId": "{nodeId2}"  
        },  
        {  
        "btType": "BTMEnumOption-592",  
        "optionName": "500 mm",  
        "option": "_500_mm",  
        "nodeId": "{nodeId3}"  
        }  
    ],  
    "visibilityCondition": {  
        "btType": "BTParameterVisibilityCondition-177"  
    },  
    "isCosmetic": false,  
    "parameterId": "{paramId}",  
    "parameterName": "Drill_Bit_Length",  
    "nodeId": "{nodeId4}"  
    }  
],  
"serializationVersion": "1.2.7",  
"sourceMicroversion": "{mid}",  
"microversionSkew": false,  
"rejectMicroversionSkew": false,  
"libraryVersion": 2522  
}  
```

##### Encode a configuration string

In this example, we’ll encode a Configuration so it can be used in other API calls. Please read the [Encoded Configuration Strings](#encoded-configuration-strings) section before beginning this example.

1. This example builds off the previous one. Please complete the [Get a Part Studio Configuration](#get-a-configuration) workflow to obtain the raw Configuration output for the Part Studio.
2. Set up a call to the [encodeConfigurationMap](https://cad.onshape.com/glassworks/explorer/#/Element/encodeConfigurationMap) endpoint. Don’t forget to replace the URL parameters with the IDs from your document, and replace `CREDENTIALS` with your authorization credentials.  
```  
curl -X 'POST' \  
    'https://cad.onshape.com/api/v6/elements/d/{did}/e/{eid}/configurationencodings' \  
    -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS' \  
    -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
    -d '{ }'  
```
3. Now we need to create our JSON body for the request. Note the structure of the body:  
```  
{  
"parameters": [  
    {  
    "parameterId": "string",  
    "parameterValue": "string"  
    }  
],  
"standardContentParametersId": "string"  
}  
```  
Fill out the request body with our information:  
   * We’re not using a standard content part, so we can delete the second key/value pair.  
   * The parameterId can be found in the response from the previous example.  
   * For the parameter value, we’ll enter one of our configuration options from the previous example. In this case, we’ll use `_500_mm` to export a 500 mm drillbit part. Note that we use the `option` and NOT the `optionName` for the parameter value.  
```  
{  
"parameters": [  
    {  
    "parameterId": "{parameterId}",  
    "parameterValue": "_500_mm"  
    }  
]  
}  
```
4. Now we can make our call:  
```  
curl -X 'POST' \  
   'https://cad.onshape.com/api/v6/elements/d/{did}/e/{eid}/configurationencodings' \  
   -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
   -H 'Authorization: Basic CREDENTIALS' \  
   -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
   -d '{  
        "parameters": [  
       {  
           "parameterId": "{parameterId}",  
           "parameterValue": "_500_mm"  
       }  
       ]  
   }'  
```
5. The call responds with two values: the ID of the encoding, and the encoded configuration string (usually begins with `configuration=`). We can use these values in other API calls to refer to this specific configuration.  
```  
{  
    "encodedId": "{encodedId}",  
    "queryParam": "{queryParam}"  
}  
```

##### Export a configured part (synchronous)

In this example, we will export a configured part. We have a drillbit with two configurations: `250 mm` and `500 mm` lengths. To export a 500 mm drillbit, we can specify the configuration as part of the export.

**Endpoint**

[GET /partstudios/d/did/w/wid/e/eid/parasolid](https://cad.onshape.com/glassworks/explorer/#/PartStudio/exportParasolid)

**Query Params**

```
{
    "includeExportIds": false,
    "configuration": {queryParam}
    "binaryExport": false'
}

```

1. This example builds off the previous two. Please complete this exercise after the [Encode a configuration](#encode-a-configuration) workflow.
2. Next, set up a call to the [PartStudio/exportParasolid](https://cad.onshape.com/glassworks/explorer/#/PartStudio/exportParasolid) endpoint.  
   * Don’t forget to replace the URL parameters with the IDs from your document, and replace `CREDENTIALS` with your authorization credentials.  
   * Note that this endpoint includes an optional `configuration` path parameter. We’ll replace the entire parameter with the `{queryParam}` from the previous step. Remember that `{queryParam}` is in the format of `configuration={encodedString}`.  
```  
curl -X 'GET' \  
    'https://cad.onshape.com/api/v6/partstudios/d/{did}/w/{wid}/e/{eid}/parasolid?includeExportIds=false&{queryParam}&binaryExport=false' \  
    -H 'Accept: */*' \  
    -H 'Authorization: Basic CREDENTIALS' \  
```
3. This endpoint returns a redirect URL. Navigate to the returned URL in your browser to download the export.  
   * Hint: The URL will look something like this, but with different IDs:  
```  
https://cad.onshape.com/api/v6/partstudios/d/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/958bceb5a2511b572dbbe851/parasolid?includeExportIds=false&configuration=List_izOjbm5HCRXEld%253D_500_mm&binaryExport=false  
```
4. Now we need to import our Parasolid to confirm the correct configuration was used. Open your document in the Onshape UI, click the Insert new tab button, and then select Import.  
![Insert new tab menu with Import highlighted in Onshape UI](https://onshape-public.github.io/docs/api-adv/configs/images/configs-insert-menu.png)
5. Navigate to the export you downloaded (with the `.x_t` extension) and import it into Onshape.
6. Use the measure tool to confirm the length of the imported drillbit is 500 mm.  
![Measure tool in Onshape UI showing drill length as 500 mm](https://onshape-public.github.io/docs/api-adv/configs/images/configs-measure-tool.png)

##### Export a configured assembly (asynchronous)

**Endpoint**

[POST /assemblies/d/did/w/wid/e/eid/translations](https://cad.onshape.com/glassworks/explorer/#/Assembly/translateFormat)

**Request Body**

```
{
    "angularTolerance": 0.001,
    "distanceTolerance": 0.01,
    "formatName": "{formatName}",
    "resolution": "fine",
    "configuration": "{encodedId}"
}

```

In this example, we will export a configured assembly. The assembly a configured part with two options: `250 mm` and `500 mm` lengths. To export an assembly that uses the `500 m` drill length, we can specify the configuration as part of the export.

1. Follow the [Get a configuration ](#get-a-configuration)steps to get the configuration details for the [DRILL\_CHUCK assembly](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/bfc8e0f5a1b9e7f91d4bcea7)  
**Request**  
```  
curl -X 'GET' \  
  'https://cad.onshape.com/api/v10/elements/d/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/bfc8e0f5a1b9e7f91d4bcea7/configuration' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS'  
```  
**Response**  
`{  
    "btType": "BTConfigurationResponse-2019",  
    "rejectMicroversionSkew": false,  
    "microversionSkew": false,  
    "currentConfiguration": [],  
    "configurationParameters": [  
        {  
        "btType": "BTMConfigurationParameterEnum-105",  
        "parameterId": "List_sCW2T7xBCmN6an",  
        "isCosmetic": false,  
        "enumName": "List_sCW2T7xBCmN6an_conf",  
        "enumOptionVisibilityConditions": {  
            "btType": "BTEnumOptionVisibilityConditionList-2936",  
            "visibilityConditions": []  
        },  
        "options": [  
            {  
            "btType": "BTMEnumOption-592",  
            "optionName": "250 mm",  
            "option": "Default",  
            "nodeId": "MWGwNOdlW3UaUCPd+"  
            },  
            {  
            "btType": "BTMEnumOption-592",  
            "optionName": "500 mm",  
            "option": "_500_mm",  
            "nodeId": "MpgGz9fyFlSDGq22Y"  
            }  
        ],  
        "namespace": "",  
        "defaultValue": "Default",  
        "nodeId": "MIqFliu7ft3jF/xLO",  
        "parameterName": "Configuration",  
        "visibilityCondition": {  
            "btType": "BTParameterVisibilityCondition-177"  
        }  
        }  
    ],  
    "libraryVersion": 2641,  
    "sourceMicroversion": "18743880b25d66c7c5742bf9",  
    "serializationVersion": "1.2.10"  
    }  
`
2. Follow the [Encode a configuration](#encode-a-configuration) steps to encode the configuration for the `500 mm` option using the following values from the previous response:  
   * `"parameterId": "List_sCW2T7xBCmN6an"`  
   * `"option": "_500_mm"`  
**Request**  
```  
curl -X 'POST' \  
    'https://cad.onshape.com/api/v10/elements/d/e60c4803eaf2ac8be492c18e/e/bfc8e0f5a1b9e7f91d4bcea7/configurationencodings' \  
    -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS'  \  
    -d '{  
        "parameters": [  
            {  
            "parameterId": "List_sCW2T7xBCmN6an",  
            "parameterValue": "_500_mm"  
            }  
        ]  
    }'  
```  
**Response**  
`{  
    "encodedId": "List_sCW2T7xBCmN6an=_500_mm",  
    "queryParam": "configuration=List_sCW2T7xBCmN6an%3D_500_mm"  
}  
`
3. Next, set up a call to the [Assembly/translateFormat](https://cad.onshape.com/glassworks/explorer/#/Assembly/translateFormat) endpoint. Don’t forget to replace the URL parameters with the IDs from your document, and replace `CREDENTIALS` with your authorization credentials. Note that this endpoint includes an optional `configuration` field in the request body. This is where we’ll enter the `encodedId` (`"List_sCW2T7xBCmN6an=_500_mm"`) from the last step.  
**Request**  
```  
curl -X 'POST' \  
    'https://cad.onshape.com/api/v10/assemblies/d/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/bfc8e0f5a1b9e7f91d4bcea7/translations' \  
    -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS'  \  
    -d '{  
        "angularTolerance": 0.001,  
        "distanceTolerance": 0.01,  
        "formatName": "STEP",  
        "resolution": "fine",  
        "configuration": "List_sCW2T7xBCmN6an=_500_mm"  
    }'  
```
4. Next, poll the [Translation/getTranslation](https://cad.onshape.com/glassworks/explorer/#/Translation/getTranslation) response (using the `id` from the last response as the `translationId`) until `requestState` changes from `ACTIVE` to `DONE` or `FAILED`. Once `requestState=DONE`, make a note of the `resultElementId` in the response. This is the element ID of the blob with the exported file.
5. Call [BlobElement/downloadFileWorkspace](https://cad.onshape.com/glassworks/explorer/#/BlobElement/downloadFileWorkspace) to retrieve the exported results.**Request**  
```  
curl -X 'GET' \  
'https://cad.onshape.com/api/v6/blobelements/d/{did}/w/{wid}/e/{resultElementId}' \  
  -H 'accept: application/octet-stream' \  
  -H 'Authorization: Basic CREDENTIALS' \  
```
6. Now we need to import our file to confirm the correct configuration was used. You can either:  
   * Call the [createTranslation](https://cad.onshape.com/glassworks/explorer/#/Translation/createTranslation) endpoint.  
   * Open your document in the Onshape UI, click the Insert new tab button, and then select **Import**.
7. In Onshape, use the measure tool to confirm the length of the dill in the imported assembly is 500 mm.

#### Workflow Video

This video demonstrates how to get a configuration, encode it, and use the encoded configuration string in a synchronous export.  

#### Additional Resources

* [API Explorer: Configurations](https://cad.onshape.com/glassworks/explorer/#/Element)
* [API Guide: API Explorer](https://onshape-public.github.io/docs/api-adv/configs/docs/api-intro/explorer)
* [Onshape Help: Configurations](https://cad.onshape.com/help/Content/configurations.htm)

---

<a id="pg-docs-api-adv-documents"></a>
### Documents

_Source: <https://onshape-public.github.io/docs/api-adv/documents/>_

This page describes the APIs Onshape provides for working with documents.

| PrerequisitesAll Onshape API calls must be properly authenticated.See the [API Keys](https://onshape-public.github.io/docs/api-adv/documents/docs/auth/apikeys) page for instructions and the [Quick Start](https://onshape-public.github.io/docs/api-adv/documents/docs/api-intro/quickstart) for an example.All applications submitted to the Onshape App Store _must_ authenticate with [OAuth2](https://onshape-public.github.io/docs/api-adv/documents/docs/auth/oauth).For Standard accounts, replace {baseUrl} with cad in all endpoints. For Enterprise accounts, replace it with your company domain. Add /api and the version number, and then provide the endpoint.https://{baseUrl}.onshape.com/api/v10/documentshttps://cad.onshape.com/api/v10/documentshttps://companySubDomain.onshape.com/api/v10/documentsOnshape IDs are written as: {did}, {wvmid}, {eid}, {pid}, {otherId}.These represent document, workspace (or version or microversion), element, part, and other IDs, respectively.See [API Guide: API Intro](https://onshape-public.github.io/docs/api-adv/documents/docs/api-intro/#onshape-api-request) for information on what these IDs mean and how to obtain them from your documents.Variables are written as: {variableId1} or <variableIdTwo>.These represent variables that must be replaced in the code before it is usable.Never include the braces {} or angle brackets <> with your IDs/variables.This page provides sample code in cURL and python.For additional instruction and video content, visit the Learning Center’s [Intro to the Onshape API](https://learn.onshape.com/learn/course/intro-to-the-onshape-api/intro-to-the-onshape-api/what-is-an-api?page=1) course. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

#### Examples

See all Document endpoints here: <https://cad.onshape.com/glassworks/explorer/#/Document>

---

##### Create a document

Create a new Onshape document named `myDocument`.

**Endpoint**

[POST /api/v10/documents](https://cad.onshape.com/glassworks/explorer/#/Document/createDocument)

**Request Body**

`{
  "name": "myDocument"
}
`

_Additional optional fields available. See the [API Explorer](https://cad.onshape.com/glassworks/explorer/#/Document/createDocument) for a full list._

**Example**

Make sure you are logged into your Onshape account, and then call the `createDocument` endpoint. In this example, we set the new document name as `myDocument`.

* cURL
* python

`curl -X 'POST' \
  'https://{baseUrl}.onshape.com/api/v10/documents' \
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \
  -H 'Authorization: Basic {credentials}' \
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09'  \
  -d '{
        "name": "myDocument"
      }'
`

`import requests 
import json

auth = (access_key, secret_key) # See Authentication guide
headers = {
  'Accept': 'application/json;charset=UTF-8;qs=0.09',
  'Content-Type': 'application/json;charset=UTF-8; qs=0.09'
}

api_url = "https://{baseUrl}.onshape.com/api/v10/documents/"
queryParams = {}
body = {
  "name": "myDocument"
}

response = requests.post( api_url, 
                          params=queryParams, 
                          json=body, 
                          auth=auth, 
                          headers=headers )
print(json.dumps(response.json(), indent=4))
`

The new document is created in your Onshape account; the new document ID (`{did}`) is returned in the response body and appears in the new document’s URL.

---

##### Get a document by ID

Search for [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/3dcd747f9d8bb6a6687fcb53) by document ID (`e60c4803eaf2ac8be492c18e`).

**Endpoint**

[GET /api/v10/documents/{did}](https://cad.onshape.com/glassworks/explorer/#/Document/getDocument)

**Example**

1. Call the [getDocument](https://cad.onshape.com/glassworks/explorer/#/Document/getDocument) endpoint on the document ID of [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/3dcd747f9d8bb6a6687fcb53): `e60c4803eaf2ac8be492c18e`.  
   * cURL  
   * python  
`curl -X 'GET' \  
  'https://cad.onshape.com/api/v10/documents/e60c4803eaf2ac8be492c18e' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic {credentials}' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09'  
`  
`import requests  
import json  
auth = (access_key, secret_key) # See Authentication guide  
headers = {  
  'Accept': 'application/json;charset=UTF-8;qs=0.09',  
  'Content-Type': 'application/json;charset=UTF-8; qs=0.09'  
}  
api_url = "https://cad.onshape.com/api/v10/documents/e60c4803eaf2ac8be492c18e"  
queryParams = {}  
response = requests.get(api_url,  
                        params=queryParams,  
                        auth=auth,  
                        headers=headers)  
print(json.dumps(response.json(), indent=4))  
`
2. Scroll to the end of the response and confirm that it matches the information below:  
`{  
  ...  
  "name": "Onshape API Guide",  
  "id": "e60c4803eaf2ac8be492c18e",  
  "href": "https://cad.onshape.com/api/v10/documents/e60c4803eaf2ac8be492c18e"  
}  
`

---

##### Get documents by search criteria

| Document Search NotesThe Onshape API enables you to search for documents in the same way as the Onshape UI.The filter query parameter corresponds to the search options on the Documents page in the Onshape UI; you can filter your results to only include Public documents, documents owned by your company, documents you created, etc. The other query parameters available will sort your results, not filter them. The best matches will appear first, followed by partial matches.![](https://onshape-public.github.io/docs/api-adv/documents/images/document-search-filters.png)To combine multiple filters (for example, all public documents owned by your company), you should filter for one criteria (i.e. "filter": 7 && "ownerId": {ownerId} to retrieve all documents owned by your company), then programmatically remove all results that are not public. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Search for [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/3dcd747f9d8bb6a6687fcb53) by name (`"Onshape API Guide"`) and owner ID (`629677dbd020f032bea73ef7`). Return 1 result in the list.

**Endpoint**

[GET /api/v10/documents](https://cad.onshape.com/glassworks/explorer/#/Document/getDocuments)

**Query Parameters**

`{
  "q": "Onshape API Guide",
  "filter": 7,
  "owner": "{ownerId}",
  "ownerType": 1,
  "sortColumn": "createdAt",
  "sortOrder": "desc",
  "offset": 0,
  "limit": 1
}
`

_Additional optional fields available. See the [API Explorer](https://cad.onshape.com/glassworks/explorer/#/Document/getDocuments) for a full list._

**Example**

1. Make sure you’re logged into your Onshape account, and then form the search query for your call. In this example, we want to locate the Onshape-owned `Onshape API Guide` document. We only want to return this one document.
2. Call the [getDocuments](https://cad.onshape.com/glassworks/explorer/#/Document/getDocuments) endpoint:  
   * cURL  
   * python  
`curl -X 'GET' \  
'https://cad.onshape.com/api/v10/documents?q=Onshape%20API%20Guide&filter=7&owner=629677dbd020f032bea73ef7&ownerType=1&sortColumn=createdAt&sortOrder=desc&offset=0&limit=1' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic {credentials}' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09'  
`  
`import requests  
import json  
auth = (access_key, secret_key) # See Authentication guide  
headers = {  
  'Accept': 'application/json;charset=UTF-8;qs=0.09',  
  'Content-Type': 'application/json;charset=UTF-8; qs=0.09'  
}  
api_url = "https://cad.onshape.com/api/v10/documents"  
queryParams = {  
    "q": "Onshape API Guide",  
    "filter": 7, # search by company owner  
    "owner": "629677dbd020f032bea73ef7", # owner company ID  
    "ownerType": 1, # company owned  
    "sortColumn": "createdAt",  
    "sortOrder": "desc",  
    "offset": 0,  
    "limit": 1  
  }  
response = requests.get(api_url,  
                        params=queryParams,  
                        auth=auth,  
                        headers=headers)  
print(json.dumps(response.json(), indent=4))  
`
3. In the response, one `item` should be returned. Scroll to the `owner` block and confirm that the owner name is `"Onshape Training Repo"`.  
`"owner": {  
      "type": 1,  
      "isEnterpriseOwnedResource": false,  
      "image": null,  
      "name": "Onshape Training Repo",  
      "id": "629677dbd020f032bea73ef7",  
      "href": "https://cad.onshape.com/api/v10/companies/629677dbd020f032bea73ef7"  
  }  
`

---

##### Update document attributes

Make a copy of [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/3dcd747f9d8bb6a6687fcb53), and change the name of the new document to `My API Doc`.

**Endpoint**

[POST /api/v10/documents/{did}](https://cad.onshape.com/glassworks/explorer/#/Document/updateDocumentAttributes)

**Request Body**

`{
  "name": "My API Doc",
  "description": "Update document description here."
}
`

_Additional optional fields available. See the [API Explorer](https://cad.onshape.com/glassworks/explorer/#/Document/updateDocumentAttributes) for a full list._

**Example**

1. Make a copy of [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/3dcd747f9d8bb6a6687fcb53), and make a note of the _new_ document ID in the URL.
2. In this example, we’ll change the document name from `Onshape API Guide - Copy` to `My API Doc`.
3. Call the [updateDocumentAttributes](https://cad.onshape.com/glassworks/explorer/#/Document/updateDocumentAttributes) on new document ID from Step 1\. Specify the new document name in the request body.  
   * cURL  
   * python  
`curl -X 'POST' \  
  'https://{baseUrl}.onshape.com/api/v10/documents/{did}' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic {credentials}' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
          "name": "My API Doc"  
      }'  
`  
`import requests  
import json  
auth = (access_key, secret_key) # See Authentication guide  
headers = {  
  'Accept': 'application/json;charset=UTF-8;qs=0.09',  
  'Content-Type': 'application/json;charset=UTF-8; qs=0.09'  
}  
api_url = "https://{baseUrl}.onshape.com/api/v10/documents/{did}"  
queryParams = {}  
body = {  
  "name": "My API Doc"  
}  
response = requests.post( api_url,  
                          params=queryParams,  
                          json=body,  
                          auth=auth,  
                          headers=headers)  
print(json.dumps(response.json(), indent=4))  
`
4. Navigate to your document in Onshape, and confirm that the document’s name is updated.  
    
![](https://onshape-public.github.io/docs/api-adv/documents/images/DocumentsGuideNewName.png)

---

##### Get a list of elements in a document

Get a list of all elements (tabs) in [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/3dcd747f9d8bb6a6687fcb53).

**Endpoint**

[GET /api/v10/documents/d/{did}/{wvm}/{wvmid}/elements](https://cad.onshape.com/glassworks/explorer/#/Document/getElementsInDocument)

**Example**

1. Open [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/3dcd747f9d8bb6a6687fcb53), and make a note of the document and workspace IDs in the URL.  
    
![](https://onshape-public.github.io/docs/api-adv/documents/images/DocumentsGuideGetElements.png)  
   * `did: e60c4803eaf2ac8be492c18e`  
   * `wvm: w`  
   * `wid: d2558da712764516cc9fec62`
2. Call the [getElementsInDocument](https://cad.onshape.com/glassworks/explorer/#/Document/getElementsInDocument) endpoint on the document and workspace:  
   * cURL  
   * python  
`curl -X 'GET' \  
  'https://cad.onshape.com/api/v10/documents/d/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/elements' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic {credentials}' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09'  
`  
`import requests  
import json  
auth = (access_key, secret_key) # See Authentication guide  
headers = {  
  'Accept': 'application/json;charset=UTF-8;qs=0.09',  
  'Content-Type': 'application/json;charset=UTF-8; qs=0.09'  
}  
api_url = "https://cad.onshape.com/api/v10/documents/d/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/elements"  
queryParams = {}  
response = requests.get(api_url,  
                        params=queryParams,  
                        auth=auth,  
                        headers=headers)  
print(json.dumps(response.json(), indent=4))  
`
3. The response returns a code block for each tab in the document. Confirm that your response includes the tab names from the document, including `ENG_BLOCK` and `CRANK`:  
`[  
  {  
    "name": "ENG_BLOCK",  
    "id": "9ff7abbba6852dc4d0bce252",  
    "type": "Part Studio",  
    "elementType": "PARTSTUDIO",  
    ...  
  },  
  {  
    "name": "CRANK",  
    "id": "6bed6b43463f6a46a37b4a22",  
    "type": "Part Studio",  
    "elementType": "PARTSTUDIO",  
    ...  
  }  
  ...  
]  
`

---

##### Create a version

Make a copy of [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/3dcd747f9d8bb6a6687fcb53), and create a new version in it.

**Endpoint**

[POST /api/v10/documents/d/{did}/versions](https://cad.onshape.com/glassworks/explorer/#/Document/createVersion)

**Request Body**

`{
  "documentId": "{did}",
  "name": "newVersion1",
  "workspaceId": "{wid}"
}
`

_Additional optional fields available. See the [API Explorer](https://cad.onshape.com/glassworks/explorer/#/Document/createVersion) for a full list._

**Example**

1. Make a copy of [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/3dcd747f9d8bb6a6687fcb53), and make a note of the _new_ document and workspace IDs in the URL.
2. Call the [createVersion](https://cad.onshape.com/glassworks/explorer/#/Document/createVersion) endpoint on the document ID from Step 1\. You must also specify the document ID and workspace ID in the request body, along with a name for the version:  
   * cURL  
   * python  
`curl -X 'POST' \  
  'https://{baseUrl}.onshape.com/api/v10/documents/d/{did}/versions' \  
  -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
      "documentId": "{did}",  
      "name": "newVersion1",  
      "workspaceId": "{wid}"  
      }'  
`  
`import requests  
import json  
auth = (access_key, secret_key) # See Authentication guide  
headers = {  
  'Accept': 'application/json;charset=UTF-8;qs=0.09',  
  'Content-Type': 'application/json;charset=UTF-8; qs=0.09'  
}  
api_url = "https://{baseUrl}.onshape.com/api/v10/documents/d/{did}/versions"  
queryParams = {}  
body = {  
  "documentId": "{did}",  
  "name": "newVersion1",  
  "workspaceId": "{wid}"  
}  
response = requests.post( api_url,  
                          params=queryParams,  
                          json=body,  
                          auth=auth,  
                          headers=headers)  
print(json.dumps(response.json(), indent=4))  
`
3. Navigate to your document and open the Versions and history graph. Confirm that `newVersion1` appears in the history.  
    
![](https://onshape-public.github.io/docs/api-adv/documents/images/DocumentsGuideNewVersion.png)

---

##### Get document versions

Get a list of all versions in a document. Complete the [Create a version](#create-a-version) example above before beginning this one.

**Endpoint**

[GET /api/v10/documents/d/{did}/versions](https://cad.onshape.com/glassworks/explorer/#/Document/getDocumentVersions)

**Query Parameters**

`{
  "offset": 0,
  "limit": 0
}
`

**Example**

1. Complete the [Create a version](#create-a-version) example above.
2. Call the [getDocumentVersions](https://cad.onshape.com/glassworks/explorer/#/Document/getDocumentVersions) endpoint your document ID:  
   * cURL  
   * python  
`curl -X 'GET' \  
  'https://{baseUrl}.onshape.com/api/v10/documents/d/{did}/versions?offset=0&limit=0' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic {credentials}' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09'  
`  
`import requests  
import json  
auth = (access_key, secret_key) # See Authentication guide  
headers = {  
  'Accept': 'application/json;charset=UTF-8;qs=0.09',  
  'Content-Type': 'application/json;charset=UTF-8; qs=0.09'  
}  
api_url = "https://{baseUrl}.onshape.com/api/v10/documents/d/{did}/versions"  
queryParams = {  
  "offset": 0,  
  "limit": 0  
}  
response = requests.get(api_url,  
                        params=queryParams,  
                        auth=auth,  
                        headers=headers)  
print(json.dumps(response.json(), indent=4))  
`
3. Scroll to the end of the response and confirm that you see the `newVersion1` version you created:  
`"documentId": "{did}",  
"thumbnail": null,  
"microversion": "{mid}",  
"parents": null,  
"name": "newVersion1",  
"id": "{vid}",  
"href": null  
`

---

##### Delete a document

Delete a document. Complete the [Create a document](#create-a-document) example above before beginning this one.

**Endpoint**

[DELETE /api/10/documents/{did}](https://cad.onshape.com/glassworks/explorer/#/Document/deleteDocument)

**Query Parameters**

`{
  "forever": "false"
}
`

**Example**

1. Complete the [Create a document](#create-a-document) example above.
2. Call the [deleteDocument](https://cad.onshape.com/glassworks/explorer/#/Document/deleteDocument) endpoint on the document ID from the Create a document tutorial:  
   * cURL  
   * python  
`curl -X 'DELETE' \  
  'https://{baseUrl}.onshape.com/api/v10/documents/{did}?forever=false' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic {credentials}' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09'  
`  
`import requests  
import json  
auth = (access_key, secret_key) # See Authentication guide  
headers = {  
  'Accept': 'application/json;charset=UTF-8;qs=0.09',  
  'Content-Type': 'application/json;charset=UTF-8; qs=0.09'  
}  
api_url = "https://{baseUrl}.onshape.com/api/v10/documents/{did}"  
queryParams = {  
  "forever" : "false"  
}  
response = requests.delete( api_url,  
                            params=queryParams,  
                            auth=auth,  
                            headers=headers )  
print(response)  
`
3. Your console should return a 200 response. Return to your Onshape account and confirm that the document has been deleted.

#### Additional Resources

* API Explorer: [Documents](https://cad.onshape.com/glassworks/explorer/#/Document)
* API Guide: [API Explorer](https://onshape-public.github.io/docs/api-adv/documents/docs/api-intro/explorer)
* Onshape Help: [Documents](https://cad.onshape.com/help/Content/introduction.htm)

---

<a id="pg-docs-api-adv-drawings"></a>
### Drawings

_Source: <https://onshape-public.github.io/docs/api-adv/drawings/>_

This page describes the APIs Onshape provides for working with Onshape drawings.

| PrerequisitesAll Onshape API calls must be properly authenticated.See the [API Keys](https://onshape-public.github.io/docs/api-adv/drawings/docs/auth/apikeys) page for instructions and the [Quick Start](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-intro/quickstart) for an example.All applications submitted to the Onshape App Store _must_ authenticate with [OAuth2](https://onshape-public.github.io/docs/api-adv/drawings/docs/auth/oauth).For Standard accounts, replace {baseUrl} with cad in all endpoints. For Enterprise accounts, replace it with your company domain. Add /api and the version number, and then provide the endpoint.https://{baseUrl}.onshape.com/api/v10/documentshttps://cad.onshape.com/api/v10/documentshttps://companySubDomain.onshape.com/api/v10/documentsOnshape IDs are written as: {did}, {wvmid}, {eid}, {pid}, {otherId}.These represent document, workspace (or version or microversion), element, part, and other IDs, respectively.See [API Guide: API Intro](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-intro/#onshape-api-request) for information on what these IDs mean and how to obtain them from your documents.Variables are written as: {variableId1} or <variableIdTwo>.These represent variables that must be replaced in the code before it is usable.Never include the braces {} or angle brackets <> with your IDs/variables.This page provides sample code in cURL and python.For additional instruction and video content, visit the Learning Center’s [Intro to the Onshape API](https://learn.onshape.com/learn/course/intro-to-the-onshape-api/intro-to-the-onshape-api/what-is-an-api?page=1) course. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

#### Sample Code

* [Onshape TypeScript Drawing Client](https://github.com/onshape-public/onshape-ts-drawing-client)
* [Onshape Drawing JSON Schemas](https://github.com/onshape-public/onshapedrawingjson)

#### Endpoints

To create drawings, Onshape allows you to send all drawing data points and information through the API as part of the request body JSON.

The following endpoints are available:

* [createDrawingAppElement](https://cad.onshape.com/glassworks/explorer/#/Drawing/createDrawingAppElement): Create a drawing  
```  
curl -X 'POST' \  
  'https://cad.onshape.com/api/v6/drawings/d/{did}/w/{wid}/create' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
    <JSON request body options from the BTDrawingParams schema>  
}'  
```  
Specify the document in which to create the drawing in the URL, and pass any additional options as part of the request body. You can provide a name for the drawing, manipulate the drawing graphics area, specify a part or template to create the drawing from, and more.  
   * See documentation for all available options in the [API Explorer](https://cad.onshape.com/glassworks/explorer/#/Drawing/createDrawingAppElement).  
   * For instructions on viewing the documentation for the request body schemas, see our [API Explorer](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-intro/explorer#view-request-body-docs) page. Check out the [Sample Workflows](#sample-workflows) section below for some practical examples.  
         
   ![BTDrawingParams schema in the createDrawingAppElement endpoint](https://onshape-public.github.io/docs/api-adv/drawings/images/BTDrawingParamsSchema.png)
* [modifyDrawing](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing): Modify a drawing and add annotations  
```  
curl -X 'POST \  
  'https://cad.onshape.doc/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/modify' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
      "description": "Description string.",  
      "jsonRequests": [  
        {  
          <JSON request body options from the jsonRequests schema>  
        }  
      ]  
    }'  
```  
Specify the drawing to modify in the URL, and pass the information on the modification in the request body.  
   * Note that the `jsonRequests` schema is not defined in the Glassworks API Explorer; see the [OnshapeDrawingJson](https://github.com/onshape-public/onshapedrawingjson) repository for this information, and check out the [Sample Workflows](#sample-workflows) section below for some practical examples.  
   * The `description` field is limited to 32 characters.
* [getModificationStatus](https://cad.onshape.com/glassworks/explorer/#/Drawing/getModificationStatus): Get the status of a drawing modification  
```  
curl -X 'GET' \  
  'https://cad.onshape.com/api/v6/drawings/modify/status/{mrid}  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
```  
   * Provide the modification ID (from the `modifyDrawing` response body) to get the status of the modification.  
   * This call also returns the unique IDs of any annotations that were successfully created or edited.  
   * The `requestState` field has three potential values:  
         * `ACTIVE`: drawing modification is in progress  
         * `DONE`: drawing modification finished successfully  
         * `FAILED`: an error occurred and the drawing was not modified  
   * To set up the call:  
         * Replace `{mrid}` with the `id` returned in the modification response, and replace `CREDENTIALS` with your credentials.  
         * Poll the modification status until the request is no longer `ACTIVE`.  
         * ⚠️ **POLL RESPONSIBLY**. See [Rate Limiting](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/errors/#429) and [API Limits](https://onshape-public.github.io/docs/api-adv/drawings/docs/auth/limits) for more information.  
   ```  
   curl -X 'GET \  
     'https://cad.onshape.doc/api/v6/drawings/modify/status/{mrid}' \  
     -H 'Authorization: Basic CREDENTIALS' \  
     -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
     -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
   ```
* [createDrawingTranslation](https://cad.onshape.com/glassworks/explorer/#/Drawing/createDrawingTranslation): Export a drawing to JSON  
```  
curl -X 'POST' \  
  'https://cad.onshape.com/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/translations' \  
  -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
      "formatName": "DRAWING_JSON"  
      }'  
```
* [getDrawingTranslatorFormats](https://cad.onshape.com/glassworks/explorer/#/Drawing/getDrawingTranslatorFormats): View available drawing export formats  
```  
curl -X 'GET' \  
'https://cad.onshape.com/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/translationformats' \  
  -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS'  
```

#### Errors

> ⚠️ **Warning**
> 
> When polling for a drawing modification to complete, use a reasonable interval (e.g., avoid polling multiple times a second, use an exponential backoff strategy, etc.). See [Rate Limiting](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/errors/#429) and [API Limits](https://onshape-public.github.io/docs/api-adv/drawings/docs/auth/limits) for more information.

##### Status codes

If a drawing modification call fails, the [modifyDrawing](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing) response will return an [error](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/errors), as expected. However, if the call includes multiple modifications, it will return `200` if any of the batch modifications succeed. The `status` field for each modification includes the status of the individual operation. For example:

`{
	"status": "OK | Partial_success | Failed",
	"statusCode": "200 |207 | 400 ",
	"errorDescription": "Some Succeeded and Some Failed | Failed",
	"changeId": "f19a07278a009f85f68f4526",
	"results": [
		{
			"status": "OK",
			"logicalId": "h:10000D09"
		},
		{
			"status": "OK",
			"logicalId": "h:10000D0A"
		},
		{
			"status": "Failed",
			"errorDescription": "Error processing Onshape::Note: Point reference is not an object."
		},
		{
			"status": "Failed",
			"logicalId": "h:10000C29",
			"errorDescription": "Error processing : Invalid handle "
		}
	]
}
`

##### Viewing drawing errors

See also: [Sample Code: Find errors in a drawing](https://github.com/onshape-public/onshape-ts-drawing-client/blob/main/find-errors-in-drawing.ts)

You can [export your drawing to JSON](#export-a-drawing-to-json) to find errors with your drawing. Each `view` in the JSON includes an `errorState` for reporting drawing errors. See the [Find dangling entities](#find-dangling-entities) tutorial for an example.

#### Annotation types

```
Onshape::Callout
Onshape::Note
Onshape::GeometricTolerance
Onshape::Centerline::PointToPoint
Onshape::Centerline::LineToLine
Onshape::Centerline::TwoPointCircular
Onshape::Centerline::ThreePointCircular
Onshape::Dimension::LineToLine
Onshape::Dimension::PointToPoint
Onshape::Dimension::PointToLine
Onshape::Dimension::Diametric
Onshape::Dimension::Radial
Onshape::Dimension::LineToLineAngular
Onshape::Dimension::ThreePointAngular
Onshape::InspectionSymbol

```

#### Examples - Create Drawings

##### Create a drawing from a part

In this example, we’ll create a drawing from the **FLYWHEEL** part in [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/v/405ba186c3a70e0227ab2941/e/6bed6b43463f6a46a37b4a22).

1. Open an Onshape document in which to create your drawing.
2. Start to form the [createDrawingAppElement](https://cad.onshape.com/glassworks/explorer/#/Drawing/createDrawingAppElement) call. Replace `{did}` and `{wid}` in the URL below with the document ID and workspace ID of your document (i.e., the _target_ document), and replace `CREDENTIAL` with your authorization credentials.  
```  
curl -X 'POST' \  
  'https://cad.onshape.com/api/v6/drawings/d/{did}/w/{wid}/create' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
```
3. Add the request body information:  
   * Add `flywheelDrawing` as the `drawingName` field.  
   * We must specify the _source_ document’s document and version IDs. Note that since our target document and source document are different, we use the `external` document and version ID fields.  
   * We must also provide the ID of the part to create the drawing from, and the ID of the element (i.e., tab) in which the part lives.  
   (Hint: You can call [getPartsWMVE](https://cad.onshape.com/glassworks/explorer/#/Part/getPartsWMVE) to get a list of part IDs in an element.)  
   ```  
   curl -X 'POST' \  
     'https://cad.onshape.com/api/v6/drawings/d/{did}/w/{wid}/create' \  
     -H 'Authorization: Basic CREDENTIALS' \  
     -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
     -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
     -d '{  
           "drawingName": "flywheelDrawing",  
           "externalDocumentId": "e60c4803eaf2ac8be492c18e",  
           "externalDocumentVersionId": "405ba186c3a70e0227ab2941",  
           "elementId": "6bed6b43463f6a46a37b4a22",  
           "partId": "JiD"  
         }'  
   ```
4. Call the endpoint and open your document. Confirm that you see the new `flywheelDrawing` element containing the drawing:  
![new drawing created from a part in an external document](https://onshape-public.github.io/docs/api-adv/drawings/images/flywheelDrawingExample1.png)

##### Create a drawing from a template

In this example, we’ll create a drawing from the standard ANSI template in [this public document](https://cad.onshape.com/documents/cbe6e776694549b5ba1a3e88/w/24d08acf10234dbc8d3ab585/e/17eef7862b224f6fb12cbc46).

1. Open an Onshape document in which to create your drawing.
2. Start to form the [createDrawingAppElement](https://cad.onshape.com/glassworks/explorer/#/Drawing/createDrawingAppElement) call. Replace `{did}` and `{wid}` in the URL below with the document ID and workspace ID of your document (i.e., the _target_ document), and replace `CREDENTIAL` with your authorization credentials.  
```  
curl -X 'POST' \  
  'https://cad.onshape.com/api/v6/drawings/d/{did}/w/{wid}/create' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
```
3. Add the request body information:  
   * Add `templateAnsiDrawing` as the `drawingName` field.  
   * We must specify the _source_ document’s document ID and workspace ID.  
   * We must also provide the ID of the element (i.e., tab) in which the template lives.  
   * Note that we use the `template` document, workspace, and element ID fields when referring to a specific template for drawing creation.  
   ```  
   curl 'https://cad.onshape.com/api/drawings/d/{did}/w/{wid}/create' \  
     -H 'Authorization: Basic CREDENTIALS' \  
     -H 'Accept: application/json, text/plain, */*' \  
     -H 'Content-Type: application/json;charset=UTF-8' \  
     -d '{  
       "drawingName": "templateAnsiDrawing",  
       "templateDocumentId":"cbe6e776694549b5ba1a3e88",  
       "templateWorkspaceId":"24d08acf10234dbc8d3ab585",  
       "templateElementId":"17eef7862b224f6fb12cbc46"  
       }'  
   ```
4. Call the endpoint and open your document. Confirm that you see the new `templateAnsiDrawing` element containing the empty drawing template.

##### Create a drawing in a custom graphics area

1. Open an Onshape document in which to create your drawing.
2. Start to form the [createDrawingAppElement](https://cad.onshape.com/glassworks/explorer/#/Drawing/createDrawingAppElement) call. Replace `{did}` and `{wid}` in the URL below with your document, and replace `CREDENTIAL` with your authorization credentials.  
```  
curl -X 'POST' \  
  'https://cad.onshape.com/api/v6/drawings/d/{did}/w/{wid}/create' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
```
3. Add information about the drawings area. In this example, we’ll add an additional column and row to the drawings area, a title block, and add a border around it.  
```  
curl -X 'POST' \  
  'https://cad.onshape.com/api/v6/drawings/d/{did}/w/{wid}/create' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
        "drawingName": "customGraphicsArea",  
        "border": "true",  
        "numberHorizontalZones": "3",  
        "numberVerticalZones": "3",  
        "titleblock": true  
      }'  
```
4. Call the endpoint and open your document. Confirm that you see the new `customGraphicsArea` element:  
![new drawing created with border and extra column and row](https://onshape-public.github.io/docs/api-adv/drawings/images/customDrawingArea.png)

#### Examples - Add Annotations

See [Annotation types](#annotation-types).

##### Add a note to a drawing

1. Open an Onshape drawing. This example uses the drawing created in the [Create a drawing from a part](#create-a-drawing-from-a-part) tutorial.
2. Start to form the [modifyDrawing](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing) call. Replace the URL parameters with the values from your document, and replace `CREDENTIALS` with your authorization credentials.  
```  
curl -X 'POST \  
  'https://cad.onshape.doc/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/modify' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
```
3. Add information about the modification. In this example, we’ll create an `Onshape::Note` on the drawing. We must specify the `messageName` and `formatVersion` for the modification, and then provide the contents and size of the annotation.  
```  
curl -X 'POST \  
  'https://cad.onshape.doc/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/modify' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
        "description": "Add a note.",  
        "jsonRequests": [ {  
          "messageName": "onshapeCreateAnnotations",  
          "formatVersion": "2021-01-01",  
          "annotations": [  
            {  
              "type": "Onshape::Note",  
              "note": {  
                "position": {  
                  "type": "Onshape::Reference::Point",  
                  "coordinate": [  
                    1,  
                    10,  
                    0  
                  ]  
                },  
                "contents": "This is a note",  
                "textHeight": 0.2  
              }  
            }  
          ]  
        }]  
      }'  
```
4. Make the call, and then get `id` from the response body. You’ll need this to poll the modification status to figure out when the modification has completed.
5. Poll the [modification status](#requestState) and wait for the modification to finish.
6. Open your drawing and confirm that you see the new note. Note that your drawing may not match this image exactly, depending on your drawing and document properties. This sample document uses Inches for units.  
![drawing with note annotation](https://onshape-public.github.io/docs/api-adv/drawings/images/drawings-addnote.png)

##### Add a callout to a drawing

1. Open an Onshape drawing. This example uses the drawing created in the [Create a drawing from a part](#create-a-drawing-from-a-part) tutorial.
2. Start to form the [modifyDrawing](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing) call. Replace the URL parameters with the values from your document, and replace `CREDENTIALS` with your authorization credentials.  
```  
curl -X 'POST \  
  'https://cad.onshape.doc/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/modify' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
```
3. Add information about the modification. In this example, we’ll add an `Onshape::Callout` to the drawing. We must specify the `messageName` and `formatVersion` for the modification, and then provide the contents and size of the annotation:  
```  
curl -X 'POST \  
  'https://cad.onshape.doc/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/modify' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
        "description": "Add a callout.",  
        "jsonRequests": [ {  
          "messageName": "onshapeCreateAnnotations",  
          "formatVersion": "2021-01-01",  
          "annotations": [  
            {  
              "callout":  
              {  
                "borderShape": "Circle",  
                "borderSize": 0,  
                "contents": "Example Callout",  
                "contentsBottom": "bottom",  
                "contentsLeft": "left",  
                "contentsRight": "right",  
                "contentsTop": "top",  
                "position": {  
                  "coordinate": [  
                    2.5,  
                    6,  
                    0  
                  ],  
                  "type": "Onshape::Reference::Point"  
                },  
                "textHeight": 0.12  
              },  
              "type": "Onshape::Callout"  
            }  
          ]  
        }]  
      }'  
```
4. Make the call, and then get `id` from the response body. You’ll need this to poll the modification status to figure out when the modification has completed.
5. Poll the [modification status](#requestState) and wait for the modification to finish.
6. Open your drawing and confirm that you see the new callout.  
![callout added to drawing](https://onshape-public.github.io/docs/api-adv/drawings/images/drawings-addcallout.png)

##### Add a centerline to a drawing

1. Open an Onshape drawing. This example uses the drawing created in the [Create a drawing from a part](#create-a-drawing-from-a-part) tutorial.
2. Start to form the [modifyDrawing](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing) call. Replace the URL parameters with the values from your document, and replace `CREDENTIALS` with your authorization credentials.  
```  
curl -X 'POST \  
  'https://cad.onshape.doc/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/modify' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
```
3. Add information about the modification. In this example, we’ll add an `Onshape::Centerline` to the drawing. We must specify the `messageName` and `formatVersion` for the modification, and then provide the coordinates of the centerline ends.
* Note: you can [Export a Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation/#export-a-drawing-as-a-json) to get the coordinates, `uniqueId` and `viewId` values shown in the request below.
* Note: if you have access, you can refer to the [ODA documentation](https://docs.opendesign.com/td/) for more detailed formatting information.  
```  
curl -X 'POST \  
  'https://cad.onshape.doc/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/modify' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
        "description": "Add a centerline",  
        "jsonRequests": [ {  
          "messageName": "onshapeCreateAnnotations",  
          "formatVersion": "2021-01-01",  
          "annotations": [  
            {  
              "pointToPointCenterline": {  
                  "point1": {  
                    "coordinate": [  
                      2,  
                      4,  
                      0  
                    ],  
                    "type": "Onshape::Reference::Point",  
                    "uniqueId": "point1",  
                    "viewId": "51fa8b6040e411dfd17a4cda",  
                    "snapPointType": "ModeStart"  
                  },  
                  "point2": {  
                    "coordinate": [  
                      7,  
                      6,  
                      1  
                    ],  
                    "type": "Onshape::Reference::Point",  
                    "uniqueId": "point2",  
                    "viewId": "51fa8b6040e411dfd17a4cda",  
                    "snapPointType": "ModeEnd"  
                  }  
              },  
              "type": "Onshape::Centerline::PointToPoint"  
            }  
          ]  
        }]  
      }'  
```
1. Make the call, and then get `id` from the response body. You’ll need this to poll the modification status to figure out when the modification has completed.
2. Poll the [modification status](#requestState) and wait for the modification to finish.
3. Open your drawing and confirm that you see the new centerline.

##### Add a geometric tolerance to a drawing

1. Open an Onshape drawing. This example uses the drawing created in the [Create a drawing from a part](#create-a-drawing-from-a-part) tutorial.
2. Start to form the [modifyDrawing](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing) call. Replace the URL parameters with the values from your document, and replace `CREDENTIALS` with your authorization credentials.  
```  
curl -X 'POST \  
  'https://cad.onshape.doc/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/modify' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
```
3. Add information about the modification. In this example, we’ll add an `Onshape::GeometricTolerance` to the drawing. We must specify the `messageName` and `formatVersion` for the modification, and then provide the frames and position of the annotation:  
```  
curl -X 'POST \  
  'https://cad.onshape.doc/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/modify' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
        "description": "Add a geometric tolerance",  
        "jsonRequests": [ {  
          "messageName": "onshapeCreateAnnotations",  
          "formatVersion": "2021-01-01",  
          "annotations": [  
            {  
              "geometricTolerance": {  
                "frames": [  
                  "{\\fDrawing Symbols Sans;◎}%%v{\\fDrawing Symbols Sans;∅}tol1{\\fDrawing Symbols Sans;Ⓜ}%%v%%v%%v%%v%%v\n",  
                  "{\\fDrawing Symbols Sans;⌖}%%vto2{\\fDrawing Symbols Sans;Ⓛ}%%v%%v%%v%%v%%v\n"  
                ],  
                "position": {  
                  "coordinate": [  
                    6,  
                    6,  
                    0  
                  ],  
                  "type": "Onshape::Reference::Point"  
                }  
              },  
              "type": "Onshape::GeometricTolerance"  
            }  
          ]  
        }]  
      }'  
```
4. Make the call, and then get `id` from the response body. You’ll need this to poll the modification status to figure out when the modification has completed.
5. Poll the [modification status](#requestState) and wait for the modification to finish.
6. Open your drawing and confirm that you see the new annotation.  
![new drawing created with border and extra column and row](https://onshape-public.github.io/docs/api-adv/drawings/images/drawings-addtolerance.png)

##### Add an inspection symbol to a drawing

1. Open an Onshape drawing. This example uses the drawing created in the [Create a drawing from a part](#create-a-drawing-from-a-part) tutorial.
2. Start to form the [modifyDrawing](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing) call. Replace the URL parameters with the values from your document, and replace `CREDENTIALS` with your authorization credentials.  
```  
curl -X 'POST \  
  'https://cad.onshape.doc/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/modify' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
```
3. Add information about the modification. In this example, we’ll add an `Onshape::InspectionSymbol` to the drawing. We must specify the `messageName` and `formatVersion` for the modification, and then provide the shape and position of the inspection symbol. (Hint: you can [Export a Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation/#export-a-drawing-to-json) to get a list of valid coordinates and handles.)  
```  
curl -X 'POST \  
  'https://cad.onshape.doc/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/modify' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
        "description": "Add an inspection symbol",  
        "jsonRequests": [ {  
          "messageName": "onshapeCreateAnnotations",  
          "formatVersion": "2021-01-01",  
          "annotations": [  
            {  
              "inspectionSymbol": {  
                "borderShape": "Circle",  
                "borderSize": 2,  
                "parentAnnotation": "h:10000577",  
                "parentLineIndex": 0.0,  
                "position": {  
                  "coordinate": [  
                    2.6,  
                    6,  
                    0  
                  ],  
                  "type": "Onshape::Reference::Point"  
                },  
                "textHeight": 2  
              },  
              "type": "Onshape::InspectionSymbol"  
            }  
          ]  
        }]  
      }'  
```
4. Make the call, and then get `id` from the response body. You’ll need this to poll the modification status to figure out when the modification has completed.
5. Poll the [modification status](#requestState) and wait for the modification to finish.
6. Open your drawing and confirm that you see the new inspection symbol.

##### Add a table to a drawing

1. Open an Onshape drawing. This example uses the drawing created in the [Create a drawing from a part](#create-a-drawing-from-a-part) tutorial.
2. Start to form the [Drawings/modifyDrawing](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing) call. Replace the URL parameters with the values from your document, and replace `CREDENTIALS` with your authorization credentials.  
```  
curl -X 'POST \  
  'https://cad.onshape.doc/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/modify' \  
  -H 'Authorization: Basic CREDENTIALS' \s  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
```
3. Add information about the modification. In this example, we’ll add an `Onshape::Table::GeneralTable` to the drawing. We must specify the `messageName` and `formatVersion` for the modification, and then provide the location, number of rows, and number of columns for the table. (Hint: you can [Export a Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation/#export-a-drawing-to-json) to get a list of valid coordinates.)  
```  
curl -X 'POST \  
  'https://cad.onshape.doc/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/modify' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
        "description": "New table",  
        "jsonRequests": [ {  
          "formatVersion": "2021-01-01",  
          "messageName": "onshapeCreateAnnotations",  
          "annotations": [  
            { "table": {  
                "cells": [  
                  {  
                    "column": 0,  
                    "content": "1.1",  
                    "row": 0  
                  },  
                  {  
                    "column": 0,  
                    "content": "2.1",  
                    "row": 1  
                  },  
                  {  
                    "column": 1,  
                    "content": "1.2",  
                    "row": 0  
                  },  
                  {  
                    "column": 1,  
                    "content": "2.2",  
                    "row": 1  
                  }  
                ],  
                "columns": 2,  
                "rows": 2,  
                "showHeaderRow": false,  
                "showTitleRow": false,  
                "position": {  
                  "coordinate": [100.0, 400.0, 0.0],  
                  "type": "Onshape::Reference::Point"  
                }  
              },  
              "type": "Onshape::Table::GeneralTable"  
            }]  
        }]  
      }'  
```
4. Make the call, and then get `id` from the response body. You’ll need this to poll the modification status to figure out when the modification has completed.
5. Poll the [modification status](#requestState) and wait for the modification to finish.
6. Open your drawing and confirm that you see the new table.

##### Add a datum to a drawing

1. Open an Onshape drawing. This example uses the drawing created in the [Create a drawing from a part](#create-a-drawing-from-a-part) tutorial.
2. Start to form the [Drawings/modifyDrawing](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing) call. Replace the URL parameters with the values from your document, and replace `CREDENTIALS` with your authorization credentials.  
```  
curl -X 'POST \  
  'https://cad.onshape.doc/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/modify' \  
  -H 'Authorization: Basic CREDENTIALS' \s  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
```
3. Add information about the modification. In this example, we’ll add a `datum` block to the drawing. We must specify the `messageName` and `formatVersion` for the modification, and then provide the info for the datum. (Hint: you can [Export a Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation/#export-a-drawing-to-json) to get a list of valid coordinates for your datum’s position.)  
```  
curl -X 'POST \  
  'https://cad.onshape.doc/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/modify' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
        "description": "New datum",  
        "jsonRequests": [ {  
          "formatVersion": "2021-01-01",  
          "messageName": "onshapeCreateAnnotations",  
          "annotations": [  
            {  
              "datum":{  
                "arrowType": "DatumFilled", // DatumFilled | DatumBlank  
                "contents": "A", // Replace with datum text  
                "datumSize": 0.25, // Datum size  
                "isDangling": false,  
                "isDatumTarget": false,  
                "logicalId":"h:100001DC",  // Datum ID  
                "position": {  // Datum location  
                  "coordinate":[  
                    6.91,  
                    3.24,  
                    -1  
                    ],  
                  "type": "Onshape::Reference::Point"  
                  },  
                  "targetPosition": { // Datum arrow location  
                    "coordinate": [  
                      0.2,  
                      0.2,  
                      -0.1  
                      ],  
                    "snapPointType":"ModeNear",  
                    "type":"Onshape::Reference::Point",  
                    "uniqueId":"F4241", // Unique ID  
                    "viewId":"{viewId}" // View ID of the drawing  
                  },  
                  "textSize": 0.25 // Datum text size  
                  },  
                  "type":"Onshape::Datum"  
            }]  
        }]  
      }'  
```
4. Make the call, and then get `id` from the response body. You’ll need this to poll the modification status to figure out when the modification has completed.
5. Poll the [modification status](#requestState) and wait for the modification to finish.
6. Open your drawing and confirm that you see the new datum.

##### Add a surface finish symbol to a drawing

This code adds a surface finish symbol (SFS) to a drawing in empty space.

* To create an SFS attached to an annotation, see: [Add an SFS to an annotation](#add-a-surface-finish-symbol-to-an-annotation)
* To attach an SFS to a view edge, see: [Associate an annotation with a view edge](#associate-an-annotation-with-a-view-edge-without-a-leader).

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Add an SFS",
  "jsonRequests": [ {
    "messageName": "onshapeCreateAnnotations",
    "formatVersion": "2021-01-01",
    "annotations": [
      { 
        "surfaceFinishSymbol": { 
          "isAllAround": false, 
          "matRemovalAllowance": "", 
          "maxRoughness": "", 
          "maxRoughnessWidth": "", 
          "methodWaviness": "", 
          "minRoughness": "", 
          "position": { 
            "coordinate": [ 
              5.2, 
              5.7, 
              0 
            ], 
            "type": "Onshape::Reference::Point" 
          }, 
          "roughnessCutoff": "", 
          "surfaceDirectionLayType": "NotSpecified", 
          "surfaceTextType": "Basic", 
          "textHeight": 0.12 
          }, 
        "type": "Onshape::SurfaceFinishSymbol" 
      }
    ]
  }]
}
`

##### Add a surface finish symbol to an annotation

You can create a surface finish symbol (SFS) that’s attached to another annotation by supplying that annotation’s logical ID in the `position.logicalId` field. In this example, we create the SFS attached to a GDT.

To attach an SFS to a view edge, follow the instructions here: [Associate an annotation with a view edge](#associate-an-annotation-with-a-view-edge-without-a-leader).

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Add an SFS to a GDT",
  "jsonRequests": [ {
    "messageName": "onshapeCreateAnnotations",
    "formatVersion": "2021-01-01",
    "annotations": [
      { 
        "surfaceFinishSymbol": {
          "isAllAround": false,
          "isDangling": false,
          "matRemovalAllowance": "",
          "maxRoughness": "",
          "maxRoughnessWidth": "",
          "methodWaviness": "",
          "minRoughness": "",
          "position": {
            "coordinate": [
              7.8,
              3.5,
              0.0
            ],
            "logicalId": "{logicalId}",
            "type": "Onshape::Reference::Point"
          },
          "roughnessCutoff": "",
          "surfaceDirectionLayType": "PerpendicularToPlaneOfProjection",
          "surfaceTextType": "RemovalOfMaterialRequired",
          "textHeight": 0.0
        },
        "type": "Onshape::SurfaceFinishSymbol"
      }
    ]
  } ]
}
`

##### Add a centermark to a circular edge

You can [Export a Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation/#export-a-drawing-to-json) to get a list of valid coordinates and IDs for your drawing.

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Add a centermark to a circular edge",
  "jsonRequests": [ {  
    "messageName": "onshapeCreateAnnotations",  
    "formatVersion": "2021-01-01",  
    "annotations": [  
      {  
        "centermark": {  
          "bottomGripPoint": {  
            "coordinate": [  
              3.1822537578892087,  
              3.6563745010106074,  
              0.25000000000000008  
            ],  
            "type": "Onshape::Reference::Point"  
          },  
          "centerPoint": {  
            "coordinate": [  
              0.025104875729290184,  
              -2.7755575615628916e-17,  
              0.025400000000000007  
            ],  
            "snapPointType": "ModeCenter",  
            "type": "Onshape::Reference::Point",  
            "uniqueId": "{uniqueIdOfCenterPoint}",  
            "viewId": "{drawingViewId}"  
          },  
          "leftGripPoint": {  
            "coordinate": [  
              2.993828561038815,  
              3.8447996978610008,  
              0.25000000000000008  
            ],  
            "type": "Onshape::Reference::Point"  
          },
          "rightGripPoint": {  
            "coordinate": [  
              3.370678954739602,  
              3.8447996978610008,  
              0.25000000000000008  
            ],  
            "type": "Onshape::Reference::Point"  
            },  
          "topGripPoint": {  
            "coordinate": [  
              3.1822537578892087,  
              4.033224894711394,  
              0.25000000000000008  
            ],  
            "type": "Onshape::Reference::Point"  
          }  
        },  
        "type": "Onshape::Centermark"  
      }  
    ]  
  } ]
}
`

##### Add a centermark aligned with a view edge

You can [Export a Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation/#export-a-drawing-to-json) to get a list of valid coordinates and IDs for your drawing.

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Add a centermark aligned with a view edge",
  "jsonRequests": [ {  
    "messageName": "onshapeCreateAnnotations",  
    "formatVersion": "2021-01-01",  
    "annotations": [  
      {  
        "centermark": {  
          "alignEdge": {  
            "deterministicId": "{edgeDeterministicId}",  
            "type": "Onshape::Reference::Edge",
            "uniqueId": "{edgeUniqueId}",  
            "viewId": "{drawingViewId}"  
          },  
          "bottomGripPoint": {  
            "coordinate": [  
              2.8352194500430278,  
              3.245579835836262,  
              0.25000000000000008  
            ],  
            "type": "Onshape::Reference::Point"  
          },  
          "centerPoint": {  
            "coordinate": [  
              0,  
              -0.02296483610015257,  
              0.025400000000000007  
            ],  
            "snapPointType": "ModeCenter",  
            "type": "Onshape::Reference::Point",  
            "uniqueId": "{centerPointUniqueId}",  
            "viewId": "{drawingViewId}"  
          },  
          "leftGripPoint": {  
            "coordinate": [  
              2.5409071315113667,  
              3.2455798358362619,  
              0.25000000000000008  
            ],  
            "type": "Onshape::Reference::Point"  
          },  
          "rightGripPoint": {  
            "coordinate": [  
              2.8352194500430278,  
              3.539892154367923,  
              0.25000000000000008
            ],  
            "type": "Onshape::Reference::Point"  
          },  
          "topGripPoint": {  
            "coordinate": [  
              2.5409071315113667,  
              3.5398921543679227,  
              0.25000000000000008  
            ],  
            "type": "Onshape::Reference::Point"  
          }  
        },  
      "type": "Onshape::Centermark"  
      }  
    ]  
  } ]
}
`

##### Add a centermark with an extension line

You can set the length of extension lines by passing individual grip points or by passing  
`extensionLineLength`. [Export a Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation/#export-a-drawing-to-json) to get a list of valid coordinates and IDs for your drawing.

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Add a centermark with an extension line",
  "jsonRequests": [
    {  
      "messageName": "onshapeCreateAnnotations",  
      "formatVersion": "2021-01-01",  
      "annotations": [  
        {  
          "centermark": {  
            "centerPoint": {  
              "coordinate": [  
                0,  
                -0.02296483610015257,  
                0.025400000000000007  
              ],  
              "snapPointType": "ModeCenter",  
              "type": "Onshape::Reference::Point",  
              "uniqueId": "{centerPointUniqueId}",
              "viewId": "{drawingViewId}"  
            },  
            "extensionLineLength": 2  
          },  
          "type": "Onshape::Centermark"  
        }  
      ]  
    }  
  ]
}
`

#### Examples - Edit Annotations

See [Annotation types](#annotation-types).

##### Edit an annotation

You can edit an annotation using the [Drawings/modifyDrawing](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing) API in the same way that you create an annotation. You’ll use the `onshapeEditAnnotations` message in place of `onshapeCreateAnnotations`, and you’ll need to supply the `logicalId` for the annotation. You must use the same `type` that you used to create the annotation.

> **Note**You can create a `logicalId` alias when you create an annotation, and refer to that alias in other drawing modifications. Currently, these aliases are not returned in a drawing export. For example, if you send `"logicalId:" "myDrawingNote"` as part of the request when creating a note annotation, you can later use `myDrawingNote` as the `logicalId` when editing the annotation.

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Update a note on a drawing.",
  "jsonRequests": [ {
    "messageName": "onshapeEditAnnotations",
    "formatVersion": "2021-01-01",
    "annotations": [
      {
        "type": "{see Type list below}",
        "note": {
          "contents": "This is new note text.",
          "logicalId": "{logicalId}"
        }
      }
    ]  
  }]
}
`

**Example**

1. Open an Onshape drawing. This example uses the drawing created in the [Create a drawing from a part](#create-a-drawing-from-a-part) tutorial.
2. Follow the steps for [exporting a Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation#export-a-drawing-to-json). In the JSON response, find the `logicalId` for the note you want to modify.
3. Add your headers and the JSON body, including the required fields mentioned above, and the new text in the `contents` field.  
```  
curl -X 'POST \  
  'https://cad.onshape.doc/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/modify' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
        "description": "Update a note on a drawing.",  
        "jsonRequests": [ {  
          "messageName": "onshapeEditAnnotations",  
          "formatVersion": "2021-01-01",  
          "annotations": [  
            {  
              "type": "Onshape::Note",  
              "note": {  
                "contents": "This is new note text.",  
                "logicalId": "{logicalId}"  
              }  
            }  
          ]  
        }]  
      }'  
```
4. Once the modification is done, open your drawing and confirm that you see the new text.

##### Attach an annotation to a parent

To attach an annotation to a parent, you can send the `parentAnnotation` field in your request body. _The new annotation’s `position` must still be provided._ The `position` determines where the annotation is placed, while the `parentAnnotation` determines when the annotation moves; an annotation that isn’t attached to a parent can be moved freely. An annotation attached to a parent moves when the parent annotation moves.

This example request body creates a geometric tolerance annotation attached to a parent annotation with logical ID `h:100000B1`.

> **Note**Surface finish symbols behave differently. See [Add a SFS to an annotation](#add-a-surface-finish-symbol-to-an-annotation) for steps.

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Create a GDT attached to a parent",
  "jsonRequests": [ {
    "messageName": "onshapeCreateAnnotations",
    "formatVersion": "2021-01-01",
    "annotations": [
      {
        "geometricTolerance": {
          "frames": [
            "{\\fDrawing Symbols Sans;◎}%%v{\\fDrawing Symbols Sans;∅}tol1{\\fDrawing Symbols Sans;Ⓜ}%%v%%v%%v%%v%%v\n",
            "{\\fDrawing Symbols Sans;⌖}%%vto2{\\fDrawing Symbols Sans;Ⓛ}%%v%%v%%v%%v%%v\n"
          ],
          "parentAnnotation": "h:100000B1",
          "position": {
            "coordinate": [
              6,
              6,
              0
            ],
            "type": "Onshape::Reference::Point"
          }
        },
        "type": "Onshape::GeometricTolerance"
      }
    ]  
  }]
}
`

##### Associate a leader with a view edge

Add the `leaderPosition` object to your request body to create a leader associated with a view edge.

`{
  "leaderPosition": {
    "coordinate": [
      0.1,
      5.6,
      0.1
    ],
    "deterministicId": "{deterministicId}",
    "snapPointType": "ModeMid",
    "type": "Onshape::Reference::Point",
    "uniqueId": "{uniqueId}",
    "viewId": "{viewId}"
  }
}
`

![annotation leader associated with a view edge](https://onshape-public.github.io/docs/api-adv/drawings/images/drawingsLeader.png)

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Add a geometric tolerance",
  "jsonRequests": [ {
    "messageName": "onshapeCreateAnnotations",
    "formatVersion": "2021-01-01",
    "annotations": [
      {
        "geometricTolerance": {
          "frames": [
            "{\\fDrawing Symbols Sans;◎}%%v{\\fDrawing Symbols Sans;∅}tol1{\\fDrawing Symbols Sans;:m:}%%v%%v%%v%%v%%v\n",
            "{\\fDrawing Symbols Sans;⌖}%%vto2{\\fDrawing Symbols Sans;Ⓛ}%%v%%v%%v%%v%%v\n"
          ],
          "position": {
            "coordinate": [
              6,
              6,
              0
            ],
            "type": "Onshape::Reference::Point"
          },
          "leaderPosition": {
            "coordinate": [
              0.1,
              5.6,
              0.1
            ],
            "deterministicId": "{deterministicId}",
            "snapPointType": "ModeMid",
            "type": "Onshape::Reference::Point",
            "uniqueId": "{uniqueId}",
            "viewId": "{viewId}"
          }
        },
        "type": "Onshape::GeometricTolerance"
      }
    ]
  }]
}
`

**Workflow**

1. Call [getDrawingViews](https://cad.onshape.com/glassworks/explorer/#/Drawing/getDrawingViews%5F1) on your drawing to get the `viewId` of the view to add the annotation to.
2. Call [getDrawingViewJsonGeometry](https://cad.onshape.com/glassworks/explorer/#/Drawing/getDrawingViewJsonGeometry%5F1) to get the `uniqueId` and `deterministicId` of the edge to add the annotation to.
3. Call [modifyDrawing](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing) with the request body shown above to create the annotation.

##### Associate an annotation with a view edge without a leader

Add the following information to the annotation’s `position` object to associate the annotation with a view edge:

`{
  "deterministicId": "{deterministicId}",
  "snapPointType": "ModeNear",
  "type": "Onshape::Reference::Point",
  "uniqueId": "{uniqueId}",
  "viewId": "{viewId}"
}
`

![annotation associated with a view edge without a leader](https://onshape-public.github.io/docs/api-adv/drawings/images/drawingsNoLeader.png)

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Add a geometric tolerance",
  "jsonRequests": [ {
    "messageName": "onshapeCreateAnnotations",
    "formatVersion": "2021-01-01",
    "annotations": [
      {
        "geometricTolerance": {
          "frames": [
            "{\\fDrawing Symbols Sans;◎}%%v{\\fDrawing Symbols Sans;∅}tol1{\\fDrawing Symbols Sans;:m:}%%v%%v%%v%%v%%v\n",
            "{\\fDrawing Symbols Sans;⌖}%%vto2{\\fDrawing Symbols Sans;Ⓛ}%%v%%v%%v%%v%%v\n"
          ],
          "position": {
            "coordinate": [
              0.05703643988890697,
              -0.04311684802152582,
              0.025400000000000004
            ],
            "deterministicId": "{deterministicId}",
            "snapPointType": "ModeNear",
            "type": "Onshape::Reference::Point",
            "uniqueId": "{uniqueId}",
            "viewId": "{viewId}"
          }
        },
        "type": "Onshape::GeometricTolerance"
      }
    ]
  }]
}
`

**Workflow**

1. Call [getDrawingViews](https://cad.onshape.com/glassworks/explorer/#/Drawing/getDrawingViews%5F1) on your drawing to get the `viewId` of the view to add the annotation to.
2. Call [getDrawingViewJsonGeometry](https://cad.onshape.com/glassworks/explorer/#/Drawing/getDrawingViewJsonGeometry%5F1) to get the `uniqueId` and `deterministicId` of the edge to add the annotation to.
3. Call [modifyDrawing](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing) with the request body shown above to create the annotation.

##### Specify a snap point

You can use the [modifyDrawing](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing) to choose the snap points for annotations. Available types of snap points are:

` ModeApint       // Apparent intersection
 ModeCenter      // Center point
 ModeEnd         // End point
 ModeIns         // Insertion point
 ModeIntersec    // Intersection
 ModeMid         // Midpoint
 ModeNear        // Nearest point
 ModeNode        // Node
 ModePar         // Parallel
 ModePerp        // Perpendicular
 ModeQuad        // Quadrant
 ModeStart       // Start point
 ModeTan         // Tangent point
`

1. Create a sketch in Onshape with two circles, then extrude both circles.
2. Create a drawing of the part’s front view. We’ll use the Drawings API to a point to point centerline snapped to the centers of the holes.  
![drawing front view of a box with two holes](https://onshape-public.github.io/docs/api-adv/drawings/images/drawings-snap-before-01.png)
3. Next, we’ll need to get the view ID of the drawing. Call the [Drawing/getDrawingViews\_1](https://cad.onshape.com/glassworks/explorer/#/Drawing/getDrawingViews%5F1) endpoint on your document to get a list of all views in the drawing, and copy the `viewId` from the response:

```
curl -X 'GET' \
  'https://cad.onshape.com/api/v8/drawings/d/{did}/w/{wid}/e/{eid}/views' \
  -H 'Authorization: Basic CREDENTIALS' \s
  -H 'accept: application/json;charset=UTF-8; qs=0.09' \
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' 

```

1. Use the `viewId` from the last step to get the `uniqueId` (or `edgeId`) of each circle’s center from the [Drawing/getDrawingViewJsonGeometry\_1)](https://cad.onshape.com/glassworks/explorer/#/Drawing/getDrawingViewJsonGeometry%5F1) endpoint:

```
curl -X 'GET' \
  'https://cad.onshape.com/api/v8/drawings/d/{did}/w/{wid}/e/{eid}/views/{viewId}/jsongeometry' \
  -H 'Authorization: Basic CREDENTIALS' \s
  -H 'accept: application/json;charset=UTF-8; qs=0.09' \

```

1. Start to form the [modifyDrawing](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing) call. Replace the URL parameters with the values from your document, and replace `CREDENTIALS` with your authorization credentials.  
```  
curl -X 'POST \  
  'https://cad.onshape.doc/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/modify' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d { }  
```
2. Add information about the modification. In this example, we’ll add a `pointToPointCenterline` to the drawing. Make sure to update the request body values as follows:
* `messageName`: `"onshapeCreateAnnotation"`
* `formatVersion`: `"2021-01-01"`
* `uniqueId`: From Step 4
* `viewId`: From Step 3
* `coordinates`: The values must be sent as part of the request, but are ignored.  
```  
    curl -X 'POST \  
  'https://cad.onshape.doc/api/v8/drawings/d/{did}/w/{wid}/e/{eid}/modify' \  
  -H 'Authorization: Basic CREDENTIALS' \s  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d {  
      "description": "creating a snap point",  
      "jsonRequests": [ {  
                "messageName": "onshapeCreateAnnotations",  
                "formatVersion": "2021-01-01",  
                "annotations": [  
                  {  
                    "pointToPointCenterline": {  
                        "point1": {  
                          "coordinate": [0,0,0],  
                          "type": "Onshape::Reference::Point",  
                          "uniqueId": "{uniqueId1}",  
                          "viewId": "{viewId}",  
                          "snapPointType": "ModeCenter"  
                        },  
                        "point2": {  
                          "coordinate": [0,0,0],  
                          "type": "Onshape::Reference::Point",  
                          "uniqueId": "{uniqueId2}",  
                          "viewId": "{viewId}",  
                          "snapPointType": "ModeCenter"  
                        }  
                    },  
                    "type": "Onshape::Centerline::PointToPoint"  
                  }  
                ]  
              }]  
      }  
```
1. Return to your document and see that the centerline has been added to the document at the snap points.  
![drawing front view of a box with two holes with a centerline between the hole centers](https://onshape-public.github.io/docs/api-adv/drawings/images/drawings-snap-after-01.png)

##### Reassociate a centermark with a new edge

You can change the associated edge of a centermark. [Export a Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation/#export-a-drawing-to-json) to get a list of valid coordinates and IDs for your drawing.

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Reassociate a centermark with a new edge",
  "jsonRequests": [
    {  
      "messageName": "onshapeEditAnnotations",  
      "formatVersion": "2021-01-01",  
      "annotations": [  
        {  
          "centermark": {  
            "centerPoint": {
              "coordinate": [  
                0.025104875729290184,  
                -2.7755575615628916e-17,  
                0.025400000000000007  
              ],  
              "snapPointType": "ModeCenter",  
              "type": "Onshape::Reference::Point",  
              "uniqueId": "{newEdgeUniqueId}",  
              "viewId": "{drawingViewId}"  
            },  
            "logicalId": "{centermarkLogicalId}"  
          },
          "type": "Onshape::Centermark"  
        }]  
    }]
}
`

#### Examples - Sketches

##### Sketch a circle

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Sketch a circle",
  "jsonRequests": [ {
    "messageName": "onshapeCreateAnnotations",
    "formatVersion": "2021-01-01",
    "annotations": [
      {
        "circle": {
          "center": {
            "coordinate": [
              6.9,
              6.1,
              0
            ],
            "type": "Onshape::Reference::Point"
          },
          "radius": 1.0
        },
        "type": "Onshape::Circle"
      }]
  }]
}
`

##### Sketch a three-point circle

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Sketch a three-point circle",
  "jsonRequests": [ {
    "messageName": "onshapeCreateAnnotations",
    "formatVersion": "2021-01-01",
    "annotations": [
      {
        "circle": {
          "point1": {
            "coordinate": [
              8.5,
              6.2,
              0
            ],
            "type": "Onshape::Reference::Point"
          },
          "point2": {
            "coordinate": [
              9.2,
              6.2,
              0
            ],
            "type": "Onshape::Reference::Point"
          },
          "point3": {
            "coordinate": [
              8.9,
              5.6,
              0
            ],
            "type": "Onshape::Reference::Point"
          }
        },
        "type": "Onshape::Circle"
      }]
  }]
}
`

##### Sketch a line

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Sketch a line",
  "jsonRequests": [ {
    "messageName": "onshapeCreateAnnotations",
    "formatVersion": "2021-01-01",
    "annotations": [
      {
        "line": {
          "endPoint": {
            "coordinate": [
              6.1,
              4.7,
              0
            ],
            "type": "Onshape::Reference::Point"
          },
          "startPoint": {
            "coordinate": [
              6.1,
              3.6,
              0
            ],
            "type": "Onshape::Reference::Point"
          }
        },
        "type": "Onshape::Line"
      }]
  }]
}
`

##### Sketch an arc

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Sketch an arc.",
  "jsonRequests": [ {
    "messageName": "onshapeCreateAnnotations",
    "formatVersion": "2021-01-01",
    "annotations": [
      {
        "arc": {
          "center": {
            "coordinate": [
              1.7,
              1.8,
              0
            ],
            "type": "Onshape::Reference::Point"
          },
          "endAngle": 5.9,
          "radius": 0.5,
          "startAngle": 2.4
        },
        "type": "Onshape::Arc"
      }]
  }]
}
`

##### Sketch a spline

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Sketch a spline.",
  "jsonRequests": [ {
    "messageName": "onshapeCreateAnnotations",
    "formatVersion": "2021-01-01",
    "annotations": [
      {
        "spline": {
          "points": [
            {
              "coordinate": [
                9.3,
                3.5,
                0
              ],
              "type": "Onshape::Reference::Point"
            },
            {
              "coordinate": [
                9.8,
                4.3,
                0
              ],
              "type": "Onshape::Reference::Point"
            },
            {
              "coordinate": [
                10.4,
                4.9,
                0
              ],
              "type": "Onshape::Reference::Point"
            },
            {
              "coordinate": [
                10.3,
                5.8,
                0
              ],
              "type": "Onshape::Reference::Point"
            }
          ]
        },
        "type": "Onshape::Spline"
      }]
  }]
}
`

##### Create a sketch point

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Create a sketch point.",
  "jsonRequests": [ {
    "messageName": "onshapeCreateAnnotations",
    "formatVersion": "2021-01-01",
    "annotations": [
      {
        "sketchPoint": {
          "position": {
            "coordinate": [
              5.7,
              2.3,
              0
            ],
            "type": "Onshape::Reference::Point"
          }
        },
        "type": "Onshape::SketchPoint"
      }]
  }]
}
`

##### Create a sketch grouped with a view

Specify the `viewId` field and `type` in the sketch object (e.g., `circle`, `line`, `arc`, etc.)

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Create a sketch grouped with a view.",
  "jsonRequests": [ {
    "messageName": "onshapeCreateAnnotations",
    "formatVersion": "2021-01-01",
    "annotations": [
      {
        "circle": {
          "center": {
            "coordinate": [
              6.9,
              6.1,
              0
            ],
            "type": "Onshape::Reference::Point"
          },
          "radius": 1.0,
          "viewId": "{viewId}"
        },
        "type": "Onshape::Circle"
      }]
  }]
}
`

##### Edit a sketch

Specify the properties to edit in the sketch object (e.g., `circle`, `line`, `arc`, etc.) for the given sketch’s logical ID. The following example edits the `center` coordinate for an arc.

`{
  "description": "Create a sketch grouped with a view.",
  "jsonRequests": [ {
    "messageName": "onshapeEditAnnotations",
    "formatVersion": "2021-01-01",
    "annotations": [
      {
        "arc": {
          "center": {
            "coordinate": [
              1.7,
              1.8,
              0
            ],
            "type": "Onshape::Reference::Point"
          },
          "endAngle": 5.9,
          "logicalId": "{logicalId}",
          "radius": 0.5,
          "startAngle": 2.4,
          "viewId": "{viewId}"
        },
        "type": "Onshape::Arc"
      }]
  }]
}
`

##### Edit a spline point

Specify both the logical ID of the spline and the spline point.

`{
  "description": "Edit a spline point.",
  "jsonRequests": [ {
    "messageName": "onshapeEditAnnotations",
    "formatVersion": "2021-01-01",
    "annotations": [
      {
        "spline": {
          "splinePoint": {
            "logicalId": "{splinePointLogicalId}",
            "position": {
              "coordinate": [
                9.9,
                7.8,
                0
              ],
              "type": "Onshape::Reference::Point"
            },
            "splineLogicalId": "{splineLogicalId}"
          },
          "type": "Onshape::SplinePoint"
        }
      }]
  }]
}
`

#### Examples - Views

> **Notes**:
> 
> See supported fields in our [sample code](https://github.com/onshape-public/onshapedrawingjson/blob/master/definitions/view.schema.json). Currently, only `TopLevel` and `Projected` view types are supported for creating and editing via the Onshape API. Other view types listed are available for export only.

##### Add a view

The code below adds a view of a part to a drawing.

* Call [getPartsWMVE](https://cad.onshape.com/glassworks/explorer/#/Part/getPartsWMVE) to get a list of part IDs in an element.
* Remove the `idTag` field from the request body to specify a Part Studio or assembly view.

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Add a part view.",
  "jsonRequests": [ 
    {
    "messageName": "onshapeCreateViews",
    "formatVersion": "2021-01-01",
    "description": "Add views",
    "views": [
        {
          "viewType": "TopLevel",
          "position": {"x": 7,"y": 6},
          "scale": {"scaleSource": "Custom", "numerator": 3, "denumerator": 1},
          "orientation": "front",
          "reference": {
            "elementId": "{partStudioOrAssemblyElementId}",
            "idTag": "{partId}"
          }
        }]
    }]
}
`

##### Add projected views

The code below adds three views as children of the view created in the last example. [Export a Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation#export-a-drawing-to-json) to obtain the logicalId of the parent view.

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Add a projected view.",
  "jsonRequests": [ 
    {
    "messageName": "onshapeCreateViews",
    "formatVersion": "2021-01-01",
    "description": "Add views",
    "views": [
        {
            "viewType": "Projected",
            "position": {"x": 16,"y":6},
            "parentView": {"logicalId" : "{parentViewLogicalId}"},
            "name": "ChangedViewName",
            "showViewLabel": true
        },
        {
            "viewType": "Projected",
            "position": {"x": 7,"y":13},
            "parentView": {"logicalId" : "{parentViewLogicalId}"},
            "showShadedView": true,
            "showCentermarks": false
        },
        {
            "viewType": "Projected",
            "position": {"x": 16,"y":13},
            "parentView": {"logicalId" : "{parentViewLogicalId}"},
            "scale": {"scaleSource": "Custom", "numerator": 2, "denumerator": 1},
            "showHiddenLines": true
        }]
    }]
}
`

##### Edit a view

You can edit a view by specifying the view’s logical ID or view ID in the request. Logical IDs are given higher priority.

This code edits the four views added in the previous example. [Export a Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation#export-a-drawing-to-json) to obtain the logicalIds of the views to edit.

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Edit a view.",
  "jsonRequests": [ 
    {
      "messageName": "onshapeEditViews",
      "formatVersion": "2021-01-01",
      "views": [
        {
            "logicalId": "{view1LogicalId}",
            "renderMode": "quality",
            "showHiddenLines": true
        },
        {
            "logicalId": "{view2LogicalId}",
            "suppressAlignmentWithParent": true,
            "rotation": "45 * Math.PI/180",
        },
        {
            "viewId": "{view3ViewId}",
            "showShadedView": false,
            "showCentermarks": true,
            "showViewLabel": true,
            "showScaleLabel": true,
            "label": "Top View"
        },
        {
            "logicalId": "{view4ViewId}",
            "scale": {"scaleSource": "Parent"},
            "showHiddenLines": false,
            "sheet": {"index": 2}
        }]
    }]
}
`

#### Examples - Dimensions

##### Add a dimension to a drawing

1. Open an Onshape drawing. This example uses the drawing created in the [Create a drawing from a part](#create-a-drawing-from-a-part) tutorial.
2. Start to form the [modifyDrawing](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing) call. Replace the URL parameters with the values from your document, and replace `CREDENTIALS` with your authorization credentials.  
```  
curl -X 'POST \  
  'https://cad.onshape.doc/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/modify' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
```
3. Add information about the modification. In this example, we’ll add an `Onshape::Dimension` to the drawing. We must specify the `messageName` and `formatVersion` for the modification, and then provide the coordinates and formatting options for the dimension. (Hint: you can [Export a Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation/#export-a-drawing-to-json) to get a list of valid coordinates and handles.)  
```  
curl -X 'POST \  
  'https://cad.onshape.doc/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/modify' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
        "description": "Add a dimension",  
        "jsonRequests": [ {  
          "messageName": "onshapeCreateAnnotations",  
          "formatVersion": "2021-01-01",  
          "annotations": [  
            {  
              "radialDimension": {  
                "centerPoint": {  
                  "coordinate": [  
                    0.2800021171569824,  
                    0.014964947476983043,  
                    0.079502  
                  ],  
                  "type": "Onshape::Reference::Point",  
                  "uniqueId": "point1",  
                  "viewId": "e11c38795c04ca55047f7ea7",  
                  "snapPointType": "ModeCenter"  
                },  
                "chordPoint": {  
                  "coordinate": [  
                    0.2920149764955524,  
                    0.010030535983985095,  
                    0.079502  
                  ],  
                  "type": "Onshape::Reference::Point",  
                  "uniqueId": "point2",  
                  "viewId": "e11c38795c04ca55047f7ea7",  
                  "snapPointType": "ModeNear"  
                },  
                "formatting": {  
                  "dimdec": 2,  
                  "dimlim": false,  
                  "dimpost": "R<>",  
                  "dimtm": 0,  
                  "dimtol": false,  
                  "dimtp": 0,  
                  "type": "Onshape::Formatting::Dimension"  
                },  
                "textOverride": "",  
                "textPosition": {  
                  "coordinate": [  
                    191.80537349378181,  
                    89.76274130852224,  
                    0  
                  ],  
                  "type": "Onshape::Reference::Point"  
                }  
              },  
              "type": "Onshape::Dimension::Radial"  
            }  
          ]  
        }]  
      }'  
```
4. Make the call, and then get `id` from the response body. You’ll need this to poll the modification status to figure out when the modification has completed.
5. Poll the [modification status](#requestState) and wait for the modification to finish.
6. Open your drawing and confirm that you see the new dimension.

##### Add a chamfer dimension to a drawing

1. Open an Onshape drawing. This example uses the drawing created in the [Create a drawing from a part](#create-a-drawing-from-a-part) tutorial.
2. Start to form the [modifyDrawing](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing) call. Replace the URL parameters with the values from your document, and replace `CREDENTIALS` with your authorization credentials.  
```  
curl -X 'POST \  
  'https://cad.onshape.doc/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/modify' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
```
3. Add information about the modification. In this example, we’ll add an `Onshape::Dimension::Chamfer` to the drawing. We must specify the `messageName` and `formatVersion` for the modification, and then provide the information for the dimension. (Hint: you can [Export a Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation/#export-a-drawing-to-json) to get a list of valid coordinates and handles.)  
```  
curl -X 'POST \  
  'https://cad.onshape.doc/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/modify' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
        "description": "Add a chamfer dimension",  
        "jsonRequests": [ {  
          "messageName": "onshapeCreateAnnotations",  
          "formatVersion": "2021-01-01",  
          "annotations": [  
            {  
              "chamferDimension": {  
                "displayedValue": ".250 X 45.0°", // Display value  
                "edge1End": {  
                    "coordinate": [  
                        0.0,  
                        -0.0063499999999999945,  
                        0.012700000000000003  
                    ],  
                    "snapPointType": "ModeEnd",  
                    "type": "Onshape::Reference::Point",  
                    "uniqueId": "{edge1Id}", // Unique ID of the edge  
                    "viewId": "{viewId}" // View ID of the drawing  
                },  
                "edge1Start": {  
                    "coordinate": [  
                        0.0063500000000000015,  
                        0.0,  
                        0.012700000000000003  
                    ],  
                    "snapPointType": "ModeStart",  
                    "type": "Onshape::Reference::Point",  
                    "uniqueId": "{edge1Id}", // Unique ID of the edge  
                    "viewId": "{viewId}" // View ID of the drawing  
                },  
                "edge2End": {  
                    "coordinate": [  
                        0.07619999999999998,  
                        0.0,  
                        0.012700000000000003  
                    ],  
                    "snapPointType": "ModeEnd",  
                    "type": "Onshape::Reference::Point",  
                    "uniqueId": "{edge2Id}", // Unique ID of the edge  
                    "viewId": "{viewId}" // View ID of the drawing  
                },  
                "edge2Start": {  
                    "coordinate": [  
                        0.0063500000000000015,  
                        0.0,  
                        0.012700000000000003  
                    ],  
                    "snapPointType": "ModeStart",  
                    "type": "Onshape::Reference::Point",  
                    "uniqueId": "{edge2Id}", // Unique ID of the edge  
                    "viewId": "{viewId}" // View ID of the drawing  
                },  
                "firstChamferOverride": "", // Override the first value in the displayedValue field  
                "formatting": {  
                    "dimdec": 3.0,  
                    "dimlim": false,  
                    "dimpost": " POST",  
                    "dimtm": 0.0,  
                    "dimtol": false,  
                    "dimtp": 0.0,  
                    "type": "Onshape::Formatting::Dimension"  
                },  
                "logicalId": "h:10000124",  
                "measurementAngle": 0.7853981633974478, // Angle of the chamfer  
                "measurementLength": 0.2500000000000002, // Length of the chamfer  
                "prefix": "PRE ", // Text to appear before the display value  
                "secondChamferOverride": "", // Override the second value in the displayedValue field  
                "suffix": " POST", // Text to appear after the display value  
                "textAbove": "ABOVE", // Text to appear above the display value  
                "textBelow": "BELOW", // Text to appear below the display value  
                "textPosition": { // Location of display value  
                    "coordinate": [  
                        1.114880743466248,  
                        6.783806096154582,  
                        0.0  
                    ],  
                    "type": "Onshape::Reference::Point"  
                }  
            },  
            "type": "Onshape::Dimension::Chamfer"  
            }  
          ]  
        }]  
      }'  
```
4. Make the call, and then get `id` from the response body. You’ll need this to poll the modification status to figure out when the modification has completed.
5. Poll the [modification status](#requestState) and wait for the modification to finish.
6. Open your drawing and confirm that you see the new chamfer dimension.

##### Create ordinate dimensions

Create ordinate dimensions (also known as (X, Y) pairs) for a feature measured from a datum. Ordinate dimensions created as a group move together when one is moved.

* [Export the Drawing to JSON](#export-a-drawing-to-json) to obtain the point coordinates and the deterministic and view IDs to specify.
* To edit an ordinate dimension, use `messageName = onshapeEditAnnotations` and provide the dimension’s `logicalId`
* Stack the dimension group horizontally or vertically with `dimensionGroup.type = horizontal | vertical`

  
![ordinate dimension examples](https://onshape-public.github.io/docs/api-adv/drawings/images/drawings-dimensions-ord-02.png)  

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Create ordinate dimensions",
  "jsonRequests": [ {  
    "messageName": "onshapeCreateAnnotations",  
    "formatVersion": "2021-01-01",  
    "annotations": [  
      {  
        "ordinateDimension": {
          "dimensionGroup": [
            {
              "attachmentPoint": {
                "coordinate": [<xOne>, <yOne>, <zOne>],
                "deterministicId": <deterministicIdPointOne>,
                "snapPointType": "ModeStart",
                "type": "Onshape::Reference::Point",
                "viewId": <viewIdDrawing>
              },
              "isOrigin": true,
              "textPosition": {
                "coordinate": [<xTwo>, <yTwo>, <zTwo>],
                "type": "Onshape::Reference::Point"
              }
            },
            {
              "attachmentPoint": {
                "coordinate": [<xThree>, <yThree>, <zThree>],
                "deterministicId": <deterministicIdPointTwo>,
                "snapPointType": "ModeStart",
                "type": "Onshape::Reference::Point",
                "viewId": <viewIdDrawing>
              },
              "isOrigin": false,
              "textPosition": {
                "coordinate": [<xFour>, <yFour>, <zFour>],
                "type": "Onshape::Reference::Point"
              }
            }
          ],
          "type": "vertical"
        },
        "type": "Onshape::Dimension::Ordinate"
      }]
  }]
}
`

##### Add text or symbols to a dimension

You can add text or symbols to display with any dimension:

  
![annotation with text above, below, before, and after the dimension](https://onshape-public.github.io/docs/api-adv/drawings/images/drawings-prefix-02.png)  

Add the following fields to any dimension definition.

`{
  "prefix": "%%c",  
  "suffix": " (x20)",  
  "textAbove": "FLAT WASHER",  
  "textBelow": "STEEL"
} 
`

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Add a dimension with text and symbols.",
  "jsonRequests": [ {  
    "messageName": "onshapeCreateAnnotations",  
    "formatVersion": "2021-01-01",  
    "annotations": [  
      {  
        "lineToLineDimension": {
          // ...  
          "prefix": "%%c",  
          "suffix": " (x20)",  
          "textAbove": "FLAT WASHER",  
          "textBelow": "STEEL"
          // ...
        },
        "type": "Onshape::Dimension::LineToLine"  
      }]  
  }]
}
`

If editing an existing dimension, [export the Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation#export-a-drawing-to-json) to obtain the dimension’s logical ID.

`{
  "description": "Add text or symbols to an existing dimension.",
  "jsonRequests": [ {  
    "messageName": "onshapeEditAnnotations",  
    "formatVersion": "2021-01-01",  
    "annotations": [  
      {  
        "pointToPointDimension": {  
          "logicalId": "h:10000675",  
          "prefix": "Prefix",  
          "suffix": "Suffix",  
          "textAbove": "Above",  
          "textBelow": "Below"
        },  
        "type": "Onshape::Dimension::PointToPoint"  
      }]  
  }]
}
`

##### Set dimension precision

By default, precision is set in the [Onshape Drawings Properties panel](https://cad.onshape.com/help/Content/drawings-properties.htm#Units), and the `isPrecisionOverridden` field in API is set to `false.`

To manually set the `precision` value when creating or editing a dimension via the API, set `isPrecisionOverridden` to `true` to override the value in the Onshape Drawings Properties panel.

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Bodies**

To set precision, set `isPrecisionOverridden` to `true` and supply the `precision` field:

`{
  "description": "Set dimension precision.",
  "jsonRequests": [ {  
    "messageName": "onshapeEditAnnotations",  
    "formatVersion": "2021-01-01",  
    "annotations": [  
      {  
        "lineToLineDimension": {  
          "logicalId": "h:100001DD",
          "isPrecisionOverridden": true,
          "precision": 3
        },  
        "type": "Onshape::Dimension::LineToLine"  
      }]  
  }]
}
`

#### Examples - Tolerances

##### Add a dimension with a symmetrical tolerance

[Export a Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation#export-a-drawing-to-json) to obtain the deterministic, unique, and view IDs to specify.

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Add a dimension with a symmetrical tolerance.",
  "jsonRequests": [ {  
    "messageName": "onshapeCreateAnnotations",  
    "formatVersion": "2021-01-01",  
    "annotations": [  
      {  
        "pointToPointDimension": {  
          "point1": {  
            "coordinate": [  
              -0.022788484925716336,  
              0.06710318401608831,  
              0.004825999999999999  
            ],  
            "deterministicId": "JIV",  
            "snapPointType": "ModeEnd",  
            "type": "Onshape::Reference::Point",  
            "uniqueId": "F4245",  
            "viewId": "2b2608befce5281dc1f651e9"  
          },  
          "point2": {  
            "coordinate": [  
              0.06483851512571645,  
              0.06710318401608831,  
              0.004825999999999999  
            ],  
            "deterministicId": "JIV",  
            "snapPointType": "ModeStart",  
            "type": "Onshape::Reference::Point",  
            "uniqueId": "F4245",  
            "viewId": "2b2608befce5281dc1f651e9"  
          },
          "textPosition": {  
            "coordinate": [  
              4.8346992569387219,  
              5.660045658601707,  
              0  
            ],  
            "type": "Onshape::Reference::Point"  
          },  
          "tolerance": {  
            "type": "Symmetrical",  
            "upperValue": 2.14  
          }
        },  
        "type": "Onshape::Dimension::PointToPoint"  
      }]
  }]
}
`

##### Add a dimension with a basic tolerance

[Export a Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation#export-a-drawing-to-json) to obtain the IDs of the edges and views.

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Add a dimension with a basic tolerance.",
  "jsonRequests": [ {  
    "messageName": "onshapeCreateAnnotations",  
    "formatVersion": "2021-01-01",  
    "annotations": [  
      {  
        "lineToLineDimension": {  
          "edge1": {  
            "deterministicId": "JIV",  
            "type": "Onshape::Reference::Edge",  
            "uniqueId": "F4245",  
            "viewId": "2b2608befce5281dc1f651e9"  
          },  
          "edge2": {  
            "deterministicId": "JJV",  
            "type": "Onshape::Reference::Edge",  
            "uniqueId": "F4243",  
            "viewId": "2b2608befce5281dc1f651e9"  
          },  
          "rotation": 0,  
          "textOverride": "",  
          "textPosition": {  
            "coordinate": [  
              4.731016024253847,  
              3.189199999999999,  
              0  
            ],  
            "type": "Onshape::Reference::Point"
          },  
          "tolerance": {  
            "type": "Basic"  
          }  
        },  
        "type": "Onshape::Dimension::LineToLine"  
      }]  
  }]
}
`

##### Add a dimension with a deviation tolerance

[Export a Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation#export-a-drawing-to-json) to obtain the IDs to specify.

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Add a dimension with a deviation tolerance.",
  "jsonRequests": [ {  
    "messageName": "onshapeCreateAnnotations",  
    "formatVersion": "2021-01-01",  
    "annotations": [  
      {  
        "pointToPointDimension": {  
          "point1": {  
            "coordinate": [  
              -0.022788484925716308,  
              0.06710318401608836,  
              0.004825999999999999  
            ],  
            "deterministicId": "JIV",  
            "snapPointType": "ModeEnd",  
            "type": "Onshape::Reference::Point",  
            "uniqueId": "F4245",  
            "viewId": "2b2608befce5281dc1f651e9"  
          },  
          "point2": {  
            "coordinate": [  
              0.0648385151257165,  
              0.06710318401608836,  
              0.004825999999999999  
            ],  
            "deterministicId": "JIV",  
            "snapPointType": "ModeStart",  
            "type": "Onshape::Reference::Point",  
            "uniqueId": "F4245",  
            "viewId": "2b2608befce5281dc1f651e9"
          },  
          "rotation": 0,  
          "textPosition": {  
            "coordinate": [  
              6.379999999999999,  
              9.903619353521464,  
              0  
            ],  
            "type": "Onshape::Reference::Point"  
          },  
          "tolerance": {  
            "lowerValue": 1.52,  
            "type": "Deviation",  
            "upperValue": 4.25  
          } 
        },  
        "type": "Onshape::Dimension::PointToPoint"  
      }]  
  }]
}
`

##### Add a dimension with a limit tolerance

[Export a Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation#export-a-drawing-to-json) to obtain the IDs to specify.

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Add a dimension with a limit tolerance.",
  "jsonRequests": [ {  
    "messageName": "onshapeCreateAnnotations",  
    "formatVersion": "2021-01-01",  
    "annotations": [  
      {  
        "pointToPointDimension": {  
          "point1": {  
            "coordinate": [  
              -0.022788484925716308,
              0.06710318401608836,  
              0.004825999999999999  
            ],  
            "deterministicId": "JIV",  
            "snapPointType": "ModeEnd",  
            "type": "Onshape::Reference::Point",  
            "uniqueId": "F4245",  
            "viewId": "2b2608befce5281dc1f651e9"  
          },  
          "point2": {  
            "coordinate": [  
              0.0648385151257165,  
              0.06710318401608836,  
              0.004825999999999999  
            ],  
            "deterministicId": "JIV",  
            "snapPointType": "ModeStart",  
            "type": "Onshape::Reference::Point",  
            "uniqueId": "F4245",  
            "viewId": "2b2608befce5281dc1f651e9"  
          },  
          "rotation": 0,  
          "textPosition": {  
            "coordinate": [  
              6.379999999999999,  
              9.492751572521588,  
              0  
            ],  
            "type": "Onshape::Reference::Point"  
          },  
          "tolerance": {  
            "lowerValue": 2.5,  
            "type": "Limit",  
            "upperValue": 4.5  
          } 
        },  
        "type": "Onshape::Dimension::PointToPoint"  
      }]  
  }]
}
`

##### Add a dimension with a minimum tolerance

[Export a Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation#export-a-drawing-to-json) to obtain the IDs to specify.

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Add a dimension with a minimum tolerance.",
  "jsonRequests": [ {  
    "messageName": "onshapeCreateAnnotations",  
    "formatVersion": "2021-01-01",  
    "annotations": [  
      {  
        "pointToPointDimension": {  
          "point1": {  
            "coordinate": [  
              -0.022788484925716308,  
              0.06710318401608836,  
              0.004825999999999999  
            ],  
            "deterministicId": "JIV",  
            "snapPointType": "ModeEnd",  
            "type": "Onshape::Reference::Point",  
            "uniqueId": "F4245",  
            "viewId": "2b2608befce5281dc1f651e9"  
          },  
          "point2": {  
            "coordinate": [  
              0.0648385151257165,  
              0.06710318401608836,  
              0.004825999999999999  
            ],  
            "deterministicId": "JIV",  
            "snapPointType": "ModeStart",  
            "type": "Onshape::Reference::Point",  
            "uniqueId": "F4245",  
            "viewId": "2b2608befce5281dc1f651e9"
          },  
          "textPosition": {  
            "coordinate": [  
              6.379999999999999,  
              9.61398841181059,  
              0  
            ],  
            "type": "Onshape::Reference::Point"  
          },  
          "tolerance": {  
            "type": "MIN"  
          } 
        },  
        "type": "Onshape::Dimension::PointToPoint"  
      }]  
  }]
}
`

##### Add a dimension with a maximum tolerance

[Export a Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation#export-a-drawing-to-json) to obtain the IDs to specify.

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Add a dimension with a maximum tolerance.",
  "jsonRequests": [ {  
    "messageName": "onshapeCreateAnnotations",  
    "formatVersion": "2021-01-01",  
    "annotations": [  
      {  
        "pointToPointDimension": {  
          "point1": {  
          "coordinate": [  
              -0.022788484925716308,  
              0.06710318401608836,  
              0.004825999999999999  
            ],
            "deterministicId": "JIV",  
            "snapPointType": "ModeEnd",  
            "type": "Onshape::Reference::Point",  
            "uniqueId": "F4245",  
            "viewId": "2b2608befce5281dc1f651e9"  
          },  
          "point2": {  
            "coordinate": [  
              0.0648385151257165,  
              0.06710318401608836,  
              0.004825999999999999  
            ],  
            "deterministicId": "JIV",  
            "snapPointType": "ModeStart",  
            "type": "Onshape::Reference::Point",  
            "uniqueId": "F4245",  
            "viewId": "2b2608befce5281dc1f651e9"  
          },  
          "textPosition": {  
            "coordinate": [  
              2.6531471291300536,  
              6.378399999999999,  
              0  
            ],  
            "type": "Onshape::Reference::Point"  
          },  
          "tolerance": {  
            "type": "MAX"  
          } 
        },  
        "type": "Onshape::Dimension::PointToPoint"  
      }]
  }]
}
`

##### Add a dimension with a fit class tolerance

You can add three types of fit class tolerance to a dimension (`Fit` | `FitWithTolerance` | `FitToleranceOnly`):

`{
  "tolerance": {  
    "fitType": "Clearance | Transition | Interference | Userdefined",  
    "holeClass": "H8", 
    "precision": 6, 
    "shaftClass": "e7",  
    "type": "Fit | FitWithTolerance | FitToleranceOnly" 
  }  
}
`

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Add a dimension with a fit class tolerance.",
  "jsonRequests": [ {  
    "messageName": "onshapeCreateAnnotations",  
    "formatVersion": "2021-01-01",  
    "annotations": [  
      {  
        "lineToLineDimension": {  
          // ...
          "tolerance": {  
            "fitType": "Clearance",  
            "holeClass": "H8",  
            "precision": 6,
            "shaftClass": "e7",
            "type": "FitWithTolerance"  
          }  
        },  
        "type": "Onshape::Dimension::LineToLine"  
      }]  
  }]
}
`

If editing an existing dimension, [export the Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation#export-a-drawing-to-json) to obtain the dimension’s logical ID.

`{
  "description": "Add a fit class tolerance to an existing dimension.",
  "jsonRequests": [ {  
    "messageName": "onshapeEditAnnotations",  
    "formatVersion": "2021-01-01",  
    "annotations": [  
      {  
        "pointToPointDimension": {  
          "logicalId": "h:10000675",  
          "tolerance": {  
            "fitType": "Interference",  
            "holeClass": "H7",  
            "precision": 6,
            "shaftClass": "f6",  
            "type": "FitToleranceOnly"  
          }
        },  
        "type": "Onshape::Dimension::PointToPoint"  
      }]  
  }]
}
`

##### Add a tolerance to an existing dimension

[Export a Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation#export-a-drawing-to-json) to obtain the dimension’s logical ID.

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Add a tolerance to an existing dimension.",
  "jsonRequests": [ {  
    "messageName": "onshapeEditAnnotations",  
    "formatVersion": "2021-01-01",  
    "annotations": [  
      {  
      "pointToPointDimension": {  
        "logicalId": "h:10000A0A",  
        "tolerance": {  
          "lowerValue": 2.14000001,  
          "type": "Deviation",  
          "upperValue": 2.140000001
        }  
      },  
      "type": "Onshape::Dimension::PointToPoint"  
      }  
    ]  
  }]
}
`

##### Edit a dimension tolerance type

[Export a Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation#export-a-drawing-to-json) to obtain the dimension’s logical ID.

**Endpoint**

[POST /drawings/d/did/w/wid/e/eid/modify](https://cad.onshape.com/glassworks/explorer/#/Drawing/modifyDrawing)

**Request Body**

`{
  "description": "Edit a dimension tolerance type",
  "jsonRequests": [ {  
    "messageName": "onshapeEditAnnotations",  
    "formatVersion": "2021-01-01",  
    "annotations": [  
      {  
      "lineToLineDimension": {  
        "logicalId": "h:10000A3D",  
        "tolerance": {  
          "type": "None"  
        } 
      },  
      "type": "Onshape::Dimension::LineToLine"  
      }]
  }]
}
`

#### Examples - Other

##### Find dangling entities

To identify dangling entities, you can export a drawing to JSON and search for any entities where `isDangling` is set to `true`.

1. Make a copy of [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/cf017fd148581f0fdc68c182/e/4edb4245a9c0121c2d5b4fd2) so you can export the drawing. Make a note of the document ID, workspace ID, and element ID of the drawing in your new document. These will be your `{did}`, `{wid}`, and `{eid}` fields for this example, unless otherwise specified.  
    
![Drawing with a dangling note and inspection symbol](https://onshape-public.github.io/docs/api-adv/drawings/images/drawings-dangling-annotations-01.png)  
    
When this drawing was created, the drill bit part included a fillet. That fillet has since been deleted, so the attached note (`This is a fillet`) and inspection item (`2`) are now dangling. Since this is a simple drawing with only a few annotations, it is easy to visually identify the dangling entities. However, in large or complex drawings, it can be helpful to obtain a list of dangling entities from the JSON export.
2. Use the [createDrawingTranslation](https://cad.onshape.com/glassworks/explorer/#/Drawing/createDrawingTranslation) endpoint to export the drawing to JSON. See the [Export a Drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation#export-a-drawing-to-json) tutorial for help. Your call should look like this:  
```curl  
curl -X 'POST' \  
'https://cad.onshape.com/api/v10/drawings/d/{did}/w/{wid}/e/{eid}/translations' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
        "formatName": "DRAWING_JSON"  
      }'  
```
3. Open the `DRILL_BIT.json` file from your document or by calling the [BlobElement/downloadFileWorkspace](https://cad.onshape.com/glassworks/explorer/#/BlobElement/downloadFileWorkspace) endpoint on the new JSON element.
4. In the JSON, search for the `isDangling` field. You’ll see that the first two annotations (`This is a note` and inspection symbol `number: 1.0`) are not dangling.  
`    {  
        "note": {  
            "contents": "{\\pxql;This is a note}",  
            "isDangling": false,  
            "logicalId": "h:100000EA",  
            "position": {  
                "coordinate": [  
                    1.9878571202278066,  
                    7.1981053727755056,  
                    0.0  
                ],  
                "type": "Onshape::Reference::Point"  
            },  
            "textHeight": 0.12  
        },  
        "type": "Onshape::Note"  
    },  
    {  
        "inspectionSymbol": {  
            "borderShape": "Circle",  
            "borderSize": 2.0,  
            "isDangling": false,  
            "itemParsing": "eByRow",  
            "logicalId": "h:100000EB",  
            "number": 1.0,  
            "parentAnnotation": "h:100000EA",  
            "parentLineIndex": 0,  
            "position": {  
                "coordinate": [  
                    1.8438571202278065,  
                    7.135399026040281,  
                    0.0  
                ],  
                "type": "Onshape::Reference::Point"  
            },  
            "textHeight": 0.08  
        },  
        "type": "Onshape::InspectionSymbol"  
    }  
`

If you scroll further, however, you’ll see that the next set of annotations (`This is a fillet` and inspection symbol `number: 2.0`) have `isDangling` set to `true`. These annotations are dangling and must be corrected in the drawing.

`  {
    "note": {
        "contents": "{\\pxqr;This is a fillet}",
        "isDangling": true,
        "leaderPosition": {
            "coordinate": [
                -0.0054142135623728715,
                0.24941421356237314,
                1.496198998029996e-17
            ],
            "snapPointType": "ModeMid",
            "type": "Onshape::Reference::Point",
            "uniqueId": "F426D",
            "viewId": "4868551da0b69cd0712723ae"
        },
        "logicalId": "h:100000EF",
        "position": {
            "coordinate": [
                2.995234893572328,
                6.3423785618475375,
                0.0
            ],
            "type": "Onshape::Reference::Point"
        },
        "textHeight": 0.12
    },
    "type": "Onshape::Note"
},
{
    "inspectionSymbol": {
        "borderShape": "Circle",
        "borderSize": 2.0,
        "isDangling": true,
        "itemParsing": "eByRow",
        "logicalId": "h:100000F7",
        "number": 2.0,
        "parentAnnotation": "h:100000EF",
        "parentLineIndex": 0,
        "position": {
            "coordinate": [
                1.8469297164606113,
                6.342509182410414,
                0.0
            ],
            "type": "Onshape::Reference::Point"
        },
        "textHeight": 0.08
    },
    "type": "Onshape::InspectionSymbol"
  }
`

1. In the drawing, select the dangling note and inspection symbol, and press the `delete` key.
2. Repeat steps 2 through 4 above for the updated drawing. Notice that all `isDangling` fields are now set to `false`.

> 📘 **Note**
> 
> Not all drawing objects support the `isDangling` field. If the `isDangling` field is not returned for an object or annotation in your drawing, no conclusions can be drawn from the API about the dangling status of the object.

##### Export a drawing to JSON

In this example, we’ll export a drawing from [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/15b07287508246ccd038e31e) to JSON. Exporting a Drawing to JSON is useful when you need to gather information about that drawing (for example, finding valid coordinates on which to place an inspection symbol).

> 📘 **Notes**
> 
> * Notes are exported with [RTF15](https://www.biblioscape.com/rtf15%5Fspec.htm) formatting.
> * Flags are not currently exported with notes.
> * Geometric tolerance frame fields are separated with `%%v`.
> * Geometric tolerance prefix and suffix fields are currently not exported.

1. Make a copy of [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/15b07287508246ccd038e31e) so you can export the drawing. Make a note of the documentId, workspaceId, and elementId of the drawing in your new document. These will be your `{did}`, `{wid}`, and `{eid}` fields for this example, unless otherwise specified.
2. Validate that JSON is a supported export file type for Drawings by calling [Drawing/getDrawingTranslatorFormats](https://cad.onshape.com/glassworks/explorer/#/Drawing/getDrawingTranslatorFormats) and confirming that `"name": "DRAWING_JSON"` appears in the response for the drawing element in your copied document.  
**request**  
```  
curl -X 'GET' \  
'https://cad.onshape.com/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/translationformats' \  
  -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS'  
```  
**response**  
```  
[  
  {  
    "name": "DRAWING_JSON",  
    "translatorName": "drawing_json",  
    "couldBeAssembly": false  
  },  
  ...  
]  
```
3. Initialize the export by calling [Drawing/createDrawingTranslation](https://cad.onshape.com/glassworks/explorer/#/Drawing/createDrawingTranslation). Replace `{did}`, `{wid}`, and `{eid}` with the document, workspace, and element IDs from your copied document. Do NOT include the curly braces (`{}`) in the final call.  
```  
curl -X 'POST' \  
  'https://cad.onshape.com/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/translations' \  
  -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
      "formatName": "DRAWING_JSON"  
      }'  
```  
   * Note that the API takes a JSON as part of the request body, in which you can specify options for the export.  
   * The only required JSON field is `formatName`, in which we’ve specified the format as found in the `getDrawingTranslatorFormats` response body.  
   * The `formatName` value must match the `name` field from the previous step exactly, including casing.
4. In the response, copy the `translationId` value from the `id` field. This is the ID of the translation itself.  
```  
{  
  "requestState": "ACTIVE",  
  "requestElementId": "{eid}",  
  "resultExternalDataIds": null,  
  "versionId": null,  
  "workspaceId": "{wid}",  
  "documentId": "{did}",  
  "resultElementIds": null,  
  "resultDocumentId": "{did}",  
  "failureReason": null,  
  "resultWorkspaceId": "{wid}",  
  "name": "GEARBOX_CHUCK",  
  "id": "{translationId}",  
  "href": "https://cad.onshape.com/api/v9/translations/{translationId}"  
}  
```
5. Next, poll the [Translation/getTranslation](https://cad.onshape.com/glassworks/explorer/#/Translation/getTranslation) response until `requestState` changes from `ACTIVE` to `DONE` or `FAILED`.  
```  
{  
  "requestState": "DONE",  
  "requestElementId": "{eid}",  
  "resultExternalDataIds": {resultElementId},  
  "versionId": null,  
  "workspaceId": "{wid}",  
  "documentId": "{did}",  
  "resultElementIds": {resultElementId},  
  "resultDocumentId": "{did}",  
  "failureReason": null,  
  "resultWorkspaceId": "{wid}",  
  "name": "GEARBOX_CHUCK",  
  "id": "{translationId}",  
  "href": "https://cad.onshape.com/api/v9/translations/{translationId}"  
}  
```
6. Once `requestState=DONE`, the JSON is uploaded to the Onshape document in a new element (tab). The element ID of the JSON blob will either appear in the `resultExternalDataIds` or `resultElementIds` field in the response.
7. Now, we can call [BlobElement/downloadFileWorkspace](https://cad.onshape.com/glassworks/explorer/#/BlobElement/downloadFileWorkspace) to retrieve the exported results.  
```  
curl -X 'GET' \  
'https://cad.onshape.com/api/v6/blobelements/d/{did}/w/{wid}/e/{resultElementId}' \  
-H 'Authorization: Basic CREDENTIALS' \  
  -H 'accept: application/octet-stream'  
```  
   * Use the `{resultElementId}` value from the translation response as the element ID. Do not include the curly braces in your call.  
   * Note that you can also open your document, click the `GEARBOX_CHUCK.JSON` tab, and download the file from there.

##### Find bounding box details

1. [Export a drawing to JSON](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-adv/translation#export-a-drawing-to-json).
2. For each bounding box in the drawing, the response includes a `boundingBoxPoints` field that specifies the box coordinates.

#### Additional Resources

* [Guide to Onshape APIs](https://onshape-public.github.io/docs/api-adv/drawings/docs/api-intro//#onshape-api-request)
* \[Guide to the API Explorer\](https://onshape-public.github.io/docs/api-adv/drawings/ docs/api-intro/explorer)
* [API Explorer: Drawings](https://cad.onshape.com/glassworks/explorer/#/Drawing)
* [Onshape Help: Drawings](https://cad.onshape.com/help/Content/drawings.htm)

---

<a id="pg-docs-api-adv-errors"></a>
### Response Codes

_Source: <https://onshape-public.github.io/docs/api-adv/errors/>_

This page details some of the response codes that may be returned by Onshape API endpoints. For each response code, we’ve provided a brief description of the response and recommended next steps.

#### Success (2xx)

The client call was successful.

##### 200 OK

The client call was successful. No action needed.

##### 204 No Content

The client call was successful, and there’s nothing to return in the response body. The empty response body cannot be parsed.

#### Redirect (3xx)

##### 307 Temporary Redirect

The client call was successful, and a redirection URL was returned. Follow the URL provided in the response.

#### Client Error (4xx)

There’s an error with the client request. Find the error code below, and follow the instructions for resolution. Calls that return 4xx response codes do not count against [API Limits](https://onshape-public.github.io/docs/api-adv/errors/docs/auth/limits).

##### 400 Bad Request

The request cannot be processed by the server due a client-side error. This could be a malformed request syntax or other issue. Check the request parameters (GET and POST) and request body (POST) to determine the cause of the failure.

##### 401 Unauthorized

The request failed the authentication/authorization checks. This could mean you are not logged in to Onshape, your API keys are invalid or for a different server, OAuth failed, etc.

Make sure the client is [authenticated](https://onshape-public.github.io/docs/auth/).

##### 402 Payment Required

[API Limits](https://onshape-public.github.io/docs/api-adv/errors/docs/auth/limits) have been reached. Reach out to your Onshape representative or [api‑support@onshape.com](mailto:api-support@onshape.com) for more information.

##### 403 Forbidden

The client doesn’t have the correct permissions to perform this operation. Check that the [API Keys or OAuth authentication](https://onshape-public.github.io/docs/auth/) have sufficient permissions to perform the operation. For example, POST operations typically require `write` scope; if the API Key was created with only `read` scope, the server will return a 403 error.

You might also need to check document and user permissions. For more details, see [Share Documents](https://cad.onshape.com/help/Content/sharedocuments.htm) (for everyone) and [Understanding and Administering Project Roles and Permission Schemes](https://cad.onshape.com/help/Content/EnterpriseHelp/Content/permission%5Fschemes.htm) (for Enterprise users and administrators).

##### 404 Not Found

The server can’t find what the client is looking for. For example, a 404 error will be returned if the client tries to make a GET request for a document that doesn’t exist.

##### 405 Method Not Allowed

Use of that method is not supported. For example, you cannot perform a DELETE request on a document version, because versions are read-only. Only GET requests on document versions are allowed.

##### 406 Not Acceptable

The server cannot provide a response for the media type requested. See <https://datatracker.ietf.org/doc/html/rfc2616#section-6.1.1>.

##### 409 Conflict

The client call includes duplicate values, causing a conflict. Modify the request to remove any conflicting values.

##### 415 Media Type Not Supported

The client call includes unsupported data types or invalid JSON. Review the client code. When performing data imports and exports, follow all [Translation guidelines](https://onshape-public.github.io/docs/api-adv/translation/) to ensure all media and file types are supported.

##### 429 Too Many Requests

The client sent too many requests to this endpoint in the Onshape-defined time window. The number of requests allowed per time window vary and are subject to change; Onshape does not publish this information.

Every Onshape API response includes the `X-Rate-Limit-Remaining` header. This is the number of times you are allowed to call this particular endpoint again within the Onshape-defined time window. For example, the following response indicates that you can call this endpoint _3000_ more times within the time window:

**200 Response** (_Additional headers may be returned._)

`<Response [200]>
{
    'Date': 'Tue, 22 Apr 2025 18:10:46 GMT', 
    'Content-Type': 'application/json;charset=utf-8', 
    'X-Api-Version': 'v10', 
    'On-Version': '1.196.54436.927372740f35', 
    'X-Rate-Limit-Remaining': '3000'
}
`

If you exceed this number of calls during the time window, you’ll receive the `429` response code with a `Retry-After` header. This is the number of seconds before the counter for this endpoint resets. You can use this value as a delay to prevent hitting the `429` error again.

In the example below, the user has `0` retries left in the `X-Rate-Limit-Remaining` header, and must wait `450` seconds before calling the endpoint again, as noted in the `Retry-After` header.

**429 Response** (_Additional headers may be returned._)

`<Response [429]>
{
    'Date': 'Tue, 22 Apr 2025 18:16:16 GMT', 
    'Content-Type': 'application/json', 
    'X-Api-Version': 'v10', 
    'On-Version': '1.196.54436.927372740f35', 
    'X-Rate-Limit-Remaining': '0', 
    'Retry-After': '450'
}
`

Onshape also limits the number of annual calls each account can make. See [API Limits](https://onshape-public.github.io/docs/api-adv/errors/docs/auth/limits/) for details.

##### 499 Timeout

This call is taking too long. Please try again later.

#### Server Error (5xx)

There’s an error with the Onshape servers. Find the error code below, and follow the instructions for resolution. Calls that return 5xx response codes do not count against [API Limits](https://onshape-public.github.io/docs/api-adv/errors/docs/auth/limits).

##### 500 Internal Server Error

The request resulted in an error. Set a limit for the number of retries, and if the request continues to fail, reach out to [support](mailto:api-support@onshape.com).

##### 503 Service Unavailable

Something is wrong with the Onshape servers. Retry after the delay specified in the response. Set a limit for the number of retries, and if the request continues to fail, reach out to [support](mailto:api-support@onshape.com).

---

<a id="pg-docs-api-adv-featureaccess"></a>
### Features

_Source: <https://onshape-public.github.io/docs/api-adv/featureaccess/>_

This page describes the APIs Onshape provides for creating and manipulating features and the Feature List in a Part Studio.

| PrerequisitesAll Onshape API calls must be properly authenticated.See the [API Keys](https://onshape-public.github.io/docs/api-adv/featureaccess/docs/auth/apikeys) page for instructions and the [Quick Start](https://onshape-public.github.io/docs/api-adv/featureaccess/docs/api-intro/quickstart) for an example.All applications submitted to the Onshape App Store _must_ authenticate with [OAuth2](https://onshape-public.github.io/docs/api-adv/featureaccess/docs/auth/oauth).For Standard accounts, replace {baseUrl} with cad in all endpoints. For Enterprise accounts, replace it with your company domain. Add /api and the version number, and then provide the endpoint.https://{baseUrl}.onshape.com/api/v10/documentshttps://cad.onshape.com/api/v10/documentshttps://companySubDomain.onshape.com/api/v10/documentsOnshape IDs are written as: {did}, {wvmid}, {eid}, {pid}, {otherId}.These represent document, workspace (or version or microversion), element, part, and other IDs, respectively.See [API Guide: API Intro](https://onshape-public.github.io/docs/api-adv/featureaccess/docs/api-intro/#onshape-api-request) for information on what these IDs mean and how to obtain them from your documents.Variables are written as: {variableId1} or <variableIdTwo>.These represent variables that must be replaced in the code before it is usable.Never include the braces {} or angle brackets <> with your IDs/variables.This page provides sample code in cURL and python.For additional instruction and video content, visit the Learning Center’s [Intro to the Onshape API](https://learn.onshape.com/learn/course/intro-to-the-onshape-api/intro-to-the-onshape-api/what-is-an-api?page=1) course. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

#### FeatureScript vs REST API

When working with complex geometry, you might find working directly in FeatureScript easier than working with the Onshape REST API.

* [FeatureScript Documentation](https://cad.onshape.com/FsDoc/)
* [FeatureScript API Guide](https://onshape-public.github.io/docs/api-adv/featureaccess/docs/api-adv/fs)

#### Endpoints

The following endpoints are available for working with features and the Feature List:

* [getPartStudioFeatures](https://cad.onshape.com/glassworks/explorer/#/PartStudio/getPartStudioFeatures)  
```  
curl -X 'GET' \  
  'https://cad.onshape.com/api/v9/partstudios/d/{did}/{wvm}/{wvmid}/e/{eid}/features?rollbackBarIndex=-1&includeGeometryIds=true&noSketchGeometry=false' \  
  -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS'  
```
* [addPartStudioFeature](https://cad.onshape.com/glassworks/explorer/#/PartStudio/addPartStudioFeature)  
```  
curl -X 'POST' \  
  'https://cad.onshape.com/api/v9/partstudios/d/{did}/{wvm}/{wvmid}/e/{eid}/features' \  
  -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
      "btType": "BTFeatureDefinitionCall-1406",  
      "feature": {  
        "btType": "BTMFeature-134",  
        "featureType": "",  
        "name": "",  
        "parameters": []  
      }  
    }'  
```
* [updatePartStudioFeature](https://cad.onshape.com/glassworks/explorer/#/PartStudio/updatePartStudioFeature)  
```  
  curl -X 'POST' \  
    'https://cad.onshape.com/api/v9/partstudios/d/{did}/w/{wid}/e/{eid}/features/featureid/{fid}' \  
    -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS' \  
    -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
    -d '{  
        "btType": "BTFeatureDefinitionCall-1406",  
        "feature": {  
          "btType": "BTMFeature-134",  
          "featureId": "{fid}",  
          "parameters": []  
        }  
      }'  
```
* [updateFeatures](https://cad.onshape.com/glassworks/explorer/#/PartStudio/updateFeatures)  
```  
  curl -X 'POST' \  
    'https://cad.onshape.com/api/v9/partstudios/d/{did}/w/{wid}/e/{eid}/features/updates' \  
    -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS' \  
    -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
    -d '{  
        "btType": "BTUpdateFeaturesCall-1748",  
        "features": [  
          {  
          "btType": "BTMFeature-134",  
          "featureId": "{fid1}",  
          "parameters": []  
          },  
          {  
          "btType": "BTMFeature-134",  
          "featureId": "{fid2}",  
          "parameters": []  
          }  
        ]  
      }'  
```
* [deletePartStudioFeature](https://cad.onshape.com/glassworks/explorer/#/PartStudio/deletePartStudioFeature)  
```  
curl -X 'DELETE' \  
  'https://cad.onshape.com/api/v9/partstudios/d/{did}/{wvm}/{wvmid}/e/{eid}/features/featureid/{fid}' \  
  -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS'  
```

##### JSON encoding

Instead of providing a translation layer between a feature’s internal and external formats, these APIs present the internal format of the feature definitions to the user. The best way to familiarize yourself with the formats involved is by calling the [Get the Feature List](https://cad.onshape.com/glassworks/explorer/#/PartStudio/getPartStudioFeatures) endpoint on existing Part Studios.

> 📘 **Notes**
> 
> * Onshape REST API parameters may change at any time. The documentation on this page is accurate for v9 of the Onshape API unless otherwise specified. The quickest way to verify what parameters are needed for a call is to create the sketch/feature in the Onshape UI, then call the [Get the Feature List](https://cad.onshape.com/glassworks/explorer/#/PartStudio/getPartStudioFeatures) API and see what parameters are returned for the feature.

> 📘 **Notes**
> 
> * Default values are sometimes omitted in the encoded output. These defaults are:  
>   * String: `""`  
>   * Boolean: `false`  
>   * Numeric: `0`
> * The JSON encoding uses a special tagging system to manage polymorphic data structures. Objects are generally by enclosing them within another object that declares the type information for the enclosed object.

##### Feature types

Below, find the available types for working with features in the API.

| Feature type   | Description               |
| -------------- | ------------------------- |
| BTMFeature-134 | General feature type      |
| BTMSketch-151  | Feature type for sketches |

##### Parameter types

All parameters have the following fields in common:

| Field       | Description                     |
| ----------- | ------------------------------- |
| parameterId | Unique ID of the parameter      |
| nodeId      | Unique ID of the parameter node |

The parameter types available for use in the API are:

| Parameter type                     | Field                                                                                                                                                                                                                                                                                                                                                                               | Description                         |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| BTMParameterQuantity-147           | expression                                                                                                                                                                                                                                                                                                                                                                          | Defines the value for the parameter |
| BTMParameterQueryList-148          | Defined by one of the following:                                                                                                                                                                                                                                                                                                                                                    |                                     |
| BTMIndividualQuery-138             | For POST requests, include only one of the following. If both are included, only deterministicIds will be used.deterministicIds \- List of deterministic IDs returned by the query; IDs should be obtained from the Part Studio, not hard-coded.queryString \- The actual query string; see [FeatureScript Query docs](https://cad.onshape.com/FsDoc/library.html#module-query.fs). |                                     |
| BTMIndividualSketchRegionQuery-140 | featureId \- Feature ID of the sketch for which to include all regions                                                                                                                                                                                                                                                                                                              |                                     |
| BTMParameterBoolean-144            | value                                                                                                                                                                                                                                                                                                                                                                               | true or false                       |
| BTMParameterEnum-145               |                                                                                                                                                                                                                                                                                                                                                                                     |                                     |
| enumName                           | Name of the enum type of which the value is a member                                                                                                                                                                                                                                                                                                                                |                                     |
| value                              | The enum member                                                                                                                                                                                                                                                                                                                                                                     |                                     |

#### Sample Workflows

Below are several examples of how the API can be used in order to help you get started. The calls could be executed using your preferred software environment but interactive use in a REST-aware tool is likely the easiest way to try the examples.

##### Get the list of features in a Part Studio

One of the best ways to familiarize yourself with the Onshape Feature APIs is to view the API details for existing features in a Part Studio. In this example, we’ll add three features to a Part Studio, and then call the [getPartStudioFeatures](https://cad.onshape.com/glassworks/explorer/#/PartStudio/getPartStudioFeatures) API on the Part Studio. We’ll then be able to view the structure of the way features are represented in the API.

1. Create a new document or open an existing one.
2. Create a new sketch in the document, and draw a long rectangle.
3. Extrude the rectangle.
4. Add a fillet to one edge of the part.
5. Call the [getPartStudioFeatures](https://cad.onshape.com/glassworks/explorer/#/PartStudio/getPartStudioFeatures) API. Replace the URL parameters with the values from your document, and replace `CREDENTIALS` with your authorization credentials.  
```  
curl -X 'GET \  
  'https://cad.onshape.com/api/v9/partstudios/d/{did}/{wvm}/{wvmid}/e/{eid}/features?rollbackBarIndex=-1&includeGeometryIds=true&noSketchGeometry=false' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09'  
```
6. Review the JSON returned in the response body. A lot of information is returned, but it will look something like the truncated snippet below. Notice that there are objects returned for each feature in the Part Studio– the sketch, the extrude, the fillet, and the chamfer. Each default plane and the origin in the Part Studio also appear in the `defaultFeatures` object. The Standard Geometry library is listed as an import, and the response also includes the state of each feature. :  
```  
{  
    "btType": "BTFeatureListResponse-2457",  
    "isComplete": true,  
    "serializationVersion": "1.2.4",  
    "rollbackIndex": 4,  
    "features": [  
      {  
        "btType": "BTMSketch-151",  
        "entities": [...],  
        "constraints": [...],  
        "name": "Sketch 1",  
        "suppressed": false,  
        "parameters": [...],  
        "featureId": "{fid1}",  
        "featureType": "newSketch",  
        "subFeatures": [...],  
        "returnAfterSubfeatures": false  
      },  
      {  
        "btType": "BTMFeature-134",  
        "name": "Extrude 1",  
        "suppressed": false,  
        "parameters": [...]  
        "featureId": "{fid2}",  
        "featureType": "extrude",  
        "subFeatures": [],  
        "returnAfterSubfeatures": false  
      },  
      {  
        "btType": "BTMFeature-134",  
        "name": "Fillet 1",  
        "suppressed": false,  
        "parameters": [...],  
        "featureId": "{fid3}",  
        "featureType": "fillet",  
        "subFeatures": [...],  
        "returnAfterSubfeatures": false  
      },  
      {  
        "btType": "BTMFeature-134",  
        "name": "Chamfer 1",  
        "suppressed": false,  
        "parameters": [...],  
        "featureId": "{fid4}",  
      }  
    ],  
    "featureStates": {  
      "{fid1}": {  
        "btType": "BTFeatureState-1688",  
        "featureStatus": "OK",  
        "inactive": false  
      },  
      ...  
    },  
    "defaultFeatures": [  
      {  
        "btType": "BTMFeature-134",  
        "name": "Origin",  
      },  
      {  
        "btType": "BTMFeature-134",  
        "name": "Top",  
      },  
      {  
        "btType": "BTMFeature-134",  
        "name": "Front",  
      },  
      {  
        "btType": "BTMFeature-134",  
        "name": "Right",  
      }  
    ],  
    "imports": [  
      {  
        "btType": "BTMImport-136",  
        "path": "onshape/std/geometry.fs",  
        "version": "2232.0"  
      }  
    ],  
    "libraryVersion": 2232  
  }  
```

##### Create a cube feature

In this example we will create a cube using the `cube` feature. The feature accepts a single parameter (the length of a side) and creates a cube with a corner at the origin and aligned with the three default planes.

1. Create a new document or open an existing one. We’ll create the cube feature in this document.
2. Begin to create the [addPartStudioFeature](https://cad.onshape.com/glassworks/explorer/#/PartStudio/addPartStudioFeature) call. Replace the URL parameters with the values from your document, and replace `CREDENTIALS` with your authorization credentials. This is a call to the same endpoint as in the previous example, but is a `POST` instead of a `GET`.  
```  
curl -X 'POST \  
  'https://cad.onshape.com/api/v9/partstudios/d/{did}/{wvm}/{wvmid}/e/{eid}/features' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09'\  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
          <JSON of feature data>  
      }'  
```
3. Add the following as the JSON body.  
   * Note the `btType` defines this as a Feature.  
   * We’ve named the feature `cube` and inserted an instance of the feature named `Cube 1` into the Part Studio.  
   * The `cube` feature has one parameter– the cube `sideLength` in inches, which is set to 1 by default.  
```  
{  
  "btType": "BTFeatureDefinitionCall-1406",  
  "feature": {  
    "btType": "BTMFeature-134",  
    "featureType": "cube",  
    "name": "Cube 1",  
    "parameters": [  
      {  
          "btType": "BTMParameterQuantity-147",  
          "isInteger": false,  
          "expression": "1 in",  
          "parameterId": "sideLength"  
        }  
    ],  
    "returnAfterSubfeatures": false,  
    "suppressed": false  
  }  
}  
```
4. Confirm your call matches the following, and then make the call:  
```  
curl -X 'POST \  
  'https://cad.onshape.com/api/v9/partstudios/d/{did}/{wvm}/{wvmid}/e/{eid}/features' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09'\  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
      "btType": "BTFeatureDefinitionCall-1406",  
      "feature": {  
        "btType": "BTMFeature-134",  
        "featureType": "cube",  
        "name": "Cube 1",  
        "parameters": [  
          {  
              "btType": "BTMParameterQuantity-147",  
              "isInteger": false,  
              "expression": "1 in",  
              "parameterId": "sideLength"  
            }  
        ],  
        "returnAfterSubfeatures": false,  
        "suppressed": false  
      }  
    }'  
```
5. Return to your console to review the endpoint response. The output returns:  
   * The feature definition that we provided as input with `nodeId`s and a `featureId`. Make a note of the `featureId`; we’ll use it in the next example.  
   * Information that the feature executed correctly  
   * The serialization version and microversion of the document that resulted from the feature addition  
```  
  {  
  "btType": "BTFeatureDefinitionResponse-1617",  
  "featureState": {  
    "btType": "BTFeatureState-1688",  
    "featureStatus": "OK",  
    "inactive": false  
  },  
  "feature": {  
    "btType": "BTMFeature-134",  
    "name": "Cube 1",  
    "suppressed": false,  
    "parameters": [  
      {  
        "btType": "BTMParameterQuantity-147",  
        "value": 0,  
        "units": "",  
        "isInteger": false,  
        "expression": "1 in",  
        "nodeId": "{nid1}",  
        "parameterId": "sideLength"  
      }  
    ],  
    "featureId": "{fid}",  
    "nodeId": "{nid2}",  
    "featureType": "cube",  
    "returnAfterSubfeatures": false,  
    "subFeatures": [],  
    "namespace": ""  
  },  
  "serializationVersion": "1.2.4",  
  "sourceMicroversion": "{mid}",  
  "microversionSkew": false,  
  "rejectMicroversionSkew": false,  
  "libraryVersion": 0  
}  
```
6. Open your document and confirm that the cube has been inserted into the Part Studio.  
![cube added to part studio via features api](https://onshape-public.github.io/docs/api-adv/featureaccess/images/features-cube-example.png)
7. Double-click `Cube 1` in the Feature List to open the Cube 1 dialog. Change the sideLength to 3 and click the checkbox. Note that the size of the cube changes automatically.  
![cube parameter updated to 3 inches](https://onshape-public.github.io/docs/api-adv/featureaccess/images/features-cube-example-02.png)

##### Update a feature

In this example we’ll update our cube feature.

1. Open the document in which you created the cube feature in [this example](#create-a-cube-feature). You will need the following from this document:  
   * Document ID  
   * Workspace ID  
   * Element ID (for the element that contains the cube feature)  
   * Feature ID (ID of the cube feature, returned in the API response in the previous example)  
         * If you need to get this `featureId` again, you can call the [getPartStudioFeatures](https://cad.onshape.com/glassworks/explorer/#/PartStudio/getPartStudioFeatures) endpoint on the document.
2. Begin to create the [updatePartStudioFeature](https://cad.onshape.com/glassworks/explorer/#/PartStudio/updatePartStudioFeature) call. Replace the URL parameters with the values from your document, and replace `CREDENTIALS` with your authorization credentials.  
```  
curl -X 'POST' \  
  'https://cad.onshape.com/api/v9/partstudios/d/{did}/w/{wid}/e/{eid}/features/featureid/{fid}' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
          <JSON of feature data>  
      }'  
```
3. Add the following as the JSON body.  
   * Note the `btType` defines this as a Feature.  
   * We specify the `featureId` again in the request body. This must match the `featureId` sent in the URL exactly.  
   * We must also specify the feature’s `featureType` and `name` in this call; if we don’t send those fields, the call will attempt to change these values to empty strings, resulting in errors.  
   * The `cube` feature has one parameter– the cube `sideLength` in inches, which we will update to 2 inches:  
```  
{  
  "btType": "BTFeatureDefinitionCall-1406",  
  "feature": {  
    "featureId": "{fid}",  
    "featureType": "cube",  
    "name": "Cube 1",  
    "parameters": [  
      {  
              "btType": "BTMParameterQuantity-147",  
              "isInteger": false,  
              "expression": "2 in",  
              "parameterId": "sideLength"  
            }  
    ]  
  }  
}  
```
4. Confirm your call matches the following, and then make the call:  
```  
    curl -X 'POST' \  
      'https://cad.onshape.com/api/v9/partstudios/d/{did}/w/{wid}/e/{eid}/features/featureid/{fid}' \  
      -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
      -H 'Authorization: Basic CREDENTIALS' \  
      -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
      -d '{  
      "btType": "BTFeatureDefinitionCall-1406",  
      "feature": {  
        "featureId": "{fid}",  
        "featureType": "cube",  
        "name": "Cube 1",  
        "parameters": [  
              {  
                "btType": "BTMParameterQuantity-147",  
                "isInteger": false,  
                "expression": "2 in",  
                "parameterId": "sideLength"  
              }  
          ]  
        }  
    }'  
```
5. Return to your console to review the endpoint response. The output returns:  
   * The updated feature definition  
   * Information that the feature executed correctly  
   * The serialization version and microversion of the document that resulted from the feature update  
```  
  {  
    "btType": "BTFeatureDefinitionResponse-1617",  
    "featureState": {  
      "btType": "BTFeatureState-1688",  
      "featureStatus": "OK",  
      "inactive": false  
    },  
    "feature": {  
      "btType": "BTMFeature-134",  
      "name": "Cube 1",  
      "suppressed": false,  
      "parameters": [  
        {  
          "btType": "BTMParameterQuantity-147",  
          "value": 0,  
          "units": "",  
          "isInteger": false,  
          "expression": "2 in",  
          "nodeId": "{nid1}",  
          "parameterId": "sideLength"  
        }  
      ],  
      "featureId": "{fid}",  
      "nodeId": "{nid2},  
      "featureType": "cube",  
      "returnAfterSubfeatures": false,  
      "subFeatures": [],  
      "namespace": ""  
    },  
    "serializationVersion": "1.2.4",  
    "sourceMicroversion": "{mid}",  
    "microversionSkew": false,  
    "rejectMicroversionSkew": false,  
    "libraryVersion": 0  
  }  
```
6. Open your document and confirm that the cube has a side length of 2 inches.  
![cube added to part studio via features api](https://onshape-public.github.io/docs/api-adv/featureaccess/images/features-cube-example-03.png)

##### Delete a feature

1. Create a new document and add a cube feature to it. See [Create a cube feature](#create-a-cube-feature) for instructions. Make a note of the following:  
   * Document ID  
   * Workspace ID  
   * Element ID (for the element containing the cube feature)
2. Call the [getPartStudioFeatures](https://cad.onshape.com/glassworks/explorer/#/PartStudio/getPartStudioFeatures) endpoint on the document to get the `featureId` of the cube feature. See [Get the Feature list](#get-the-list-of-features-in-a-part-studio) for instructions.
3. Create and execute the [deletePartStudioFeature](https://cad.onshape.com/glassworks/explorer/#/PartStudio/deletePartStudioFeature) call. Replace the URL parameters with the values from your document, and replace `CREDENTIALS` with your authorization credentials.  
```  
curl -X 'DELETE' \  
  'https://cad.onshape.com/api/v9/partstudios/d/{did}/w/{wid}/e/{eid}/features/featureid/{fid}' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS'  
```
4. Confirm that the cube feature has been removed from your document.

##### Create a sketch via queryString

In this example, we’ll create a circular sketch feature with the following properties:

* While other features use a `btType` of `BTMFeature-141`, sketches have their own special type: `BTMSketch-151`
* Sketches must use the `newSketch` featureType
* Sketch plane ID: Front
* Radius: 0.025 inches
* Location: (0.05, 0.05)
1. Open a new Part Studio. Note the following:  
   * Document ID  
   * Workspace ID  
   * Element ID (of the Part Studio tab)
2. We want to create the circle on the Front plane. Instead of getting the sketch plane ID explicitly, we’ll just specify the query string as `"query=qCreatedBy(makeId(\"Front\"), EntityType.FACE);"` in the `BTMIndividualQuery-138` parameter of our request payload. Let’s create the JSON structure for our sketch. **All sketches must be created with the `BTMSketch-151` btType and the `newSketch` featureType.** Make a note of how we’ve specified the geometry details.  
```  
{  
  "feature" : {  
    "btType": "BTMSketch-151",  
    "featureType": "newSketch",  
    "name": "Sketch 1",  
    "parameters": [  
      {  
        "btType": "BTMParameterQueryList-148",  
        "queries": [  
          {  
            "btType": "BTMIndividualQuery-138",  
            "queryString": "query=qCreatedBy(makeId(\"Front\"), EntityType.FACE);"  
          }  
        ],  
        "parameterId": "sketchPlane"  
      }  
    ],  
    "entities": [  
      {  
        "btType": "BTMSketchCurve-4",  
        "geometry": {  
          "btType": "BTCurveGeometryCircle-115",  
          "radius": 0.025,  
          "xCenter": 0.05,  
          "yCenter": 0.05,  
          "xDir": 1,  
          "yDir": 0,  
          "clockwise": false  
        },  
        "centerId": "circle-entity.center",  
        "entityId": "circle-entity"  
      }  
    ],  
    "constraints": [  
    ]  
  }  
}  
```
3. Now we’ll add the JSON to the [PartStudio/addPartStudioFeature](https://cad.onshape.com/glassworks/explorer/#/PartStudio/addPartStudioFeature) request. Replace the URL parameters with the values from your document, and replace `CREDENTIALS` with your authorization credentials.  
```  
curl -X 'POST' \  
  'https://cad.onshape.com/api/v9/partstudios/d/{did}/{wvm}/{wvmid}/e/{wid}/features' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
      "feature" : {  
        "btType": "BTMSketch-151",  
        "featureType": "newSketch",  
        "name": "Sketch 1",  
        "parameters": [  
          {  
            "btType": "BTMParameterQueryList-148",  
            "queries": [  
              {  
                "btType": "BTMIndividualQuery-138",  
                "queryString": "query=qCreatedBy(makeId(\"Front\"), EntityType.FACE);"  
              }  
            ],  
            "parameterId": "sketchPlane"  
          }  
        ],  
        "entities": [  
          {  
            "btType": "BTMSketchCurve-4",  
            "geometry": {  
              "btType": "BTCurveGeometryCircle-115",  
              "radius": 0.025,  
              "xCenter": 0.05,  
              "yCenter": 0.05,  
              "xDir": 1,  
              "yDir": 0,  
              "clockwise": false  
            },  
            "centerId": "circle-entity.center",  
            "entityId": "circle-entity"  
          }  
        ],  
        "constraints": [  
        ]  
      }  
    }'  
```
4. Note the new sketch’s `featureId` in the call response; you’ll need this for the [Create a cylinder](#create-a-cylinder) tutorial.
5. Open your Part Studio and confirm that the sketch has been added:  
    
![circle sketch created via features api](https://onshape-public.github.io/docs/api-adv/featureaccess/images/features-create-sketch.png)

##### Create a sketch via deterministicId

In this example, we’ll create a circular sketch feature with the following properties:

* While other features use a `btType` of `BTMFeature-141`, sketches have their own special type: `BTMSketch-151`
* Sketches must use the `newSketch` featureType
* Sketch plane ID: Front
* Radius: 0.025 inches
* Location: (0.05, 0.05)
1. Open a new PartStudio. Note the following:  
   * Document ID  
   * Workspace ID  
   * Element ID (of the Part Studio tab)
2. We want to create the circle on the Front plane, so we’ll call the [evalFeaturescript](https://cad.onshape.com/glassworks/explorer/#/PartStudio/evalFeatureScript) endpoint to get its ID. See [API Guide: Evaluating FeatureScript](https://onshape-public.github.io/docs/api-adv/featureaccess/docs/api-adv/fs#sketch-plane-ids) for more information.  
```  
curl -X 'POST' \  
  'https://cad.onshape.com/api/v9/partstudios/d/{did}/w/{wid}/e/{eid}/featurescript?rollbackBarIndex=-1' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
        "script": "function(context is Context, queries) { return transientQueriesToStrings(evaluateQuery(context, qCreatedBy(makeId(\"Front\"), EntityType.FACE))); }"  
}'  
```  
The call returns the following, identifying the plane as `JCC`.  
```  
{  
  "btType": "BTFeatureScriptEvalResponse-1859",  
  "result": {  
    "btType": "com.belmonttech.serialize.fsvalue.BTFSValueArray",  
    "value": [  
      {  
        "btType": "com.belmonttech.serialize.fsvalue.BTFSValueString",  
        "value": "JCC",  
        "typeTag": ""  
      }  
    ],  
    "typeTag": ""  
  }  
}  
```
3. Now we’ll create the JSON structure for our sketch. _All sketches must be created with the `BTMSketch-151` btType and the `newSketch` featureType._ Note how we’ve specified the plane to use in the `sketchPlane` parameter, and the `geometry` details.  
```  
{  
  "feature" : {  
    "btType": "BTMSketch-151",  
    "featureType": "newSketch",  
    "name": "Sketch 1",  
    "parameters": [  
      {  
        "btType": "BTMParameterQueryList-148",  
        "queries": [  
          {  
            "btType": "BTMIndividualQuery-138",  
            "deterministicIds": [ "JCC" ]  
          }  
        ],  
        "parameterId": "sketchPlane"  
      }  
    ],  
    "entities": [  
      {  
        "btType": "BTMSketchCurve-4",  
        "geometry": {  
          "btType": "BTCurveGeometryCircle-115",  
          "radius": 0.025,  
          "xCenter": 0.05,  
          "yCenter": 0.05,  
          "xDir": 1,  
          "yDir": 0,  
          "clockwise": false  
        },  
        "centerId": "circle-entity.center",  
        "entityId": "circle-entity"  
      }  
    ],  
    "constraints": [  
    ]  
  }  
}  
```
4. Now we’ll add the JSON structure to the [addPartStudioFeature](https://cad.onshape.com/glassworks/explorer/#/PartStudio/addPartStudioFeature) endpoint. Replace the URL parameters with the values from your document, and replace `CREDENTIALS` with your authorization credentials.  
```  
curl -X 'POST' \  
  'https://cad.onshape.com/api/v9/partstudios/d/{did}/{wvm}/{wvmid}/e/{eid}/features' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
      "feature" : {  
        "btType": "BTMSketch-151",  
        "featureType": "newSketch",  
        "name": "Sketch 1",  
        "parameters": [  
          {  
            "btType": "BTMParameterQueryList-148",  
            "queries": [  
              {  
                "btType": "BTMIndividualQuery-138",  
                "deterministicIds": [ "JCC" ]  
              }  
            ],  
            "parameterId": "sketchPlane"  
          }  
        ],  
        "entities": [  
          {  
            "btType": "BTMSketchCurve-4",  
            "geometry": {  
              "btType": "BTCurveGeometryCircle-115",  
              "radius": 0.025,  
              "xCenter": 0.05,  
              "yCenter": 0.05,  
              "xDir": 1,  
              "yDir": 0,  
              "clockwise": false  
            },  
            "centerId": "circle-entity.center",  
            "entityId": "circle-entity"  
          }  
        ],  
        "constraints": [  
        ]  
      }  
    }'  
```
5. Find the new sketch’s `featureId` in the call response. You’ll need this for the [Create a cylinder](#create-a-cylinder) tutorial.
6. Open your Part Studio and confirm that the sketch has been added:  
    
![circle sketch created via features api](https://onshape-public.github.io/docs/api-adv/featureaccess/images/features-create-sketch.png)

##### Create a cylinder

In this tutorial, we’ll extrude an sketch with the following properties:  
  
![Extrude dialog in Onshape UI](https://onshape-public.github.io/docs/api-adv/featureaccess/images/features-extrude-dialog.png)

1. This tutorial expands on the [Create a sketch](#create-a-sketch) tutorial. You’ll need the following from the document containing your circular sketch:  
   * Document ID  
   * Workspace ID  
   * Element ID of the tab containing the sketch  
   * Feature ID of the sketch  
         * If you need to get this `featureId` again, you can call the [getPartStudioFeatures](https://cad.onshape.com/glassworks/explorer/#/PartStudio/getPartStudioFeatures) endpoint on the document.
2. Begin to create the [addPartStudioFeature](https://cad.onshape.com/glassworks/explorer/#/PartStudio/addPartStudioFeature) call. Replace the URL parameters with the values from your document, and replace `CREDENTIALS` with your authorization credentials.  
```  
curl -X 'POST \  
  'https://cad.onshape.com/api/v9/partstudios/d/{did}/{wvm}/{wvmid}/e/{eid}/features' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09'\  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
          <JSON of feature data>  
      }'  
```
3. We’ll start by initializing an extrude in the JSON with the `btType` and `featureType` shown below:

```
  {
  "btType": "BTFeatureDefinitionCall-1406",
  "feature": 
    {
      "btType": "BTMFeature-134",
      "featureType": "extrude",
      "name": "Extrude 1",
      "suppressed": false,
      "parameters": [

      ]
    }
}

```

1. Now, we’ll add values for the options we want to our `parameters` block. Don’t forget to replace `{featureId}` in the code below with the feature ID of the sketch.

```
  {
    "btType": "BTMParameterEnum-145",
    "value": "SOLID",
    "enumName": "ExtendedToolBodyType",
    "parameterId": "bodyType"
  },
  {
    "btType": "BTMParameterEnum-145",
    "value": "NEW",
    "enumName": "NewBodyOperationType",
    "parameterId": "operationType"
  },
  {
    "btType": "BTMParameterQueryList-148",
    "queries": [
      {
        "btType": "BTMIndividualSketchRegionQuery-140",
        "featureId": "{featureId}"
      }
    ],
    "parameterId": "entities"
  },
  {
    "btType": "BTMParameterEnum-145",
    "value": "BLIND",
    "enumName": "BoundingType",
    "parameterId": "endBound"
  },
  {
    "btType": "BTMParameterQuantity-147",
    "expression": "1 in",
    "parameterId": "depth"
  }

```

1. Now our JSON is complete, and we can make our call.

```
  curl -X 'POST \
    'https://cad.onshape.com/api/v9/partstudios/d/{did}/{wvm}/{wvmid}/e/{eid}/features' \
    -H 'Authorization: Basic CREDENTIALS' \
    -H 'Accept: application/json;charset=UTF-8; qs=0.09'\
    -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \
    -d '{
          "btType": "BTFeatureDefinitionCall-1406",
          "feature": {
            "btType": "BTMFeature-134",
            "featureType": "extrude",
            "name": "Extrude 1",
            "parameters": [
              {
                "btType": "BTMParameterEnum-145",
                "value": "SOLID",
                "enumName": "ExtendedToolBodyType",
                "parameterId": "bodyType"
              },
              {
                "btType": "BTMParameterEnum-145",
                "value": "NEW",
                "enumName": "NewBodyOperationType",
                "parameterId": "operationType"
              },
              {
                "btType": "BTMParameterQueryList-148",
                "queries": [
                  {
                    "btType": "BTMIndividualSketchRegionQuery-140",
                    "featureId": "{featureId}"
                  }
                ],
                "parameterId": "entities"
              },
              {
                "btType": "BTMParameterEnum-145",
                "value": "BLIND",
                "enumName": "BoundingType",
                "parameterId": "endBound"
              },
              {
                "btType": "BTMParameterQuantity-147",
                "expression": "1 in",
                "parameterId": "depth"
              }
                ],
            "returnAfterSubfeatures": false,
            "suppressed": false
          }
        }'

```

1. Open your document and confirm that the sketch has been extruded into a cylinder.  
    
![circle sketch created via features api](https://onshape-public.github.io/docs/api-adv/featureaccess/images/features-extrude-example.png)

#### Additional Resources

* [API Guide: API Explorer](https://onshape-public.github.io/docs/api-adv/featureaccess/docs/api-intro/explorer)
* [API Guide: FeatureScript](https://onshape-public.github.io/docs/api-adv/featureaccess/docs/api-adv/fs)

---

<a id="pg-docs-api-adv-fs"></a>
### Evaluating FeatureScript

_Source: <https://onshape-public.github.io/docs/api-adv/fs/>_

This page describes some of the APIs Onshape provides for evaluating [FeatureScript](https://cad.onshape.com/FsDoc/).

| PrerequisitesAll Onshape API calls must be properly authenticated.See the [API Keys](https://onshape-public.github.io/docs/api-adv/fs/docs/auth/apikeys) page for instructions and the [Quick Start](https://onshape-public.github.io/docs/api-adv/fs/docs/api-intro/quickstart) for an example.All applications submitted to the Onshape App Store _must_ authenticate with [OAuth2](https://onshape-public.github.io/docs/api-adv/fs/docs/auth/oauth).For Standard accounts, replace {baseUrl} with cad in all endpoints. For Enterprise accounts, replace it with your company domain. Add /api and the version number, and then provide the endpoint.https://{baseUrl}.onshape.com/api/v10/documentshttps://cad.onshape.com/api/v10/documentshttps://companySubDomain.onshape.com/api/v10/documentsOnshape IDs are written as: {did}, {wvmid}, {eid}, {pid}, {otherId}.These represent document, workspace (or version or microversion), element, part, and other IDs, respectively.See [API Guide: API Intro](https://onshape-public.github.io/docs/api-adv/fs/docs/api-intro/#onshape-api-request) for information on what these IDs mean and how to obtain them from your documents.Variables are written as: {variableId1} or <variableIdTwo>.These represent variables that must be replaced in the code before it is usable.Never include the braces {} or angle brackets <> with your IDs/variables.This page provides sample code in cURL and python.For additional instruction and video content, visit the Learning Center’s [Intro to the Onshape API](https://learn.onshape.com/learn/course/intro-to-the-onshape-api/intro-to-the-onshape-api/what-is-an-api?page=1) course. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

#### FeatureScript vs REST API

When working with complex geometry, you might find working directly in FeatureScript easier than working with the Onshape REST API. [Click here to see the FeatureScript documentation.](https://cad.onshape.com/FsDoc/)

#### Endpoints

* [evalFeatureScript](https://cad.onshape.com/glassworks/explorer#/PartStudio/evalFeatureScript)  
```  
curl -X 'POST' \  
    'https://cad.onshape.com/api/v6/partstudios/d/{did}/w/{wid}/e/{eid}/featurescript?rollbackBarIndex=-1' \  
    -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS'\  
    -d '{  
            "libraryVersion": 2144,  
            "script": ""  
    }  
```

> **Important Note**
> 
> Only lambda expressions can be evaluated with this endpoint.

##### Sketch plane IDs

The following string can be sent along with the [featurescript](https://cad.onshape.com/glassworks/explorer/#/PartStudio/evalFeatureScript) API to get the plane ID. You can then use that ID to specify the plane on which to create a sketch.

```
function(context is Context, queries) { 
  return transientQueriesToStrings(evaluateQuery(context, qCreatedBy(makeId(\"{planeName}\"), EntityType.FACE))); 
}

```

For example, to get the ID of the Top plane, you would make the following call:

```
curl -X 'POST' \
  'https://cad.onshape.com/api/v8/partstudios/d/{did}/w/{wid}/e/{eid}/featurescript?rollbackBarIndex=-1' \
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \
  -H 'Authorization: Basic CREDENTIALS' \
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \
  -d '{
        "script": "function(context is Context, queries) { return transientQueriesToStrings(evaluateQuery(context, qCreatedBy(makeId(\"Top\"), EntityType.FACE))); }"
}'

```

#### Sample Workflows

##### Calculate a tight bounding box

Though the Onshape API offers a [getPartStudioBoundingBoxes](https://cad.onshape.com/glassworks/explorer/#/PartStudio/getPartStudioBoundingBoxes) endpoint, it does not result in a tight bounding box. The values returned are meant for graphics and visualization, and are approximate. To calculate a more accurate bounding box, we’ll use the [evalFeatureScript](https://cad.onshape.com/glassworks/explorer#/PartStudio/evalFeatureScript) endpoint.

1. Call the [evalFeatureScript](https://cad.onshape.com/glassworks/explorer#/PartStudio/evalFeatureScript). Replace the URL parameters with the IDs from the Part Studio you’re working with, and replace `CREDENTIALS` with your authorization credentials. The endpoint will return a tight bounding box in the response.  
```  
    curl -X 'POST' \  
    'https://cad.onshape.com/api/v6/partstudios/d/{did}/w/{wid}/e/{eid}/featurescript?rollbackBarIndex=-1' \  
    -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS'\  
    -d '{ "libraryVersion": 2144,  
        "script": "function(context is Context, definition is map) {const boundingBoxTight = evBox3d(context, { \n \"topology\" :  qConstructionFilter(qEverything(), ConstructionObject.NO),\n \"tight\" : true\n}); \n return (boundingBoxTight);}"  
        }'  
```

##### Create a sketch

See [API Guide: Features](https://onshape-public.github.io/docs/api-adv/fs/docs/api-adv/featureaccess#create-a-sketch) for the `Create a sketch` tutorial.

#### Additional Resources

* [FeatureScript](https://cad.onshape.com/FsDoc/)
* [API Explorer: Part Studio](https://cad.onshape.com/glassworks/explorer/#/PartStudio)
* [API Guide: API Explorer](https://onshape-public.github.io/docs/api-adv/fs/docs/api-intro/explorer)

---

<a id="pg-docs-api-adv-metadata"></a>
### Metadata

_Source: <https://onshape-public.github.io/docs/api-adv/metadata/>_

This page describes the APIs Onshape provides for working with metadata.

| PrerequisitesAll Onshape API calls must be properly authenticated.See the [API Keys](https://onshape-public.github.io/docs/api-adv/metadata/docs/auth/apikeys) page for instructions and the [Quick Start](https://onshape-public.github.io/docs/api-adv/metadata/docs/api-intro/quickstart) for an example.All applications submitted to the Onshape App Store _must_ authenticate with [OAuth2](https://onshape-public.github.io/docs/api-adv/metadata/docs/auth/oauth).For Standard accounts, replace {baseUrl} with cad in all endpoints. For Enterprise accounts, replace it with your company domain. Add /api and the version number, and then provide the endpoint.https://{baseUrl}.onshape.com/api/v10/documentshttps://cad.onshape.com/api/v10/documentshttps://companySubDomain.onshape.com/api/v10/documentsOnshape IDs are written as: {did}, {wvmid}, {eid}, {pid}, {otherId}.These represent document, workspace (or version or microversion), element, part, and other IDs, respectively.See [API Guide: API Intro](https://onshape-public.github.io/docs/api-adv/metadata/docs/api-intro/#onshape-api-request) for information on what these IDs mean and how to obtain them from your documents.Variables are written as: {variableId1} or <variableIdTwo>.These represent variables that must be replaced in the code before it is usable.Never include the braces {} or angle brackets <> with your IDs/variables.This page provides sample code in cURL and python.For additional instruction and video content, visit the Learning Center’s [Intro to the Onshape API](https://learn.onshape.com/learn/course/intro-to-the-onshape-api/intro-to-the-onshape-api/what-is-an-api?page=1) course. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

#### Updating Metadata

To update metadata, you send a JSON in the API request body in the following general format:

`{
  "properties": [
    {
      "value": "", // new value for the property
      "propertyId": "{propertyId}" // ID of the property
    }
  ]
}
`

#### Examples

---

##### Update a part property

Update a part’s description by getting the current metadata for the part and then posting an update to that metadata.

**Endpoint**

[POST v10/metadata/d/{did}/w/{wid}/e/{eid}/p/{pid}](https://cad.onshape.com/glassworks/explorer/#/Metadata/getWMVEPMetadata)

**Request Body**

`{
  "jsonType": "metadata-part",
  "partId": "{pid}",
  "properties": [
    {
      "value": "",
      "propertyId": "{propertyId}"
    }
  ]
}
`

_Additional optional fields available. See the [API Explorer](https://cad.onshape.com/glassworks/explorer/#/Metadata/getWMVEPMetadata) for a full list._

**Example**

1. Make a copy of [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/958bceb5a2511b572dbbe851). Make a note of the _new_ document’s document ID, workspace ID, and element ID.
2. Get the ID of the part to update. Call the [getPartsWMVE](https://cad.onshape.com/glassworks/explorer/#/Part/getPartsWMVE) endpoint on your document to get a list of part IDs in the element. Only one part exists in the document, with a part ID of `JHD`.  
`{  
  "name": "Main",  
  // ...  
  "microversionId": "{mid}",  
  "partNumber": null,  
  "elementId": "{eid}",  
  "partId": "JHD",  
  "bodyType": "sheet",  
  // ...  
}  
`
3. Now, get the metadata of the part by calling the [getWMVEPMetadata](https://cad.onshape.com/glassworks/explorer/#/Metadata/getWMVEPMetadata) endpoint to get the current metadata JSON for the part.  
   * cURL  
   * python  
`  curl -X 'GET' \  
    'https://{baseUrl}.onshape.com/api/v10/metadata/d/{did}/w/{wid}/e/{eid}/p/JHD' \  
    -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS' \  
    -H 'Content-Type: application/json;charset=UTF-8; qs=0.09'  
`  
`import requests  
import json  
auth = (access_key, secret_key) # See Authentication guide  
headers = {  
  'Accept': 'application/json;charset=UTF-8;qs=0.09',  
  'Content-Type': 'application/json;charset=UTF-8; qs=0.09'  
}  
api_url = "https://{baseUrl}.onshape.com/api/v10/metadata/d/{did}/w/{wid}/e/{eid}/p/JHD"  
queryParams = {}  
response = requests.get(  api_url,  
                          params=queryParams,  
                          auth=auth,  
                          headers=headers )  
print(json.dumps(response.json(), indent=4))  
`
4. Locate the property to update in the response. Scroll to the `Description` properties block of the JSON response, and notice that the `value` field is an empty string.  
`{  
  "name": "Description",  
  "value": "",  
  "defaultValue": null,  
  "computedPropertyError": null,  
  "propertySource": 3,  
  "validator": { },  
  "required": false,  
  "editable": true,  
  "propertyId": "{propertyId}",  
  "editableInUi": true,  
  "dateFormat": null,  
  "valueType": "STRING",  
  "enumValues": null,  
  "multivalued": false,  
  "computedAssemblyProperty": false,  
  "computedProperty": false,  
  "propertyOverrideStatus": 0  
}  
`
5. Find the metadata’s property ID; in this example, we want the `propertyId` for the `Description` property. We’ll need this ID to update the metadata.
6. Make the [updateWVEPMetadata](https://cad.onshape.com/glassworks/explorer/#/Metadata/updateWVEPMetadata) call. Replace the `{propertyId}` value with the ID from the last step.  
   * cURL  
   * python  
`  curl -X 'POST' \  
  'https://cad.onshape.com/api/v10/metadata/d/{did}/w/{wid}/e/{eid}/p/JHD' \  
    -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS' \  
    -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
    -d '{  
        "jsonType": "metadata-part",  
        "partId": "JHD",  
        "properties": [  
          {  
            "value": "Drill bit",  
            "propertyId": "{propertyId}"  
          }  
        ]  
        }'  
`  
`import requests  
import json  
auth = (access_key, secret_key) # See Authentication guide  
headers = {  
  'Accept': 'application/json;charset=UTF-8;qs=0.09',  
  'Content-Type': 'application/json;charset=UTF-8; qs=0.09'  
}  
api_url = "https://{baseUrl}.onshape.com/api/v10/metadata/d/{did}/w/{wid}/e/{eid}/p/JHD"  
queryParams = {}  
body = {  
  "jsonType": "metadata-part",  
  "partId": "JHD",  
  "properties": [  
    {  
    "value": "Drill bit",  
    "propertyId": "{propertyId}"  
    }  
  ]  
}  
response = requests.post( api_url,  
                          params=queryParams,  
                          json=body,  
                          auth=auth,  
                          headers=headers )  
print(json.dumps(response.json(), indent=4))  
`
7. Repeat steps 3 and 4 to confirm that the Description `value` for the part is now `Drill bit`.

---

##### Update a part number

**Endpoint**

[POST v14/metadata/d/{did}/{wvm}/{wvmid}/e/{eid}/{iden}/{pid}](https://cad.onshape.com/glassworks/explorer/#/Metadata/updateWVEPMetadata)

**Request Body**

`{
  "jsonType": "metadata-part",
  "partId": <pid>,
  "properties": [
    {
      "value": <newPartNumber>,
      "propertyId": <propertyId>
    }
  ]
}
`

_Additional optional fields available. See the [API Explorer](https://cad.onshape.com/glassworks/explorer/#/Metadata/updateWVEPMetadata) for a full list._

**Example**

1. `pid` and `partId` \- Get the part ID to update:  
   * Call [getPartsWMV](https://cad.onshape.com/glassworks/explorer/#/Part/getPartsWMV) or [getPartsWMVE](https://cad.onshape.com/glassworks/explorer/#/Part/getPartsWMVE)  
   * Response field - `partId`
2. `value` \- Get the new part number:  
   * Call [nextNumbers](https://cad.onshape.com/glassworks/explorer/#/NumberingScheme/nextNumbers)  
   * Response field - `partNumber`  
   * See [Get the available next part number](https://onshape-public.github.io/docs/api-adv/metadata/docs/api-adv/relmgmt#get-the-next-available-part-number) for instructions.  
   * For this example, we’ll use `PRT-002` as the value.
3. `propertyId` \- Get the ID of the part number property:  
   * Call [getWMVEPMetadata](https://cad.onshape.com/glassworks/explorer/#/Metadata/getWMVEPMetadata)  
   * Response field - `properties.propertyId` where `property.name="Part number"`
4. Call the update endpoint:  
   * cURL  
   * python  
`  curl -X 'POST' \  
  'https://cad.onshape.com/api/v14/metadata/d/{did}/w/{wid}/e/{eid}/p/{pid}' \  
    -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS' \  
    -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
    -d '{  
          "jsonType": "metadata-part",  
          "partId": "{pid}",  
          "properties": [  
            {  
              "value": "PRT-002",  
              "propertyId": "{propertyId}"  
            }  
          ]  
        }'  
`  
`import requests  
import json  
auth = (access_key, secret_key) # See Authentication guide  
headers = {  
  'Accept': 'application/json;charset=UTF-8;qs=0.09',  
  'Content-Type': 'application/json;charset=UTF-8; qs=0.09'  
}  
api_url = "https://{baseUrl}.onshape.com/api/v14/metadata/d/{did}/w/{wid}/e/{eid}/p/{pid}"  
queryParams = {}  
body = {  
  "jsonType": "metadata-part",  
  "partId": "{pid}",  
  "properties": [  
    {  
    "value": "PRT-002",  
    "propertyId": "{propertyId}"  
    }  
  ]  
}  
response = requests.post( api_url,  
                          params=queryParams,  
                          json=body,  
                          auth=auth,  
                          headers=headers )  
print(json.dumps(response.json(), indent=4))  
`
5. Repeat Step 3 to confirm that `properties.value` is now `PRT-002` where `properties.name="Part number"`.

---

##### Update a tab name

In this example we will update an element’s tab name by getting the current metadata for the element, and then posting an update to that metadata. Remember that in Onshape, an element is typically represented as a tab in the Onshape UI.

**Endpoint**

[POST api/v10/metadata/d/{did}/w/{wid}/e/{eid}](https://cad.onshape.com/glassworks/explorer/#/Metadata/updateWVEMetadata)

**Request Body**

`{
  "properties": [
    {
      "value": "",
      "propertyId": "{propertyId}"
    }
  ]
}
`

1. Make a copy of [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/4561b91a53c595c0010d5cdb). Make a note of the new document’s document ID, workspace ID, and element ID. Note the tab name of the element is “NEW\_PART”.  
    
![Onshape document with NEW_PART tab name](https://onshape-public.github.io/docs/api-adv/metadata/images/metadata-update-tab-before.png)
2. To get the current metadata of the element, call the [getWMVEMetadata](https://cad.onshape.com/glassworks/explorer/#/Metadata/getWMVEMetadata) endpoint to get the current metadata JSON for the element. Don’t forget to replace the URL parameters with the IDs from your new document, and replace `CREDENTIALS` with your authorization credentials.  
   * cURL  
   * python  
`curl -X 'GET' \  
    'https://cad.onshape.com/api/v10/metadata/d/{did}/w/{wid}/e/{eid}' \  
    -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS' \  
    -H 'Content-Type: application/json;charset=UTF-8; qs=0.09'  
`  
`import requests  
import json  
auth = (access_key, secret_key) # See Authentication guide  
headers = {  
  'Accept': 'application/json;charset=UTF-8;qs=0.09',  
  'Content-Type': 'application/json;charset=UTF-8; qs=0.09'  
}  
api_url = "https://{baseUrl}.onshape.com/api/v10/metadata/d/{did}/w/{wid}/e/{eid}"  
queryParams = {}  
response = requests.get(  api_url,  
                          params=queryParams,  
                          auth=auth,  
                          headers=headers )  
print(json.dumps(response.json(), indent=4))  
`
3. The call returns a response body in JSON format. Scroll to the `Name` properties block of the JSON response, and notice that the `value` field matches our current tab name, “NEW\_PART”.  
`{  
  "jsonType": "metadata-element",  
  "elementType": 0,  
  "mimeType": "onshape/partstudio",  
  "elementId": "{eid}",  
  "properties": [  
    {  
      "name": "Name",  
      "value": "NEW_PART",  
      "validator": {},  
      "required": true,  
      "editable": true,  
      "propertyId": "{propertyId}",  
      // ..  
    }, // ...  
  ], // ...  
}  
`
4. Copy the Name block’s `propertyId` in the response. We’ll need this ID to update the metadata.
5. Set up the [updateWVEMetadata](https://cad.onshape.com/glassworks/explorer/#/Metadata/updateWVEMetadata) call.  
Note that we need to include the `propertyId` and the value to update. In the request JSON, replace `{propertyId}` with the property ID you found in the last step, then change the empty `value` string to `"PISTON"`:  
   * cURL  
   * python  
`curl -X 'POST' \  
'https://cad.onshape.com/api/v10/metadata/d/{did}/w/{wid}/e/{eid}' \  
    -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS' \  
    -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
    -d '{  
        "properties": [  
            {  
                "value": "PISTON",  
                "propertyId": "{propertyId}"  
            }  
            ]  
        }'  
`  
`import requests  
import json  
auth = (access_key, secret_key) # See Authentication guide  
headers = {  
  'Accept': 'application/json;charset=UTF-8;qs=0.09',  
  'Content-Type': 'application/json;charset=UTF-8; qs=0.09'  
}  
api_url = "https://{baseUrl}.onshape.com/api/v10/metadata/d/{did}/w/{wid}/e/{eid}"  
queryParams = {}  
body = {  
  "properties": [  
      {  
          "value": "PISTON",  
          "propertyId": "{propertyId}"  
      }  
      ]  
  }  
response = requests.post( api_url,  
                          params=queryParams,  
                          json=body,  
                          auth=auth,  
                          headers=headers )  
print(json.dumps(response.json(), indent=4))  
`
6. Open your document and confirm that the tab name is now `PISTON`.  
    
![Onshape document with NEW_PART tab name](https://onshape-public.github.io/docs/api-adv/metadata/images/metadata-update-tab-after.png)

---

##### Update standard content part metadata

| Standard Content Notes{linkedDocumentId}: ID of the document into which the standard content part is inserted.You can call [getAssemblyDefinition](https://cad.onshape.com/glassworks/explorer/#/Assembly/getAssemblyDefinition) to get the other values needed for the call:{did}, {vid}, {eid}: IDs of the document, version, and element in which the standard content part lives.{companyId}: ID of the company that owns the standard content part. All metadata changes to this standard content part will populate for the entire company.{pid}: Part ID of the standard content part.{config}: Encoded configuration string.For each items.properties object, include a unique propertyId and at least one key/value metadata pair.Updates made to standard content are global for all users and documents within the company. |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

**Endpoint**

[POST api/v12/metadata/standardcontent/d/{did}](https://cad.onshape.com/glassworks/explorer/#/Metadata/updateVEOPStandardContentPartMetadata)

**Request Body**

`{
  "items": [
    {
    "href": "https://{baseUrl}.onshape.com/api/v10/metadata/standardcontent/d/{did}/v/{vid}/e/{eid}/c/{companyId}/p/{pid}?configuration={config}&linkDocumentId={linkDocumentId}&applyToAllConfigs=false",
    "properties": [
      { 
        "value": "", 
        "propertyId": "{propertyId1}" 
      },
      { 
        "value": "", 
        "propertyId": "{propertyId2}" 
      }
    ]
    }
  ]
}
`

#### Additional Resources

* [API Explorer: Metadata](https://cad.onshape.com/glassworks/explorer/#/Metadata)
* [API Guide: API Explorer](https://onshape-public.github.io/docs/api-adv/metadata/docs/api-intro/explorer)

---

<a id="pg-docs-api-adv-relmgmt"></a>
### Release Management

_Source: <https://onshape-public.github.io/docs/api-adv/relmgmt/>_

This page describes the APIs Onshape provides for viewing revisions and for creating, submitting, approving, and publishing releases.

| PrerequisitesAll Onshape API calls must be properly authenticated.See the [API Keys](https://onshape-public.github.io/docs/api-adv/relmgmt/docs/auth/apikeys) page for instructions and the [Quick Start](https://onshape-public.github.io/docs/api-adv/relmgmt/docs/api-intro/quickstart) for an example.All applications submitted to the Onshape App Store _must_ authenticate with [OAuth2](https://onshape-public.github.io/docs/api-adv/relmgmt/docs/auth/oauth).For Standard accounts, replace {baseUrl} with cad in all endpoints. For Enterprise accounts, replace it with your company domain. Add /api and the version number, and then provide the endpoint.https://{baseUrl}.onshape.com/api/v10/documentshttps://cad.onshape.com/api/v10/documentshttps://companySubDomain.onshape.com/api/v10/documentsOnshape IDs are written as: {did}, {wvmid}, {eid}, {pid}, {otherId}.These represent document, workspace (or version or microversion), element, part, and other IDs, respectively.See [API Guide: API Intro](https://onshape-public.github.io/docs/api-adv/relmgmt/docs/api-intro/#onshape-api-request) for information on what these IDs mean and how to obtain them from your documents.Variables are written as: {variableId1} or <variableIdTwo>.These represent variables that must be replaced in the code before it is usable.Never include the braces {} or angle brackets <> with your IDs/variables.This page provides sample code in cURL and python.For additional instruction and video content, visit the Learning Center’s [Intro to the Onshape API](https://learn.onshape.com/learn/course/intro-to-the-onshape-api/intro-to-the-onshape-api/what-is-an-api?page=1) course. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

#### Custom Workflows

Enterprise administrators can create customized release and obsoletion workflows. See the following Onshape Help article on designing release management processes for your Enterprise: **[Designing Release Management Processes](https://cad.onshape.com/help/Content/relmgmt%5Fcustom.htm)**.

#### Examples

> Note:
> 
> Workflow IDs and property IDs are stable across your company or enterprise. You only need to `GET` these IDs once.

---

##### Create a release candidate

Create a release candidate and add items to the release in the `items` array. This example creates a release candidate with one part. Items can also be added to the release later with the [updateRelease](#add-items-to-a-release-candidate) endpoint.

> Notes:
> 
> * The response includes an `id`; this is your release candidate package ID (`rpid`).  
>   * This ID cannot easily be obtained later from a different endpoint, so store it securely.  
>   * This ID can be obtained later from the Onshape UI: [Review the release candidate](https://cad.onshape.com/help/Content/Release/reviewing%5Fapproving%5Frejecting%5Fcandidates.htm#Review) in the UI and click the **Copy link** icon. The release ID is included at the end of the copied URL.
> * To add items from other documents, you must select `Allow adding items from other documents` in your [Release Management settings](https://cad.onshape.com/help/Content/Plans/release%5Fmanagement%5F2.htm#rel%5Fcandidate%5Fdialog).

**Endpoint**

`createReleasePackage` \- [POST /releasepackages/release/{wfid}](https://cad.onshape.com/glassworks/explorer/#/ReleasePackage/createReleasePackage)

**Parameters**

* `wfid` \- Workflow ID  
   * Call [getActiveWorkflows](https://cad.onshape.com/glassworks/explorer/#/Workflow/getActiveWorkflows)  
         * This endpoint takes `documentId` and not the usual `did`.  
   * Response field - `releaseWorkflow.id`  
         * The default `releaseWorkflow.name` is `"Onshape default release workflow"`.  
         * To use a custom workflow, find the `releaseWorkflow.id` field for the `releaseWorkflow.name` to use.

**Request Body**

`{
  "items": [
    {
      "documentId": <did>,
      "elementId": <eid>,
      "partId": <partId>,
      "versionId": <vid>
    }
  ]
}
`

**Example**

1. `wfid` \- Get ID of the workflow to use for the release.  
   * Call [getActiveWorkflows](https://cad.onshape.com/glassworks/explorer/#/Workflow/getActiveWorkflows)  
         * This endpoint takes `documentId` and not the usual `did`.  
   * Response field - `releaseWorkflow.id`
2. Create a document with one Part Studio that contains at least one part:  
   * `did` \- Document ID  
   * `eid` \- Element ID of the Part Studio
3. `partId` \- Get the ID of Part 1:  
   * Call [getPartsWMVE](https://cad.onshape.com/glassworks/explorer/#/Part/getPartsWMVE)  
   * Response field - `partId`
4. `vid` \- Create a version in the document.  
   * Call [createVersion](https://cad.onshape.com/glassworks/explorer/#/Document/createVersion).  
   * Provide the document `documentId` and `workspaceId` in the request body.  
   * Provide a `name` for the version in the request body.
5. Create the release candidate:  
```curl  
curl -X 'POST' \  
'https://cad.onshape.com/api/v14/releasepackages/release/{wfid}?debugMode=false' \  
-H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
-H 'Authorization: Basic CREDENTIALS' \  
-H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
-d '{  
  "items": [  
    {  
      "documentId": "{did}",  
      "elementId": "{eid}",  
      "partId": "{partId}",  
      "versionId": "{vid}"  
    }  
  ]  
}'  
```
6. `rpid` \- The release candidate is created, and contains only the first part from the Part Studio. Find the `id` at the end of the response. This is the release ID.

---

##### Add items to a release candidate

This example adds items to an existing release candidate.

**Endpoint**

`updateReleasePackage` \- [POST /releasepackages/{rpid}](https://cad.onshape.com/glassworks/explorer/#/ReleasePackage/updateReleasePackage)

**Parameters**

* `rpid` \- ID of the release candidate to update
* `action` \- `"ADD_ITEMS"`

**Request Body**

`{
  "items": [
    {
      "documentId": <did>,
      "elementId": <eid>,
      "partId": <partIdTwo>,
      "versionId": <vid>
    },
    {
      "documentId": <did>,
      "elementId": <eid>,
      "partId": <partIdThree>,
      "versionId": <vid>
    }
  ]
}
`

**Example**

1. Complete the [Create a release candidate](#create-a-release-candidate) example before this one.
* `rpid` \- ID of the release candidate to update.
* `did`, `vid`, and `eid` \- Document, version, and element that contain the parts to add.
1. Add two parts to the document.
2. `partId` \- Get the IDs of the two new parts:  
   * Call [getPartsWMVE](https://cad.onshape.com/glassworks/explorer/#/Part/getPartsWMVE)  
   * Response field - `partId` for the new parts.
3. Call the `updateReleasePackage` endpoint:  
```curl  
curl -X 'POST' \  
'https://cad.onshape.com/api/v14/releasepackages/{rpid}?action=ADD_ITEMS' \  
-H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
-H 'Authorization: Basic CREDENTIALS' \  
-H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
-d '{  
  "items": [  
    {  
      "documentId": "{did}",  
      "elementId": "{eid}",  
      "partId": "{partIdTwo}",  
      "versionId": "{vid}"  
    },  
    {  
      "documentId": "{did}",  
      "elementId": "{eid}",  
      "partId": "{partIdThree}",  
      "versionId": "{vid}"  
    }  
  ]  
}'  
```
4. The response indicates that all three parts are now in the release candidate.

---

##### View release candidate details

View release candidate properties and all existing items included in the release.

**Endpoint**

`getReleasePackage` \- [GET /releasepackages/{rpid}](https://cad.onshape.com/glassworks/explorer/#/ReleasePackage/getReleasePackage)

**Parameters**

* `rpid` \- ID of the release candidate to update
* `detailed` \- `true | false`

**Example**

1. `rpid` \- ID of the release candidate to update. Complete the [Create a release candidate](#create-a-release-candidate) example before this one.
2. Call the `getReleasePackage` endpoint:  
```curl  
curl -X 'GET' \  
  'https://{baseUrl}.onshape.com/api/v14/releasepackages/{rpid}?detailed=false' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS'  
```
3. In the response, find the `items` array. Each item included in the release appears in the array and includes an `items.id` and an array of `items.properties`.
4. Find the `workflow.state.name` field. This is the current state of the release.
5. Find the `workflow` object and make a note of each available `workflow.actions.action`. These are your available `wfaction` strings that can be used to transition the workflow to a different state. You’ll need these if you want to submit or release the candidate later.

---

##### Remove items from a release candidate

This example removes parts from an existing release candidate. See [View release candidate details](#view-release-candidate-details) to obtain a list of item IDs that can be removed.

**Endpoint**

`updateReleasePackage` \- [POST /releasepackages/{rpid}](https://cad.onshape.com/glassworks/explorer/#/ReleasePackage/updateReleasePackage)

**Parameters**

* `rpid` \- ID of the release candidate to update
* `action` \- `"REMOVE_ITEMS"`

**Request Body**

`{
  "itemIds": [ <itemIdTwo>, <itemIdThree> ]
}
`

**Example**

1. `rpid` \- ID of the release candidate to update. Complete the [Create a release candidate](#create-a-release-candidate) example to get this id.
2. `itemIds` \- The items to remove  
   * Complete the [Add items to a release candidate](#add-items-to-a-release-candidate) to add the items we’ll now remove.  
   * Complete the [View release candidate details](#view-release-candidate-details) to get the IDs of items to remove. There should be three items total. We will remove the two we just added, leaving only the original item in the release.
3. Call the `updateReleasePackage` endpoint:  
```curl  
  curl -X 'POST' \  
  'https://{baseUrl}.onshape.com/api/v14/releasepackages/{rpid}?action=REMOVE_ITEMS' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
    "itemIds": [ "{itemIdTwo}", "{itemIdThree}" ]  
  }'  
```
4. Repeat the [View release candidate details](#view-release-candidate-details) example to confirm that only one part is left in the release candidate.

---

##### Get all revisions

The following endpoints all return revision information for the specified items:

| Item        | Endpoint                                | Path                                                                                                                                                        |
| ----------- | --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Company     | enumerateRevisions                      | [GET /revisions/companies/{cid}](https://cad.onshape.com/glassworks/explorer/#/Revision/enumerateRevisions)                                                 |
| Document    | getAllInDocument                        | [GET /revisions/d/{did}](https://cad.onshape.com/glassworks/explorer/#/Revision/getAllInDocument)                                                           |
| Version     | getAllInDocumentVersion                 | [GET /revisions/d/{did}/v/{vid}](https://cad.onshape.com/glassworks/explorer/#/Revision/getAllInDocumentVersion)                                            |
| Element     | getRevisionHistoryInCompanyByElementId  | [GET /revisions/companies/{cid}/d/{did}/{wv}/{wvid}/e/{eid}](https://cad.onshape.com/glassworks/explorer/#/Revision/getRevisionHistoryInCompanyByElementId) |
| Part number | getRevisionHistoryInCompanyByPartNumber | [GET /revisions/companies/{cid}/partnumber/{pnum}](https://cad.onshape.com/glassworks/explorer/#/Revision/getRevisionHistoryInCompanyByPartNumber)          |
| Part ID     | getRevisionHistoryInCompanyByPartId     | [GET /revisions/companies/{cid}/d/{did}/e/{eid}/p/{pid}](https://cad.onshape.com/glassworks/explorer/#/Revision/getRevisionHistoryInCompanyByPartId)        |

**Parameters**

* `elementType` or `et`: Element type  
   * See the [API Explorer](https://cad.onshape.com/glassworks/explorer/#/PartNumber) for a full list for allowed values and additional parameter options.  
   * View instructions on locating the request body docs in the API Explorer: [View request body docs](https://onshape-public.github.io/docs/api-adv/relmgmt/docs/api-intro/explorer#view-request-body-docs) as needed.

**Example**

1. `cid` \- Company ID  
   * Call [findCompany](https://cad.onshape.com/glassworks/explorer/#/Company/findCompany)  
   * Response field - `id` (NOT `address.id` or `ownerId`)
2. `pnum` \- The part number to get revision info for  
   * Call [getPartsWMVE](https://cad.onshape.com/glassworks/explorer/#/Part/getPartsWMVE)  
   * Response field - `partNumber`
3. `elementType` \- Element type  
   * View the [getLatestInDocumentOrCompany](https://cad.onshape.com/glassworks/explorer/#/Revision/getLatestInDocumentOrCompany) endpoint parameters to see available options.  
   * In this example, we’ll use `elementType=0` to indicate the part is in a Part Studio.
4. Call the [getRevisionByPartNumber](https://cad.onshape.com/glassworks/explorer/#/Revision/getRevisionByPartNumber) endpoint:  
   * cURL  
   * python  
`curl -X 'POST' \  
  'https://{baseUrl}.onshape.com/api/v14/revisions/c/{cid}/partnumber/{pnum}/?elementType=0' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic {credentials}' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09'  
`  
`import requests  
import json  
auth = (access_key, secret_key) # See Authentication guide  
headers = {  
  'Accept': 'application/json;charset=UTF-8;qs=0.09',  
  'Content-Type': 'application/json;charset=UTF-8; qs=0.09'  
}  
api_url = "https://{baseUrl}.onshape.com/api/v14/revisions/c/{cid}/partnumber/{pnum}/"  
queryParams = {  
  "elementType": 0  
}  
response = requests.get( api_url,  
                          params=queryParams,  
                          auth=auth,  
                          headers=headers )  
print(json.dumps(response.json(), indent=4))  
`
5. Review the response, which includes information for each revision. Each item in the list includes the `releaseName` and `revision` fields.

---

##### Get latest revision info

**Endpoint**

`getLatestInDocumentOrCompany` \- [GET /revisions/{cd}/{cdid}/p/{pnum}/latest](https://cad.onshape.com/glassworks/explorer/#/Revision/getLatestInDocumentOrCompany)

**Parameters**

* `et`: `integer`  
   * See the [API Explorer](https://cad.onshape.com/glassworks/explorer/#/PartNumber) for a full list for allowed `et` values and additional parameter options.  
   * View instructions on locating the request body docs in the API Explorer: [View request body docs](https://onshape-public.github.io/docs/api-adv/relmgmt/docs/api-intro/explorer#view-request-body-docs)

**Example**

1. `did` \- The ID of any document owned by the company.
2. `pnum` \- The part number to get revision info for  
   * Call [getPartsWMVE](https://cad.onshape.com/glassworks/explorer/#/Part/getPartsWMVE)  
   * Response field - `partNumber`
3. `et` \- Element type  
   * View the [getLatestInDocumentOrCompany](https://cad.onshape.com/glassworks/explorer/#/Revision/getLatestInDocumentOrCompany) endpoint parameters to see available options.  
   * In this example, we’ll use `et=0` to indicate the part is in a Part Studio.
4. Call the [getLatestInDocumentOrCompany](https://cad.onshape.com/glassworks/explorer/#/Revision/getLatestInDocumentOrCompany) endpoint:  
   * cURL  
   * python  
`curl -X 'POST' \  
  'https://{baseUrl}.onshape.com/api/v14/revisions/d/{did}/p/{pnum}/latest?et=0' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic {credentials}' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09'  
`  
`import requests  
import json  
auth = (access_key, secret_key) # See Authentication guide  
headers = {  
  'Accept': 'application/json;charset=UTF-8;qs=0.09',  
  'Content-Type': 'application/json;charset=UTF-8; qs=0.09'  
}  
api_url = "https://{baseUrl}.onshape.com/api/v14/revisions/d/{did}/partnumber/{pnum}/"  
queryParams = {  
  "et": 0  
}  
response = requests.get( api_url,  
                          params=queryParams,  
                          auth=auth,  
                          headers=headers )  
print(json.dumps(response.json(), indent=4))  
`  
   * Note that you could also use `/c/{cid}` to submit a company ID instead of a document ID. Either is acceptable.
5. From the response, locate the `releaseName` and `revision` fields.

---

##### Get the next available part number

**Endpoint**

[POST /numberingscheme/nextNumbers](https://cad.onshape.com/glassworks/explorer/#/NumberingScheme/nextNumbers)

**Query Params**

`{
  "cid": <cid>,
  "did": <did>
}
`

* You must provide either the company ID or the ID of a document owned by the company.

**Request Body**

`{
  "itemPartNumbers": [
    {
      "documentId": <did>,
      "elementId": <eid>,
      "elementType": <elementType>,
      "numberSchemeResourceTypeId": <numberSchemeResourceTypeId>,
      "partId": <partId>,
      "workspaceId": <wid>
    }
  ]
}
`

* See the [nextNumbers](https://cad.onshape.com/glassworks/explorer/#/NumberingScheme/nextNumbers) request body schema for a full list for allowed values for `elementType` and `numberSchemeResourceTypeId`, and for additional parameter options, including configurations.
* View instructions on locating the request body docs in the API Explorer: [View request body docs](https://onshape-public.github.io/docs/api-adv/relmgmt/docs/api-intro/explorer#view-request-body-docs)

**Example**

1. `did` \- Document ID  
   * In the path parameter, this is the ID of any document owned by the company. This identifies the company’s numbering scheme.  
   * In the request body, this is the document that contains the part to get a part number for.
2. `eid` and `wid` \- The element (tab) and workspace that contain the part to get a part number for.
3. `partId` \- Part to get the next part number for:  
   * Call [getPartsWMVE](https://cad.onshape.com/glassworks/explorer/#/Part/getPartsWMVE)  
   * Response field - `partId`
4. See the [nextNumbers](https://cad.onshape.com/glassworks/explorer/#/NumberingScheme/nextNumbers) request body schema for a full list for allowed values for `elementType` and `numberSchemeResourceTypeId`.  
   * Use `elementType=0` to indicate a Part Studio.  
   * Use `numberSchemeResourceTypeId="8c96700620f77935a0b2cddc"` to indicate a Part Studio.
5. Call the endpoint:  
   * cURL  
   * python  
`curl -X 'POST' \  
  'https://{baseUrl}.onshape.com/api/v14/numberingscheme/nextNumbers?did={did}' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic {credentials}' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
      "itemPartNumbers": [  
        {  
          "documentId": "{did}",  
          "elementId": "{eid}",  
          "elementType": 0,  
          "numberSchemeResourceTypeId": "8c96700620f77935a0b2cddc",  
          "partId": "{partId}",  
          "workspaceId": "{wid}"  
        }  
      ]  
    }'  
`  
`import requests  
import json  
auth = (access_key, secret_key) # See Authentication guide  
headers = {  
  'Accept': 'application/json;charset=UTF-8;qs=0.09',  
  'Content-Type': 'application/json;charset=UTF-8; qs=0.09'  
}  
api_url = "https://{baseUrl}.onshape.com/api/v14/numberingscheme/nextNumbers"  
queryParams = {  
  "did": "{did}"  
}  
body = {  
  "itemPartNumbers": [  
    {  
      "documentId": "{did}",  
      "elementId": "{eid}",  
      "elementType": 0,  
      "numberSchemeResourceTypeId": "8c96700620f77935a0b2cddc",  
      "partId": "{partId}",  
      "partNumber": "{partNumber}",  
      "workspaceId": "{wid}"  
    }  
  ]  
}  
response = requests.post( api_url,  
                          params=queryParams,  
                          json=body,  
                          auth=auth,  
                          headers=headers )  
print(json.dumps(response.json(), indent=4))  
`
6. The next available `partNumber` is listed in the response.
7. You can apply this new part number when you submit the release, or as part of a [metadata update](https://onshape-public.github.io/docs/api-adv/relmgmt/docs/api-adv/metadata#update-a-part-number).

---

##### Submit a release candidate for approval

**Endpoint**

[POST /releasepackages/{rpid}](https://cad.onshape.com/glassworks/explorer/#/ReleasePackage/updateReleasePackage)

**Parameters**

* `rpid` \- ID of the release candidate to submit
* `action` \- `"UPDATE"`
* `wfaction` \- The workflow transition name to perform:  
   * Call [getReleasePackage](https://cad.onshape.com/glassworks/explorer/#/ReleasePackage/getReleasePackage)  
   * Response field - `workflow.actions.action`  
   * In the Onshape default release workflow, this is the `SUBMIT` action.  
   * Note the corresponding `workflow.actions.requiredProperties`. You need to set these in the request body `properties` array.

**Request Body**

`{
  "items": [
    {
      "id": <items.id>,
      "documentId": <items.documentId>,
      "elementId": <items.elementId>,
      "versionId": <items.versionId>,
      "href": <items.href>,
      "properties": [
        {
          "propertyId": <items.properties.propertyIdRevision>,
          "value": <revisionName>
        },
        {
          "propertyId": <items.properties.propertyIdPartNumber>,
          "value": <partNumber>
        }
      ]
    }
  ],
  "properties": [
    {
      "propertyId": <properties.propertyIdApprovers>,
      "value": [{"id": <userId>}]
    }
  ]
}
`

**Example**

1. `rpid` \- ID of the release candidate to update. Complete the [Create a release candidate](#create-a-release-candidate) example to get this id.
2. Complete the [View release candidate details](#view-release-candidate-details) example to obtain the following info from the response:  
   * `wfaction`  
         * `workflow.actions.action`  
         * For this example, we’ll use the `SUBMIT` transition from the Onshape default release workflow.  
   * `items` \- For each item to release, get the following info:  
         * `items.id`  
         * `items.documentId`  
         * `items.elementId`  
         * `items.versionId`  
         * `items.href`  
   * `items.properties` \- For each item to release, get the following properties:  
         * `items.property.propertyIdRevision` \- `items.properties.propertyId` where `items.properties.name="Revision"`  
         * `items.property.propertyIdPartNumber` \- `items.properties.propertyId` where `items.properties.name="Part number"`  
   * `properties.propertyId`  
         * Locate the `properties.propertyId` field that matches the `workflows.actions.requiredProperties` for your workflow action.  
         * Hint: make sure you’re looking at the top-level release candidate `properties`, not individual `items.properties`  
         * In this example, `properties.name="Approvers"`, indicating that we must include approvers with our submission.  
         * We’ll call this `properties.propertyIdApprovers` in the example for clarity.
3. `revisionName` \- The new revision for the released item.  
   * Must be unique. See [Get all revisions](#get-all-revisions) to see previous revisions.  
   * We’ll use `B` in this example.
4. `partNumber` \- The new part number for the released item.  
   * Must be unique. See [Get the next available part number](#get-the-next-available-part-number).  
   * We’ll use `PRT-002` in this example.
5. `userId` \- The approver to submit to  
   * Call [findCompany](https://cad.onshape.com/glassworks/explorer/#/Company/findCompany) to get the company `id`.  
   * Call [getAllowedApprovers](https://cad.onshape.com/glassworks/explorer/#/Workflow/getAllowedApprovers) using the company `id` as the `cid`.  
   * Response field - `items.user.id`
6. Submit the release:  
`curl -X 'POST' \  
  'https://cad.onshape.com/api/v14/releasecandidates/{rpid}?action=UPDATE&wfaction=SUBMIT' \  
  -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
        "items": [  
          {  
            "id": "{items.id}",  
            "documentId": "{items.documentId}",  
            "elementId": "{items.elementId}",  
            "versionId": "{items.versionId}",  
            "href": "{items.href}",  
            "properties": [  
              {  
                "propertyId": "{items.property.propertyIdRevision}",  
                "value": "B"  
              },  
              {  
                "propertyId": "{items.propertyIdPartNumber}",  
                "value": "PRT-002"  
              }  
            ]  
          }  
        ],  
        "properties": [  
          {  
            "propertyId": "{properties.propertyIdApprovers}",  
            "value": [{"id": "{userId}"}]  
          }  
        ]  
    }'  
`
7. The response indicates that the release candidate has been submitted for approval.

---

##### Approve a release candidate

You must be set as an approver in your [Onshape settings](https://cad.onshape.com/help/Content/Release/setting%5Fup%5Frelease%5Fmanagement.htm#Delegati) to approve a release.

**Endpoint**

`updateReleasePackage` \- [POST /releasepackages/{rpid}](https://cad.onshape.com/glassworks/explorer/#/ReleasePackage/updateReleasePackage)

**Parameters**

* `rpid` \- ID of the release candidate to publish
* `action` \- `"UPDATE"`
* `wfaction` \- The workflow transition name to perform:  
   * Call [getReleasePackage](https://cad.onshape.com/glassworks/explorer/#/ReleasePackage/getReleasePackage)  
   * Response field - `workflow.actions.action`  
   * In the Onshape default release workflow, this is the `RELEASE` action.

**Request Body**

`{}
`

**Example**

1. `rpid` \- ID of the release candidate to update. Complete the [Create a release candidate](#create-a-release-candidate) example to get this ID.
2. Complete the [Submit a release for approval](#submit-a-release-candidate-for-approval) example before this one.
3. `wfaction` \- The workflow transition name to perform:  
   * Call - [getReleasePackage](https://cad.onshape.com/glassworks/explorer/#/ReleasePackage/getReleasePackage)  
   * Response field - `workflow.actions.action`  
   * In this example, we’ll use the `RELEASE` transition from the Onshape default release workflow.
4. Submit the release. Note that you must send an empty json request body.  
`curl -X 'POST' \  
  'https://cad.onshape.com/api/v14/releasepackages/{rpid}?action=UPDATE&wfaction=RELEASE' \  
  -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{}'  
`

---

##### Release a part without approval

**Endpoint**

`updateReleasePackage` \- [POST /releasepackages/{rpid}](https://cad.onshape.com/glassworks/explorer/#/ReleasePackage/updateReleasePackage)

**Parameters**

* `rpid` \- ID of the release candidate to publish
* `action` \- `"UPDATE"`
* `wfaction` \- The workflow transition name to perform:  
   * Call - [getReleasePackage](https://cad.onshape.com/glassworks/explorer/#/ReleasePackage/getReleasePackage)  
   * Response field - `workflow.actions.action`  
   * In the Onshape default release workflow, this is the `CREATE_AND_RELEASE` action.

**Request Body**

`{
  "items": [
    {
      "id": <items.id>,
      "documentId": <items.documentId>,
      "elementId": <items.elementId>,
      "versionId": <items.versionId>,
      "href": <items.href>,
      "properties": [
        {
          "propertyId": <items.propertyIdRevision>,
          "value": "A"
        },
        {
          "propertyId": <items.propertyIdPartNumber>,
          "value": <items.partNumber>
        }
      ]
    }
  ]
}
`

**Example**

1. `rpid` \- ID of the release candidate to update. Complete the [Create a release candidate](#create-a-release-candidate) example before this one.
2. Complete the [View release candidate details](#view-release-candidate-details) example to obtain the following information:
* `wfaction`  
   * `workflow.actions.action`  
   * For this example, we’ll use the `CREATE_AND_RELEASE` transition from the default Onshape release workflow.
* `items` \- For each item to release, obtain the following:  
   * `items.id`  
   * `items.documentId`  
   * `items.elementId`  
   * `items.versionId`  
   * `items.href`
* `items.properties` \- For each item to release, obtain the following:  
   * `propertyIdRevision` \- `items.properties.propertyId` where `properties.name="Revision"`  
   * `propertyIdPartNumber` \- `items.properties.propertyId` where `properties.name="Part number"`
1. `partNumber` \- See [Get the next available part number](#get-the-next-available-part-number).
2. Submit the release:  
`curl -X 'POST' \  
  'https://cad.onshape.com/api/v14/releasepackages/{rpid}?action=UPDATE&wfaction=CREATE_AND_RELEASE' \  
  -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
  "items": [  
    {  
      "id": "{items.id}",  
      "documentId": "{items.documentId}",  
      "elementId": "{items.elementId}",  
      "versionId": "{items.versionId}",  
      "href": "{items.href}",  
      "properties": [  
        {  
          "propertyId": "{items.propertyIdRevision}",  
          "value": "A"  
        },  
        {  
          "propertyId": "{items.propertyIdPartNumber}",  
          "value": "{items.partNumber}"  
        }  
      ]  
    }  
  ]  
}'  
`

---

#### Additional Resources

* API Explorer: [Revision Endpoints](https://cad.onshape.com/glassworks/explorer/#/Revision)
* API Explorer: [Release Endpoints](https://cad.onshape.com/glassworks/explorer/#/ReleasePackage)
* API Guide: [Using the API Explorer](https://onshape-public.github.io/docs/api-adv/relmgmt/docs/api-intro/explorer)
* Onshape Help: [Release Management](https://cad.onshape.com/help/Content/release%5Fmanagement.htm)

---

<a id="pg-docs-api-adv-translation"></a>
### Import & Export

_Source: <https://onshape-public.github.io/docs/api-adv/translation/>_

This page describes the APIs Onshape provides for importing files to Onshape and exporting files from Onshape into different formats. We refer to the process of importing and exporting files from one format to another as _translating_ the files.

Onshape provides several APIs to support this format translation. These fall into three categories:

* [Asynchronous exports](#asynchronous-exports) \- Export Onshape elements to one of many supported formats.
* [Synchronous exports](#synchronous-exports) \- Faster export to specific formats with limited settings options.
* [Import to Onshape](#imports) \- Import a translatable file by uploading it to an Onshape blob element.
  
> ⚠️ **Warning**
> 
> When polling for translations to complete, use a reasonable interval (e.g., avoid polling multiple times a second, use an exponential backoff strategy, etc.) or use [Webhooks](https://onshape-public.github.io/docs/api-adv/translation/docs/app-dev/webhook). See [Rate Limiting](https://onshape-public.github.io/docs/api-adv/translation/docs/api-adv/errors/#429) and [API Limits](https://onshape-public.github.io/docs/api-adv/translation/docs/auth/limits) for more information.

  
| PrerequisitesAll Onshape API calls must be properly authenticated.See the [API Keys](https://onshape-public.github.io/docs/api-adv/translation/docs/auth/apikeys) page for instructions and the [Quick Start](https://onshape-public.github.io/docs/api-adv/translation/docs/api-intro/quickstart) for an example.All applications submitted to the Onshape App Store _must_ authenticate with [OAuth2](https://onshape-public.github.io/docs/api-adv/translation/docs/auth/oauth).For Standard accounts, replace {baseUrl} with cad in all endpoints. For Enterprise accounts, replace it with your company domain. Add /api and the version number, and then provide the endpoint.https://{baseUrl}.onshape.com/api/v10/documentshttps://cad.onshape.com/api/v10/documentshttps://companySubDomain.onshape.com/api/v10/documentsOnshape IDs are written as: {did}, {wvmid}, {eid}, {pid}, {otherId}.These represent document, workspace (or version or microversion), element, part, and other IDs, respectively.See [API Guide: API Intro](https://onshape-public.github.io/docs/api-adv/translation/docs/api-intro/#onshape-api-request) for information on what these IDs mean and how to obtain them from your documents.Variables are written as: {variableId1} or <variableIdTwo>.These represent variables that must be replaced in the code before it is usable.Never include the braces {} or angle brackets <> with your IDs/variables.This page provides sample code in cURL and python.For additional instruction and video content, visit the Learning Center’s [Intro to the Onshape API](https://learn.onshape.com/learn/course/intro-to-the-onshape-api/intro-to-the-onshape-api/what-is-an-api?page=1) course. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

#### Translation Endpoint Details

##### Asynchronous exports

These endpoints provide a way to export Onshape elements to other formats, and provide options for tessellation control and other settings.

> ℹ️ **Note**
> 
> Asynchronous exports can take longer than synchronous options, but support more formats and provide more control over tessellation and other settings.

The exports in the next section perform the format translation synchronously, returning the output immediately after some processing delay. Other format conversions are more complex and time-consuming, and in many cases, cannot be completed quickly enough to prevent connection errors. For those use cases, the asynchronous endpoints presented in this section are the preferred option.

Note that the source format for an export is currently always automatically detected by Onshape. File uploads have their type determined by the filename suffix. For example, a file named _part7.step_ is assumed to be in `STEP` format. Part Studios and Assemblies use the `ONSHAPE` format.

The following asynchronous translation APIs are available:

* Part Studios:  
   * [createPartStudioExportGltf](https://cad.onshape.com/glassworks/explorer/#/PartStudio/createPartStudioExportGltf): Export a Part Studio to glTF.  
   * [createPartStudioExportObj](https://cad.onshape.com/glassworks/explorer/#/PartStudio/createPartStudioExportObj): Export a Part Studio to OBJ.  
   * [createPartStudioExportStep](https://cad.onshape.com/glassworks/explorer/#/PartStudio/createPartStudioExportStep): Export an Part Studio to STEP.  
   * [createPartStudioTranslation](https://cad.onshape.com/glassworks/explorer/#/PartStudio/createPartStudioTranslation): Export a Part Studio to the specified `formatName`. Use only when a format-specific asynchronous endpoint is unavailable.
* Assemblies:  
   * [createAssemblyExportGltf](https://cad.onshape.com/glassworks/explorer/#/Assembly/createAssemblyExportGltf): Export an Assembly to glTF.  
   * [createAssemblyExportObj](https://cad.onshape.com/glassworks/explorer/#/Assembly/createAssemblyExportObj): Export an Assembly to OBJ.  
   * [createAssemblyExportStep](https://cad.onshape.com/glassworks/explorer/#/Assembly/createAssemblyExportStep): Export an Assembly to STEP.  
   * [translateFormat](https://cad.onshape.com/glassworks/explorer/#/Assembly/translateFormat): Export an Assembly to the specified `formatName`. Use only when a format-specific asynchronous endpoint is unavailable.
* Drawings: [createDrawingTranslation](https://cad.onshape.com/glassworks/explorer/#/Drawing/createDrawingTranslation): Export a Drawing to the specified `formatName`.
* Blob Elements: [createBlobTranslation](https://cad.onshape.com/glassworks/explorer/#/BlobElement/createBlobTranslation): Export a Blob Element to the specified `formatName`.

To export your Onshape content to another format:

1. For non-format-specific endpoints, determine what export format file types are available for your content by calling: [Translations/getAllTranslatorFormats](https://cad.onshape.com/glassworks/explorer/#/Translation/getAllTranslatorFormats).  
   * Note that Drawings have their own API for this call: [Drawing/getDrawingTranslatorFormats](https://cad.onshape.com/glassworks/explorer/#/Drawing/getDrawingTranslatorFormats)
2. Next, initiate the export by calling one of the asynchronous translation APIs.  
   * Note that each of these APIs takes a JSON for specifying options for the export as part of the request body. Refer to the [API Explorer](https://onshape-public.github.io/docs/api-adv/translation/docs/api-intro/explorer) page for help viewing these JSON docs.  
   * For non-format-specific endpoints, the target file format **must be specified in the `formatName` field** in the request body, and must match a valid format found in Step 1.  
   * By default, `storeInDocument` is set to `false` in the request body to export to a single data file (or a zip of multiple files). Set to `true` to export as a blob element in your document.
3. Wait for the translation to complete. You can either register a webhook and wait to receive a notification that the translation is complete (see [Webhook Notifications](https://onshape-public.github.io/docs/api-adv/translation/docs/app-dev/webhook/)), or you can poll the translation’s `requestState`:  
   * You can poll the `requestState` from the initial translation’s response, or you can call [Translation/getTranslation](https://cad.onshape.com/glassworks/explorer/#/Translation/getTranslation) on the `translationId` from the initial translation’s response.  
   * ⚠️ **Poll at a reasonable interval**. See [Rate Limiting](https://onshape-public.github.io/docs/api-adv/translation/docs/api-adv/errors/#429) and [API Limits](https://onshape-public.github.io/docs/api-adv/translation/docs/auth/limits) for more information.  
   * When a translation is complete, `requestState` will change from `ACTIVE` to either `DONE` or `FAILED`.  
   * When `requestState=DONE`, results are available to be used.
4. Retrieve the exported results:  
   * If you exported to an external file, call [Documents/downloadExternalData](https://cad.onshape.com/glassworks/explorer/#/Document/downloadExternalData) to retrieve the exported result.  
         * Note that this API takes the source document ID and a “foreign ID” as required parameters.  
         * Use the `resultExternalDataIds` from the translation response as the foreign ID (`fid`).  
         * External data is associated with, but external to, the document used as translation context. This data is not versioned like with in-document data.  
   * If your translation request body specified `storeInDocument=true`, retrieve the blob element data with [BlobElement/downloadFileWorkspace](https://cad.onshape.com/glassworks/explorer/#/BlobElement/downloadFileWorkspace).  
         * The element IDs for the new blob elements can be found in the `resultElementIds` field in the translation response.

##### Synchronous exports

These endpoints synchronously export parts or Part Studios to glTF, Parasolid, and STL formats. They provide faster results than asynchronous export options at the expense of control over tessellation and other settings.

> ℹ️ **Note**
> 
> Synchronous exports are much faster than asynchronous options, but provide limited control on tessellation settings. Use [Asynchronous exports](#asynchronous-exports) for more control.

Most of the interfaces defined here operate by requesting an HTTP redirect to a different URL where the request is fulfilled. Applications must explicitly handle the redirect and attachment authentication headers to the follow-up request, or it will fail.

> ℹ️ **Note**
> 
> Synchronous exports return a 307 redirect from which to download the exported file.

The following synchronous endpoints are available:

* [Export Part to glTF](https://cad.onshape.com/glassworks/explorer/#/Part/exportPartGltf)
* [Export Part to Parasolid](https://cad.onshape.com/glassworks/explorer/#/Part/exportPS)
* [Export Part to STL](https://cad.onshape.com/glassworks/explorer/#/Part/exportStl)
* [Export PartStudio to glTF](https://cad.onshape.com/glassworks/explorer/#/PartStudio/exportPartStudioGltf)
* [Export PartStudio to Parasolid](https://cad.onshape.com/glassworks/explorer/#/PartStudio/exportParasolid)
* [Export PartStudio to STL](https://cad.onshape.com/glassworks/explorer/#/PartStudio/exportPartStudioStl)
* [Export Document to JSON](https://cad.onshape.com/glassworks/explorer/#/Document/export2Json)

##### Imports

Files can be imported to Onshape as blob elements. When uploading a file to a blob element, either as a new element or an update to an existing element, if the file is a recognized format for import, it will be translated into `ONSHAPE` format by default. This behavior can be overridden by the application, if desired.

* [Translation/createTranslation](https://cad.onshape.com/glassworks/explorer/#/Translation/createTranslation)  
```  
curl -X 'POST' \  
  'https://cad.onshape.com/api/v6/translations/d/{did}/w/{wid}' \  
  -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Content-Type: multipart/form-data' \  
  -F 'storeInDocument=true' \  
  -F 'flattenAssemblies=true  
  -F 'file=@/path/filename.ext'  
  -F 'formatName=' \  
  ...  
```
* [BlobElement/uploadFileCreateElement](https://cad.onshape.com/glassworks/explorer/#/BlobElement/uploadFileCreateElement)  
```  
curl -X 'POST' \  
  'https://cad.onshape.com/api/v6/blobelements/d/{did}/w/{wid}' \  
    -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS' \  
    -H 'Content-Type: multipart/form-data' \  
    -F 'storeInDocument=true' \  
    -F 'file=@/path/filename.ext'  
    -F 'formatName=' \  
    ...  
```
* [BlobElement/uploadFileUpdateElement](https://cad.onshape.com/glassworks/explorer/#/BlobElement/uploadFileUpdateElement)  
```  
  curl -X 'POST' \  
  'https://cad.onshape.com/api/v6/blobelements/d/{did}/w/{wid}/e/{eid}' \  
    -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS' \  
    -H 'Content-Type: multipart/form-data' \  
    -F 'storeInDocument=true' \  
    -F 'locationElementId=' \  
    -F 'file=@/path/filename.ext'  
    ...  
```

Note that these endpoints require you to specify the target document ID and workspace ID. You must also include the file to import. These APIs also includes a request body JSON for specifying options for the import.

* Override the translation to `ONSHAPE` format by specifying a valid format in the `formatName` field. Get a list of valid import formats by calling [Translation/getAllTranslatorFormats](https://cad.onshape.com/glassworks/explorer/#/Translation/getAllTranslatorFormats).
* Specify `storeInDocument=true` to import the data as a blob element into the target document. Change to `false` to only create an external data file.
* If the source file contains an assembly and `flattenAssemblies=true`, the assembly structure is removed and a single part studio is created.
* Note that when using cURL, you must begin the path to the file with an `@` symbol.

#### Async Export Examples

##### Export a Part Studio to glTF, OBJ, or STEP

**Endpoints**

* [POST /partstudios/d/{did}/{wv}/{wvid}/e/{eid}/export/gltf](https://cad.onshape.com/glassworks/explorer/#/PartStudio/createPartStudioExportGltf)
* [POST /partstudios/d/{did}/{wv}/{wvid}/e/{eid}/export/obj](https://cad.onshape.com/glassworks/explorer/#/PartStudio/createPartStudioExportObj)
* [POST /partstudios/d/{did}/{wv}/{wvid}/e/{eid}/export/step](https://cad.onshape.com/glassworks/explorer/#/PartStudio/createPartStudioExportStep)

**Request Body**

```
{
  "meshParams": {
    "angularTolerance": 0.001,
    "distanceTolerance": 0.001,
    "maximumChordLength": 0.01,
    "resolution": "FINE",
    "unit": "METER"
  },
  "storeInDocument": true
}

```

_Additional optional fields available. See the [API Explorer](https://cad.onshape.com/glassworks/explorer/#/PartStudio) for a full list._

**Example**

1. Create a new Part Studio or open an existing one. Make a note of the documentId, workspaceId, and elementId of the Part Studio in your new document.
2. Make the call to one of the endpoints listed above (the example exports to `glTF` format). Replace `{did}`, `{wv}`, `{vwid}`, and `{eid}` with the document, workspace, and element IDs from your copied document. Do NOT include the curly braces (`{}`) in the final call.  
```  
curl -X 'POST' \  
  'https://cad.onshape.com/api/v11/partstudios/d/{did}/{wv}/{wvid}/e/{eid}/export/gltf' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
    "meshParams": {  
      "angularTolerance": 0.001,  
      "distanceTolerance": 0.001,  
      "maximumChordLength": 0.01,  
      "resolution": "FINE",  
      "unit": "METER"  
    },  
    "storeInDocument": true  
  }'  
```  
   * Note that the API takes a JSON as part of the request body, in which you can specify options for the export.  
   * In the example above, we’ve just shown a snippet of the entire JSON where we set the required mesh options.  
   * Set `storeInDocument` to `true` to upload the file as a blob element in your document.
3. In the response, copy the value in the `id` field. This is the ID of the translation itself.
4. Next, poll the [Translation/getTranslation](https://cad.onshape.com/glassworks/explorer/#/Translation/getTranslation) response until `requestState` changes from `ACTIVE` to `DONE` or `FAILED`.  
```  
{  
  "requestState": "DONE",  
  "requestElementId": "{eid}",  
  "resultExternalDataIds": null,  
  "versionId": null,  
  "workspaceId": "{wid}",  
  "documentId": "{did}",  
  "resultElementIds": [  
    "{resultElementId}"  
  ],  
  "resultDocumentId": "{did}",  
  "failureReason": null,  
  "resultWorkspaceId": "{wid}",  
  "name": "Part Studio 1",  
  "id": "{translationId}", // use the translationId from the previous step  
  "href": "https://cad.onshape.com/api/v11/translations/{translationId}"  
}  
```
5. Once `requestState=DONE`, make a note of the `resultElementId` in the response. This is the element ID of the blob with the exported file.
6. Now, we can call [BlobElement/downloadFileWorkspace](https://cad.onshape.com/glassworks/explorer/#/BlobElement/downloadFileWorkspace) to retrieve the exported results.  
```  
curl -X 'GET' \  
'https://cad.onshape.com/api/v6/blobelements/d/{did}/{wv}/{wvid}/e/{resulteid}' \  
  -H 'accept: application/octet-stream' \  
  -H 'Authorization: Basic CREDENTIALS' \  
```  
   * Use the `resultElementIds` value from the translation response as the element ID (`{resulteid}`).  
   * Note that since we set `storeInDocument=true`, you can also open the file from the new `Part Studio 1.zip` tab in your document.

##### Export a Part Studio to another format

Use only when a format-specific asynchronous endpoint is unavailable.

**Endpoint**

[POST /partstudios/d/{did}/{wv}/{wvid}/e/{eid}/translations](https://cad.onshape.com/glassworks/explorer/#/PartStudio/createPartStudioTranslation)

**Request Body**

```
{
  "formatName": "{formatName}",
  "storeInDocument": false,
  "translate": true
}

```

_Additional optional fields available. See the [API Explorer](https://cad.onshape.com/glassworks/explorer/#/PartStudio/createPartStudioTranslation) for a full list._

**Example**

We will export the `CRANK` PartStudio from [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/6bed6b43463f6a46a37b4a22) to an ACIS file.

1. Validate that ACIS is a supported export file type by calling [Translation/getAllTranslatorFormats](https://cad.onshape.com/glassworks/explorer/#/Translation/getAllTranslatorFormats) and confirming that `validDestinationFormat=true` for `translatorName=ACIS`.  
**request**  
```  
curl -X 'GET' \  
'https://cad.onshape.com/api/v6/translations/translationformats' \  
  -H 'accept: application/json;charset=UTF-8; qs=0.09'  \  
  -H 'Authorization: Basic CREDENTIALS' \  
```  
**response**  
```  
[  
  {  
    "validSourceFormat": true,  
    "validDestinationFormat": true,  
    "name": "ACIS",  
    "translatorName": "acis",  
    "couldBeAssembly": true  
  }  
]  
```
2. Next, initialize the export by calling [PartStudio/createPartStudioTranslation](https://cad.onshape.com/glassworks/explorer/#/PartStudio/createPartStudioTranslation).  
```  
curl -X 'POST' \  
'https://cad.onshape.com/api/v6/partstudios/d/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/6bed6b43463f6a46a37b4a22/translations' \  
 -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
 -H 'Authorization: Basic CREDENTIALS' \  
 -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
 -d '{  
      "formatName": "ACIS",  
      "storeInDocument": false,  
      "translate": true  
 }'  
```  
   * Note that the API takes a JSON as part of the request body, in which you can specify options for the export.  
   * A `formatName` string must be specified that matches one of the valid formats you found in the first step. In this example, we set `formatName` to `ACIS.`  
   * We want to export this to a new file, so we’ll leave `storeInDocument` set to `false`.
3. Execute the call and get the `id` from the response. This is your `translationId`.
4. Poll the response or call the [Translation/getTranslation](https://cad.onshape.com/glassworks/explorer/#/Translation/getTranslation) endpoint, using the `{translationId}` from the previous call’s response.  
```  
curl -X 'GET' \  
'https://cad.onshape.com/api/v9/translations/{translationId}' \  
  -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS'  
```
5. Once `requestState` in the response changes from `ACTIVE` to `DONE`, the `resultExternalDataIds` field will be populated.  
```  
{  
  "failureReason": null,  
  "resultElementIds": null,  
  "resultDocumentId": "e60c4803eaf2ac8be492c18e",  
  "resultWorkspaceId": "d2558da712764516cc9fec62",  
  "requestState": "DONE",  
  "requestElementId": "6bed6b43463f6a46a37b4a22",  
  "resultExternalDataIds": [  
    "{resultExternalDataId}"  
  ],  
  "versionId": null,  
  "workspaceId": "d2558da712764516cc9fec62",  
  "documentId": "e60c4803eaf2ac8be492c18e",  
  "name": "CRANK,  
  "id": "{translationId}",  
  "href": "https://cad.onshape.com/api/v9/translations/{translationId}"  
}  
```
6. Finally, call [Documents/downloadExternalData](https://cad.onshape.com/glassworks/explorer/#/Document/downloadExternalData) to retrieve the exported result.  
```  
curl -X 'GET' \  
'https://cad.onshape.com/api/v6/documents/d/e60c4803eaf2ac8be492c18e/externaldata/{fid}'  
```  
   * Use the `resultExternalDataId` value from the translation response as the foreign ID (`fid`).  
   * The new ACIS file is returned as the response and will be downloaded to wherever the API call is made.

##### Export an Assembly to glTF, OBJ, or Step

**Endpoints**

* [POST /assemblies/d/{did}/{wv}/{wvid}/e/{eid}/export/gltf](https://cad.onshape.com/glassworks/explorer/#/Assembly/createAssemblyExportGltf)
* [POST /assemblies/d/{did}/{wv}/{wvid}/e/{eid}/export/obj](https://cad.onshape.com/glassworks/explorer/#/Assembly/createAssemblyExportObj)
* [POST /assemblies/d/{did}/{wv}/{wvid}/e/{eid}/export/step](https://cad.onshape.com/glassworks/explorer/#/Assembly/createAssemblyExportStep)

**Request Body**

```
{
  "meshParams": {
    "angularTolerance": 0.001,
    "distanceTolerance": 0.001,
    "maximumChordLength": 0.01,
    "resolution": "FINE",
    "unit": "METER"
  },
  "storeInDocument": true
}

```

_Additional optional fields available. See the [API Explorer](https://cad.onshape.com/glassworks/explorer/#/Assembly) for a full list._

**Example**

1. Create a new assembly or open an existing one. Make a note of the documentId, workspaceId, and elementId of the assembly in your new document.
2. Make the call to one of the endpoints listed above. This example exports to `glTF`. Replace `{did}`, `{wv}`, `{wvid}`, and `{eid}` with the document, workspace, and element IDs from your copied document. Do NOT include the curly braces (`{}`) in the final call.  
```  
curl -X 'POST' \  
  'https://cad.onshape.com/api/v11/assemblies/d/{did}/{wv}/{wvid}/e/{eid}/export/gltf' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
    "meshParams": {  
      "angularTolerance": 0.001,  
      "distanceTolerance": 0.001,  
      "maximumChordLength": 0.01,  
      "resolution": "FINE",  
      "unit": "METER"  
    },  
    "storeInDocument": true  
  }'  
```  
   * Note that the API takes a JSON as part of the request body, in which you can specify options for the export.  
   * In the example above, we’ve just shown a snippet of the entire JSON where we set the required mesh options.  
   * Set `storeInDocument` to `true` to upload the file as a blob element in your document.
3. In the response, copy the value in the `id` field. This is the ID of the translation itself.
4. Next, poll the [Translation/getTranslation](https://cad.onshape.com/glassworks/explorer/#/Translation/getTranslation) response until `requestState` changes from `ACTIVE` to `DONE` or `FAILED`.  
```  
{  
  "requestState": "DONE",  
  "requestElementId": "{eid}",  
  "resultExternalDataIds": null,  
  "versionId": null,  
  "workspaceId": "{wid}",  
  "documentId": "{did}",  
  "resultElementIds": [  
    "{resultElementId}"  
  ],  
  "resultDocumentId": "{did}",  
  "failureReason": null,  
  "resultWorkspaceId": "{wid}",  
  "name": "Assembly 1",  
  "id": "{translationId}", // use the translationId from the previous step  
  "href": "https://cad.onshape.com/api/v11/translations/{translationId}"  
}  
```
5. Once `requestState=DONE`, make a note of the `resultElementId` in the response. This is the element ID of the blob with the exported file.
6. Now, we can call [BlobElement/downloadFileWorkspace](https://cad.onshape.com/glassworks/explorer/#/BlobElement/downloadFileWorkspace) to retrieve the exported results.  
```  
curl -X 'GET' \  
'https://cad.onshape.com/api/v6/blobelements/d/{did}/{wv}/{wvid}/e/{resulteid}' \  
  -H 'accept: application/octet-stream' \  
  -H 'Authorization: Basic CREDENTIALS' \  
```  
   * Use the `resultElementIds` value from the translation response as the element ID (`{resulteid}`).  
   * Note that since we set `storeInDocument=true`, you can also open the file from the new `Assembly 1.zip` tab in your document.

##### Export an Assembly to another format

Use only when a format-specific asynchronous endpoint is unavailable.

**Endpoint**

[POST /assemblies/d/{did}/{wv}/{wvid}/e/{eid}/translations](https://cad.onshape.com/glassworks/explorer/#/Assembly/translateFormat)

**Request Body**

```
{
  "allowFaultyParts": true,
  "angularTolerance": 0.001,
  "formatName": "{formatName}",
  "storeInDocument": true
}

```

_Additional optional fields available. See the [API Explorer](https://cad.onshape.com/glassworks/explorer/#/Assembly/translateFormat) for a full list._

**Example**

In this example, we’ll export an assembly from [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/23a9385cd48c50167c32d6d1) to an ACIS file.

1. Make a copy of [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/23a9385cd48c50167c32d6d1) so you can export the assembly. Make a note of the documentId, workspaceId, and elementId of the assembly in your new document.
2. Validate that ACIS is a supported export file type for assemblies by calling [Translation/getAllTranslatorFormats](https://cad.onshape.com/glassworks/explorer/#/Translation/getAllTranslatorFormats) and confirming that `validDestinationFormat=true` and `couldBeAssembly=true` for `translatorName=ACIS`.  
**request**  
```  
curl -X 'GET' \  
'https://cad.onshape.com/api/v6/translations/translationformats' \  
  -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS' \  
```  
**response**  
```  
[  
  {  
    "validSourceFormat": true,  
    "validDestinationFormat": true,  
    "name": "ACIS",  
    "translatorName": "step",  
    "couldBeAssembly": true  
  },  
  ...  
]  
```
3. Initialize the export by calling [Assembly/translateFormat](https://cad.onshape.com/glassworks/explorer/#/Assembly/translateFormat). Replace `{did}`, `{wv}`, `{wvid}`, and `{eid}` with the document, workspace, and element IDs from your copied document. Do NOT include the curly braces (`{}`) in the final call.  
```  
curl -X 'POST' \  
'https://cad.onshape.com/api/v11/assemblies/d/{did}/{wv}/{wvid}/e/{eid}/translations' \  
  -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
      "allowFaultyParts": true,  
      "angularTolerance": 0.001,  
      "formatName": "ACIS",  
      "storeInDocument": true  
      }'  
```  
   * Note that the API takes a JSON as part of the request body, in which you can specify options for the export.  
   * In the example above, we’ve just shown a snippet of the entire JSON where we allow faulty parts to be exported and set the angular tolerance to 0.001.  
   * A `formatName` string must be specified that matches one of the valid formats you found in the last step. In this example, we set `formatName` to `ACIS.`  
   * Set `storeInDocument` to `true` to upload the STEP file as a blob element in your document.
4. In the response, copy the value in the `id` field. This is the ID of the translation itself.  
```  
{  
  "requestState": "ACTIVE",  
  "requestElementId": "{eid}",  
  "resultExternalDataIds": null,  
  "versionId": null,  
  "workspaceId": "{wid}",  
  "documentId": "{did}",  
  "resultElementIds": null,  
  "resultDocumentId": "{did}",  
  "failureReason": null,  
  "resultWorkspaceId": "{wid}",  
  "name": "PISTON",  
  "id": "{translationId}",  
  "href": "https://cad.onshape.com/api/v9/translations/{translationId}"  
}  
```
5. Next, poll the [Translation/getTranslation](https://cad.onshape.com/glassworks/explorer/#/Translation/getTranslation) response until `requestState` changes from `ACTIVE` to `DONE` or `FAILED`.  
```  
{  
  "requestState": "DONE",  
  "requestElementId": "{eid}",  
  "resultExternalDataIds": null,  
  "versionId": null,  
  "workspaceId": "{wid}",  
  "documentId": "{did}",  
  "resultElementIds": [  
    "{resultElementId}"  
  ],  
  "resultDocumentId": "{did}",  
  "failureReason": null,  
  "resultWorkspaceId": "{wid}",  
  "name": "PISTON",  
  "id": "{translationId}",  
  "href": "https://cad.onshape.com/api/v9/translations/{translationId}"  
}  
```
6. Once `requestState=DONE`, make a note of the `resultElementId` in the response. This is the element ID of the blob with the exported file.
7. Now, we can call [BlobElement/downloadFileWorkspace](https://cad.onshape.com/glassworks/explorer/#/BlobElement/downloadFileWorkspace) to retrieve the exported results.  
```  
curl -X 'GET' \  
'https://cad.onshape.com/api/v6/blobelements/d/{did}/{wv}/{wvid}/e/{resulteid}' \  
  -H 'accept: application/octet-stream' \  
  -H 'Authorization: Basic CREDENTIALS' \  
```  
   * Use the `resultElementIds` value from the translation response as the element ID (`{resulteid}`).  
   * Note that you can also open your document, click the `PISTON.sat` tab, and download the file from there.

##### Export an Assembly to a binary

Assemblies can be exported to a Parasolid binary.

**Endpoint**

[POST /assemblies/d/{did}/{wv}/{wvid}/e/{eid}/translations](https://cad.onshape.com/glassworks/explorer/#/Assembly/translateFormat)

**Request Body**

```
{
  "formatName": "PARASOLID",
  "parasolidMode": "BINARY", 
  "storeInDocument": true
}

```

_Additional optional fields available. See the [API Explorer](https://cad.onshape.com/glassworks/explorer/#/Assembly/translateFormat) for a full list._

#### Synchronous Exports Examples

##### Export a PartStudio to STL

We will export the `CRANK` PartStudio from [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/6bed6b43463f6a46a37b4a22) to an STL file.

1. Call the [Part Studios/exportPartStudioStl](https://cad.onshape.com/glassworks/explorer/#/PartStudio/exportPartStudioStl) endpoint on the document:  
```  
curl -X 'GET' \  
'https://cad.onshape.com/api/v6/partstudios/d/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/6bed6b43463f6a46a37b4a22/stl?mode=text&grouping=true&scale=1&units=inch' \  
  -H 'accept: */*'  
```
2. Navigate to the request URL to download the resulting STL file:  
```  
https://cad.onshape.com/api/v6/partstudios/d/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/6bed6b43463f6a46a37b4a22/stl?mode=text&grouping=true&scale=1&units=inch  
```
3. Open the _CRANK.stl_ file from wherever your downloads are saved.

##### Export a Part to Parasolid

We will export the `FLYWHEEL` part from [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/6bed6b43463f6a46a37b4a22) to an STL file.

1. Call the [Part/getPartsWMV](https://cad.onshape.com/glassworks/explorer/#/Part/getPartsWMV) endpoint on your document and get all the part IDs:  
```  
curl -X 'GET' \  
'https://cad.onshape.com/api/v6/parts/d/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62?elementId=6bed6b43463f6a46a37b4a22&withThumbnails=false&includePropertyDefaults=false' \  
  -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS'  
```
2. Locate the part to export (hint: look for `name = yourPartName`) in the response body. Get the part ID from the `partId` field. In the example below, `partId = JiD` for `name=FLYWHEEL`:  
```  
[  
  ...  
  {  
    "name" : "FLYWHEEL",  
    "state" : "IN_PROGRESS",  
    "propertySourceTypes" : {  
      "57f3fb8efa3416c06701d60f" : 3,  
      "57f3fb8efa3416c06701d60d" : 3,  
      "57f3fb8efa3416c06701d61e" : 3,  
      "57f3fb8efa3416c06701d60e" : 3,  
      "57f3fb8efa3416c06701d60c" : 3  
    },  
    "defaultColorHash" : "FzHLKqGeuTBFjmY_2_0",  
    "ordinal" : 1,  
    "isMesh" : false,  
    "description" : "Flywheel",  
    "microversionId" : "bdb504d2d4c948493a87ccf3",  
    "partNumber" : "PRT-10241",  
    "elementId" : "6bed6b43463f6a46a37b4a22",  
    "partId" : "JiD",  
    "bodyType" : "solid",  
    "customProperties" : {  
      "57f3fb8efa3416c06701d61e" : "false"  
    }  
  ...  
]  
```
3. Call the [Part/exportPS](https://cad.onshape.com/glassworks/explorer/#/Part/exportPS) endpoint on the FLYWHEEL part:  
```  
curl -X 'GET' \  
'https://cad.onshape.com/api/v6/parts/d/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/6bed6b43463f6a46a37b4a22/partid/JiD/parasolid?version=0' \  
  -H 'accept: application/octet-stream' \  
  -H 'Authorization: Basic CREDENTIALS'  
```
4. Navigate to the request URL to download the resulting file:  
```  
https://cad.onshape.com/api/v6/parts/d/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/6bed6b43463f6a46a37b4a22/partid/JiD/parasolid?version=0  
```
5. Open the _CRANK.x\_t_ file from your downloads. Note that the file is automatically named after the PartStudio to which the part belongs.

##### Export a drawing to JSON

In this example, we’ll export a drawing from [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/15b07287508246ccd038e31e) to JSON. Exporting a Drawing to JSON is useful when you need to gather information about that drawing (for example, finding valid coordinates on which to place an inspection symbol).

> 📘 **Notes**
> 
> * Notes are exported with [RTF15](https://www.biblioscape.com/rtf15%5Fspec.htm) formatting.
> * Flags are not currently exported with notes.
> * Geometric tolerance frame fields are separated with `%%v`.
> * Geometric tolerance prefix and suffix fields are currently not exported.

1. Make a copy of [this public document](https://cad.onshape.com/documents/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/15b07287508246ccd038e31e) so you can export the drawing. Make a note of the documentId, workspaceId, and elementId of the drawing in your new document. These will be your `{did}`, `{wid}`, and `{eid}` fields for this example, unless otherwise specified.
2. Validate that JSON is a supported export file type for Drawings by calling [Drawing/getDrawingTranslatorFormats](https://cad.onshape.com/glassworks/explorer/#/Drawing/getDrawingTranslatorFormats) and confirming that `"name": "DRAWING_JSON"` appears in the response for the drawing element in your copied document.  
**request**  
```  
curl -X 'GET' \  
'https://cad.onshape.com/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/translationformats' \  
  -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS'  
```  
**response**  
```  
[  
  {  
    "name": "DRAWING_JSON",  
    "translatorName": "drawing_json",  
    "couldBeAssembly": false  
  },  
  ...  
]  
```
3. Initialize the export by calling [Drawing/createDrawingTranslation](https://cad.onshape.com/glassworks/explorer/#/Drawing/createDrawingTranslation). Replace `{did}`, `{wid}`, and `{eid}` with the document, workspace, and element IDs from your copied document. Do NOT include the curly braces (`{}`) in the final call.  
```  
curl -X 'POST' \  
  'https://cad.onshape.com/api/v6/drawings/d/{did}/w/{wid}/e/{eid}/translations' \  
  -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
  -d '{  
      "formatName": "DRAWING_JSON"  
      }'  
```  
   * Note that the API takes a JSON as part of the request body, in which you can specify options for the export.  
   * The only required JSON field is `formatName`, in which we’ve specified the format as found in the `getDrawingTranslatorFormats` response body.  
   * The `formatName` value must match the `name` field from the previous step exactly, including casing.
4. In the response, copy the `translationId` value from the `id` field. This is the ID of the translation itself.  
```  
{  
  "requestState": "ACTIVE",  
  "requestElementId": "{eid}",  
  "resultExternalDataIds": null,  
  "versionId": null,  
  "workspaceId": "{wid}",  
  "documentId": "{did}",  
  "resultElementIds": null,  
  "resultDocumentId": "{did}",  
  "failureReason": null,  
  "resultWorkspaceId": "{wid}",  
  "name": "GEARBOX_CHUCK",  
  "id": "{translationId}",  
  "href": "https://cad.onshape.com/api/v9/translations/{translationId}"  
}  
```
5. Next, poll the [Translation/getTranslation](https://cad.onshape.com/glassworks/explorer/#/Translation/getTranslation) response until `requestState` changes from `ACTIVE` to `DONE` or `FAILED`.  
```  
{  
  "requestState": "DONE",  
  "requestElementId": "{eid}",  
  "resultExternalDataIds": {resultElementId},  
  "versionId": null,  
  "workspaceId": "{wid}",  
  "documentId": "{did}",  
  "resultElementIds": {resultElementId},  
  "resultDocumentId": "{did}",  
  "failureReason": null,  
  "resultWorkspaceId": "{wid}",  
  "name": "GEARBOX_CHUCK",  
  "id": "{translationId}",  
  "href": "https://cad.onshape.com/api/v9/translations/{translationId}"  
}  
```
6. Once `requestState=DONE`, the JSON is uploaded to the Onshape document in a new element (tab). The element ID of the JSON blob will either appear in the `resultExternalDataIds` or `resultElementIds` field in the response.
7. Now, we can call [BlobElement/downloadFileWorkspace](https://cad.onshape.com/glassworks/explorer/#/BlobElement/downloadFileWorkspace) to retrieve the exported results.  
```  
curl -X 'GET' \  
'https://cad.onshape.com/api/v6/blobelements/d/{did}/w/{wid}/e/{resultElementId}' \  
-H 'Authorization: Basic CREDENTIALS' \  
  -H 'accept: application/octet-stream'  
```  
   * Use the `{resultElementId}` value from the translation response as the element ID. Do not include the curly braces in your call.  
   * Note that you can also open your document, click the `GEARBOX_CHUCK.JSON` tab, and download the file from there.

#### Import Examples

##### Import a Parasolid file as a Part

In this example, we’ll import the _FLYWHEEL_ part from the _CRANK.x\_t_ file we created in the [Export a Part to Parasolid](#export-a-part-to-parasolid) example.

1. Open or create a new Onshape document in which to import the Part. Make a note of the documentId and workspaceId of your document.
2. Validate that Parasolid is a supported export file type for imports by calling [Translation/getAllTranslatorFormats](https://cad.onshape.com/glassworks/explorer/#/Translation/getAllTranslatorFormats) and confirming that `validSourceFormat=true` for `translatorName=parasolid`.  
**request**  
```  
curl -X 'GET' \  
'https://cad.onshape.com/api/v6/translations/translationformats' \  
  -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS'  
```  
**response**  
```  
[  
  {  
    "validSourceFormat": true,  
    "validDestinationFormat": true,  
    "name": "PARASOLID",  
    "translatorName": "parasolid",  
    "couldBeAssembly": true  
  }  
]s  
```
3. Initialize the import by calling [Translation/createTranslation](https://cad.onshape.com/glassworks/explorer/#/Translation/createTranslation). In this example, the filename is `CRANK.x_t`.  
```  
curl -X 'POST' \  
'https://cad.onshape.com/api/v6/translations/d/{did}/w/{wid}' \  
  -H 'accept: application/json;charset=UTF-8; qs=0.09's \  
  -H 'Authorization: Basic CREDENTIALS' \  
  -H 'Content-Type: multipart/form-data' \  
  -F 'formatName=' \  
  -F 'flattenAssemblies=true' \  
  -F 'translate=true' \  
  -F 'file=@/pathToFile/CRANK.x_t'  
```  
   * Replace `{did}` and `{wid}` in the URL with the document and workspace IDs for the document you want to import the part to.  
   * Note that when using cURL, you must begin the path to the file with an `@` symbol.  
   * Note that the API takes a JSON as part of the request body, in which you can specify options for the import.  
   * When importing files, the API assumes we are importing to the `ONSHAPE` file type. You can override this and import to a different file type using the `formatName` field. In this case, we can leave the `formatName` field blank to import to the `ONSHAPE` file type.
4. Get the `translationId` from the `id` field in the response:  
```  
{  
  "requestState": "ACTIVE",  
  "requestElementId": "{eid}",  
  "resultExternalDataIds": null,  
  "versionId": null,  
  "workspaceId": "{wid}",  
  "documentId": "{did}",  
  "resultElementIds": null,  
  "resultDocumentId": "{did}",  
  "failureReason": null,  
  "resultWorkspaceId": "{wid}",  
  "name": "GEARBOX_CHUCK",  
  "id": "{translationId}",  
  "href": "https://cad.onshape.com/api/v9/translations/{translationId}"  
}  
```
5. Next, poll the [Translation/getTranslation](https://cad.onshape.com/glassworks/explorer/#/Translation/getTranslation) response until `requestState` changes from `ACTIVE` to `DONE` or `FAILED`.  
```  
{  
  "requestState": "DONE",  
  "requestElementId": "{eid}",  
  "resultExternalDataIds": {resultExternalDataId},  
  "versionId": null,  
  "workspaceId": "{wid}",  
  "documentId": "{did}",  
  "resultElementIds": null,  
  "resultDocumentId": "{did}",  
  "failureReason": null,  
  "resultWorkspaceId": "{wid}",  
  "name": "GEARBOX_CHUCK",  
  "id": "{translationId}",  
  "href": "https://cad.onshape.com/api/v9/translations/{translationId}"  
}  
```
6. Once `requestState=DONE`, we can view the imported file as a Part in our Onshape document. The `FLYWHEEL` part appears in a new PartStudio named `CRANK` in our document.

#### Additional Examples

##### Use an export rule

This example duplicates a previous one, but with the addition of an export rule. Refer to the [Export a Part Studio to ACIS](https://onshape-public.github.io/docs/api-adv/translation/docs/api-adv/translation#export-a-part-studio-to-acis) example as needed.

1. Create an export rule in Onshape for all Part Studios exported to ACIS. The translation endpoint response will include an `exportRuleFileName` value that matches the **Convention** you set for the export rule (e.g., `Onshape Export - ${name}`, which will append the Part Studio’s name to the “Onshape Export” prefix"). See the [Help docs](https://cad.onshape.com/help/Content/Plans/preferences.htm#proco-export-rules) for more information on export rules.
* Please note that using an export rule does not update the exported file name; you’ll need to manually point to the `exportRuleFileName` to use that string as the file name if so desired.
1. Call the [PartStudio/createPartStudioTranslation](https://cad.onshape.com/glassworks/explorer/#/PartStudio/createPartStudioTranslation) endpoint.  
```  
curl -X 'POST' \  
'https://cad.onshape.com/api/v6/partstudios/d/e60c4803eaf2ac8be492c18e/w/d2558da712764516cc9fec62/e/6bed6b43463f6a46a37b4a22/translations' \  
 -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
 -H 'Authorization: Basic CREDENTIALS' \  
 -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
 -d '{  
      "formatName": "ACIS",  
      "evaluateExportRule": true,  
      "storeInDocument": false,  
      "translate": true  
 }'  
```  
   * Note that the API takes a JSON as part of the request body, in which you can specify options for the export.  
   * A `formatName` string must be specified that matches one of the valid formats you found in the first step. In this example, we set `formatName` to `ACIS.`  
   * We want to apply our export rule to the export, so we set `evaluateExportRule` to `true`.  
   * We want to export this to a new file, so we’ll leave `storeInDocument` set to `false`.
2. Execute the call and view the response. You can see that the `exportRuleFileName` field is correctly set to `Onshape Export - CRANK`.  
```  
{  
  "failureReason": null,  
  "resultElementIds": null,  
  "resultDocumentId": "e60c4803eaf2ac8be492c18e",  
  "resultWorkspaceId": "d2558da712764516cc9fec62",  
  "requestState": "ACTIVE",  
  "requestElementId": "6bed6b43463f6a46a37b4a22",  
  "resultExternalDataIds": null,  
  "versionId": null,  
  "workspaceId": "d2558da712764516cc9fec62",  
  "documentId": "e60c4803eaf2ac8be492c18e",  
  "exportRuleFileName": "Onshape Export - CRANK",  
  "name": "CRANK",  
  "id": "{translationId}",  
  "href": "https://cad.onshape.com/api/v9/translations/{tid}"  
}  
```

##### Export a configured part

See the [Configurations API Guide](https://onshape-public.github.io/docs/api-adv/translation/docs/api-adv/configs) for examples.

#### Additional Resources

* [Onshape Help: Translation](https://cad.onshape.com/help/Content/translation.htm)
* [Onshape Help: Webhooks](https://cad.onshape.com/help/Content/Plans/webhooks.htm)
* [API Guide: Webhook Notifications](https://onshape-public.github.io/docs/api-adv/translation/docs/app-dev/webhook)
* [API Explorer](https://onshape-public.github.io/docs/api-adv/translation/docs/api-intro/explorer)

---

<a id="sec-app-development"></a>
## App Development

<a id="pg-docs-app-dev"></a>
### App Development

_Source: <https://onshape-public.github.io/docs/app-dev/>_

The primary APIs provided by Onshape are REST interfaces that can be accessed over HTTPS. The client can be a web server or a desktop application (including command line tools, such as curl). Onshape does not support use of the APIs directly from a browser client due to cross-domain scripting concerns.

Partner applications typically interact with Onshape in three ways:

* **File Exchange**: Onshape provides extensive import and export translation capabilities to interact with applications that can read or write a variety of file formats.
* **Live Link Integration**: Desktop or server applications can use REST calls to read information from the Onshape servers and store information back. These applications can gain “cloud value” by using Onshape data management capabilities for sharing, versioning, and durability.
* **In-Tab Integration**: Web server applications can create a tightly integrated experience within Onshape by using a combination of REST and client-side APIs to build a seamless interaction by interacting with users inside an Onshape tab.

The following diagram illustrates basic desktop integration and cloud integration architecture:

![images](https://onshape-public.github.io/docs/app-dev/images/apioverviewimage00.png)

The Onshape Server Stack consists of several cooperating servers that provide the underlying support for the Onshape CAD experience. The Onshape servers are built with a variety of technologies, including Java and C++, database and message services, geometry and constraint management systems, and much more.

Partner cloud applications can be written in any web framework. Onshape provides a set of sample apps in [Github](https://github.com/onshape-public), as well as [text tutorials](https://onshape-public.github.io/docs/app-dev/docs/tutorials).

#### Create an application

> **Note**
> 
> These steps are for creating a private application on a personal account. To create an internal application for a company, classroom, or enterprise, see [Enterprise Settings: Developer](https://cad.onshape.com/help/Content/Plans/enterprise%5Fsettings%5Fdeveloper.htm).

1. For personal accounts, go to the dev portal: <https://cad.onshape.com/appstore/dev-portal>.
2. Click **OAuth applications** in the sidebar.
3. Click the **Create new OAuth application** button.  
![Create an application in the dev portal](https://onshape-public.github.io/docs/app-dev/images/create-app-01.png)
4. Fill out the form:  
![Create an application form in the dev portal](https://onshape-public.github.io/docs/app-dev/images/oauth-create-02.png)  
   * **Name**: Application name  
   * **Primary format**: com.example.example  
   * **Summary**: Brief summary of the app  
   * **Redirect URLs**: URL of the app landing page  
   * **Permissions**: Select the applicable permissions  
   * **OAuth URL**: URL for the OAuth login. All apps submitted to the App Store for public use _must_ use [OAuth2](https://onshape-public.github.io/docs/app-dev/docs/auth/oauth)
5. Click **Create application**.
6. A window opens with your OAuth key and secret. You cannot find this secret again, so store it securely.

Next, see:

1. [OAuth2](https://onshape-public.github.io/docs/app-dev/docs/auth/oauth) \- Public applications submitted to the App Store _must_ authenticate with OAuth2.
2. [Extensions](https://onshape-public.github.io/docs/app-dev/docs/app-dev/extensions) \- Add apps directly to the Onshape UI.
3. [Create an App Store entry](https://onshape-public.github.io/docs/app-dev/docs/app-store/#create-an-app-store-entry) \- Submit your app to the Onshape App Store for public use.

#### Integration considerations

There is much to Onshape that is different from traditional CAD and PDM systems. For system integrators who have previous experience with these types of systems, the instinct is to try and apply the concepts developed for those integrations to an Onshape integration. This is a mistake. Applying existing integration concepts to Onshape simply won’t work.

Key Onshape integration considerations include:

1. **Do not limit the capabilities of the software**: When applying integration practices of legacy file-based solutions to Onshape, you must adjust the way designers work in Onshape to accommodate the limitations of your integration. Instead, the integration should follow best practices and methodologies that can be applied to modern SaaS-based solutions.
2. **Enable designers the freedom to work without constraints**: Designers working in a CAD system should never be restricted in their ability to use the software features to the fullest. The software is designed to provide its users with the freedom to innovate and the flexibility to adjust to how a designer wants to work.
3. **Utilize the best in class features from each solution**: Different software solutions are designed to provide features that should provide expected functionality for whatever function the software was designed to do. For instance, a CAD system should have best-in-class tools for modeling, whereas data management tools should provide capabilities to manage, analyze and report on data. While there might be overlap between systems, it is best practice to let each software solution do exactly what it was designed to do, instead of forcing one to perform the functions of the other.
4. **Map out your business processes**: Decide which software solution is responsible for which part of the process. It will be impossible to develop a successful integration if the requirements aren’t clearly stated. The business process(es) that you manage through the integration should be mapped out, along with the systems involved and which system is responsible for which function.
5. **Use standards and Published APIs**: Developers hate when thousands of lines of code and days of work are thrown away because of an upgrade of a piece of software. By using industry standards and published APIs, you will protect yourself from such a disaster.

#### Resources

* The Developer Portal is your place to create and administer applications: <https://cad.onshape.com/appstore/dev-portal>
* Find Onshape documentation at: <https://cad.onshape.com/help/Content> (or at `https://<companyName>.onshape.com/help/Content` for Enterprise accounts.)
* Find developer documentation on this site. We specifically recommend reviewing the following sections:  
   * [Introduction to the Onshape REST API](https://onshape-public.github.io/docs/app-dev/docs/api-intro)  
   * [Onshape App Development](https://onshape-public.github.io/docs/app-dev/docs/app-dev)  
   * [Onshape App Store](https://onshape-public.github.io/docs/app-dev/docs/app-store)
* Find sample apps: <https://github.com/onshape-public>
* Speak to other developers in the forum: <https://forum.onshape.com/categories/developer-community>

---

###### [Extensions](https://onshape-public.github.io/docs/app-dev/docs/app-dev/extensions/)

###### [Client Messaging](https://onshape-public.github.io/docs/app-dev/docs/app-dev/clientmessaging/)

###### [Structured Storage](https://onshape-public.github.io/docs/app-dev/docs/app-dev/structuredstorage/)

###### [Webhooks](https://onshape-public.github.io/docs/app-dev/docs/app-dev/webhook/)

---

<a id="pg-docs-app-dev-clientmessaging"></a>
### Client Messaging

_Source: <https://onshape-public.github.io/docs/app-dev/clientmessaging/>_

Application extensions and the Onshape JavaScript web client need to communicate directly, calling across the iframe containing the application extension using post message.![image alt text](https://onshape-public.github.io/docs/app-dev/clientmessaging/images/extension-right-panel-02.png)

---

#### Message initiation

Onshape client messaging can be split into those that are initiated from the _application extension_ and those that are initiated from the _Onshape client_.

##### Messages from the extension

These client messages can be initiated from the application extension:

* **Click/close flyouts events**: Notify the Onshape client that the user has clicked in the application extension, which should cause Onshape flyouts (versions, history, uploads, etc.) and dropdown menus (profile dropdown menu, document menu) to close. Without this, flyouts and menus might remain open over the application extension.
* **Shortcut keyboard events**: Shortcut keys (such as `?`, which opens the Onshape Help dialog), can be handled by the application extension by posting a message to the Onshape client to open the dialog.
* **keepAlive**: Notify the Onshape client that the user is actively working in the application extension, which triggers the Onshape client to send a message to the server to keep the browser session alive. Without this, the Onshape browser session will timeout and ask the user to sign in again.
* **Standard Onshape dialogs**: Request from the application extension to the Onshape client to open one of the Onshape standard dialogs and send the user’s choices back to the application extension. For example, if the application extension needs the user to choose a part or assembly to be operated on, the application extension can post a message to the Onshape client requesting that dialog be opened and the selected part or assembly information sent back to the application extension.
* **UI customization**": Request from the application extension to the Onshape client to customize the Onshape UI (e.g., add commands to menus, add buttons to the toolbars, etc). When these commands or toolbar buttons are clicked, the Onshape client posts a message to the application extension with the available context.  
   * **Note**: This is limited to cases where the application extension is made active by the user; application extensions are not automatically loaded when a document is opened. Most UI customizations should be done when you register the application with Onshape, as those change the Onshape client automatically without needing to load the application extension first.
* **Content/material insertion**: Request from the application extension to insert content into the Onshape document. For example, insert a part into a new or existing Part Studio, apply a material to a part, add a material to a material library, etc.

##### Messages from Onshape

The following messages can be initiated from the Onshape client:

* **User action notification**: The Onshape client can notify an application extension when various user actions occur. For example, the Onshape client might notify when the user has made the application extension active or inactive (when the user clicks on document tabs). When an application extension is made inactive, it is moved off the edges of the browser, so it cannot be seen, but is still active, preserving its state.
* **Printing**: The Onshape client can notify an application extension when the user has chosen the **Print** command from the main Onshape document menu, enabling the application extension to perform a print operation.

---

#### Security considerations

To ensure security, an application extension must:

* **Parse for document, workspace, and element IDs**: Parse for the `documentId`, `workspaceId`, and `elementId` that were passed as query parameters within the application extension’s iframe `src` URL. You must post these back in each `POST` message.
* **Parse for the server**: Parse for the `server` that was passed as a query parameter within the application extension’s iframe `src` URL. You must use this to validate messages received.  
   * If the application extension uses a JavaScript library or framework (e.g., BackboneJS or AngularJS), it can parse the query parameters and maintain state in other ways.
* **Not redirect to another base URL**: The browser tells the Onshape client the origin base URL from which a `POST` message is received. The Onshape client ignores messages posted from an origin URL that doesn’t match the original iframe `src` URL. It is _extremely important_ to the security of your application that you verify that the origin of all messages you receive is the same as the original server query parameter in the iframe `src` (i.e., `if (server === e.origin)`). In production operation especially, the message IS NOT SAFE if the message origin does not match the iframe `src` server query parameter. Application extensions should not redirect to another base URL after the iframe has been opened, or the messages will be ignored.
* **Post a message on startup**: Onshape will not post messages until a newly started application extension has first posted a valid message to Onshape. This constraint is in effect anytime an application extension is (re)started and exists to avoid posting messages to application extensions that are not ready to handle them, are not fully loaded, etc. After your application extension is fully loaded and ready to receive messages, post a message to Onshape. A `keepAlive` message is a great first message to send to Onshape. Once Onshape receives a valid message, Onshape will start posting messages to the application extension. If the application extension later sends an invalid message Onshape will stop sending messages until a valid message is posted to Onshape.

`POST` messages submitted by application extensions to Onshape will be ignored if any of the following are true:

* The documentId, workspaceId, or elementId are missing or not valid.
* The message name is missing or not recognized.
* The origin of the `POST` message does not match the original iframe `src` URL.

---

#### Extension types

All [Security Considerations](#security-considerations) above apply to both Element tab and Element right panel extensions, with the following notes:

* Initial message from the application extension to the Onshape client, in the form of an `applicationInit` message (or one of any other messages supported by the element right panel extensions), is required to ensure the Onshape client does not send messages to the extension until it is ready.
* Once a valid `applicationInit` message is received by the Onshape client, it will start sending messages with the `messageName` value `SELECTION` upon user selection interactions.
* Prior to accepting _any_ message from the Onshape client as secure, the `origin` attribute value included in incoming messages must be validated as equal to the original `server` query parameter value used to load the application extension.

---

##### Element tab extensions

Messages may be sent and received by element tab application extensions. This is the menu option for `+ menu -> Add application` inside a document . After menu click, a new tab will be created with the action url associated with this extension.

![image alt text](https://onshape-public.github.io/docs/app-dev/clientmessaging/images/extension-tab-01.png)

###### Sent

The following messages can be _sent_ by Element tab application extensions:

| **Message name (case sensitive)** | **Additional properties**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | **Notes**                                                                                                                                                                                                                                |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| applicationInit                   | notifyWhenSaveRequired: Whether Onshape should send a notification to save pending changes during certain operations. (default: false)                                                                                                                                                                                                                                                                                                                                                                                                                                 | Send once on application startup.                                                                                                                                                                                                        |
| closeFlyoutsAndMenus              | Send when a mouse click or other event happens in the application extension. Closes Onshape flyouts and dropdown menus.                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                          |
| closeSelectItemDialog             | Closes the select item dialog.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                          |
| connectionLost                    | Displays the standard Onshape connection lost message in a message bubble, forcing the user to either reload the document or return to the documents page.                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                          |
| errorReload                       | message: your message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Similar to the connectionLost message, but enables an application to specify the first part of the message, which will be used instead of "Onshape is not connected." The user must reload the document or return to the documents page. |
| finishedSaving                    | messageId: the id sent in the corresponding saveChanges message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Response to a saveChanges message sent from Onshape. Should be sent after application has cleaned up any pending edits.                                                                                                                  |
| keepAlive                         | Send periodically while while the user is actively working to avoid the session from timing out.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                          |
| saveAVersion                      | Send when the user types Shift-S in the application extension, the keyboard shortcut for save a version.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                          |
| showKeyboardShortcutsHelp         | Send when the user types ? (Shift-? on most keyboards) in the application extension, the keyboard shortcut for the keyboard shortcuts help dialog.                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                          |
| showMessageBubble                 | message: your message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Send when you want to show a string in the message bubble at the top of the Onshape app.                                                                                                                                                 |
| startLoadingSpinner               | message: your message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Send to start a large spinner in the middle of the browser window with your message underneath it.                                                                                                                                       |
| stopLoadingSpinner                | Send to stop the large spinner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                          |
| startWorkingSpinner               | Send to start a small spinner in the middle bottom of the browser window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                          |
| stopWorkingSpinner                | Send to stop the small spinner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                          |
| openSelectItemDialog              | dialogTitle: your dialog title (default="")selectBlobs: true or false (default)selectParts: true or false (default)selectPartStudios: true or false (default)selectAssemblies: true or false (default)selectMultiple: true or false (default)selectBlobMimeTypes: comma-delimited string of blob mime types to show in dialog (e.g. “application/dwt,application/dwg”); (default="")showBrowseDocuments: Whether "Other documents" choice should be available (default=true)showStandardContent: Whether "Standard content" choice should be available (default=false) | Send when your application wants to open a dialog in which the user will select one or multiple items - blobs, parts, part studios or assemblies.                                                                                        |
| requestCameraProperties           | graphicsElementId: string, element ID of the part studio or assembly                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Send to request camera properties of a specific part studio or assembly element. Note: The element should have been opened at least once in the current session. The messageName of the response is cameraProperties.                    |

###### Received

The following messages can be _received_ by Element tab application extensions:

| **Message name (case sensitive)** | **Additional properties**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | **Notes**                                                                                                                                                                                                         |            |                                                                                                                        |                                                                                                                                                                                                                                                            |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| show                              | Sent when an element tab application extension is shown (made active) within the Onshape client. This message is NOT sent when the element tab application extension is created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                   |            |                                                                                                                        |                                                                                                                                                                                                                                                            |
| hide                              | Sent when an element tab application extension is made inactive within the Onshape client. This message is NOT sent when an element tab application extension is deleted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                   |            |                                                                                                                        |                                                                                                                                                                                                                                                            |
| itemSelectedInSelectItemDialog    | documentId: ID of selected item’s documentworkspaceId: ID of selected item’s workspace; empty if versionId is not empty.versionId: ID of selected item’s version; empty if workspaceId is not empty.elementId: ID of element selected or containing the selected part.elementName: Name of element selected or containing the selected part.elementType: Type of element selected or containing the selected part partstudio \| assembly                                                                                                                                                                                                                                         | blobelementMicroversionId: Microversion id of the elementitemType: Type of item selected: part                                                                                                                    | partStudio | assemblypartName: Name of part selected; empty if itemType is not partidTag: ID of part; empty if no part is selected. | Sent when the user selects an item (blob, part, part studio or assembly) in the select item dialog that was opened due to an openSelectItemDialog message sent earlier. When a part is not selected, the partXxx message properties will be empty strings. |
| print                             | Sent when the user chooses the Print command while the application is the active element. The application can choose to handle this as either a print or an export to a PDF or other format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                   |            |                                                                                                                        |                                                                                                                                                                                                                                                            |
| selectItemDialogClosed            | Sent when the select item dialog closes, either because the user selected an item and selectMultiple is false, or the user changed the active element or the user closed the dialog with the "X" button.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                   |            |                                                                                                                        |                                                                                                                                                                                                                                                            |
| startFirstViewCommand             | documentId: ID of selected item’s documentworkspaceId: ID of selected item’s workspace; empty if versionId is not empty.versionId: ID of selected item’s version; empty if workspaceId is not empty.elementId: ID of element selected or containing the selected part.elementName: Name of element selected or containing the selected part.elementType: Type of element selected or containing the selected part partstudio \| assembly                                                                                                                                                                                                                                         | blobelementMicroversionId: Microversion id of the elementitemType: Type of item selected: part                                                                                                                    | partStudio | assemblypartName: Name of part selected; empty if itemType is not partidTag: ID of part; empty if no part is selected. | Sent to a drawings application extension when the drawing is created with zero views.                                                                                                                                                                      |
| export                            | fileExtension: the file extension of the export type the user chose: .dwg \| .dxfbaseFileName: the base portion of the expected output file. Default: “{documentName} - {elementName}”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Sent when the user chooses a command to export the contents of the application to a file.                                                                                                                         |            |                                                                                                                        |                                                                                                                                                                                                                                                            |
| cameraProperties                  | graphicsElementId: string; Element ID of the part studio or assemblyisValid: boolean; Indicates if the properties are valid or not. false if element ID is invalid or element has not been open in the current sessionprojectionType: string; Denotes the projection method. Values are ‘orthographic’, ‘perspective’ . Empty string ‘’ if isValid is falseviewMatrix: 16 element numeric matrix with elements at index 13, 14, 15 corresponding to position of the cameraprojectionMatrix: 16 element numeric matrixverticalFieldOfView: number; 0 in case of orthographic projectionviewportHeight: number; height of the viewportviewportWidth: number; width of the viewport | Sent when application posts a requestCameraProperties message                                                                                                                                                     |            |                                                                                                                        |                                                                                                                                                                                                                                                            |
| takeFocus                         | Sent when the Onshape client sets focus on the content window of the element tab application extension.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                   |            |                                                                                                                        |                                                                                                                                                                                                                                                            |
| saveChanges                       | messageId: a unique identifier for this message. Should be passed back in the finishedSaving message.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Sent if the application specified notifyWhenSaveRequired in the applicationInit message. Indicates that the application should cleanup any pending edits before an Onshape process continues (i.e. version save). |            |                                                                                                                        |                                                                                                                                                                                                                                                            |

---

##### Element right panel extensions

Most client messaging functionality had been limited to that occurring between the Onshape client and application elements (the **Element tab** location). Limited functionality in now also available for client messaging to work with application extensions in the **Element right panel** location. This is the panel inside a document. It currently houses the BOM, configurations, etc. Applications can use this extension location to add items in this panel.

![image alt text](https://onshape-public.github.io/docs/app-dev/clientmessaging/images/extension-right-panel-02.png)

Contexts:

* Part Studio
* Assembly
* Document

The following messages are supported by Element Right Panel application extensions:

| Message name (case sensitive)        | Properties                        | Notes                                                                                                                                                                                                                                      |
| ------------------------------------ | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| showMessageBubble                    | message: string                   | Display a string in the blue message bubble at the top of the application extension.                                                                                                                                                       |
| applicationInit                      | Send once on application startup. |                                                                                                                                                                                                                                            |
| requestViewerImage                   | width?: numberheight?: number     | Take a screenshot of the current window at the provided image size.                                                                                                                                                                        |
| requestSelection                     |                                   |                                                                                                                                                                                                                                            |
| requestSelectionHighlight            |                                   |                                                                                                                                                                                                                                            |
| stopRequest                          |                                   |                                                                                                                                                                                                                                            |
| openAnotherElementInCurrentWorkspace | anotherElementId: string          | Specify the ID of the element to open.                                                                                                                                                                                                     |
| openFeatureDialog                    | featureId: string                 | Call [PartStudio/getPartStudioFeatures](https://cad.onshape.com/glassworks/explorer/#/PartStudio/getPartStudioFeatures) or [Assembly/getFeatures](https://cad.onshape.com/glassworks/explorer/#/Assembly/getFeatures) to get the featureId |
| closeFeatureDialog                   | accept: boolean                   | accept=true mimics closing the dialog by clicking the green check mark or Accept button. accept=false mimics closing the dialog by clicking the X or Cancel button.                                                                        |

---

#### Code snippets

##### Parse query parameters

This JavaScript code parses the iframe `src` query parameters and uses them to post a message:

`  var documentId;
  var workspaceId;
  var elementId;
  var server;

  // Parse query parameters
  var queryParameters = decodeURIComponent(window.location.search.substr(1));
  var queryParametersArray = queryParameters.split('&');
  for (var i = 0; i < queryParametersArray.length; i++) {
    var parameterArray = queryParametersArray[i].split('=');
    if (parameterArray.length === 2) {
      switch (parameterArray[0]) {
        case 'documentId':
          documentId = parameterArray[1];
          break;
        case 'workspaceId':
          workspaceId = parameterArray[1];
          break;
        case 'elementId':
          elementId = parameterArray[1];
          break;
        case 'server':
          server = parameterArray[1];
          break;
      }
    }
  }

  // Listen for clicks and post a message to the Onshape client
  document.getElementById('<id of your topmost element>').
    addEventListener('click', function() {
      var message = {documentId: documentId,
                     workspaceId: workspaceId,
                     elementId: elementId,
                     messageName: 'closeFlyoutsAndMenus'};
      window.parent.postMessage(message, '*');
    }, true);
`

##### Create a message object

The message object posted to the Onshape client is of the form:

`{
    documentId: documentId,
     workspaceId: workspaceId,
     elementId: elementId,
     messageName: '<message name>',
    // … other properties as needed for other message types …
}
`

The message data object posted to the application extension is of the form:

`{
    messageName: '<message name>',
 //    … other properties as needed for other message types …
}
`

The message will always have a `messageName` property.

##### Listen for messages

To listen for messages from the Onshape client:

`  // server is one of the iframe src query parameters - see above

  var handlePostMessage = function(e) {
    console.log("Post message received in application extension.");
    console.log("e.origin = " + e.origin);

    // Verify the origin matches the server iframe src query parameter
    if (server === e.origin) {
      console.log("Message safe and can be handled as it is from origin '"
                  + e.origin +
                  "', which matches server query parameter '"
                  + server + "'.");
      if (e.data && e.data.messageName) {
        console.log("Message name = '" + e.data.messageName + "'");
      } else {
        console.log("Message name not found. Ignoring message.");
      }
    } else {
      console.log("Message NOT safe and should be ignored.");
    }
  };

  window.addEventListener('message', handlePostMessage, false);
`

##### Send and handle messages

The following is an example of how one might send an initialization message to, and handle post messages from, the Onshape client.

> _**Note:**_ Proper clean-up of event listeners is not included in the snippet

`` function handlePostMessage(event) {
  // ensure that the event data is from a legit source:
  if(theServerStringFromActionUrl !== event.origin) {
    console.error('origin of message is not legitimate');
    return;
  }

  // branch based on messageName attribute
  switch(event.data.messageName) {
    case 'SELECTION':
      console.debug('SELECTION event data: %o', event.data);
      break;
    default:
      console.debug(`${event.data.messageName} not handled`);
    }
}

window.addEventListener('message', handlePostMessage);

const initMessage = {
  documentId:  theDocumentId,    // required - parsed from action url
  workspaceId: theWorkspaceId,   // required - parsed from action url
  elementId:   theElementId,     // required - parsed from action url
  messageName: 'applicationInit' // required
};

window.parent.postMessage(initMessage, '*');
 ``

##### Right panel interaction sequence

The sequence diagram below illustrates the interaction between an Element right panel application extension and the Onshape client:

Application ExtensionOnshape Clientvia configured buttonloop[selection interactions]via configured buttonuserstart element right panel extensioninvoke action url (with query params)postMessage(messageName: 'applicationInit')selectpostMessage(messageName: 'SELECTION')stop element right panel extensiondestroy

##### Right panel message exchange

The following messages are exchanged for application extensions located in the element right panel and configured for Part Studio, Assembly, or Document contexts.

The first message with `messageName` attribute set to `applicationInit` is sent to the Onshape client by an application extension once it is loaded and ready to receive and process incoming messages:

`    {
        documentId: '<document id>',
        workspaceId: '<workspace id>',
        elementId: '<element id>',
        messageName: 'applicationInit'
    }
`

The values `<document id>`, `<workspace id>`, `<element id>`, and `<server id>`:

* Are originally included as query parameters in the action URL used to request the content of the application extension
* Must be included in messages sent to the Onshape client

While initialization is the specific intent of the `applicationInit` message, other supported `messageName` attributes have the same initialization effect upon their first receipt by the Onshape client.

Next, as the user interacts with Onshape by selecting various parts of the model, messages with the `messageName` attribute set to `SELECTION` are sent to the application extension:

`{
    messageName: 'SELECTION',
    selections: [
        {
            selectionType: 'ENTITY',
            selectionId: 'KRiB',
            entityType: 'FACE',
            occurrencePath: [
                'MfOieM8xKIDGHe37c'
            ],
            workspaceMicroversionId: 'a781c53fbd1095e3462d2b70'
        },
        {
            selectionType: 'ENTITY',
            selectionId: 'KRdC',
            entityType: 'EDGE',
            occurrencePath: [
                'MfOieM8xKIDGHe37c'
            ],
            workspaceMicroversionId: 'a781c53fbd1095e3462d2b70'
        }
    ]
}
`

---

#### Notes

* Keyboard focus will not be transferred to an application until the user clicks in the application or the application programmatically takes focus. An application should programmatically take focus when it is first loaded and when it receives a `show` message from Onshape. Shortcut keys will work immediately when the application is shown.
* New message types will be added as needed. If your application extension needs a message not listed in this document, please notify us, and we’ll work with you on it.
* Mobile clients are currently not supported.

---

<a id="pg-docs-app-dev-extensions"></a>
### Extensions

_Source: <https://onshape-public.github.io/docs/app-dev/extensions/>_

This page provides information for some of the more common options for embedding a third-party application into the Onshape interface. Onshape provides many options for embedding commands in various menus, fly-out panels, and elements. In this example, you will embed a custom web page inside a document’s right side fly-out panel. This interface will receive information from Onshape and push information from the panel back to Onshape, providing a complete, bi-directional integration scenario.

Please see also:

* [Create an Extension tutorial](https://onshape-public.github.io/docs/app-dev/extensions/docs/tutorials/createextension/): A step-by-step walkthrough of creating an extension.
* Create an Extension Video Sample:[![OAuth app creation video](https://onshape-public.github.io/docs/app-dev/extensions/images/ExtensionsVideoCard.png)](https://onshape.wistia.com/medias/0ivxxngkjz?embedType=async&seo=false&videoFoam=true&videoWidth=640&wvideo=0ivxxngkjz%29)

#### Extension Types

We can classify extensions into two high-level types. The first type embeds a UI _from_ the application _into_ the Onshape UI. The embedded UI is an HTTPS page displayed in an iFrame in the Onshape UI. The UI is served from the application, and can choose to make API calls to Onshape for additional information. This is exactly like the traditional tab-based applications in Onshape, except that such extensions exist at different UI locations.

The second type of extension embeds an action that calls a REST API _exposed by_ the application _from_ the Onshape UI (e.g., context menu actions and toolbar actions). These types of extensions rely on External OAuth information to authenticate and make a call where Onshape acts as a client, and the application acts as a server.

#### Extension Attributes

Each extension exists at a specific place in the Onshape UI and works with a specific context or selection. The attributes of an extension are:

1. **Name**: This should be short and explicit. It will appear in the Onshape UI as a menu item, a toolbar tooltip, a collapsed panel icon tooltip, or a panel icon. It might be truncated in the UI if it is too long.
2. **Description**: This is where the developer can record a detailed description of the extension. It does not appear in the Onshape UI, but could appear in the grant process.
3. **Location**: This describes where the extension exists in the Onshape UI. Over time, this will cover various panels in the UI, context menus, toolbars, actions in dialogs, etc. You can see the list of currently supported locations [here](#supported-locations-and-contexts).  
   * Please note that you can create only one element tab extension per application.
4. **Context** (selection): Some locations will work in the context of a selection. Let’s say the application developer wants to show some information from a third-party system, pertinent only to parts (not assemblies or drawings). In this scenario, the developer would choose a location like ‘Document list info panel’, and the context as ‘Selected part’. If the user searches for something in the document list, some documents, Part Studios, parts, and Assemblies would be returned. This extension will show up in the Info panel only if the selected entity is a part. Using context enables application developers to control when the extension is displayed. Check the list of contexts available for different locations [here](#supported-locations-and-contexts).
5. **Action URL**: Locations that embed a UI use the action URL to define the address of the page to display. The action URL is used to specify the REST endpoint if the location is an action (context menu, toolbar item, action in dialog etc.) and the action type is GET or POST. If the location is an action and the action is ‘Open in new window’, the action URL is the URL to open in the new window.  
The action URL can be parameterized to pass information from Onshape to the application. The action URL replaces attributes in the format {$attribute} with the appropriate value. These attributes can be used to identify the selected entity and/or make calls back to Onshape via the API. The currently supported attributes are:  
   * `{$documentId}` \- The Onshape ID for the current or selected document.  
   * `{$workspaceOrVersion}` \- This will be either `w` or `v` for workspace or version respectively depending on current opened document state or selection.  
   * `{$workspaceOrVersionId}` \- The Onshape ID for the current or selected workspace or version.  
   * `{$workspaceId}` \- Use `{$workspaceOrVersionId}` instead.  
   * `{$versionId}` \- Use `{$workspaceOrVersionId}` instead.  
   * `{$microversionId}` \- The Onshape ID for the current or select document microversion.  
   * `{tabElementId}` \- The Onshape ID for the current tab.  
   * `{$elementId}` \- The Onshape ID for the current or selected element.  
   * **Note**: In most cases, `tabElementId` and `elementId` will be the same. However, when creating an extension with the `Selected instance` context, `tabElementId` indicates the current tab (i.e., the target element), and `elementId` indicates the tab from which the instance/subassembly was inserted (i.e., the source element).  
   * `{$partId}` \- The Onshape ID for the current or selected part.  
   * `{$partNumber}` \- The Part number property for the current or selected part, assembly or drawing.  
   * `{$revision}` \- The Revision property for the current or selected part, assembly or drawing.  
   * `{$companyId}` \- The ID for the company that owns the document.  
   * `{$mimeType}` \- The mime type if the current or selected element is a blob.  
   * `{$featureId}` \- In case of feature selected in the Feature list in a Part Studio.  
   * `{$nodeId}` \- In case of mate or mate feature selected in the Assembly list.  
   * `{$occurrencePath}` \- In case of part instances, mates, mate connectors and sub assemblies.  
   * `{$configuration}` \- In case of extensions inside the document, this attribute will be replaced by current element active configuration.  
   * `{$sessionCompanyId}` \- The company ID for the signed-in user’s session.

The attributes can exist as path parameters or query parameters or attributes in the POST body. For example:

```
[https://whispering-sea-42267.herokuapp.com/oauthSignin?documentId={$documentId}&workspaceOrVersion={workspaceOrVersion}&workspaceOrVersionId={$workspaceOrVersionId}&elementId={$elementId}&partId={$partId}&server=https://cad.onshape.com&companyId=cad&userId=5f1eba76c14a434817d9c588&locale=en-US](https://whispering-sea-42267.herokuapp.com/oauthSignin?documentId=%7B$documentId%7D&workspaceId=%7B$workspaceId%7D&elementId=%7B$elementId%7D&partId=%7B$partId) 

```

or

```
[https://cad.onshape.com/api/partstudios/d/{$documentId}/{$workspaceOrVersion}/{$workspaceOrVersionId}/e/{$elementId}/stl?server=https://cad.onshape.com&companyId=cad&userId=5f1eba76c14a434817d9c588&locale=en-US](https://cad.onshape.com/api/partstudios/d/%7B$documentId%7D/w/%7B$workspaceId%7D/e/%7B$elementId%7D/stl) 

```

The attributes available for replacement differ by location and context selection. You can see the available attributes for each location [here](#supported-locations-and-contexts).

The **timeout** for `action_url` of type `GET` or `POST` is **180 seconds**.

1. **Action type**: The action type is only applicable for locations that act as actions and not for locations that embed UIs. Check if action type is valid for a location [here](#supported-locations-and-contexts). The supported action types are:  
   * `GET` \- This makes a GET API call using the action URL. Parameter replacement is done on the action URL.  
   * `POST` \- This makes a POST API call using the action URL and the action body as the post body. Parameter replacement is done on both the action URL and the action body.  
   * `Open in new window` \- This opens the action URL in a new browser window. Parameter replacement is done on the action URL.
2. **Action body**: This is only applicable if the action type is POST. The action body is passed in a POST API call and must be in a valid json format.
3. **Show response**: This is only applicable if the action type is GET or POST. If this is checked, the UI will wait for a response and show the response in a dialog in the UI. The response must be in a valid json format.
4. **Icon**: The icon will be shown where the extension exists. This can be an icon in an Info panel, context menu action, toolbar button, action button in a dialog, or other supported locations.

#### Supported Locations and Contexts

This is the list of supported locations, their valid contexts, and whether they support action types.

##### Element context menu

This is the context menu for elements.

![image alt text](https://onshape-public.github.io/docs/app-dev/extensions/images/extensionsimage04.png)

Supported contexts:

* `Part Studio`
* `Assembly`
* `Drawing`
* `Blob element`

Supported parameters for replacements:

* `{$documentId}`
* `{$workspaceOrVersion}`
* `{$workspaceOrVersionId}`
* `{$workspaceId}` DEPRECATED
* `{$versionId}` DEPRECATED
* `{$elementId}`
* `{$partNumber}`
* `{$mimeType}`
* `{$configuration}`

Default parameters as query string:

* `server`
* `companyId` \- Default value is ‘cad’. If the document owner is company/enterprise, then the value is company/enterprise ID.
* `userId`
* `locale`
* `clientId`

This location supports action types.

##### Tree context menu

This is the context menu for the part tree, assembly tree and feature tree in part studios.

![image alt text](https://onshape-public.github.io/docs/app-dev/extensions/images/extensionsimage05.png)

Supported contexts:

* `Part`
* `Sub assembly`
* `Feature`
* `Mate`
* `Mate feature`
* `Instance`

Supported parameters for replacement:

* `{$documentId}`
* `{$workspaceOrVersion}`
* `{$workspaceOrVersionId}`
* `{$workspaceId}` DEPRECATED
* `{$versionId}` DEPRECATED
* `{$elementId}`
* `{$partId}` (`Part` and `Instance` contexts only)
* `{$partNumber}`
* `{$revision}`
* `{$featureId}`
* `{$nodeId}`
* `{$occurrencePath}`
* `{$configuration}`

Default parameters as query string:

* `server`
* `companyId` \- Default value is ‘cad’. If the document owner is company/enterprise, then the value is company/enterprise ID.
* `userId`
* `locale`
* `clientId`

This location supports action types.

##### Document list context menu

This the context menu available on items in the document list. This is normally documents but can be multiple types based on search results.

![image alt text](https://onshape-public.github.io/docs/app-dev/extensions/images/extensionsimage06.png)

Supported contexts:

* `Part`
* `Document`
* `Part Studio`
* `Assembly`
* `Drawing`
* `Blob element`

Supported parameters for replacement:

* `{$documentId}`
* `{$workspaceOrVersion}`
* `{$workspaceOrVersionId}`
* `{$workspaceId}` DEPRECATED
* `{$versionId}` DEPRECATED
* `{$elementId}`
* `{$partId}` (`Part` context only)
* `{$partNumber}`
* `{$revision}`
* `{$configuration}`

Default parameters as query string:

* `server`
* `companyId` \- Default value is ‘cad’. If the document owner is company/enterprise, then the value is company/enterprise ID.
* `userId`
* `locale`
* `clientId`

This location supports action types.

##### Document list info panel

This is the Info panel to the right in the document list. The document list normally contains documents, but can contain other entities as the result of a search.

![image alt text](https://onshape-public.github.io/docs/app-dev/extensions/images/extensionsimage07.png)

Supported contexts:

* `Part`
* `Document`
* `Part Studio`
* `Assembly`
* `Drawing`
* `Blob element`

Supported parameters for replacement:

* `{$documentId}`
* `{$workspaceOrVersion}`
* `{$workspaceOrVersionId}`
* `{$workspaceId}` DEPRECATED
* `{$versionId}` DEPRECATED
* `{$elementId}`
* `{$partId}`

Default parameters as query string:

* `server`
* `companyId` \- Default value is ‘cad’. If the document owner is company/enterprise, then the value is company/enterprise ID.
* `userId`
* `locale`
* `clientId`

This location does NOT support action types.

##### Element right panel

This is the panel inside a document. It currently houses the BOM, configurations, etc. Applications can use this extension location to add items in this panel.

![image alt text](https://onshape-public.github.io/docs/app-dev/extensions/images/extension-right-panel-02.png)

Supported contexts:

* `Part`
* `Document`
* `Part Studio`
* `Assembly`
* `Sub assembly`
* `Feature`
* `Mate`
* `Mate feature`

Supported parameters for replacement:

* `{$documentId}`
* `{$workspaceOrVersion}`
* `{$workspaceOrVersionId}`
* `{$workspaceId}` DEPRECATED
* `{$versionId}` DEPRECATED
* `{$elementId}`
* `{$partNumber}`
* `{$revision}`
* `{$featureId}`
* `{$nodeId}`
* `{$occurrencePath}`
* `{$configuration}`

Default parameters as query string:

* `server`
* `companyId` \- Default value is ‘cad’. If the document owner is company/enterprise, then the value is company/enterprise ID.
* `userId`
* `locale`
* `clientId`

This location does NOT support action types.

##### New Element tab

This is the menu option for `+ menu -> Add application` inside a document . After menu click, a new tab will be created with the action url associated with this extension.

![image alt text](https://onshape-public.github.io/docs/app-dev/extensions/images/extension-tab-01.png)

Supported contexts:

* There are no supported contexts.

Supported parameters for replacement:

* Parameter replacement not supported.

Default parameters as query string:

* `documentId`
* `workspaceId`
* `versionId`
* `elementId`
* `server`
* `companyId` \- Default value is ‘cad’. If the document owner is company/enterprise, then the value is company/enterprise ID.
* `userId`
* `locale`
* `clientId`

This location supports action types.

##### Part number generator

This extension helps partners to embed their own custom part number generation scheme in Onshape. Each application can have only one extension of this type. Once defined, these extensions are listed as one of the part numbering schemes in the release management configuration in Company settings.

![image alt text](https://onshape-public.github.io/docs/app-dev/extensions/images/extensionsimage10.png)

In the above screen shot, ‘Part number generation scheme’ is the user-defined name of the extension.

Supported contexts:

* There are no supported contexts.

Supported parameters for replacement:

* Parameter replacement is not supported.

Default parameters as query string:

* No default query parameters

Action URL defined by the user is assumed to be a POST API. This API should consume a predefined request body as shown below. This definition may have additional attributes in future.

` [
   {
           "id" : <internal part number id>,
           "documentId" : <documentId>,
           "elementId" : <elementId>,
           "workspaceId" : <workspaceId>,
           "elementType" : <elementType>,
           "partId" : <partId>,
           "companyId" : <companyId>, // Id of the company that owns the document, else the text “cad”
           "partNumber" : <current part number>,
           "configuration" : <configuration string>,
           "categories" : <array of category ids and names> // [ { "id": <String>, "name": <string> } ]
   }
 ]
`

**Note**: Categories are only passed from the Release dialog and properties dialogs for now. They are empty when part number generation is called from the BOM table or configuration table.

Expected response sent to Onshape is as follows:

` [   
   {
           "id" : <internal part number id>,
           "documentId" : <documentId>,
           "elementId" : <elementId>,
           "workspaceId" : <workspaceId>,
           "elementType" : <elementType>,
           "partId" : <partId>,
           "partNumber" : <next part number generated by third party numbering scheme>
   }
 ]
`

Third-party applications can simply fill the `"partNumber"` attribute with the part number generated by the custom numbering scheme and send it as a response. However, the response should at least contain `"id"` and `"partNumber"` as highlighted above; other attributes are optional.

Custom numbering schemes for part generation, once set in the Release management page, can be invoked from all the places where we set part numbers, including the Release candidate dialog shown below:

![image alt text](https://onshape-public.github.io/docs/app-dev/extensions/images/extensionsimage11.png)

#### Sample code

We have provided a sample application that supports the features described in this document.

The source code for this `Inventory management` application can be found [in our public GitHub repository](https://github.com/onshape-public/inventory-oauth2-app).

The instructions to install and the application are available in the `README.md` file in the repository.

The application is built on the Passport node module. It is based on this [article](http://scottksmith.com/blog/2014/05/02/building-restful-apis-with-node/). Please read the article before proceeding with this section.

Some structural information about the application:

* The dependencies are defined in `package.json`
* The routing for inbound calls is defined in `server.js`. This includes routing for OAuth2 calls as well as calls for the rest APIs we expose that Onshape can call via the extensions.
* The OAuth2 calls are routed to `controllers/oauth2.js`. These include calls to authenticate as calls to get the bearer token.
* `controllers/oauth2.js` uses `controllers/auth.js` to interact with Passport to manage the authentication and storage.
* Other API calls to get part number, etc, route to the appropriate controller in the controllers directory.
* The controllers use the model defined in the model directory.

The application is defined in the Developer Portal with extensions that use the exposed APIs.

The following screenshots define the base configuration of the application and some of the sample extensions.

---

<a id="pg-docs-app-dev-structuredstorage"></a>
### Structured Storage

_Source: <https://onshape-public.github.io/docs/app-dev/structuredstorage/>_

#### Sub Elements

Onshape provides application elements storage that is controlled by applications through the API. These elements allow a set of named sub-elements.

The application can make changes to sub-elements independently or in arbitrary groupings. Changes may be wholesale replacements, or may be deltas. When performing a delta update, the application may post a full version as well, which allows the api to return a smaller number of deltas for subsequent queries.

An application may need to perform multiple versionable actions in the course of performing a user-level action, and we want to allow the individual actions to be collected into a single action from the perspective of document history. We do this by providing support for creation of a private transaction and support for atomically committing the transaction to the document workspace as a single user-visible action.

Onshape does not assume any knowledge about the semantics of application deltas. All merging of deltas into a consolidated form is done by the application. Applications should typically send checkpoint state for a sub-element if many delta changes have been made since the last checkpoint.

Document content and changes are logically an array of bytes, but since they are transmitted through JSON, then are expected to be presented a Base-64 encoding of the array into string form.

We use some terminology in this document that is new.

* **changeId** \- an opaque identifier for the state of an application element. Each change to the application element results in a new changeId
* **transaction** \- a private workspace within a document workspace for composing modifications to an application element. These changes are not visible to the user until committed.
* **transaction commit** \- an operation that moves the changes performed within a transaction to the application element workspace as a single user-visible action.

**Concurrent access by multiple users**

If the element is being concurrently accessed by multiple sessions, updates may encounter conflicts during update. If the application has a mechanism that ensures that all accesses to the element are mediated by a single process, as is done with our part studio and assemblies, this can be addressed directly by the application. However, if the application is not able to mediate access in this way, updates by one session may invalidate state held by another session. We address this by notifying updaters when an update cannot be directly applied because their state is out of date and allowing them to refresh their state before re-applying the change.

This policy of requiring the application have current state when posting updates could be overly conservative in some cases. Detecting conflict at the sub-element level might provide for better concurrent access performance, but there probably are cases where this fails, so it probably would need some level of application control.

#### JSON Tree

In contrast with sub elements, JSON tree storage is a more managed data storage mechanism that Onshape itself can merge and diff. At the root of it, the data structure is a single JSON object per Application Element. The user submits incremental changes that are then applied by Onshape to the JSON tree. Onshape stores these ‘diffs’ in a new microversion created as a result of the update request, or during a subsequent transaction commit request. When the user then performs a merge or restore operation, Onshape can sum and apply the requisite incremental changes. By storing diffs, Onshape provides to the user a storage mechanism that is more robust to race conditions, since multiple simultaneous edits can be optionally merged by Onshape. All of these qualities make JSON tree a preferred way to store application element data in an Onshape-native manner.

##### JSON Tree Edit Semantics

###### BTJEdit Encoding

A JSON tree edit represents an incremental change to an application element’s JSON tree. The edit is a `BTJEdit` class, which is encoded as one of the following:

* Deletion:

`{ "btType" : "BTJEditDelete-1992", "path" : "path" }
`

* Insertion:

`{ "btType" : "BTJEditInsert-2523", "path" : "path", "value" : "newValue" }
`

* Change:

`{ "btType" : "BTJEditChange-2636", "path" : "path", "value" : "newValue" }
`

* Move:

`{ "btType" : "BTJEditMove-3245", "sourcePath" : "path", "destinationPath" : "path" }
`

* List (where edit1, edit2, etc. are zero or more edits.):

`{ "btType" : "BTJEditList-2707", "edits" : [ "edit1", "edit2", "..."] }
`

Within the above encoding, `newValue` is a stand in for any valid JSON, and `path` is a stand in for an object representing a path to the node at which to perform the edit.

###### BTJPath Encoding

The BTJPath object describes a path through the JSON tree to a particular node, and is encoded as follows:

`{ "btType" : "BTJPath-3073", "startNode" : "startNode", "path" : [ "pathElement1", "pathElement2", "..."] }
`

where startNode is a string that is either empty to specify the root node or a nodeId of a node in the tree. The pathElement is one of:

* Key:

`{ "btType" : "BTJPathKey-3221", "key" : "string" }
`

* Index:

`{ "btType" : "BTJPathIndex-1871", "index" : "integer" }
`

In the insertion and move type edits the path elements can describe a path that doesn’t currently exist. Onshape will generate the proper keys and values as needed to place the node value in the proper location.

##### JSON Tree Examples

Below are some examples that show the body required to perform the particular edit on a JSON tree.

###### Deletion Example

If the pre-existing JSON tree looks like:

`{"myKey":  "myValue"}
`

and a delete edit looks like:

`{"btType": "BTJEditDelete-1992",
     "path": {"btType": "BTJPath-3073", "startNode": "", "path": [{"btType": "BTJPathKey-3221", "key": "myKey"}]}}
`

then the resulting JSON is the result of deleting the node specified by `path`:

`{}
`

###### Insert Example

If the pre-existing JSON tree looks like:

`{}
`

and the insertion edit looks like:

`{"btType": "BTJEditInsert-2523",
     "path": {"btType": "BTJPath-3073", "startNode": "", "path": [{"btType": "BTJPathKey-3221", "key": "insertedKey"}]},
     "value": "myValue"}
`

then the resulting JSON is the result of inserting the node described by `value` at the node specified by `path`:

`{"insertedKey": "myValue"}
`

###### Change Example

If the pre-existing JSON tree looks like:

`{"myKey":  "myValue"}
`

and the change edit looks like:

`{"btType": "BTJEditChange-2636",
     "path": {"btType": "BTJPath-3073", "startNode": "", "path": [{"btType": "BTJPathKey-3221", "key": "myKey"}]},
     "value": "myOtherValue"}
`

then the resulting JSON is the result of changing the node specified by `path` to the node described by `value`:

`{"myKey":  "myOtherValue"}
`

###### Move Example

If the pre-existing JSON tree looks like:

`{"myKey":  "myValue", "myOtherKey":  "myOtherValue"}
`

and the move edit looks like:

`{"btType": "BTJEditMove-3245", "sourcePath": {"btType": "BTJPath-3073", "startNode": "",
                                                  "path": [{"btType": "BTJPathKey-3221", "key": "myKey"}]},
     "destinationPath": {"btType": "BTJPath-3073", "startNode": "",
                         "path": [{"btType": "BTJPathKey-3221", "key": "keyCreatedFromMove"}]}}
`

then the resulting JSON is the result of moving the node from the specified `sourcePath` to the `destinationPath`:

`{"keyCreatedFromMove": "myValue"}
`

###### List Example

If the pre-existing JSON tree looks like:

`{}
`

and the list edit looks like:

`{"btType": "BTJEditList-2707", "edits": [
        {"btType": "BTJEditInsert-2523", "path": {"btType": "BTJPath-3073", "startNode": "", "path": [{"btType": "BTJPathKey-3221", "key": "myKey"}]},
         "value": "myValue"},
        {"btType": "BTJEditChange-2636", "path": {"btType": "BTJPath-3073", "startNode": "",
                                                  "path": [{"btType": "BTJPathKey-3221", "key": "myKey"}]},
         "value": ["firstValue", "secondValue"]},
        {"btType": "BTJEditInsert-2523", "path": {"btType": "BTJPath-3073", "startNode": "",
                                                  "path": [{"btType": "BTJPathKey-3221", "key": "myKey"},
                                                           {"btType": "BTJPathIndex-1871", "index": 1}]},
         "value": "myBetterSecondValue"},
        {"btType": "BTJEditDelete-1992", "path": {"btType": "BTJPath-3073", "startNode": "",
                                                  "path": [{"btType": "BTJPathKey-3221", "key": "myKey"},
                                                           {"btType": "BTJPathIndex-1871", "index": 2}]}}
    ]}
`

then the resulting JSON is the result of applying all the given edits in order:

`{"myKey": ["firstValue", "myBetterSecondValue"]}
`

The intermediate steps were:

1. Insertion:  
`   {"myKey":  "myValue"}  
`
2. Change:  
`   {"myKey": ["firstValue", "secondValue"]}  
`
3. List insertion:  
`   {"myKey": ["firstValue", "myBetterSecondValue", "secondValue"]}  
`
4. List deletion:  
`   {"myKey": ["firstValue", "myBetterSecondValue"]}  
`

All the examples above were tested and validated using the Python client [here](https://github.com/onshape-public/onshape-clients/blob/next/python/test/test%5Fapp%5Felement%5Fjson%5Ftree.py).

---

<a id="pg-docs-app-dev-webhook"></a>
### Webhooks

_Source: <https://onshape-public.github.io/docs/app-dev/webhook/>_

This page describes the Webhook APIs Onshape provides for working with notifications.

Notifications are delivered to an application as an HTTP `POST` with a JSON body, which includes information about the identity of the registration request and information specific to the event and notification message.

Webhooks are an alternative approach to polling; instead of your application continuously asking Onshape for new information, webhooks automatically send a notification from Onshape any time an event you are subscribed to occurs.

An application may register for notifications to a URL that uses either HTTP or HTTPS. If HTTPS is specified by the URL template, the notification server must supply a certificate that is signed by a certificate authority (CA) recognized by Onshape. Self-signed certificates (as well as certificates signed by unrecognized CAs) will be rejected, causing notification delivery to fail.

Webhooks can also have an additional level of authentication. See the [Onshape Help: Webhooks](https://cad.onshape.com/help/Content/Plans/webhooks.htm) page for more information.

> 📘 **Notes**
> 
> * This page provides sample code as curls. See the [curl documentation](https://curl.se/docs/) for more information.
> * All Onshape API calls must be properly authenticated by replacing the `CREDENTIALS` variable in the curls below. See the [API Keys](https://onshape-public.github.io/docs/app-dev/webhook/docs/auth/apikeys) page for instructions and the [Quick Start](https://onshape-public.github.io/docs/app-dev/webhook/docs/api-intro/quickstart) for an example. All applications submitted to the Onshape App Store _must_ authenticate with [OAuth2](https://onshape-public.github.io/docs/app-dev/webhook/docs/auth/oauth).
> * This documentation refers to Onshape IDs in the following format: `{did}, {wid}, {eid}, {pid}, {otherId}`. These represent document, workspace, element, part, and other IDs (respectively) that are needed make the API calls. We sometimes abbreviate these variables as `DWVEM` Please see [API Guide: API Intro](https://onshape-public.github.io/docs/app-dev/webhook/docs/api-intro/#onshape-api-request) for information on what these IDs mean and how to obtain them from your documents. Sometimes, this page will use a stand-in string to represent these IDs (`000000000000000000000000`). Never include the curly braces (`{}`) in your API calls.
> * For Enterprise accounts, replace **cad** in all Onshape URLs with your company domain. https://**cad**.onshape.com > https://**companyName**.onshape.com

#### Events

Each type of event that an application may receive notifications for has a unique identifier known as the event type. Event types are grouped into Event Groups. Each group shares specification requirements.

> 📘 **Note**Webhooks you create are automatically cleaned up after a period of inactivity. To prevent this cleanup, set `isTransient` to `false` when creating your webhook.

Event types are categorized into several different groups based on the dominant user resource of the event. The group that a given event is part of defines the required parameters needed in the registration process to identify the resource or group of resources to watch. For instance, if registering for an event in the `document` event group, the application must identify either a specific document’s id or a specific company’s id. If registered for a company, the event will be registered for all present and future documents owned by the company.

> 📘 **Note**
> 
> You can see the full list of available events in the Glassworks API Explorer. Expand the [createWebhook](https://cad.onshape.com/glassworks/explorer/#/Webhook/createWebhook) endpoint, then click **Callbacks**.
> 
> ![callbacks in the Glassworks Webhook > createWebhook > Callback page](https://onshape-public.github.io/docs/app-dev/webhook/images/webhooks-callbacks.png)

##### Application Group

Monitor changes to applications.

**Supported Event Types**

* `onshape.user.lifecycle.updateappsettings` \- Occurs when user application settings are modified

**Registration Requirements**

* `clientId` \- Must be specified in the registration body
* `event` \- Must be set to `onshape.user.lifecycle.updateappsettings`
* `options.collapseEvents` \- Must be set to `true` or `false`
* `url` \- Must be provided to receive the webhook notifications

```
{
  "clientId": "000000000000000000000000",
  "events": [
    "onshape.user.lifecycle.updateappsettings"
  ],
  "options": {
    "collapseEvents": false
  },
  "url": "https://sampleUrl.org"
}

```

##### Document Group

Monitor various aspects of document changes.

**Supported Event Types**

* `onshape.comment.create` \- Occurs when a comment is created
* `onshape.comment.delete` \- Occurs when a comment is deleted
* `onshape.comment.update` \- Occurs when a comment is updated
* `onshape.document.lifecycle.created` \- Occurs when a document is created
* `onshape.document.lifecycle.shared` \- Occurs when a document share is created, modified, or removed (via the Share dialog only)
* `onshape.document.lifecycle.statechange` \- Occurs when a document changes state
* `onshape.model.lifecycle.changed` \- Occurs when a change to a model is made
* `onshape.model.lifecycle.changed.externalreferences` \- Occurs when an external reference changes
* `onshape.model.lifecycle.createelement` \- Occurs when a new element is created
* `onshape.model.lifecycle.createversion` \- Occurs when a new version of a document is created
* `onshape.model.lifecycle.createworkspace` \- Occurs when a new workspace is created
* `onshape.model.lifecycle.deleteelement` \- Occurs when an element is deleted
* `onshape.model.lifecycle.metadata` \- Occurs when part or element metadata is modified
* `onshape.model.translation.complete` \- Occurs when a translation request is complete
* `onshape.revision.created` \- Occurs when a revision is created

**Registration Requirements**

* `documentId` OR `companyId` must be specified in the registration body  
   * Only `documentId` is valid for the `onshape.document.lifecycle.statechange`
* `event` \- Must be set to one of the supported event types listed above  
   * May be set to `false` if the application is always listening to webhook notifications and `companyId` is specified.  
   * If `false`, unregister the webhook when it is no longer needed.
* `options.collapseEvents` \- Must be set to `true` or `false`
* `url` \- Must be provided to receive the webhook notifications

```
{
  "documentId": "000000000000000000000000",
  "events": [
    "onshape.user.lifecycle.updateappsettings"
  ],
  "options": {
    "collapseEvents": false
  },
  "url": "https://sampleUrl.org"
}

```

##### Workflow Group

Monitor release management actions.

**Supported Event Types**

* `onshape.workflow.transition` \- Occurs when a revision or release package transitions through workflow states

**Registration Requirements**

* `companyId` \- Must be specified in the registration body
* `event` \- Must be set to `onshape.workflow.transition`  
   * May be set to `false` if the application is always listening to webhook notifications.  
   * If `false`, unregister the webhook when it is no longer needed.
* `options.collapseEvents` \- Must be set to `true` or `false`
* `url` \- Must be provided to receive the webhook notifications

```
{
  "companyId": "000000000000000000000000",
  "events": [
    "onshape.workflow.transition"
  ],
  "options": {
    "collapseEvents": false
  },
  "url": "https://sampleUrl.org"
}

```

##### Lifecycle Group

Monitor webhook changes. You do not need to register for these events; they are sent automatically when a webhook for another event type is registered, unregistered, or pinged.

**Supported Event Types**

* `webhook.register` \- Occurs in response to a notification registration API call
* `webhook.unregister` \- Occurs in response to a notification deregistration API call
* `webhook.ping` \- Occurs either:  
   * In response to a request by an application to call the [pingWebhook](https://cad.onshape.com/glassworks/explorer/#/Webhook/pingWebhook) endpoint.  
   * As a post-registration validation initiated by Onshape

#### Example Notifications

**webhook.register**

`{
  "timestamp": "2024-05-05T23:45:10.611-0500",
  "event": "webhook.register",
  "workspaceId": "000000000000000000000000",
  "elementId": "000000000000000000000000",
  "webhookId": "000000000000000000000000",
  "messageId": "000000000000000000000000",
  "data": "Some data",
  "documentId": "000000000000000000000000",
  "versionId":  "000000000000000000000000"
}
`

**webhook.ping**

`{
  "timestamp": "2024-05-05T23:45:10.611-0500",
  "event": "webhook.ping",
  "workspaceId": "000000000000000000000000",
  "elementId": "000000000000000000000000",
  "webhookId": "000000000000000000000000",
  "messageId": "000000000000000000000000",
  "data": "Some data",
  "documentId": "000000000000000000000000",
  "versionId":  "000000000000000000000000"
}
`

**onshape.model.lifecycle.changed**

`{
  "timestamp": "2024-05-05T23:46:29.284-0500",
  "event": "onshape.model.lifecycle.changed",
  "workspaceId": "000000000000000000000000",
  "elementId": "000000000000000000000000",
  "webhookId": "000000000000000000000000",
  "messageId": "000000000000000000000000",
  "data": "Some data",
  "documentId": "000000000000000000000000",
  "versionId":  "000000000000000000000000"
}
`

**onshape.document.lifecycle.statechange**

`{
  "timestamp": "2024-05-05T23:46:29.284-0500",
  "event": "onshape.document.lifecycle.statechange",
  "workspaceId": "000000000000000000000000",
  "elementId": "000000000000000000000000",
  "webhookId": "000000000000000000000000",
  "messageId": "000000000000000000000000",
  "data": "Some data",
  "documentId": "000000000000000000000000",
  "versionId":  "000000000000000000000000",
  "documentState": "TRASH"
}
`

Possible values of `documentState` are:

* `ACTIVE` \- Document is in a normal, usable state.
* `TRASH` \- Document has been moved to the trash; user can move document back to `ACTIVE` state.
* `DELETED` \- Document has been deleted; user cannot access document.

**onshape.user.lifecycle.updateappsettings**

`{
  "timestamp": "2024-05-05T23:46:29.284-0500",
  "event": "onshape.user.lifecycle.updateappsettings",
  "workspaceId": "000000000000000000000000",
  "elementId": "000000000000000000000000",
  "webhookId": "000000000000000000000000",
  "messageId": "000000000000000000000000",
  "data": "Some data",
  "userId": "000000000000000000000000",
  "clientId":"000000000000000000000000"
}
`

**onshape.model.translation.complete**

`{
  "timestamp": "2024-05-05T23:46:29.284-0500",
  "event": "onshape.model.translation.complete",
  "workspaceId": "000000000000000000000000",
  "elementId": "000000000000000000000000",
  "webhookId": "000000000000000000000000",
  "messageId": "000000000000000000000000",
  "data": "Some data",
  "documentId": "000000000000000000000000",
  "userId": "000000000000000000000000",
  "translationId": "000000000000000000000000"
}
`

**onshape.comment.create**

`{
  "timestamp": "2024-05-05T23:46:29.284-0500",
  "event": "onshape.comment.create",
  "workspaceId": "000000000000000000000000",
  "elementId": "000000000000000000000000",
  "webhookId": "000000000000000000000000",
  "messageId": "000000000000000000000000",
  "documentId": "000000000000000000000000",
  "commentId": "000000000000000000000000"
}
`

#### Endpoints

Webhook notifications allow an application to register to receive notifications of certain events that occur within the Onshape environment. To receive a notification, an application must expose an endpoint that Onshape can call.

* [Webhook/getWebhooks](https://cad.onshape.com/glassworks/explorer/#/Webhook/getWebhooks)  
```  
  curl -X 'GET' \  
    'https://cad.onshape.com/api/v6/webhooks?user={uid}&offset=0&limit=20' \  
    -H 'aAccept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS'  
```
* [Webhook/createWebhook](https://cad.onshape.com/glassworks/explorer/#/Webhook/createWebhook)  
```  
  curl -X 'POST' \  
    'https://cad.onshape.com/api/v6/webhooks' \  
    -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS' \  
    -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
    -d '{  
          "events": [  
            "eventType" // See the [Events](#events) section above for valid event types.  
          ],  
          "options": {  
            "collapseEvents": true | false  
          },  
          "url": "https://sampleUrl.org"  
          //Other parameters may be required. See the [Events](#events) section above.  
        }'  
```
* [Webhook/getWebhook](https://cad.onshape.com/glassworks/explorer/#/Webhook/getWebhook)  
```  
curl -X 'GET' \  
  'https://cad.onshape.com/api/v6/webhooks/webhookId' \  
  -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
  -H 'Authorization: Basic CREDENTIALS'  
```
* [Webhook/updateWebhook](https://cad.onshape.com/glassworks/explorer/#/Webhook/updateWebhook)  
```  
  curl -X 'POST' \  
    'https://cad.onshape.com/api/v6/webhooks/webhookId' \  
    -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS' \  
    -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \  
    -d '{  
          "id": "webhookId",  
          "options": {  
            "collapseEvents": true | false  
          }  
        }'  
```  
   * Note that the webhook `id` must be sent in both the URL and the request body.
* [Webhook/unregisterWebhook](https://cad.onshape.com/glassworks/explorer/#/Webhook/unregisterWebhook)  
```  
  curl -X 'DELETE' \  
    'https://cad.onshape.com/api/v6/webhooks/{webhookId}?blockNotification=false' \  
    -H 'accept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS'  
```
* [Webhook/pingWebhook](https://cad.onshape.com/glassworks/explorer/#/Webhook/pingWebhook)  
```  
  curl -X 'POST' \  
    'https://cad.onshape.com/api/v6/webhooks/{webhookId}/ping' \  
    -H 'Accept: application/json;charset=UTF-8; qs=0.09' \  
    -H 'Authorization: Basic CREDENTIALS'  
```

#### Sample Workflows

##### Create a webhook

An application registers for event notification by:

1. Making a REST call to the Onshape web service
2. Providing a URL to notify
3. Providing the required parameters for the event types to be registered

If the registration request is well-formed, the registration API call returns information about the registration, including a unique `id` string that identifies the webhook registration. This corresponds to the `webhookId` field in other endpoints. No de-duplication of notification registrations is performed by the API. Each registration call will yield a new `registrationId`, even if the parameters are identical to those passed in a prior call.

Shortly after an application calls the notification registration API, Onshape will make make an asynchronous trial notification call to the URL generated from the URL template with an event type of `webhook.register` to test if the application notification server is accessible. If the trial notification delivery fails to return an HTTP `200` status code, the notification registration is cancelled. The trial notification is usually delivered after the notification registration has been received by the application. However, variations in network delays may result in the trial notification occurring before the response is received and processed by the application, so the notification handler should be ready to process notifications before the registration call is made.

In this example, we use a webhook to send information from Onshape to another server. You need a URL for Onshape to send notifications to, and a way to view the messages sent with those notifications.

1. Open an Onshape document, or create a new one.
2. In this example, we want to receive a notification from Onshape any time a new version is created in the specified document. For this, we’ll use `onshape.model.lifecycle.createversion` as our `event`.
3. The event type requires one parameter. We’ll use our `documentId` for this field (shown as `000000000000000000000000` in the example below).
4. All event types require specifying `true` or `false` for the `options.collapseEvents` field. In this case, set the field to `false`.
5. Next, we need the URL to send the notification to. You must provide your own URL to receive notifications here.
6. Confirm your [createWebhook](https://cad.onshape.com/glassworks/explorer/#/Webhook/createWebhook) call looks like this (substitute your own authorization credentials, document ID, and URL), then make the call.

```
  curl -X 'POST' \
    'https://cad.onshape.com/api/v6/webhooks' \
    -H 'Accept: application/json;charset=UTF-8; qs=0.09' \
    -H 'Authorization: Basic CREDENTIALS' \
    -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \
    -d '{
        "documentId": "000000000000000000000000",
        "events": [
          "onshape.model.lifecycle.createversion"
        ],
        "options": {
          "collapseEvents": false
        },
        "url": "https://sampleUrl.org"
    }'

```

1. In your application, confirm that you received the `webhook.register` event from Onshape.
2. In Onshape, create a new version in your document.
3. In your application, confirm that you received the `onshape.model.lifecycle.createversion` event from Onshape. Make note of the `id` in the response; use this as your `webhookId` in subsequent examples.

##### Get webhook info

1. Complete the [Create a webhook](#create-a-webhook) steps above to obtain a `webhookId`.
2. Create your [getWebhook](https://cad.onshape.com/glassworks/explorer/#/Webhook/getWebhook) call. substitute your own authorization credentials and `webhookId` (shown as `000000000000000000000000` in the example below), then make the call.

```
  curl -X 'GET' \
    'https://cad.onshape.com/api/v6/webhooks/000000000000000000000000' \
    -H 'Accept: application/json;charset=UTF-8; qs=0.09' \
    -H 'Authorization: Basic CREDENTIALS' \

```

1. Confirm that the `event` in the response is `onshape.model.lifecycle.createversion`.

##### Update a webhook

1. Complete the [Create a webhook](#create-a-webhook) steps above to obtain a `webhookId`. Note that in the same response, the webhook `description` is `null`.
2. Create your [updateWebhook](https://cad.onshape.com/glassworks/explorer/#/Webhook/updateWebhook) call. In this example, ww update the webhook’s `description`. Substitute your own authorization credentials and `webhookId` (shown as `000000000000000000000000` in the example below in both the URL and request body). Then make the call.

```
  curl -X 'POST' \
    'https://cad.onshape.com/api/v6/webhooks/000000000000000000000000' \
    -H 'accept: application/json;charset=UTF-8; qs=0.09' \
    -H 'Authorization: Basic CREDENTIALS' \
    -H 'Content-Type: application/json;charset=UTF-8; qs=0.09' \
    -d '{
          "id": "000000000000000000000000",
          "description": "Send a notification each time a document version is created.",
          "options": {
            "collapseEvents": false
          }
      }'

```

1. Confirm in the response that the webhook `description` is set to `Send a notification each time a document version is created.`

##### Delete a webhook

When an application no longer needs to be notified of changes specified by a particular notification registration, it should normally deregister the notification request. Deregistration is performed by making an HTTP that specifies the hook to deregister. Onshape will attempt to call the deregistered hook with an event type of `webhook.unregister` as validation that the deregistration is complete. If the application does not deregister the webhook, Onshape will continue delivering notifications until the the application either returns an error in response to a notification for the webhook or fails to respond at all for an extended period of time.

1. Complete the [Create a webhook](#create-a-webhook) steps above to obtain a `webhookId`.
2. Create your [deleteWebhook](https://cad.onshape.com/glassworks/explorer/#/Webhook/deleteWebhook) call. substitute your own authorization credentials and `webhookId` (shown as `000000000000000000000000` in the example below), then make the call.

```
  curl -X 'DELETE' \
    'https://cad.onshape.com/api/v6/webhooks/000000000000000000000000' \
    -H 'Accept: application/json;charset=UTF-8; qs=0.09' \
    -H 'Authorization: Basic CREDENTIALS=' \

```

1. In your application, confirm that you received the `webhook.unregister` event from Onshape.
2. In Onshape, create a new version in your document.
3. In your application, confirm that no new events have been received.

#### Additional Resources

* [Onshape Help: Webhooks](https://cad.onshape.com/help/Content/Plans/webhooks.htm)
* [API Guide: API Explorer](https://onshape-public.github.io/docs/app-dev/webhook/docs/api-intro/explorer)
* [API Explorer: Webhooks](https://cad.onshape.com/help/Content/Plans/webhooks.htm)
* [Sample Code: Python Webhooks](https://github.com/onshape-public/onshape-clients/blob/master/python/test/test%5Fwebhooks.py#L126)

---

<a id="sec-app-store"></a>
## App Store

<a id="pg-docs-app-store"></a>
### Onshape App Store

_Source: <https://onshape-public.github.io/docs/app-store/>_

Onshape makes applications available through the [Onshape App Store](https://appstore.onshape.com). The App Store is actively promoted to users, making it easy for users to find, purchase, and use third-party applications.

> To submit an application to the Onshape App Store, complete the [Launch Checklist](https://onshape-public.github.io/docs/app-store/docs/app-store/checklist), which provides a step-by-step guide that you can follow to make your app public.

#### Create an App Store entry

> **Note**
> 
> All public apps submitted to the App Store must authenticate with [OAuth2](https://onshape-public.github.io/docs/app-store/docs/auth/oauth).

1. First, [create your application](https://onshape-public.github.io/docs/app-store/docs/app-dev/#create-an-application).
2. Click the app’s **Details** tab.
3. Click **Create store entry**.  
![Create store entry button in the dev portal](https://onshape-public.github.io/docs/app-store/images/create-store-entry-01.png)
4. Fill out the form:  
![Create store entry form in the dev portal](https://onshape-public.github.io/docs/app-store/images/create-store-form-01.png)
* **Category**: `General`
* **Description**: `Embeds the Onshape Learning Center as an Element Right Panel extension.`
* **Vendor Name**: `Your Name`
1. Click **Create**.

##### Subscribe to the app

When working in an Enterprise, administrators can assign apps to users, aliases, or teams directly. All other users can subscribe to the app in the App Store:

1. Go to the Onshape App Store: <https://cad.onshape.com/appstore?sort=date>  
   * If working in an enterprise, remember to replace `cad` in the URL with your company name.
2. Select the app.  
![New entry appears in the app store as PRIVATE](https://onshape-public.github.io/docs/app-store/images/app-store-entry-01.png)
3. Click **Subscribe**.  
![Click the Subscribe button in the app store](https://onshape-public.github.io/docs/app-store/images/app-store-subscribe-01.png)
4. Follow the on-screen prompts to subscribe to the app.

#### End users

Users can browse the Onshape App Store and install third-party applications:

[![Onshape App Store video](https://onshape-public.github.io/docs/app-store/images/AppStoreVideoCard.png)](https://onshape.wistia.com/medias/qt3so13tf1)

When a user registers an application, there are several possible integration points to expose the application within the Onshape user experience. At this time, applications that provide a UI in an Onshape tab will be added to the **+** button menu on the Onshape tab bar. See the [Extensions](https://onshape-public.github.io/docs/app-store/docs/app-dev/extensions/) page for more information on supported app locations and contexts.

![image](https://onshape-public.github.io/docs/app-store/images/apioverviewimage02.png)

#### Feedback

Your comments, questions, and concerns are always welcome!

* For API support, email us at [api-support@onshape.com](mailto:api-support@onshape.com) at any time.
* For all other developer-related feedback, email us at [onshape-developer-relations@ptc.com](mailto:onshape-developer-relations@ptc.com).

---

###### [Launch Checklist](https://onshape-public.github.io/docs/app-store/docs/app-store/checklist/)

###### [Testing Guidelines](https://onshape-public.github.io/docs/app-store/docs/app-store/testingguidelines/)

###### [Quality Considerations](https://onshape-public.github.io/docs/app-store/docs/app-store/quality/)

---

<a id="pg-docs-app-store-checklist"></a>
### Launch Checklist

_Source: <https://onshape-public.github.io/docs/app-store/checklist/>_

This checklist combines the processes you should follow to ensure your app launches successfully. While all tasks must be completed to submit your app to the Onshape App Store, the task sequence provided here is a suggestion.

If you do not have access to Developer Licenses yet, please contact the [Developer Relations team](mailto:onshape-developer-relations@ptc.com).

##### Understand quality expectations

These are to ensure that the Onshape App Store remains a trusted resource and that quality is maintained. Review the [Quality Considerations](https://onshape-public.github.io/docs/app-store/checklist/docs/app-store/quality/) page, and reach out to the [Developer Relations team](mailto:onshape-developer-relations@ptc.com) with any questions.

##### Sign in to your developer account

Sign in to the [Onshape Dev Portal](https://cad.onshape.com/appstore/dev-portal), and ensure your developer account details are accurate. Contact our [API Support team](mailto:api-support@onshape.com) if you need assistance.

##### Authenticate your app

Please refer to the [OAuth API Guide](https://onshape-public.github.io/docs/app-store/checklist/docs/auth/oauth) for information on authenticating your app with OAuth2.

##### Build your app

While building your app, use the resources in our Onshape Developer Documentation, including this API Guide and our [API Explorer](https://cad.onshape.com/glassworks). We recommend familiarizing yourself with the following pages:

* [Introduction to the Onshape REST API](https://onshape-public.github.io/docs/app-store/checklist/docs/api-intro/)
* [Onshape Architecture](https://onshape-public.github.io/docs/app-store/checklist/docs/api-intro/architecture/)
* [Onshape App Development](https://onshape-public.github.io/docs/app-store/checklist/docs/app-dev/)
* [Extensions](https://onshape-public.github.io/docs/app-store/checklist/docs/app-dev/extensions/)
* [Client Messaging](https://onshape-public.github.io/docs/app-store/checklist/docs/app-dev/clientmessaging/)
* [Onshape App Store](https://onshape-public.github.io/docs/app-store/checklist/docs/app-store/s)

##### Prepare your store entry

Prepare the descriptions, promotional graphics, screenshots, and videos you’ll add to your store entry. If necessary, include a link to Download or sign in. Watch this video for more details.

See the video below for a walkthrough:

Questions about preparing and submitting a Store Entry? Contact our [Developer Relations team](mailto:onshape-developer-relations@ptc.com).

##### Run beta tests

During the beta period, try to enlist at least 5 active testers to get feedback before making your app available to the general public.

1. To find beta testers, contact our [Developer Relations team](mailto:onshape-developer-relations@ptc.com) and recruit via the [Onshape Forum](https://forum.onshape.com/categories/developer-community).
2. To give beta users early visibility, first create a team and then ensure your app is shared with that team in the [Onshape Dev Portal](https://cad.onshape.com/appstore/dev-portal). For a walkthrough, read the [Create a team in Onshape](https://learn.onshape.com/courses/company-organization-in-onshape?returnTo=/learn/article/company-organization-in-onshape) article.

##### Determine your app’s price

Once you’ve determined your monetization model, set up your price, billing, and other details. Billing should be tested, and to do so a staging environment is available. See the [Account](https://cad.onshape.com/glassworks/explorer/#/Account) and [Billing](https://cad.onshape.com/glassworks/explorer/#/Billing) APIs for more details.

We also strongly encourage offering a free trial period to allow potential customers to try out your product before purchasing.

##### Sign and return the developer agreement

Email the [Developer Relations team](mailto:onshape-developer-relations@ptc.com) to obtain yours.

##### Submit your app for final testing

Once you’ve returned the developer agreement, you can submit your app for final testing. To submit your app for QA testing, review the [Testing Guidelines](https://onshape-public.github.io/docs/app-store/checklist/docs/app-store/testingguidelines), and reach out to your [Developer Relations contact](mailto:onshape-developer-relations@ptc.com) for our most current testing suggestions.

During this testing period (expect up to a week, depending on complexity), changes to code are prohibited unless requested. At the conclusion of the test, you will receive one of the following notifications from our Developer Relations team:

* Approved for release
* Approved for release with feedback
* Changes required before another round of testing

##### Integrate your support systems

Whether you use Zendesk, Jira, or email support, we’ll help you determine and set up this integration. Contact the Developer Relations team to explore these options. This is the channel we will use to test your app and provide feedback.

##### Connect via Slack

Connecting directly with our Support, Tech, and Sales teams has proven to be valuable to app developers. This dedicated channel is simple to implement if you already have a paid Slack account. If not (or if you want to use the free version of Slack), we can add members of your team as guests to our account. Please contact the Developer Relations team to establish this connection.

##### Final check and publish

First, double-check you’ve done everything on this list. Now you’re ready to publish your app to the production channel. Send an email detailing **when** you’d like your app to be published, to the Developer Relations team.

##### Promote your app

Start promoting your app with the [Onshape Logo](https://www.ptc.com/en/brand-guide/logos/onshape) on social media, and by posting in Onshape communities such as:

* The official [Onshape Forum](https://forum.onshape.com/categories/developer-community)
* [Onshape Users LinkedIn Group](https://www.linkedin.com/groups/7426836/)
* [r/Onshape](https://www.reddit.com/r/Onshape/)

We also recommend completing this [Co-Marketing Packet](https://onshape-public.github.io/docs/app-store/checklist/pdfs/OnshapeAppStoreCoMarketingPacket.pdf) and sending a copy to the [Developer Relations team](mailto:onshape-developer-relations@ptc.com). This provides the Onshape Marketing team with the necessary information to promote your app via official Onshape channels.

_Note: Promotion of your application by the Onshape Marketing team is up to the sole discretion of the Onshape Marketing team. Completion of the Co-Marketing Packet does not guarantee promotion._

##### Encourage reviews from users

The value of reviews is not to be underestimated. Reviews give users an opportunity to provide feedback, and can also signal to others that your app is worth investigating.

We strongly encourage you to request reviews from your users. Reviews can help elevate your listing’s standing in the Onshape App Store. Point users of your app to your app listing in the Onshape App Store to leave a review.

##### Maintain your app

Continually fix stability and performance issues. Improving the user experience will result in more engaged users, higher ratings, and in turn, more success.

Failure to respond to customer tickets in a reasonable time will result in your app being removed from the Onshape App Store.

##### Increase engagement and retention

Aim to increase user engagement, retain and grow your audience, and earn more revenue by:

* Encouraging repeat visits with a nurture stream and training materials
* Integrating more features from user requests
* Interacting with and understanding your audience via the [Onshape Forum](https://forum.onshape.com/categories/developer-community), social media, etc.

##### Address app security

At some point, a prospect or user will enquire about your app’s security controls. To address this, we recommend that you understand SOC 2 Compliance requirements, and consider filling out the [Consensus Assessment Initiative Questionnaire](https://cloudsecurityalliance.org/artifacts/consensus-assessments-initiative-questionnaire-v3-1/) (CAIQ). Onshape/PTC cannot and will not attest to your compliance. More on SOC Compliance can be found at the following links:

* [AICPA.org](https://us.aicpa.org/interestareas/frc/assuranceadvisoryservices/aicpasoc2report)
* [Wikipedia: System and Organization Controls](https://en.wikipedia.org/wiki/System%5Fand%5FOrganization%5FControls)

---

<a id="pg-docs-app-store-quality"></a>
### Quality Considerations

_Source: <https://onshape-public.github.io/docs/app-store/quality/>_

#### Core App Quality

Onshape users expect high-quality apps. App quality directly influences the long-term success of your app in terms of installs, user rating and reviews, engagement, and user retention.

This page helps you assess the core aspects of quality in your app, through a compact set of quality criteria and associated tests. All Onshape apps should meet these criteria.

Before publishing your apps, test them against these criteria to ensure that they function well. Your testing should go well beyond what’s described here; the purpose of this page is to specify the essential quality characteristics all apps should display, so that you can cover them in your test plans.

#### Functionality

These criteria ensure that your app provides the expected functional behavior, with the appropriate level of permissions.

| Area        | Description                                                                                           |
| ----------- | ----------------------------------------------------------------------------------------------------- |
| Permissions | The app requests only the _absolute minimum_ permissions that it needs to support core functionality. |

#### Compatibility, Performance, and Stability

These criteria ensure that apps provide the compatibility, performance, stability, and responsiveness expected by users.

| Area           | Description                                                                                                                                                       |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stability      | The app does not crash, force close, freeze, or otherwise function abnormally.                                                                                    |
| Performance    | The app loads quickly or provides onscreen feedback to the user (e.g., a progress indicator or similar cue) if the app takes longer than two (2) seconds to load. |
| Visual quality | The app displays graphics, text, images, and other UI elements without noticeable distortion, blurring, or pixelation.                                            |

#### Security

These criteria ensure that apps handle user data and personal information safely.

| Area       | Description                                                                                                                                                                                               |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data       | All private data is stored in the app’s internal storage.All data from external storage is verified before being accessed.No personal or sensitive user data is logged to the system or app-specific log. |
| Networking | All network traffic is sent over SSL.                                                                                                                                                                     |

#### Onshape App Store

These criteria ensure that your apps are ready to publish on Onshape App Store.

| Area             | Description                                                                                                                                                                                                                                                                               |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| App Details page | The app’s feature graphic follows guidelines such as:\- The app listing includes a high-quality feature graphic.\- The feature graphic does not resemble an advertisement.\- The app’s screenshots or videos do not represent the content and experience of your app in a misleading way. |
| User support     | User-reported bugs are addressed if they are reproducible.                                                                                                                                                                                                                                |

#### Test procedures

These test procedures help you discover various types of quality issues in your app. You can combine the tests or integrate groups of tests together in your own test plans. See the sections above for references that associate criteria with these test procedures.

| Type       | Description                                                                                                             |
| ---------- | ----------------------------------------------------------------------------------------------------------------------- |
| Core suite | Navigate to all parts of the app: all screens, dialogs, settings, and all user flows.                                   |
| Security   | \- Review all data stored in external storage.\- Review how data loaded from external storage is handled and processed. |

---

<a id="pg-docs-app-store-testingguidelines"></a>
### Testing Guidelines

_Source: <https://onshape-public.github.io/docs/app-store/testingguidelines/>_

The purpose of this document is to help you get your application and App Store entry ready for QA testing.

#### Application Release Workflow (ARW)

Each application submitted to the Onshape App Store goes through a series of stage-gates:

1. Starting state: `Ok to deploy to limited visibility on Production` (Beta testing)
2. `Ok to make Public`
3. Goal state: `Application is Public`

To advance to the next stage, your application must pass testing, and your App Store entry must pass review.

#### Kick Off Testing

While completing the [Launch Checklist](https://onshape-public.github.io/docs/app-store/testingguidelines/docs/app-store/checklist), you will need to use Jira to request testing and release for your application. You can initiate the following tasks from Jira:

* `Request application testing`: This puts your application in the testing queue. We will note when testing has started (`in progress`) and when concluded, the ticket will be closed. The outcome will include notes and links to any issues generated (`tickets`). This phase may include as many iterations as needed to get your application ready.
* `Request public (general) authorization`: We will note when testing has started (`in progress`), and this request will trigger a review of your app store entry and any outstanding bugs. Note there is no implied testing of your application, simply a review of outstanding issues (`tickets`) and of the App Store entry. Success at this stage will advance the Application Release Workflow (ARW), and you can request public release.
* `Request public (general) release`: This request states that you have coordinated with the [Developer Relations team](mailto:onshape-developer-relations@ptc.com) and the Onshape Marketing team, and agreement has been reached that the app is ready for launch. Congratulations!

#### Testing Protocol

_Applications_ are first tested against the checklist in [Addendum A](#addendum-a). _Production App Store_ entries are then performed against the checklist in [Addendum B](#addendum-b).

Results will be viewable in your Onshape support system (i.e., Zendesk, Jira). The result of each test will be one of:

* `Pass`:  
   * No action needed.  
   * No notification issued.
* `Enhancement`: Suggestions we believe would make the application better.  
   * Will NOT prevent the application from being turned on for public access.
* `Bug (low priority)`: Slight deviations from the criteria that have low end user impact.  
   * Will NOT prevent the application being turned on for public access.  
   * No stipulated time-frame for resolution.
* `Bug (medium priority)`: Material deviations from the criteria that are noticeable to the end-user. Represents a minor problem that requires a work-around.  
   * Will NOT prevent the application from being turned on for public access.  
   * Must be fixed within 30 days.
* `Bug (high priority)`: Significant deviation from the criteria.  
   * WILL prevent the application from being turned on for public access.
* `Bug (MUST FIX)`: Significant deviation from protocol or security violation.  
   * WILL prevent the application from being turned on for public access.  
   * If the application is already public, it may be temporarily suspended from the App Store.

#### Testing Notes

* Testing may be requested at any time.
* Testing is done on a first-come basis.
* When testing is complete (pass or fail), you go to the back of the queue.

#### Addendum A

Application Test Criteria

* The application must use the Onshape OAUTH mechanism
* The OAUTH must be against the correct stack
* To be promoted to the Production stack, and hosted service must be on a monitored production server with worldwide 24/7 availability.
* The application should not generate any avoidable console (browser) errors
* The application should should provide one or more of the following options. The user should not have to leave the registration workflow to complete a pre-requisite.  
   * Sign in using the Onshape ID (account created silently on first use)  
   * Sign in with partner product account credentials  
   * Create a new partner account
* The application must be capable of managing/displaying documents in excess of 20\. The application must display reasonable performance when reading documents, workspaces, elements, and parts. At scale, an account may have thousands of documents, many with multiple workspaces and each with multiple elements. Suggested strategies include:  
   * Using a `Next` button to load the next 20 documents  
   * Using infinite scroll (loading the next 20 if the scrollbar reaches the bottom of the dialog)  
   * Displaying the most recently-opened documents first  
   * Displaying a counter of documents/workspaces/elements read  
   * Using progressive loading
* The application should correctly list valid documents when `per document app access` is turned on.
* The application should correctly handle selection of versions.
* The application should correctly handle selection of workspaces (branches).
* The application should correctly handle/display elements that are:  
   * Part Studios that contain nothing  
   * Assemblies that contain nothing  
   * Part Studios that contain only surfaces  
   * Part Studios that contain only wire data (e.g., helices)
* The application should appropriately handle revocation of a grant.

#### Addendum B

App Store Testing Criteria

* The application should have a descriptive name
* The application summary should be accurate
* The redirect URLS should be valid
* The iframe URL should be valid
* The `Grant` (permissions) request should be no more than is needed
* The `Application Type` should be correctly set
* Team visibility should be set (optional)
* The category should be appropriate
* The application description should be accurate
* The Sign-In URL should be valid
* The pricing summary should be accurate  
   * i.e., trials should not be listed as `Free`; `Free for xx days and then $xx/month` is more accurate.
* All pay plans should have accurate descriptions.
* The support URL should point to a resource for help (the resource should NOT be an FAQ page, unless that page also contains one of the other options):  
   * Support ticketing system (e.g., Zendesk, Jira, etc.)  
   * Web page with a telephone number  
   * Web page with an email address  
   * Forum
* The EULA link should point to an English Language EULA.

---

<a id="sec-tutorials"></a>
## Tutorials

<a id="pg-docs-tutorials"></a>
### Sample Apps

_Source: <https://onshape-public.github.io/docs/tutorials/>_

The easiest way to get started with the Onshape API is to look at our sample applications. Each sample application is provided as a Github repository. For access, go to <https://github.com/onshape-public>.

---

###### [Create an Extension](https://onshape-public.github.io/docs/tutorials/docs/tutorials/createextension/)

###### [glTF Viewer](https://onshape-public.github.io/docs/tutorials/docs/tutorials/gltf/)

---

<a id="pg-docs-tutorials-createextension"></a>
### Create an Extension

_Source: <https://onshape-public.github.io/docs/tutorials/createextension/>_

In this example, you will create a custom web page (as shown in the image below) that is displayed in the right-hand fly-out panel. This interface displays metadata pulled from a third-party system when a part in Onshape is selected. This interface can also update metadata in Onshape through the `Update` functionality.

> **Note**
> 
> These steps are for creating a private application on a personal account. To create an internal application for a company, classroom, or enterprise, see [Enterprise Settings: Developer](https://cad.onshape.com/help/Content/Plans/enterprise%5Fsettings%5Fdeveloper.htm). To create a public application for the Onshape App Store, see [OAuth](https://onshape-public.github.io/docs/tutorials/createextension/docs/auth/oauth) and [App Development](https://onshape-public.github.io/docs/tutorials/createextension/docs/app-dev/).

##### Define the extension

This tutorials builds off the [Generate Derivative Files](https://onshape-public.github.io/docs/tutorials/createextension/docs/tutorials/derivative) tutorial. Please complete that one before starting on this one.

1. Navigate to the Developer portal from <https://cad.onshape.com/appstore/dev-portal>.
2. Click **OAuth applications** in the left menu.
3. Select your application, and the click the **Extensions** tab.![Graphical user interface, application, Teams Description automatically generated](https://onshape-public.github.io/docs/tutorials/createextension/images/integrationguideimage91.png)
4. Click the **Add Extension** button on the top right.
5. Select `Element Right Panel`.![Graphical user interface, application Description automatically generated](https://onshape-public.github.io/docs/tutorials/createextension/images/integrationguideimage92.png)
6. Next, define the context. The context defines what parameters can be sent from Onshape to the application. Some basic parameters are automatically sent with any context, additional information can be passed to our application, depending on the context selected. Click the `Selected part` option. This sends the `partId` and `partNumber` to the application, along with the `documentId`, `elementId`, and the `workspaceOrVersionId`.
7. In the `Action URL` field, fill in the URL of the page to load in the right element panel. The parameters can be added as arguments (variable that get replaced with real values when the page is loaded from Onshape).  
```  
https://ourserver.com/bom?documentId=${documentid}&elementId=${elementid}&partId={$partId}&partNumber={$partNumber}  
```
8. Finally, select an icon for the extension. This will appear on the tab that opens the right element panel.

You have now defined the extension, and it will appear in the Onshape interface.

##### Call a page in the extension

The following code snippet shows how to use your previous definition to pull data from the third-party application and send it to the web page:

`//https://myserver.com/bom?documentId=${documentId}&elementId=${elementId}&
//partId=${partId}&partNumber=${partNumber}
app.get('/bom', (req, res) => {
  if (req.query.partNumber !== '${partNumber'}) {
    partController.getPartsList(req.query.partNumber).then((parts) => {
      catController.getCatById(parts.Category).then((cat) => {
        res.render('bomview', {
          parts: parts,
          cat: cat
        })
      })
    })
  } else {
    res.render('bomview', {
      parts: { "_id": 0 },
      cat: { "_id": 0 }
    })
  }
})
`

This code checks to see if the `partNumber` parameter was actually populated (i.e., that a part number was defined for the selected part). If defined, you can use the part number to retrieve information about the selected part from our third-party application.

If the part number isn’t defined, you can send an alert to the web page to notify the user that a part number must be defined to use this web page.

You can also use the document ID, the element ID, and the Part ID to retrieve the correct part as long as they are stored with the part in your application.

##### Use the extension

1. In Onshape, load a document. You will see your icon embedded in the location you chose for you extension.
2. Select a part in a Part Studio, and click the icon to open the extension application:![Graphical user interface Description automatically generated](https://onshape-public.github.io/docs/tutorials/createextension/images/integrationguideimage94.png)  
If the part you selected has not yet been synced with your third-party application, no part number has been generated, and the system can’t find a corresponding object in our database.  
When you select a part that has been synced, and a part number has been generated, you will see the expected result:  
![Graphical user interface Description automatically generated](https://onshape-public.github.io/docs/tutorials/createextension/images/integrationguideimage95.png)  
Since the context you selected for this application extension was `Selected Part`, a part must be selected to load anything in the extension. If no part is selected, you will see a notification similar to the following:  
![Graphical user interface, text, application Description automatically generated](https://onshape-public.github.io/docs/tutorials/createextension/images/integrationguideimage96.png)

---

<a id="pg-docs-tutorials-gltf"></a>
### glTF Viewer

_Source: <https://onshape-public.github.io/docs/tutorials/gltf/>_

The GLTF Viewer is a sample application that demonstrates:

* How to fetch a glTF representation of an Onshape model
* How to create an app that runs as a tab inside an Onshape document
* OAuth2 authentication
* Use of REST APIs
* Use of document context

The application is built using Express and is deployed on Heroku.

Refer to the [gltf-viewer-app README](https://github.com/onshape-public/app-gltf-viewer) for instructions on running this sample app.

---

<a id="sec-help"></a>
## Help

<a id="pg-docs-help"></a>
### Get Help

_Source: <https://onshape-public.github.io/docs/help/>_

#### Onshape Help

See the Onshape Help Docs at <https://cad.onshape.com/help/Content> (or `https://<companyName>.onshape.com/help/Content` for Enterprise accounts).

#### Contact Us

You can contact the Onshape API Support team at `api-support@onshape.com`, or browse through our FAQs and troubleshooting tips below.

#### FAQs

##### What is the user experience of granting and revoking OAuth access?

Once users have purchased the application from the App Store, they will start seeing actions and panel icons as described by the extensions. When they try to use these actions and panels, they will be prompted by an error message stating that they need to grant access first.

They can grant access by navigating to the ‘Applications’ section under ‘My Account’.

![image alt text](https://onshape-public.github.io/docs/help/images/extensionsimage22.png)

Users will have to grant 2 permissions. The first button called ‘Onshape access’ will enable the application to make calls to the Onshape API. This will require the user’s Onshape credentials.

The second button calls ‘External access’ and enables Onshape to make calls to the application API. This will require the user’s credentials in the application. Both modes of access use OAuth, so credentials are not stored in the other system.

If the access is revoked at any time, the actions and panels will ask the user to re-authenticate from the ‘Applications’ page. Access may be revoked manually from Onshape or the application, or because a new version is installed that requires a different scope.

##### Who can get access to my app, and how?

Applications with extensions are only available to people who have been explicitly granted this permission in Onshape. Users who have been given this permission will be able to go to the App Store and purchase the application. There is no change to this process from earlier. They will then be able to grant access to the application as described in the previous question.

Do not publish your application if it contains extensions in the App Store for all users. Other users (who have not been granted permission) will not be able to see the extensions and will have a bad experience.

##### How is my application informed about selection changes in the Onshape UI?

Let’s take the case where your application has an extension that is showing some information in the document info panel that is based on document selection. As the selection changes, the action URL passed to the extension will change (based on parameterization). The new action URL will be loaded into the IFrame for the extension, and the application page will reload. We are adding support for post messages to reduce loading overhead in the future.

##### What is the timeout for the action\_url of extensions? Is it configurable?

Timeout set for each GET or POST request set as action\_url of an extension is 180 seconds. Timeout is not configurable.

##### What changed when my legacy application migrated to extensions?

If you had created a desktop or connected cloud app, nothing has changed.

If you had created an integrated cloud app, the following changes have been made to the app.

* The IFrame URL has been changed to the OAuth URL. This is now invoked from the user’s application setting page to grant OAuth access. A redirect URL is passed along with the call as a query parameter named ‘redirectOnshapeUri’. You will need to modify your code to redirect to this URL if it is present.
* A new tab extension is automatically created for your applications. The target URL for this extension is the earlier IFrame URL. This should continue to work as earlier.
* The tab icon will also be populated into the extension from the earlier application icon and should work as earlier.

---

<a id="sec-changelog"></a>
## Changelog

<a id="pg-docs-changelog"></a>
### Changelog

_Source: <https://onshape-public.github.io/docs/changelog/>_

###### `rel-1.213` \- released 2026-04-03

* New list company users endpoint `GET` : `/companies/{cid}/users`
* Updated `POST` : `/drawings/d/{did}/w/{wid}/e/{eid}/modify` to support creation and modification of ordinate dimensions <https://onshape-public.github.io/docs/api-adv/drawings/#create-ordinate-dimensions>
* Updated documentation for `DELETE` and `POST` for `/companies/{cid}/globalpermission/{type}/{id}` <https://cad.onshape.com/help/Content/Plans/global%5Fpermissions.htm#Assignin>

###### `rel-1.212` \- released 2026-03-13

* Updated `GET` : `/users/settings` and `/users/{uid}/settings` to include a new response property `usePenAsMouse`
* Updated documentation on all release management endpoints `/releasepackages/`
* New tutorial on how to create release packages <https://onshape-public.github.io/docs/api-adv/relmgmt/>

###### `rel-1.211` \- released 2026-02-20

* New `V14` version to the api (<https://cad.onshape.com/api/versions%29>, to return the correct value of referenceType for part studios, assemblies, and bills of materials in /references and /resolvereferences.
* Updated behavior when api version is not recognized, the newest version will be used.
* New tutorial on creating assembly transforms <https://onshape-public.github.io/docs/api-adv/assemblies/#assembly-transforms>
* New tutorial on how to transfer an application to another owner <https://onshape-public.github.io/docs/auth/oauth/#app-ownership>
* New tutorial on how to upload a file in Glassworks <https://onshape-public.github.io/docs/api-intro/explorer/#upload-a-file>
* Fixed schema for file upload parameters, the type is now correctly set to string

###### `rel-1.210` \- released 2026-01-30

* Updated `POST` : `/webhooks` and `/webhooks/{:wid}` added new request property `name`
* Updated `GET` : `/documents/d/{did}/{wvm}/{wvmid}/elements` endpoint when `withZipContents=true` will no longer return names for more than 10 zip files (applies to all versions of the API)
* Fixed incomplete OpenAPI schema for `BTMSketchCurve` to return the attribute `geometry`

###### `rel-1.209` \- released 2026-01-09

* New `V13` version to the api (<https://cad.onshape.com/api/versions%29>, to support creating a version for moving tabs to another document
* Updated `POST` : `/documents/d/{did}/w/{wid}/moveelement` added new request property `sourceVersionName` and `targetVersionName` (V13 or later)
* New tutorial for creating mates and mate connectors <https://onshape-public.github.io/docs/api-adv/assemblies/#create-a-mate-connector-in-an-assembly>
* New tutorial for setting dimension precision <https://onshape-public.github.io/docs/api-adv/drawings/#set-dimension-precision>

###### `rel-1.208` \- released 2025-12-12

* Updated `POST` : `/drawings/d/[:did]/w/[:wid]/e/[:eid]/modify` to support creation and modification of fit class tolerances <https://onshape-public.github.io/docs/api-adv/drawings/#add-fit-class-tolerance-to-a-dimension>
* Updated `POST` : `/drawings/d/[:did]/w/[:wid]/e/[:eid]/modify` to support creation and modification of prefix, suffix, above and below text to drawing dimensions <https://onshape-public.github.io/docs/api-adv/drawings/#add-text-or-symbols-to-a-dimension>

###### `rel-1.206` \- released 2025-10-31

* Updated `POST` : `/appelements/d/[:did]/[:wvm]/[:wvmid]/e/[:eid]/content` now requires specifying `btType` in the `jsonTreeEdit` field
* Updated all `/appelements/` endpoints to include a new required response property `jsonDifference/btType`

###### `rel-1.205` \- released 2025-10-10

* New list standard content endpoint `GET` : `/standardcontent/list`
* New list standard content parameter values endpoint `GET` : `/standardcontent/[:did]/parametervalues`
* New create standard content custom parameters endpoint `POST` : `/standardcontent/[:did]/customparameters`
* Updated `POST` : `/drawings/d/[:did]/w/[:wid]/e/[:eid]/modify` to support creation and modification of dimension tolerances type (symmetrical, deviation, limits, basic, min and max) <https://onshape-public.github.io/docs/api-adv/drawings/#examples---dimensions>
* Support export of title block bounding box in Drawings (DRAWING\_JSON)

###### `rel-1.204` \- released 2025-09-19

* Updated assembly BOM endpoint `/assemblies/d/[:did]/w/[:wid]/e/[:eid]/bom` to include new response property `partIdentity`
* API keys are no longer part of the dev-portal and are now located under the `Developer` area of user preferences, PRO and Enterprise company settings

###### `rel-1.203` \- released 2025-08-29

* Updated `POST` : `/drawings/d/[:did]/w/[:wid]/e/[:eid]/modify` to support the addition and editing of views in drawings: <https://onshape-public.github.io/docs/api-adv/drawings/#examples---views>
* Updated `POST` : `/drawings/d/[:did]/w/[:wid]/e/[:eid]/modify` to support creation and modification of centermarks: <https://onshape-public.github.io/docs/api-adv/drawings/#add-a-centermark-to-a-circular-edge>
* Updated javascript web client to support client messaging to `openFeatureDialog` and `closeFeatureDialog`: <https://onshape-public.github.io/docs/app-dev/clientmessaging/#element-right-panel-extensions>
* Updated details in documentation about how to find the bounding box: <https://onshape-public.github.io/docs/app-dev/drawings/#find-bounding-box-details>
* Updated details in documentation about `logicalID` aliases in the annotation section: <https://onshape-public.github.io/docs/app-dev/drawings/#edit-an-annotation>
* Fixed a specific issue where GD&T symbols can be placed unexpectedly for Drawings modify endpoint
* Fixed an issue where notes can associate to an unexpected view on creation for Drawings modify endpoint

###### `rel-1.202` \- released 2025-08-07

* New webhook event for document share, unshare and share changes `onshape.document.lifecycle.shared`: <https://onshape-public.github.io/docs/app-dev/webhook/#document-group>

###### `rel-1.201` \- released 2025-07-18

* New `V12` version to the api (<https://cad.onshape.com/api/versions%29>, to support translation endpoints checking if input elements match the expected element type
* New update global permissions endpoint (Enterprise) `POST` : `/companies/[:cid]/globalpermission/[type]/[id]`
* New delete global permissions endpoint (Enterprise) `DELETE` : `/companies/[:cid]/globalpermission/[type]/[id]`
* Support export of the bounding box for view in Drawings (DRAWING\_JSON)
* Add `contentType` and `fileExtensions` to the response for `/translations/translationformats` endpoint
* Deprecate `globalPermissions` field for `POST` : `/companies/[:cid]/users[:uid]` (Use new endpoints above for global permission modifications)
* Fixed an issue with updateUserCompany not removing global permissions correctly

###### `rel-1.200` \- released 2025-06-27

* New workflow endpoint (`GET` : `/workflow/obj/[:objectId]`) as a lightweight alternative to (`GET` : `/releasepackages/..` to get status on a release package
* Updated drawings modify endpoint (`POST` : `/drawings/d/[:did]/[:wv]/[:wvid]/e/[:eid]/modify`) with support for export, create, edit and delete of surface finish symbols
* New tutorial for creating surface finish symbols to a drawing and an annotation: <https://onshape-public.github.io/docs/api-adv/drawings/#add-a-surface-finish-symbol-to-a-drawing> <https://onshape-public.github.io/docs/api-adv/drawings/#add-a-surface-finish-symbol-to-an-annotation>
* Updated `DRAWING_JSON` export format to include dimensions to sketched entities
* Updated translations endpoint (`POST` : `/translations/d/[:did]/[:wv]/[:wvid]`) with the optional request property `parasolidMode`: <https://onshape-public.github.io/docs/api-adv/translation/#export-an-assembly-to-a-binary>
* Updated drawings modify endpoint (POST : /drawings/d/\[:did\]/\[:wv\]/\[:wvid\]/e/\[:eid\]/modify) with support for creating sketches in drawings <https://onshape-public.github.io/docs/api-adv/drawings/#examples---create-sketches>
* Fixed missing `parent view id` information using `/drawings/d/[:did]/[:wvm]/[:wvmid]/e/[:eid]/views` API

###### `rel-1.199` \- released 2025-06-06

* New `V11` version to the api (<https://cad.onshape.com/api/versions%29>, added to support `getElementsInDocument` endpoint adds query parameter `withZipContents` to return the contents of a zip file tab
* New assembly direct translation endpionts `POST` : `/d/[:did]/[:wv]/[:wvid]/e/[:eid]/export/gltf`, `/obj` , `/solidworks`, and `/step`: <https://onshape-public.github.io/docs/api-adv/translation/#export-an-assembly-to-gltf-obj-solidworks-or-step>
* New Part Studio direct translation endpionts `POST` : `/d/[:did]/[:wv]/[:wvid]/e/[:eid]/export/gltf`, `/obj` , `/solidworks`, and `/step`: <https://onshape-public.github.io/docs/api-adv/translation/#export-a-part-studio-to-gltf-obj-solidworks-or-step>
* New documents endpoint (`POST` : `/documents/d/[:did]/[:wv]/[:wvid]/contents`) to retrieve tabs and folders inside the document
* New documentation page for Revision and Part number tutorials: <https://onshape-public.github.io/docs/api-adv/relmgmt/>
* Updated blobelements endpoint (`GET` : `/blobelements/d/[:did]/[:wv]/[:wvid]`) with the optional request property `versionDescription`, `versionId` and `versionName`
* Updated blobelements endpoint (`POST` : `/blobelements/d/[:did]/[:wv]/[:wvid]/e/[:eid]`) with the optional request property `versionDescription`, `versionId' and `versionName\`
* Updated translations endpoint (`POST` : `/translations/d/[:did]/[:wv]/[:wvid]`) with the optional request property `versionDescription`, `versionId` and `versionName`
* Updated documents endpoint (`GET` : `/documents/d/[:did]/[:wv]/[:wvid]/elements`) with the optional request property `withZipContents`
* Updated Part Studio features endpoint (`POST` : `/partstudios/d/[:did]/[:wv]/[:wvid]/e/[:eid]/features`) with the optional request property `feature/suppressionState`
* Updated Part Studio direct translation endpoint `POST` : `/d/[:did]/[:wv]/[:wvid]/e/[:eid]/export/step` with request property `stepUnit` as a list of enum values:

| stepUnit                                                 |
| -------------------------------------------------------- |
| CENTIMETER, FOOT, INCH, METER, MILLIMETER, UNKNOWN, YARD |

###### `rel-1.198` \- released 2025-05-16

* New list items endpoint `GET` : `/items`
* New create item endpoint `POST` : `/items`
* New list item endpoint `GET` : `/items/[:iid]`
* New update item endpoint `POST` : `/items/[:iid]`
* New asyncronous STEP export endpoint (`POST` : `/partstudios/d/[:did]/[:wv]/[:wvid]/e/[:eid]/export/step`)
* Updated blobelements endpoint (`POST` : `/blobelements/d/[:did]/[:wv]/[:wvid]`) with the optional request property `repointAppElementVersionRefs`
* Updated blobelements endpoint (`POST` : `/blobelements/d/[:did]/[:wv]/[:wvid]/e/[:eid]`) with the optional request property `repointAppElementVersionRefs`
* Updated document workspace copy endpoint (`POST` : `/documents/[:did]/workspaces/[:wid]/copy`) with the optional request property `repointAppElementVersionRefs`
* Updated insertables endpoints (`GET` : `/documents/d/[:did]/[:wv]/[:wvid]/insertables` and `/insertables/d/[:did]/latest` with new optional `query` request parameter `isObsoletion`)
* Deprecate `GET` : `/releasepackages/companyreleaseworkflow` endpoint
* New tutorial for associating a leader with a drawings view edge: <https://onshape-public.github.io/docs/api-adv/drawings/#associate-a-leader-with-a-view-edge>
* New tutorial for associating an annotation with a drawings view edge: <https://onshape-public.github.io/docs/api-adv/drawings/#associate-an-annotation-with-a-view-edge-without-a-leader>
* Updated description of how to use encoded configurations: <https://onshape-public.github.io/docs/api-adv/configs/#encoded-configurations>
* New tutorial for specifying a configuration during an asynchronous export: <https://onshape-public.github.io/docs/api-adv/configs/#export-a-configured-assembly-asynchronous>

###### `rel-1.197` \- released 2025-04-25

* New appelements subelements endpiont `GET` : `/appelements/d/[:did]/w/[:wid]/e/[:eid]/content/subelements`
* A new response header field `x-deprecated` is now returned when invoking a deprecated API (<https://onshape-public.github.io/docs/api-intro/#onshape-api-response>)
* Updated blobelements endpoint (`POST` : `/blobelements/d/[:did]/[:wv]/[:wvid]`) with the optional request property `documentId` and `preserveSourceIds`
* Updated blobelements endpoint (`POST` : `/blobelements/d/[:did]/[:wv]/[:wvid]/e/[:eid]`) with the optional request property `documentId` and `preserveSourceIds`
* Updated comments endpoint (`POST` : `/comments/[:cid]/attachment`) with the required request property `isMarkup`
* Updated drawings modify endpoint (`POST` : `/drawings/d/[:did]/[:wv]/[:wvid]/e/[:eid]/modify`) with the new optional request property `jsonRequests/items/description`
* Updated translations endpoint (`POST` : `/translations/d/[:did]/[:wv]/[:wvid]`) with the optional request property `documentId` and `preserveSourceIds`
* Updated documentation to address rate limiting 429 requests (<https://onshape-public.github.io/docs/api-adv/errors/#429-too-many-requests>)

###### `rel-1.196` \- released 2025-04-04

* Extensions: Add `sessionCompanyId` as a default query string prarmeter for Drawing tabs
* Fixed an issue that can cause `/glTF` export endpoint to skip certain nested composite parts in an assembly
* Fixed error message when using `/features` to create or update Part Studio features
* Updated documentation for translation endpoints around async vs sync endpoints (<https://onshape-public.github.io/docs/api-adv/translation/>)

###### `rel-1.195` \- released 2025-03-14

* Updated all translation endpoints with new optional request property `rhinoVersion` and `stlMode`
* Updated `GET` : `/assemblies/d/[:did]/[:wv]/[:wvid]/e/[:eid]/matevalues` now supports versions `v`
* Added new documentation for Document CRUD (<https://onshape-public.github.io/docs/api-adv/documents/>)
* Added new documentation for Metadata with python snippets (<https://onshape-public.github.io/docs/api-adv/metadata/>)
* Added new documentation for Drawings tutorial for attaching an annotation to a parent (<https://onshape-public.github.io/docs/api-adv/drawings/#attach-an-annotation-to-a-parent>)
* Fixed unexpected responses for `viewHref` and `href` fields

###### `rel-1.193` \- released 2025-01-31

* Updated `POST` : `/drawings/d/[:did]/w/[:wid]/e/[:eid]/modify` to support creation and modification of chamfer dimensions (<https://onshape-public.github.io/docs/api-adv/drawings/#add-a-chamfer-dimension-to-a-drawing>)
* Updated `POST` : `/drawings/d/[:did]/w/[:wid]/e/[:eid]/modify` to support creation and modification of datums (<https://onshape-public.github.io/docs/api-adv/drawings/#add-a-datum-to-a-drawing>)
* Deprecate request property `addAllDrawingsActive` from `POST` : `/releasepackages/[:rpid]` (automatically done by the server for stability)
* Update `DELETE` : `/documents/d/[:did]/workspaces/[:wid]` to not require global permisson `PermanentlylDelete`

###### `rel-1.192` \- released 2025-01-10

* Updated all translation endpoints with new optional request property `excludeOffSheetContent`
* Updated document export endpoint (`POST` : `/documents/d/[:did]/[:wv]/[:wvid]/e/[:eid]/export`) with the request property `includeCboreCsink`
* Updated release package endpoints (`POST` : `releasepackages/release[:wfid]` and `releasepackages/[:rpid]`) with the request property `items/items/revisionId`
* Updated all configuration endpoints with a new attribute `visibilityCondition` for configuration parameters
* Extensions: Add `sessionCompanyId` as a parameter for the Action URL

###### `rel-1.191` \- released 2024-12-13

* New share anonmyous endpoint `POST` : `/documents/[:did]/acl/anonymousAccess`
* New share public endpoint `POST` : `/documents/[:did]/acl/public`
* Added documentation in the API Guide for Part Studios (<https://onshape-public.github.io/docs/api-adv/partstudios/>)
* Added a quick start video to the API Guide (<https://onshape-public.github.io/docs/api-intro/quickstart/>)

###### `rel-1.190` \- released 2024-11-22

* Added new `V10` version to the api (<https://cad.onshape.com/api/versions%29>, added to support future functionality
* New list assembly matevalues endpiont `GET` : `/assemblies/d/[:did]/w/[:wid]/e/[:eid]/matevalues`
* New create assembly matevalues endpiont `POST` : `/assemblies/d/[:did]/w/[:wid]/e/[:eid]/matevalues`
* Updated export Drawing JSON response to include ‘isDangling’ field
* Fixed issue with Attributes xCenter, yCenter, xDir and yDir not returning in the response for BTCurveGeometryCircle and BTCurveGeometryEllipse
* Added new quick start video to the API Guide (<https://onshape-public.github.io/docs/api-intro/quickstart>)
* Added documentation for export Drawing JSON for inspection symbols having `isDangling` field (<https://onshape-public.github.io/docs/api-adv/drawings/#find-dangling-entities>)
* Updated Features API documentation for creating and updating circles (<https://onshape-public.github.io/docs/api-adv/featureaccess>)

###### `rel-1.189` \- released 2024-11-01

* Updated `POST` : `/drawings/d/[:did]/w/[:wid]/e/[:eid]/modify` with new optional property `outputStatusCode`

###### `rel-1.188` \- released 2024-10-11

* New appelements endpoint to resolve bulk app element references `GET`: `/appelements/d/:[did]/[:wvm]/[:wvimid]/resolvereferences`
* Updated all translation endpoints with new optional request property `evaluateExportRule`
* Updated all translation endpoints with new optional request property `excludeHiddenEntities`
* Updated all translation endpoints with new optional response property `exportRuleFileName`
* Removed from all translation endpoints the request property `invisibleEntitiesExportFilter`
* Removed from `POST` : `/documents/d/[:did]/[:wv]/[:wvid]/e/[:eid]/export` the request property `excludeSuppressedEntities`

###### `rel-1.187` \- released 2024-09-20

* New assembly display states endpoint `GET`: `/assemblies/d/[did]/[wvm]/[wvmid]/e/[eid]/displaystates`
* Updated drawings translation endpoint for the formate `DRAWING_JSON` to include the field `isDangling` on callouts, centerlines, GD&T and notes
* Increase allowed size for `POST` to `/featurestudio` endpoint

###### `rel-1.186` \- released 2024-08-29

* Added new `V9` version to the api (<https://cad.onshape.com/api/versions%29>, returning `deterministicIds` in query responses for `GET` : ‘/features’.
* New list tasks endpoint `GET` : `/tasks`
* New create task endpoint `POST` : `/tasks`
* New list tasks endpoint `GET` : `/tasks/[:tid]`
* New update task endpoint `POST` : `/tasks/[:tid]`
* New transition task endpoint `POST` : `/tasks/[:tid]/[:transition]`
* Updated modify drawings endpoint `POST` : `/drawings/d/[:did]/w/[:wid]/e/[:eid]/modify` to support editing annotations (`messageName` \= `onshapeEditAnnotations`)

###### `rel-1.185` \- released 2024-08-12

* Updated all endpoints that return a user summary (createdBy, modifiedBy) have a new boolean property `isOnshapeSupport` for use to separate Onshape support employee activities.
* Updated all `bodyDetails`, `tessellatededged`, and `tessellatedfaces` endpionts (parts and Part Studios) to include `errorEnum` vales for detecting new mate position, curve pattern and Simulation material checks.

###### `rel-1.184` \- released 2024-07-19

* Updated API version to `V8`, (<https://cad.onshape.com/api/versions%29>, A new microversion will not be created when a document restore operation results in a no-op.
* Remove inconsistencies in assembly definition endpoint (`/assemblies/d/[did]/[wvm]/[wvmid]/e/[eid]`) related to configuration parameters
* Update all translation endpoints (`POST` : `../translations`) to include new request property `useFileNameToSetSinglePartName`
* Update all revision endpoints (`GET` : `/revisions/..`) to include response property `canChangeType` (supporting new admin option to change type part, assembly, file, etc)
* Update `GET` : `/users/[:uid]/settings` endpoint to include responses for `highlightLaminarEdges` and `perspectiveModeOn` for `default` status

###### `rel-1.183` \- released 2024-06-28

* Added new `V7` version to the api (<https://cad.onshape.com/api/versions>)
* Updated `GET` : `V7/partstudios/d/[did]/[wvm]/[wvmid]/e/[eid]/sketches` to return fully defined status (UNDERDEFINED, WELL\_DEFINED, OVERDEFINED, UNKNOWN)
* Updated `GET` : `V7/partstudios/d/[did]/[wvm]/[wvmid]/e/[eid]/sketches` vectors are now maps instead of arrays, and may be `BTVector2d` or `BTVector3d` depending on the `output3D` parameter
* Updated `GET` : `V7/partstudios/d/[did]/[wvm]/[wvmid]/e/[eid]/sketches` to use more consistent naming:

| Fields                               |
| ------------------------------------ |
| sketch \-> name                      |
| sketchId \-> featureId               |
| transformMatrix \-> sketchMatrix     |
| featuresUsed \-> featuresUsingSketch |
| geomEntities \-> entities            |

* Updated `GET` : `/variables` endpoint to return variable description when variable is set through custom feature
* Updated `POST` : `/webhooks` endpoint to default to `isTransient = true` if not specified (auto cleanup)
* Updated descriptions for Assembly, Documents, Metadata, Parts, Part Studios, Revisions, Variables and Versions enddpoints

###### `rel-1.182` \- released 2024-06-07

* Updated descriptions for `webhooks` endpoints

###### `rel-1.181` \- released 2024-05-17

* Update Document, Assembly, Blob, Drawing and Part Studio translation `POST` endpoints to have a new request body property `occurancesToExport`
* Update to `/elements` endpoint summary and descriptions in Glassworks
* Updated documentation for webhooks (<https://onshape-public.github.io/docs/app-dev/webhook/>)

###### `rel-1.180` \- released 2024-04-26

* New Drawings sample application (public repo: <https://github.com/onshape-public/onshapedrawingjson>)
* New API Guide section for response codes (<https://onshape-public.github.io/docs/api-adv/errors/>)
* Support export of tables in JSON of Drawings `GET` : `/appelements/[:did]/[:wvm]/[:wvmid]/e/[:eid]/views/[:viewid]/jsongeometry`
* Update Assembly, Blob, Drawing and Part Studio translation `POST` endpoints to have a new request body property `resolution`

###### `rel-1.179` \- released 2024-04-05

* New drawing views list endpoint `GET` : `/appelements/[:did]/[:wvm]/[:wvmid]/e/[:eid]/views`
* New drawing view endpoint `GET` : `/appelements/[:did]/[:wvm]/[:wvmid]/e/[:eid]/views/[:viewid]/jsongeometry`
* New updated features endpoint documentation
* Updated glassworks for all metadata endpoints to reference developer documentation
* Added description of output to schema for Metadata APIs
* Updated translation endpoints with new request property `specifyMaterialData`

###### `rel-1.178` \- released 2024-03-15

* Update Part Studio translation `POST` endpoint to have a new request body property `importMaterialDensity`
* Update active workflow endpost `GET`: `/workflow/active` to have a new response property `hasInactiveCustomWorkflows`
* Updated authorization (OAuth2 and BasicAuth) for publication endpoints
* Various updates to descriptions of data types and query parameters
* Fixed delete publication endpoint (`HTTP::200` now removes publication)

###### `rel-1.177` \- released 2024-02-23

* Updated translation endpoints with new request property `useIGESImportPostProcessing`
* Updated translation endpoints with modified request property `stepParasolidPreprocessingOption`
* Updated descriptions for `metadata` | `releasepackages` for property `propertyOverrideStatus`

###### `rel-1.176` \- released 2024-02-02

* New create publication endpoint `POST` : `/publications`
* New update publication endpoint `POST`: `/publications/[:pid]`
* New delete publication endpoint `DELETE`: `/publications/[:pid]`
* New create publication item endpoint `POST` : `/publications/item`
* New update publication item endpoint `POST`: `/publications/item/[:iid]`
* New delete publication item endpoint `DELETE`: `/publications/item/[:iid]`

###### `rel-1.175` \- released 2024-01-12

* Exclude suppressed sub assemblies from rootAssembly occurrences for `GET`: `/assemblies/d/[did]/[wvm]/[wvmid]/e/[eid]`

###### `rel-1.174` \- released 2023-12-15

* Add microversion id the extension url `[$microversionId]`
* Updated translation endpoints with new request property `pdfVersion`
* Fixed issue with bodydetails endpoints always returning `isInner` and `isOuter` the same
* Update all endpoints for `bodydetails` | `tessellatededges` | `tessellatedfaces` | `featurescript` to include new response body `errorEnum`:

| errorEnum                                 |
| ----------------------------------------- |
| BODY\_DRAFT\_STRAY\_NONMITER\_EDGES       |
| MASS\_PROPERTY\_FACES\_NOT\_COPLANAR      |
| PARAMETER\_VALUE\_INVALID                 |
| SHEET\_METAL\_CHAMFER\_NO\_TANGENT\_BASED |
| CHAMFER\_DIRECTION\_OVERRIDE\_NO\_EFFECT  |
| FILLET\_CHAMFER\_UNSUPPORTED              |
| CHAMFER\_HELD\_BACK                       |
| SWEEP\_BAD\_LOCK\_DIRECTION               |
| SHEET\_METAL\_COUNTER\_HOLE\_UNSUPPORTED  |
| SWEEP\_SELECT\_DIRECTION                  |

* Update all endpoints for `bodydetails` | `tessellatededges` | `tessellatedfaces` | `featurescript` to include new property `imageForeignId`
* Support sending a list of emails to `POST` : `/classrooms/[cid]/members`

###### `rel-1.173` \- released 2023-11-28

* Update all classroom endpoints (`/classrooms/`) to support OAuth
* Add description of output to schema for getAssemblyShadedViews API

###### `rel-1.172` \- released 2023-11-06

* Update all endpoints for `bodydetails` | `tessellatededges` | `tessellatedfaces` | `featurescript` to include new response body `errorEnum`:

| errorEnum                                    |
| -------------------------------------------- |
| FIT\_TOLERANCE\_LIMITS\_NOT\_FOUND           |
| FIT\_TOLERANCE\_SIZE\_TOO\_LARGE\_ISO        |
| FIT\_TOLERANCE\_SIZE\_TOO\_LARGE\_ANSI       |
| OFFSET\_WIRE\_SHEET\_CREATION\_FAILED        |
| REPLACE\_FACE\_SHEET\_SMALL                  |
| REPLACE\_FACES\_NOT\_ADJACENT                |
| SHEET\_METAL\_HOLE\_REBUILD\_FAILED          |
| CPLANE\_TANGENT\_INPUT                       |
| CPLANE\_TANGENT\_SELECT\_REFERENCE           |
| CNE\_TANGENT\_PLANE\_INVALID                 |
| CPLANE\_TANGENT\_POINT\_INVALID              |
| REPLACE\_FACES\_NOT\_SAME\_BODY              |
| MUST\_USE\_DEFAULT\_RADIUS\_WITH\_FACE\_BEND |
| CANNOT\_RIP\_A\_FACE\_BEND                   |
| CANNOT\_MAKE\_A\_FACE\_BEND\_TANGENT         |

* References to `API Guide` for endpoint descriptions in Glassworks

###### `rel-1.171` \- released 2023-10-13

* Update all translation `POST` endpoints to have a new request body properties `hideInspectionItems` and `textOption`
* Replaced `GET` : `/releasepackages/companyreleaseworkflow` | `/workflow/active` property `canCurrentUserSyncVersionsToArena` with `canCurrentUserSyncStandardContentToArena`
* Updated `GET` and `POST` : `/tabletemplates` endpoint with new response property `valueType`
* Comprehensive update to remaining endpoint summary and descriptions in Glassworks

###### `rel-1.170` \- released 2023-09-22

* New appelements delete subelement endpoint `DELETE` : `/appelements/d/[did]/[wvm]/[wvmid]/e/[eid]/content/subelements`
* New company add new user endoint `POST` : `/companies/[cid]/users`
* New company update user endoint `POST` : `/companies/[cid]/users/[uid]`
* New company delete user endoint `DELETE` : `/companies/[cid]/users/[uid]`
* Comprehensive update to remaining endpoint summary and descriptions in Glassworks

###### `rel-1.169` \- released 2023-09-01

* Comprehensive update to most endpoint summary and descriptions in Glassworks
* Update all translation endpoints to include new property `importAppearances`
* Update `POST` : `/partstudios/d/[did]/[wvm]/[wvmid]/e/[eid]/featurescript` has a new property `expressionErrorInfo`
* Update `GET` and `POST` : `/releasepackages/[rpid]` property `workflow/actions` has a new enum value `REASSIGN_TASK`

###### `rel-1.168` \- released 2023-08-11

* Deprecated `POST` : `/api/drawings/create` \-> Replaced with `POST` : `/api/drawings/d/[did]/w/w/[wid]/create`
* Update `GET` : `/api/documents` endpoint has a new property `publishedVersion`
* Update `GET` and `POST` : `/api/releasepackages/[rpid]` has a new property `syncedWithPLM`

###### `rel-1.167` \- released 2023-07-21

* Update glTF translation endpoints to use new field `useGltfCompression` (bool)
* Update STEP translation endpoints to use new field `stepParasolidPreprocessingOption` (0-None, 1-Advanced, 2-Automatic, 3-Basic)
* Update `GET` : `/api/documents` | `/api/documents/[did]` | `/api/companies/[cid]/documentsbyname` to include new field `forceExportRules`

###### `rel-1.165` \- released 2023-06-12

* Support `partId` array string for `GET` : `/api/partstudios/bodydetails` endpoint for the option of getting a subset of parts from a partstudio (empty = all parts)

###### `rel-1.163` \- released 2023-04-28

* Update documentation for the Documents endpoint (`/api/documents`)
* Update Releasepackage endpoint `GET` : `/api/releasepackage` to include `type` to understand action (ie. Approve vs Reject)
* Update API to V6 - Fix a bug in how updating the JSON tree of an app element in a transaction returns the diff

###### `rel-1.162` \- released 2023-04-12

* New Assembly modify endpoint `POST` : `/api/assemblies/d/{did}/w/{wid}/e/{eid}/modify` for bulk deletion and suppression of instances and features

###### `rel-1.161` \- released 2023-03-20

* New BOM templates endpoint (`/api/tabletemplates`)
* Support POST `/api/webhooks` parameter `isTransient = true` to specify auto cleanup after a set number of days

###### `rel-1.160` \- released 2023-02-24

* Support configuratons for `GET` : `/api/partstudios/d/{did}/{wvm}/{wvmid}/e/{eid}/features`
* Remove deprecated `GET` : `/api/elements/:emid`
* Remove deprecated `GET` and `POST` : `/api/elements/d/:did/[wvm]/:wvmid/e/:eid/metadata`
* Deprecated `GET` and `POST` : `/api/parts/standardcontent/d/:did/v/:vid/e/:eid/[cu]/:cuid/partid/:pid/metadata`
* Deprecated `GET` and `POST` : `/api/parts/d/:did/[wvm]/:wmvid/e/:eid/partid/:pid/metadata`

###### `rel-1.158` \- released 2023-01-11

* New example values in Glassworks API documentation

###### `rel-1.155` \- released 2022-11-01

* Support Parasolid binary (x\_b) exports

###### `rel-1.154` \- released 2022-10-10

* Add face color, hidden state and type of composite to body details endpoint

###### `rel-1.152` \- released 2022-08-30

* Support more parameters to filter the partstudio endpoint

###### `rel-1.147` \- released 2022-05-16

* Support global tree node endpoint for impacting recently opened filter

###### `rel-1.146` \- released 2022-04-25

* Support API versioning
* Return ‘nodeId’ when adding or updating an AppElement

###### `rel-1.145` \- released 2022-04-05

* Fixed issue where assembly feature errors were missing

###### `rel-1.140` \- released 2021-12-15

* Add mass properties for assemblies

###### `rel-1.139` \- released 2021-11-15

* Relax casing search in Glassworks (Swagger client)
* BOM and Metadata API endpoint responses now matched

###### `rel-1.138` \- released 2021-10-25

* Updated webhook documentation

###### `rel-1.135` \- released 2021-8-20

* Webhook events for Enterprise SSO configuration changes

###### `rel-1.134` \- released 2021-07-30

* Support comment events (add, update, delete) for the web-hook endpoint

###### `rel-1.131` \- released 2021-06-01

* Add synchronous glTF/gLB endpoint for assemblies

###### `rel-1.128` \- released 2021-03-29

* Support face color for export of glTF/gLB
* Add document API endpoint for comments

###### `rel-1.127` \- released 2021-03-08

* Add translation option dtkPeriodicFacesPolicy=3 for CATIA parts

###### `rel-1.126` \- released 2021-02-12

* Add GLTF and GLB accepts option to the tessellation APIs

###### `rel-1.125` \- released 2021-01-25

* Add ‘good/better/best’ quality query parameters to tessellation endpoint

###### `rel-1.122` \- released 2020-11-18

* Enforce OAuth endpoint rate limiting
* Add release package action/transition based webhooks

###### `rel-1.119` \- released 2020-09-15

* Add rollback bar to EvalFeatureScript endpoint

###### `rel-1.118` \- released 2020-08-25

* PartStudio GET support for sketch constraints in features endpoint

###### `rel-1.116` \- released 2020-07-15

* Specify starting elements to create document endpoint

###### `rel-1.114` \- released 2020-06-03

* Project endpoints

###### `rel-1.113` \- released 2020-05-11

* Output GLTF files for an element (tab)

###### `rel-1.111` \- released 2020-03-31

* Support ownership transfer for teams

###### `rel-1.110` \- released 2020-03-09

* Add support for exploded views

###### `rel-1.108` \- released 2020-01-29

* Drawings endpoints for create 4 view, get view geometry and view definition

###### `rel-1.102` \- released 2019-09-11

* Added webhook events for release management
* Added webhook event for document version creation

###### `rel-1.99` \- released 2019-07-08

* Assembly BOM API support for items

###### `rel-1.96` \- released 2019-05-03

* Part Studio compare endpoint

###### `rel-1.93` \- released 2019-03-01

* Webhook subscriptions for a company

###### `rel-1.86` \- released 2018-09-28

* Export Drawings to DXF, DWG and PDF

---
