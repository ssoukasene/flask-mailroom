import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor, DoesNotExist

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

@app.route('/add_donation/', methods=['GET','POST'])
def add_donation():
    if request.method == 'POST':
        donor = request.form['donor']
        if donor == '':
            return render_template("add_donation.jinja2", error="The Donor Name cannot be blank")
        try:
            add_donation = float(request.form['donation'])
        except:
            return render_template("add_donation.jinja2", error="Please enter a valid amount")
        if add_donation <= 0:
            return render_template("add_donation.jinja2", error="Please enter a valid amount")
        try:
            donor_id = Donor.get(Donor.name == donor).id
        except DoesNotExist:
            donor_id = Donor.create(name=donor).id
        finally:
            Donation.create(value=add_donation, donor=donor_id)
            return redirect(url_for('all'))

    else:
        return render_template("add_donation.jinja2")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

