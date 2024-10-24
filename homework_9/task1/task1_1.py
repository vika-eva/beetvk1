def clean_tel(tel_number):
    clean_tel = tel_number.replace(" ", "").replace("-", "").replace(")", "").replace("(", "")
    return clean_tel

print(clean_tel(input("Enter tel number: ")))

#def main():
