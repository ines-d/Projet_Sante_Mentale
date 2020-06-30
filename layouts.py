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
from urllib.parse import quote
from query import query1, query2, query3, query4, query5, query6, query7
from fonctions import create_plot_bar, create_plot_bar2, create_plot, create_plot1, create_plot2, create_plot3
import os


engine = create_engine("mysql+pymysql://ines@localhost/SONDAGE")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


colors = {
    'background': '#EEB1E6',
    'text': '#111111'
}

# lors d'un entretien

# j'ai separé les 2 requetes pour avoir 2 dataframes afin defaire le pourcentage"%" sur les bonnes valeurs(par annee, reponse)
data1 = pd.read_sql_query(query1, engine)
data2 = pd.read_sql_query(query2, engine)
dff = pd.concat([data1,data2], axis=1)



question1 = data1.groupby(['annee', 'question1']).agg({'mental_reponse': 'sum'}) 
annee1 = data1.groupby(['annee']).agg({'mental_reponse': 'sum'}) 
df1 = question1.div(annee1, level='annee') * 100 
df1 = df1.pivot_table(index=['annee'],columns=['question1'],values=['mental_reponse'])

question2 = data2.groupby(['annee', 'question2']).agg({'physique_reponse': 'sum'}) 
annee2 = data2.groupby(['annee']).agg({'physique_reponse': 'sum'}) 
df2 = question2.div(annee2, level='annee') * 100 
df2 = df2.pivot_table(index=['annee'],columns=['question2'],values=['physique_reponse'])
df = pd.concat([df1,df2])


# Votre employeur a-t-il déjà discuté de la santé mentale
dff1 = pd.read_sql_query(query3, engine)
question = dff1.groupby(['annee', 'reponse']).agg({'nbre': 'sum'}) 
annee = dff1.groupby(['annee']).agg({'nbre': 'sum'}) 
df1 = question.div(annee, level='annee') * 100 
df1 = df1.pivot_table(index=['annee'],columns=['reponse'],values=['nbre'])


# les prestation de santé mentale offertes par l'employeur.

dff2 = pd.read_sql_query(query4, engine)
question = dff2.groupby(['annee', 'reponse']).agg({'nbre': 'sum'}) 
annee = dff2.groupby(['annee']).agg({'nbre': 'sum'}) 
df2 = question.div(annee, level='annee') * 100 
df2 = df2.pivot_table(index=['annee'],columns=['reponse'],values=['nbre'])

# Option de prestation

dff3 = pd.read_sql_query(query5, engine)
question = dff3.groupby(['annee', 'reponse']).agg({'nbre': 'sum'}) 
annee = dff3.groupby(['annee']).agg({'nbre': 'sum'}) 
df3 = question.div(annee, level='annee') * 100 
df3 = df3.pivot_table(index=['annee'],columns=['reponse'],values=['nbre'])


#Anonymat

dff4 = pd.read_sql_query(query6, engine)

question = dff4.groupby(['annee', 'reponse']).agg({'nbre': 'sum'}) 
annee = dff4.groupby(['annee']).agg({'nbre': 'sum'}) 
df4 = question.div(annee, level='annee') * 100 
df4 = df4.pivot_table(index=['annee'],columns=['reponse'],values=['nbre'])

question = dff4.groupby(['country', 'reponse']).agg({'nbre': 'sum'}) 
country = dff4.groupby(['country']).agg({'nbre': 'sum'}) 
df5 = question.div(country, level='country') * 100 
df5 = df5.pivot_table(index=['country'],columns=['reponse'],values=['nbre'])



# Experience
dff6 = pd.read_sql_query(query7, engine)
question = dff6.groupby(['annee', 'reponse']).agg({'nbre': 'sum'}) 
annee = dff6.groupby(['annee']).agg({'nbre': 'sum'}) 
df6 = question.div(annee, level='annee') * 100 
df6 = df6.pivot_table(index=['annee'],columns=['reponse'],values=['nbre'])


