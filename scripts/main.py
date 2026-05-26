import requests
import pandas as pd
import matplotlib.pyplot as plt

all_data = []
page = 1

url = "https://api.worldbank.org/v2/country/all/indicator/SH.TBS.INCD?format=json&per_page=1000"
response = requests.get(url=url)
data = response.json()

total_pages = data[0]["pages"]

print(f"Total pages: {total_pages}")

records = data[1]

for page in range(1, total_pages + 1):

    url = f"https://api.worldbank.org/v2/country/all/indicator/SH.TBS.INCD?format=json&per_page=1000&page={page}"
    response = requests.get(url)
    data = response.json()

    records = data[1]

    for record in records:

        country = record["country"]["value"]
        year = record["date"]
        value = record["value"]

        # Skip missing values
        if value is None:
            continue

        all_data.append({
            "Country": country,
            "Year": int(year),
            "TB_Incidence": value
        })

# Create dataframe
df = pd.DataFrame(all_data)

exclude_keywords = [
    "income",
    "World",
    "IDA",
    "IBRD",
    "OECD",
    "dividend",
    "states",
    "Central",
    "Polynesia",
    "Europe",
    "Asia",
    "Caribbean",
    "Middle East",
    "North America",
    "South Asia",
    "Sub-Saharan"
]

for keyword in exclude_keywords:
    df = df[~df["Country"].str.contains(keyword, case=False, na=False)]

# Save CSV
df.to_csv("tb_incidence.csv", index=False)

# In the last year, which countries had the highest incidence
latest_year = df["Year"].max()

latest_data = df[df["Year"] == latest_year]

top_countries = latest_data.sort_values(
    by="TB_Incidence",
    ascending=False
).head(10)

# print(top_countries.head(10))
plt.figure(figsize=(12, 6))

plt.bar(
    top_countries["Country"],
    top_countries["TB_Incidence"]
)

# Labels
plt.title(f"Top 10 TB Incidence Countries ({latest_year})")
plt.xlabel("Country")
plt.ylabel("TB Incidence")

# Rotate labels
plt.xticks(rotation=45)

# Show
plt.show()

# What is the trend of TB incidence in South Africa
south_africa = df[df["Country"].str.contains("South Africa", case=False)]

south_africa = south_africa.sort_values(by="Year")

plt.figure(figsize=(10, 5))

plt.plot(
    south_africa["Year"],
    south_africa["TB_Incidence"]
)

# Labels
plt.title("TB Incidence in South Africa Over Time")
plt.xlabel("Year")
plt.ylabel("TB Incidence")

plt.show()
