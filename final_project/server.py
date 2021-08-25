from machinetranslator import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    print(textToTranslate)
    french_output = translator.english_to_french(textToTranslate)
    print(french_output)
    return render_template('englishToFrench.html', variable = french_output)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    english_output = translator.french_to_english(textToTranslate)
    return render_template('frenchToEnglish.html', variable = english_output)

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
