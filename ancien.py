from os import stat
from re import T
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt
import requests


# Titre du document
st.title('Dashboard : Prédiction de crédit')

# Ouverture des fichiers
read_and_cache_csv = st.cache(pd.read_csv)
data = read_and_cache_csv("tableau_credit.csv")

# Premier chapitre
st.sidebar.markdown("## Premier chapitre : Information personnel")

# Texte au centre du document

# Traduction des mots en anglais en français
def type_org(data, val):
    statut = ['Business Entity Type 3', 'School', 'Government', 'Religion', 'Other', 'XNA', 'Electricity', 'Medicine',
       'Business Entity Type 2', 'Self-employed', 'Transport: type 2', 'Construction', 'Housing', 'Kindergarten', 'Trade: type 7',
       'Industry: type 11', 'Military', 'Services', 'Security Ministries', 'Transport: type 4', 'Industry: type 1', 'Emergency', 'Security',
       'Trade: type 2', 'University', 'Transport: type 3', 'Police', 'Business Entity Type 1', 'Postal', 'Industry: type 4',
       'Agriculture', 'Restaurant', 'Culture', 'Hotel', 'Industry: type 7', 'Trade: type 3', 'Industry: type 3', 'Bank',
       'Industry: type 9', 'Insurance', 'Trade: type 6', 'Industry: type 2', 'Transport: type 1', 'Industry: type 12',
       'Mobile', 'Trade: type 1', 'Industry: type 5', 'Industry: type 10', 'Legal Services', 'Advertising', 'Trade: type 5', 'Cleaning',
       'Industry: type 13', 'Trade: type 4', 'Telecom', 'Industry: type 8', 'Realtor', 'Industry: type 6']
    statut_vf = ['Entité commerciale de type 3', 'École', 'Gouvernement', 'Religion', 'Autre', 'XNA', 'Électricité', 'Médecine',
       'Entité commerciale de type 2', 'Indépendant', 'Transport : type 2', 'Construction', 'Habitation', 'Maternelle', 'Commerce : type 7',
       'Industrie : type 11', 'Militaire', 'Services', 'Ministères de la sécurité', 'Transport : type 4', 'Industrie : type 1', 'Urgence', 'Sécurité',
       'Commerce : type 2', 'Université', 'Transport : type 3', 'Police', 'Entité commerciale de type 1', 'Poste', 'Industrie : type 4',
       'Agriculture', 'Restaurant', 'Culture', 'Hôtel', 'Industrie : type 7', 'Commerce : type 3', 'Industrie : type 3', 'Banque',
       'Industrie : type 9', 'Assurances', 'Commerce : type 6', 'Industrie : type 2', 'Transport : type 1', 'Industrie : type 12',
       'Mobile', 'Commerce : type 1', 'Industrie : type 5', 'Industrie : type 10', 'Services juridiques', 'Publicité', 'Commerce : type 5', 'Nettoyage',
       'Industrie : type 13', 'Commerce : type 4', 'Télécom', 'Industrie : type 8', 'Agent immobilier', 'Industrie : type 6']

    for i in range(0, len(statut), 1) :
        if data["ORGANIZATION_TYPE"].iloc[val] == statut[i] :
            st.write("Le type d'organisation est : ", statut_vf[i])

def statut_educ(data, val):
    statut = ['Secondary / secondary special', 'Higher education', 'Incomplete higher', 'Lower secondary', 'Academic degree']
    statut_vf = ["Secondaire", "Enseignement supérieur", "Enseignement incomplet", "Secondaire inférieur", "Diplôme universitaire"]

    for i in range(0, len(statut), 1) :
        if data["NAME_EDUCATION_TYPE"].iloc[val] == statut[i] :
            st.write("Le niveau de scolarité est : ", statut_vf[i])

def statut_mar(data, val):
    statut = data["NAME_FAMILY_STATUS"].unique()

    for i in range(0, len(statut), 1) :
        if data["NAME_FAMILY_STATUS"].iloc[val] == statut[i] :
            st.write("Le niveau de scolarité est : ", statut[i])

def statut_dom(data, val):
    statut = data["NAME_INCOME_TYPE"].unique()

    for i in range(0, len(statut), 1) :
        if data["NAME_INCOME_TYPE"].iloc[val] == statut[i] :
            st.write("Le niveau de scolarité est : ", statut[i])

