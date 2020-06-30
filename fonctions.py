#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import dash_table
from dash.dependencies import Output, Input
import plotly.graph_objects as go  
from sqlalchemy import create_engine
import pymysql
import os


engine = create_engine("mysql+pymysql://ines@localhost/SONDAGE")



def create_plot_bar(dataframe):
    trace1 = go.Bar(
                    x = dataframe.index,
                    y = dataframe[("nbre", "Yes")],
                    name = "YES",
                    marker = dict(color = 'rgba(237, 47, 96, 0.5)',
                                line = dict(color ='rgb(0,0,0)',width =1.5)),
                    text = dataframe[('nbre', "Yes")])

    trace2 = go.Bar(
                    x = dataframe.index,
                    y = dataframe[('nbre', "I don't Know")],
                    name = "Not sure",
                    marker = dict(color = 'rgba(255, 174, 255, 0.5)',
                                line = dict(color = 'rgb(0,0,0)',width = 1.5)),
                    text = dataframe[('nbre', "I don't Know")])
    trace3 = go.Bar(
                    x = dataframe.index,
                    y = dataframe[('nbre',"No")],
                    name = "NO",
                    marker = dict(color = 'rgba(251, 240, 28, 0.5)',
                                line = dict(color = 'rgb(0,0,0)',width = 1.5)),
                    text = dataframe[('nbre',"No")])

    data = [trace1, trace2, trace3]
    return dcc.Graph(
                    id="plot5",
                    figure={
                        'data':data,
                        "layout":  go.Layout(#title = "Avez-vous vecu ou observé des conséquences négatives lié aux problèmes de santé mentale sur votre lieu de travail ?",
                            xaxis={'title': 'Pays'},
                            yaxis={'title': 'Valeurs en %'})
                        }
                )

def create_plot_bar2(dataframe):
    return dcc.Graph(
                        id="plot5",
                        figure={
                            'data':[
                                {'x': dataframe.index, 'y': dataframe[('nbre','Yes')], 'type': 'bar', 'name': 'Yes'},
                                {'x': dataframe.index, 'y': dataframe[('nbre', "I don't Know")], 'type': 'bar', 'name': "I don't Know"},
                                {'x': dataframe.index, 'y': dataframe[('nbre', "No")], 'type': 'bar', 'name': 'No'}
                            ] ,
                            "layout": {
                                #'title' : 'Avez-vous vecu ou observé des conséquences négatives lié aux problèmes de santé mentale sur votre lieu de travail?',
                                'xaxis': {'title': 'Pays'},
                                'yaxis': {'title': 'Valeurs en %'},
                                'barmode': 'relative'}
                            }
                    )


def create_plot1(dataframe):
    trace1 = go.Scatter(
                        x = dataframe.index,
                        y = dataframe[('mental_reponse',   'Yes')],
                        mode = "lines",
                        name = "Yes",
                        marker = dict(color = 'rgba(21, 83, 211, 0.8)'),
                        text = dataframe[('mental_reponse',   'Yes')])
    trace2 = go.Scatter(
                        x = dataframe.index,
                        y = dataframe[('mental_reponse', 'Maybe')],
                        mode = "lines",
                        name = "Maybe",
                        marker = dict(color = 'rgba(21, 218, 95, 0.8)'),
                        text = dataframe[('mental_reponse', 'Maybe')])
    trace3 = go.Scatter(
                        x = dataframe.index,
                        y = dataframe[('mental_reponse', 'No')],
                        mode = "lines",
                        name = "No",
                        marker = dict(color = 'rgba(233, 47, 25, 0.8)'),
                        text = dataframe[('mental_reponse', 'No')])

    data = [trace1, trace2, trace3]
    return dcc.Graph(
                        id="plot1",
                        figure={
                            'data':data,
                            "layout": go.Layout(title = "Lors d'un entretien souhaitez vous parler d'un problème de santé Mentale",
                                xaxis={'title': 'Années'},
                                yaxis={'title': 'Valeurs en %'}
                                )
                        }
                    )

