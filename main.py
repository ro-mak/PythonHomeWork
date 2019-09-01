from ListElementChooser import choose_random_element
from DirCreator import create_dirs, delete_dirs

create_dirs()
delete_dirs()
some_list = [1, 2, 3, 4, 5]
print(choose_random_element(some_list))
some_list = []
print(choose_random_element(some_list))
