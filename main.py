from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from fastapi import Form
#from models.pretrained_sentiment import sentimentDetector
#from models.pretrained_emotion import emotionDetector
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
async def welcome(request:Request):
    return templates.TemplateResponse('welcome.html', context={'request':request})
 
@app.post('/analyse') 
async def process_text(text_input: str = Form(...), choice: str = Form(...)):
    return {"input_text": text_input,
            "method": choice} 



if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        reload = True  
    )