# 🌱 Arkrishitech

### Climate-aware agriculture and indigenous knowledge for Nepal.

Arkrishitech is an agricultural decision-support platform designed to help farmers make informed farming decisions through climate data, crop simulation, agricultural research, and field-level monitoring.

<p align="center">
  <a href="https://arckrishitech.vercel.app/">
    <img src="docs/screenshots/dashboard.png" alt="Arkrishitech application dashboard" width="100%">
  </a>
</p>

<p align="center">
  <a href="https://arckrishitech.vercel.app/"><strong>🌐 OPEN LIVE APPLICATION</strong></a>
  &nbsp; · &nbsp;
  <a href="https://github.com/lineo01/Arkrishitech"><strong>VIEW SOURCE CODE</strong></a>
</p>

<p align="center">
  <em>Click the dashboard image above to open the live application.</em>
</p>

---

## About the Project

Agriculture in Nepal is strongly influenced by local climate, soil conditions, seasonal rainfall, and traditional farming practices. However, farmers often lack accessible tools that bring these factors together when deciding what and when to grow.

Arkrishitech aims to bridge this gap by combining scientific agricultural methods with indigenous knowledge and connected field monitoring.

## Features

| Feature | Description |
|---|---|
| **Crop Recommendations** | Evaluates crop suitability using historical climate conditions, planting periods, and estimated economic performance. |
| **Crop Simulation** | Simulates crop-water requirements and potential performance across different planting dates. |
| **Crop Comparison** | Helps compare candidate crops and planting options using model-based estimates. |
| **Climate Insights** | Uses historical climate information and weather forecasts to provide environmental context. |
| **Sensor Monitoring** | Designed to integrate field measurements such as soil moisture, temperature, and pH. |
| **Agricultural Knowledge Base** | Makes documented agricultural research and traditional practices accessible. |
| **Indigenous Knowledge AI** | Planned Nepal-focused AI system for locally relevant agricultural guidance. |

## How It Works

Arkrishitech brings together three main parts:

**1. Agricultural Intelligence Platform**

The web application and backend process climate information, run crop simulations, and present recommendations through an accessible dashboard.

**2. Connected Field Hardware**

Distributed ESP-based sensor nodes are intended to collect measurements from different locations in a farm. An Arduino UNO Q acts as the central hub, coordinating the sensor network and processing field information.

**3. Indigenous Knowledge Intelligence**

The intended system includes a locally deployed agricultural AI on the Arduino UNO Q. It will be developed using Nepal-focused agricultural research and documented indigenous farming knowledge, with the goal of making relevant guidance available closer to the field.

## Crop Recommendation Engine

The crop simulation engine uses historical climate data and simplified agricultural modelling to estimate crop performance.

- **NASA POWER:** Historical daily climate data, covering approximately 30 years where available.
- **Open-Meteo:** Weather forecast information.
- **FAO-56 Penman–Monteith:** Reference evapotranspiration estimation.
- **Crop coefficients (Kc):** Crop water requirement estimation.
- **FAO-33 yield response:** Estimates the effect of water stress on potential yield.

The engine evaluates candidate planting dates against historical weather conditions and ranks options using risk-adjusted economic estimates.

These results are simulations, not measured historical farm yields or guaranteed harvest predictions.

## The Intended Hardware System

The final system is designed around a distributed sensor network and a central edge-computing hub.

```text
       FARM SENSOR NETWORK
       
    ESP Node 1   ESP Node 2   ESP Node 3
         \          |          /
          \         |         /
           ARDUINO UNO Q
             CENTRAL HUB
                  |
       +----------+----------+
       |                     |
   STM32U585              QRB2210
 Sensor & Hardware      Linux Processing
    Control                  |
                             |
                 Indigenous Knowledge AI
                    (Planned Local AI)
                             |
                    Backend / Platform
                             |
                     Arkrishitech Web App
```

The UNO Q is intended to coordinate field hardware while its Linux processor provides the environment for local AI applications. The wider platform provides climate analysis, crop simulation, and the web interface.

## Research and Knowledge

The project draws on Nepal-focused agricultural research and documented traditional practices, including:

- [Indigenous agricultural knowledge for climate adaptation — Khumbu, Nepal (2022)](https://doi.org/10.3389/fclim.2022.1067630)
- [Adoption of indigenous agricultural knowledge — Bhirkot, Syangja (2021)](https://doi.org/10.1080/23311932.2021.1914384)
- [Traditional plant-based pest and disease management — Pokhara-32, Kaski (2023)](https://doi.org/10.3126/hebids.V9i1.59586)
- [Traditional crop diversity and farmer seed conservation — Kailash Sacred Landscape (2017)](https://www.nepjol.info/index.php/AEJ/article/view/19886/16374)
- [Traditional crop seed systems (2020)](https://giwmscdnone.gov.np/media/app/public/75/posts/1685027773_12.pdf)

These sources contribute to the agricultural knowledge component. They are not treated as direct crop-yield datasets, and documented practices retain their geographical and research context.

## Technology

| Area | Technology |
|---|---|
| Backend | Python, FastAPI |
| Frontend | Web application |
| Climate data | NASA POWER, Open-Meteo |
| Crop modelling | FAO-56 and FAO-33 methodologies |
| Sensor nodes | ESP-based devices |
| Central hub | Arduino UNO Q |
| Hardware control | STM32U585 |
| Edge computing | Qualcomm QRB2210, Debian Linux |
| Knowledge system | Research-backed searchable knowledge library |
| Local AI | Fine-tuned agricultural model (planned) |

## Run Locally

**Requirements:** Python 3.10+ and Node.js with npm.

Clone the repository:

```bash
git clone https://github.com/lineo01/Arkrishitech.git
cd Arkrishitech
```

Start the backend:

```bash
pip install -r requirements.txt
uvicorn backend.app.main:app --reload
```

Start the frontend:

```bash
cd frontend
npm install
npm run dev
```

For deployment details, see [DEPLOYMENT.md](DEPLOYMENT.md).

## Project Status

Arkrishitech is under active development.

The web application, backend foundation, climate-data integration, initial crop simulation engine, and searchable agricultural knowledge library form the current software foundation.

The distributed ESP sensor network, complete Arduino UNO Q integration, and fine-tuned local Indigenous Knowledge AI are part of the intended final system and require further implementation and testing.

## Project Vision

The long-term goal is to connect scientific agricultural modelling, Nepal's indigenous farming knowledge, and real-time field information in one practical system.

**Arkrishitech — Bringing field intelligence and indigenous knowledge together for climate-aware agriculture in Nepal.**

---

<p align="center">
  <a href="https://arckrishitech.vercel.app/"><strong>Visit Arkrishitech</strong></a>
  &nbsp; · &nbsp;
  <a href="https://github.com/lineo01/Arkrishitech"><strong>GitHub Repository</strong></a>
</p>
