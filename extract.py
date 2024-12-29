import json
import csv

# Path to the uploaded GeoJSON file
input_geojson_path = 'export.geojson'
output_csv_path = 'extracted_coordinates.csv'

# Load the GeoJSON data
with open(input_geojson_path, 'r') as geojson_file:
    geojson_data = json.load(geojson_file)

# Extract coordinates
coordinates = []
for feature in geojson_data.get('features', []):
    geometry = feature.get('geometry', {})
    if geometry['type'] == 'Point':
        # Extract coordinates directly for Point geometries
        coordinates.append(geometry['coordinates'])
    elif geometry['type'] == 'Polygon':
        # Extract the first coordinate of the first ring for Polygon geometries
        if geometry['coordinates'] and geometry['coordinates'][0]:
            coordinates.append(geometry['coordinates'][0][0])

# Write the extracted coordinates to a CSV file
with open(output_csv_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Latitude', 'Longitude'])  # Write header
    for lon, lat in coordinates:  # GeoJSON uses (lon, lat) order
        csv_writer.writerow([lat, lon])

output_csv_path 