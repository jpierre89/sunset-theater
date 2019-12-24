# from app package import app object
from application import app, db


# for flask shell - python interpreter with auto import
# add symbols in dictionary to auto import
#@app.shell_context_processor
#def make_shell_context():
#    return {'db': db}


if __name__ == "__main__":
    app.run(debug=True)
