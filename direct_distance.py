import math

def calculate_direct_distance(lat1, lon1, lat2, lon2):
    
    R = 6371.0 # Earth's mean radius in km
    
    # degrees to radians convertion
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    
    # Apply Haversine formula
    a = (math.sin(delta_phi / 2) ** 2 + 
         math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2)
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # final distance calculation
    distance = R * c
    return distance

# sample values for testing
resort_lat, resort_lon = 36.1147, -115.1728  # resort coordinates
activity_lat, activity_lon = 36.0119, -114.9389 # activity coordinates

total_distance = calculate_direct_distance(resort_lat, resort_lon, activity_lat, activity_lon)
print(f"Direct Distance: {total_distance:.2f} km")

