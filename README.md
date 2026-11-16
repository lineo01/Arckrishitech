# Arkrishitech

**Farm intelligence for Nepal — grounded in climate data, field observations and local farming knowledge.**

Arkrishitech is a decision-support prototype that helps farmers map a field, examine historical and forecast weather, compare crop options, build a dated cultivation schedule, explore what-if scenarios and ask a retrieval-based assistant for Nepal-focused farming practices.

## What it does

- **Field mapping:** draw a field polygon and estimate its area and location.
- **Climate analysis:** fetch historical NASA POWER daily weather and Open-Meteo forecast data when available.
- **Crop comparison:** replay crop water-balance and yield-response calculations across historical seasons. Outputs are model estimates, not guaranteed yields.
- **Farm calendar:** generate sowing, field-care, irrigation and harvest tasks.
- **What-if scenarios:** compare changes in water, mulch and farm-management inputs.
- **Local knowledge assistant:** retrieves concise Nepal-focused practices covering seed saving, mixed cropping, mulching, titepati, traditional storage, compost and seasonal indicators. It is a retrieval system, not a general-purpose LLM.
- **Market reference:** shows a dated weekly snapshot of Kalimati wholesale rates displayed by Ramro Patro. This is not a live feed and not a farm-gate quote.
- **Sensor interface:** manual values and device-connected readings are supported; demo sensor readings are labelled simulated until hardware is connected.

## Data labels

- **Fetched:** external weather or market data with source and date.
- **Modelled:** yield, crop suitability, water balance, risk and scenario outputs.
- **Simulated:** demo sensor readings when no physical sensor is connected.
- **Weekly snapshot:** market data captured from the source page; it is not live.

## Market price methodology

The bundled snapshot is from [Ramro Patro's Kalimati vegetable-rate page](https://ramropatro.com/vegetable), captured on 16 November 2026. Values are average wholesale rates in NPR/kg, with minimum and maximum values retained in the JSON. A weekly GitHub Actions workflow attempts to refresh the static snapshot. It fails closed if the source table cannot be parsed.

The potato crop model uses the matching red-long potato wholesale benchmark (NPR 58/kg in the bundled snapshot). The current Kalimati vegetable list does not provide matching quotes for finger millet, buckwheat, maize/beans, lentil, mustard, wheat/barley or turmeric/ginger. Those crops' price/cost values remain model assumptions and must not be represented as observed market prices. Wholesale rates may differ from a farmer's farm-gate price.

## Local knowledge sources

The knowledge records are grounded in published Nepal-focused studies and are summarized as practical entries, not displayed as paper abstracts. The research references and mapping of practices are in [`docs/research/NEPAL-LOCAL-KNOWLEDGE-AND-MARKET.md`](docs/research/NEPAL-LOCAL-KNOWLEDGE-AND-MARKET.md). Practices are geographically scoped: a Khumbu practice is not automatically applicable in the Terai or another elevation zone.

## Stack

- Backend: Python, FastAPI, Pydantic
- Frontend: HTML, CSS, vanilla JavaScript
- Maps: Leaflet and Leaflet Draw
- Climate: NASA POWER, Open-Meteo
- Crop water balance: FAO-56 Penman–Monteith reference evapotranspiration and daily soil-water balance; yield response is modelled
- Storage: SQLite
- Deployment: Vercel-compatible FastAPI entry point and static frontend

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn backend.app.main:app --reload
```

Open http://127.0.0.1:8000. The first NASA POWER history request can take time. For offline tests, set `KS_OFFLINE=1`.

## Tests

```bash
cd backend
KS_OFFLINE=1 pytest -q
```

## Weekly market snapshot

The scheduled workflow runs Monday at 07:15 Nepal time. To run manually:

```bash
python scripts/update_market_snapshot.py
```

It updates `public/market_snapshot.json` and `frontend/market_snapshot.json`. Review the diff before publishing. The application reads only this bundled snapshot; it does not call Ramro Patro on each page view.

## Important limitations

This is a prototype for decision support, not a substitute for local agronomic advice. Model outputs depend on crop parameters, weather coverage, soil assumptions and user inputs. Market benchmarks are wholesale snapshots, not farm-gate offers. Local knowledge entries should be adapted with community and extension input; the assistant will return no-match rather than invent a recipe when it cannot find relevant material.

## UI editing

See [`docs/UI-GUIDE.md`](docs/UI-GUIDE.md) for the exact frontend file map and instructions for editing the assistant, references panel, branding, styles, and responsive layout.
