from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def initail():
    return """
    Welcome here idiote
        """
        
if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(port=port)