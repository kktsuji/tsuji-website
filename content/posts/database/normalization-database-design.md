---
title: "Normalization in Database Design"
description: ""
date: 2025-12-31T11:00:00+09:00
lastmod:
math: false
draft: false
---

## Normalization in Database Design

Normalization is a systematic approach to organizing data in a database to minimize redundancy and improve data integrity. The process involves decomposing tables into smaller, well-structured tables based on a set of normal forms.

The main normal forms are as follows:

- Denormalization
- First Normal Form (1NF)
- Second Normal Form (2NF)
- Third Normal Form (3NF)
- Fourth Normal Form (4NF)
- Fifth Normal Form (5NF)
- Boyce-Codd Normal Form (BCNF)

The normalization process typically follows these steps. In practice, databases are often normalized up to the Third Normal Form (3NF) or Boyce-Codd Normal Form (BCNF) to balance data integrity and performance.

## Denormalization

- Intentionally introduces redundancy into a normalized database
- Combines data from multiple tables to reduce the number of joins
- Improves query performance by avoiding complex joins
- Trades off data integrity and storage space for faster read operations
- Commonly used in data warehouses and reporting systems
- Requires careful maintenance to keep redundant data synchronized

## First Normal Form (1NF)

- Each column contains only atomic (indivisible) values
- No repeating groups or arrays within a single column
- Each row must be unique (typically enforced by a primary key)
- Each column must have a unique name
- The order of rows and columns does not matter
- Forms the foundation for all other normal forms

## Second Normal Form (2NF)

- Must already be in First Normal Form (1NF)
- Eliminates partial dependencies on the primary key
- All non-key attributes must depend on the entire primary key, not just part of it
- Only applies to tables with composite primary keys
- Prevents data redundancy caused by partial functional dependencies
- Requires splitting tables to separate partially dependent attributes

## Third Normal Form (3NF)

- Must already be in Second Normal Form (2NF)
- Eliminates transitive dependencies between non-key attributes
- Non-key attributes must depend only on the primary key, not on other non-key attributes
- Prevents update anomalies caused by indirect dependencies
- Further reduces data redundancy
- Most databases aim to achieve at least this level of normalization

## Boyce-Codd Normal Form (BCNF)

- A stricter version of Third Normal Form (3NF)
- Every determinant must be a candidate key
- Addresses certain anomalies that can exist in 3NF
- Particularly important when a table has multiple overlapping candidate keys
- May require decomposing tables that are already in 3NF
- Ensures that all functional dependencies are based on keys
