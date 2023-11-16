#...


#import libraries
import pandas as pd
import matplotlib.pyplot as plt

#import dataset
df_emissions = pd.read_csv("C:\\Users\\thorb\\OneDrive - Technische Universität Berlin\\Dokumente\\Uni\\Master\\Wi Ing\\TU Berlin\\Semester\\5. Sem - WiSe 23 24 Ausland\\Study\\Python for Sustainability Analysis\\TEP4221\\Project\\Data\\Dataset EEA 2023.csv", header=0, index_col=0, delimiter='\t')

#filter and clean dataset
df_nh3_rawdata = (df_emissions.loc[(df_emissions['Pollutant_name'] == "NH3")])
df_nh3_clean = df_nh3_rawdata.dropna(subset=["Emissions"])


# Create a variable (dictionary) that maps each country to its region in europe
country_to_region= {
    'Austria': 'West',
    'Belgium': 'West',
    'Denmark': 'North',
    'Finland': 'North',
    'France': 'West',
    'Germany': 'West',
    'Greece': 'South',
    'Ireland': 'West',
    'Italy': 'South',
    'Luxembourg': 'West',
    'Netherlands': 'West',
    'Portugal': 'South',
    'Spain': 'South',
    'Sweden': 'North',
    'Bulgaria': 'East',
    'Croatia': 'East',
    'Cyprus': 'South',
    'Czechia': 'East',
    'Estonia': 'East',
    'Hungary': 'East',
    'Lithuania': 'East',
    'Latvia': 'East',
    'Malta': 'South',
    'Poland': 'East',
    'Romania': 'East',
    'Slovenia': 'East',
    'Slovakia': 'East',
    'EU27': 'Various', # EU27 includes countries from different regions
    'Switzerland': 'West',
    'Iceland': 'North',
    'Liechtenstein': 'West',
    'Norway': 'North',
    'Türkiye': 'East',
    'EEA32': 'Various' # EEA32 includes countries from different regions (EU countries + Iceland, Liechtenstein, Norway + EU(?) + UK(???))           
}

# Create a DataFrame with countries and their assigned regions
country_data = pd.DataFrame({'Country': list(country_to_region.keys()), 'Region': list(country_to_region.values())})
print(country_data)


#create df that contains the emissions of the given dataset per year
TotalEmissions_per_year = df_nh3_clean.groupby("Year").sum()

#add region information to dataframe
df_nh3_clean['Region'] = df_nh3_clean['Country'].map(country_to_region)

#df_nh3_clean.to_excel("nh3 total.xlsx")

#prepare information that is to be plotted
df_emissions_by_reg_and_year = df_nh3_clean.groupby(["Region","Year"]).sum()


#Plotting total emissions for each region and Europe
regions = ["North", "East", "South", "West"]
colors = ['blue', 'orange', 'red', 'green']

# %%
# Plot total NH3 emissions in Europe per region & total

plt.figure(figsize=(12, 6))

for i, region in enumerate(regions):
    region_data = df_emissions_by_reg_and_year.loc[region]
    plt.plot(region_data.index, region_data["Emissions"], label=region, color=colors[i])

# Plot total emissions for Europe
df_nh3_clean_filtered = df_nh3_clean[df_nh3_clean.Region != "Various"]
TotalEmissions_per_year_filtered= df_nh3_clean_filtered.groupby("Year").sum()

europe_data = TotalEmissions_per_year_filtered
plt.plot(europe_data.index, europe_data["Emissions"], label="Europe", color='black', linestyle='--')

# Modify and safe plot
plt.xlabel("Year")
plt.ylabel("NH3 Emissions [Gg]")
plt.title("Total NH3 Emissions in Europe")
plt.legend()
plt.grid(True)

plt.savefig("Total NH3 Emissions in Europe.png")
plt.show()


# %%
# Plot agricultural NH3 emissions in Europe per region & total


# Preparation - NH3 Data only for the agricultural sectos
# List of sector names related to agriculture

agriculture_sector_names = [
    "Agriculture/Forestry/Fishing: Off-road vehicles and other machinery",
    "Agriculture/Forestry/Fishing: National fishing",
    "Agriculture/Forestry/Fishing: Stationary"
    "Farm-level agricultural operations including storage, handling and transport of agricultural products",
    "Off-farm storage, handling and transport of bulk agricultural products",
    "Cultivated crops",
    "Use of pesticides",
    "Field burning of agricultural residues",
    "Agriculture other",
    "Manure management - Dairy cattle",
    "Manure management - Non-dairy cattle",
    "Manure management - Sheep",
    "Manure management - Swine",
    "Manure management - Buffalo",
    "Manure management - Goats",
    "Manure management - Horses",
    "Manure management - Mules and asses",
    "Manure mangement - Laying hens",
    "Manure mangement - Broilers",
    "Manure mangement - Turkeys",
    "Manure mangement - Other poultry",
    "Manure management - Other animals",
    "Inorganic N-fertilizers (includes also urea application)",
    "Animal manure applied to soils",
    "Sewage sludge applied to soils",
    "Other organic fertilisers applied to soils (including compost)",
    "Urine and dung deposited by grazing animals",
    "Crop residues applied to soils",
    "Indirect emissions from managed soils",
]

