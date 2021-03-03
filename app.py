"""
testing hosting on heroku
"""

import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash(__name__)
server = app.server()

app.layout = html.Div(
    [
        "How casual are we talking?",
        dcc.Slider(min=0, max=5, value=2, marks={0: "0", 5: "5"}),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
