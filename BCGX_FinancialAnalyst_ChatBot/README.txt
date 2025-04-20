Financial Chatbot Prototype
----------------------------

This is a simple rule-based financial chatbot designed to respond to predefined queries using financial data from Task 1.

How it Works:
- The chatbot matches exact user queries using if-else logic.
- It provides financial data summaries based on 2024 financials for AAPL, MSFT, and TSLA.

Supported Queries:
- What is the total revenue for AAPL?
- What is the total revenue for MSFT?
- What is the total revenue for TSLA?
- How has AAPL's net income changed over the last year?
- How has MSFT's net income changed over the last year?
- How has TSLA's net income changed over the last year?

Limitations:
- Only handles exact predefined queries.
- Cannot answer follow-up or unexpected questions.
- No real-time data fetching; static values based on analysis results.

Run:
$ python financial_chatbot.py
