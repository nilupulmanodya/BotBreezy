from .funcs import reg_event
#staff_info,hostel_info,uni_info,test,course_info,faculty_info,career_info,event_info,entry_info,reg_event,sports_info,

#dispatcher = { 'staff_info' : staff_info.staff_info,'hostel_info':hostel_info.hostel_info,'uni_info':uni_info.uni_info,'course_info':course_info.course_info,'faculty_info':faculty_info.faculty_info,'career_info':career_info.career_info,'event_info':event_info.event_info,'entry_info':entry_info.entry_info,'reg_event':reg_event.reg_event,'test':test.test,'sports_info':sports_info.sports_info,'reg_event':reg_event.reg_event}
dispatcher = {'reg_event':reg_event.reg_event}
print('dispatcher loading success')

