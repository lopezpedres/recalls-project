














@auth_bp.route('/login', methods= ['GET', 'POST'])
def go_login():
    if current_user.is_authenticated:
        return redirect('index')

    form = LoginForm()
    if form.validate_on_submit():
        user=User.get_by_email(form.email.data)

        if user is None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page= request.args.get(url_for('public.index'))
#Como funciona el next page?! Se que es para darle seguridad a la pagina pe
            if not next_page or url_parse(next_page).netlog !='':
                return redirect('index.html')

    return render_template('auth/login.html', form=form)



