def remove_duplicates(data):
    s_ids=set()
    u_data=[]
    for entry in data:
        if entry['id'] not in s_ids:
            s_ids.add(entry['id'])
            u_data.append(entry)
    
    return u_data
data = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 1, "name": "Charlie"},
    {"id": 3, "name": "Alice"}
]
x=remove_duplicates(data)
print(x)
