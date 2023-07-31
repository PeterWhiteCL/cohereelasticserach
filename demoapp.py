import streamlit as st
from create_cosine_index import search

def search_function(query):

    matches = search(query)
    result_1 = [matches[0]["abstract"], matches[0]["score"]]
    result_2 = [matches[1]["abstract"], matches[1]["score"]]
    result_3 = [matches[2]["abstract"], matches[2]["score"]]
    return [result_1, result_2, result_3]

def main():
    st.title("ElasticSearch Search Interface")
    st.markdown(
        """
        Enter a query you'd like to use to search the ArXiv index using Cohere vectors and Elasticsearch: 
        """
    )

    query = st.text_input("Enter your query here")
    search_button = st.button("Search")

    if search_button:
        results = search_function(query)
        i = 1
        for result in results:
            st.text("Match " + str(i) + ". Score: " + str(result[1]))
            st.text("Abstract: " + str(result[0]))
            i = i + 1

if __name__ == "__main__":
    main()