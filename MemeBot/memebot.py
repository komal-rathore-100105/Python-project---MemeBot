from meme_generator import generate_meme
from get_random_quote import get_random_quote
 
def main():
    
    print("\n============================")
    print("🤖  Welcome to MemeBot!")
    print("============================\n")

    print("Choose an option:")
    print("1. Generate meme with random quote")
    print("2. Generate meme with your own quote")

    choice = input("Enter 1 or 2: ")
    quote = " " 
    if choice == "1":
        quote = get_random_quote()
        generate_meme(quote=quote)

    elif choice == "2":
        quote_text = input("Enter your quote: ")
        author = input("Enter author name (optional): ")
        quote = f"{quote_text} - {author if author else 'Anonymous'}"
        generate_meme(quote=quote)
    else:
        print("Invalid option. Exiting.")
        return

    # Save quote to a temp file or pass directly
    print("\n🖼️ Generating your meme...")
    generate_meme(quote=quote)  # Uses the quote from get_random_quote() or user input quote

    print("✅ Meme created: generated_meme.jpeg")
    send_option = input("\n📧 Do you want to email this meme? (yes/no): ").lower()

    if send_option == "yes":
        from send_email import send_meme_email
        receiver_email = input("Enter recipient's email: ")
        send_meme_email(receiver_email,quote)      

if __name__ == "__main__":
    main()