text = """
Le sujet du projet touche à la santé mentale au travail et plus précisément dans le secteur du numérique, il repose sur un sondage réalisé chaque année de 2014 à 2019.   
Ce projet a pour but de montrer l’évolution des mentalités par rapport à la santé mentale au travail en essayant d'étudier plusieurs questions.  
    - **Question 1** : Lors d’un entretien souhaitez-vous parler d’un problème de santé mentale ou santé physique ?.  
    - **Question 2** : Votre employeur a-t-il discuter officiellement de la santé mentale dans le cadre d’un programme de bien être des employés ?.  
    - **Question 3** :  Votre employeur offre-t-il des prestations de santé mentale ?.  
    - **Question 4** : Connaissez-vous les options de soins de santé mentale disponibles dans le cadre de votre couverture maladie fournie par l’employeur ?.  
    - **Question 5** : L’anonymat est-t-il respecté ?.  
    - **Question 6** : Avez-vous vécu ou observé des conséquences négatives liés aux problèmes de santé mentale sur votre lieu de travail ?.

"""
def Header():
    return html.Div([
        get_logo(),
        get_header(),
        html.Br([]),
        get_menu()
    ])

def get_logo():
    logo = html.Div([
        html.Div([
            html.Img(src='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTBzhp1ApNsKaG7vICEpZ4T8L7nCC2jmP6m9RsuIPe4wnYes_t8&usqp=CAU', 
            height='180', 
            width='150')
        ], className="ten columns padded"),
    ], className="row gs-header")
    return logo


def get_header():
    header = html.Div([
        html.Div([
            html.Div(style={'backgroundColor': '#ACDBED'}, children=[
                html.H3(
                children= 'Evolution des mentalilés par rapport à la santé mentale au travail (secteur Numérique).', 
                style={'textAlign': 'center', 'color':'rgba(0,0,7,0.7)', 'border':'3px double black'}#colors['text']}
                )
            ]),
            dcc.Markdown(text, style={'font-size':'18px'})
            #html.H5(children=text)
        ], className="twelve columns padded")
    ], className="row")
    return header


def get_menu():
    menu = html.Div(style={'font-size': '20px', 'background-color':'#EBF0F5', 'textAlign': 'center', 'color':'rgba(0,0,7,0.7)'}, children=[ 

        dcc.Link('              Entretien      |        ', href='/entretien', className='mb-3'),

        dcc.Link('              Discuter de la santé mentale     |          ', href='/discuter', className="mb-3"),

        dcc.Link("              Préstations proposées par l'employeur     |         ", href='/prestation', className="mb-3"),

        dcc.Link('              les Options de Préstations     |        ', href='/OptionPrestation', className="mb-3"),

        dcc.Link("              Respect de l' Anonymat     |        ", href='/Anonymat', className="mb-3"),

        dcc.Link('              Experience Négative     |       ', href='/Experience', className="mb-3")

    ], className="rows")
    return menu


# Generate Table
def generate_table(dataframe):
    return html.Div([   
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in dataframe.columns],
            data=dataframe.to_dict('records'),
            editable=True,
            css=[{'selector': '.dash-cell div.dash-cell-value', 'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'}],
            style_table={'overflowX': 'scroll',
                         'maxHeight': '1000px',
                         'maxWidth': '100%',
                         'overflowY': 'scroll',
                         'maxHeight': '300px',
                         'maxWidth': '1500px',
                         'width': '100%',
                         'Height' : '49%',
                         'display': 'inline-block',
                         'vertical-align': 'middle'},
            style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'center'},
            style_cell_conditional=[
                {
                    'if': {'column_id': c},
                    'textAlign': 'left'
                } for c in ['Date', 'Region']
            ],
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': '#F2A2AB',
                    'color': 'white'
                }
            ],
            style_header={
                'backgroundColor': '#C33544',
                'color' : 'white',
                'fontWeight': 'bold'
            },
        )
    ],className="twelve columns")


layout1 = html.Div([
    Header(),
    html.Div([
        html.H4("Lors d'un entretien souhaitez vous parler d'un problème de Santé Mentale ou Santé Physique ?"),
        html.H6("Tableau des reponses pour la question 1"),
        generate_table(dff),
        # Download Button
            html.Div([
                html.A(html.Button('Download data'),
                    id="download-button",
                    download='Entretien.csv',
                    href="data:text/csv;charset=utf-8,"+quote(dff.to_csv(index=False)),
                    target="_blank"),
                ]), 
        html.Div([
            html.Div([
                html.H5("Santé Mentale"),
                create_plot1(df)
                    
        ], className="six columns"),

        html.Div([
            html.H5("Santé Physique"),
              create_plot2(df)
        ], className="six columns"),

    ],className="row"),

    ]),

    html.Div(id='id1'),
    dcc.Link('Go to App 2', href='/discuter')
])

