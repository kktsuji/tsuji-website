---
title: "Three-schema Architecture in Database Systems"
description: ""
date: 2025-12-31T11:00:00+09:00
lastmod:
math: false
draft: false
---

## Three-schema Architecture in Database Systems

The three-schema architecture is a framework used in database systems to separate the different levels of abstraction in data representation and management. It consists of three levels: the internal level, the conceptual level, and the external level.

## Internal Level

- Describes how data is physically stored on storage devices (e.g., file structures, indexes, access paths)
- Deals with data compression, encryption, and optimization for performance
- Closest to the hardware layer and handles low-level data management operations

## Conceptual Level

- Represents the logical structure of the entire database, including entities, relationships, and constraints
- Provides a unified view of all data in the organization, independent of physical storage details
- Serves as a bridge between the internal and external levels, ensuring data independence

## External Level

- Defines user-specific views of the database tailored to different application requirements
- Multiple external schemas can exist for different user groups or applications
- Provides data abstraction and security by limiting access to only relevant portions of the database
