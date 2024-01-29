from flask import Flask,request
from youtube_transcript_api import YouTubeTranscriptApi
from transformers  import pipeline

app=Flask(__name__)

@app.get("/summary")
def summary_api():
    url=request.args.get('url','')
    video_id=url.split('=')[1]
    summary=get_Summary(get_transcript(video_id))
    return summary,200


def get_transcript(video_id):
    transcript_list=YouTubeTranscriptApi.get_transcript(video_id,languages=['en','en-GB'])
    transcript=''.join([d['text'] for d in transcript_list])
    print(r"""
          
          
          
___________   ___.            __________                                ____    _______   
\__    ___/_ _\_ |__   ____   \______   \ ____   ____ _____  ______    /_   |   \   _  \  
  |    | |  |  \ __ \_/ __ \   |       _// __ \_/ ___\\__  \ \____ \    |   |   /  /_\  \ 
  |    | |  |  / \_\ \  ___/   |    |   \  ___/\  \___ / __ \|  |_> >   |   |   \  \_/   \
  |____| |____/|___  /\___  >  |____|_  /\___  >\___  >____  /   __/    |___| /\ \_____  /
                   \/     \/          \/     \/     \/     \/|__|             \/       \/ 

        
        
        
                        
          
          
          
          
          
          
          
          
          """)
    print("+++++++++++++++++++++++++++++||TRANSCRIPT||+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(transcript)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    return transcript

def get_Summary(transcript):
    summarizer =pipeline("summarization", model="facebook/bart-large-cnn")
    summary=''
    for i in range((len(transcript)//1000)+1):
        summary_text=summarizer(transcript[i*1000:(i+1)*1000])[0]['summary_text']
        summary=summary+summary_text+' '
    return summary

if __name__=="__main__":
    app.run(debug=True)