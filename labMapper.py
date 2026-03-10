#! /usr/bin/env python3
"""
    Author: Samuel Schulthies
    Contributors:
    Last updated: 2026-01-29

    This is a tool in development for using Snipe-IT's API to create an inventory mapping tool.
"""

# import exceptions
import requests
from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
import sys

# # # # # # Constants # # # # # #
BASE_URL = "https://inventory.cs.byu.edu/api/v1"  # Production Snipe-IT Server
FIELDNAMES = ("Asset Tag Number", "Station", "Location")

# def find_asset(asset_tag: str, headers: dict):
#     """
#     Create a map with desired asset highlighted

#     :param headers: HTTP headers for making the API calls
#     :param asset_tag: the asset tag number of the asset you are looking for
#     :return: True if successful
#     """
#     print ("Hello world")
def findAsset():
    assetToStation1138 = {
        "1017521" : 1,
        "1002502" : 2,
        "1017455" : 3,
        "1002512" : 4,
        "1017530" : 5,
        "1017519" : 6,
        "1017535" : 7,
        "1017529" : 8,
        "1002535" : 9,
        "1031634" : 10,
        "1017534" : 11
    }
    assetTag = sys.argv[1]
    station = assetToStation1138[assetTag]
    assetDetails = asset(1138, station, assetTag)

    generateMap(assetDetails)


def generateMap(asset):
    if asset.room == 1138:
        print1138(asset.station)

def print1138(assetStation):
    console = Console()
    preMap = [[10, 9, 8, 7, "  DOOR->"],
             [None, None, None, None, None],
             [None, None, 6, None, 1],
             [None, None, 5, None, 2],
             [11, None, 4, None, 3]]

    print(Panel.fit(buildMap(preMap, assetStation), title="1138", border_style="white"))
 
def renderStation(mapStation, assetStation):
    if mapStation == assetStation:
        return Panel.fit("[blink blue] X ", border_style="white")
    elif mapStation == None:
        return "   "
    elif mapStation == "  DOOR->":
        return mapStation
    return Panel.fit("   ", border_style="white")

def buildMap(preMap, assetStation):
    map = Table.grid(expand=False)
    for _ in range(5):
        map.add_column()
    for row in preMap:
        map.add_row(*(renderStation(mapStation, assetStation) for mapStation in row))

    return map


class asset():
    def __init__(self, room, station, tag):
        self.room = room
        self.station = station
        self.tag = tag

class mapStation():
    def __init__(self, panel, station):
        self.panel = panel
        self.station = station

    def __rich__(self):
        return self.panel

findAsset()
