def Intent_clasification(utterance='How to go to university'):
    

    results = {
        'text':utterance,
        'values':{
            'value_1':{
                'class':'entry_info',
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
