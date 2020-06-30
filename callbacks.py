#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from dash.dependencies import Input, Output
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

from app import app

@app.callback(
    Output('id1', 'children'),
    [Input('plot1', 'value')])

def display_value(value):
    return 'You have selected "{}"'.format(value)

@app.callback(
    Output('id2', 'children'),
    [Input('plot', 'value')])

def display_value(value):
    return 'You have selected "{}"'.format(value)

@app.callback(
    Output('id3', 'children'),
    [Input('plot', 'value')])

def display_value(value):
    return 'You have display"{}"'.format(value)

@app.callback(
    Output('id4', 'children'),
    [Input('plot4', 'value')])

def display_value(value):
    return 'You have display"{}"'.format(value)

@app.callback(
    Output('id5', 'children'),
    [Input('plot5', 'value')])

def display_value(value):
    return 'You have display"{}"'.format(value)