def create_plot2(dataframe):
    trace1 = go.Scatter(
                        x = dataframe.index,
                        y = dataframe[('physique_reponse',   'Yes')],
                        mode = "lines",
                        name = "Yes",
                        marker = dict(color = 'rgba(21, 83, 211, 0.8)'),
                        text = dataframe[('physique_reponse',   'Yes')])
    trace2 = go.Scatter(
                        x = dataframe.index,
                        y = dataframe[('physique_reponse', 'Maybe')],
                        mode = "lines",
                        name = "Maybe",
                        marker = dict(color = 'rgba(21, 218, 95, 0.8)'),
                        text = dataframe[('physique_reponse', 'Maybe')])
    trace3 = go.Scatter(
                        x = dataframe.index,
                        y = dataframe[('physique_reponse', 'No')],
                        mode = "lines",
                        name = "No",
                        marker = dict(color = 'rgba(233, 47, 25, 0.8)'),
                        text = dataframe[('physique_reponse', 'No')])

    data = [trace1, trace2, trace3]
    return dcc.Graph(
                id="plot1",
                figure={
                    'data':data,
                    "layout": go.Layout(title = "Lors d'un entretien souhaitez vous parler d'un problème de santé Physique",
                        xaxis={'title': 'Années'},
                        yaxis={'title': 'Valeurs en %'})
                    }
            )

def create_plot3(dataframe):
    trace1 = go.Scatter(
                        x = dataframe.index,
                        y = dataframe[('nbre',   'Yes')],
                        mode = "lines",
                        name = "Yes",
                        marker = dict(color = 'rgba(21, 83, 211, 0.8)'),
                        text = dataframe[('nbre',   'Yes')])
    trace2 = go.Scatter(
                        x = dataframe.index,
                        y = dataframe[('nbre', 'Not sure')],
                        mode = "lines",
                        name = "Not sure",
                        marker = dict(color = 'rgba(21, 218, 95, 0.8)'),
                        text = dataframe[('nbre', "Not sure")])
    trace3 = go.Scatter(
                        x = dataframe.index,
                        y = dataframe[('nbre', 'No')],
                        mode = "lines",
                        name = "No",
                        marker = dict(color = 'rgba(233, 47, 25, 0.8)'),
                        text = dataframe[('nbre', 'No')])

    data = [trace1, trace2, trace3]
    return dcc.Graph(
                    id="plot4",
                    figure={
                        'data':data,
                        "layout":  go.Layout(title = "Connaissez-vous les options de soins de santé mentale disponibles dans le cadre de votre couverture maladie fournie par l'employeur?",
                            xaxis={'title': 'Années'},
                            yaxis={'title': 'Valeurs en %'})
                        }
                )

def create_plot(dataframe):
    trace1 = go.Scatter(
                        x = dataframe.index,
                        y = dataframe[('nbre',   'Yes')],
                        mode = "lines",
                        name = "Yes",
                        marker = dict(color = 'rgba(21, 83, 211, 0.8)'),
                        text = dataframe.index)
    trace2 = go.Scatter(
                        x = dataframe.index,
                        y = dataframe[('nbre', "I don't Know")],
                        mode = "lines",
                        name = "I Don't Know",
                        marker = dict(color = 'rgba(21, 218, 95, 0.8)'),
                        text = dataframe.index)
    trace3 = go.Scatter(
                        x = dataframe.index,
                        y = dataframe[('nbre', 'No')],
                        mode = "lines",
                        name = "No",
                        marker = dict(color = 'rgba(233, 47, 25, 0.8)'),
                        text = dataframe.index)

    data = [trace1, trace2, trace3]
    return  dcc.Graph( 
        id="plot",
        figure={
            'data':data,
            'layout': go.Layout(#title = "Votre employeur a-t-il discuté officiellement de la santé mentale dans le cadre d'un programme de bien-être des employés?",
                                xaxis={'title': 'Années'},
                                yaxis={'title': 'Valeurs en %'})
                    }
                )