layout2 = html.Div([
    Header(),
    html.Div([ 
        html.H4("Votre employeur a-t-il discuté officiellement de la santé mentale dans le cadre d'un programme de bien-être des employés ?"),
        html.H6("Tableau des reponses pour la question 2"),
        generate_table(dff1),
        # Download Button
            html.Div([
                html.A(html.Button('Download data'),
                    id="download-button",
                    download='Discuter.csv',
                    href="data:text/csv;charset=utf-8,"+quote(dff1.to_csv(index=False)),
                    target="_blank"),
                ]),
        html.Div([
             html.H5("Votre employeur a-t-il discuté officiellement de la santé mentale dans le cadre d'un programme de bien-être des employés ?"),
               create_plot(df1)
        ], className="nine columns"),

    ]),

    html.Div(id='id2'),
    dcc.Link('Go to App 1', href='/entretien')
])


layout3 = html.Div([
    Header(),
    html.Div([ 
        html.H4("Votre employeur offre-t-il des prestation de santé mentale ?"),
        html.H6("Tableau des reponses pour la question 3"),
        generate_table(dff2),
        # Download Button
            html.Div([
                html.A(html.Button('Download data'),
                    id="download-button",
                    download='Prestation.csv',
                    href="data:text/csv;charset=utf-8,"+quote(dff2.to_csv(index=False)),
                    target="_blank"),
                ]),
        html.Div([
             html.H4("Préstation de Santé Mentale"),
                create_plot(df2)
        ], className="ten columns"),

    ]),

    html.Div(id='id3'),
    dcc.Link('Go to App 2', href='/discuter')
])

layout4 = html.Div([
    Header(),
    html.Div([ 
        html.H4("Connaissez-vous les options de soins de santé mentale disponibles dans le cadre de votre couverture maladie fournie par l'employeur?"),
        html.H6("Tableau des reponses pour la question 4"),
        generate_table(dff3),
        # Download Button
            html.Div([
                html.A(html.Button('Download data'),
                    id="download-button",
                    download='Option_prestation.csv',
                    href="data:text/csv;charset=utf-8,"+quote(dff3.to_csv(index=False)),
                    target="_blank"),
                ]),
        html.Div([
             html.H4("Options de Préstation de Santé Mentale"),
                create_plot3(df3)
        ], className="ten columns"),

    ]),

    html.Div(id='id4'),
    dcc.Link('Go to App 2', href="/Préstation")
])

layout5 = html.Div([
    Header(),
    html.Div([ 
        html.H4("L'Anonymat est-t-il respecté ?"),
        html.H6("Tableau des reponses pour la question 5"),
        generate_table(dff4),
        # Download Button
            html.Div([
                html.A(html.Button('Download data'),
                    id="download-button",
                    download='Anonymat.csv',
                    href="data:text/csv;charset=utf-8,"+quote(dff4.to_csv(index=False)),
                    target="_blank"),
                ]),
        html.Div([
             html.H4("L'Anonymat est-t-il respecté"),
                create_plot(df4)
        ], className="ten columns"),
        html.Div([
            html.H4("L'Anonymat est-t-il respecté"),
                create_plot_bar(df4)
        ], className="ten columns"),

    ]),

    html.Div(id='id5'),
    dcc.Link('Go to App 3', href="/OptionPréstation")
])

layout6 = html.Div([
    Header(),
    html.Div([
        html.H4('Avez-vous vecu ou observé des conséquences négatives lié aux problèmes de santé mentale sur votre lieu de travail ?'),
        html.H6("Tableau des reponses pour la question 6"), 
        generate_table(dff6),
        # Download Button
            html.Div([
                html.A(html.Button('Download data'),
                    id="download-button",
                    download='Experience.csv',
                    href="data:text/csv;charset=utf-8,"+quote(dff6.to_csv(index=False)),
                    target="_blank"),
                ]),
        html.Div([
             html.H5('Avez-vous vécu ou observé une experience négatives ?'),
             create_plot_bar(df6)
                
        ], className="ten columns"),
        html.Div([
            html.H5('Avez-vous vécu ou observé une experience négatives ?'),
                create_plot_bar2(df6)
        ], className="ten columns"),
        html.Div([
            html.H5('Avez-vous vécu ou observé une experience négatives ?'),
            create_plot(df6)
                
        ], className="ten columns"),
    ]),

    html.Div(id='id5'),
    dcc.Link('Go to App 2', href="/Anonymat")
])