# Filter the (EU-country)filtered DataFrame "df_nh3_clean_filtered" based on the agriculture sector names
df_agriculture = df_nh3_clean_filtered[df_nh3_clean_filtered['Sector_name'].isin(agriculture_sector_names)]

agric_emissions_per_year = df_agriculture.groupby("Year")["Emissions"].sum()


# Plot total emissions for each region
plt.figure(figsize=(12, 6))

df_agric_by_reg_and_year = df_agriculture.groupby(["Region","Year"]).sum()
for i, region in enumerate(regions):
    region_data = df_agric_by_reg_and_year.loc[region]
    plt.plot(region_data.index, region_data["Emissions"], label=region, color=colors[i])

# Plot total emissions for Europe
AgricEmissions_per_year_filtered= df_agriculture.groupby("Year").sum()

europe_data_agric = AgricEmissions_per_year_filtered
plt.plot(europe_data_agric.index, europe_data_agric["Emissions"], label="Europe", color='black', linestyle='--')

#Modify
plt.xlabel("Year")
plt.ylabel("NH3 Emissions [Gg]")
plt.title("Agricultural NH3 Emissions in Europe")
plt.legend()
plt.grid(True)

plt.savefig("Agricultural NH3 Emissions in Europe.png")
plt.show()

# %%
# Reference data - PM 2.5

#filter and clean dataset
df_pm25 = (df_emissions.loc[(df_emissions['Pollutant_name'] == "PM2.5")])
df_pm25_clean = df_pm25.dropna(subset=["Emissions"])

#Add regions to dataframe 
df_pm25_clean['Region'] = df_pm25_clean['Country'].map(country_to_region)


df_pm25_EEA32 = df_pm25_clean[(df_pm25_clean['Region'] != "Various") & (df_pm25_clean['Sector_code'] == "NATIONAL TOTAL")]
# Calculate the total sum of emissions of all sectors
TotalEmissions_per_year = df_pm25_EEA32.groupby("Year")["Emissions"].sum() 

# %%
# Plot total PM 2.5 emissions in Europe per region & total

# data for europe
years = TotalEmissions_per_year.index
total_emissions = TotalEmissions_per_year.values

# data for regions
region_emissions = {}
for region in regions:
    region_data = df_pm25_EEA32[df_pm25_EEA32['Region'] == region]
    region_emissions[region] = region_data.groupby("Year")["Emissions"].sum().values

# creating plot
plt.figure(figsize=(12, 6))

# plotting regions
for region, color in zip(regions, colors):
    plt.plot(years, region_emissions[region], label=region, color=color)

# plotting emissions for europe
plt.plot(years, total_emissions, label="Europe", color='black', linestyle='--')

plt.xlabel("Year")
plt.ylabel("PM 2.5 Emissions [Gg]")
plt.title("Total PM 2.5 Emissions in Europe")
plt.legend()
plt.grid(True)

plt.savefig('Total PM 2.5 Emissions in Europe.png')
plt.show()

# %%
# Plot agricultural PM25 emissions in Europe per region & total


# Preparation - PM25 Data only for the agricultural sectos
# List of sector names related to agriculture

agriculture_sector_names = [
    "Agriculture/Forestry/Fishing: Off-road vehicles and other machinery",
    "Agriculture/Forestry/Fishing: National fishing",
    "Agriculture/Forestry/Fishing: Stationary",
    "Farm-level agricultural operations including storage, handling and transport of agricultural products",
    "Off-farm storage, handling and transport of bulk agricultural products",
    "Cultivated crops",
    "Use of pesticides",
    "Field burning of agricultural residues",
    "Agriculture other",
    "Manure management - Dairy cattle",
    "Manure management - Non-dairy cattle",
    "Manure management - Sheep",
    "Manure management - Swine",
    "Manure management - Buffalo",
    "Manure management - Goats",
    "Manure management - Horses",
    "Manure management - Mules and asses",
    "Manure mangement - Laying hens",
    "Manure mangement - Broilers",
    "Manure mangement - Turkeys",
    "Manure mangement - Other poultry",
    "Manure management - Other animals",
    "Inorganic N-fertilizers (includes also urea application)",
    "Animal manure applied to soils",
    "Sewage sludge applied to soils",
    "Other organic fertilisers applied to soils (including compost)",
    "Urine and dung deposited by grazing animals",
    "Crop residues applied to soils",
    "Indirect emissions from managed soils",
]

