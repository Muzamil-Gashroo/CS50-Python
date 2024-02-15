




list = ["42",'forty two','forty-two']

def main():
    text =input('What is the Great Question of Life, the Universe and Everything? ')
    text = text.lower().strip()
    if text in list:
        print("yes")
    else:
        print("no")

main()














