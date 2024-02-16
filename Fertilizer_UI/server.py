from flask import Flask, request, render_template
import pickle
import warnings
warnings.filterwarnings("ignore")

# load the model
# with open('../../models/cb.pkl', 'rb') as file:
#with open('/home/user/Downloads/Precision_farming_final/Fertilizer.pkl', 'rb') as file:
with open('/home/user/Documents/Project_PF/Fertilizer_UI/Fertilizer.pkl', 'rb') as file:
    model = pickle.load(file)


# create a flask application
app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    # read the file contents and send them to client
    return render_template('index.html')


@app.route("/classify", methods=["POST"])
def classify():
    # get the values entered by user
    print(request.form)
    T = float(request.form.get("T"))
    H = float(request.form.get("H"))
    R = float(request.form.get("R"))
    pH = float(request.form.get("pH"))
    N = float(request.form.get("N"))
    P = float(request.form.get("P"))
    K= float(request.form.get("K"))
    Soil = float(request.form.get("soil"))
    Crop = float(request.form.get("crop"))

    output = model.predict([
        [T, H, R, pH, N, P, K, Soil, Crop]])

    d = {'DAP and MOP': 1, 'Good NPK' : 2, 'MOP' : 3, 'Urea and DAP': 4, 'Urea and MOP': 5,'Urea': 6, 'DAP': 7}


    for i in d.values():
        if output == i:
            keys = [k for k, i in d.items() if i == output]
    return "Recommended fertilizer : ", keys[0].upper()


# start the application
app.run(host="0.0.0.0", port=8000, debug=True)

