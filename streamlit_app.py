import streamlit as st
import pandas as pd

def home_page():
    # Add the slide image at the top of the page
    #st.image("Slide1.PNG", use_column_width=True)

    # Add the title of the app
    st.title("- Mushtari Khan")
    st.write("This is the home page of the app.")
    st.markdown("""
    Welcome to our Global Financial Inclusion Data Mining Project! In this app, we embark on a captivating journey through the Global Financial Inclusion (Global Findex)
    Database 2021 to foster a deeper understanding of financial inclusion worldwide. 
    Our mission is to leverage powerful data mining techniques to uncover hidden insights, patterns, and trends that shape the landscape of 
    financial access and usage across the globe. By analyzing the vast wealth of data from the Global Findex 2021, we aim to shed light on key 
    factors that promote financial inclusion, identify successful strategies, and explore opportunities to empower underserved populations. 
    Through interactive visualizations and data-driven exploration, we invite you to join us in unraveling the complexities of financial inclusion and together, 
    pave the way for a more inclusive and equitable financial ecosystem. Let's dive into the data and discover the untold stories of financial inclusion on a global scale!
    """)
  
def about_page():
    st.title("About")
    # Add links to datasets
    st.header("Dataset")
    st.markdown("""
       The Global Findex is the world’s most comprehensive database on financial inclusion. 
       It is also the only global demand-side data source allowing for global and 
       regional cross-country analysis to provide a rigorous and multidimensional picture of how adults save, 
       borrow, make payments, and manage financial risks.
    """)
    st.markdown("[Dataset](https://microdata.worldbank.org/index.php/catalog/4607/study-description)")
    st.markdown("[MetaData](https://microdata.worldbank.org/index.php/catalog/4607/data-dictionary)")
    
    # Load your data
    #data = pd.read_csv('HighIncomeGroup.csv')

    # Display the data using a DataFrame widget
    # st.write(data)

    # Add a slider to control the number of rows displayed
   # num_rows = st.slider('Select the number of rows to display', min_value=1, max_value=len(data), value=50)
    #st.write(data.head(num_rows))

    
def insights_page():
    #st.image("Slide3.PNG", use_column_width=True)
    st.title("Insights")
    st.write("This is the insights page of the app.")
    
def documentation_page():
    st.title("Documentation")
    st.write("This is the documentation page of the app.")
    
def code_page():
   # st.image("Slide2.PNG", use_column_width=True)
    st.title("Code")
    st.write("This is the code page of the app.")
    
# Create a function to switch pages based on user input
def main():
    st.sidebar.title("Navigation")
    pages = ["Home", "About", "Insights", "Documentation", "Code"]
    choice = st.sidebar.radio("Go to", pages)

    if choice == "Home":
        home_page()
    elif choice == "About":
        about_page()
    elif choice == "Insights":
        insights_page()
    elif choice == "Documentation":
        documentation_page()
    elif choice == "Code":
        code_page()

if __name__ == "__main__":
    main()
