{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "65c76f1c-0b5c-4e5a-9b44-bf6401f035af",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from dash import Dash, dcc, html, Input, Output\n",
    "import plotly.express as px"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "8d0feac1-2a23-4265-84e9-953ca05fa369",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"100%\"\n",
       "            height=\"650\"\n",
       "            src=\"http://127.0.0.1:8060/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x74ec503796f0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#https://assignment-6-c4ba.onrender.com\n",
    "df = pd.read_csv(\"FIFA World Cup winners.csv\")\n",
    "country_wins = df['Winner'].value_counts().reset_index()\n",
    "country_wins.columns = ['Country', 'Wins']\n",
    "\n",
    "app = Dash(__name__)\n",
    "\n",
    "\n",
    "fig_map = px.choropleth(\n",
    "    country_wins, locations='Country', locationmode='country names',\n",
    "    color='Wins', color_continuous_scale='Blues',\n",
    "    title='FIFA World Cup Winning Countries'\n",
    ")\n",
    "\n",
    "\n",
    "app.layout = html.Div([\n",
    "    html.H1(\"FIFA World Cup Dashboard\", style={'textAlign': 'center'}),\n",
    "    dcc.Graph(figure=fig_map),\n",
    "    \n",
    "\n",
    "    html.Label(\"Select a country:\"),\n",
    "    dcc.Dropdown(\n",
    "        id='country-dropdown',\n",
    "        options=[{'label': c, 'value': c} for c in country_wins['Country']],\n",
    "        placeholder=\"Choose a country\"\n",
    "    ),\n",
    "    html.Div(id='country-output'),\n",
    "    \n",
    "\n",
    "    html.Label(\"Select a year:\"),\n",
    "    dcc.Dropdown(\n",
    "        id='year-dropdown',\n",
    "        options=[{'label': y, 'value': y} for y in df['Year']],\n",
    "        placeholder=\"Choose a year\"\n",
    "    ),\n",
    "    html.Div(id='year-output')\n",
    "])\n",
    "\n",
    "\n",
    "@app.callback(\n",
    "    Output('country-output', 'children'),\n",
    "    Input('country-dropdown', 'value')\n",
    ")\n",
    "def update_country(selected_country):\n",
    "    if selected_country:\n",
    "        wins = country_wins.loc[country_wins['Country'] == selected_country, 'Wins'].values[0]\n",
    "        return f\"{selected_country} has won {wins} times.\"\n",
    "\n",
    "@app.callback(\n",
    "    Output('year-output', 'children'),\n",
    "    Input('year-dropdown', 'value')\n",
    ")\n",
    "def update_year(selected_year):\n",
    "    if selected_year:\n",
    "        row = df[df['Year'] == selected_year].iloc[0]\n",
    "        return f\"In {selected_year}, {row['Winner']} won, and {row['Runner-up']} was the runner-up.\"\n",
    "        \n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True, port=8060) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "360318e8-e112-4cfa-8334-18fa5e1d393b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "anaconda-2024.02-py310",
   "language": "python",
   "name": "conda-env-anaconda-2024.02-py310-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.14"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
