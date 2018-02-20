import getimage
from getimage import get_pics
from flask import Flask, render_template
from shutil import copyfile
app = Flask(__name__)

@app.route("/")
def main():
    # return render_template('index.html')
    items = {}
    items = get_pics('ladiyanos', 'outputvideo.mp4')
    return str(items) + """
    <img src="/static/0.jpg" height="400" width="400">
    <img src="/static/1.jpg" height="400" width="400">
    <img src="/static/2.jpg" height="400" width="400">
    <video id="VideoElement" width="400" height="400" muted controls src="/static/out1.mp4"  type="video/mp4"></video>
    <video id="VideoElement" width="400" height="400" muted controls src="/static/out2.mp4"  type="video/mp4"></video>
    """

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)


