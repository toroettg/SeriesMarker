#!/usr/bin/python

#==============================================================================
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 - 2016 Tobias Röttger <toroettg@gmail.com>
#
# This file is part of SeriesMarker.
#
# SeriesMarker is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# SeriesMarker is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SeriesMarker.  If not, see <http://www.gnu.org/licenses/>.
#==============================================================================

from pytvdbapi import api
import datetime
from abc import ABCMeta

def fetch_series_data(series):
    print("attributes = {")

    for key in dir(series):
        value = getattr(series, key)

        if key in ["seasons", "actor_objects"]:
            print("   #'{}' : ignored".format(key))
            continue
#        elif key == "Overview":
#            value = value.replace("\n", "")
#            value = value.encode("unicode_escape")
        elif key in ["api", "banner_objects", "lang", "language"]:
            continue

        if type(value) is str:
            value = "'{}'".format(value)
        elif type(value) is datetime.date:
            value = "date({y}, {m}, {d})".format(y=value.year, m=value.month, d=value.day)

        print("    '{key}': {value},".format(key=key, value=value))

    print("}")

def fetch_episode_data(series):
    season_number = int(input("Enter season number: "))
    episode_number = int(input("Enter episode number: "))

    episode = series[season_number][episode_number]

    print("attributes = {")

    for key in dir(episode):
        value = getattr(episode, key)

        if key == "season":
            print("   #'season' : ignored")
            continue
        elif key == "Overview":
            value = value.replace("\n", "")
            value = value.replace("'", "\\'")

        if type(value) is str:
            value = "'{}'".format(value)
        elif type(value) is datetime.date:
            value = "date({y}, {m}, {d})".format(y=value.year, m=value.month, d=value.day)

        print("    '{key}': {value},".format(key=key, value=value))

    print("}")

def fetch_banner_data(series):
    for banner in series.banner_objects:
        print("attributes = {")

        for key in dir(banner):
            value = getattr(banner, key)

            if type(value) is str:
                value = "'{}'".format(value)

            print("    '{key}': {value},".format(key=key, value=value))

        print("}")

        print("\n\n")

def fetch_role_data(series):
    for role in series.actor_objects:
        print("attributes = {")

        for key in dir(role):
            value = getattr(role, key)

            if type(value) is str:
                value = "'{}'".format(value)

            print("    '{key}': {value},".format(key=key, value=value))

        print("}")

        print("\n\n")

def fetch_data(db):
    input_id = None

    if input_id is None:
        input_id = input("Enter series ID to fetch attributes: ")

    series = db.get(input_id, "en")
    series.update()

    choice = input("Fetch series (1), episode (2), banner (3) or role data (4)?")

    if choice == "1":
        fetch_series_data(series)
    elif choice == "2":
        fetch_episode_data(series)
    elif choice == "3":
        fetch_banner_data(series)
    elif choice == "4":
        fetch_role_data(series)



def scan_attributes(db):
    search = db.search("a", "en")

    show_attributes = {}
    episode_attributes = {}

    for show in search:
        show.update()
        for attribute in dir(show):
            if attribute == "Overview":
                continue

            value = [type(getattr(show, attribute)), str(show), getattr(show, attribute)]

            if attribute not in show_attributes:
                if getattr(show, attribute) == "":
                    show_attributes[attribute] = [[]]
                else:
                    show_attributes[attribute] = value
            elif getattr(show, attribute) != "" and show_attributes[attribute][0] != type(getattr(show, attribute)):
                show_attributes[attribute].append(value)

        for season in show.seasons.values():
            for episode in season.episodes.values():
                for attribute in dir(episode):
                    if attribute == "Overview":
                        continue

                    value = [type(getattr(episode, attribute)), str(episode), getattr(episode, attribute)]


                    if attribute not in episode_attributes:
                        if getattr(episode, attribute) == "":
                            episode_attributes[attribute] = [[]]
                        else:
                            episode_attributes[attribute] = value
                    elif getattr(episode, attribute) != "":
                        entry = episode_attributes[attribute]

                        if entry[0] != type(getattr(episode, attribute)):
                            episode_attributes[attribute].append(value)

    print("##### Show Attributes\n")

    '''    for attribute, typev in show_attributes.items():
        if typev != "":
            print(attribute + " is " + str(typev))
        else:
            print(attribute + " not found")'''


    print("##### Episode Attributes\n")

    for attribute, typev in episode_attributes.items():
        if typev != "":
            print(attribute + " is " + str(typev))
        else:
            print(attribute + " not found")

    print()
    print()
    print("##### DEBUG Attributes\n")

    for attribute, typev in episode_attributes.items():
        if typev != "":
            types = []

            if type(typev[0]) in [type, ABCMeta]:
                types.append(str(typev[0]))
            else:
                for dire in typev:
                    if len(dire) != 0 and str(dire[0]) not in types:
                        types.append(str(dire[0]))

            print("{} is {}".format(attribute, types))



def main():
    db = api.TVDB("B43FF87DE395DF56", banners=True, actors=True)  # TODO use own api-key

    choice = input("Fetch data (1) or scan attribute types (2)? ")

    if choice == "1":
        fetch_data(db)
    elif choice == "2":
        scan_attributes(db)




if __name__ == '__main__':
    main()
