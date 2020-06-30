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





# reponse lors d'un entretien
query1="""select case
    when "" then "2014"
    else "2014"
end as annee
, country
, question_18 as question1
, count(question_18) as mental_reponse from sondage_2014
group by  question_18 
union 
select case
    when "" then "2015"
    else "2015"
end as annee
, country
, question_18
, count(question_18) as mental_reponse from sondage_2015
group by  question_18 
union
select case
    when "" then "2016"
    else "2016"
end as annee
, country
, question_39
, count(question_39) as mental_reponse from sondage_2016
group by  question_39 
union 
select case
    when "" then "2017"
    else "2017"
end as annee
, country
, question_98
, count(question_98) as mental_reponse  from sondage_2017
group by question_98 
union 
select case
    when "" then "2018"
    else "2018"
end as annee
, country
, question_98
, count(question_98) as mental_reponse from sondage_2018
group by question_98 
union
select case
    when "" then "2019"
    else "2019"
end as annee
, country
, question_62
, count(question_62) as mental_reponse from sondage_2019
group by  question_62 """

query2="""select case
    when "" then "2014"
    else "2014"
end as annee
, country
, question_19 as question2
, count(question_19) as physique_reponse from sondage_2014
group by  question_19 
union 
select case
    when "" then "2015"
    else "2015"
end as annee
, country
, question_19
, count(question_19) as physique_reponse from sondage_2015
group by  question_19 
union
select case
    when "" then "2016"
    else "2016"
end as annee
, country
, question_37
, count(question_37) as physique_reponse from sondage_2016
group by question_37
union 
select case
    when "" then "2017"
    else "2017"
end as annee
, country
, question_96
, count(question_96) as physique_reponse from sondage_2017
group by question_96
union 
select case
    when "" then "2018"
    else "2018"
end as annee
, country
, question_96
, count(question_96) as physique_reponse from sondage_2018
group by  question_96
union
select case
    when "" then "2019"
    else "2019"
end as annee
, country
, question_60
, count(question_60) as physique_reponse from sondage_2019
group by   question_60;"""

# Votre employeur a-t-il déjà discuté de la santé mentale
query3 = """select  case
    when year='' then '2014'
    else '2014'
    end as annee
, country
, question_10
, count(question_10)  as nbre
, case 
    when question_10="Don't Know" then "I don't Know" 
    when question_10="No" then "No" 
    when question_10="Yes" then "Yes"
    else "I don't Know"
end as reponse
from sondage_2014  
group by country, question_10
union 
select  case
    when year='' then '2015'
    else '2015'
    end as annee
, country
, question_10
, count(question_10)  as nbre
, case 
    when question_10="Don't Know" then "I don't Know" 
    when question_10="No" then "No" 
    when question_10="Yes" then "Yes"
    else "I don't Know"
end as reponse
 from sondage_2015 
group by country, question_10
union
select  case
    when '' then '2016'
    else '2016'
    end as annee
, country
, question_7
, count(question_7)  as nbre
, case 
    when question_7="Don't Know" then "I don't Know" 
    when question_7="No" then "No" 
    when question_7="Yes" then "Yes"
    else "I don't Know"
end as reponse
from sondage_2016  
group by country, question_7
union
select  case
    when '' then '2017'
    else '2017'
    end as annee
, country
, question_7
, count(question_7)  as nbre
, case 
    when question_7="Don't Know" then "I don't Know" 
    when question_7="No" then "No" 
    when question_7="Yes" then "Yes"
    else "I don't Know"
end as reponse
from sondage_2017  
group by country, question_7
union
select  case
    when '' then '2018'
    else '2018'
    end as annee
, country
, question_7
, count(question_7)  as nbre
, case 
    when question_7="Don't Know" then "I don't Know" 
    when question_7="No" then "No" 
    when question_7="Yes" then "Yes"
    else "I don't Know"
end as reponse
from sondage_2018 
group by country, question_7
union
select  case
    when '' then '2019'
    else '2019'
    end as annee
, country
, question_7
, count(question_7) as nbre 
, case 
    when question_7="Don't Know" then "I don't Know" 
    when question_7="No" then "No" 
    when question_7="Yes" then "Yes"
    else "I don't Know"
end as reponse
from sondage_2019  
group by country, question_7;"""

