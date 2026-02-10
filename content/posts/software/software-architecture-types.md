---
title: "Common Software Architecture Types"
description: ""
date: 2026-02-10T18:00:00+09:00
lastmod:
draft: false
---

## Common Software Architecture Types

### 1. Layered (N-Tier)

**Structure:** Horizontal layers (Presentation → Business → Data Access → Database)

- ✅ Simple, familiar, separation of concerns
- ❌ Tight coupling between layers, changes cascade down

```
src/
├── presentation/    # Controllers, Views
├── business/        # Services, Business Logic
├── dataaccess/      # Repositories, DAOs
└── models/          # Shared DTOs, Entities
```

### 2. Hexagonal (Ports & Adapters)

**Structure:** Core domain surrounded by ports (interfaces) and adapters (implementations)

- ✅ Highly testable, domain-centric, swappable infrastructure
- ❌ More complex setup, overkill for simple apps

```
src/
├── domain/          # Core business logic
│   ├── models/
│   └── services/
├── ports/           # Interfaces (in/out)
│   ├── inbound/
│   └── outbound/
└── adapters/        # Implementations
    ├── web/         # REST controllers
    └── persistence/ # Database adapters
```

### 3. Vertical Slice

**Structure:** Features organized as independent slices cutting through all layers

- ✅ Low coupling between features, easier to understand single features
- ❌ Potential code duplication, harder to enforce consistency

```
src/
├── features/
│   ├── create-order/
│   │   ├── handler.ts
│   │   ├── validator.ts
│   │   └── repository.ts
│   ├── get-order/
│   │   ├── handler.ts
│   │   └── repository.ts
│   └── cancel-order/
└── shared/          # Cross-cutting concerns
```

### 4. Clean Architecture

**Structure:** Concentric circles (Entities → Use Cases → Interface Adapters → Frameworks)

- ✅ Framework-independent, highly testable, flexible
- ❌ Steep learning curve, lots of boilerplate

```
src/
├── entities/        # Enterprise business rules
├── usecases/        # Application business rules
├── interfaces/      # Adapters (controllers, gateways)
│   ├── controllers/
│   └── gateways/
└── frameworks/      # External tools (DB, Web)
    ├── database/
    └── web/
```

### 5. Microservices

**Structure:** Independent, deployable services communicating via APIs

- ✅ Independent scaling/deployment, tech flexibility, fault isolation
- ❌ Network complexity, distributed system challenges, operational overhead

```
services/
├── user-service/
│   ├── src/
│   ├── Dockerfile
│   └── package.json
├── order-service/
│   ├── src/
│   ├── Dockerfile
│   └── package.json
├── payment-service/
└── api-gateway/
```

### 6. Monolithic

**Structure:** Single deployable unit containing all functionality

- ✅ Simple deployment, easy debugging, low latency
- ❌ Scaling limitations, large codebase, deployment risk

```
src/
├── controllers/
├── services/
├── models/
├── repositories/
├── utils/
└── config/
```

### 7. Event-Driven

**Structure:** Components communicate through events/messages

- ✅ Loose coupling, scalable, real-time processing
- ❌ Debugging complexity, eventual consistency, event ordering challenges

```
src/
├── events/
│   ├── definitions/     # Event schemas
│   └── handlers/        # Event processors
├── publishers/          # Event emitters
├── subscribers/         # Event listeners
└── services/
```

### 8. CQRS (Command Query Responsibility Segregation)

**Structure:** Separate models for reading and writing data

- ✅ Optimized read/write performance, scalable
- ❌ Increased complexity, eventual consistency

```
src/
├── commands/            # Write operations
│   ├── handlers/
│   └── models/
├── queries/             # Read operations
│   ├── handlers/
│   └── models/
└── shared/
    └── events/
```

### 9. Domain-Driven Design (DDD)

**Structure:** Software modeled around the business domain with bounded contexts, aggregates, and ubiquitous language

- ✅ Aligns code with business, handles complex logic well
- ❌ Steep learning curve, overkill for simple CRUD apps

```
src/
├── bounded-contexts/
│   ├── ordering/
│   │   ├── domain/      # Aggregates, Entities, Value Objects
│   │   ├── application/ # Use cases, Services
│   │   └── infrastructure/
│   └── shipping/
│       ├── domain/
│       ├── application/
│       └── infrastructure/
└── shared-kernel/       # Shared domain concepts
```
