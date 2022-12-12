
import pandas as pd
import numpy as np
import plotly.express as px
import dash
from dash import Dash, dcc, html, Input, Output, dash_table


dt_df = pd.read_excel('report.xlsx', sheet_name='AC_DT')
pot_df = pd.read_excel('report.xlsx', sheet_name='Pot_cand')
parlimentary_df = pd.read_excel('report.xlsx', sheet_name='Lok Sabha 14 & 19')
assembly_df = pd.read_excel('report.xlsx', sheet_name='AE 08, 13 & 18')
ae_pos_df = pd.read_excel('report.xlsx', sheet_name='ae_pos')
ls_pos_df = pd.read_excel('report.xlsx', sheet_name='ls_pos')
caste_df = pd.read_excel('report.xlsx', sheet_name='Caste')
support_df = pd.read_excel('report.xlsx', sheet_name='Support')
issues_df = pd.read_excel('report.xlsx', sheet_name='Issues')
intro_df = pd.read_excel('report.xlsx', sheet_name='Intro')

ac_list = list(dt_df['Assembly Constituency'].unique())
district_list = list(dt_df['District'].unique())
district_list = sorted(district_list)


app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1("Assembly Constituency Report",style={'text-align':'centre','fontWeight':'bold'})],
        className='Header'),
    
    html.Div([
        html.Label("Select District", style={'colour': '#000000',
                                             'fontsize' : '16px','fontWeight':'bold'}),
        dcc.Dropdown(id="District",
                options=[{"label" : i, "value" : i} for i in district_list],
                placeholder="Select Discrict",
                multi=False,
                searchable=True,
                value= 'Tonk',
                clearable=False,
                style={'width': '100%', 'verticalAlign': 'middle',
                       'color':'black'}
                )],className='Dropdown1'),
        html.Div([
        html.Label("Select Assembly Constituency", 
                   style={'color':'#000000','text-align':'centre',
                          'fontSize':'16px','fontWeight':'bold'}),
        dcc.Dropdown(id="AC",
                     options=[],
                     placeholder="Select Assembly Constituency",
                     multi = False,
                     searchable=True,
                    #  value='None',
                     clearable=False,
                     style={'width': '100%', 'verticalAlign': 'middle',
                            'color':'black'})
        ],className="Dropdown2"),

        html.Div(id='output_container', children=[],className='Tab'),

        html.Div(children=[
            html.Label('Assembly Election Stats',style={'fontSize': 11.5,'fontWeight':'bold'}),
            dash_table.DataTable(id='AC_part_table', style_cell={'text-align':'left',
                                                'height':'auto',
                                                'fontSize': 11.5,
                                                'maxWidth': '35%',
                                                'font-family': 'HelveticaNeue'
                                                },
                                    style_header={'fontWeight':'bold',
                                                            'color': '#ffffff',
                                                            'backgroundColor':'#052F5F'},
                                    style_data={'fontWeight':'bold',
                                                        'whiteSpace': 'normal',
                                                        'height': 'auto',
                                                        'backgroundColor': 'transparent' 
                                                        },
                                    style_cell_conditional=[
                                        {'if': {'column_id':'Turnout'}, 'width' : '30%'},
                                        {'if': {'column_id':'Electors'}, 'width' : '30%'},
                                        {'if':{'column_id':'Valid Votes'},'width':'30%'}
                                        ], 
                                    style_as_list_view=True,
            )],className='ac_part'),
        html.Div(children=[
            html.Label('Lok Sabha Election Stats',style={'fontSize': 11.5,'fontWeight':'bold'}),
            dash_table.DataTable(id='LS_part_table',
             style_cell={'text-align':'left',
                                                'height':'auto',
                                                'fontSize': 11.5,
                                                'maxWidth': '35%',
                                                'font-family': 'HelveticaNeue'
                                                },
                                    style_header={'fontWeight':'bold',
                                                            'color': '#ffffff',
                                                            'backgroundColor':'#052F5F'},
                                    style_data={'fontWeight':'bold',
                                                        'whiteSpace': 'normal',
                                                        'height': 'auto',
                                                        'backgroundColor': 'transparent' 
                                                        },
                                    style_cell_conditional=[

                                        {'if':{'column_id':'Year'},'width':'10%'}
                                        ], 
                                    style_as_list_view=True,            
            )],className='ls_part'),
        html.Div(children=[
            html.Label('Assembly Election Summary',style={'fontSize': 11.5,'fontWeight':'bold'}),
            dash_table.DataTable(id='AC_pos_table',
             style_cell={'text-align':'left',
                                                'height':'auto',
                                                'fontSize': 11.5,
                                                'maxWidth': '35%',
                                                'font-family': 'HelveticaNeue'
                                                },
                                    style_header={'fontWeight':'bold',
                                                            'color': '#ffffff',
                                                            'height': 'auto',
                                                            'backgroundColor':'#052F5F'},
                                    style_data={'fontWeight':'bold',
                                                        'whiteSpace': 'normal',
                                                        'height': 'auto',
                                                        'backgroundColor': 'transparent' 
                                                        },
                                    style_cell_conditional=[
                                        # {'if': {'column_id':'Year'}, 'width' : '5%'},
                                        {'if': {'column_id':'1st'}, 'width' : '15%'},
                                        {'if':{'column_id':'1st Party'},'width':'5%'},
                                        {'if': {'column_id':'1st Votes'}, 'width' : '5%'},
                                        {'if':{'column_id':'1st Vote %'},'width':'5%'},
                                        {'if': {'column_id':'2nd'}, 'width' : '15%'},
                                        {'if':{'column_id':'2nd Party'},'width':'5%'},
                                        {'if': {'column_id':'2nd Votes'}, 'width' : '5%'},
                                        {'if':{'column_id':'2nd Vote %'},'width':'5%'},
                                        {'if': {'column_id':'3rd'}, 'width' : '15%'},
                                        {'if':{'column_id':'3rd Party'},'width':'5%'},
                                        {'if': {'column_id':'3rd Votes'}, 'width' : '5%'},
                                        {'if':{'column_id':'3rd Vote %'},'width':'5%'}
                                        ],  
                                    style_as_list_view=True,
            )],className='ae_summ'),
        html.Div(children=[
            html.Label('Lok Sabha Election Summary',style={'fontSize': 11.5,'fontWeight':'bold'}),
            dash_table.DataTable(id='LS_pos_table',
             style_cell={'text-align':'left',
                                                'height':'auto',
                                                'fontSize': 11.5,
                                                'maxWidth': '35%',
                                                'font-family': 'HelveticaNeue'
                                                },
                                    style_header={'fontWeight':'bold',
                                                            'color': '#ffffff',
                                                            'backgroundColor':'#052F5F'},
                                    style_data={'fontWeight':'bold',
                                                        'whiteSpace': 'normal',
                                                        'height': 'auto',
                                                        'backgroundColor': 'transparent' 
                                                        },
                                    style_cell_conditional=[
                                        # {'if': {'column_id':'Year'}, 'width' : '5%'},
                                        {'if': {'column_id':'1st'}, 'width' : '15%'},
                                        {'if':{'column_id':'1st Party'},'width':'5%'},
                                        {'if': {'column_id':'1st Votes'}, 'width' : '5%'},
                                        {'if':{'column_id':'1st Vote %'},'width':'5%'},
                                        {'if': {'column_id':'2nd'}, 'width' : '15%'},
                                        {'if':{'column_id':'2nd Party'},'width':'5%'},
                                        {'if': {'column_id':'2nd Votes'}, 'width' : '5%'},
                                        {'if':{'column_id':'2nd Vote %'},'width':'5%'},
                                        {'if': {'column_id':'3rd'}, 'width' : '15%'},
                                        {'if':{'column_id':'3rd Party'},'width':'5%'},
                                        {'if': {'column_id':'3rd Votes'}, 'width' : '5%'},
                                        {'if':{'column_id':'3rd Vote %'},'width':'5%'}
                                        ],  
                                    style_as_list_view=True,
            )],className='ls_summ'),


        html.Div(children=[
            html.Label('Potential Candidate',style={'fontWeight':'bold'}),
            dash_table.DataTable(id='pot_table',
             style_cell={'text-align':'left',
                                                'height':'auto',
                                                'fontSize': 11.5,
                                                'maxWidth': '35%',
                                                'font-family': 'HelveticaNeue'
                                                },
                                    style_header={'fontWeight':'bold',
                                                            'color': '#ffffff',
                                                            'backgroundColor':'#052F5F'},
                                    style_data={'fontWeight':'bold',
                                                        'whiteSpace': 'normal',
                                                        'height': 'auto',
                                                        'backgroundColor': 'transparent' 
                                                        },
                                    style_cell_conditional=[
                                        {'if':{'column_id':'Caste'},'width':'12%'},
                                        {'if': {'column_id':'Financials (In CR)'}, 'width' : '17%'},
                                        {'if':{'column_id':'Popularity'},'width':'15%'}
                                        ], 
                                    style_as_list_view=True,
            )],className='poten'),
        html.Div(children=[
            html.Label('Issues Of Constituency',style={'fontWeight':'bold'}),
            dash_table.DataTable(id='issues_table',
             style_cell={'text-align':'left',
                                                'height':'auto',
                                                'fontSize': 11.5,
                                                'maxWidth': '35%',
                                                'font-family': 'HelveticaNeue'
                                                },
                                    style_header={'fontWeight':'bold',
                                                            'color': '#ffffff',
                                                            'backgroundColor':'#052F5F'},
                                    style_data={'fontWeight':'bold',
                                                        'whiteSpace': 'normal',
                                                        'height': 'auto',
                                                        'backgroundColor': 'transparent' 
                                                        },
                                    style_cell_conditional=[

                                         {'if':{'column_id':'Key Issues'},'width':'40%'}
                                        ], 
                                    style_as_list_view=True,
            )],className='issue'),
        html.Div(children=[
            html.Label('Intro Of Constituency',style={'fontWeight':'bold'}),
            dash_table.DataTable(id='intro_table',
             style_cell={'text-align':'left',
                                                'height':'auto',
                                                'fontSize': 11.5,
                                                'maxWidth': '35%',
                                                'font-family': 'HelveticaNeue'
                                                },
                                    style_header={'fontWeight':'bold',
                                                            'color': '#ffffff',
                                                            'backgroundColor':'#052F5F'},
                                    style_data={'fontWeight':'bold',
                                                        'whiteSpace': 'normal',
                                                        'height': 'auto',
                                                        'backgroundColor': 'transparent' 
                                                        },
                                    style_cell_conditional=[

                                         {'if':{'column_id':'Stat'},'width':'40%'}
                                        ], 
                                    style_as_list_view=True,
            )],className='intro'),
        

        html.Div([
            html.Label('AC Caste Breakdown',style={'fontWeight':'bold'}),
            dcc.Graph(id='pie_caste')
                    ],className='pie'),
        html.Div([
            html.Label('Potential Candidate Support',style={'fontWeight':'bold'}),
            dcc.Graph(id='bar_supp')
                    ],className='bar')
                        
    ], className='repo')

