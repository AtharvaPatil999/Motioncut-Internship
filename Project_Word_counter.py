def count_words(text):
    
    # Split the text by whitespace and filter out empty strings
    words = text.split()
    return len(words)

def main():
    while True:
        phrase = input("\nEnter any textual data (or type 'exit' to quit): ").strip()
        
        if phrase.lower() == "exit":
            print("Thank you for response!")
            break
        
        if not phrase:
            print("Please enter valid text.")
            continue
        
        # Count words
        count = count_words(phrase)
        print(f"The text contains {count} word(s).")

main() 