import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_preds(results,df):
  # Get input as a slider
  d = st.slider("Select Number of days for prediction", min_value=1, max_value=365, step=1, value=31)
  pred_uc = results.get_forecast(steps=d)
  pred_ci = pred_uc.conf_int()
  ax = df.plot(label='observed', figsize=(14, 7))
  pred_uc.predicted_mean.plot(ax=ax, label='Forecast')
  ax.fill_between(pred_ci.index,
                  pred_ci.iloc[:, 0],
                  pred_ci.iloc[:, 1], color='k', alpha=.25)
  ax.set_xlabel('Date')
  ax.set_ylabel('Receipt')
  plt.legend()
  st.pyplot()

def plot(df):
  plt.figure(figsize=(10, 6))
  sns.barplot(x=df.index, y='Receipt_Count', data=df)
  plt.xlabel('Month')
  plt.ylabel('Receipt Count')
  plt.title('Receipt Counts Comparison')
  plt.xticks(rotation=90)
  st.pyplot()

def get_preds(results, df_month):
  # Get predictions
  preds = results.get_forecast(steps=365).predicted_mean
  date_range = pd.date_range(start="2022-01-01", end="2022-12-31", freq='D')
  new_df = pd.DataFrame(index=date_range, columns=['Receipt_Count'])
  new_df['Receipt_Count'] = preds.values.astype(int)
  new_df = new_df.resample('M').sum()

  show_df = pd.DataFrame()
  show_df.index = new_df.index.strftime('%B')

  new_df.index = new_df.index.strftime('%B') + " 2022"
  new_df = new_df.rename_axis('# Date')

  show_df['2021 Receipt_Count'] = df_month.Receipt_Count.values.astype(int)
  show_df['2022 Receipt_Count'] = new_df["Receipt_Count"].values.astype(int)

  return show_df, new_df