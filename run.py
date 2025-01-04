from app import app_init
from dotenv import load_dotenv

load_dotenv()

app = app_init()

if __name__ == '__main__':
    app.run(debug=True)