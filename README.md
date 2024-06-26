# Market Next Door

## Introduction
Welcome to the backend repository of Market Next Door! Market Next Door is a application to connect a local vender with a customer to establish preorders for an upcoming farmers market. This repository houses the codebase for our backend services, crafted using Python and the Django REST framework.

---
## Table of Contents
- [Introduction](#introduction)
- [Table of Contents](#table-of-contents)
- [Directory](#directory)
- [Tech Stack](#tech-stack)
- [Key Features](#key-features)
- [Getting Started](#getting-started)
- [RESTful Endpoints](#restful-endpoints)
  - [V1](#v1)
    - [Markets](#markets)
    - [Customers](#customers)
    - [Vendors](#vendors)
    - [Items](#items)
    - [Preorders](#preorders)
    - [Weather](#weather-v2)
  - [V2](#v2)
    - [Markets](#markets)
    - [Customers](#customers)
    - [Vendors](#vendors)
    - [Customers by Market](#customers-by-market)
    - [Vendors by Market](#vendors-by-market)
    - [Items](#items)
    - [Customer Preorders](#customer-preorders)
    - [Vendor Preorders](#vendor-preorders)
    - [Vendor Markets](#vendor-markets)
    - [Customer Markets](#customer-markets)
    - [Weather](#weather-v2)
- [Team](#team)
---

## Directory
[Hosted Website](https://market-next-door-fe-f6728ad38b62.herokuapp.com/)

[Hosted Server](https://quiet-depths-54407-77a00505f51e.herokuapp.com/)

## Tech Stack
<a href="https://www.python.org/" target="_blank"><img style="margin: 15px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" height="50" /></a>
<a href="https://www.djangoproject.com/" target="_blank"><img style="margin: 15px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" alt="Django" height="50" /></a>
<a href="https://aws.amazon.com/?nc2=h_lg" target="_blank"><img style="margin: 15px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/amazonwebservices/amazonwebservices-plain-wordmark.svg" alt="Amazon Web Services logo" height="50" /></a>
- **Python:** Our primary programming language offering simplicity and versatility
- **Django REST Framework:** Used for building API's, ensuring a scalable and secure connection between our frontend and backend services.

## Key Features 
1. **AWS Integration:** S3 file storage and CloudFront CDN to deliver the S3 assets.
2. **Data Management:** Employs Django ORM for seamless database queries and data manipulation.
3. **Preorder Management:** Handles all CRUD operations related to Preorders, enabling the creation, updates, and deletion.
---
## Getting Started
1. **Clone the Repository:** Get started with Market Next Door Backend by cloning the repository to your local machine.
2. **Install Requirements:** Navigate into the cloned repository and install necessary dependencies
3. **Start the Server:** Start the Django server.
Note: Please ensure you have Python and pip installed on your machine before running these commands.

## RESTful Endpoints

Base url to reach the endpoints listed below:
```
https://quiet-depths-54407-77a00505f51e.herokuapp.com/
```

## V1
<details close>

### Markets
```
Get /api/v1/markets/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

[
    {
        "id": 1,
        "market_name": "Denver Saturday Market",
        "location": "Denver, CO",
        "details": "All the vendors!!",
        "start_date": "2023-12-06",
        "end_date": "2023-12-06",
        "date_created": "2023-12-06T18:02:28.458557Z",
        "updated_at": "2023-12-06T18:02:28.458571Z"
    }
]
```

</details>
<br>

```
Post /api/v1/markets/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
     {
        "id": 1,
        "market_name": "Denver Saturday Market",
        "location": "Denver, CO",
        "details": "All the vendors!!",
        "start_date": "2023-12-06",
        "end_date": "2023-12-06",
        "date_created": "2023-12-06T18:02:28.458557Z",
        "updated_at": "2023-12-06T18:02:28.458571Z"
    }
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json

{
    "id": 1,
    "market_name": "Denver Saturday Market",
    "location": "Denver, CO",
    "details": "All the vendors!!",
    "start_date": "2023-12-06",
    "end_date": "2023-12-06",
    "date_created": "2023-12-06T18:02:28.458557Z",
    "updated_at": "2023-12-06T18:02:28.458571Z"
}
```

</details>


#### Markets (External API)
```
Get /api/v1/markets/location/:zipcode/:radius/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
/api/v1/markets/location/78750/5/
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

[
    {
        "market_name": "Texas Farmers' Market at Lakeline",
        "address": "Lakeline Mall parking lot, behind Sears & Dillard's, Cedar Park, Texas 78613",
        "lat": "-97.806683",
        "lon": "30.469036",
        "website": "www.TexasFarmersMarket.org",
        "zipcode": "78613",
        "phone": "5129537959"
    },
    {
        "market_name": "AUSTIN FARMERS MARKET",
        "address": "9607 RESEARCH BLVD, AUSTIN, Texas 78759",
        "lat": "-97.741448",
        "lon": "30.387094",
        "website": "www.farmergeorge.market",
        "zipcode": "78759",
        "phone": "9562867775"
    }
]
```

</details>
<br>

---

### Customers

```
Get /api/v1/customers/  (for all customers)
Get /api/v1/customers/:customer_id/ (for single customer)
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

[
    {
        "id": 3,
        "first_name": "Market",
        "last_name": "Next Door",
        "phone": "4565421346",
        "email": "Market@gmail.com",
        "location": "location"
    },
    {
        "id": 4,
        "first_name": "Is the",
        "last_name": "Best!",
        "phone": "4565421346",
        "email": "NextDoor@gmail.com",
        "location": "location"
    }
]
```

</details>
<br>

```
Post /api/v1/customers/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
     {
        "id": 1,
        "market_name": "Denver Saturday Market",
        "location": "Denver, CO",
        "details": "All the vendors!!",
        "start_date": "2023-12-06",
        "end_date": "2023-12-06",
        "date_created": "2023-12-06T18:02:28.458557Z",
        "updated_at": "2023-12-06T18:02:28.458571Z"
    }
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json

{
    "id": 5,
    "first_name": "Market",
    "last_name": "NextDoor",
    "phone": "4565421346",
    "email": "george@gmail.com",
    "password": "134134",
    "location": "location"
}
```

</details>
<br>

```
Put /api/v1/customers/:customer_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
     {
    "id": 5,
    "first_name": "Market",
    "last_name": "UPDATE",
    "phone": "4565421346",
    "email": "george@gmail.com",
    "location": "UPDATE"
     }
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "id": 5,
    "first_name": "Market",
    "last_name": "UPDATE",
    "phone": "4565421346",
    "email": "george@gmail.com",
    "location": "UPDATE"
}
```

</details>
<br>

```
Delete /api/v1/customer/:customer_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

| Code | Description |
| :--- | :--- |
| 204 | `No Content` |

</details>

___

### Vendors

```
Get /api/v1/vendors/  (for all vendors)
Get /api/v1/vendors/:vendor_id/ (for single vendor)
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

[
    {
        "id": 1,
        "market": 1,
        "vendor_name": "Potato Vendor",
        "first_name": "Joseph's",
        "last_name": "Potatoes",
        "email": "jp@gmail.com",
        "location": "Cental Ln"
    },
    {
        "id": 2,
        "market": 1,
        "vendor_name": "Another Potato Vendor",
        "first_name": "Terry's",
        "last_name": "Potatoes",
        "email": "jp@gmail.com",
        "location": "Cental Ln"
    }
]
```

</details>
<br>

```
Post /api/v1/vendors/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
     {
    "market": null,
    "vendor_name": "Saturday Market",
    "first_name": "George",
    "last_name": "Picket",
    "email": "gpicket@gmail.com",
    "location": null
     }
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json

{
    "id": 2,
    "market": null,
    "vendor_name": "Saturday Market",
    "first_name": "George",
    "last_name": "Picket",
    "email": "gpicket@gmail.com",
    "location": null
}
```

</details>
<br>

```
Put /api/v1/vendors/:vendor_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
     {
    "id": 2,
    "market": 1,
    "vendor_name": "Saturday Market",
    "first_name": "George",
    "last_name": "Picket",
    "email": "gpicket@gmail.com",
    "location": "location_info"
     }
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "id": 2,
    "market": 1,
    "vendor_name": "Saturday Market",
    "first_name": "George",
    "last_name": "Picket",
    "email": "gpicket@gmail.com",
    "location": "location_info"
}
```

</details>
<br>

```
Delete /api/v1/vendors/:vendor_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

| Code | Description |
| :--- | :--- |
| 204 | `No Content` |

</details>

___

### Items

```
Get /api/v1/vendors/:vendor_id/items/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

[
    {
        "id": 3,
        "item_name": "Red Potatoes",
        "vendor": 1,
        "price": "3.00",
        "size": "2 lb",
        "quantity": 6,
        "availability": false,
        "description": "Red Potatoes!",
        "image": null,
        "date_created": "2023-12-06T18:08:57.592411Z",
        "updated_at": "2023-12-07T04:02:29.086898Z"
    }
]
```

</details>
<br>

```
Post /api/v1/vendors/:vendor_id/items/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
     {
        "item_name": "garlic",
        "vendor": 1,
        "price": "1.99",
        "size": "each",
        "quantity": 250,
        "availability": true,
        "description": "GARLIC",
        "image": null,
    }
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json

{
        "id": 6,
        "item_name": "garlic",
        "vendor": 1,
        "price": "1.99",
        "size": "each",
        "quantity": 250,
        "availability": true,
        "description": "GARLIC",
        "image": null,
        "date_created": "2023-12-07T21:44:17.012677Z",
        "updated_at": "2023-12-07T21:44:17.012693Z"
    }
```

</details>
<br>

```
Put /api/v1/vendors/:vendor_id/items/:item_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
     {
        "id": 6,
        "item_name": "garlic",
        "vendor": 1,
        "price": "1.99",
        "size": "each",
        "quantity": 250,
        "availability": true,
        "description": "Not GARLIC",
        "image": null,
    }
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
        "id": 6,
        "item_name": "garlic",
        "vendor": 1,
        "price": "1.99",
        "size": "each",
        "quantity": 250,
        "availability": true,
        "description": "Not GARLIC",
        "image": null,
}
```

</details>
<br>

```
Delete /api/v1/vendors/:vendor_id/items/:item_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

| Code | Description |
| :--- | :--- |
| 204 | `No Content` |

</details>

___

### PreOrders 
### (customer)

```
Get /api/v1/customers/:customer_id/preorders/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

[
    {
        "id": 1,
        "customer": 1,
        "item": 1,
        "packed": false,
        "fulfilled": false,
        "ready": true,
        "quantity_requested": 5,
        "vendor_id": 1,
        "date_created": "2023-12-06T18:05:43.715193Z",
        "updated_at": "2023-12-07T16:36:37.206279Z"
    }
]
```

</details>
<br>

```
Post /api/v1/customers/:customer_id/preorders/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
     {
        "item": 1,
        "quantity_requested": 5,
    }
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json

{
        "id": 1,
        "customer": 1,
        "item": 1,
        "packed": false,
        "fulfilled": false,
        "ready": true,
        "quantity_requested": 5,
        "vendor_id": 1,
        "date_created": "2023-12-06T18:05:43.715193Z",
        "updated_at": "2023-12-07T16:36:37.206279Z"
}
```

</details>
<br>

```
Put /api/v1/customers/:customer_id/preorders/:preorder_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
{
    "item": 1,
    "quantity_requested": 6,
}
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "id": 1,
    "customer": 1,
    "item": 1,
    "packed": false,
    "fulfilled": false,
    "ready": true,
    "quantity_requested": 6,
    "vendor_id": 1,
    "date_created": "2023-12-06T18:05:43.715193Z",
    "updated_at": "2023-12-07T16:36:37.206279Z"
}
```

</details>
<br>

```
Delete /api/v1/customers/:customer_id/preorders/:preorder_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

| Code | Description |
| :--- | :--- |
| 204 | `No Content` |

</details>

### (Vendor)

```
Get /api/v1/vendors/:vendor_id/preorders/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

[
    {
        "id": 5,
        "customer": 1,
        "item": 1,
        "packed": false,
        "fulfilled": false,
        "ready": true,
        "quantity_requested": 12,
        "vendor_id": 1,
        "date_created": "2023-12-07T04:11:14.470164Z",
        "updated_at": "2023-12-07T04:11:14.470176Z"
    }
]
```

</details>
<br>

```
Post /api/v1/vendors/:vendor_id/preorders/:preorder_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
{
    "id": 5,
    "customer": 1,
    "item": 1,
    "packed": false,
    "fulfilled": false,
    "ready": true,
    "quantity_requested": 12,
}
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json

{
    "id": 5,
    "customer": 1,
    "item": 1,
    "packed": false,
    "fulfilled": false,
    "ready": true,
    "quantity_requested": 12,
    "vendor_id": 1,
    "date_created": "2023-12-07T04:11:14.470164Z",
    "updated_at": "2023-12-07T04:11:14.470176Z"
}
```

</details>
<br>

```
Put /api/v1/vendors/:vendor_id/preorders/:preorder_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
{
    "item": 1,
    "packed": false,
    "fulfilled": false,
    "ready": true,
    "quantity_requested": 12,
}
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "id": 5,
    "customer": 1,
    "item": 1,
    "packed": false,
    "fulfilled": false,
    "ready": true,
    "quantity_requested": 12,
    "vendor_id": 1,
    "date_created": "2023-12-07T04:11:14.470164Z",
    "updated_at": "2023-12-07T04:11:14.470176Z"
}
```

</details>
<br>

```
Delete /api/v1/vendors/:vendor_id/preorders/:preorder_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

| Code | Description |
| :--- | :--- |
| 204 | `No Content` |

</details>

___

### Weather

```
Get /api/v1/weather/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
Parameters: zipcode
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

    {
        "description": "overcast clouds",
        "temp": 35,
        "icon": "04d"
    }
```

</details>
<br>

</details>

---

## V2
<details close>

### Markets
```
Get /api/v2/markets/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

[
    {
        "id": 1,
        "market_name": "Denver Saturday Market",
        "location": "Denver, CO",
        "details": "All the vendors!!",
        "start_date": "2023-12-06",
        "end_date": "2023-12-06",
        "date_created": "2023-12-06T18:02:28.458557Z",
        "updated_at": "2023-12-06T18:02:28.458571Z"
    }
]
```

</details>
<br>

```
Post /api/v2/markets/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
     {
        "id": 1,
        "market_name": "Denver Saturday Market",
        "location": "Denver, CO",
        "details": "All the vendors!!",
        "start_date": "2023-12-06",
        "end_date": "2023-12-06",
        "date_created": "2023-12-06T18:02:28.458557Z",
        "updated_at": "2023-12-06T18:02:28.458571Z"
    }
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json

{
    "id": 1,
    "market_name": "Denver Saturday Market",
    "location": "Denver, CO",
    "details": "All the vendors!!",
    "start_date": "2023-12-06",
    "end_date": "2023-12-06",
    "date_created": "2023-12-06T18:02:28.458557Z",
    "updated_at": "2023-12-06T18:02:28.458571Z"
}
```

</details>


#### Markets (External API)
```
Get /api/v2/markets/location/:zipcode/:radius/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
/api/v2/markets/location/78750/5/
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

[
    {
        "market_name": "Texas Farmers' Market at Lakeline",
        "address": "Lakeline Mall parking lot, behind Sears & Dillard's, Cedar Park, Texas 78613",
        "lat": "-97.806683",
        "lon": "30.469036",
        "website": "www.TexasFarmersMarket.org",
        "zipcode": "78613",
        "phone": "5129537959"
    },
    {
        "market_name": "AUSTIN FARMERS MARKET",
        "address": "9607 RESEARCH BLVD, AUSTIN, Texas 78759",
        "lat": "-97.741448",
        "lon": "30.387094",
        "website": "www.farmergeorge.market",
        "zipcode": "78759",
        "phone": "9562867775"
    }
]
```

</details>
<br>

---

### Customers

```
Get /api/v2/customers/  (for all customers)
Get /api/v2/customers/:customer_id/ (for single customer)
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

[
    {
        "id": 3,
        "first_name": "Market",
        "last_name": "Next Door",
        "phone": "4565421346",
        "email": "Market@gmail.com",
        "location": "location"
    },
    {
        "id": 4,
        "first_name": "Is the",
        "last_name": "Best!",
        "phone": "4565421346",
        "email": "NextDoor@gmail.com",
        "location": "location"
    }
]
```

</details>
<br>

```
Post /api/v2/customers/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
     {
        "id": 1,
        "market_name": "Denver Saturday Market",
        "location": "Denver, CO",
        "details": "All the vendors!!",
        "start_date": "2023-12-06",
        "end_date": "2023-12-06",
        "date_created": "2023-12-06T18:02:28.458557Z",
        "updated_at": "2023-12-06T18:02:28.458571Z"
    }
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json

{
    "id": 5,
    "first_name": "Market",
    "last_name": "NextDoor",
    "phone": "4565421346",
    "email": "george@gmail.com",
    "password": "134134",
    "location": "location"
}
```

</details>
<br>

```
Put /api/v2/customers/:customer_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
     {
    "id": 5,
    "first_name": "Market",
    "last_name": "UPDATE",
    "phone": "4565421346",
    "email": "george@gmail.com",
    "location": "UPDATE"
     }
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "id": 5,
    "first_name": "Market",
    "last_name": "UPDATE",
    "phone": "4565421346",
    "email": "george@gmail.com",
    "location": "UPDATE"
}
```

</details>
<br>

```
Delete /api/v2/customer/:customer_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

| Code | Description |
| :--- | :--- |
| 204 | `No Content` |

</details>

___

### Vendors

```
Get /api/v2/vendors/  (for all vendors)
Get /api/v2/vendors/:vendor_id/ (for single vendor)
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

[
    {
        "id": 1,
        "market": 1,
        "vendor_name": "Potato Vendor",
        "first_name": "Joseph's",
        "last_name": "Potatoes",
        "email": "jp@gmail.com",
        "location": "Cental Ln"
    },
    {
        "id": 2,
        "market": 1,
        "vendor_name": "Another Potato Vendor",
        "first_name": "Terry's",
        "last_name": "Potatoes",
        "email": "jp@gmail.com",
        "location": "Cental Ln"
    }
]
```

</details>
<br>

```
Post /api/v2/vendors/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
     {
    "market": null,
    "vendor_name": "Saturday Market",
    "first_name": "George",
    "last_name": "Picket",
    "email": "gpicket@gmail.com",
    "location": null
     }
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json

{
    "id": 2,
    "market": null,
    "vendor_name": "Saturday Market",
    "first_name": "George",
    "last_name": "Picket",
    "email": "gpicket@gmail.com",
    "location": null
}
```

</details>
<br>

```
Put /api/v2/vendors/:vendor_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
     {
    "id": 2,
    "market": 1,
    "vendor_name": "Saturday Market",
    "first_name": "George",
    "last_name": "Picket",
    "email": "gpicket@gmail.com",
    "location": "location_info"
     }
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "id": 2,
    "market": 1,
    "vendor_name": "Saturday Market",
    "first_name": "George",
    "last_name": "Picket",
    "email": "gpicket@gmail.com",
    "location": "location_info"
}
```

</details>
<br>

```
Delete /api/v2/vendors/:vendor_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

| Code | Description |
| :--- | :--- |
| 204 | `No Content` |

</details>

---

### Customers by Market
```
Get /api/v2/markets/:market_id/customers/  (for all customers at that market)
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json
[
    {
        "id": 3,
        "first_name": "Market",
        "last_name": "Next Door",
        "phone": "4565421346",
        "email": "Market@gmail.com",
        "location": "location"
    },
    {
        "id": 4,
        "first_name": "Is the",
        "last_name": "Best!",
        "phone": "4565421346",
        "email": "NextDoor@gmail.com",
        "location": "location"
    }
]
```

</details>
<br>

```
Post /api/v2/markets/:market_id/customers/    (Create an association between a customer and a market)
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
{
    "id": 2
}
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json

{
    "message": "Customer association created successfully."
}
```

</details>
<br>

```
Get /api/v2/markets/:market_id/customers/:customer_id/ (for a single customer at that market)
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json
{
    "id": 3,
    "first_name": "Market",
    "last_name": "Next Door",
    "phone": "4565421346",
    "email": "Market@gmail.com",
    "location": "location"
}
```

</details>
<br>

```
Delete /api/v2/markets/:market_id/customers/:customer_id/    (Delete an association between a customer and a market)
```

<details close>
<summary> Endpoint Details </summary>
<br>

| Code | Description |
| :--- | :--- |
| 204 | `No Content` |

</details>

---

### Vendors by Market

```
Get /api/v2/markets/:market_id/vendors/  (for all vendors at that market)
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

[
    {
        "id": 1,
        "market": 1,
        "vendor_name": "Potato Vendor",
        "first_name": "Joseph's",
        "last_name": "Potatoes",
        "email": "jp@gmail.com",
        "location": "Cental Ln"
    },
    {
        "id": 2,
        "market": 1,
        "vendor_name": "Another Potato Vendor",
        "first_name": "Terry's",
        "last_name": "Potatoes",
        "email": "jp@gmail.com",
        "location": "Cental Ln"
    }
]
```

</details>
<br>

```
Post /api/v2/markets/:market_id/vendors/    (Create an association between a vendor and a market)
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
{
    "id": 2
}
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json

{
    "message": "Vendor association created successfully."
}
```

</details>
<br>

```
Get /api/v2/markets/:market_id/vendors/:vendor_id/ (for a single vendor at that market)
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json
{
    "id": 1,
    "market": 1,
    "vendor_name": "Potato Vendor",
    "first_name": "Joseph's",
    "last_name": "Potatoes",
    "email": "jp@gmail.com",
    "location": "Cental Ln"
}
```

</details>
<br>

```
Delete /api/v2/markets/:market_id/vendors/:vendor_id/    (Delete an association between a vendor and a market)
```

<details close>
<summary> Endpoint Details </summary>
<br>

| Code | Description |
| :--- | :--- |
| 204 | `No Content` |

</details>


---

### Items

```
Get /api/v2/vendors/:vendor_id/items/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

[
    {
        "id": 3,
        "item_name": "Red Potatoes",
        "vendor": 1,
        "price": "3.00",
        "size": "2 lb",
        "quantity": 6,
        "availability": false,
        "description": "Red Potatoes!",
        "image": null,
        "date_created": "2023-12-06T18:08:57.592411Z",
        "updated_at": "2023-12-07T04:02:29.086898Z"
    }
]
```

</details>
<br>

```
Post /api/v2/vendors/:vendor_id/items/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
     {
        "item_name": "garlic",
        "vendor": 1,
        "price": "1.99",
        "size": "each",
        "quantity": 250,
        "availability": true,
        "description": "GARLIC",
        "image": null,
    }
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json

{
        "id": 6,
        "item_name": "garlic",
        "vendor": 1,
        "price": "1.99",
        "size": "each",
        "quantity": 250,
        "availability": true,
        "description": "GARLIC",
        "image": null,
        "date_created": "2023-12-07T21:44:17.012677Z",
        "updated_at": "2023-12-07T21:44:17.012693Z"
    }
```

</details>
<br>

```
Put /api/v2/vendors/:vendor_id/items/:item_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
     {
        "id": 6,
        "item_name": "garlic",
        "vendor": 1,
        "price": "1.99",
        "size": "each",
        "quantity": 250,
        "availability": true,
        "description": "Not GARLIC",
        "image": null,
    }
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
        "id": 6,
        "item_name": "garlic",
        "vendor": 1,
        "price": "1.99",
        "size": "each",
        "quantity": 250,
        "availability": true,
        "description": "Not GARLIC",
        "image": null,
}
```

</details>
<br>

```
Delete /api/v2/vendors/:vendor_id/items/:item_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

| Code | Description |
| :--- | :--- |
| 204 | `No Content` |

</details>

---

### Customer Preorders

```
Get /api/v2/markets/:market_id/customers/:customer_id/preorders/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

[
    {
        "id": 1,
        "customer": 1,
        "item": 1,
        "packed": false,
        "fulfilled": false,
        "ready": true,
        "quantity_requested": 5,
        "vendor_id": 1,
        "date_created": "2023-12-06T18:05:43.715193Z",
        "updated_at": "2023-12-07T16:36:37.206279Z"
    }
]
```

</details>
<br>

```
Post /api/v2/markets/:market_id/customers/:customer_id/preorders/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
     {
        "item": 1,
        "quantity_requested": 5,
    }
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json

{
        "id": 1,
        "customer": 1,
        "item": 1,
        "packed": false,
        "fulfilled": false,
        "ready": true,
        "quantity_requested": 5,
        "vendor_id": 1,
        "date_created": "2023-12-06T18:05:43.715193Z",
        "updated_at": "2023-12-07T16:36:37.206279Z"
}
```

</details>
<br>

```
Put /api/v2/markets/:market_id/customers/:customer_id/preorders/:preorder_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
{
    "item": 1,
    "quantity_requested": 6,
}
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "id": 1,
    "customer": 1,
    "item": 1,
    "packed": false,
    "fulfilled": false,
    "ready": true,
    "quantity_requested": 6,
    "vendor_id": 1,
    "date_created": "2023-12-06T18:05:43.715193Z",
    "updated_at": "2023-12-07T16:36:37.206279Z"
}
```

</details>
<br>

```
Delete /api/v2/markets/:market_id/customers/:customer_id/preorders/:preorder_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

| Code | Description |
| :--- | :--- |
| 204 | `No Content` |

</details>

---

### Vendor Preorders

```
Get /api/v2/markets/:market_id/vendors/:vendor_id/preorders/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

[
    {
        "id": 5,
        "customer": 1,
        "item": 1,
        "packed": false,
        "fulfilled": false,
        "ready": true,
        "quantity_requested": 12,
        "vendor_id": 1,
        "date_created": "2023-12-07T04:11:14.470164Z",
        "updated_at": "2023-12-07T04:11:14.470176Z"
    },
    {
        "id": 6,
        "customer": 20,
        "item": 1,
        "packed": false,
        "fulfilled": false,
        "ready": true,
        "quantity_requested": 2,
        "vendor_id": 1,
        "date_created": "2023-12-07T04:11:14.470164Z",
        "updated_at": "2023-12-07T04:11:14.470176Z"
    }
]
```

</details>
<br>

```
Get /api/v2/markets/:market_id/vendors/:vendor_id/preorders/:preorder_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json
{
    "id": 5,
    "customer": 1,
    "item": 1,
    "packed": false,
    "fulfilled": false,
    "ready": true,
    "quantity_requested": 12,
    "vendor_id": 1,
    "date_created": "2023-12-07T04:11:14.470164Z",
    "updated_at": "2023-12-07T04:11:14.470176Z"
}
```

</details>
<br>

```
Post /api/v2/markets/:market_id/vendors/:vendor_id/preorders/:preorder_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
{
    "id": 5,
    "customer": 1,
    "item": 1,
    "packed": false,
    "fulfilled": false,
    "ready": true,
    "quantity_requested": 12,
}
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json

{
    "id": 5,
    "customer": 1,
    "item": 1,
    "packed": false,
    "fulfilled": false,
    "ready": true,
    "quantity_requested": 12,
    "vendor_id": 1,
    "date_created": "2023-12-07T04:11:14.470164Z",
    "updated_at": "2023-12-07T04:11:14.470176Z"
}
```

</details>
<br>

```
Put /api/v2/markets/:market_id/vendors/:vendor_id/preorders/:preorder_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
{
    "item": 1,
    "packed": false,
    "fulfilled": false,
    "ready": true,
    "quantity_requested": 12,
}
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

{
    "id": 5,
    "customer": 1,
    "item": 1,
    "packed": false,
    "fulfilled": false,
    "ready": true,
    "quantity_requested": 12,
    "vendor_id": 1,
    "date_created": "2023-12-07T04:11:14.470164Z",
    "updated_at": "2023-12-07T04:11:14.470176Z"
}
```

</details>

---

### Vendor Markets
```
Get /api/v2/vendors/:vendor_id/markets/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json
[
	{
		"id": 4,
		"vendor": 1,
		"market": 2,
		"active": true,
		"date_created": "2024-04-12T12:00:00Z",
		"updated_at": "2024-04-11T21:42:24.850243Z"
	},
	{
		"id": 12,
		"vendor": 1,
		"market": 1,
		"active": true,
		"date_created": "2024-04-12T12:00:00Z",
		"updated_at": "2024-04-11T22:14:46.441837Z"
	}
]
```

</details>
<br>

```
Post /api/v2/vendors/:vendor_id/markets/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
{
    "vendor": 1,
    "market": 3
}
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json
{
    "id": 12,
    "vendor": 1,
    "market": 3,
    "active": true,
    "date_created": "2024-04-12T12:00:00Z",
    "updated_at": "2024-04-11T22:14:46.441837Z"
}
```

</details>
<br>

```
Get /api/v2/vendors/:vendor_id/markets/market_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json
{
    "id": 4,
    "vendor": 1,
    "market": 2,
    "active": true,
    "date_created": "2024-04-12T12:00:00Z",
    "updated_at": "2024-04-11T21:42:24.850243Z"
}
```

</details>
<br>

```
Put /api/v2/vendors/:vendor_id/markets/:market_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
{
    "active": false
}
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json
{
    "id": 4,
    "vendor": 1,
    "market": 2,
    "active": false,
    "date_created": "2024-04-12T12:00:00Z",
    "updated_at": "2024-04-11T21:42:24.850243Z"
}
```

</details>
<br>

```
Delete /api/v2/vendors/:vendor_id/markets/:market_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

| Code | Description |
| :--- | :--- |
| 204 | `No Content` |

</details>

---

### Customer Markets
```
Get /api/v2/customers/:customer_id/markets/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json
[
	{
		"id": 4,
		"customer": 1,
		"market": 2,
		"active": true,
		"date_created": "2024-04-12T12:00:00Z",
		"updated_at": "2024-04-11T21:42:24.850243Z"
	},
	{
		"id": 12,
		"customer": 1,
		"market": 1,
		"active": true,
		"date_created": "2024-04-12T12:00:00Z",
		"updated_at": "2024-04-11T22:14:46.441837Z"
	}
]
```

</details>
<br>

```
Post /api/v2/customers/:customer_id/markets/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```json
{
    "customer": 1,
    "market": 3
}
```

| Code | Description |
| :--- | :--- |
| 201 | `Created` |

Response:

```json
{
    "id": 12,
    "customer": 1,
    "market": 3,
    "active": true,
    "date_created": "2024-04-12T12:00:00Z",
    "updated_at": "2024-04-11T22:14:46.441837Z"
}
```

</details>
<br>

```
Get /api/v2/customers/:customer_id/markets/market_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
No Parameters
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json
{
    "id": 4,
    "customer": 1,
    "market": 2,
    "date_created": "2024-04-12T12:00:00Z",
    "updated_at": "2024-04-11T21:42:24.850243Z"
}
```

</details>
<br>

```
Delete /api/v2/customers/:customer_id/markets/:market_id/
```

<details close>
<summary> Endpoint Details </summary>
<br>

| Code | Description |
| :--- | :--- |
| 204 | `No Content` |

</details>

---

### Weather V2

```
Get /api/v2/weather/
```

<details close>
<summary> Endpoint Details </summary>
<br>

Request: <br>
```
Parameters: zipcode
```

| Code | Description |
| :--- | :--- |
| 200 | `OK` |

Response:

```json

    {
        "description": "overcast clouds",
        "temp": 35,
        "icon": "04d"
    }
```

</details>
<br>

</details>

---

## Team

<table>
  <tr>
    <th>Ethan Van Gorkom</th>
    <th>Kaylee Janes</th>
    <th>Antoine Aube</th>
    <th>Jorja Fleming</th>
    <th>Dylan Timmons</th>
  </tr>

<tr>
  <td><img src="https://avatars.githubusercontent.com/u/132889569?v=4" width="135" height="135"></td>
  <td><img src="https://avatars.githubusercontent.com/u/132856753?v=4" width="135" height="135"></td>
  <td><img src="https://avatars.githubusercontent.com/u/55931218?v=4" width="135" height="135"></td>
  <td><img src="https://avatars.githubusercontent.com/u/124719472?v=4" width="135" height="135"></td>
  <td><img src="https://avatars.githubusercontent.com/u/129700694?v=4" width="135" height="135"></td>
</tr>


  <tr>
    <td>
      <a href="https://github.com/EVanGorkom" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
        </a><br>
      <a href="https://www.linkedin.com/in/evangorkom/" rel="nofollow noreferrer">
    <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
        </a>
    </td>
        <td>
       <a href="https://github.com/kbug819" rel="nofollow noreferrer">
            <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
      </a><br>
        <a href="https://www.linkedin.com/in/kaylee-janes" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
      </a>
    </td>
        <td>
       <a href="https://github.com/Antoine-Aube" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
      </a><br>
        <a href="https://www.linkedin.com/in/antoineaube/" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
      </a>
    </td>
        <td>
       <a href="https://github.com/JorjaF" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
      </a><br>
        <a href="https://www.linkedin.com/in/jorjaf/" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
      </a>
    </td>
        <td>
       <a href="https://github.com/DylanScotty" rel="nofollow noreferrer">
            <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
      </a><br>
        <a href="https://www.linkedin.com/in/dylan-timmons/" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
      </a>
    </td>
  </tr>
</table>