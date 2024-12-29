# 
# app 
#   - project serving application 
# 

# imports
from flask import Flask, render_template, request, flash, url_for, redirect
from .model_deploy import output_model


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # configs
    app.config['SECRET_KEY'] = 'dgrshobfmewkg#%@$TWcvm$^#g'


    # routes
    @app.route('/', methods=['GET', 'POST'])
    def index():
        result = 'null'
        if request.method == 'POST':
            form = request.form
            sample = []
            features = ['length', 'diameter', 'height', 'weight-1', 'weight-2', 'weight-3', 'shell']
            
            sex = form.get('sex')
            if not sex or sex == 'Select Sex':
                flash("sex is required!", "warning")
                return redirect(url_for('index'))

            sample.append(int(sex))

            for feat in features:
                data = form.get(feat)
                if not data:
                    flash(f'{feat} is required!', 'warning')
                    return redirect(url_for('index'))
                
                sample.append(float(data))


            print(sample)
            result = output_model.predict(sample)


        return render_template('index.html', result=result)

    return app
