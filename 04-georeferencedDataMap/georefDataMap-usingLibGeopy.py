import folium
from geopy.geocoders import Nominatim
import time

def get_coordinates(city, country):
    """Retrieve latitude and longitude for a given city using geopy."""
    geolocator = Nominatim(user_agent="geo_lookup")
    location = geolocator.geocode(f"{city}, {country}")
    if location:
        return location.latitude, location.longitude
    return None

def read_hits_file(filename):
    """Read the file and extract city, country, and hits."""
    hits_data = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if ':' in line:
                location, hits = line.rsplit(':', 1)
                city, country = map(str.strip, location.split(','))
                hits = int(hits.strip())
                hits_data.append((city, country, hits))
    return hits_data

def create_map(hits_data):
    """Generate a folium map with markers for each city."""
    city_map = folium.Map(location=[20, 0], zoom_start=2)
    
    for city, country, hits in hits_data:
        coords = get_coordinates(city, country)
        if coords:
            folium.Marker(
                location=coords,
                popup=f"{city}, {country}: {hits} hits",
                icon=folium.Icon(color='blue')
            ).add_to(city_map)
        time.sleep(1)  # Prevent rate limiting
    
    city_map.save("website_hits_map.html")
    print("Map saved as website_hits_map.html")

if __name__ == "__main__":
    hits_data = read_hits_file("website_hits.txt")
    create_map(hits_data)
