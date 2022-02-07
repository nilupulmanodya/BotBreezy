import spacy
from spacy.lang.en import English

nlp = English()
ruler = nlp.add_pipe("entity_ruler")

patterns = [{"label": "FAC", "pattern": [{"LOWER":"engineering"}], "id": "foe"},
            {"label": "FAC", "pattern": [{"LOWER":"eng"}], "id": "foe"},
            {"label": "FAC", "pattern": [{"LOWER":"foe"}], "id": "foe"},
            {"label": "FAC", "pattern": [{"LOWER": "computing"}], "id": "foc"},
            {"label": "FAC", "pattern": [{"LOWER": "com"}], "id": "foc"},
            {"label": "FAC", "pattern": [{"LOWER": "foc"}], "id": "foc"},
           
            {"label": "COU", "pattern": [{"LOWER":"computer"},{"LOWER":"science"}], "id": "ccs"},
            {"label": "COU", "pattern": [{"LOWER":"computer"},{"LOWER":"sci"}], "id": "ccs"},
            {"label": "COU", "pattern": [{"LOWER":"com"},{"LOWER":"sci"}], "id": "ccs"},
            {"label": "COU", "pattern": [{"LOWER":"cs"}], "id": "ccs"},
            {"label": "COU", "pattern": [{"LOWER":"computerscience"}], "id": "ccs"},
            {"label": "COU", "pattern": [{"LOWER": "bio"},{"LOWER":"medical"},{"LOWER":"engineering"}], "id": "cbme"},
            {"label": "COU", "pattern": [{"LOWER": "bme"}], "id": "cbme"},
            {"label": "COU", "pattern": [{"LOWER": "b"},{"LOWER":"m"},{"LOWER":"e"}], "id": "cbme"},
            {"label": "COU", "pattern": [{"LOWER": "bio"},{"LOWER":"med"},{"LOWER":"eng"}], "id": "cbme"},
            {"label": "COU", "pattern": [{"LOWER": "biomedicalengineering"}], "id": "cbme"},
           
            {"label": "PLA", "pattern": [{"LOWER":"lec1"}], "id": "l1"},
            {"label": "PLA", "pattern": [{"LOWER":"lec"},{"LOWER":"1"}], "id": "l1"},
            {"label": "PLA", "pattern": [{"LOWER":"l1"}], "id": "l1"},
            {"label": "PLA", "pattern": [{"LOWER":"lec2"}], "id": "l2"},
            {"label": "PLA", "pattern": [{"LOWER":"lec"},{"LOWER":"2"}], "id": "l2"},
            {"label": "PLA", "pattern": [{"LOWER":"l2"}], "id": "l2"},
            {"label": "PLA", "pattern": [{"LOWER": "auditorium"}], "id": "aud"},
            {"label": "PLA", "pattern": [{"LOWER": "aud"}], "id": "aud"},
            {"label": "PLA", "pattern": [{"LOWER": "audi"}], "id": "aud"},
            {"label": "PLA", "pattern": [{"LOWER": "ground"}], "id": "grd"},
            {"label": "PLA", "pattern": [{"LOWER": "grd"}], "id": "grd"},
            {"label": "PLA", "pattern": [{"LOWER": "grnd"}], "id": "grd"},
           
            {"label": "EVT", "pattern": [{"LOWER":"robotics"},{"LOWER":"day"}], "id": "rbd"},
            {"label": "EVT", "pattern": [{"LOWER":"rbt"},{"LOWER":"dy"}], "id": "rbd"},
            {"label": "EVT", "pattern": [{"LOWER":"invention"},{"LOWER":"exhibition"}], "id": "ine"},
            {"label": "EVT", "pattern": [{"LOWER":"inv"},{"LOWER":"exh"}], "id": "ine"},
            {"label": "EVT", "pattern": [{"LOWER":"inven"},{"LOWER":"exh"}], "id": "ine"},
            {"label": "EVT", "pattern": [{"LOWER":"inv"},{"LOWER":"exhibition"}], "id": "ine"},
            {"label": "EVT", "pattern": [{"LOWER":"inventionexhibition"}], "id": "ine"},
            
            {"label": "SPT", "pattern": [{"LOWER":"cricket"}], "id": "cri"},
            {"label": "SPT", "pattern": [{"LOWER":"cri"}], "id": "cri"},
            {"label": "SPT", "pattern": [{"LOWER":"karate"}], "id": "krt"},
            {"label": "SPT", "pattern": [{"LOWER":"karathe"}], "id": "krt"},
            
            
            {"label": "PSL", "pattern": [{"TEXT" : {"REGEX": "(?:S[0-9]..)"}}], "id": "rg"},
            {"label": "PSL", "pattern": [{"ORTH":"S"},{"SHAPE":"ddd"}], "id": "rg"},
            {"label": "PSL", "pattern": [{"ORTH":"s"},{"SHAPE":"ddd"}], "id": "rg"},



           ]

ruler.add_patterns(patterns)

def Entity_extractor(doc_text):
    doc = nlp(doc_text)
    ent_dict={}
    for i in range(0,len(doc.ents)):
        #print(i)
        #print((doc.ents[i].ent_id_, doc.ents[i].text, doc.ents[i].label_))
        ent_dict[i] = {'ent_id':i,
               'ent_data':(doc.ents[i].ent_id_, doc.ents[i].text, doc.ents[i].label_)
               }
    #print([(ent.text, ent, ent.ent_id_) for ent in doc.ents])
    #print(doc.ents[0].ent_id_)
    #print(ent_dict)
    return ent_dict
    
    #print(doc.ents)
'''
return type  dict

{0: {'ent_id': 0, 'ent_data': ('l1', 'lec1', 'PLA')},
 1: {'ent_id': 1, 'ent_data': ('grd', 'ground', 'PLA')},
 .
 .
 .}
'''

