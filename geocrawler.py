# import modules
import json
import sys
from pathlib import Path


def add_filepath(file, path):
    """add absolute path of each file to files's properties"""
    file['properties']['filepath'] = str(path)


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
                                add_filepath(feat, filepath)
                                points_geojson.append(feat)
                            elif feat['geometry']['type'] == 'LineString':
                                add_filepath(feat, filepath)
                                lines_geojson.append(feat)
                            elif feat['geometry']['type'] == 'Polygon':
                                add_filepath(feat, filepath)
                                polygons_geojson.append(feat)
                            else:
                                continue
            # exceptions
                    except json.JSONDecodeError:
                        print('Invalid JSON format: ', filepath)
            except PermissionError:
                print('Not adequate access rights: ', filepath)
            except Exception:
                print('Unknown error: ', filepath)
    try:
        # export files to geojson format to geometry
        gj_structure_points = {'type': 'FeatureCollection', 'features': points_geojson}
        with open("points.geojson", "w", encoding="utf-8") as outfile1:
            json.dump(gj_structure_points, outfile1, indent=2, ensure_ascii=False)

        gj_structure_lines = {'type': 'FeatureCollection', 'features': lines_geojson}
        with open("lines.geojson", "w", encoding="utf-8") as outfile2:
            json.dump(gj_structure_lines, outfile2, indent=2, ensure_ascii=False)

        gj_structure_polygons = {'type': 'FeatureCollection', 'features': polygons_geojson}
        with open("polygons.geojson", "w", encoding="utf-8") as outfile3:
            json.dump(gj_structure_polygons, outfile3, indent=2, ensure_ascii=False)
    # exceptions
    except PermissionError:
        print('Not permission to write in this directory: ', sys.argv[1])
    except Exception:
        print('Unknown error in directory: ', sys.argv[1])


split_gjs_by_geometry()
