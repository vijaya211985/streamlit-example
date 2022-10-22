
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns

iris = sns.load_dataset('iris')
sns.boxplot(data=iris)

