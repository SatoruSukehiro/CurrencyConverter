import re
from flask import Flask,redirect,request,render_template,flash
from flask_debug import Debug
from forex_python.converter import CurrencyRates,CurrencyCodes
app = Flask(__name__)
Debug(app)
app.secret_key= 'Hello'
app.run(debug=True)
code=CurrencyCodes()
c = CurrencyRates()
@app.route('/')
def homepage():
    
    return render_template('form.html')

@app.route('/convert')
def getData():
    
    try: 
        curr1 = request.args['currency1']
        curr2 = request.args['currency2']
        amount = request.args['Amount']
        converted = round(c.convert(curr1,curr2,int(amount)),2)
        symbol = code.get_symbol(f'{curr2}')
        
        
        return render_template('converted.html',converted=converted,symbol=symbol)
    except:
        if len(amount) == 0 :
            flash('Sorry We Cant Convert That')
            return render_template('form.html')
        else:
            flash('Currency Code You Input IS INVALID')
            return render_template('form.html')