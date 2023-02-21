"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.
"""
import csv
import json

from models import CloseApproach, NearEarthObject


def load_neos(neo_csv_path: str) -> list[NearEarthObject]:
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A list of `NearEarthObject`s.
    """
    data_to_return = []
    with open(neo_csv_path, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            info = {
                "name": row["name"],
                "diameter": row["diameter"],
                "hazardous": row["pha"],
            }
            neo = NearEarthObject(row["pdes"], **info)
            data_to_return.append(neo)
    return data_to_return


def load_approaches(cad_json_path: str) -> list[CloseApproach]:
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A list of `CloseApproach`es.
    """
    data_to_return = []
    with open(cad_json_path, "r") as jsonfile:
        reader = json.load(jsonfile)
        for row in reader["data"]:
            cad = CloseApproach(row[0], row[3], row[4], row[7])
            data_to_return.append(cad)
    return data_to_return
