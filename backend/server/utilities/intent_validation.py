import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer() 
from gensim.models import Word2Vec
import re

import string

def Intent_clasification(vectorizer, gboost_m, transformer, utterance):
    


 ####Preprocessing and cleaning train data
    print('utternce is',utterance)
    process_text=data_cleaning(utterance)       
    intent_vector = vectorizer.transform([process_text[0]])
    
    
    #print(intent_vector)
    intent_vector_data = transformer.transform(intent_vector).toarray()
    predicted_class = gboost_m.predict(intent_vector_data)[0]
    print('pre class',predicted_class)
    d={"12" :"uni_info",
    "1" :"course_info",
    "4" :"faculty_info",
    "11":"staff_info",
    "7":"hostel_info",
    "8":"placesinfo",
    "0" :"career_info",
    "3" :"event_info" ,
    "10":"sports_info",
    "2":"entry_info",
    "9":"reg_event",
    "5":"fillhostelapplication",
    "6":"greetings"}
    t_class =  d[str(predicted_class)]
    print("tclass",t_class)
    

    

    results = {
        'text':utterance,
        'values':{
            'value_1':{
                'class':t_class,
                'value':0.7890
            },
            'value_2':{
                'class':'career_info',
                'value':0.6804
            },
            'value_3':{
                'class':'event_info',
                'value':0.1255
            },
        }
    }
    return results


def Validate_top_class(input_):#input must be formated as results of intent classifier
	#check top intent class based on score
	test_value = 0.05	#different test_score
	
	#identify top intent with accuracy score and wheather decide pass or not
	if((test_value <= abs(input_['values']['value_1']['value']-input_['values']['value_2']['value']))):
		print('values is greater than test value:',test_value)
              
		print(input_['values']['value_1']['value']-input_['values']['value_2']['value'])
        #execute querry for top intent
		return { 'validated_top_class':True,
		'top_class':input_['values']['value_1']['class']
		}
    
	else :
		print('value is less than test value:',test_value)
        #suggesting top 3 classes
		top_three_classes = [input_['values']['value_1']['class'],input_['values']['value_2']['class'],input_['values']['value_3']['class']]
        
        #print(input_['values']['value_1']['value']-input_['values']['value_2']['value'])'''
		print(top_three_classes)
		return { 'validated_top_class':False,
		'top_class':top_three_classes
		}


def data_cleaning(data):
    cleaned_data = []
    fillerWord = ("so","yeah","okay","um","uh","mmm","ahan","uh","huh","ahm","oh","sooo","uh","huh","yeh","yah","hmm","bye")
    fillerword_reg= "bye[.,]|so[.,]|yeah[.,]|okay[.,]|um[.,]|uh[.,]|mmm[.,]|ahan[.,]|uh[.,]|huh[.,]|ahm[.,]|oh[.,]|sooo[.,]|uh[.,]|huh[.,]|yeh[.,]|yah[.,]|hmm[.,]"
    STOPWORDS = set(stopwords.words('english'))
    remove=["doesn't","not","nor","neither","isn't","hadn't","mightn't","needn't","wasn't"]
    for i in remove:
        STOPWORDS.discard(i)
    
    STOPWORDS.add(fillerWord)  
    for i in range(len(data)):
        intent = re.sub("#", "", data[i])#extracting hashtags
        intent = re.sub(r'^https?:\/\/.*[\r\n]*', '',intent, flags=re.MULTILINE)#extracting links
        html=re.compile(r'<.*?>')#extracting html tags
        intent =html.sub(r"", intent)
        #extracting symbols and characters
        intent=re.sub(r'@\w+',"",intent)
        intent=re.sub(r'#\w+',"",intent) 
        intent=re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', intent) 
        punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        intent.rstrip(string.punctuation)
        intent=re.sub('[^A-Za-z\s]+',"", intent)
        intent = intent.lower()
        intent = intent.split()
        #Lemmatization to normalise text
        intent = [lemmatizer.lemmatize(word) for word in intent if not word in STOPWORDS]
        intent = ' '.join(intent)
        filler=re.compile(fillerword_reg)
        intent=filler.sub("",intent)
        cleaned_data.append(intent)
    return cleaned_data