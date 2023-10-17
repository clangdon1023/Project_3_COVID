from flask import Flask, render_template
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_leaflet as dl

app = Flask(__name__)

# Your Dash application
dash_app = dash.Dash(__name__, server=app, url_base_pathname='/dashboard/')

dash_app.layout = html.Div([
    html.H1('Interactive Map Dashboard'),
    dl.Map(id='map', center=[51.505, -0.09], zoom=10, style={'width': '100%', 'height': '400px'}),
])

@dash_app.callback(
    Output('map', 'center'),
    Output('map', 'zoom'),
    Input('map', 'click_lat_lng'),
)
def update_map(click_lat_lng):
    if click_lat_lng:
        return click_lat_lng, 10
    return [51.505, -0.09], 10

# Your Flask route to serve the combined HTML with Dash
@app.route('/')
def index():
    return render_template('index.html', dash_url='/dashboard/')

if __name__ == '__main__':
    app.run(debug=True)
