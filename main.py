
PATH = "/home/shukhratkhuja/Desktop/MyProjects/bookbot/books/frankenstein.txt"

plist = PATH.split('/')
del plist[-2]
REPORT_PATH = "/".join(plist).replace(".txt", "_report.txt")

def readFile(file_path):
    with open(file_path) as f:
        content = f.read()
        return content
    

def countWords(file_path):

    file_content = readFile(file_path=file_path)

    words_count = len(file_content.split())
    return words_count
    

def countCharacters(file_path):
    d = {}
    file_content = readFile(file_path=file_path)
    for c in file_content.lower():
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

def makeReport(file_path, report_path):

    words_count = countWords(file_path=file_path)
    letter_dict = countCharacters(file_path=file_path)

    with open(report_path, 'w') as f:
                
        f.write(f"--- Begin report of {file_path} ---\n")
        f.write(f"{words_count} words found in the document\n\n")

        sorted_dict = dict(sorted(letter_dict.items(), key=lambda x: x[1], reverse=True))

        for letter, count in sorted_dict.items():
            if letter.isalpha():
                f.write(f"The '{letter}' character was found {count} times\n")
        
        f.write("\n--- End report ---")

    with open(report_path) as f:
        report = f.readlines()
        return report    
    
report = makeReport(file_path=PATH, report_path=REPORT_PATH)
print(report)