from core import create_app

from core.db import db

application = create_app()

# Setup database
@application.before_first_request
def initialize_database():
    db.create_all()

def serve():
    return application

if __name__ == '__main__':
    application.run(debug=True)
