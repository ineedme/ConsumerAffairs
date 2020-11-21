# Review RESTAPI

These API allows reviews to be viewed or edited and JSON response.

## Endpoints that require Authentication

The endpoints require a valid Token to be included in the header of the request.

### Review

Endpoints for viewing and manipulating the Reviews that the Authenticated User
has permissions to access.

* [Show Accessible Reviews](#show-accessible-reviews) : `GET /api/reviews/`
* [Submit Review](#submit-review) : `POST /api/reviews/`
* [Retrieve An Review](#retrieve-single-review) : `GET /api/reviews/:pk/`
* [Update An Review](#delete-review) : `PUT /api/reviews/:pk/`
* [Delete An Review](#delete-review) : `DELETE /api/reviews/:pk/`

# Show Accessible Reviews

Show all Reviews the active User can access.

**URL** : `/api/reviews/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : 
Reviews that had been submit by the current user.

## Success Responses

**Condition** : User cannot see any Reviews.

**Code** : `200 OK`

**Content** : `{[]}`

### OR

**Condition** : User can see one or more Reviews.

**Code** : `200 OK`

**Example** : 

```json
[
    {
        "id": 1,
        "rating": 1,
        "title": "Great Company",
        "summary": "Awesome Company to work",
        "ip_address": "192.168.10.51",
        "submitted_at": "2020-11-19T16:16:41.858000Z",
        "company": 1,
        "reviewer": 1
    },
    {
        "id": 6,
        "rating": 1,
        "title": "Apple",
        "summary": "Rotten",
        "ip_address": "192.168.1.1",
        "submitted_at": "2020-11-20T15:43:29Z",
        "company": 1,
        "reviewer": 1
    }
]
```

# Submit Review

Submit Review for the authenticated User.

**URL** : `/api/reviews/`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : None

**Data constraints**

Provide data of Review to be submitted.
All fields must be sent.

```json
{
    "rating": 1,
    "title": "Great Company",
    "summary": "Awesome Company to work",
    "company": 1
}
```

## Success Response

**Condition** : If everything is OK.

**Code** : `201 CREATED`

**Content example**

```json
{
    "id": 11,
    "rating": 1,
    "title": "Same Old",
    "summary": "Same Old",
    "ip_address": "127.0.0.1",
    "submitted_at": "2020-11-21T08:44:32.814878Z",
    "company": 1,
    "reviewer": 1
}
```

## Error Responses


**Condition** : If fields are missed.

**Code** : `400 BAD REQUEST`

**Content example**

```json
{
    "title": [
        "This field may not be blank."
    ],
    "summary": [
        "This field may not be blank."
    ]
}
```

# Retrieve Single Review

Show a single Review if current User has access to it.

**URL** : `/api/reviews/:pk/`

**URL Parameters** : `pk=[integer]` where `pk` is the ID of the Review on the server.

**Method** : `GET`

**Auth required** : YES

**Permissions required** :

User is the Reviewer of the Review requested:

**Data**: `{}`

## Success Response

**Condition** : If Review exists.

**Code** : `200 OK`

**Content example**

```json
{
        "id": 6,
        "rating": 1,
        "title": "Apple",
        "summary": "Rotten",
        "ip_address": "192.168.1.1",
        "submitted_at": "2020-11-20T15:43:29Z",
        "company": 1,
        "reviewer": 1
    }
```

## Error Responses

**Condition** : If Review does not exist with `id` of provided `pk` parameter.

**Code** : `404 NOT FOUND`

**Content** : 
`{
    "detail": "Not found."
}`

### Or

**Condition** : If Review exists but Authorized User is not the Reviewer.

**Code** : `404 NOT FOUND`

**Content** :

```json
{
    "detail": "Not found."
}
```

    
# Update Review

Update the Review of the Authenticated User.

**URL** : `/api/reviews/:pk/`

**Method** : `PUT`

**Auth required** : YES

**Permissions required** : Current User is the Reviewer

**Data example** 

```json
{
    "rating": 1,
    "title": "Great Company",
    "summary": "Awesome Company to work",
    "company": 1
}
```

## Success Responses

**Condition** : Update can be performed by the Reviewer.

**Code** : `200 OK`

**Content example** :

```json
{
        "id": 6,
        "rating": 1,
        "title": "Apple",
        "summary": "Rotten",
        "ip_address": "192.168.1.1",
        "submitted_at": "2020-11-20T15:43:29Z",
        "company": 1,
        "reviewer": 1
    }
```

## Error Response

**Condition** : Review does not exist at URL

**Code** : `404 NOT FOUND`

**Content** : 
`{
    "detail": "Not found."
}`

### Or

**Condition** : Authorized User is not the Reviewer of the Review.

**Code** : `403 FORBIDDEN`

**Content** : `{}`

## Notes

### Data ignored

Endpoint will ignore irrelevant and read-only data such as parameters that
don't exist, or `id` and `reviewer` fields which are not editable.

E.g. if Reviewer already exits:

**Data example**

```json
{
    "rating": 1,
    "title": "Great Company",
    "summary": "Awesome Company to work",
    "company": 1
}
```

**Code** : `200 OK`

**Content example**

```json
{
        "id": 6,
        "rating": 1,
        "title": "Apple",
        "summary": "Rotten",
        "ip_address": "192.168.1.1",
        "submitted_at": "2020-11-20T15:43:29Z",
        "company": 1,
        "reviewer": 1
    }
```

# Delete Review

Delete the Review of the Authenticated User if he is the Reviewer.

**URL** : `/api/reviews/:pk/`

**URL Parameters** : `pk=[integer]` where `pk` is the ID of the Review in the database.

**Method** : `DELETE`

**Auth required** : YES

**Permissions required** : User is Review Reviewer

**Data** : `{}`

## Success Response

**Condition** : If the Review exists.

**Code** : `204 NO CONTENT`

**Content** : `{}`

## Error Responses

**Condition** : If there was no Review available to delete.

**Code** : `404 NOT FOUND`

**Content** : `{}`

### Or

**Condition** : Authorized User is not the Reviewer of the Review.

**Code** : `404 NOT FOUND`

**Content** : `{}`
