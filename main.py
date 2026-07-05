from recommendation import search_and_summarize

def main():
    print("=" * 60)
    print("AI Research Paper Recommendation System")
    print("=" * 60)

    query = input("Enter your research topic: ")
    k = int(input("Number of papers to retrieve: "))

    search_and_summarize(query, k)

if __name__ == "__main__":
    main()
