#spoofs test data and inserts into database

import pandas as pd
import gpxpy
import gpxpy.gpx

trail_name = 'notg'

def gpx_to_pandas(gpx_file_path):
    """Takes a gpx filepath, parses files with gpxpy into pandas dataframe of lat,lon,elev.

    Args:
        gpx_file_path (string): Filepath to gpx file

    Returns:
        gpx_df (Pandas DataFrame): Pandas DataFrame with the columns: [lat,lon,elev]
    """

    lat_list = []
    lon_list = []
    elev_list = []
    gpx_file = open(gpx_file_path,'r')
    gpx = gpxpy.parse(gpx_file)
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                lat_list.append(point.latitude)
                lon_list.append(point.longitude)
                elev_list.append(point.elevation)
    gpx_df = pd.DataFrame({'lat':lat_list, 'lon':lon_list,'elev':elev_list})
    return gpx_df

def build_trail_meta(trail_name):
    df = pd.DataFrame({'trail_ID':[''],'trail_name':["""{}""".format(trail_name)]})
    return df


"""pd.read_csv("../data_folder/data.csv")"""

def grab_trail_traj(trail_name):
    trail_traj_path  = """../gpx/{trail_name}.gpx""".format(trail_name=trail_name)
    df = gpx_to_pandas(trail_traj_path)
    return df

dftm = build_trail_meta(trail_name)
dftraj = grab_trail_traj(trail_name)


gpx_file_path = '../gpx/notg.gpx'
gpx_file = open(gpx_file_path,'r')
gpx = gpxpy.parse(gpx_file)
