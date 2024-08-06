#-----------------------------------Импорт библиотек-----------------------------------#
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Output, Input, State
import duckdb
from etl import get_data
import dash_bootstrap_components as dbc
from connector import set_connection
import plotly.graph_objects as go
from dash import dash_table
#--------------------------------------------Импорт данных--------------------------------------------#
tab1_df = get_data('get_v_match')

tab2_df = get_data('get_v_player').dropna(how='all', axis=0)
tab2_df['birthday'] = pd.to_datetime(tab2_df['birthday'])
tab2_df['date'] = pd.to_datetime(tab2_df['date'])
#-----------------------------------Создание элементов управления-----------------------------------#
my_theme = {
    'layout': {
        'plot_bgcolor': '#081228',
        'paper_bgcolor': '#081228',
        'font': {'family': 'Century Gothic', 'color':'white'},
        'legend': {'orientation': 'h', 'title_text': '', 'x': 0, 'y': 1.1}
    }
}

tab1_dd_country = dcc.Dropdown(
    id='tab1_dd_country',
    options=[{'label':x, 'value':x} for x in sorted(tab1_df['country'].unique())],
    value=sorted(tab1_df['country'].unique())[0],
    style={'color':'black'}
)

tab1_dd_team = dcc.Dropdown(
    id='tab1_dd_team',
    style={'color':'black'}
)

tab1_dd_year = dcc.Dropdown(
    id='tab1_dd_year',
    options=[{'label':x, 'value':x} for x in range(2008, 2017)],
    value=2012,
    style={'color':'black'}
    
)

tab2_dd_player = dcc.Dropdown(
    id='tab2_dd_player',
    options=[{'label':x, 'value':x} for x in sorted(tab2_df['player_name'].unique())],
    value='Cristiano Ronaldo',
    style={'color':'black'}
)

tab2_dd_year = dcc.Dropdown(
    id='tab2_dd_year',
    style={'color':'black'}
)

tables = [
        'Country', 
        'Team', 
        'Player', 
        'League', 
        'Player_Attributes', 
        'Team_Attributes', 
        'Match'
    ]
tab3_dd_table = dcc.Dropdown(
    id='tab3_dd_table',
    options=[{'label':x, 'value':x} for x in tables],
    value='Country',
    style={'color':'black'}
)



#-----------------------------------Создание Тabs content-----------------------------------#

tab1_content = [
    dbc.Row([
        dbc.Col([
            html.H6('Select a country'),
            html.Div(tab1_dd_country)
        ], width={'size':4}),
        
        dbc.Col([
            html.H6('Select a team'),
            html.Div(tab1_dd_team)
        ], width={'size':4}),
        
        dbc.Col([
            html.H6('Select the year'),
            html.Div(tab1_dd_year)
        ], width={'size':4})
        
    ], style={'marginTop':'10px'}),
    
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='tab1_bar'),
            style={'marginTop':'10px'}

        )
    ]),
    
    dbc.Row([
        dbc.Col([
            html.Div('The Total Goal'),
            dcc.Graph(id='tab1_bar_small_1')
        ], width={'size':4}
        ),
        
        dbc.Col([
            html.Div('The Average Goal'),
            dcc.Graph(id='tab1_bar_small_2')
        ], width={'size':4}
        ),
        
        dbc.Col([
            html.Div('The Max Goal in Game'),
            dcc.Graph(id='tab1_bar_small_3')
        ], width={'size':4}
        )
    ], style={'marginTop':'50px'})
    
]

tab2_content = [
    dbc.Row([
        dbc.Col([
            html.H6('Select a player'),
            html.Div(tab2_dd_player)
        ], width={'size':4}),
        
        dbc.Col([
            html.H6('Select the year'),
            html.Div(tab2_dd_year)
        ], width={'size':4})
    ], style={'marginTop':'10px'}),
    
    dbc.Row([
        dbc.Col([
            html.Div(id='tab2_info')
        ], width={'size':5}, style={'marginTop':'20px'}),
        
        dbc.Col([
            dcc.Graph(id='tab2_radar')
        ], width={'size':7})
        
    ], style={'marginTop':'10px'})
    
]

