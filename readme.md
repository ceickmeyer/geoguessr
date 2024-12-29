### README.md

# OverPass Turbo GeoJSON to GeoGuessr CSV Coordinates

This script extracts coordinates from a GeoJSON file and saves them in a CSV file. It supports Point and Polygon geometries, converting them into a format suitable for use in tools like [MapCheckr](https://mapcheckr.vercel.app/) to create high-quality GeoGuessr maps.

## Features

- **Supports Point and Polygon geometries**: Extracts coordinates for `Point` directly and takes the first coordinate of the first ring for `Polygon`.
- **Easy CSV Export**: Outputs a CSV file with `Latitude` and `Longitude` columns for easy use in map-making tools.
- **Streamlined Workflow**: Designed to integrate with Overpass Turbo and GeoGuessr's map-making process.

---

## Requirements

- **Python 3.x**
- Standard Python libraries: `json`, `csv`

---

## How to Use

### Step 1: Create and Export a GeoJSON File

1. Use [Overpass Turbo](https://overpass-turbo.eu/) to create a query.
2. Export the results as a **GeoJSON** file.
3. Save the file in the same directory as the script and rename it to `export.geojson`.

---

### Step 2: Run the Script

1. Save the provided Python script as `export.py`.
2. Open a terminal and navigate to the directory containing `export.py` and `export.geojson`.
3. Run the script using:
   ```bash
   python export.py
   ```
4. The script will generate a file named `extracted_coordinates.csv` in the same directory.

---

### Step 3: Verify and Publish Your Map

1. Open the CSV file to ensure the coordinates are correct.
2. Upload the coordinates to GeoGuessr's map-making tool.
3. Use [MapCheckr](https://mapcheckr.vercel.app/) to resolve issues such as:
   - Duplicate locations within 10 meters.
   - Any other anomalies in the map data.

---

## Output Example

The `extracted_coordinates.csv` will look like this:

| Latitude | Longitude |
| -------- | --------- |
| 47.6097  | -122.3331 |
| 40.7128  | -74.0060  |
| ...      | ...       |

---

## Notes

- Ensure your GeoJSON file contains valid `Point` or `Polygon` geometries. Other geometry types are not supported.
- GeoJSON uses the `(longitude, latitude)` coordinate order, which the script automatically converts to `(latitude, longitude)` for CSV export.

Feel free to adapt the script to your specific requirements!

---

Happy map-making!
