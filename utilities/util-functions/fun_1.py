def course_info(utterance=''):
    if utterance == '':
        #if utterance is empty string
        print('utterance is empty')
        return 'ask another utterance'
    else:
        #function consists one entity
            #ent_PLA
        
        ent_PLA=str()
        
        entities = Entity_extractor(utterance)
        
        for i in range(0, len(entities)):
            
            #entities needs to course_info (bio medical engineering,computer science)
            if entities[i]['ent_data'][2]=='COU':
                ent_PLA = entities[i]['ent_data'][0]
                #pint('COU entity detected')
                #need to complite action from db
                
        if (ent_PLA==''):
            #no intents found
            #two options to choose bme,cs
            #need develop
            return 'options to choose'
        return ent_PLA