---
title: "Three Types of Approaches to Database Design"
description: ""
date: 2025-12-31T11:00:00+09:00
lastmod:
math: false
draft: false
---

## Three Types of Approaches to Database Design

Three primary approaches to database design are commonly used: Process-Centered, Data-Centered, and Object-Oriented. Each approach has its own focus and methodology for structuring and organizing data within a database system.

Nowadays, the Data-Centered Approach is the most widely adopted, especially for relational database design.

In practice, these approaches can be combined to leverage their respective strengths and create a more robust database design.

- Design the overall database structure using the Data-Centered Approach.
- Implement specific functionalities or modules using the Process-Centered or Object-Oriented Approaches as needed.

## Process-Centered Approach

- Focuses on business processes and workflows as the primary design driver
- Uses data flow diagrams (DFD) to model how data moves through the system
- Emphasizes "what the system does" rather than "what data it stores"
- Processes mean the functions of the software system that manipulate data

## Data-Centered Approach

- Centers on data structures, relationships, and their integrity
- Uses Entity-Relationship (ER) diagrams to model data entities and relationships
- Most common approach for relational database design, focusing on normalization

## Object-Oriented Approach

- Combines data and behavior into unified objects with encapsulation
- Uses UML (Unified Modeling Language) class diagrams to represent classes, attributes, and methods
- Integrates data structures with the operations that manipulate them
