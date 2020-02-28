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
    return json({'name': user.nickname, 'id': user.id})


@app.route('/json', methods=['POST'])
def post_json(request):
    return json({"message": request.json})


@app.route('/query_string', methods=['POST'])
def query_string(request):
    return json({
        "args": request.args,
        "query_args": request.query_args,
        "raw_args": request.raw_args,
        "url": request.url,
        "query_string": request.query_string
    })


@app.route("/files", methods=['POST'])
def another_function(request):
    test_file = request.files.get('test')

    file_parameters = {
        'body': test_file.body,
        'name': test_file.name,
        'type': test_file.type,
    }

    return json({"received": True,
                 "file_names": request.files.keys(),
                 "test_file_parameters": file_parameters})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
