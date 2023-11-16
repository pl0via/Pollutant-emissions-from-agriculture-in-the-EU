# Pollutant-emissions-from-agriculture-in-the-EU


## Overview
This Python script is designed for analyzing and visualizing ammonia (NH3) and particulate matter (PM2.5) emissions data in Europe. The script utilizes the pandas and matplotlib libraries to import, clean, and visualize the emissions data.

## Requirements

Make sure you have the following libraries installed before running the script:

- pandas
- matplotlib

You can install them using the following command:

```bash
pip install pandas matplotlib
```

Additionally, you can set up a virtual environment using the provided `env.yml` file:

```bash
conda env create -f env.yml
conda activate your_environment_name
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/pl0via/Agricultural-Emissions.git
cd Agricultural-Emissions
```

2. Run the Python script:

```bash
python TEP4221_project.py
```

3. The script will generate multiple plots showcasing total and agricultural NH3 and PM2.5 emissions in Europe and its regions over the specified years. The resulting plots will be saved as image files in the same directory.

## Features

Custom Region Mapping: Users can customize the mapping of countries to EU regions ("North", "West", "South", "East") by modifying the "country_to_region" dictionary in the script.

Sector Selection: Explore different industrial sectors by adjusting the "agriculture_sector_names" list in the script to focus on specific areas of interest.

Plot Customization: Users can modify the type, size, names, and colors of the generated plots according to their preferences by tweaking the corresponding parameters in the script.

## Data Source

The script relies on a CSV file named "CLRTAP_NVFR19_V23_1_GF_csv.csv". It contains open source emissions data from Eurostat, accessible via the following link:
https://www.eea.europa.eu/en/datahub/datahubitem-view/5be6cebc-ed2b-4496-be59-93736fc4ad78

There is also an online European Environments Agency's (EEA) Data Explorer based on the CLRTAP data, accessible via the following link:
https://www.eea.europa.eu/data-and-maps/dashboards/air-pollutant-emissions-data-viewer-5

Make sure to replace the csv file with your own dataset or update the file path accordingly.

## File Structure

- `TEP4221_project.py`: The main Python script.
- `Total NH3 Emissions in Europe.png`: Image file depicting total NH3 emissions in Europe and its regions.
- `Agricultural NH3 Emissions in Europe.png`: Image file illustrating agricultural NH3 emissions in Europe and its regions.
- `Total PM 2.5 Emissions in Europe.png`: Image file showing total PM2.5 emissions in Europe and its regions.
- `Agricultural PM 2.5 Emissions in Europe.png`: Image file displaying agricultural PM2.5 emissions in Europe and its regions.
- `Total Emissions Overview.png`: Combined image file showcasing total NH3 and PM2.5 emissions in Europe.
- `Agricultural Emissions Overview.png`: Combined image file illustrating agricultural NH3 and PM2.5 emissions in Europe.

## Environment

The required Python environment can be set up using the provided `env.yml` file. Download and activate the environment using the following commands:

```bash
conda env create -f env.yml
conda activate your_environment_name
```

## License

This script is released under the [MIT License](LICENSE). Feel free to use, modify, and distribute it according to your needs. If you find it helpful, consider providing attribution.

## Contact

For questions or feedback, please contact the author (mailto:ts656686@gmail.com).
