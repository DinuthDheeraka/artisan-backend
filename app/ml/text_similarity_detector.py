from sentence_transformers import SentenceTransformer, util

# Load the pre-trained SentenceTransformer model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')


def similarity(sentences):
    # Encode the sentences to obtain their embeddings
    embeddings = model.encode(sentences)

    # Calculate cosine similarity between the two sentence embeddings
    similarity_score_1 = util.pytorch_cos_sim(embeddings[0].reshape(1, -1), embeddings[1].reshape(1, -1))
    similarity_score_2 = util.pytorch_cos_sim(embeddings[0].reshape(1, -1), embeddings[2].reshape(1, -1))

    return {"title": similarity_score_1.item(), "keywords": similarity_score_2.item()}
