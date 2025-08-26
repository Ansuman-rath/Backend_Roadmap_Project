
# 📂 Image Processing Service

This project demonstrates how to upload images to **Amazon S3** using Node.js, Express, and the AWS SDK. Uploaded images are stored in an S3 bucket with a unique filename and can be accessed publicly if permissions are set correctly.

[Image Processing Service](https://roadmap.sh/projects/image-processing-service)

---

## 🚀 Features

* Upload images to **AWS S3** via API endpoint.
* Automatically generates **unique file names** using `uuid`.
* Supports **file MIME types** and preserves original file extension.
* Allows public access (optional) for easy retrieval and transformations.

---

## 🛠 Tech Stack

* **Node.js**
* **Express.js**
* **AWS SDK for JavaScript (v2)**
* **Multer** (for handling file uploads)

---

## 📦 Installation

Clone this repo and install dependencies:

```bash
git clone https://github.com/Ansuman-rath/Backend_Roadmap_Project
cd Image Processing Service
npm install
```

---

## 🔑 AWS Setup

1. **Create an S3 bucket** (e.g., `mybucket`).
2. **Disable "Block All Public Access"** if you want files to be publicly accessible.
3. Apply the following **Bucket Policy** for public read access:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowPublicRead",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::mybucket/*"
    }
  ]
}
```

4. Create an **IAM User** with permissions:

   * `AmazonS3FullAccess` (or restricted permissions to your bucket).
   * Save the **Access Key ID** and **Secret Access Key**.

---

## ⚙️ Environment Variables

Create a `.env` file in the root directory:

```env
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_REGION=your-region
S3_BUCKET_NAME=mybucket
PORT=5000
```

---

## 📝 Usage

### 1. Start the server

```bash
node server.js
```

### 2. Upload an image

Send a `POST` request to:

```
POST http://localhost:5000/upload
```

* **Form field name:** `file`
* **Content type:** `multipart/form-data`

Example with `curl`:

```bash
curl -X POST http://localhost:5000/upload \
  -F "file=@/path/to/your/image.png"
```

Response:

```json
{
  "url": "https://.................image.png"
}
```

---

## ⚠️ Common Issues

* **403 Forbidden:**

  * Check bucket policy (`s3:GetObject` must be allowed).
  * Ensure **Block Public Access** is disabled.
  * Verify IAM user has permissions.

* **Access Denied on Transformations (like Imgix/CloudFront):**

  * Make sure images are **publicly readable**.
  * Double-check bucket CORS settings.

