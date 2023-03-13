from flask import Flask, render_template, request, url_for, redirect, Markup
from nta_lists import boro_lists
from treedata import nta_table_maker

app = Flask(__name__)

def clean(input):
    return input.strip(",/()")

@app.route('/', methods=["GET", "POST"])
def pick_nta():
    if request.method == "POST":
       # getting input with name = lname in HTML form
       nta_select = clean(request.form.get("Neighborhood"))
       table = nta_table_maker(nta_select, 10)
       return redirect(url_for('results', table=table, nta_select=nta_select))
    return render_template("index.html", boro_lists=boro_lists)

@app.route('/results/')
def results():
    table = Markup(request.args.get('table', None))
    nta_select = request.args.get('nta_select', None)
    return render_template('results.html', table=table, nta_select=nta_select) 

if __name__ == '__main__':
    app.run(debug=True)
