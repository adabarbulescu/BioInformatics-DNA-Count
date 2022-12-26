import streamlit as st
import pandas as pd
import altair as alt


class NucleotideCounter:
    def __init__(self, sequence):
        self.sequence = sequence
        self.nuc_count = self.count_nucleotides()

    def count_nucleotides(self):
        nuc_count = {
            "A": self.sequence.count("A"),
            "T": self.sequence.count("T"),
            "C": self.sequence.count("C"),
            "G": self.sequence.count("G"),
        }
        return nuc_count

    def print_nuc_count(self):
        # Print dictionary
        st.subheader("1. Print dictionary")
        st.write(self.nuc_count)

        # Print text
        st.subheader("2. Print text")
        st.write(f"There are {str(self.nuc_count['A'])} adenine (A)")
        st.write(f"There are {str(self.nuc_count['T'])} thymine (T)")
        st.write(f"There are {str(self.nuc_count['C'])} cytosine (C)")
        st.write(f"There are {str(self.nuc_count['G'])} guanine (G)")

    def display_df(self):
        # Display DataFrame
        st.subheader("3. Display DataFrame")
        df = pd.DataFrame.from_dict(self.nuc_count, orient="index")
        df = df.rename({0: "count"}, axis="columns")
        df.reset_index(inplace=True)
        df = df.rename(columns={"index": "nucleotide"})
        st.write(df)
        return df

    def display_barchart(self, df):
        # Display Barchart
        st.subheader("4. Display Bar chart")

        p = alt.Chart(df).mark_bar().encode(x="nucleotide", y="count")
        p = p.properties(width=alt.Step(80))
        st.write(p)


# main function
def main():
    sequence_input = st.text_area("Sequence input: ", height=250)
    sequence = sequence_input.upper()
    sequence = sequence.replace("\n", "")

    counter = NucleotideCounter(sequence)
    counter.print_nuc_count()
    df = counter.display_df()
    counter.display_barchart(df)


# run main function
if __name__ == "__main__":
    main()