# requete sur les prestation de santé mentale offertes par l'employeur.
query4 = """
select case
    when "" then "2014"
    else "2014"
end as annee
, country
, question_8
, count(question_8) as nbre
, case 
        when question_8="Don't Know" then "I don't Know" 
        when question_8="No" then "No" 
        when question_8="Yes" then "Yes"
        else "I don't Know"
    end as reponse
from sondage_2014
group by country, reponse
union 
select case
    when "" then "2015"
    else "2015"
end as annee
, country
, question_8
, count(question_8) as nbre 
, case 
        when question_8="Don't Know" then "I don't Know" 
        when question_8="No" then "No" 
        when question_8="Yes" then "Yes"
        else "I don't Know"
    end as reponse
from sondage_2015
group by country, reponse
union
select case
    when "" then "2016"
    else "2016"
end as annee
, country
, question_5
, count(question_5) nbre 
, case 
        when question_5="Don't Know" then "I don't Know" 
        when question_5="No" then "No" 
        when question_5="Yes" then "Yes"
        else "I don't Know"
    end as reponse
from sondage_2016
group by country, reponse
union
select case
    when "" then "2017"
    else "2017"
end as annee
, country
, question_5
, count(question_5) as nbre 
, case 
        when question_5="Don't Know" then "I don't Know" 
        when question_5="No" then "No" 
        when question_5="Yes" then "Yes"
        else "I don't Know"
    end as reponse
from sondage_2017
group by country, reponse
union 
select case
    when "" then "2018"
    else "2018"
end as annee
, country
, question_5
, count(question_5) as nbre 
, case 
        when question_5="Don't Know" then "I don't Know" 
        when question_5="No" then "No" 
        when question_5="Yes" then "Yes" 
        else "I don't Know"
    end as reponse
from sondage_2018 
group by country, reponse
union
select case
    when "" then "2019"
    else "2019"
end as annee
, country
, question_5
, count(question_5) as nbre 
, case 
        when question_5="Don't Know" then "I don't Know" 
        when question_5="No" then "No" 
        when question_5="Yes" then "Yes"  
        else "I don't Know"
    end as reponse
from sondage_2019 
group by country, reponse;"""

# Option de prestation
query5 = """
select case
    when "" then "2014"
    else "2014"
end as annee
, country
, question_9
, count(question_9) as nbre
, case 
        when question_9="Not sure" then "Not sure" 
        when question_9="No" then "No" 
        when question_9="Yes" then "Yes" 
        else "Not sure"
    end as reponse
from sondage_2014
group by country, reponse
union 
select case
    when "" then "2015"
    else "2015"
end as annee
, country
, question_9
, count(question_9) as nbre 
, case 
        when question_9="Not sure" then "Not sure" 
        when question_9="No" then "No" 
        when question_9="Yes" then "Yes" 
        else "Not sure"
    end as reponse
from sondage_2015
group by country, reponse
union
select case
    when "" then "2016"
    else "2016"
end as annee
, country
, question_6
, count(question_6) nbre 
, case 
        when question_6="I am not sure" then "Not sure" 
        when question_6="No" then "No" 
        when question_6="Yes" then "Yes" 
        else "Not sure"
    end as reponse
from sondage_2016
group by country, reponse
union
select case
    when "" then "2017"
    else "2017"
end as annee
, country
, question_6
, count(question_6) as nbre 
, case 
        when question_6="Not sure" then "Not sure" 
        when question_6="No" then "No" 
        when question_6="Yes" then "Yes" 
        else "Not sure"
    end as reponse
from sondage_2017
group by country, reponse
union 
select case
    when "" then "2018"
    else "2018"
end as annee
, country
, question_6
, count(question_6) as nbre 
, case 
        when question_6="Not sure" then "Not sure" 
        when question_6="No" then "No" 
        when question_6="Yes" then "Yes" 
        else "Not sure"
    end as reponse
from sondage_2018
group by country, reponse
union
select case
    when "" then "2019"
    else "2019"
end as annee
, country
, question_6
, count(question_6) as nbre 
, case 
        when question_6="Not sure" then "Not sure" 
        when question_6="No" then "No" 
        when question_6="Yes" then "Yes" 
        else "Not sure"
    end as reponse
from sondage_2019 
group by country, reponse;"""

