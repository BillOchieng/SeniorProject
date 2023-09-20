from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import plotly.express as px
import io

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    plot_div = None

    if request.method == "POST":
        csv_file = request.files["file"]
        if not csv_file:
            return "No file uploaded", 400

        # Read CSV into pandas DataFrame
        df = pd.read_csv(csv_file)

        # For this example, let's just visualize the data in a simple line chart.
        # You can replace this with your specific analysis logic.
        fig = px.line(df)

        # Convert the Plotly graph to HTML div and store it
        plot_div = fig.to_html(full_html=False)

    return render_template("dashboard.html", plot_div=plot_div)


@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return redirect(request.url)
    file = request.files["file"]
    if file.filename == "":
        return redirect(request.url)
    if file:
        data = pd.read_csv(io.StringIO(file.read().decode("utf-8")))
        # Your analysis and trajectory logic here...
        # Return the results...
        pass

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
