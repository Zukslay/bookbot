def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return len(file_contents.split())
    
def get_total_characters(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        temp_dict = {}
        for character in file_contents:
            if character.lower() not in temp_dict:
                temp_dict[character.lower()] = 1
            else:
                temp_dict[character.lower()] += 1
        return temp_dict
    
def sorted_characters(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        temp_dict = {}
        
        for character in file_contents:
            if not character.isalpha():
                continue
            if character.lower() not in temp_dict:
                temp_dict[character.lower()] = 1
            else:
                temp_dict[character.lower()] += 1
        
        return dict(sorted(temp_dict.items(), key = lambda x:x[1], reverse = True))
        
