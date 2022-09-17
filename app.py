from src import create_app

application = create_app()

def serve():
    return application

if __name__ == '__main__':
    application.run(debug=True)
