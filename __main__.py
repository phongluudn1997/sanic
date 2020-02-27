from gino.ext.sanic import Gino
from sanic import Sanic
from sanic.response import json


app = Sanic(__name__)
app.config.DB_HOST = 'localhost'
app.config.DB_DATABASE = 'sqlalchemy'
app.config.DB_USER = 'postgres'
app.config.DB_PASSWORD = 'postgres'
app.config.DB_PORT = '5433'

db = Gino()
db.init_app(app)


class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = dict(schema="User")

    id = db.Column(db.Integer(), primary_key=True)
    nickname = db.Column(db.Unicode(), default='none')

    def __str__(self):
        return '{}<{}>'.format(self.nickname, self.id)


@app.route("/users/<user_id>")
async def get_user(request, user_id):
    user = await User.get_or_404(int(user_id))
    return json({'name': user.nickname})


if __name__ == '__main__':
    app.run(debug=True)
