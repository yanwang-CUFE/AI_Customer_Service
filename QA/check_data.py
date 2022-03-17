import json
with open('CMRC2018/dev.json', 'r') as f:
    content = f.read()
    dev = json.loads(content)
    datas = dev['data']
    for data in datas[:2]:
        paragraphs = data['paragraphs'][0]
        article = paragraphs['context']
        qas = paragraphs['qas']
        for qa in qas:
            question = qa['question']
            answers = qa['answers'][0]['text']
            print("\n",article,"\n----", question,"\n----", answers,"\n")