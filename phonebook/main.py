

book_dict = {}


def read_phonebook():
  with open('phonebook/phonebook.txt', 'r', encoding='UTF-8') as file:
    data = file.read()
  return data 

print(read_phonebook())      


def add_contact(name, number):
  with open('phonebook/phonebook.txt', 'a', encoding='UTF-8') as file:
    book_dict[name] = number
    return book_dict

# print(add_contact('RAZ', 123))

def find_contact(name):
  with open("phonebook/phonebook.txt", 'r', ecording='utf-8') as fh:
    for i in fh.readlines():
      if i:
        key, val = i.strip().split(':')
        book_dict[key] = val
    for i in book_dict.keys():
      if i == name:
        return f"{i} - {book_dict[i]} "
      else:
        return "Контакт не найден"


# print(find_contact('Роберт'))

def save_change(name,tel):
  with open("phonebook/phonebook.txt", 'a', ecording='utf-8') as fh:
    fh.write('{}:{} \n'.format(name, tel))


def change_contact(name, new_name):
  with open("phonebook/phonebook.txt", 'r', ecording='utf-8') as fh:
    for i in fh.readlines():
      if i:
        key, val = i.strip().split(':')
        book_dict[key] = val
    for i in book_dict.keys():
      if i == name:
        i = new_name
        book_dict.update( [new_name] )
        with open("phonebook/phonebook.txt", 'a', ecording='utf-8') as fh:
           fh.write('\n{}'.format(new_name))
        return new_name
    else:
        return "Контакт не найден"
    

def delete_contact(name):
  contact = ''
  with open("phonebook/phonebook.txt", 'r', ecording='utf-8') as fh:
    for i in fh.readlines():
      if i:
        key, val = i.strip().split(':')
        book_dict[key] = val
    for i in book_dict.keys():
      if i == name:
        contact = 1
        with open("phonebook/phonebook.txt", 'w', ecording='utf-8') as fh:
          book_dict.pop(contact)
          for key, val in book_dict.items():
            fh.write(f'{key}:{val}\n')
        return "Контакт удален успешно"
    else:
        return "Контакт не найден"
    
print(delete_contact("Роберт"))





