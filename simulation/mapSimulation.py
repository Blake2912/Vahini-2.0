import re
import time
import ipyleaflet as ipl
from ipyleaflet import Map, Circle, Marker, AwesomeIcon, Polyline
import osmnx as ox
import networkx as nx

class InteractiveMap:
    def __init__(self, center, zoom=18):
        self.center = center
        self.zoom = zoom
        self.maps = ipl.Map(center=center, basemap=ipl.basemaps.CartoDB.Positron, zoom=self.zoom)
        self.maps.layout.height = '800px'
        self.marker = None

    def add_trees(self, G):
        pattern = r't\-[0-9]+'
        for point_name in list(G.nodes()):
            if re.match(pattern, point_name):
                latitude = G.nodes[point_name]['y']
                longitude = G.nodes[point_name]['x']
                circle = Circle(
                    location=(latitude, longitude),
                    radius=2,
                    color="tomato",
                )
                self.maps.add_layer(circle)

    def add_marker(self, location):
        icon = AwesomeIcon(
            name='fa-truck',
            marker_color='green',
            icon_color='black',
            spin=False
        )
        self.marker = Marker(icon=icon, location=location)
        self.maps.add_layer(self.marker)

    def display_map(self):
        return self.maps

    def traversal(self, G, orig_node, dest_node):
        try: 
          self.maps.remove_layer(lines)
        except:
          pass
        shortest_route = nx.shortest_path(G, orig_node, dest_node, weight='length')
        locations = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in shortest_route]
        lines = Polyline(
            locations=locations,
            color="tomato",
            fill=False
        )
        self.maps.add_layer(lines)

        step = 0.5
        pattern = r't\-[0-9]+'
        for point in shortest_route:
            latitude = G.nodes[point]['y']
            longitude = G.nodes[point]['x']
            self.marker.location = (latitude, longitude)
            if re.match(pattern, point):
                time.sleep(1)
                visited = Circle(
                    location=(latitude, longitude),
                    radius=2,
                    color="#00b521",
                    fill_color="#7fff96",
                    fill=True,
                    fill_opacity=0.85
                )
                self.maps.add_layer(visited)
            time.sleep(step)

    def battery_check(self, G, current_vehicle_location, base_location, range):
          shortest_route = nx.shortest_path(G, current_vehicle_location, base_location, weight='length')
          route_coords = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in shortest_route]

          total_distance = sum(ox.distance.great_circle_vec(lat1, lng1, lat2, lng2) for (lat1, lng1), (lat2, lng2) in zip(route_coords[:-1], route_coords[1:]))

          if range >= total_distance:
            step = 1.5
            self.marker.location = route_coords[0]
            self.marker.color = "red"

            shortest_path = Polyline(
                locations=route_coords,
                color="tomato",
                fill=False
            )
            self.maps.add_layer(shortest_path)
            for point in route_coords:
                self.marker.location = point
                time.sleep(step)
          else:
            print("Vehicle cannot move with the given battery level range")

    def water_check(self, G, current_vehicle_location, base_location, water_level, water_threshold):
        shortest_route = nx.shortest_path(G, current_vehicle_location, base_location, weight='length')
        route_coords = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in shortest_route]

        if water_level <= water_threshold:
            step = 1.5
            self.marker.location = route_coords[0]
            self.marker.color = "yellow"

            shortest_path = Polyline(
                locations=route_coords,
                color="blue",
                fill=False
            )
            self.maps.add_layer(shortest_path)
            for point in route_coords:
                self.marker.location = point
                time.sleep(step)
        else:
            print("Vehicle can continue with the given water level")