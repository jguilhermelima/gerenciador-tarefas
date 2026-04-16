from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Date, Text
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields import DateField
from flask_ckeditor import CKEditor, CKEditorField
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
ckeditor = CKEditor(app)
Bootstrap5(app)

class Base(DeclarativeBase):
    pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tarefas.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Tarefa(db.Model):
    id: Mapped[int] =  mapped_column(Integer, primary_key=True)
    titulo: Mapped[str] =  mapped_column(String(250), nullable=False)
    prioridade: Mapped[int] = mapped_column(Integer, nullable=False)
    comentario: Mapped[str] = mapped_column(Text)
    data: Mapped[Date] = mapped_column(Date, nullable=False)

with app.app_context():
    db.create_all()

class AddForm(FlaskForm):
    titulo = StringField("Title", validators=[DataRequired()])
    prioridade = SelectField(u"Prioridade", choices=[(1, "Urgente"), (2, "Normal"), (3, "Baixa")])
    comentario = CKEditorField("Detalhes Tarefa", validators=[DataRequired()])
    data =  DateField("Data", format="%Y-%m-%d")
    submit = SubmitField("Salvar")

def clean_comentario(comentario):
    comentario = comentario[3:-6]
    return comentario

@app.route("/")
def home():
    result = db.session.execute(db.select(Tarefa).order_by(Tarefa.data)).scalars().all()
    tarefas = result

    return render_template("index.html", tarefas=tarefas)

@app.route("/add", methods=['GET', 'POST'])
def new_todo():
    form = AddForm()
    if form.validate_on_submit():
        comentario = clean_comentario(form.comentario.data)
        new_todo = Tarefa(
            titulo=form.titulo.data,
            prioridade=form.prioridade.data,
            comentario=comentario,
            data=form.data.data
        )
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("new-todo.html", form=form)

@app.route("/edit-tarefa/<int:tarefa_id>", methods=['GET', 'POST'])
def edit_tarefa(tarefa_id):
    tarefa = db.get_or_404(Tarefa, tarefa_id)
    edit_form = AddForm(
        titulo=tarefa.titulo,
        prioridade=tarefa.prioridade,
        comentario=tarefa.comentario,
    )

    if edit_form.validate_on_submit():
        tarefa.titulo = edit_form.titulo.data
        tarefa.prioridade = edit_form.prioridade.data
        comentario = clean_comentario(edit_form.comentario.data)
        tarefa.comentario = comentario
        tarefa.data = edit_form.data.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("new-todo.html", form=edit_form, is_edit=True)

@app.route("/delete-tarefa/<int:tarefa_id>", methods=['GET', 'POST'])
def delete_tarefa(tarefa_id):
    tarefa = db.get_or_404(Tarefa, tarefa_id)
    db.session.delete(tarefa)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True, port=5003)