import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

df = pd.read_csv('out.csv')

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                dict(
                    x=df[df['versicolor_prob'] == i]['sepal length (cm)_shap'],
                    y=df[df['versicolor_prob'] == i]['sepal length (cm)'],
                    text=df[df['versicolor_prob'] == i]['sepal width (cm)_shap'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.versicolor_prob.unique()
            ],
            'layout': dict(
                xaxis={'type': 'log', 'title': 'versicolor_prob according to shap vs non_shap values'},
                yaxis={'title': 'Sepal length (cm)_shap'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    ),

    dcc.Graph(
        id='sepal width',
        figure={
            'data': [
                dict(
                    x=df[df['versicolor_prob'] == i]['sepal width (cm)_shap'],
                    y=df[df['versicolor_prob'] == i]['sepal width (cm)'],
                    text=df[df['versicolor_prob'] == i]['sepal width (cm)_shap'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.versicolor_prob.unique()
            ],
            'layout': dict(
                xaxis={'type': 'log', 'title': 'versicolor_prob according to shap vs non_shap values'},
                yaxis={'title': 'sepal width (cm)_shap'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    ),
     dcc.Graph(
        id='petal length',
        figure={
            'data': [
                dict(
                    x=df[df['versicolor_prob'] == i]['petal length (cm)_shap'],
                    y=df[df['versicolor_prob'] == i]['petal length (cm)'],
                    text=df[df['versicolor_prob'] == i]['petal width (cm)_shap'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.versicolor_prob.unique()
            ],
            'layout': dict(
                xaxis={'type': 'log', 'title': 'versicolor_prob according to shap vs non_shap values'},
                yaxis={'title': 'petal length (cm)_shap'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    ),
     dcc.Graph(
        id='petal width',
        figure={
            'data': [
                dict(
                    x=df[df['versicolor_prob'] == i]['petal width (cm)_shap'],
                    y=df[df['versicolor_prob'] == i]['petal width (cm)'],
                    text=df[df['versicolor_prob'] == i]['petal width (cm)_shap'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.versicolor_prob.unique()
            ],
            'layout': dict(
                xaxis={'type': 'log', 'title': 'versicolor_prob according to shap vs non_shap values'},
                yaxis={'title': 'petal width (cm)_shap'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    ),
    dcc.Graph(
        id='petal width1',
        figure={
            'data': [
                dict(
                    x=df[df['versicolor_prob'] == i]['sepal length (cm)_shap'],
                    y=df[df['versicolor_prob'] == i]['sepal width (cm)_shap'],
                    text=df[df['versicolor_prob'] == i]['sepal length (cm)_shap'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.versicolor_prob.unique()
            ],
            'layout': dict(
                xaxis={'type': 'log', 'title': 'versicolor_prob'},
                yaxis={'title': 'sepal length (cm)_shap and sepal width (cm)_shap'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    ),
    dcc.Graph(
        id='petal width2',
        figure={
            'data': [
                dict(
                    x=df[df['versicolor_prob'] == i]['petal length (cm)_shap'],
                    y=df[df['versicolor_prob'] == i]['petal width (cm)_shap'],
                    text=df[df['versicolor_prob'] == i]['petal width (cm)_shap'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.versicolor_prob.unique()
            ],
            'layout': dict(
                xaxis={'type': 'log', 'title': 'versicolor_prob'},
                yaxis={'title': 'petal length (cm)_shap and petal width (cm)_shap'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )



])

if __name__ == '__main__':
    app.run_server(debug=True)
