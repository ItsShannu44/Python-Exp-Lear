def create_file(filepath):
    open(filepath, 'x') #Creates a file if it do not exist
    print(f'{filepath}created successfully.') 
create_file('new_file.txt')