from flask import render_template, request, send_file
from app import app
from app.utils import download_youtube_video, download_tiktok_video

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        platform = request.form["platform"]
        output_path = "downloaded_video.mp4"
        
        if platform == "youtube":
            download_youtube_video(url, output_path)
        elif platform == "tiktok":
            download_tiktok_video(url, output_path)
        
        return send_file(output_path, as_attachment=True)
    return render_template("index.html")