tab3_content = [
    dbc.Row([
        dbc.Col([
            html.H6('Select a Table'),
            html.Div(tab3_dd_table)
        ], width={'size':4}),
    ], style={'marginTop':'10px'}),
    
    
    dbc.Row([
        dbc.Col([
            html.Div(id='tab3_table')
        ], width={'size':'12'}, style={'marginTop':'20px'}),
        
    ], style={'marginTop':'10px'})
    
]

text = """
The Soccer Data Visualization is an interactive web application designed for visualizing and analyzing data about European Soccer. 

Author: Shohin Karimov

Project objective: The final project for the course "Data Analytics" to demonstrate skills in data analysis and visualization, as well as for the practical application of the acquired knowledge within the course.

The project is created using Dash and Plotly, providing users with a convenient interface to obtain information about teams and players.

Functionality:
First tab - Team Selection:
- Users can select a team from the list.
- Team statistics are displayed, including the number of goals scored and conceded in matches.

Second tab - Player Characteristics:
- Player characteristics are presented:
    - Date of Birth: information about the player's date of birth.
    - Height: player's height.
    - Weight: player's weight.
    - Preferred Foot: Left or Right.
    

Third tab - Tables:
	These are relatively small tables characterizing the tables that were used.
	

Technologies used:
- Dash: a library for creating interactive web applications in Python.
- Plotly: a library for creating charts and visualizations.
- DuckDB: a database library for storing and using data.
"""

tab4_content = [
    dbc.Row(dcc.Markdown(text, style={'marginLeft':'40px', 
                                      'marginTop':'20px', 
                                      'color': 'white',
                                      'fontSize':'18px'}))
    
]
#--------------------------------------------Front--------------------------------------------#
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
server = app.server

### AppLayout
app.layout = html.Div([
    
    ### Header
    dbc.Row([
        dbc.Col(
            html.Img(src=app.get_asset_url('images/shoot.png'), 
                     style={
                         'width':'80px', 
                         'marginLeft':'10px', 
                         'marginTop':'10px'}),
            width={'size':1}
        ),
           
        
        
        dbc.Col([
            html.H1('Soccer Data Visualization', style={'marginBottom':'-10px'}), 
            html.Div('Obtained from open sources')
        ], style={'marginLeft':'-1px'}, width={'size':'auto'}),
        
        
        dbc.Col(
            html.Div('Created by Karimov Shohin', style={'color':'lightgrey'}),
            style={'marginLeft':'90px'}
        ),
    ], className='app-header'),
    
    ### Body
    dbc.Tabs([
        dbc.Tab(tab1_content, label='Match'),
        dbc.Tab(tab2_content, label='Players'),
        dbc.Tab(tab3_content, label='Data'),
        dbc.Tab(tab4_content, label='About')
    ])
])

#--------------------------------------------CallBacks Tab1--------------------------------------------#
### tab1_dd_team
@app.callback(
    Output(component_id='tab1_dd_team', component_property='options'),
    Output(component_id='tab1_dd_team', component_property='value'),
    Input(component_id='tab1_dd_country', component_property='value'),
)
def to_tab1_dd_country(country):
    countries = sorted(tab1_df[tab1_df['country']==country]['home_team_name'].unique())
    return [{'label':x, 'value':x} for x in countries], countries[0]

### Bar
@app.callback(
    Output(component_id='tab1_bar', component_property='figure'),
    Input(component_id='tab1_dd_team', component_property='value'),
    Input(component_id='tab1_dd_year', component_property='value')
)
def create_tab1_bar(team, year):
    tab1_bar_df = tab1_df[(tab1_df['date'].dt.year == year) & 
                          (tab1_df['home_team_name']==team)]
    
    tab1_bar = go.Figure()
    tab1_bar.add_trace(go.Bar(
        x=[tab1_bar_df['away_team_name_short'], tab1_bar_df['date'].dt.strftime('%Y-%m-%d')],
        y=tab1_bar_df['home_team_goal'],
        name=team,
        marker_color='#00F8FC',
    ))
    tab1_bar.add_trace(go.Bar(
        x=[tab1_bar_df['away_team_name_short'], tab1_bar_df['date'].dt.strftime('%Y-%m-%d')],
        y=tab1_bar_df['away_team_goal'],
        name='Oponent',
        marker_color='#7709F5',
    ))

    tab1_bar.update_layout(barmode='group', xaxis_tickangle=-45, template=my_theme)
    return tab1_bar