#Creating df with emissions only of agricultural sectors
df_agriculture = df_pm25_clean[(df_pm25_clean['Region'] != "Various") & df_pm25_clean['Sector_name'].isin(agriculture_sector_names)]

#Creating df with total agriculture emissions per year
agric_emissions_per_year = df_agriculture.groupby("Year")["Emissions"].sum()

#df_agriculture.to_excel("agric_emissions_per_year pm25.xlsx")

# %%
#Plotting PM 2.5 emissions of agriculture
import matplotlib.pyplot as plt

regions = ["North", "East", "South", "West"]
colors = ['blue', 'orange', 'red', 'green']

# data for europe
years = agric_emissions_per_year.index
agric_emissions = agric_emissions_per_year.values

# data for regions
region_emissions = {}
for region in regions:
    region_data = df_agriculture[df_agriculture['Region'] == region]
    region_emissions[region] = region_data.groupby("Year")["Emissions"].sum().values

# creating plot
plt.figure(figsize=(12, 6))

# plotting regions
for region, color in zip(regions, colors):
    plt.plot(years, region_emissions[region], label=region, color=color)

# plotting emissions for europe
plt.plot(years, agric_emissions, label="Europe", color='black', linestyle='--')

plt.xlabel("Year")
plt.ylabel("PM 2.5 Emissions [Gg]")
plt.title("Agricultural PM 2.5 Emissions in Europe")
plt.legend()
plt.grid(True)

plt.savefig('Agricultural PM 2.5 Emissions in Europe.png')
plt.show()

# %%
# Combine Total Emissions Diagrams 

# Create figure with 2 subplots and one x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Plot "Total NH3 Emissions by Region and Year" on 1st subplot
for i, region in enumerate(regions):
    region_data = df_emissions_by_reg_and_year.loc[region]
    ax1.plot(region_data.index, region_data["Emissions"], label=region, color=colors[i])

ax1.plot(europe_data.index, europe_data["Emissions"], label="Europe", color='black', linestyle='--')

ax1.set_ylabel("NH3 Emissions [Gg]")
ax1.set_title("Total NH3 and PM 2.5 Emissions in Europe")
ax1.legend(loc="center right")
ax1.grid(True)

#Plot second subplot - PM 2.5

region_emissions = {}
for region in regions:
    region_data = df_pm25_EEA32[df_pm25_EEA32['Region'] == region]
    region_emissions[region] = region_data.groupby("Year")["Emissions"].sum().values

for region, color in zip(regions, colors):
    plt.plot(years, region_emissions[region], label=region, color=color)

ax2.plot(years, total_emissions, label="Europe", color='black', linestyle='--')
ax2.set_xlabel("Year")
ax2.set_ylabel("PM2.5 Emissions [Gg]")
ax2.legend()
ax2.grid(True)


plt.tight_layout()
plt.savefig('Total Emissions Overview.png')
plt.show()



# %%
# Combine Agricultural Emissions Diagrams 

# Create figure with 2 subplots and one x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Plot "Agricultural NH3 Emissions by Region and Year" on 1st subplot

for i, region in enumerate(regions):
    region_data = df_agric_by_reg_and_year.loc[region]
    ax1.plot(region_data.index, region_data["Emissions"], label=region, color=colors[i])

ax1.plot(europe_data_agric.index, europe_data_agric["Emissions"], label="Europe", color='black', linestyle='--')

# Modify
ax1.set_ylabel("NH3 Emissions [Gg]")
ax1.set_title("Agricultural NH3 and PM 2.5 Emissions in Europe")
ax1.legend()
ax1.grid(True)

# Plot second subplot - PM 2.5

region_emissions = {}
for region in regions:
    region_data = df_agriculture[df_agriculture['Region'] == region]
    region_emissions[region] = region_data.groupby("Year")["Emissions"].sum().values

for region, color in zip(regions, colors):
    ax2.plot(years, region_emissions[region], label=region, color=color)

ax2.plot(years, agric_emissions, label="Europe", color='black', linestyle='--')
ax2.set_xlabel("Year")
ax2.set_ylabel("PM 2.5 Emissions [Gg]")
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig('Agricultural Emissions Overview.png')
plt.show()


# %%
# Combine Agricultural Emissions Diagrams
