# Simple Banking Chatbot

balance = 10000

print("🏦 Welcome to Smart Bank Chatbot")
print("Type 'exit' to quit")

while True:
    print("\nServices: balance, deposit, withdraw, help")
    user = input("You: ").lower()

    if user == "balance":
        print("Bot: Your current balance is ₹", balance)

    elif user == "deposit":
        amount = float(input("Enter amount to deposit: ₹"))
        balance += amount
        print("Bot: ₹", amount, "deposited successfully.")
        print("Bot: New balance is ₹", balance)

    elif user == "withdraw":
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= balance:
            balance -= amount
            print("Bot: ₹", amount, "withdrawn successfully.")
            print("Bot: Remaining balance is ₹", balance)
        else:
            print("Bot: Insufficient balance!")

    elif user == "help":
        print("Bot: I can help you with:")
        print(" - Check balance")
        print(" - Deposit money")
        print(" - Withdraw money")

    elif user == "exit":
        print("Bot: Thank you for using Smart Bank. Have a nice day! 😊")
        break

    else:
        print("Bot: Sorry, I didn't understand that command.")