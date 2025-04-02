import streamlit as st
from groq import Groq
from keys import API_KEY  

st.title("💰 BudgetBuddy")
st.write("Welcome to BudgetBuddy!")

if 'transactions' not in st.session_state:
    st.session_state.transactions = []

def savings(income, expenses):
    savings = income - expenses
    st.success(f"You have Rs {savings} left over each month.")
    
    choice = st.radio("Would you like to save or spend this money?", ("save", "spend"))
    if choice == "save":
        save_amount = st.number_input("How much would you like to save?", min_value=0.0, max_value=savings)
        if st.button("Confirm Save"):
            savings += save_amount
            st.success(f"You now have Rs {savings} saved.")
    elif choice == "spend":
        spend_amount = st.number_input("How much would you like to spend?", min_value=0.0, max_value=savings)
        if st.button("Confirm Spend"):
            savings -= spend_amount
            st.success(f"You now have Rs {savings} left over.")
    
    if savings <= 0:
        st.error("You have run out of money!")
    else:
        st.success(f"You have Rs {savings} left over.")

def add_transaction(date, category, amount, description, type):
    st.session_state.transactions.append({
        "date": date,
        "category": category,
        "amount": amount,
        "description": description,
        "type": type
    })
    st.success("Transaction added successfully!")
    st.write(f"Date: {date}")
    st.write(f"Category: {category}")
    st.write(f"Amount: Rs {amount}")
    st.write(f"Description: {description}")
    st.write(f"Type: {type}")

def view_balance(income, expenses):
    st.write(f"Income: Rs {income}")
    st.write(f"Expenses: Rs {expenses}")
    st.write(f"Balance: Rs {income - expenses}")

def get_advice(prompt):
    try:
        client = Groq(api_key=API_KEY)
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are a financial advisor. Provide concise, actionable advice."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1024
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error fetching advice: {e}"

income = st.number_input("Monthly Income (Rs)", min_value=0.0)
expenses = st.number_input("Monthly Expenses (Rs)", min_value=0.0)

if income < expenses:
    st.error("Your expenses exceed your income! Please adjust.")
elif income == expenses:
    st.warning("Your income equals expenses. No savings left.")
else:
    option = st.selectbox(
        "Choose an action:",
        ("Add Transaction", "View Balance", "Calculate Savings", "Get Financial Advice", "Exit")
    )

    if option == "Add Transaction":
        with st.form("transaction_form"):
            date = st.date_input("Date")
            category = st.text_input("Category")
            amount = st.number_input("Amount (Rs)", min_value=0.0)
            description = st.text_input("Description")
            trans_type = st.radio("Type", ("income", "expense"))
            if st.form_submit_button("Add Transaction"):
                add_transaction(date, category, amount, description, trans_type)

    elif option == "View Balance":
        view_balance(income, expenses)

    elif option == "Calculate Savings":
        savings(income, expenses)

    elif option == "Get Financial Advice":
        st.subheader("Need Financial Advice?")
        prompt = st.text_input("Ask a question (e.g., 'How to save money?'):")

        if st.button("Get Advice"):
            if prompt:
                with st.spinner("Fetching advice..."):
                    advice = get_advice(prompt)
                    st.markdown(f"**Advice:**\n\n{advice}")
        else:
            st.warning("Please enter a question!")

    elif option == "Exit":
        st.success("Thank you for using BudgetBuddy!")