### Small
@app.callback(
    Output(component_id='tab1_bar_small_1', component_property='figure'),
    Output(component_id='tab1_bar_small_2', component_property='figure'),
    Output(component_id='tab1_bar_small_3', component_property='figure'),
    Input(component_id='tab1_dd_team', component_property='value'),
    Input(component_id='tab1_dd_year', component_property='value')
)
def create_tab1_bar_small(team, year):
    tab1_small_df = get_data('get_for_small')
    tab1_small_df = tab1_small_df[(tab1_small_df['name']==team) & 
                                  (tab1_small_df['year']==year)]
    tab1_small_df = pd.DataFrame({
    'name':[tab1_small_df['name'].iloc[0], 'opponent'],
    'total_goal':[tab1_small_df['total_home_goal'].iloc[0], tab1_small_df['total_away_goal'].iloc[0]],
    'avg_goal':[tab1_small_df['avg_home_goal'].iloc[0], tab1_small_df['avg_away_goal'].iloc[0]],
    'max_goal':[tab1_small_df['max_home_goal'].iloc[0], tab1_small_df['max_away_goal'].iloc[0]],
})
    ##--------------
    tab1_bar_small_1 = go.Figure()
    tab1_bar_small_1.add_trace(go.Bar(
        x=[tab1_small_df['name'].iloc[0]],
        y=[tab1_small_df['total_goal'].iloc[0]],
        name=team,
        marker_color='#00F8FC',
    ))
    tab1_bar_small_1.add_trace(go.Bar(
        x=['Opponents'],
        y=[tab1_small_df['total_goal'].iloc[1]],
        name='Oponent',
        marker_color='#7709F5',
    ))

    tab1_bar_small_1.update_layout(barmode='group', xaxis_tickangle=-45, template=my_theme)
    
    ##--------------
    tab1_bar_small_2 = go.Figure()
    tab1_bar_small_2.add_trace(go.Bar(
        x=[tab1_small_df['name'].iloc[0]],
        y=[tab1_small_df['avg_goal'].iloc[0]],
        name=team,
        marker_color='#00F8FC',
    ))
    tab1_bar_small_2.add_trace(go.Bar(
        x=['Opponents'],
        y=[tab1_small_df['avg_goal'].iloc[1]],
        name='Oponent',
        marker_color='#7709F5',
    ))

    tab1_bar_small_2.update_layout(barmode='group', xaxis_tickangle=-45, template=my_theme)
    
    ##--------------
    tab1_bar_small_3 = go.Figure()
    tab1_bar_small_3.add_trace(go.Bar(
        x=[tab1_small_df['name'].iloc[0]],
        y=[tab1_small_df['max_goal'].iloc[0]],
        name=team,
        marker_color='#00F8FC',
    ))
    tab1_bar_small_3.add_trace(go.Bar(
        x=['Opponents'],
        y=[tab1_small_df['max_goal'].iloc[1]],
        name='Oponent',
        marker_color='#7709F5',
    ))

    tab1_bar_small_3.update_layout(barmode='group', xaxis_tickangle=-45, template=my_theme)
    return tab1_bar_small_1, tab1_bar_small_2, tab1_bar_small_3

#--------------------------------------------CallBacks Tab2--------------------------------------------#
@app.callback(
    Output(component_id='tab2_dd_year', component_property='options'),
    Output(component_id='tab2_dd_year', component_property='value'),
    Input(component_id='tab2_dd_player', component_property='value')
)

def return_year(player):
    tab2_df_year = tab2_df[tab2_df['player_name']==player]['date'].dt.year.unique()
    
    return [{'label':x, 'value':x} for x in tab2_df_year], tab2_df_year[0]


