from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("best_model.pkl")

@app.route("/", methods=["GET", "POST"])
def predict():

    prediction = None

    if request.method == "POST":

        features = [
            float(request.form["OverallQual"]),
            float(request.form["GrLivArea"]),
            float(request.form["GarageCars"]),
            float(request.form["TotalBsmtSF"]),
            float(request.form["FullBath"]),
            float(request.form["BedroomAbvGr"]),
            float(request.form["YearBuilt"])
        ]

        prediction = model.predict([features])[0]

    return render_template(
        "index.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)