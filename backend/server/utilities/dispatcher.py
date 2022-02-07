from .funcs import staff_info,hostel_info,uni_info,test,course_info,faculty_info,career_info,event_info,entry_info

dispatcher = { 'staff_info' : staff_info.staff_info,'hostel_info':hostel_info.hostel_info,'uni_info':uni_info.uni_info,'course_info':course_info.course_info,'faculty_info':faculty_info.faculty_info,'career_info':career_info.career_info,'event_info':event_info.event_info,'entry_info':entry_info.entry_info,'test':test.test}
print('dispatcher loading success')

