# p(a)= a/A

data= ['red', 'blue', 'green', 'red', 'green', 'green', 'yellow', 'red', 'blue', 'yellow', 'green', 'red']

event= 'red'

event_count= data.count(event)
total_event= len(data)

probability= event_count/total_event
print(f"Probability of drawing {event}: {probability:.2f}")