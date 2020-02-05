import json, os, sys
from pathlib import Path


def add_filepath(file):
    """add absolute path of each file to files's properties"""
    file['features']['properties']['filepath'] = os.path.abspath(file)


def split_gjs_by_geometry():
    """open geojson and json files and merge all point/linestirng/polygon features into separate geojsons"""

    points_geojson = []
    lines_geojson = []
    polygons_geojson = []

    extensions = ['*.geojson', '*.json']

    for e in extensions:
        for filepath in Path(sys.argv[1]).rglob(e):
            try:
                # noinspection PyTypeChecker
                with open(filepath, 'r+', encoding='utf-8') as f:
                    try:
                        print(filepath)
                        data = json.load(f)
                        for feat in data['features']:
                            if feat['geometry']['type'] == 'Point':
                                feat['filepath'] = str(filepath)
                                points_geojson.append(feat)
                            elif feat['geometry']['type'] == 'LineString':
                                feat['filepath'] = str(filepath)
                                lines_geojson.append(feat)
                            elif feat['geometry']['type'] == 'Polygon':
                                feat['filepath'] = str(filepath)
                                polygons_geojson.append(feat)
                            else:
                                pass
                    except json.JSONDecodeError:
                        print('Invalid JSON format: ', filepath)
            except PermissionError:
                print('Invalid JSON format: ', filepath)

    with open("points.geojson", "w", encoding="utf-8") as outfile1:
        json.dump(points_geojson, outfile1, indent=2, ensure_ascii=False)

    with open("lines.geojson", "w", encoding="utf-8") as outfile2:
        json.dump(lines_geojson, outfile2, indent=2, ensure_ascii=False)

    with open("polygons.geojson", "w", encoding="utf-8") as outfile3:
        json.dump(polygons_geojson, outfile3, indent=2, ensure_ascii=False)


split_gjs_by_geometry()
