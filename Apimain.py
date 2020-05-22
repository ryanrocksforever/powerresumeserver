from flask import *
import mainwork
app = Flask(__name__)

@app.route('/')
def upload():
	return '<html><head>    <title>upload</title></head><body><form action = "/success" method = "post" enctype="multipart/form-data">    <input type="file" name="file" />    <input type="text" name="percentage" />    <input type="text" name="bedtemp" />    <input type="text" name="endtemp" />    <input type = "submit" value="Upload"></form></body></html>'

@app.route('/success', methods = ['POST'])
def success():
	if request.method == 'POST':
		f = request.files['file']
		f.save("./temp/" + f.filename)
		content = request.data
		print(content)
		print(f.filename)
		fname = "./temp/" + f.filename
		#content["percentage"], content["bedtemp"], content["endtemp"]
		print(request.values.get("percentage") + " " +  request.values.get("bedtemp") + " " + request.values.get("endtemp"))
		mainwork.creategcodefile(f.filename, request.values.get("percentage"), request.values.get("bedtemp"), request.values.get("endtemp"))

		#subprocess.call(['python', 'mainwork.py', f.filename, request.values.get("percentage"), request.values.get("bedtemp"), request.values.get("endtemp")])
		return send_from_directory("./temp", f.filename, as_attachment=True)
		#return '<html><head>    <title>success</title></head><body><p>File uploaded successfully</p><p>File Name: ' + f.filename + '</p></body></html>', send_from_directory("./temp", f.filename, as_attachment=True)


if __name__ == '__main__':
	app.run(debug = True)
