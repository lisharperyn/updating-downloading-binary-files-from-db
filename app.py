try:
    from flask import Flask, request, redirect, url_for, render_template, send_file, flash, jsonify
    from flask_wtf import FlaskForm
    from wtforms import FileField, SubmitField
    from wtforms.validators import DataRequired
    from mysql_db_connection import insert_data_to_db, download_data_from_db, fetch_filenames_from_db
    import os
    from io import BytesIO

    print("All modules loaded!")

except:

    print('Some modules are missing...')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


class UploadForm(FlaskForm):
    file = FileField('File', validators=[DataRequired()])
    submit = SubmitField('Enviar')


# CREATE
@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()

    if request.method == 'POST' and form.validate_on_submit():
        file = form.file.data
        file_name = file.filename    # Obtendo o nome do arquivo
        file_content = file.read()    # Lendo o conteúdo do arquivo

        insert_data_to_db(file_name, file_content)    # Passando o nome e o conteúdo do arquivo para a função

        return redirect(url_for('index'))
    return render_template('home.html', form=form)


# Exemplo da função create()
"""
@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()

    if request.method == 'POST' and form.validate_on_submit():
        file = form.file.data
        file_name = file.filename
        file_content = file.read()

        create(file_name, file_content)

        return redirect(url_for('index'))
    return render_template('home.html', form=form)
"""


# READ
@app.route('/download', methods=['GET'])
def download():
    file_name = request.args.get('file_name')

    if not file_name:
        flash('O nome do arquivo é obrigatório')
        return redirect(url_for('index'))

    file_content = download_data_from_db(file_name)

    if file_content:
        return send_file(BytesIO(file_content), download_name=file_name, as_attachment=True)
    else:
        flash('Arquivo não encontrado')
        return redirect(url_for('index'))


# Rota para exibir lista de sugestão de arquivos
@app.route('/suggest', methods=['GET'])
def suggest():
    term = request.args.get('term', '')
    print(f"Search term: {term}")  # Log para depuração
    suggestions = fetch_filenames_from_db(term)
    print(f"Suggestions: {suggestions}")  # Log para depuração
    return jsonify(suggestions)


if __name__ == '__main__':
    app.run(debug=True)
