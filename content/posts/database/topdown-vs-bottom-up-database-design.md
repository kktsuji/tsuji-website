---
title: "Top-down vs Bottom-up Database Design"
description: ""
date: 2025-12-31T11:00:00+09:00
lastmod:
math: false
draft: false
---

## Top-down vs Bottom-up Database Design

Database design can be approached in two primary ways: top-down and bottom-up. Each approach has its own methodology for structuring and organizing data within a database system.

See also: [Three-level Data Modeling in Databases](https://tsuji.tech/three-level-data-modeling/)

## Top-down Approach

- Starts with a high-level overview of the system and breaks it down into smaller components
- Conceptual level -> Logical level

1. Define Entity-Relationship (ER) diagrams to capture business requirements
2. Convert ER diagrams into relational schemas (tables, columns, keys)
3. Normalize the database to eliminate redundancy and ensure data integrity

## Bottom-up Approach

- Starts with detailed data requirements and builds up to a complete system
- Better for existing systems where data is already defined
- Logical level -> Conceptual level

1. Define tables based on existing data and application needs
2. Normalize tables to ensure data integrity
3. Create ER diagrams to represent the overall database structure
