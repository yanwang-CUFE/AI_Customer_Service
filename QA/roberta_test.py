from transformers import AutoModelForQuestionAnswering,AutoTokenizer,pipeline
import json
from collections import Counter

model = AutoModelForQuestionAnswering.from_pretrained('luhua/chinese_pretrain_mrc_roberta_wwm_ext_large')
tokenizer = AutoTokenizer.from_pretrained('luhua/chinese_pretrain_mrc_roberta_wwm_ext_large')
QA = pipeline('question-answering', model=model, tokenizer=tokenizer)

# QA_input = {'question': "著名诗歌《假如生活欺骗了你》的作者是",'context': "普希金从那里学习人民的语言，吸取了许多有益的养料，这一切对普希金后来的创作产生了很大的影响。这两年里，普希金创作了不少优秀的作品，如《囚徒》、《致大海》、《致凯恩》和《假如生活欺骗了你》等几十首抒情诗，叙事诗《努林伯爵》，历史剧《鲍里斯·戈都诺夫》，以及《叶甫盖尼·奥涅金》前六章。"}
# print(QA(QA_input))
# --------------------------
# input:  dict {'question' , 'context'}
# output:  dcit{'score', 'start', 'end', 'answer'}

test_dict = ["trial","train", "dev", "test"]
test_id = 3
tot_num, EM_num, tot_f1 = 0, 0, 0

with open('CMRC2018/{}.json'.format(test_dict[test_id]), 'r') as f:
    content = f.read()
    dev = json.loads(content)
    datas = dev['data']
    for data in datas:
        paragraphs = data['paragraphs'][0]
        article = paragraphs['context']
        qas = paragraphs['qas']
        for qa in qas:
            question = qa['question']
            ans_len = len(qa['answers'])
            answers = [qa['answers'][i]['text'] for i in range(ans_len)]
            if question:
                QA_input = {'question': question, 'context': article}
                QA_output = QA(QA_input)
                tot_num += 1
                idx = 0
                for i in range(ans_len):
                    if QA_output['answer'] == answers[i]:
                        EM_num += 1
                        idx = i
                        break
                out_char = Counter(QA_output['answer'])
                label_char = Counter(answers[idx])
                inter = out_char & label_char
                precision = sum(inter.values()) / sum(out_char.values())
                recall = sum(inter.values()) / sum(label_char.values())
                if recall + precision==0:
                    f1 = 0
                else:
                    f1 = 2*recall*precision / (recall + precision)
                tot_f1 += f1
                # print("answers", answers)
                # print("out_answers", QA_output['answer'])
                print("F1", f1)
                # print("---")

    print(EM_num / tot_num)
    print(tot_f1 / tot_num)