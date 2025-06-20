'''
requirements:
tensorflow==2.3
'''
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Load Huggingface transformers
from transformers import BertTokenizer,  BertTokenizerFast, TFBertModel,TFAutoModel, TFAlbertModel

# Then what you need from tensorflow.keras
from tensorflow.keras.layers import Input, Dropout, Dense, GlobalAveragePooling1D
from tensorflow.keras.models import Model


# We don't use GPU
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# home
def home(request):
    return render(request, "app_sentiment_bert/home.html")

# api get sentiment score
@csrf_exempt
def api_get_sentiment(request):
    
    new_text = request.POST.get('input_text')
    #new_text = request.POST['input_text']
    print(new_text)

    # See the content_type and body從前端送過來的資料格式
    print(request.content_type)
    print(request.body) # byte format

    sentiment_prob = get_sentiment_proba(new_text)

    return JsonResponse(sentiment_prob)



def load_cutom_classifier_model(bert):
    # Max length of tokens
    # Make the length of every document equal to 250
    # 每個評論必須長度一致 最多為250個字詞 Padding(文章填塞變成長度一樣)
    # 文件若較長，必須放大一些 最長為512
    max_length = 250

    # Define our model's input format
    input_ids = Input(shape=(max_length,), name='input_ids', dtype='int32')
    attention_mask = Input(shape=(max_length,), name='attention_mask', dtype='int32') 
    inputs = {'input_ids': input_ids, 'attention_mask': attention_mask}

    g = bert(inputs)
    g = GlobalAveragePooling1D(name='global_pooling')(g.last_hidden_state) #g[0]
    g = Dropout(0.1)(g)
    g = Dense(128, activation='relu', name='dense_output')(g)
    g = Dropout(0.2)(g)
    # output layer
    out_sentiment = Dense(2, activation='softmax', name='sentiment')(g)
    # Construct our custom model
    model = Model(inputs=inputs, outputs=out_sentiment)
    return model


pretrained_bert_path='ckiplab/albert-tiny-chinese'
# Load Bert model
bert = TFAlbertModel.from_pretrained(pretrained_bert_path, from_pt=True)
model = load_cutom_classifier_model(bert)
## Load best trained weights
# best_weights_name='best_model/best-albert-tiny-weights.h5'
#best_weights_name='app_sentiment_bert/model_bert/best-albert-tiny-weights.h5'
best_weights_name='app_sentiment_bert/model_bert/best-model-weights-v1.h5'
#best_weights_name='app_sentiment_bert/model_bert/albert-tiny-model_v1.h5'
model.load_weights(best_weights_name)

# Step 2: Load tokenizer
# pretrained_bert_path='bert-base-chinese' # the same
tokenizer = BertTokenizer.from_pretrained(pretrained_bert_path) 


def preprocessing_for_bert(input_sentences):
    result = tokenizer(
        text=list(input_sentences),
        add_special_tokens=True,
        max_length=250,  # 文件若較長，必須放大一些 最長為512
        truncation=True,
        #padding=True, 
        padding='max_length',
        return_tensors='tf',
        return_token_type_ids = False,
        return_attention_mask = True,
        verbose = True)

    return result
# Step 3: Define prediction function 
# get sentiment probability
def get_sentiment_proba( text ):
    X_data = preprocessing_for_bert([text])
    X_newText = {'input_ids': X_data['input_ids'], 'attention_mask': X_data['attention_mask']}
    result = model.predict(X_newText)
    # print(result)
    response = {'Negative': round(float(result[0, 0]), 2), 'Positive': round(float(result[0, 1]), 2)}
    # Note that result is numpy format and it should be convert to float
    return response

print("Loading app bert sentiment classification.")
