while True:
    s=input("Enter a string:")
    if s.lower()=="exit":
        break
    try:
        print("Integer:",int(s))
    except ValueError:
        print("The Input is not an Integer. Try again.")