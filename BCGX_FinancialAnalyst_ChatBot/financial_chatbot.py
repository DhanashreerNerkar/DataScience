def financial_chatbot(query):
    if query == "What is the total revenue for AAPL?":
        return "Apple's total revenue for 2024 is $391,035 million."
    elif query == "What is the total revenue for MSFT?":
        return "Microsoft's total revenue for 2024 is $245,122 million."
    elif query == "What is the total revenue for TSLA?":
        return "Tesla's total revenue for 2024 is $97,690 million."
    elif query == "How has AAPL's net income changed over the last year?":
        return "Apple's net income has decreased by 3.36% compared to the previous year."
    elif query == "How has MSFT's net income changed over the last year?":
        return "Microsoft's net income has increased by 21.8% compared to the previous year."
    elif query == "How has TSLA's net income changed over the last year?":
        return "Tesla's net income has decreased by 52.23% compared to the previous year."
    else:
        return "Sorry, I can only provide information on predefined queries."


# Example interaction
if __name__ == "__main__":
    while True:
        user_input = input("Ask a financial question (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        response = financial_chatbot(user_input)
        print(response)
