from chatbot import ask_bot

while True:

    query = input("\nAsk: ")

    if query.lower() == "exit":
        break

    answer = ask_bot(
        query
    )

    print(
        "\nBot:",
        answer
    )