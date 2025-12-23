try:
    with open("new_file.txt",'r')as f:
        for line in f:
            
            line=line.strip()
            try:
                num=int(line)
                print("Converted:",num)
            except ValueError:
                print("ValueError: Cannot convert string to integer.",line)
except FileNotFoundError:
    print("File not found")