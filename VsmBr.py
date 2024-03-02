import math

class InformationRetrieval:
    def __init__(self, documents):
        self.documents = documents
        self.tf_idf = self.calculate_tf_idf()

    def calculate_tf_idf(self):
        tf_idf = {}
        total_docs = len(self.documents)

        # Compute term frequency (TF) and inverse document frequency (IDF)
        for doc_id, doc in enumerate(self.documents):
            tf = {}
            for term in doc:
                if term in tf:
                    tf[term] += 1
                else:
                    tf[term] = 1

            for term in tf:
                doc_freq = sum(1 for d in self.documents if term in d)
                #print(f"Term: {term}, Doc Frequency: {doc_freq}")
                if doc_freq != 0:
                    idf = math.log(total_docs / doc_freq)
                else:
                    idf = 0  # Set IDF to 0 if doc_freq is 0
                #print(f"IDF for {term}: {idf}")
                tf[term] *= idf

            tf_idf[doc_id] = tf

        return tf_idf

    def vsm_query(self, query_terms):
        query_vector = {}
        for term in query_terms:
            if term in query_vector:
                query_vector[term] += 1
            else:
                query_vector[term] = 1

        # Compute TF-IDF for query
        for term in query_vector:
            if term in self.tf_idf[0]:  # Consider only the first document for IDF calculation
                doc_freq = sum(1 for d in self.documents if term in d)
                idf = math.log(len(self.documents) / doc_freq)
                query_vector[term] *= idf

        #print("Query Vector:")
        #print(query_vector)

        # Compute cosine similarity
        similarities = {}
        for doc_id, doc in enumerate(self.documents):
            common_terms = set(query_terms) & set(doc)
            dot_product = sum(query_vector.get(term, 0) * self.tf_idf[doc_id].get(term, 0) for term in common_terms)
            query_norm = math.sqrt(sum(val ** 2 for val in query_vector.values()))
            doc_norm = math.sqrt(sum(val ** 2 for val in self.tf_idf[doc_id].values()))
            similarity = dot_product / (query_norm * doc_norm) if query_norm != 0 and doc_norm != 0 else 0
            similarities[doc_id] = similarity



        # Sort documents by similarity
        ranked_docs = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
        return ranked_docs

    def boolean_query(self, query_terms):
        results = []
        for doc_id, doc in enumerate(self.documents):
            if all(term in doc for term in query_terms):
                results.append(doc_id)
        return results


# Example usage:
documents = [
    ["data", "mining", "techniques"],
    ["data", "visualization", "tools"],
    ["machine", "learning", "algorithms"]
]

ir = InformationRetrieval(documents)

# VSM query
query_terms_vsm = ["data", "mining"]
results_vsm = ir.vsm_query(query_terms_vsm)
print("Vector Space Model (VSM) Search Results:")
for doc_id, similarity in results_vsm:
    print(f"Document {doc_id + 1}: Similarity = {similarity:.4f}")

# Boolean query
query_terms_boolean = ["data", "mining"]
results_boolean = ir.boolean_query(query_terms_boolean)
print("\nBoolean Retrieval Model (BRM) Search Results:")
for doc_id in results_boolean:
    print(f"Document {doc_id + 1}")
