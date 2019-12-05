#Eduardo Imery
#04-12-2019
#importing libraries for dash
import dash
from dash.dependenies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
#some controller
import managerdb.py


global product_df

product_df = dbm.read()

#Creating the main layout
app.layout = html.Div([
	html.Div([
		html.H1('Price Optimization Dashboard'),
		html.H2('Choose a product name'),
		dcc.Dropdown(
			id ='product-dropdown',




#activating the dash server
app = dash.Dash(__name__)
server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
