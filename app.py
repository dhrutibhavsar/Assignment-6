import pandas as pd
import numpy as np
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

#https://assignment-6-c4ba.onrender.com
df = pd.read_csv("FIFA World Cup winners.csv")

country_wins = df['Winner'].value_counts().reset_index()
country_wins.columns = ['Country', 'Wins']

app = Dash(__name__)


fig_map = px.choropleth(
    country_wins, locations='Country', locationmode='country names',
    color='Wins', color_continuous_scale='Blues',
    title='FIFA World Cup Winning Countries'
)


app.layout = html.Div([
    html.H1("FIFA World Cup Dashboard", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig_map),
    

    html.Label("Select a country:"),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': c, 'value': c} for c in country_wins['Country']],
        placeholder="Choose a country"
    ),
    html.Div(id='country-output'),
    

    html.Label("Select a year:"),
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': y, 'value': y} for y in df['Year']],
        placeholder="Choose a year"
    ),
    html.Div(id='year-output')
])


@app.callback(
    Output('country-output', 'children'),
    Input('country-dropdown', 'value')
)
def update_country(selected_country):
    if selected_country:
        wins = country_wins.loc[country_wins['Country'] == selected_country, 'Wins'].values[0]
        return f"{selected_country} has won {wins} times."

@app.callback(
    Output('year-output', 'children'),
    Input('year-dropdown', 'value')
)
def update_year(selected_year):
    if selected_year:
        row = df[df['Year'] == selected_year].iloc[0]
        return f"In {selected_year}, {row['Winner']} won, and {row['Runner-up']} was the runner-up."
        
if __name__ == '__main__':
    app.run(debug=True, port=8060) 

server = app.server