@app.callback(
    Output('AC','options'),
    Output('AC', 'value'),
    [Input('District','value')]
)
def update_ac(District):
    df = dt_df[dt_df['District']== District]
    k = df["AC"].unique()
    return[{'label':i, 'value':i} for i in df['AC'].unique()],k[0]

@app.callback(
    [
    Output('AC_part_table','data'),
    Output('AC_part_table', 'columns'),
    Output('LS_part_table','data'),
    Output('LS_part_table', 'columns'),
    Output('AC_pos_table','data'),
    Output('AC_pos_table', 'columns'),
    Output('LS_pos_table','data'),
    Output('LS_pos_table', 'columns'),
    Output('pot_table','data'),
    Output('pot_table', 'columns'),   
    Output('issues_table','data'),
    Output('issues_table', 'columns'),   
    Output('intro_table','data'),
    Output('intro_table', 'columns'),  

    ],
    [Input('AC','value')]
    )

def update_table(Constituency):

    ## Data table for ac participation
    df_par = assembly_df[assembly_df['AC'] == Constituency]
    df_par = df_par.drop(columns=['AC'])
    df_par = df_par.drop_duplicates(subset=['Year'])
    df_par = df_par[["Year","Turnout","Electors",'Valid Votes']]
    df_par = df_par.sort_values(by='Year',ascending=False)
    columns = [{'name':col,'id':col} for col in df_par.columns]
    data = df_par.to_dict(orient='records')

    ## Data table for ls participation
    df_ls = parlimentary_df[parlimentary_df['AC'] == Constituency]
    df_ls = df_ls.drop(columns=['AC'])
    df_ls = df_ls.drop_duplicates(subset=['Year'])
    df_ls = df_ls[["Year",'Valid Votes']]
    df_ls = df_ls.sort_values(by='Year',ascending=False)
    columns_ls = [{'name':cols,'id':cols} for cols in df_ls.columns]
    data_ls = df_ls.to_dict(orient='records')

    ## Data table for ac top 3
    df_ae_pos = ae_pos_df[ae_pos_df['AC'] == Constituency]
    df_ae_pos = df_ae_pos.drop(columns=['AC'])
     # df_ae_pos = df_ae_pos[["Year","Turnout_Percentage","Electors",'Valid_Votes']]
    df_ae_pos = df_ae_pos.sort_values(by='Year',ascending=False)
    columns_df_ae_pos = [{'name':colls,'id':colls} for colls in df_ae_pos.columns]
    data_df_ae_pos = df_ae_pos.to_dict(orient='records')

    ## Data table for ls top 3
    df_ls_pos = ls_pos_df[ls_pos_df['AC'] == Constituency]
    df_ls_pos = df_ls_pos.drop(columns=['AC'])
      # df_ls_pos = df_ls_pos[["Year","Turnout_Percentage","Electors",'Valid_Votes']]
    df_ls_pos = df_ls_pos.sort_values(by='Year',ascending=False)
    columns_df_ls_pos = [{'name':collls,'id':collls} for collls in df_ls_pos.columns]
    data_df_ls_pos = df_ls_pos.to_dict(orient='records')

    ## Data table for pot
    df_pot = pot_df[pot_df['AC'] == Constituency]
    df_pot = df_pot.drop(columns=['AC'])
      # df_ls_pos = df_ls_pos[["Year","Turnout_Percentage","Electors",'Valid_Votes']]
    columns_df_pot = [{'name':i,'id':i} for i in df_pot.columns]
    data_df_pot = df_pot.to_dict(orient='records')

    ## Data table for issues
    df_issues = issues_df[issues_df['AC'] == Constituency]
    df_issues = df_issues.drop(columns=['AC'])
    # # df_ls_pos = df_ls_pos[["Year","Turnout_Percentage","Electors",'Valid_Votes']]
    columns_df_issues = [{'name':ii,'id':ii} for ii in df_issues.columns]
    data_df_issues = df_issues.to_dict(orient='records')
    
    ## Data table for intro
    df_intro = intro_df[intro_df['AC'] == Constituency]
    df_intro = df_intro.drop(columns=['AC'])
    # df_ls_pos = df_ls_pos[["Year","Turnout_Percentage","Electors",'Valid_Votes']]
    columns_df_intro = [{'name':iii,'id':iii} for iii in df_intro.columns]
    data_df_intro = df_intro.to_dict(orient='records')
    

    ## Always put data first and then columns
    return data,columns,data_ls,columns_ls,data_df_ae_pos,columns_df_ae_pos,data_df_ls_pos,columns_df_ls_pos,data_df_pot,columns_df_pot,data_df_issues,columns_df_issues,data_df_intro,columns_df_intro
    
@app.callback(
    Output('pie_caste', 'figure'),
    [Input('AC','value')]
)
def update_graph(Const):
    df_cas = caste_df[caste_df['AC'] == Const]

    piechart=px.pie(
            data_frame=df_cas,
            names='Caste',
            values='Number',
            hole=.3,
            )
    return (piechart)

@app.callback(
    Output('bar_supp', 'figure'),
    [Input('AC','value')]
)
def update_support(Cons):
    df_supp = support_df[support_df['AC'] == Cons]

    barchart=px.bar(
            data_frame=df_supp,
            x='Candidate',
            y='Number',
            color='Caste',
            text='Number',            
            opacity=0.9,
            orientation='v',
            barmode='relative',
            # width=400
            )
    return (barchart)

# @app.callback(
#     Output('output_container', 'children'),
#     [Input('AC','value')]
# )

# def update_figure(con):
#         df_booth = booth_df[booth_df['AC'] == con]
#         df_boot = df_booth[df_booth['Party']=='BJP']
#         df_boo = df_boot.loc[df_boot['PS VoteShare']>0.7]

#         count = len(df_boo)
#         container = "The number of booths where BJP got more than 70% votes in 2018 are: {}".format(count)

#         return container


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=True)