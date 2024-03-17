from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Read data from Excel file
df = pd.read_csv('Cost.Csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_cost_of_living():
    Country = request.form['Country']
    # Filter data for the selected city
    Country_data = df[df['Country'] == Country]
    if not Country_data.empty:
        Country = Country_data['Country'].values[0]
        cost_of_living = Country_data['Cost of Living Index'].values[0]
        rent = Country_data['Rent Index'].values[0]
        groceries_price = Country_data['Groceries Index'].values[0]
        restaurant_price = Country_data['Restaurant Price Index'].values[0]
        local_purchasing_price = Country_data['Local Purchasing Power Index'].values[0]
        return render_template('result.html',
                               Country= Country,
                               cost_of_living=cost_of_living,
                               rent=rent,
                               groceries_price=groceries_price,
                               restaurant_price=restaurant_price,
                               local_purchasing_price=local_purchasing_price)
    else:
        return render_template('error.html', message="Country not found")

if __name__ == '__main__':
    app.run(debug=True)
