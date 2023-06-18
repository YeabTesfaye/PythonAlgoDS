import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person

# time it took for list 
t01 = time.process_time()
people = people_list(1000000)
t02 = time.process_time()
print('Took {} Seconds for list'.format(t02 - t01))
# time it took for generator 
t1 = time.process_time()
people = people_generator(1000000)
t2 = time.process_time()

print('Took {} Seconds for generator'.format(t2 - t1))


#Credit for CoreyMSchafer