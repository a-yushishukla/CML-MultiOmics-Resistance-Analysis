import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="CML Resistance Analyzer", layout="wide")

st.title("🧬 CML Multi-Omics: Prognostic Marker Discovery")
st.markdown("### Identifying BCR-ABL Independent Resistance Pathways")

# Sidebar for parameters
st.sidebar.header("Analysis Settings")
fold_change_cutoff = st.sidebar.slider("Log2 Fold Change Cutoff", 0.0, 5.0, 2.0)
p_value_cutoff = st.sidebar.slider("p-value Cutoff (-log10)", 0.0, 10.0, 1.3)

# Mock Data Generation (Simulating a DESeq2 output)
genes = ['AXL', 'MET', 'STAT5', 'BTK', 'SRC', 'JAK2', 'RUNX1', 'ASXL1', 'TET2']
data = {
    'Gene': genes,
    'Log2FoldChange': [3.2, 2.8, 1.5, 4.1, -0.5, 2.1, -2.4, 3.8, 0.2],
    'p_value': [0.001, 0.005, 0.08, 0.0001, 0.4, 0.01, 0.002, 0.0005, 0.9]
}
df = pd.DataFrame(data)
df['-log10(p-value)'] = -np.log10(df['p_value'])

col1, col2 = st.columns(2)

with col1:
    st.subheader("Volcano Plot: Differential Expression")
    fig = px.scatter(df, x='Log2FoldChange', y='-log10(p-value)', text='Gene',
                     color='Log2FoldChange', size='-log10(p-value)',
                     color_continuous_scale='RdBu_r')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Top Prognostic Candidates")
    significant = df[(df['Log2FoldChange'].abs() >= fold_change_cutoff) & 
                    (df['-log10(p-value)'] >= p_value_cutoff)]
    st.write(significant.sort_values(by='-log10(p-value)', ascending=False))

st.info("Note: This dashboard is designed to visualize BCR-ABL independent markers identified via RNA-seq and NGS integration.")
