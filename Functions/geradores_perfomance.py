import memory_profiler as mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print('Memory (Before): ' + str(mem_profile.memory_usage()) + 'MB' )

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

# Com listas
# t1 = time.perf_counter()
# people = people_list(1000000)
# t2 = time.perf_counter()

# Com Geradores
t1 = time.perf_counter()
people = people_generator(1000000)
t2 = time.perf_counter()

print('Memory (After) : ' + str(mem_profile.memory_usage()) + 'MB')

print ('Took ' + str(t2-t1) + ' Seconds')