def statut_trav(data, val):
    statut = ['Laborers', 'Core staff', 'Accountants', 'Managers', 'Drivers', 'Sales staff', 'Cleaning staff', 'Cooking staff',
       'Private service staff', 'Medicine staff', 'Security staff', 'High skill tech staff', 'Waiters/barmen staff',
       'Low-skill Laborers', 'Realty agents', 'Secretaries', 'IT staff', 'HR staff']
    statut_vf = ['Ouvriers', 'Personnel de base', 'Comptables', 'Managers', 'Chauffeurs', "Personnel de vente", "Personnel de nettoyage",
                "Personnel de cuisine", 'Personnel de service privé', 'Personnel de médecine', 'Personnel de sécurité',
                'Personnel technique hautement qualifié', 'Serveurs/barmen', 'Ouvriers peu qualifiés', 'Agents immobiliers', 'Secrétaires',
                'Personnel informatique', "personnel RH"]

    for i in range(0, len(statut), 1) :
        if data["OCCUPATION_TYPE"].iloc[val] == statut[i] :
            st.write("Le client travail comme : ", statut_vf[i])


def statut_appt(data, val):
    statut = ['House / apartment', 'Rented apartment', 'With parents',
                'Municipal apartment', 'Office apartment', 'Co-op apartment']
    statut_vf = ['Maison / appartement', 'Appartement loué', 'Avec parents',
                'Appartement municipal', 'Appartement bureau', 'Appartement coopératif']

    for i in range(0, len(statut), 1) :
        if data["NAME_HOUSING_TYPE"].iloc[val] == statut[i] :
            st.write("Le client habite dans : ", statut_vf[i])

# Graphique et le texte du milieu
def graphique(val, data, mes_1, target_label):

    st.markdown("## Premier chapitre : Information personnel")
 
    if target_label == 0:
        st.success("Le client n'est pas à risque")
    else :
        st.error("Le client est à risque")
    st.write("L'âge du client est : ", data['DAYS_BIRTH'].iloc[val].round(0), "ans.")
    statut_educ(data, val)
    statut_trav(data, val)
    type_org(data, val)

    st.markdown("## Deuxième chapitre : Information sur le crédit")

    st.write("Le statut du crédit est : ", mes_1)

    #st.write("Le revenue du client par année est de ", data["AMT_INCOME_TOTAL"].iloc[val], "$")
    #st.write("Le crédit demandé est de", data["AMT_CREDIT"].iloc[val], "$")
    #st.write("Le client devra rembourser, ce montant : ", data["AMT_ANNUITY"].iloc[val], "$ par année")

    tab = data[["SK_ID_CURR", "AMT_INCOME_TOTAL", "AMT_CREDIT", "AMT_ANNUITY"]].copy()
    tab.set_index('SK_ID_CURR', inplace = True)

    tab.rename(columns={'AMT_INCOME_TOTAL': 'Salaire', 'AMT_CREDIT': 'Crédit',
                        'AMT_ANNUITY': 'Rente'}, inplace=True)

    bar_chart = px.bar(tab[["Salaire", "Crédit", "Rente"]].iloc[val],
                        title="Information sur le crédit", text_auto=True)
    bar_chart.update_layout(xaxis_title='Information crédit du client', yaxis_title='Dolars ($)')
    st.write(bar_chart)
    

# Texte sur le côté

# Création des tableaux en fonction de la sélection

# Choix du client si son crédit est acceptée ou pas
def tab_target(data, val):
    statut = [0,1]
    for i in range(0, len(statut), 1) :
        if val == statut[i] :
            data_target = data[data["TARGET"] == statut[i]]
            return data_target

# Choix du statut marital du client
def tab_mar(data, val) :
    statut = ['Married', 'Single / not married', 'Civil marriage', 'Widow', 'Separated', 'Unknown']
    for i in range(0, len(statut), 1) :
        if val == statut[i] :
            data_mar = data[data["NAME_FAMILY_STATUS"] == statut[i]]
            return data_mar

# Choix du domaine
def tab_dom(data, val) :
    statut = ["Working", "Commercial associate", "Pensioner", "State servant", "Unemployed", "Student", "Businessman", "Maternity leave"]
    for i in range(0, len(statut), 1) :
        if val == statut[i] :
            data_dom = data[data["NAME_INCOME_TYPE"] == statut[i]]
            return data_dom

# L'âge du client

# On récupère le min et le max des colonnes et on les mets à la dizaine inférieur et supérieur

# Calcul des âges minimums
def def_min(min):
    if min % 10==0:
        return min
    else:
        while min % 10>0:
            min=min-1
    return min

# Calcul des âges maximums
def def_max(max):
    if max % 10==0:
        return max
    else:
        while max % 10>0:
            max=max-1
    return max

# Construction du tableau selon l'âge et si le tableau est vide, il renvoie un message
def tab_age(data, val):
    statut = list(range(20, 60, 10))
    if val == 60 :
        data_age = data[data['DAYS_BIRTH'] >= 60]
        return data_age
    for i in range(0, len(statut), 1) :
        if val == statut[i] :
            data_age = data[(data['DAYS_BIRTH'] >= statut[i]) & (data['DAYS_BIRTH'] < statut[i]+10)]
            return data_age
                
