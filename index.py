#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import os
from query import query1, query2, query3, query4, query5, query6, query7
from fonctions import create_plot_bar, create_plot_bar2, create_plot, create_plot1, create_plot2, create_plot3

from app import app
from app import server
from layouts import layout1, layout2, layout3, layout4, layout5, layout6
import callbacks

colors = {
    'background': '#FCFAFC',
    'text': '#111111'
}

app.layout = html.Div(style={'padding': '30px'},children=[
    html.H2(
       # children= 'Evolution des mentalilés par rapport à la santé mentale au travail (secteur Numérique).', style={'textAlign': 'center', 'color':'red'}#colors['text']}
    ),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/' or pathname == '/entretien':
         return layout1
    elif pathname == '/discuter':
        return layout2
    elif pathname == '/prestation':
         return layout3
    elif pathname == "/OptionPrestation":
        return layout4
    elif pathname == "/Anonymat":
        return layout5
    elif pathname == '/Experience':
        return layout6
    else:
        return layout1

if __name__ == '__main__':
    app.run_server(debug=True)
