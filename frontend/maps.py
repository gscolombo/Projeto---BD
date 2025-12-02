import folium
import streamlit as st

def create_interactive_map(center=None, zoom_start=5, marker_locations=None, clickable=False):
    """Create a Folium map for location selection"""
    if center is None:
        center = st.session_state.map_center
    
    m = folium.Map(
        location=center,
        zoom_start=zoom_start,
        control_scale=True,
        tiles='OpenStreetMap',
    )
    
    # Add click event to get coordinates
    if clickable:
        m.add_child(folium.LatLngPopup())
    
    # Add marker if location is provided
    if marker_locations:
        for loc in marker_locations:
            folium.Marker(
                loc,
                popup=f"Latitude: {loc[0]:.6f}\nLongitude: {loc[1]:.6f}",
                tooltip="Clique para ver coordenadas",
                icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(m)
    
    return m