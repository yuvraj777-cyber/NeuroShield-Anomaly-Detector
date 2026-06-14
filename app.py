from flask import Flask, render_template
import pandas as pd
from sklearn.ensemble import IsolationForest

app = Flask(name)

@app.route("/")
def home():

data = pd.read_csv("sample_logs.csv")

model = IsolationForest(contamination=0.2, random_state=42)

model.fit(data)

data["Prediction"] = model.predict(data)

anomalies = data[data["Prediction"] == -1]

return render_template(
    "index.html",
    tables=[anomalies.to_html(classes="data", index=False)],
    anomaly_count=len(anomalies)
)

if name == "main":
app.run(debug=True)
