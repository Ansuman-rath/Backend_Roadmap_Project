
# URL Shortener 🔗

A simple **URL Shortener service** built using **Node.js, Express, and MongoDB**.
This project allows you to shorten long URLs, retrieve the original URL, update shortened links, track access counts, and redirect users like Bitly.

[URL Shortner](https://roadmap.sh/projects/url-shortening-service)

---

## 🚀 Features

* Shorten any long URL into a short code.
* Retrieve original URL from a short code.
* Redirect to the original URL using the short code.
* Update an existing short URL with a new destination.
* Track number of times each short link was accessed.
* REST API with JSON responses.

---

## 🛠️ Tech Stack

* **Backend**: Node.js, Express.js
* **Database**: MongoDB + Mongoose
* **Tools**: cURL / Postman for API testing

---

## 📦 Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/url-shortener.git
   cd url-shortener
   ```

2. **Install dependencies**

   ```bash
   npm install
   ```

3. **Start MongoDB locally**
   Make sure MongoDB is running (`mongod` or `mongosh` installed).

4. **Run the server**

   ```bash
   node express.js
   ```

   The server will run at: `http://localhost:3000`

---

## 📌 API Endpoints (Example)


### 1. Shorten URL

**POST** `/shorten`
Request:

```json
{
  "url": "https://www.google.com"
}
```

Response:

```json
{
  "url": "https://www.google.com",
  "shortCode": "RSYORSBYD",
  "accessCount": 0,
  "_id": "68a6cdb678b4978b8378f26b",
  "createdAt": "2025-08-21T07:41:42.127Z",
  "updatedAt": "2025-08-21T07:41:42.127Z",
  "__v": 0
}
```

---

### 2. Retrieve Original URL (API JSON)

**GET** `/shorten/:shortCode`
Response:

```json
{
  "_id": "68a6cdb678b4978b8378f26b",
  "url": "https://www.google.com",
  "shortCode": "RSYORSBYD",
  "accessCount": 1,
  "createdAt": "2025-08-21T07:41:42.127Z",
  "updatedAt": "2025-08-21T07:43:00.321Z",
  "__v": 0
}
```

---

### 3. Redirect to Original URL

**GET** `/:shortCode`
Example:

```
http://localhost:3000/RSYORSBYD
```

Redirects → `https://www.google.com`

---

### 4. Update Shortened URL

**PUT** `/shorten/:shortCode`
Request:

```json
{
  "url": "https://www.github.com"
}
```

Response:

```json
{
  "_id": "68a6cdb678b4978b8378f26b",
  "url": "https://www.github.com",
  "shortCode": "RSYORSBYD",
  "accessCount": 1,
  "createdAt": "2025-08-21T07:41:42.127Z",
  "updatedAt": "2025-08-21T07:50:11.432Z",
  "__v": 0
}
```

---

## 🧪 Testing with cURL

* Shorten:

  ```bash
  curl -X POST http://localhost:3000/shorten \
  -H "Content-Type: application/json" \
  -d "{\"url\":\"https://www.google.com\"}"
  ```

* Retrieve:

  ```bash
  curl http://localhost:3000/shorten/RSYORSBYD
  ```

* Redirect (open in browser):

  ```
  http://localhost:3000/RSYORSBYD
  ```

* Update:

  ```bash
  curl -X PUT http://localhost:3000/shorten/RSYORSBYD \
  -H "Content-Type: application/json" \
  -d "{\"url\":\"https://www.github.com\"}"
  ```

---
