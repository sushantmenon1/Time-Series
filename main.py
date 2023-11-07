import streamlit as st
import pandas as pd
import utilities
import statsmodels.api as sm 
st.set_option('deprecation.showPyplotGlobalUse', False)

# Apply custom CSS to fill the screen
st.set_page_config(layout="wide")

# Center-align the main title using Markdown with inline CSS
st.markdown(
    """
    <h1 style='text-align: center;'>Receipt Count Predictor</h1>
    """,
    unsafe_allow_html=True
)

st.subheader(" Data Visualization")

df = pd.read_csv('data_daily.csv', parse_dates=['# Date'], index_col='# Date')
df_month = df.resample('M').sum()
df_month.index = df_month.index.strftime('%B') + " 2021"

mod = sm.tsa.statespace.SARIMAX(df,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()

utilities.plot_preds(results,df)
show_df, new_df = utilities.get_preds(results, df_month)

st.subheader("Predictions")
# User input for 2022 months
selected_months = st.multiselect('Select Months', ['All'] + list(new_df.index))

# Plot selected 2022 months
if 'All' in selected_months:
    selected_months = list(new_df.index)


if selected_months:
  plot_df = pd.DataFrame(index=list(df_month.index) + list(new_df.loc[selected_months,"Receipt_Count"].index), columns=['Receipt_Count'])
  plot_df['Receipt_Count'] = list(df_month.Receipt_Count) + list(new_df.loc[selected_months,"Receipt_Count"].values)
  utilities.plot(plot_df)
else:
  utilities.plot(df_month)

show_df['Percentage Change'] = ((show_df['2022 Receipt_Count'] - show_df['2021 Receipt_Count']) / show_df['2021 Receipt_Count']) * 100

st.dataframe(show_df,2100,450)  
