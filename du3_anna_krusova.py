import glob, json, os, sys


def add_filepath(file):
    """add absolute path of each file to files's properties and print print the directory being browsed"""
    file['features']['properties']['filepath'] = os.path.abspath(file)

    print(os.path.dirname(os.path.abspath(file)))


def split_gjs_by_geometry(direct):
    """open geojson and json files and merge all point/linestirng/polygon features into separate geojsons"""
    points_geojson = []
    lines_geojson = []
    polygons_geojson = []

    for f in glob.glob([direct + '/**/*.geojson', direct + '/**/*.json'], recursive=True):
        with open(f, 'r+', encoding='utf-8') as infile:
            data = json.load(infile)
            try:
                if data['features']['geometry']['type'] == 'Point':
                    add_filepath(data)
                    points_geojson.append(data)
                elif data['features']['geometry']['type'] == 'Linestring':
                    add_filepath(data)
                    lines_geojson.append(data)
                elif data['features']['geometry']['type'] == 'Polygon':
                    add_filepath(data)
                    polygons_geojson.append(data)
                else:
                    print('Invalid GeoJSON'.format(data))
            except ValueError as e:
                print('Invalid GeoJSON:'.format(data), e)

    with open('points.geojson', 'w', encoding='utf-8') as outfile:
        json.dump(points_geojson, outfile, indent=2, ensure_ascii=False)
    with open('lines.geojson', 'w', encoding='utf-8') as outfile:
        json.dump(lines_geojson, outfile, indent=2, ensure_ascii=False)
    with open('polygons.geojson', 'w', encoding='utf-8') as outfile:
        json.dump(polygons_geojson, outfile, indent=2, ensure_ascii=False)


# directory as a command line argument, set to working directory
directory = sys.argv[1]
os.chdir(os.path.abspath(directory))

split_gjs_by_geometry(directory)
