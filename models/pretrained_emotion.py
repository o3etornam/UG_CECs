from transformers import AutoTokenizer, AutoModelWithLMHead

### emotion detection pretrained model
link = 'mrm8488/t5-base-finetuned-emotion'
tokenizer = AutoTokenizer.from_pretrained(link)
model = AutoModelWithLMHead.from_pretrained(link)

def emotionDetector(text):
    input_ids = tokenizer.encode(text + '</s>', return_tensors='pt')
    output = model.generate(input_ids = input_ids,max_length = 2)
    dec = [tokenizer.decode(ids) for ids in output]
    return dec[0]