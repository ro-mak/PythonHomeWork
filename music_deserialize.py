import json, pickle


def deserialize_json():
    json_file = open("group.json", "r", encoding='UTF-8')
    json_bytes = json_file.read()
    json_file.close()
    print("Reading json from file")
    print(json_bytes)
    my_dict = json.loads(json_bytes)
    print("My json dict")
    print(my_dict)
    print(type(my_dict))


def deserialize_pickle():
    pickle_file = open("group.pickle", "rb")
    pickle_bytes = pickle_file.read()
    print("Reading pickle from file")
    print(pickle_bytes)
    my_dict = pickle.loads(pickle_bytes)
    print("My pickle dict")
    print(my_dict)
    print(type(my_dict))


deserialize_json()
deserialize_pickle()
