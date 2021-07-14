import json

data = {}
data['user'] = []
data['user'].append({
    'name': 'Alex',
    'email': 'alex@gmail.com'
})
data['user'].append({
    'name': 'Bob',
    'email': 'bob@gmail.com'
})
data['user'].append({
    'name': 'Christ',
    'email': 'christ@gmail.com'
})

# data=[{
#     'name': 'Alex',
#     'email': 'alex@gmail.com'
# },{
#     'name': 'Bob',
#     'email': 'bob@gmail.com'
# },{
#     'name': 'Christ',
#     'email': 'christ@gmail.com'
# }]

print(data)
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)