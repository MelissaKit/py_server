# from flask import Flask, render_template, abort, request, jsonify
# from flask_cors import CORS

# from dostoevsky.tokenization import RegexTokenizer
# from dostoevsky.models import FastTextSocialNetworkModel

# import pickle
# import pandas as pd


# app = Flask(__name__)


# def getApp():
#     return app


# CORS(app)

# def sentiment(sentence):
#     tokenizer = RegexTokenizer()
#     model = FastTextSocialNetworkModel(tokenizer=tokenizer)
#     messages = [sentence]
#     results = model.predict(messages, k = 2)

#     for message, sentiment in zip(messages, results):
#         print(message, '->', sentiment)
#         return sentiment


# def category(text):
#     filename = 'posts_model1.sav'
#     loaded_model = pickle.load(open(filename, 'rb'))

#     data = {'Post_clean' : text}
#     s = pd.Series(data)

#     predicted_sgd = loaded_model.predict(s)

#     return predicted_sgd[0]

# @app.route("/sentiment/", methods = ["GET","POST"])
# def sentimentRequest():
#     print('sentimental')
#     if request.method == "POST":
#         print('post')
#         sentence = request.form['q']
#         sent = sentiment(sentence)
#         return sent
#     else:
#         print('get')
#         sentence = request.args.get('q')
#         sent = sentiment(sentence)
#         return sent


# @app.route("/category/", methods = ["GET","POST"])
# def blaRequest():
#     print('category')
#     output = {}
#     if request.method == "POST":
#         print('post')
#         sentence = request.form['q']
#         output['category'] = category(sentence)
#         return jsonify(output)
#     else:
#         print('get')
#         sentence = request.args.get('q')
#         output['category'] = category(sentence)
#         print(output['category'])
#         return output

# if __name__ == "__main__":
#     app.run(debug=True)
    
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"