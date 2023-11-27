from db import create_collection, insert_data, query_data

# create collections
# create_collection('student1')
# create_collection('student2')
# create_collection('researcher')


# insert allen data
#  insert_data('student1', 'Allen is a college student.', 'student1')
print(query_data('student1', 'who is Allen?')['documents'][0][0])
