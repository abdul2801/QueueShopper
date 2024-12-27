#!/bin/bash
# Wait for Kafka to be ready
sleep 10

# Create required topics
kafka-topics.sh --create --topic order_placed --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1
kafka-topics.sh --create --topic payment_success --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1
kafka-topics.sh --create --topic inventory_updated --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1
