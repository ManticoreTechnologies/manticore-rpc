# Manticore RPC Service

Welcome to the Manticore RPC Service! This service is designed to facilitate communication with the Evrmore blockchain through a set of remote procedure calls (RPC). This README will guide you through the prerequisites, setup, configuration, and usage of the service.

## Prerequisites

Before you can run the Manticore RPC Service, ensure that the following system and Python packages are installed on your system.

### System Packages

- **redis-server**: Used as a persistent storage backend for rate limiting.
- **python3**: The application is written in Python, so Python 3 is required.

### Python Packages

- **redis**: Python client for Redis, used to interact with the Redis server.
- **flask**: A lightweight web framework used to build the application.
- **flask_limiter**: A Flask extension used to add rate limiting to the application.
- **colorlog**: A package for colorful logging in Python, making logs easier to read.

## Getting Started

Follow these steps to set up and run the Manticore RPC Service.

### 1. Install Redis Server

First, you need to install the Redis server on your system. Redis will be used to store rate limit data persistently.

```bash
sudo apt install redis-server
```

### 2. Install Required Python Packages

Next, install the necessary Python packages using pip:

```bash
pip3 install redis flask flask_limiter colorlog
```

### 3. Configure the Service

The service uses a `settings.conf` file to manage configuration settings. Below is a breakdown of the configuration options:

#### General Settings

```ini
[General]
log_level = INFO
port = 8000
timeout = 30
address = EaHp99kaAWKde7osRT69pRSyKR2QdCptVe
amount = 0.01
rate_limit = 1
```

- **`log_level`**: The logging level for the application. Can be set to `DEBUG`, `INFO`, `WARNING`, `ERROR`, or `CRITICAL`.
- **`port`**: The desired port for the service to listen on.
- **`timeout`**: The time (in seconds) to wait for a response from the blockchain node.
- **`address`**: The address from which the service will interact with the blockchain.
- **`amount`**: The amount of cryptocurrency (in Evrmore) to be sent per request.
- **`rate_limit`**: The maximum number of requests allowed per day from a single user.

#### Permission Settings

```ini
[Permission]
user = user
group = user
```

- **`user`**: The system user under which the application will run.
- **`group`**: The system group under which the application will run.

#### Node Settings

```ini
[Node]
host = 127.0.0.1
port = 8819
user = user
password = password
```

- **`host`**: The IP address or hostname of the Evrmore node.
- **`port`**: The port on which the Evrmore node is listening.
- **`user`**: The username for authenticating with the node.
- **`password`**: The password for authenticating with the node.

#### Logging Settings

```ini
[Logging]
log_file = /var/log/manticore_rpc.log
```

- **`log_file`**: The path to the log file where the application's logs will be written. Ensure that the specified path is writable by the application.

### 4. Run the Application

Once you have configured the service, you can run the Flask application using Gunicorn or directly with Python:

#### Running with Gunicorn (Recommended for Production)

```bash
gunicorn -w 1 -b 0.0.0.0:8080 startup:app
```

#### Running with Python (Development Mode)

```bash
python3 startup.py
```

### 5. Access the Application

Open your web browser and navigate to `http://localhost:8080` (or the IP/port specified) to start using the Manticore RPC Service.

## Managing the Service

You can manage the Manticore RPC Service as a systemd service. The service management script allows you to easily install or uninstall the service on your system.

### Install the Service

To install the service:

```bash
sudo python3 manage_service.py install
```

### Uninstall the Service

To uninstall the service:

```bash
sudo python3 manage_service.py uninstall
```

After installing the service, it will start automatically on system boot and can be managed using systemd commands.

## License

(c) 2024 Manticore Technologies LLC. All rights reserved.

---

Thank you for using the Manticore RPC Service! If you encounter any issues or have any questions, feel free to reach out.