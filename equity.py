import streamlit as st

def calculate_equity(hours_worked_a, hourly_rate_a, cash_invested_a, hours_worked_b, hourly_rate_b, cash_invested_b):
    total_value_a = (hours_worked_a * hourly_rate_a) + cash_invested_a
    total_value_b = (hours_worked_b * hourly_rate_b) + cash_invested_b
    total_value = total_value_a + total_value_b

    equity_a = (total_value_a / total_value) * 100
    equity_b = (total_value_b / total_value) * 100

    return equity_a, equity_b

def main():
    st.title("Slicing Pie Equity Calculator")
    st.write("Use the Slicing Pie model to calculate equity allocation for a startup with two individuals.")

    st.header("Enter Your Inputs")

    hours_worked_a = st.number_input("Total Hours Worked by Person A", min_value=0, value=0, step=1)
    hourly_rate_a = st.number_input("Hourly Rate for Person A", min_value=0, value=0, step=1)
    cash_invested_a = st.number_input("Cash Invested by Person A", min_value=0, value=0, step=1)

    hours_worked_b = st.number_input("Total Hours Worked by Person B", min_value=0, value=0, step=1)
    hourly_rate_b = st.number_input("Hourly Rate for Person B", min_value=0, value=0, step=1)
    cash_invested_b = st.number_input("Cash Invested by Person B", min_value=0, value=0, step=1)

    if st.button("Calculate Equity"):
        equity_a, equity_b = calculate_equity(hours_worked_a, hourly_rate_a, cash_invested_a, hours_worked_b, hourly_rate_b, cash_invested_b)
        st.success(f"Equity Allocation:\nPerson A: {equity_a:.2f}%\nPerson B: {equity_b:.2f}%")

if __name__ == "__main__":
    main()
