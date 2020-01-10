from flask import Flask
app = Flask('hello-gitops')

@app.route('/')
def hello():
  return "Welcome to Fekete Jozsi gitops !!\n"

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)