# On vérifie si les valeurs minimum est maximum sont égaux, ou pas et appelle la fonction du dessus

# Pour la construction du tableau
def egal(data, min, max) :
    if min == max :
        age_label = st.sidebar.write("Age du client : ", min)
        data = tab_age(data, min)
        return data
    else :
        age_label = st.sidebar.slider("Age du client : ", min_value=min, max_value=max, step=10)
        data = tab_age(data, age_label)
        return data

# Construction du tableau type de crédit
def tab_cred(data, desired_label):
    statut = ["Cash loans", "Revolving loans"]
    for i in range(0, len(statut), 1) :
        if desired_label == statut[i] :
            data_cred = data[data["NAME_CONTRACT_TYPE"] == statut[i]]
            return data_cred

# Si il y a deux valeurs ou une, il sera envoyé dans la fonction du dessus pour récupérer le tableau
def cred(data) :
    st.sidebar.markdown("## Deuxième chapitre : Information sur le crédit")
    st.sidebar.markdown("Choix pour le type de crédit.")
    cred_label = st.sidebar.radio("Demande de crédit : ", data["NAME_CONTRACT_TYPE"].unique())
    data = tab_cred(data, cred_label)
    return data, cred_label

# Si le client possède un appartement ou pas
def appt(data) :
    statut = ["Y", "N"]
    val = st.sidebar.radio("Le client possèdent-ils un appartement ?", data["FLAG_OWN_REALTY"].unique())
    for i in range(0, len(statut), 1) :
        if val == statut[i] :
            data_appt = data[data["FLAG_OWN_REALTY"] == statut[i]]
            return data_appt
    

# Construction du premier chapitre

# Les premières sélections vont se faire, les informations personnelles
def premier_chapitre(data) :
    target_label = st.sidebar.radio('Client pas à risque (0) et Client à risque (1) :', [0,1])
    data = tab_target(data, target_label)

    st.sidebar.markdown("Choix des informations personnelles : statut maritale, domaine de travail et âge.")

    mar_label = st.sidebar.selectbox("Statut marital", data["NAME_FAMILY_STATUS"].unique())
    data = tab_mar(data, mar_label)

    dom_label = st.sidebar.selectbox("Domaine de travail", data["NAME_INCOME_TYPE"].unique())
    data = tab_dom(data, dom_label)

    min_val = data["DAYS_BIRTH"].min()
    max_val = data["DAYS_BIRTH"].max()
    min_val= def_min(int(min_val))
    max_val= def_max(int(max_val))
    data = egal(data, min_val, max_val)
    return data, target_label

# Construction du deuxième chapitre

# Les sélections sur le crédit et gère les tableaux vide
def deuxième_chapitre(data, target_label) :
    if len(data) == 0 :
        st.warning("Pas de client avec ces critères")
    else :
        data, cred_label = cred(data)

        data = data.reset_index()

        val = st.sidebar.selectbox('Choix du client : ', data["SK_ID_CURR"])
        val = data[data["SK_ID_CURR"] == val].index.values.astype(int)[0]

        if cred_label == "Cash loans" :
            mes_1 = "Premier emprunt"
        else :
            mes_1 = "Renouvellement"
        graphique(val, data, mes_1, target_label)
        troisième_chapitre(data, val)
        quatrieme_chapitre(data, val)

# Construction du troisième chapitre

# Les informations sur le dossier

