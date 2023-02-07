import requests
import folium
import webbrowser
from folium.plugins import TagFilterButton
from folium.features import DivIcon
import json
import natural_event_tracker.constants
import importlib.resources


def get_references():
    """Get references from json file"""
    with importlib.resources.open_text('natural_event_tracker', 'reference.json') as file_handle:
        file_contents = file_handle.read()
        reference = json.loads(file_contents)
        return reference


def get_events():
    """Get list of Event objects from nasa eonet api"""
    events = requests.get(get_references()['find_open']).json()
    return [Event(event_data) for event_data in events['events']]


def get_all_possible_event_categories():
    """Get list of all possible event categories from eonet api"""
    categories = requests.get(get_references()['find_categories']).json()
    return [element["id"] for element in categories["categories"]]


class Event:
    def __init__(self, data):
        """
        Event constructor:
        :data: list of dictionaries imported from nasa eonet API
        """
        self._data = data

    def info(self):
        """Get event description"""
        return self._data['title']

    def category_id(self):
        """Get event category id"""
        return self._data['categories'][0]['id']

    def category_title(self):
        """Get event category title"""
        return self._data['categories'][0]['title']

    def pos(self):
        """Get event latitude and longitude"""
        lon = self._data['geometry'][0]['coordinates'][0]
        lat = self._data['geometry'][0]['coordinates'][1]
        return [float(lat), float(lon)]

    @property
    def data(self):
        """
        Data getter:
        get event data"""
        return self._data

    def __str__(self):
        """Get info about event"""
        return self.info()


class Map:
    def __init__(self, name: str = None):
        """
        Map constructor:
        :name: map name, default name=map
        """
        self._name = "map" if name is None else str(name)
        self._center = natural_event_tracker.constants.CENTER
        self._zoom = natural_event_tracker.constants.ZOOM

    @property
    def name(self):
        """
        Name getter:
        get map name
        """
        return self._name

    def create_map(self):
        """Create default map"""
        return folium.Map(location=self._center,
                          zoom_start=self._zoom,
                          API_key=get_references()['api_key'])

    def show_map(self):
        """Show map in browser"""
        webbrowser.open(f"{self._name}.html")

    def create_full_map_and_save(self):
        """Add markers and filtring to map and save it to a file"""
        return self.add_markers_and_filtring().save(f'{self._name}.html')

    def add_markers_and_filtring(self):
        """Add markers to map and filtring possibility by
        event category title"""
        map = self.create_map()
        categories = []
        info_location = natural_event_tracker.constants.INFO_LOCATION
        info_icon_size = natural_event_tracker.constants.INFO_ICON_SIZE
        info_icon_anchor = natural_event_tracker.constants.INFO_ICON_ANCHOR
        for event in get_events():
            categories.append(event.category_title())
            folium.Marker(
                location=event.pos(),
                popup=event.info(),
                tags=[event.category_title()]
            ).add_to(map)
        folium.Marker(
            location=info_location,
            icon=DivIcon(
                icon_size=info_icon_size,
                icon_anchor=info_icon_anchor,
                html='<div style="font-size: 20pt">'
                + 'All current natural events</div>',
                )
        ).add_to(map)
        TagFilterButton(list(set(categories))).add_to(map)
        return map
