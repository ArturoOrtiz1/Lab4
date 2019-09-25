def main():
    print("This program determines a persons numeric character trait for their name")
    name= input("Please type in name in lowercase letters:")
    print("\nHere is your numeric trait:")
    sum=0
    for ch in name:
        sum=sum+ord(ch)-96

    print(sum)
main()
    
