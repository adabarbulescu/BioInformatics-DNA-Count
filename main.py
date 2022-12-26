import streamlit as st
import pandas as pd
import altair as alt

# page title
st.image("https://cdn.pixabay.com/photo/2018/07/15/10/44/dna-3539309_960_720.jpg")
st.write("# DNA Nucleotide Count Web App")
st.write("This app counts the nucleotide composition of query DNA")
st.write("***")

# enter DNA sequence
st.header("Enter DNA sequence")
sequence_input = st.text_area("Sequence input: ", height=250)
sequence = sequence_input.upper()
sequence = sequence.replace("\n", "")

st.write("***")

# DNA nucleotide count
st.header("Output (DNA Nucleotide Count)")


def nucleotide_count(seq):
    nucdict = {
        "A": seq.count("A"),
        "T": seq.count("T"),
        "C": seq.count("C"),
        "G": seq.count("G"),
    }
    return nucdict


def print_nuc_count(nuc_count):
    # Print dictionary
    st.subheader("1. Print dictionary")
    st.write(nuc_count)

    # Print text
    st.subheader("2. Print text")
    st.write(f"There are {str(nuc_count['A'])} adenine (A)")
    st.write(f"There are {str(nuc_count['T'])} thymine (T)")
    st.write(f"There are {str(nuc_count['C'])} cytosine (C)")
    st.write(f"There are {str(nuc_count['G'])} guanine (G)")


X = nucleotide_count(sequence)
X_label = list(X)
X_values = list(X.values())


def display_df(nuc_count):
    # Display DataFrame
    st.subheader("3. Display DataFrame")
    df = pd.DataFrame.from_dict(X, orient="index")
    df = df.rename({0: "count"}, axis="columns")
    df.reset_index(inplace=True)
    df = df.rename(columns={"index": "nucleotide"})
    st.write(df)

    return df


def display_barchart(df):
    # Display Barchart
    st.subheader("4. Display Bar chart")

    p = alt.Chart(df).mark_bar().encode(x="nucleotide", y="count")
    p = p.properties(width=alt.Step(80))
    st.write(p)


# main function
def main():
    nuc_count = nucleotide_count(sequence)
    print_nuc_count(nuc_count)
    df = display_df(nuc_count)
    display_barchart(df)


# run main function
if __name__ == "__main__":
    main()