@app.callback(
    Output(component_id='tab2_info', component_property='children'),
    Output(component_id='tab2_radar', component_property='figure'),
    Input(component_id='tab2_dd_player', component_property='value'),
    Input(component_id='tab2_dd_year', component_property='value')
)
def create_tab1_content(player, year):
    tab2_df_info = tab2_df[(tab2_df['player_name']==player) &
                           (tab2_df['date'].dt.year==year)]
    tab2_df_radar = pd.DataFrame(dict(
        theta=['Pace', 'Shooting', 'Passing', 'Dribbling', 'Defending', 'Physical'],
        r=[tab2_df_info['PAC'].iloc[0],
           tab2_df_info['SHO'].iloc[0],
           tab2_df_info['PAS'].iloc[0],
           tab2_df_info['DRI'].iloc[0],
           tab2_df_info['DEF'].iloc[0],
           tab2_df_info['PHY'].iloc[0]
        ]
    ))
    
    if not tab2_df_info.empty:
        tab2_info = html.Div([
            dbc.Card(
                dbc.CardBody([
                    html.H6("Birthday", className="card-title"),
                    html.H6(
                        f'{tab2_df_info['birthday'].dt.date.iloc[0]} ({year - tab2_df_info['birthday'].dt.year.iloc[0]} years)',
                        className="card-text"
                    ),
                ], style={"backgroundColor": "#132242"}), style={'marginBottom':'10px'}
                
            ),
            dbc.Card(
                dbc.CardBody([
                    html.H6("Height", className="card-title"),
                    html.H6(
                        str(tab2_df_info['height'].iloc[0])[:7]+' Cm',
                        className="card-text"
                    ),
                ], style={"backgroundColor": "#132242"}), style={'marginBottom':'10px'}
                
            ),
            dbc.Card(
                dbc.CardBody([
                    html.H6("Weight", className="card-title"),
                    html.H6(
                        str(tab2_df_info['weight'].iloc[0])[:7]+' Kg',
                        className="card-text"
                    ),
                ], style={"backgroundColor": "#132242"}), style={'marginBottom':'10px'}
                
            ),
            dbc.Card(
                dbc.CardBody([
                    html.H6("Preferred Foot", className="card-title"),
                    html.H6(
                        str(tab2_df_info['preferred_foot'].iloc[0]).title(),
                        className="card-text"
                    ),
                ], style={"backgroundColor": "#132242"}), style={'marginBottom':'10px'}
                
            ),
            # html.Div(f'Birthday: {tab2_df_info['birthday'].dt.date.iloc[0]}'),
            # html.Div(f'Height: {str(tab2_df_info['height'].iloc[0])[:7]+' Cm'}'),
            # html.Div(f'Weight: {str(tab2_df_info['weight'].iloc[0])[:7]+' Kg'}'),
            # html.Div(f'Pref. Foot: {str(tab2_df_info['preferred_foot'].iloc[0]).title()}'),
        ], className='player-info')
    
        tab2_radar = px.line_polar(
            data_frame=tab2_df_radar,
            r='r', theta='theta', line_close=True
        )
        tab2_radar.update_traces(fill='toself')
        tab2_radar.update_layout(template=my_theme)
        tab2_radar.update_layout(
            polar=dict(
                bgcolor='#081228'  # Цвет фона полярного графика
            ),
        )
        return tab2_info, tab2_radar


#--------------------------------------------CallBacks Tab3--------------------------------------------#
@app.callback(
    Output(component_id='tab3_table', component_property='children'),
    Input(component_id='tab3_dd_table', component_property='value')
)
def get_table(table):
    table_df = get_data(table)
    table_ret = html.Div([
    dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in table_df.columns],
        data=table_df.head(100).to_dict('records'),
        style_cell={
            'backgroundColor': '#081228',  # Фон ячеек
            'textAlign': 'left',
            'padding': '5px',
            'color': '#ffffff'
        },
        style_header={
            'backgroundColor': '#7709f5',  # Фон заголовков столбцов
            'color': 'white',  # Цвет текста в заголовках
            'fontWeight': 'bold'
        },
    )
    ])
    return table_ret


if __name__ == '__main__':
    app.run_server()
