import sys
from datetime import datetime
from io import StringIO

import boto3
import pandas as pd
from sqlalchemy import create_engine
import inspect

con_db_ar = create_engine(sys.argv[1])
con_db_fw = create_engine(sys.argv[2])
schema_fw = sys.argv[3]
id_proyecto = sys.argv[4]
bucket = sys.argv[5]
folder_s3 = sys.argv[6]


def get_data_query(query: str, is_fw=False, conexion_ar=con_db_ar, conexion_fw=con_db_fw):
    """
    Consulta de un select sobre una base de datos

    Parameters:
        query(str): Texto con el select a realizar
        is_fw(boolean): Si debe ejecutarse en las tablas del FW o en RedShift
        conexion_redshift: Conexion a RedShift
        conexion_fw: Conexion al framework

    Returns:
        _(DataFrame): Devuelve el DataFrame de respuesta a la consulta
    """
    if is_fw:
        conexion = conexion_fw
    else:
        conexion = conexion_ar

    return pd.read_sql(query, conexion)
