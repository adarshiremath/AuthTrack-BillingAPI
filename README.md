# AuthTrack BillingAPI

## Overview
AuthTrack BillingAPI is a FastAPI-based application that provides functionalities for user authentication, telemetry monitoring, and billing through Stripe. This project is designed to offer a comprehensive solution for managing secure access, monitoring API usage, and handling billing operations.

## Features
- Authentication: Secure user login and token-based authentication.
- Telemetry: API usage monitoring with Prometheus.
- Billing: Stripe integration for handling billing and payments.

## Getting Started
### Prerequisites
- Docker
- Docker Compose

### Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/AuthTrack-BillingAPI.git
cd AuthTrack-BillingAPI
```
Build and run the Docker containers:
```bash
docker-compose up --build
```
The application will be accessible at http://127.0.0.1:8000.

### Environment Variables
Create a `.env` file in the root directory of the project and add the following variables:
```env
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
STRIPE_SECRET_KEY=your_stripe_secret_key
```

## Usage
### Authentication
#### Get Access Token
```sh
curl -X POST "http://127.0.0.1:8000/auth/token" -H "Content-Type: application/x-www-form-urlencoded" -d "username=johndoe&password=your_password"
```
#### Get Current User
```sh
curl -X GET "http://127.0.0.1:8000/users/me" -H "Authorization: Bearer your_access_token"
```

### Billing
#### Create Checkout Session
```sh
curl -X POST "http://127.0.0.1:8000/billing/create-checkout-session" -H "Authorization: Bearer your_access_token"
```

### Telemetry
#### Prometheus Metrics
```sh
curl -X GET "http://127.0.0.1:8000/metrics"
```

## Project Structure
```
.
├── app
│   ├── api
│   │   ├── endpoints
│   │   │   ├── auth.py
│   │   │   ├── billing.py
│   │   │   └── users.py
│   │   └── __init__.py
│   ├── core
│   │   ├── config.py
│   │   └── __init__.py
│   ├── main.py
│   ├── models
│   │   ├── user.py
│   │   └── __init__.py
│   ├── schemas
│   │   ├── token.py
│   │   └── __init__.py
│   └── services
│       ├── auth.py
│       └── __init__.py
├── .env
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Docker Compose File
```yaml
version: '3.8'

services:
    web:
        build:
            context: .
            dockerfile: Dockerfile
        ports:
            - "8000:8000"
```
