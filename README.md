# Supply Chain Downstreaming Automation

A Python-based supply chain automation project that simulates the weekly downstreaming process from a main Distribution Center (DC) to warehouses based on inventory and forecast data.

## Project Goal

Build a Python decision engine that determines:
- whether a Distribution Order (DO) is needed,
- which item should be transferred,
- from which warehouse to which warehouse,
- and the required transfer quantity.

The project is inspired by a real supply-chain architecture:

```text
Voyager (Forecast) + Databricks (Supply Chain Data)
                    ↓
                  Python
          Decision / Business Rules
                    ↓
                Infor M3
              Create DO
                    ↓
          Warehouse Execution
                    ↓
             M3 → Databricks
                    ↓
                Power BI
```

For the learning project, the enterprise systems are simulated locally:

| Real environment | Project simulation |
|---|---|
| Databricks | SQLite / SQL database |
| Voyager | Forecast table/data |
| Decision process | Python decision engine |
| Infor M3 | Simulated Distribution Order |
| Power BI | Later reporting phase |

## Project Roadmap

### Phase 1 — Define the Process ✅
- Understand the current downstreaming process
- Identify the role of each system
- Define the target automation architecture

### Phase 2 — Database Fundamentals 📍 CURRENT PHASE
- Set up SQLite
- Define items
- Define warehouses
- Define inventory
- Add realistic sample data
- Practice basic SQL queries

**Output:** A small supply-chain database that simulates the data layer.

### Phase 3 — Forecast Data
- Create weekly forecast data
- Connect item and warehouse forecasts with inventory data
- Simulate Voyager input

### Phase 4 — Python Decision Engine
Python will:
1. Read inventory
2. Read forecast
3. Calculate projected shortages
4. Check main DC availability
5. Apply safety-stock and downstreaming rules
6. Decide whether a DO is required
7. Calculate the transfer quantity

**Output:** `CREATE DO` or `NO DO`.

### Phase 5 — Simulate M3
Create a simulated Distribution Order containing:
- DO number
- item
- source warehouse
- destination warehouse
- quantity
- status

Example:

```text
DO-0001 | X001 | MAIN_DC → WH_A | 50 pcs | CREATED
```

### Phase 6 — Integration & Reporting
- Simulate DO execution
- Update inventory after execution
- Add logging and error handling
- Add reporting
- Explore API/integration concepts for connecting Python to ERP systems such as M3

## Current Position

```text
Phase 1 ✅ → Phase 2 📍 → Phase 3 → Phase 4 → Phase 5 → Phase 6
```

We are currently building the database foundation before implementing the Python decision engine.
