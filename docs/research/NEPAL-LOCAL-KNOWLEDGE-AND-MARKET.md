# Nepal-focused indigenous farming knowledge and market data

The in-app knowledge assistant uses concise, Nepal-focused practice records rather than research-paper abstracts. Each practice retains a geographic scope so that a method documented in one locality is not presented as universally applicable.

## Nepal research references used

- **Khumbu, Solukhumbu:** “Indigenous people's perception of indigenous agricultural knowledge for climate change adaptation in Khumbu, Nepal” (Frontiers in Climate, 2022). Documents moisture management, dry-leaf/bamboo cover, potato planting around spring soil moisture, titepati use, crop diversity, local planting indicators and potato storage. https://doi.org/10.3389/fclim.2022.1067630
- **Bhirkot, Syangja:** “Perceived attributes and adoption of Indigenous Technological Knowledge on agriculture” (2021). Describes local plant materials, sun-drying grain, farmyard manure, mixed cropping and traditional storage such as bhakari and hanging maize. https://doi.org/10.1080/23311932.2021.1914384
- **Pokhara-32, Kaski:** “Study on Plant-Based Traditional Knowledge for Pest and Disease Management of Crop Plants” (Himalayan Biodiversity, 2023). https://doi.org/10.3126/hebids.V9i1.59586
- **Kailash Sacred Landscape:** “Conservation and Management Practices of Traditional Crop Genetic Diversity by the Farmers” (Journal of Agriculture and Environment, 2017). Documents local crop and varietal diversity and farmer-managed seed conservation. https://www.nepjol.info/index.php/AEJ/article/view/19886/16374
- **Mountain seed systems:** “Seed Systems of Traditional Crops in the Mountains of Nepal” (2020), based on 328 households across Humla, Jumla, Lamjung and Dolakha; reports the importance of informal seed systems and own-saved seed. https://giwmscdnone.gov.np/media/app/public/75/posts/1685027773_12.pdf

These studies are used as context for practical knowledge records, not as proof that every practice works in every crop or location. No paper abstract is displayed in the application.

## Weekly market-price proof of concept

`public/market_snapshot.json` and `frontend/market_snapshot.json` contain a Kalimati wholesale snapshot displayed by Ramro Patro, captured 16 November 2026. Rates are NPR/kg and retain minimum, maximum and average values. The app reads this bundled snapshot; it does not call the website on every page view.

Source: https://ramropatro.com/vegetable

The GitHub Actions workflow `.github/workflows/weekly-market-snapshot.yml` attempts a refresh each Monday. The parser fails closed if the source table changes or too few expected commodities are found, preserving the previous snapshot rather than publishing guessed values.

Potato uses the matching red-long potato average from the snapshot (NPR 58/kg on the capture date). The current vegetable list has no matching quote for millet, buckwheat, maize/beans, lentil, mustard, wheat/barley or turmeric/ginger. Their price values remain model assumptions and are labelled accordingly. Wholesale prices are not guaranteed farm-gate prices.
