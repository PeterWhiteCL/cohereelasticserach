import streamlit as st
from create_cosine_index import search

def dummy_search_function(query):

    matches = search(query)

    result_1 = matches[0]
    result_2 = matches[1]
    result_3 = matches[2]
    return [result_1, result_2, result_3]

def main():
    st.title("Streamlit Search Interface")

    query = st.text_input("Enter your query here")
    search_button = st.button("Search")

    if search_button:
        results = dummy_search_function(query)
        for result in results:
            st.text(result)

if __name__ == "__main__":
    main()