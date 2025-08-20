
# 🗂️ Caching Proxy Server (CLI Tool)

A simple **CLI-based caching proxy server** built with Node.js.
It forwards requests to an origin server, caches the responses, and serves them from cache on repeated requests.

## ✨ Features

* Start a proxy server on any port and forward requests to an origin server
* Caches `GET` requests in memory
* Adds response headers:

  * `X-Cache: MISS` → First request (fetched from origin)
  * `X-Cache: HIT` → Subsequent requests (served from cache)
* Clear the cache via CLI
* Transparent forwarding of all request headers

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/Ansuman-rath/Backend_Roadmap_Project
cd Caching Proxy
npm install
npm link   # allows you to run `caching-proxy` globally
```

---

## 🚀 Usage

### Start the proxy

```bash
caching-proxy --port <number> --origin <url>
```

Example:

```bash
caching-proxy --port 3000 --origin http://dummyjson.com
```

This starts the proxy at:

```
http://localhost:3000
```

and forwards requests to:

```
http://dummyjson.com
```

---

### Example Request

```bash
curl.exe -i http://localhost:3000/products
```

* **First request**:

  ```
  X-Cache: MISS
  ```
* **Second request**:

  ```
  X-Cache: HIT
  ```

---

### Clear Cache

```bash
caching-proxy --clear-cache
```

---

## 🧩 How It Works

1. Proxy listens for requests on the given port.
2. Checks if the requested URL exists in memory cache:

   * If yes → returns cached response (`X-Cache: HIT`)
   * If no → forwards request to origin, saves response in cache, and returns it (`X-Cache: MISS`)
3. Cache is stored in memory and cleared when the server restarts or via `--clear-cache`.

---

