#spoofs test data and inserts into database

import pandas as pd
import gpxpy
import gpxpy.gpx
import glob
import os
from trailsporks.insert import connection as cnxn


def grab_trail_names_from_gpx_dir():
    trail_names_list = pd.Series([os.path.basename(x) for x in glob.glob("../gpx/*")]).str.split(".",expand=True)[0].to_list()
    return trail_names_list 

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

def grab_trail_ID(trail_name):
    """returns trail ID for input trail_name"""
    trail_id = cnxn.pandas_read_sql("""SELECT * FROM tblTrails WHERE trail_name = '{trail_name}'""".format(trail_name=trail_name)).reset_index()["index"][0]
    return trail_id


def build_trail_meta(trail_name):
    df = pd.DataFrame({'trail_name':["""{}""".format(trail_name)]})
    return df

def grab_trail_traj(trail_name):
    trail_traj_path  = """../gpx/{trail_name}.gpx""".format(trail_name=trail_name)
    df = gpx_to_pandas(trail_traj_path)
    return df

for trail in grab_trail_names_from_gpx_dir():
    print(trail)
    dftm = build_trail_meta(trail)
    cnxn.pandas_to_postgres(dftm, 'tbltrails')

    dftraj = grab_trail_traj(trail)
    dftraj.insert(0,'trail_id',grab_trail_ID(trail))

    cnxn.pandas_to_postgres(dftraj, 'tbltrail_trajectory')
