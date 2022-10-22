
install seaborn
import seaborn as sns
import streamlit as st
import numpy as np
import pandas as pd


iris = sns.load_dataset('iris')
fig = plt.figure(figsize=(10, 4))
sns.boxplot(data=iris)
st.pyplot(fig)
