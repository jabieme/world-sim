# Things learned
## Folder Layout Structures:
- `app/api/` = HTTP layer (routes, request parsing, status codes)
- `app/models/` = data shapes (Pydantic schemas, domain models)
- `app/services/` = business logic (simulation tick, applying events, persistence orchestration)
- `app/core/` = config, settings, constants, small shared helpers

## Routes
> Are controllers used to handle HTTP operations
- Validate input
- Call Service functions
- Return outputs

NO SIMULATION MATH

## Services
> These are where your game rules live
---
## Configuration
> Constant Variables, starting values and environment variables are all initialized here