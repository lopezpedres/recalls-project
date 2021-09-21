from . import auth_bp
from .models import User
from.forms import LoginForm, SignupForm
import logging
from werkzeug.urls import url_parse
from flask_login import login_user, current_user,logout_user
from app import login_manager
from flask import redirect, request, url_for, render_template


logger = logging.getLogger(__name__)

@auth_bp.route("/")
def go_index():
    logger.info("Getting index page")
    return render_template('auth/index.html')

@auth_bp.route('/login/', methods= ['GET', 'POST'])
def go_login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.go_index'))

    form = LoginForm()
    if form.validate_on_submit():
        user=User.get_by_email(form.email.data)

        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page= request.args.get("next", None)
#Como funciona el next page?! Se que es para darle seguridad a la pagina pe
            if not next_page or url_parse(next_page).netlog !='':
                next_page= url_for('auth.go_index')
                return redirect(next_page)
    return render_template('auth/login.html', form=form)


@auth_bp.route('/signup/', methods=['GET','POST'])
def go_signup():
    form=SignupForm()
    error=None
    if form.validate_on_submit():
        name=form.name.data
        email=form.email.data
        password=form.password.data

        logger.info('Form validated')

        user=User.get_by_email(email)
        if user is not None:
            error=f'La cuenta {email} ya existe.'
        else:
            user=User(name=name, email=email)
            user.set_password(password)
            user.save()
            logger.info('New user created')

            login_user(user, remember=True)
            next_page= request.args.get("next", None)
#Como funciona el next page?! Se que es para darle seguridad a la pagina pe
            if not next_page or url_parse(next_page).netlog !='':
                next_page= url_for('auth.go_index')
                return redirect(next_page)

    return render_template('auth/signup.html', form=form, error=error)

@auth_bp.route('/logout/')
def go_logout():
    logout_user()
    return redirect(url_for('auth.go_index'))    
        
@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)





