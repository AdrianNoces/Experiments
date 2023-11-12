from flask import Flask
from flask import render_template
import jyserver.Flask as jsf



app = Flask(__name__)

@jsf.use(app)

class App:
    def __init__(self):
        self.count = 0
               
       
    def increment(self):
        self.count += 1
        self.js.document.getElementById('count').innerHTML = self.count
        
@app.route('/')

def index():
    return App.render(render_template('index.html'))
    
if __name__ == '__maign__':
    app.run()
    
    
if messanges == recover:
		recover(recover_messages(kert garcia	))
		if recover():
				delete.account():
						with no recover()
						
hack().run() 