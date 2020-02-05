# import modules
import json
import os
import sys
from pathlib import Path


def add_filepath(file):
    """add absolute path of each file to files's properties"""
    file['filepath'] = os.path.abspath(str(file))


def split_gjs_by_geometry():
    """open geojson and json files and merge all point/linestirng/polygon features into separate geojsons"""

    # empty output lists
    points_geojson = []
    lines_geojson = []
    polygons_geojson = []

    # select extensions being browsed
    extensions = ['*.geojson', '*.json']

    for e in extensions:
        # directory gained from command line
        for filepath in Path(sys.argv[1]).rglob(e):
            try:
                # noinspection PyTypeChecker
                with open(filepath, 'r+', encoding='utf-8') as f:
                    try:
                        # print file being browsed
                        print(filepath)
                        data = json.load(f)
                        for feat in data['features']:
                            # select file by geometry
                            if feat['geometry']['type'] == 'Point':
                                add_filepath(feat)
                                points_geojson.append(feat)
                            elif feat['geometry']['type'] == 'LineString':
                                add_filepath(feat)
                                lines_geojson.append(feat)
                            elif feat['geometry']['type'] == 'Polygon':
                                add_filepath(feat)
                                polygons_geojson.append(feat)
                            else:
                                continue
                    except json.JSONDecodeError:
                        print('Invalid JSON format: ', filepath)
            except PermissionError:
                print('Not adequate access rights: ', filepath)

    with open("points.geojson", "w", encoding="utf-8") as outfile1:
        json.dump(points_geojson, outfile1, indent=2, ensure_ascii=False)

    with open("lines.geojson", "w", encoding="utf-8") as outfile2:
        json.dump(lines_geojson, outfile2, indent=2, ensure_ascii=False)

    with open("polygons.geojson", "w", encoding="utf-8") as outfile3:
        json.dump(polygons_geojson, outfile3, indent=2, ensure_ascii=False)


split_gjs_by_geometry()
