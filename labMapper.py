#! /usr/bin/env python3
"""
    Author: Samuel Schulthies
    Contributors:
    Last updated: 2026-01-29

    This is a tool in development for using Snipe-IT's API to create an inventory mapping tool.
"""

#import exceptions

# # # # # # Constants # # # # # #
BASE_URL = "https://inventory.cs.byu.edu/api/v1"  # Production Snipe-IT Server
BYU_FIELDNAMES = ("Asset Tag Number", "Station")

def find_asset(asset_tag: str, headers: dict):
    """
    Create a map with desired asset highlighted

    :param headers: HTTP headers for making the API calls
    :param asset_tag: the asset tag number of the asset you are looking for
    :return: True if successful
    """
    print ("Hello world")

find_asset("test",{1:1})

