from app import app, docs, api
from routers import add_routers

add_routers(api, docs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
