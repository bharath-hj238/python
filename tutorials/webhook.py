from flask import Flask,request,json

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Webhooks with Python!'


if __name__ == '__main__':
    app.run(host='localhost', debug=True)


@app.route('/githubIssue', methods=['POST'])
def githubIssue():
    data = request.json
    print(f'Issue {data["issue"]["title"]} {data["action"]}')
    print(f'{data["issue"]["body"]}')
    print(f'{data["issue"]["url"]}')
    return data
  
  
  """
  Commands to be executed:
  $ pythin3 webhook.py  (to start flask server)
  $ sudo ngrok authtoken <TOKEN> (available from the ngrok account login)
  $ sudo ngrok http http://localhost:5000
  """
  
  
