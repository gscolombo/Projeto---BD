import streamlit as st
from streamlit_folium import st_folium

from request_utils import get_locations
from maps import create_interactive_map


@st.cache_data
def _get_locations():
    return get_locations()


def reset_form(loc):
    st.session_state.disable_local = False
    st.session_state.local_nome = ""
    st.session_state.local_descricao = ""
    st.session_state.selected_location = loc
    st.session_state.new_location = True


def find_location(locations, needle):
    for loc in locations:
        if ((abs(needle[0] - loc["lat"]) < 0.0005) and
                (abs(needle[1] - loc["lng"]) < 0.0005)):
            st.session_state.local_nome = loc["nome"]
            st.session_state.local_descricao = loc["descricao"]
            st.session_state.disable_local = True
            st.session_state.selected_marker = [loc["lat"], loc["lng"]]
            break


def location_map():
    state = st.session_state

    st.subheader("Local da sede")
    # Get stored locations
    locations = _get_locations()

    # Create map
    m = create_interactive_map(zoom_start=10, marker_locations=[
                               (loc["lat"], loc["lng"]) for loc in locations], clickable=True)

    # Display map and get click events
    map_data = st_folium(
        m, use_container_width=True, height=400, returned_objects=["last_clicked", "last_object_clicked"])

    loc = list(loc.values()) if (loc := map_data.get("last_object_clicked")) else None
    lc = list(lc.values()) if (lc := map_data.get("last_clicked")) else None
    
    # Check if location changed
    if [*(state.selected_marker or [None]), *(state.selected_point or [None])] != [*(loc or [None]), *(lc or [None])]:
        
        # Handle marker click
        if loc and state.selected_marker != loc:
            find_location(locations, loc)

        # Handle map click
        if lc and state.selected_point != lc:
            state.selected_point = lc
            
        if state.selected_location is None:  # First click
            state.selected_location = state.selected_point or state.selected_marker
        elif state.selected_location == state.selected_point:  # Clicked on marker
            state.selected_location = state.selected_marker
        elif state.selected_location == state.selected_marker:
            reset_form(state.selected_point)

    if state.selected_location is not None:
        st.success(
            f"📌 **Local selecionado**: {state.selected_location[0]:.2f}, {state.selected_location[1]:.2f}")
    else:
        st.info("💡 **Clique no mapa acima para selecionar a localização**")

    st.text_input("Nome do Local (opcional)", key="local_nome",
                  disabled=state.get("disable_local", False))
    st.text_area("Descrição do Local (opcional)",
                 key="local_descricao", disabled=state.get("disable_local", False))

