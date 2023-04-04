from flask import Flask , render_template ,request
from app.utils import Heart_prediction
import CONFIG

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict",methods=["GET","POST"])
def load_raw():
    data = request.form
    pred_obj = Heart_prediction()
    predict_disease = pred_obj.predict_result(data)
    print(predict_disease)

    return render_template("index.html",result = predict_disease)

if __name__ == "__main__":
    app.run(host=CONFIG.HOST,port=CONFIG.PORT,debug=CONFIG.DEBUGE)
