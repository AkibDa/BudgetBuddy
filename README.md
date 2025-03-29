# BudgetBuddy - Your AI-Powered Personal Finance Tracker

BudgetBuddy is a user-friendly personal finance tracker designed to help you manage your income and expenses effectively. This application goes beyond basic tracking by integrating AI-powered financial advice, providing instant insights to optimize your financial decisions.

## Key Features

1.  **Income & Expense Tracking:**
    * Enter your monthly income and expenses.
    * Automatically calculates your remaining balance.
    * Provides a clear overview of your financial health.

2.  **Savings Calculator:**
    * Shows how much money you have left after expenses.
    * Offers the flexibility to allocate remaining funds for savings or spending.
    * Provides real-time warnings to prevent overspending.

3.  **Transaction Logging:**
    * Log detailed transactions with:
        * Date
        * Category (e.g., "Food," "Rent")
        * Amount
        * Description
        * Type (income or expense)
    * Maintains a comprehensive record of your financial activities.

4.  **AI-Powered Financial Advice (Powered by Groq/Llama 3):**
    * Leverages the Groq API with Llama 3 to provide instant AI-generated financial advice.
    * Ask questions like:
        * "How can I save more money?"
        * "Best ways to invest Rs 10,000?"
    * Get quick, personalized insights from a virtual financial advisor.

5.  **User-Friendly Dashboard:**
    * Built with Streamlit for a simple and interactive user interface.
    * No complex setup required; just run the application and start managing your finances.

## Example Use Cases

* **Student:** Track pocket money and avoid overspending.
* **Freelancer:** Monitor irregular income and plan savings.
* **Family:** Log household expenses and optimize budgets.
* **Investor:** Get quick financial advice without hiring an advisor.

## How It Works (Behind the Scenes)

* **Python:** Used for core logic, calculations, and API interactions.
* **Streamlit:** Powers the web-based user interface, eliminating the need for HTML/CSS.
* **Groq API (with Llama 3):** Provides AI-driven financial advice.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/AkibDa/Finance]
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd BudgetBuddy
    ```
3.  **Install dependencies:**
    ```bash
    pip install streamlit
    ```
4. **Set up the Groq API key:**
    * You will need an API key from Groq to use the AI functionality.
    * Set your API key as an environment variable or directly in your python file.
5.  **Run the application:**
    ```bash
    streamlit run main.py 
    ```

## Future Enhancements

* [List potential future features or improvements]
* Example: Implement data visualization of spending patterns.
* Example: Add recurring transaction support.
* Example: Implement budget per category.

## Contributing

If you'd like to contribute to BudgetBuddy, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them.
4.  Push your changes to your fork.
5.  Submit a pull request.


## Acknowledgments

* Groq for providing the Llama 3 API.
* Streamlit for the easy to use UI framework.

## Contact

* [AkibDa] - [ahammedskakib@gmail.com]
