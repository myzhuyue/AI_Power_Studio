#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  4 22:12:19 2025

@author: ryan
"""

import pandas as pd
import glob
import os


# ************************** Merge CSV files **********************************
# Step 1: Set the folder path
folder_path = '/Users/ryan/Desktop/DataGlassdoor/Raw'

# Step 2: Get all CSV files in that folder
csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

# Step 3: Read and merge
df_merged = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)



# ************************* Select Tech-Related Roles *************************

# Final cleaned keyword list
tech_keywords = [
    # From left column - job titles in screenshot 1
    "business analyst", "business intelligence developer", "decision analyst",
    "data analyst", "data strategy", "data management", "data scientist",
    "data engineer", "quant developer", "quantitative developer",
    "operational risk", "risk engineer", "risk modelling", "business manager",
    "business functional analyst", "project manager", "program manager",
    "change manager", "transformation director", "cloud transformation",
    "implementation manager", "governance manager", "control manager",
    "software engineer", "software developer", "software programming",
    "programmer", "systems analyst", "applications support", "desktop support",
    "windows systems", "gateway support", "ux designer", "it consultant",
    "it auditor",

    # From right column - keyword triggers
    "data", "bi", "pmo", "project", "change", "transformation",
    "implementation", "governance", "control", "tester", "software",
    "developer", "devops", "qa", "engineer", "architect", "infrastructure",
    "desktop", "cyber", "security", "ux", "ui", "it", "technology", "tech",
    "technician",

    # From automation team (screenshot 2)
    "business analyst", "business analyst lead", "solution architect",
    "automation developer", "infrastructure lead", "test developer",
    "project manager", "program manager", "citizen developer",
    "automation champions"
]


# Normalize job titles
df_merged['jobTitle_clean'] = (
    df_merged['jobTitle']
    .astype(str)
    .str.lower()
    .str.strip()
    .str.replace(r'[^a-z0-9\s]', ' ', regex=True)  # remove special characters
    .str.replace(r'\s+', ' ', regex=True)  # collapse multiple spaces
)

# Build keyword pattern
pattern = '|'.join(tech_keywords)

# Filter rows where jobTitle_clean contains any tech-related keyword
df_filtered = df_merged[df_merged['jobTitle_clean'].str.contains(pattern, na=False)]



# ********************** Normalize:LengthOfEmployment *************************

# Show all unique LengthOfEmployment values
unique_lengths = df_filtered['LengthOfEmployment'].dropna().unique()
print(f"Total unique LengthOfEmployment values: {len(unique_lengths)}")
print(unique_lengths)

# Map numeric LengthOfEmployment to readable categories
def map_experience(years):
    if years == 0:
        return 'less than 1 year'
    elif years <= 1:
        return 'more than 1 year'
    elif years <= 3:
        return 'more than 3 years'
    elif years <= 5:
        return 'more than 5 years'
    elif years <= 8:
        return 'more than 8 years'
    else:
        return 'more than 10 years'

# Apply mapping to create a new column
df_filtered['LengthOfEmployment_Label'] = df_filtered['LengthOfEmployment'].apply(map_experience)



# ************************** Location Add Country******************************


# Show all unique location values
unique_locations = df_filtered['location'].dropna().unique()
print(f"Total unique locations: {len(unique_locations)}")
print(unique_locations)


from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import time
import json


# Step 1: Try to load existing location-to-country mapping
mapping_path = '/Users/ryan/Desktop/DataGlassdoor/location_to_country_mapping.json'

try:
    with open(mapping_path, 'r', encoding='utf-8') as f:
        location_to_country = json.load(f)
    print("Loaded existing location-to-country mapping.")
except FileNotFoundError:
    location_to_country = {}
    print("No existing mapping found. Will create one.")

# Step 2: Initialize geocoder
geolocator = Nominatim(user_agent="glassdoor-location-augmenter")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# Step 3: Collect all unique location values
unique_locations = df_filtered['location'].dropna().unique()
print(f"Total unique locations: {len(unique_locations)}")

# Step 4: Update mapping for missing values with normalized lookup
for loc in unique_locations:
    if loc not in location_to_country:
        # Normalize for lookup only
        norm_loc = (
            loc.strip()
            .lower()
            .replace("  ", " ")
            .replace("-", " ")
            .replace("_", " ")
        )

        # Optional aliases
        aliases = {
            "nyc": "new york, ny",
            "la": "los angeles, ca",
            "sf": "san francisco, ca",
            "hk": "hong kong",
            "sg": "singapore",
            "london": "london, england"
        }
        norm_loc = aliases.get(norm_loc, norm_loc)

        try:
            geo = geocode(norm_loc)
            if geo:
                country = geo.address.split(",")[-1].strip()
                location_to_country[loc] = f"{loc}, {country}"
            else:
                location_to_country[loc] = f"{loc}, Unknown"
        except Exception as e:
            location_to_country[loc] = f"{loc}, Error"
            print(f"Error for {loc}: {e}")
        time.sleep(1)


# Step 5: Save the updated mapping
with open(mapping_path, 'w', encoding='utf-8') as f:
    json.dump(location_to_country, f, ensure_ascii=False, indent=2)
    print("Saved updated location-to-country mapping.")

# Step 6: Create df_country with updated location info
df_country = df_filtered.copy()
df_country['location_with_country'] = df_country['location'].map(location_to_country)



# *********************** Basic Information ***********************************

df_filtered.info(), df_filtered.head()

df_filtered.describe()



# ****************** Save/ Update files ***************************************

# Save the full merged data
df_merged.to_csv('/Users/ryan/Desktop/DataGlassdoor/Glassdoor_Merged.csv', index=False)

# Save the tech-role-filtered data
df_filtered.to_csv('/Users/ryan/Desktop/DataGlassdoor/Gladdsoor_Merge_Select.csv', index=False)

# Save the normalize data
df_filtered.to_csv('/Users/ryan/Desktop/DataGlassdoor/Gladdsoor_Merge_Select_Normalize.csv', index=False)

# Save the location country data
df_country.to_csv('/Users/ryan/Desktop/DataGlassdoor/Gladdsoor_Merge_Select_Country.csv', index=False)



