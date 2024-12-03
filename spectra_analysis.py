from dash import Dash, html, dash_table, dcc
import pandas as pd 
import plotly.express as px

df = pd.read_csv("/home/lme/Spectra_Analysis/example_spectra/7732-18-5-IR(1).csv",sep = "\s" ,names=["Wavenumber","Intensity"])

print(df)

# Normalize the Data
df["Intensity"] = df["Intensity"] / df["Intensity"].max()

print(df["Intensity"])

# This initializes the app
app = Dash()

# This initializes the app_layout
app.layout = [
    html.Div(children='Spectra Visualization'),
    dcc.Graph(figure=px.scatter(y = df["Intensity"],x =df["Wavenumber"]))
]

if __name__ == '__main__':
    app.run(debug=True)

