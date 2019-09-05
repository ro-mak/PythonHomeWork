import json, pickle

my_favourite_group = {
    "name": "Offspring",
    "tracks": ["Pretty fly", "Dirty magic"],
    "Albums": [{"name": "Americana", "year": 2000},
               {"name": "Days go by", "year": 2000}]}


def write_json(group):
    json_bytes = json.dumps(group)
    print("Json")
    print(json_bytes)
    json_file = open("group.json", "wb")
    json_file.write(json_bytes.encode(encoding="UTF-8"))
    json_file.close()


def write_bytes_with_pickle(group):
    pickle_bytes = pickle.dumps(group)
    print("Pickle")
    print(pickle_bytes)
    pickle_file = open("group.pickle", "wb")
    pickle_file.write(pickle_bytes)
    pickle_file.close()


write_json(my_favourite_group)
write_bytes_with_pickle(my_favourite_group)
