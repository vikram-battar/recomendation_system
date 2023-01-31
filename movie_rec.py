from flask import Flask, render_template

from flask import Flask, jsonify, request
from flask_cors import CORS
from App import Recommender

app = Flask(__name__)
CORS(app)
@app.route("/recommend/", methods=['GET'])
def recommend():
    print('Inside Recommend')
    title = request.args.get('title')
    print(title)
    result = Recommender().get_recommendation(title)
    #print(list(result))
    #result_dict = {'Recommended': list(result)}
    return render_template('data.html', result=result)

@app.route("/",methods=['GET'])
def default():
   return render_template('index.html')


if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=False)

