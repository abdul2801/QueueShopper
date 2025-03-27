# QueueShopper

## Overview
QueueShopper is a scalable e-commerce application using Kafka to handle asynchronous communication between services like order management, inventory updates, and payment processing.

---

## Features
- Order Creation and Processing
- Inventory Stock Management
- Payment Confirmation and Notification
- Kafka Producer/Consumer for Event Handling
- Flask API for Backend Logic

---

## Tech Stack
- **Backend:** Python (Flask)
- **Queue:** Kafka
- **Database:** MySQL
- **API Security:** JWT Authentication

---


## Setup Instructions


### 2. Set Up Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Start Kafka and Zookeeper
```bash
docker-compose up -d
```

### 4. Run Flask Application
```bash
python app.py
```


### 5. Run Frontend React
```bash
npm install
npn run start
```

---



