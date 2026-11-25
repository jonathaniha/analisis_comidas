import streamlit as st
import pandas as pd

st.title("Análisis del Menú Completo de McDonald's 🍟📊")

# Cargar menú completo
df = pd.read_csv("MenuMcDonalds.csv")

# 1) Los 5 más calóricos
st.subheader("¿Cuáles son los 5 alimentos más calóricos del menú?")
st.dataframe(df.sort_values('Calories', ascending=False).head(5)[['Item', 'Calories']])

# 2) El alimento con más proteína
st.subheader("¿Cuál tiene más proteína?")
st.write(df.loc[df['Protein'].idxmax(), ['Item', 'Protein']])

# 3) Promedio de calorías por categoría
st.subheader("Promedio de calorías por tipo de comida:")
st.dataframe(df.groupby('Category')['Calories'].mean().sort_values(ascending=False))

# 4) Proporción proteína / grasa
st.subheader("Top 10 alimentos según la proporción proteína/grasa (indicador de “saludable”):")
df['Protein_to_Fat'] = df['Protein'] / df['Total Fat']
st.dataframe(df.sort_values('Protein_to_Fat', ascending=False).head(10))

st.title("Desayunos Saludables 🍳")
df_break = pd.read_csv("desayunos_saludables.csv")
st.dataframe(df_break)

st.title("Comidas Saludables 🍽️")
df_food = pd.read_csv("comidas_saludables.csv")
st.dataframe(df_food)

st.title("Gráficas de Comidas Saludables 🍽️📊")

# Cargar tu CSV filtrado
df2 = pd.read_csv("comidas_saludables.csv")

st.subheader("Vista previa del dataset")
st.dataframe(df2)

# =========================================
# 1) Gráfica de barras: Calorías por alimento
# =========================================
st.subheader("Calorías por alimento")
st.bar_chart(df2.set_index("Item")["Calories"])


# =========================================
# 2) Gráfica de barras: Proteína por alimento
# =========================================
st.subheader("Proteína por alimento")
st.bar_chart(df2.set_index("Item")["Protein"])


# =========================================
# 3) Scatter Plot: Relación entre calorías y proteína
# =========================================
st.subheader("Relación entre Calorías y Proteína")
st.scatter_chart(df2.set_index("Item"), x="Calories", y="Protein")


# =========================================
# 4) Scatter: Proteína vs Grasa
# =========================================
if "Total Fat" in df2.columns:
    st.subheader("Relación entre Proteína y Grasa")
    st.scatter_chart(df2, x="Total Fat", y="Protein")
else:
    st.info("⚠️ El CSV no tiene la columna 'Total Fat'")


# =========================================
# 5) Pie chart por categoría
# =========================================
if "Category" in df2.columns:
    st.subheader("Distribución de comidas saludables por categoría")
    
    cat_counts = df2["Category"].value_counts()
    st.write(cat_counts)  # tabla
    
    # Pie chart sencillo con Altair
    import altair as alt
    pie_data = pd.DataFrame({
        "Category": cat_counts.index,
        "Count": cat_counts.values
    })
    
    pie_chart = alt.Chart(pie_data).mark_arc().encode(
        theta="Count",
        color="Category",
        tooltip=["Category", "Count"]
    )
    st.altair_chart(pie_chart, use_container_width=True)
else:
    st.info("⚠️ El CSV no tiene columna 'Category'")