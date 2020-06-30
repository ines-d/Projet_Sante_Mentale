#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import dash_table
from dash.dependencies import Output, Input
import plotly.graph_objects as go  
from sqlalchemy import create_engine
import pymysql
from urllib.parse import quote
from query import query1, query2, query3, query4, query5, query6, query7
from fonctions import create_plot_bar, create_plot_bar2, create_plot, create_plot1, create_plot2, create_plot3
import os


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']




app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.config.suppress_callback_exceptions = True