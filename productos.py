import streamlit as st


def mostrar_productos():
    st.header("Productos")
    st.write(
        "Catálogo de productos disponibles en el sistema."
    )

    productos = [
        {"Producto": "Producto A", "Categoría": "General", "Precio": 5.00, "Stock": 20},
        {"Producto": "Producto B", "Categoría": "General", "Precio": 8.50, "Stock": 15},
        {"Producto": "Producto C", "Categoría": "Especial", "Precio": 12.00, "Stock": 8},
    ]

    st.metric("Total de productos", len(productos))
    st.dataframe(productos)
