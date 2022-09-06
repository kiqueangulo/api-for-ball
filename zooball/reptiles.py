from flask import (Blueprint, request, redirect)
from . import models

bp = Blueprint('reptiles', __name__, url_prefix = '/reptiles')

@bp.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        common_name = request.form['common_name']
        scientific_name = request.form['scientific_name']
        conservation_status = request.form['conservation_status']
        native_habitat = request.form['native_habitat']
        fun_fact = request.form['fun_fact']

        new_reptile = models.Reptile(
            common_name = common_name,
            scientific_name = scientific_name,
            conservation_status = conservation_status,
            native_habitat = native_habitat,
            fun_fact = fun_fact)

        models.db.session.add(new_reptile)
        models.db.session.commit()

        print('Added successfully')

        return redirect('/reptiles')
    
    query_reptiles = models.Reptile.query.all()
    all_reptiles = [{
        "_id": reptile.id,
        "common_name": reptile.common_name,
        "scientific_name": reptile.scientific_name,
        "conservation_status": reptile.conservation_status,
        "native_habitat": reptile.native_habitat,
        "fun_fact": reptile.fun_fact
    } for reptile in query_reptiles]

    return all_reptiles

@bp.route('/<int:id>')
def show_reptile(id):
    reptile = models.Reptile.query.filter_by(id = id).first()

    return {
        "_id": reptile.id,
        "common_name": reptile.common_name,
        "scientific_name": reptile.scientific_name,
        "conservation_status": reptile.conservation_status,
        "native_habitat": reptile.native_habitat,
        "fun_fact": reptile.fun_fact
    }