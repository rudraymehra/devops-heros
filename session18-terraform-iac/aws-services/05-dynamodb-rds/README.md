# DynamoDB and RDS

## DynamoDB

DynamoDB is a managed NoSQL key-value/document database. A table contains items;
items contain attributes. Every item is addressed by a partition key or a composite
partition-and-sort key. Key design determines distribution and supported access
patterns, so it should be chosen before loading data.

It suits high-scale, low-latency workloads such as sessions, carts, device state,
and event metadata. Important features include on-demand/provisioned capacity,
secondary indexes, TTL, Streams, transactions, point-in-time recovery, and global
tables.

## RDS

RDS manages relational database engines including PostgreSQL, MySQL, MariaDB,
Oracle, SQL Server, and Amazon Aurora. A DB instance supplies compute and storage.
Security Groups, subnet groups, encryption, IAM/database authentication, and Secrets
Manager help protect access.

Automated backups enable point-in-time restore. Multi-AZ creates a synchronous
standby for availability; it is not primarily for read scaling. Read replicas use
asynchronous replication to offload reads and may lag. RDS suits transactional data
requiring joins, constraints, and SQL.

Choose DynamoDB for known key-based access patterns and horizontal scale; choose RDS
for relational modeling and flexible SQL queries.
