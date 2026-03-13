#! /usr/bin/env pythonj
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
    assetToStation1130 = {
        "1031635" : 1,
        "1017524" : 2,
        "1017452" : 3,
        "1017461" : 4,
        "1017449" : 5,
        "1017463" : 6,
        "1017443" : 7,
        "1017533" : 8,
        "1017459" : 9,
        "1017462" : 10,
        "1017454" : 11,
        "1017525" : 12,
        "1017448" : 13,
        "1017446" : 14,
        "1017518" : 15,
        "1017522" : 16,
        "1017520" : 17,
        "1017442" : 18,
        "1017456" : 19,
        "1017451" : 20,
        "1017457" : 21,
        "1017523" : 22,
        "1017453" : 23,
        "1017444" : 24,
        "1017532" : 25,
        "1017528" : 26,
        "1017445" : 27,
        "1017450" : 28,
        "1017447" : 29,
        "1017527" : 30,
        "1017458" : 31
    }
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
    assetToStation1102 = {
        "1002542" : 1,
        "1002541" : 2,
        "1017455" : 3,
        "1002528" : 4,
        "1002536" : 5,
        "1002554" : 6,
        "1002525" : 7,
        "1002555" : 8,
        "1002526" : 9,
        "1002532" : 10,
        "1002537" : 11,
        "1002527" : 12,
        "1002533" : 13
    }
    assetToStation1029 = {
        "293788" : 1,
        "293789" : 2,
        "293787" : 3,
        "293786" : 4,
        "293792" : 5,
        "293793" : 6,
        "293790" : 7,
        "293791" : 8,
        "293795" : 9,
        "293798" : 10,
        "293799" : 11,
        "293794" : 12,
        "293796" : 13,
        "293797" : 14,
        "293807" : 15,
        "293806" : 16,
        "293801" : 17,
        "293800" : 18,
        "293802" : 19,
        "293803" : 20,
        "293804" : 21,
        "293805" : 22,
        "293808" : 23,
        "293809" : 24,
        "293813" : 25,
        "293812" : 26,
        "1017526" : 27,
        "293810" : 28
    }
    rooms = {
        1130 : assetToStation1130,
        1138 : assetToStation1138, 
        1102 : assetToStation1102, 
        1029 : assetToStation1029
    } 
    assetTag = sys.argv[1]
    station = 0
    room = 0
    for roomNum, roomToStation in rooms.items():
        if assetTag in roomToStation:
            station = roomToStation[assetTag]
            room = roomNum 
            break
    assetDetails = asset(room, station, assetTag)

    generateMap(assetDetails)


def generateMap(asset):
    if asset.room == 1130:
        print1130(asset.station)
    if asset.room == 1138:
        print1138(asset.station)
    if asset.room == 1102:
        print1102(asset.station)
    if asset.room == 1029:
        print1029(asset.station)



def print1130(assetStation):
    preMap = [[26, 27, None, 30, 31],
             [24, 25, None, 28, 29],
             [None, None, None, None, None],
             [20, 21, None, 22, 23],
             [18, 19, None, None, "  DOOR->"],
             [None, None, None, None, None],
             [13, 14, None, 17, None],
             [11, 12, None, 15, 16],
             [None, None, None, None, None],
             [5, 6, None, 9, 10],
             [3, 4, None, 7, 8],
             [None, None, None, None, None],
             [1, None, None, None, 2]]

    print(Panel.fit(buildMap(preMap, assetStation), title="1130", border_style="white"))

def print1138(assetStation):
    preMap = [[10, 9, 8, 7, "  DOOR->"],
             [None, None, None, None, None],
             [None, None, 6, None, 1],
             [None, None, 5, None, 2],
             [11, None, 4, None, 3]]

    print(Panel.fit(buildMap(preMap, assetStation), title="1138", border_style="white"))

def print1102(assetStation):
    preMap = [["DOOR ^", None, None, 13, None, 12],
             [None, None, None, None, None, None],
             [1, None, 5, 6, None, 11],
             [2, None, None, 7, None, 10],
             [3, None, 4, 8, None, 9]]

    print(Panel.fit(buildMap(preMap, assetStation), title="1102", border_style="white"))

def print1029(assetStation):
    preMap = [[1, 2, None, 3, 4],
             [None, None, None, None, None],
             [5, 6, None, 7, 8],
             [None, None, None, None, None],
             [9, 10, None, 11, 12],
             [None, None, None, None, None],
             ["<-DOOR  ", None, None, 13, 14],
             [None, None, None, None, None],
             [None, None, None, 17, 18],
             [None, None, None, None, None],
             [15, 16, None, 19, 20],
             [None, None, None, None, None],
             [21, 22, None, 23, 24],
             [None, None, None, None, None],
             [25, 26, None, 27, 28]]

    print(Panel.fit(buildMap(preMap, assetStation), title="1029", border_style="white"))
 
 
 
 
def renderStation(mapStation, assetStation):
    if mapStation == assetStation:
        return Panel.fit("[blink blue] X ", border_style="white")
    elif mapStation == None:
        return "   "
    elif mapStation == "  DOOR->" or mapStation == "<-DOOR  " or mapStation == "DOOR ^":
        return mapStation
    return Panel.fit("   ", border_style="white")

def buildMap(preMap, assetStation):
    map = Table.grid(expand=False)
    for _ in range(len(preMap[0])):
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
