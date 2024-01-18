from flask import Flask, render_template, request,send_file
from pytube import YouTube 
import os 
from moviepy.editor import *

devil=Flask(__name__)

def devil_tube_out(link):
    def devil(name):
        try:
            name_out=(name.split(' -')[1]).split('(')[0]
        except:
            try:
                name_out=name.split('(')[0]
            except:
                name_out=name
        return name_out
    [os.remove(f"static/song/{i}") for i in os.listdir("static/song/")]
    yt=YouTube(link) 
    video=yt.streams.filter(only_audio=True).first() 
    out_file=video.download(output_path="static/song/") 
    name=os.listdir('static/song/')[0]
    video_=AudioFileClip(f"static/song/{name}")
    video_.write_audiofile(f"static/song/{name.split('.')[0]}.mp3")
    return f"{name.split('.')[0]}.mp3"
@devil.route("/mp3_out",methods=['POST','GET'])
def mp3_div():
    if request.method == 'POST':
        return send_file(f"static/song/{request.form['button']}",as_attachment=True)

@devil.route("/link_out",methods=['POST','GET'])
def link_div():
    if request.method == 'POST':
        if request.form['link']!="":
            all_out=request.form.get('link').split(":")
            if all_out[0]!="https":
                return render_template("devil_mp3_in.html",devil="ENTER A VALUED LINK",devil_=None,devil_choice=True)
    devil_angel=devil_tube_out(":".join(all_out))
    return render_template("devil_mp3_in.html",devil_=devil_angel,devil=None,devil_choice=True)

@devil.route("/",methods=['POST','GET'])
def main_div():
    return render_template("devil_mp3_in.html",devil_choice=False)
if __name__ == '__main__':
    devil.run(debug=True)




#f"static/song/{os.listdir('static/song/')[0]}"
#"https://mail.google.com/mail/u/0/"
