# Arkrishitech — implementation blueprint

1. Map a farm polygon and calculate area/location.
2. Retrieve historical NASA POWER daily weather and Open-Meteo forecast when available.
3. Calculate FAO-56 reference evapotranspiration and daily soil-water balance.
4. Replay crop parameters over historical seasons and compare modelled yield/risk.
5. Generate a dated crop calendar and irrigation/field-care prompts.
6. Run what-if scenarios using explicit inputs.
7. Retrieve Nepal-focused indigenous farming knowledge; if there is no relevant match, do not invent advice.
8. Show Kalimati wholesale rates as a dated weekly snapshot, never as a live or guaranteed farm-gate quote.
9. Support sensor readings; label demo readings as simulated until hardware is connected.

## Stack

FastAPI, Python, vanilla HTML/CSS/JavaScript, Leaflet, SQLite, NASA POWER, Open-Meteo and a deterministic crop water-balance engine.

## Known limitations

Crop coefficients, yield parameters, sowing windows and cost assumptions need local agronomic review. Wholesale market prices may differ from farm-gate prices. Nepal's altitude, microclimate and crop varieties vary substantially; local knowledge should retain its geographic context.
