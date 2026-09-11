# FAO OpenEO Documentation

Documentation for the FAO OpenEO API, organized following the [Diataxis framework](https://diataxis.fr/).

## Tutorials

Step-by-step learning experiences using Jupyter notebooks. Start from the beginning and work through each tutorial in order.

| # | Tutorial | Description |
|---|----------|-------------|
| 1 | [Getting Started](tutorials/01_getting_started.ipynb) | Connect, authenticate, explore collections, load your first data cube |
| 2 | [NDVI Time Series](tutorials/02_ndvi_time_series.ipynb) | Vegetation monitoring — time series, anomalies, drought classification |
| 3 | [Zonal Statistics](tutorials/03_zonal_statistics.ipynb) | Aggregate raster data over administrative regions and polygons |
| 4 | [Climate Risk (CRTB)](tutorials/04_climate_risk_crtb.ipynb) | Hazard, vulnerability, exposure, and adaptive capacity assessment |
| 5 | [Planting Recommendations](tutorials/05_planting_recommendations.ipynb) | Agricultural planning with PLAN-T maize variety and stressor analysis |

### Running the Notebooks

```bash
pip install openeo matplotlib pandas numpy rasterio
jupyter notebook docs/tutorials/
```

The notebooks connect to the FAO OpenEO backend at `https://data.fao.org/openeo`. Use the demo credentials (`demo`/`demo`) or authenticate via OIDC for production access.

### Web Editor

For a visual, no-code interface, use the [OpenEO Web Editor](https://data.fao.org/editor/?server=data.fao.org%2Fopeneo).

## Documentation Structure (Diataxis)

```
docs/
├── tutorials/          # Learning-oriented — guided Jupyter notebooks
│   ├── 01_getting_started.ipynb
│   ├── 02_ndvi_time_series.ipynb
│   ├── 03_zonal_statistics.ipynb
│   ├── 04_climate_risk_crtb.ipynb
│   └── 05_planting_recommendations.ipynb
├── how-to/             # Task-oriented — (planned) practical guides
├── reference/          # Information-oriented — (planned) API and process reference
└── explanation/        # Understanding-oriented — (planned) concepts and architecture
```
