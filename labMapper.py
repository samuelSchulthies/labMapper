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

# # # # # # Constants # # # # # #
BASE_URL = "https://inventory.cs.byu.edu/api/v1"  # Production Snipe-IT Server
FIELDNAMES = ("Asset Tag Number", "Station", "Location")

def find_asset(asset_tag: str, headers: dict):
    """
    Create a map with desired asset highlighted

    :param headers: HTTP headers for making the API calls
    :param asset_tag: the asset tag number of the asset you are looking for
    :return: True if successful
    """
    print ("Hello world")

def generateMap(asset):
    if asset.room == "1139":
        print1138(asset.station)

def print1138(station):
    map = Table.grid(expand=False)
    map.add_column()
    map.add_column()
    map.add_column()
    map.add_column()
    map.add_column()
    map.add_row(
        Panel.fit("   ", border_style="white"),
        Panel.fit("   ", border_style="white"),
        Panel.fit("   ", border_style="white"),
        Panel.fit("   ", border_style="white"),
        "  DOOR->"
    )
    map.add_row(
        "   ",
        "   ",
        "   ",
        "   "
    )
    map.add_row(
        "   ",
        "   ",
        Panel.fit("   ", border_style="white"),
        "   ",
        Panel.fit("   ", border_style="white")
    )
    map.add_row(
        "   ",
        "   ",
        Panel.fit("[blink blue] X ", border_style="white"),
        "   ",
        Panel.fit("   ", border_style="white")
    )
 
    map.add_row(
        Panel.fit("   ", border_style="white"),
        "   ",
        Panel.fit("   ", border_style="white"),
        "   ",
        Panel.fit("   ", border_style="white")
    )


    print(Panel.fit(map, title="1138", border_style="white"))
 


def printStation(assetStation, mapStation):
    if assetStation == mapStation:
        print(Panel.fit("[blink blue] X ", border_style="white"))
    else:
        print(Panel.fit("[]   ", border_style="white"))
 


class asset():
    def __init__(self, room, station, tag):
        self.room = room
        self.station = station
        self.tag = tag


print1138(1)