# Il se fait appeller par la fonction deuxième_chapitre
def troisième_chapitre(data, val) :
    st.sidebar.markdown("## Troisième chapitre : Retard / Problème")
    st.markdown("## Troisième chapitre : Information sur le crédit")

    st.sidebar.markdown("Affiche si le client n'a pas de défaut ou de retard de paiment. Si il y en a,\
            il affiche le nombre de problèmes et le nombre de jours de retards sur les 30 à 60 derniers jours.")
    
    if (data["REG_REGION_NOT_LIVE_REGION"].iloc[val] == 0 and data["OBS_30_CNT_SOCIAL_CIRCLE"].iloc[val] == 0.0 and
        data["DEF_30_CNT_SOCIAL_CIRCLE"].iloc[val] == 0.0 and data["OBS_60_CNT_SOCIAL_CIRCLE"].iloc[val] == 0.0 and
        data["DEF_60_CNT_SOCIAL_CIRCLE"].iloc[val] == 0.0) :
            st.success("Pas de problème de dossier et de retard")
    else :
        if data["REG_REGION_NOT_LIVE_REGION"].iloc[val] == 0 :
            st.success("Pas de problème de dossier")
        else :
            st.warning("Problème de dossier, adresse différente donner")

        if data["OBS_30_CNT_SOCIAL_CIRCLE"].iloc[val] == 0.0 :
            st.success("Pas de défaut sur les 30 derniers jours")
        else :
            st.warning("Défaut observable trouvé sur les 30 derniers jours")
            st.write("Défaut observable : ", data["OBS_30_CNT_SOCIAL_CIRCLE"].iloc[val])

        if data["DEF_30_CNT_SOCIAL_CIRCLE"].iloc[val] == 0.0 :
            st.success("Pas de retard sur les 30 derniers jours")
        else :
            st.warning("Retard observable trouvé sur les 30 derniers jours")
            st.write("Nombre de jours de retard : ", data["DEF_30_CNT_SOCIAL_CIRCLE"].iloc[val])

        if data["OBS_60_CNT_SOCIAL_CIRCLE"].iloc[val] == 0.0 :
            st.success("Pas de défaut sur les 30 derniers jours")
        else :
            st.warning("Défaut observable trouvé sur les 60 derniers jours")
            st.write("Défaut observable : ", data["OBS_60_CNT_SOCIAL_CIRCLE"].iloc[val])

        if data["DEF_60_CNT_SOCIAL_CIRCLE"].iloc[val] == 0.0 :
            st.success("Pas de retard sur les 60 derniers jours")
        else :
            st.warning("Retard observable trouvé sur les 60 derniers jours")
            st.write("Nombre de jours de retard : ", data["DEF_60_CNT_SOCIAL_CIRCLE"].iloc[val])

# Affichage des notes    
def quatrieme_chapitre(data, val):

    st.sidebar.markdown("## Quatrième chapitre : Note Appartement / Ville / Régions")
    st.markdown("## Quatrième chapitre : Note Appartement / Ville / Régions")

    st.sidebar.markdown("Dans ce chapitre, les notes des clients sur leur appartement, ville et régions seront consignées. Note interne et externe.\
        Une note élevée montre une ville avec beaucoup de population, une ville active.")

    data = appt(data)
    statut_appt(data, val)

    st.write("Note normalisé sur la région ou vit le client, (une note élevée siginifie une population élevée")
    if data["REGION_POPULATION_RELATIVE"].iloc[val] < 0.33 :
        note = 1
        st.write("Note Région : ", note)
    elif 0.33 < data["REGION_POPULATION_RELATIVE"].iloc[val] < 0.66 :
        note = 2
        st.write("Note Région : ", note)
    else :
        note = 3
        st.write("Note Région : ", note)

    if data["APARTMENTS_AVG"].iloc[val] < 0.33 :
        note = 1
    elif 0.33 < data["APARTMENTS_AVG"].iloc[val] < 0.66 :
        note = 2
    else :
        note = 3

    data["Score Appartement"] = note
    tab = data[["SK_ID_CURR", "Score Appartement", "REGION_RATING_CLIENT", "REGION_RATING_CLIENT_W_CITY"]].copy()
    tab.set_index('SK_ID_CURR', inplace = True)

    tab.rename(columns={'REGION_RATING_CLIENT': 'Score Regions',
                        'REGION_RATING_CLIENT_W_CITY': 'Score Region/Ville'}, inplace=True)

    bar_chart = px.bar(tab[["Score Appartement", "Score Regions", "Score Region/Ville"]].iloc[val],
                            title="Score sur l'appartement, régions et ville du client")

    bar_chart.update_layout(yaxis=dict(range=[0,3]))
    bar_chart.update_layout(xaxis_title='Score donnée interne', yaxis_title='Valeur')
    st.write(bar_chart)

    st.write("Score normalisé à partir d'une source de données externe")

    tab = data[["SK_ID_CURR", "EXT_SOURCE_1", "EXT_SOURCE_2", "EXT_SOURCE_3"]].copy()
    tab.set_index('SK_ID_CURR', inplace = True)
    tab.rename(columns={'EXT_SOURCE_1': 'Score externe 1', 'EXT_SOURCE_2': 'Score externe 2',
                'EXT_SOURCE_3': 'Score externe 3'}, inplace=True)
    bar_chart = px.bar(tab[["Score externe 1", "Score externe 2", "Score externe 3"]].iloc[val],
                            title="Score externe")
    bar_chart.update_layout(yaxis=dict(range=[0,1]))
    bar_chart.update_layout(xaxis_title='Score', yaxis_title='Valeur')
    st.write(bar_chart)

# Main
if __name__ == '__main__':
    # Appel du premier chapitre
    data, target_label = premier_chapitre(data)

    #Appelle du second et du troisième chapitre
    deuxième_chapitre(data, target_label)