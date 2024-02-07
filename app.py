import Flask

app = Flask(__name__)

if __name__ == "-__main__":
    app.run()
    
@app.route("/")
def home_page():
    return "Hello", 200