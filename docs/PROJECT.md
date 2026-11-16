# Arkrishitech — current project reference

## Product

A Nepal-focused farm decision-support prototype. A farmer maps a plot, the app fetches NASA POWER historical weather and Open-Meteo forecast data, estimates crop water balance and yield response, compares crop options, creates a dated farm calendar, explores what-if scenarios and asks a retrieval-based local farming knowledge assistant.

## Current components

- `backend/app/main.py`: FastAPI endpoints and static website serving.
- `backend/app/data.py`: NASA POWER history and Open-Meteo forecast retrieval/cache.
- `backend/app/engine.py`: FAO-56 ET0, soil-water balance, historical replay, crop comparison, schedule and what-if calculations.
- `backend/app/knowledge.json`: Nepal-focused local practices with geographic context and limitations.
- `backend/app/kb.py`: keyword retrieval; not an LLM.
- `public/` and `frontend/`: synchronized website files.
- `public/market_snapshot.json`: static weekly Kalimati wholesale snapshot.
- `scripts/update_market_snapshot.py`: weekly source-page parser.
- `.github/workflows/weekly-market-snapshot.yml`: scheduled refresh workflow.

## Data boundaries

- Weather is fetched from external services when available.
- Yield, water balance, crop ranking and scenarios are modelled outputs.
- Sensor demo values are simulated until physical hardware sends readings.
- Market rates are weekly static wholesale snapshots from Ramro Patro's Kalimati page, not live and not farm-gate prices.
- Potato uses the matching red-long potato average from the snapshot. Other crop prices remain explicitly identified model assumptions when the snapshot has no matching quote.
- Local knowledge records are based on Nepal-focused published research; a practice documented in one locality is not automatically applicable everywhere.

## API

| Method | Path | Purpose |
|---|---|---|
| GET | `/api/health` | Health check |
| POST | `/api/analyze` | Field, weather, alerts, crop comparison and schedule |
| POST | `/api/schedule` | Crop-specific calendar |
| POST | `/api/whatif` | Scenario comparison |
| POST | `/api/fields` | Save a field |
| GET | `/api/fields` | List saved fields |
| GET | `/api/fields/{id}` | Load a field |
| POST | `/api/sensors/{field_id}` | Store sensor/manual reading |
| GET | `/api/sensors/{field_id}/latest` | Latest reading |
| POST | `/api/chat` | Retrieve local knowledge entry |

## Validation

Run `KS_OFFLINE=1 pytest -q` from `backend/`. The offline weather generator is for automated tests only; do not present it as fetched weather.
