from flask import session
from .send_emails import send_emails
from ..entity_extractor import Entity_extractor


def reg_event(utterance,mycursor,db_connection):
	
	#updating session 
	#function consists one entity EVT
    if session['ses_validate']['entities']==None:
        print('begining reg event',session['ses_validate'])
        session['ses_validate']['entities']={
            'EVT':None,'PSL':None
            }
        print("after 1 update",session['ses_validate'])
    #session['ses_validate']['entities']={'EVT':None}
    print('..................',session['ses_validate'])
	
	#ent_PLA        
    ent_EVT=str()
    ent_EVT_ls=[]
    ent_PSL=str()
    ent_PSL_ls=[]
    entities = Entity_extractor(utterance)
    
    if session['ses_validate']['entities']['EVT']==None:
      #print('getting to the evt')
      if len(entities)>0:
          for i in range(0, len(entities)):
            #print('getting to for loop')

                #entities needs to reg_event:events (robotic day, invention day)
            if entities[i]['ent_data'][2]=='EVT':
              ent_EVT = entities[i]['ent_data'][0]
              ent_EVT_ls.append(entities[i])

              #print(ent_EVT_ls)
              print('EVT entity detected')
          if len(ent_EVT_ls)==1:
                if ent_EVT == 'rbd':
                    #session update for entity
                    session['ses_validate']['entities']['EVT']='rbd'
                   
                elif ent_EVT == 'ine':
                    #session update for entity
                    session['ses_validate']['entities']['EVT']='ine'

                    
          else:
                response = {'fun_res':{
                        'is_completed':False,
                        'content':'Tell me, which event do you like to register ?',
                        'is_option':False,
                        'is_entity':True,
                        'options':None,
                        'entities':['Robotics Day','Invention Exhibition']}}
                #return to choose intent
                session['ses_validate']['understand']-=1
                return response
            
    if session['ses_validate']['entities']['PSL']==None:
        if len(entities)>0:
            for i in range(0, len(entities)):

                #entities needs to reg_event:reg num (S***)
                if entities[i]['ent_data'][2]=='PSL':
                    ent_PSL = entities[i]['ent_data'][0]
                    ent_PSL_ls.append(entities[i])

                    #print(ent_PSL_ls)
                    #pint('EVT ent_PSL detected')
            if len(ent_PSL_ls)==1:
                if ent_PSL == 'rg':
                    #session update for entity
                    session['ses_validate']['entities']['PSL']=ent_PSL_ls[0]['ent_data'][1]                   
            else:
                print('8989898989',session['ses_validate'])
                response = {'fun_res':{
                        'is_completed':False,
                        'content':'Tell me your student registration number ?',
                        'is_option':False,
                        'is_entity':True,
                        'options':None,
                        'entities':None}}
                #return to choose intent
                session['ses_validate']['understand']-=1
                return response
        
    if session['ses_validate']['entities']['PSL'] !=None and session['ses_validate']['entities']['EVT']!=None:
        
        #checking the registered evt
        if session['ses_validate']['entities']['EVT']=='ine':
        #function success
            try:
                #getting student email adress from db
              #print("registraion number is :",session['ses_validate']['entities']['PSL'])
              reg=session['ses_validate']['entities']['PSL']
              sql_q_email ="""select email from students where reg_no= %s """
              mycursor.execute(sql_q_email,(str(reg),)) 
              myresult = mycursor.fetchall()
              std_email=myresult[0][0]
              #print(std_email)

                #API calling to send email
              send_email=send_emails(std_email,'Invention Exhibition',session['ses_validate']['entities']['PSL'])

              if send_email==1:
                  #print("1")
                    #db query-sent email 1
                  sql_q_insert_db ="""insert into event_registrations values('Invention Exhibition',%s,1,0)"""
                  mycursor.execute(sql_q_insert_db,(str(reg),))
                  db_connection.commit()
                  
                    #response registered sucess email send success
                    
                  #generating and return response with successs status
                  response = {'fun_res':{
                        		'is_completed':True,
                        		'content':'Okay.. Successfully registered '+session['ses_validate']['entities']['PSL']+' to Invention Exhibition. Please check confirmation email sent by Demo University for more details.',
                        		'is_option':False,
                        		'is_entity':False,
                        		'options':None,
                        		'entities':['EVT','PSL']}}
                  return response
              else :
                    #db query sent email 0
                  #print("0")
                    #response registered success email sent fail
                  sql_q_insert_db ="""insert into event_registrations values('Invention Exhibition',%s,0)"""
                  mycursor.execute(sql_q_insert_db,(str(reg),))
                  db_connection.commit()
                    #generating and return response with successs status
                  response = {'fun_res':{
                        'is_completed':True,
                        'content':'Okay.. Successfully registered '+session['ses_validate']['entities']['PSL']+' to Invention Exhibition. But We cannot send confirmation email to your email address because of some internal or external issues. Please contact administrator for more details through (+94) 123456',
                        'is_option':False,
                        'is_entity':False,
                        'options':None,
                        'entities':['EVT','PSL']}}
                  return response
            except:
                #generate response for not success registered
                
                #print("1")
                response = {'fun_res':{
							'is_completed':True,
							'content':'Sorry.. I can not register you.. please contact adminstrator for more information through (+94) 123456',
							'is_option':False,
							'is_entity':False,
							'options':None,
							'entities':['EVT','PSL']}}
                return response
        
        elif session['ses_validate']['entities']['EVT']=='rbd':
            #function success
            try:
                #getting student email adress from db
              #print("registraion number is :",session['ses_validate']['entities']['PSL'])
              reg=session['ses_validate']['entities']['PSL']
              sql_q_email ="""select email from students where reg_no= %s """
              mycursor.execute(sql_q_email,(str(reg),)) 
              myresult = mycursor.fetchall()
              std_email=myresult[0][0]
              #print(std_email)

                #API calling to send email
              send_email=send_emails(std_email,'Robotics Day',session['ses_validate']['entities']['PSL'])

              if send_email==1:
                  #print("1")
                    #db query-sent email 1
                  sql_q_insert_db ="""insert into event_registrations values('Robotics Day',%s,1)"""
                  mycursor.execute(sql_q_insert_db,(str(reg),))
                  db_connection.commit()
                  
                    #response registered sucess email send success
                    
                  #generating and return response with successs status
                  response = {'fun_res':{
                        		'is_completed':True,
                        		'content':'Okay.. Successfully registered '+session['ses_validate']['entities']['PSL']+' to Robotics Day. Please check confirmation email sent by Demo University for more details.',
                        		'is_option':False,
                        		'is_entity':False,
                        		'options':None,
                        		'entities':['EVT','PSL']}}
                  return response
              else :
                    #db query sent email 0
                  #print("0")
                    #response registered success email sent fail
                  sql_q_insert_db ="""insert into event_registrations values('Robotics Day',%s,0,1)"""
                  mycursor.execute(sql_q_insert_db,(str(reg),))
                  db_connection.commit()
                    #generating and return response with successs status
                  response = {'fun_res':{
                        'is_completed':True,
                        'content':'Okay.. Successfully registered '+session['ses_validate']['entities']['PSL']+' to Robotics Day. But We cannot send confirmation email to your email address because of some internal or external issues. Please contact administrator for more details through (+94) 123456',
                        'is_option':False,
                        'is_entity':False,
                        'options':None,
                        'entities':['EVT','PSL']}}
                  return response
            except:
                #generate response for not success registered
                
                #print("1")
                response = {'fun_res':{
							'is_completed':True,
							'content':'Sorry.. I can not register you.. please contact adminstrator for more information through (+94) 123456',
							'is_option':False,
							'is_entity':False,
							'options':None,
							'entities':['EVT','PSL']}}
                return response
            
            
            
            
            
            
        else:
            print('Error occured event_reg')
    if (ent_EVT==''):
		#no entity found
		#return to choose intent
        response = {'fun_res':{
					'is_completed':False,
					'content':'Currently we have Robotics day and Inovation exhibtion, tell me.. which event do you like to register ?',
					'is_option':False,
					'is_entity':True,
					'options':None,
					'entities':['Robotics Day','Invention Exhibition']}}
		#two options
        session['ses_validate']['understand']-=1
        print(session['ses_validate']['understand'])
        return response
		
		 
