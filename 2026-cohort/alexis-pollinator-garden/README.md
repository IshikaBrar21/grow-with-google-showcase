# Native Plant & Pollinator Recommender — Data

**Project:** Catalyst Architects — Grow with Google Capstone
**SDG Goal:** Goal 15 — Life on Land
**Problem statement:** Urban gardeners lack simple, automated tools to identify native plant species that support local pollinator populations. This project recommends native plants suited to a gardener's location and conditions.

**Role:** Data Analyst — dataset scoping, schema design, species research, data cleaning, verification

## What's in this folder

| File | Description |
|---|---|
| `data/plant_species_maryland_piedmont.csv` | Final dataset — 40 native plant species scoped to Maryland's Piedmont Plateau ecoregion |
| `data/data_dictionary.md` | Column-by-column documentation of the dataset schema and standardized values |
| `data/plant_species_template.csv` | Blank schema template, useful if the dataset is later expanded to other regions |

## Dataset summary

- **40 species** covering perennial flowers, trees, shrubs, and vines
- Scoped to the **Eastern Broadleaf Forest ecoregion (#221)**, specifically the **Piedmont Plateau** portion of Maryland
- 14-column schema: species ID, common/scientific name, native range, bloom window, sun/soil/moisture needs, pollinators supported, hardiness zones, and source
- Sourced primarily from the **Pollinator Partnership's Eastern Broadleaf Forest regional planting guide**, cross-checked against the **Maryland DNR native plant guide (HG#120)** and **Kew's Plants of the World Online (POWO)** for native-status verification

## Verification status

- **21 species** formally confirmed as Maryland-native via MD DNR and/or Kew POWO
- **17 species** flagged with a lighter note — their documented native range covers the broader Mid-Atlantic region, but individual Maryland/county-level confirmation is still recommended (BONAP/USDA spot-check) before treating as fully verified
- **1 species (Liatris spicata)** flagged as historically rare/localized within Maryland (recorded mainly in Baltimore and Washington counties) — usable, but worth noting in the app if precision matters
- **1 species (Echinacea purpurea / Purple Coneflower)** — flagged as a team decision. It is not on Maryland's official native plant list (its native range is the central/midwestern US), though it's widely planted and naturalized here. Team should decide whether to keep it as a regionally-adapted pollinator plant or swap it for a confirmed Piedmont native.

See the `notes` column in the CSV for verification detail on every individual row.

## Known limitations / next steps

- Full BONAP county-level spot-check for the 17 flagged species
- Team decision on Purple Coneflower
- Dataset could be expanded beyond 40 species (target range considered: 50–100) using the guide's Host Plant table or additional BONAP/USDA sourcing
- All values are grounded in the sources cited in `source_url`; further changes should preserve source citations for traceability
