# FAO OpenEO Documentation

Documentation for the FAO OpenEO API, organized following the [Diataxis framework](https://diataxis.fr/).

## Tutorials

Step-by-step learning experiences using Jupyter notebooks. Start from the beginning and work through each tutorial in order.

| # | Tutorial | Description |
|---|----------|-------------|
| 1 | [Getting Started](tutorials/01_getting_started.ipynb) | Connect, authenticate, explore collections, load your first data cube |
| 2 | [Vegetation Time Series](tutorials/02_ndvi_time_series.ipynb) | Vegetation monitoring with VCI — time series, anomalies, drought classification |
| 3 | [Zonal Statistics](tutorials/03_zonal_statistics.ipynb) | Aggregate raster data over administrative regions and polygons |
| 4 | [Climate Risk (CRTB)](tutorials/04_climate_risk_crtb.ipynb) | Hazard, vulnerability, exposure, and adaptive capacity assessment |
| 5 | [Planting Recommendations](tutorials/05_planting_recommendations.ipynb) | Agricultural planning with PLAN-T maize variety and stressor analysis |
| 6 | [Data Cube Operations](tutorials/06_data_cube_operations.ipynb) | Filtering, cube arithmetic, masking, merging, resampling, convolution, temporal aggregation |
| 7 | [Drought Monitoring](tutorials/07_drought_monitoring.ipynb) | Climatological normals, percent of normal, severity classes, county ranking, CSV export |
| 8 | [Reusable Process Graphs](tutorials/08_reusable_process_graphs.ipynb) | Process graph JSON, user-defined processes with parameters, Web Editor round trip |

### Running the Notebooks

```bash
pip install -r requirements.txt jupyter
jupyter notebook tutorials/
```

The notebooks connect to the FAO OpenEO backend at `https://data.fao.org/openeo` and authenticate via OIDC (FAO Single Sign-On).

### Web Editor

For a visual, no-code interface, use the [OpenEO Web Editor](https://data.fao.org/editor/?server=data.fao.org%2Fopeneo).

## Building the Site

The site is built with [Quarto](https://quarto.org/). Notebooks are not executed during rendering; the published pages show the outputs saved in each `.ipynb`.

```bash
quarto preview   # live local preview
quarto render    # build into _site/
```

Pushes to `main` are rendered and deployed to GitHub Pages by `.github/workflows/publish-docs.yml`.

## Documentation Structure (Diataxis)

```
├── tutorials/          # Learning-oriented — guided Jupyter notebooks
│   ├── 01_getting_started.ipynb
│   ├── 02_ndvi_time_series.ipynb
│   ├── 03_zonal_statistics.ipynb
│   ├── 04_climate_risk_crtb.ipynb
│   ├── 05_planting_recommendations.ipynb
│   ├── 06_data_cube_operations.ipynb
│   ├── 07_drought_monitoring.ipynb
│   ├── 08_reusable_process_graphs.ipynb
│   └── data/           # Sample boundary files used by the tutorials
├── how-to/             # Task-oriented — Web Editor, workspaces
├── reference/          # Information-oriented — processes, FAO processes, formats and limits
├── scripts/            # generate_process_reference.py (regenerates reference/processes.qmd)
└── explanation/        # Understanding-oriented — (planned) concepts and architecture
```