#Anonymat
query6 = """select  case
    when year='' then '2014'
    else '2014'
    end as annee
, country
, question_12
, count(question_12)  as nbre 
, case 
    when question_12="Don't Know" then "I don't Know" 
    when question_12="No" then "No" 
    when question_12="Yes" then "Yes"
    else "I don't Know"
end as reponse
from sondage_2014  
group by country, question_12
union 
select  case
    when year='' then '2015'
    else '2015'
    end as annee
, country
, question_12
, count(question_12)  as nbre
, case 
    when question_12="Don't Know" then "I don't Know" 
    when question_12="No" then "No" 
    when question_12="Yes" then "Yes"
    else "I don't Know"
end as reponse
 from sondage_2015 
group by country, question_12
union
select  case
    when '' then '2016'
    else '2016'
    end as annee
, country
, question_9
, count(question_9)  as nbre 
, case 
    when question_9="Don't Know" then "I don't Know" 
    when question_9="No" then "No" 
    when question_9="Yes" then "Yes"
    else "I don't Know"
end as reponse
from sondage_2016  
group by country, question_9
union
select  case
    when '' then '2017'
    else '2017'
    end as annee
, country
, question_9
, count(question_9)  as nbre 
, case 
    when question_9="Don't Know" then "I don't Know" 
    when question_9="No" then "No" 
    when question_9="Yes" then "Yes"
    else "I don't Know"
end as reponse
from sondage_2017  
group by country, question_9
union
select  case
    when '' then '2018'
    else '2018'
    end as annee
, country
, question_9
, count(question_9)  as nbre 
, case 
    when question_9="Don't Know" then "I don't Know" 
    when question_9="No" then "No" 
    when question_9="Yes" then "Yes"
    else "I don't Know"
end as reponse
from sondage_2018 
group by country, question_9
union
select  case
    when '' then '2019'
    else '2019'
    end as annee
, country
, question_9
, count(question_9) as nbre 
, case 
    when question_12="Don't Know" then "I don't Know" 
    when question_12="No" then "No" 
    when question_12="Yes" then "Yes"
    else "I don't Know"
end as reponse
from sondage_2019  
group by country, question_9;"""

#Experience
query7 = """select case
    when year= '' then '2014'
    else '2014'
    end as annee
, country
, question_21
, count(question_21) as nbre 
, case
    when question_21 = "Yes" then "Yes"
    when question_21="Yes, I observed" then "Yes"
    when question_21="Yes, I experienced" then "Yes"
    when question_21="No" then "No"
    else "I don't Know"
end as reponse
from sondage_2014
group by country, question_21
union
select case
    when year= '' then '2015'
    else '2015'
    end as annee
, country
, question_21
, count(question_21) as reponse 
, case
    when question_21 = "Yes" then "Yes"
    when question_21="Yes, I observed" then "Yes"
    when question_21="Yes, I experienced" then "Yes"
    when question_21="No" then "No"
    else "I don't Know"
end as reponse
from sondage_2015
group by country, question_21
union
select case
    when '' then '2016'
    else '2016'
end as annee
, country
, question_16
, count(question_16) as nbre
, case
    when question_16 = "Yes" then "Yes"
    when question_16="Yes, I observed" then "Yes"
    when question_16="Yes, I experienced" then "Yes"
    when question_16="No" then "No"
    else "I don't Know"
end as reponse
from sondage_2016
group by country, question_16
union
select case
    when '' then '2017'
    else '2017'
    end as annee
, country
, question_104
, count(question_104) as reponse 
, case
    when question_104 = "Yes" then "Yes"
    when question_104="Yes, I observed" then "Yes"
    when question_104="Yes, I experienced" then "Yes"
    when question_104="No" then "No"
    else "I don't Know"
end as reponse
from sondage_2017
group by country, question_104
union
select case
    when '' then '2018'
    else '2018'
    end as annee
, country
, question_104
, count(question_104) as reponse 
, case
    when question_104 = "Yes" then "Yes"
    when question_104="Yes, I observed" then "Yes"
    when question_104="Yes, I experienced" then "Yes"
    when question_104="No" then "No"
    else "I don't Know"
end as reponse
from sondage_2018
group by country, question_104
union
select case
    when '' then '2019'
    else '2019'
    end as annee
, country
, question_68
, count(question_68) as reponse 
, case
    when question_68 ="Yes" then "Yes"
    when question_68="Yes, I observed" then "Yes"
    when question_68="Yes, I experienced" then "Yes"
    when question_68="No" then "No"
    else "I don't Know"
end as reponsese
from sondage_2019
group by country, question_68;"""