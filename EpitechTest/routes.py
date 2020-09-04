from app import app, db2
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from models.models import *
import forms


# view for landing/login page
@app.route('/', methods=['GET', 'POST'])
@app.route('/landingPage', methods=['GET', 'POST'])
def landingPage():
    formLogin = forms.LoginForm()
    if formLogin.validate_on_submit():
        user = (User.query.filter_by(name=formLogin.name.data)).filter_by(password=formLogin.password.data).first()
        if user:
            return redirect(url_for("library"), user_id=user.id)
        else:
            return redirect(url_for("landingPage"))

    return render_template('landingPage.html', form=formLogin)







# view where the user can register as new user
@app.route('/newUser', methods=['GET', 'POST'])
def newUser():
    formNewUser = forms.NewUserForm()
    if formNewUser.validate_on_submit():
        # encrypt pw if time left
        user = User(name=formNewUser.name.data,
                companyName=formNewUser.companyName.data,
                emailAddress=formNewUser.emailAddress.data,
                telephoneNumber=formNewUser.telephoneNumber.data,
                password=formNewUser.password.data)
        db2.session.add(user)
        db2.session.commit()
        #flash("New User has been added to the database")
        return redirect(url_for("landingPage"))
    return render_template('newUser.html', form=formNewUser)





# view where user can add buisness cards and vew his card library
@app.route('/library/<int:user_id>', methods=['GET', 'POST'])
def library(user_id):
    formCard = forms.AddCard()
    if formCard.validate_on_submit():
        card = Card(name=formCard.name.data,
                companyName=formCard.companyName.data,
                emailAddress=formCard.emailAddress.data,
                telephoneNumber=formCard.telephoneNumber.data,
                user_id=user_id)
        db2.session.add(card)
        db2.session.commit()
        flash("New card successfully added to the database")
        return redirect(url_for("library"), user_id=user_id)

    user = User.query.get(user_id)
    return render_template('library.html', form=formCard, user=user, user_id=user_id)