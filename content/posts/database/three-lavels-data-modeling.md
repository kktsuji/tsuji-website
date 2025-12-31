---
title: "Three-level Data Modeling in Databases"
description: ""
date: 2025-12-31T11:00:00+09:00
lastmod:
math: false
draft: false
---

## Three-level Data Modeling in Databases

Three-level data modeling is a framework used in database design to separate the different levels of abstraction in data representation. It consists of three levels: the conceptual level, the logical level, and the physical level.

The data modeling process typically follows these steps:

1. Conceptual Level
2. Logical Level
3. Physical Level

## Conceptual Level

- Represents high-level business requirements and entities without implementation details
- Uses Entity-Relationship (ER) diagrams to model relationships between business concepts
- Independent of any specific database technology or implementation approach (e.g., relational, hierarchical, network, etc.) and DBMS(Database Management System)-independent (e.g., Oracle, MySQL, PostgreSQL, etc.)

## Logical Level

- Defines tables, columns, primary keys, foreign keys, and relationships in a structured format
- Based on a specific data model (e.g., relational model) but remains DBMS-independent
- Includes normalization rules and data integrity constraints

Note: Nowadays, the relational model or NoSQL is predominantly used.

## Physical Level

- Specifies actual implementation details for a particular DBMS (e.g., PostgreSQL, MySQL)
- Includes indexes, partitions, storage parameters, and performance optimization settings
- Contains file organization, data types, and physical storage structures
