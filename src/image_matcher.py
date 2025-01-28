import os
import glob
from PIL import Image
from sentence_transformers import SentenceTransformer, util

class MemeMatcher:
    def __init__(self):
        self.model = SentenceTransformer('clip-ViT-B-32')
        self.image_folder = "images"
        self.image_paths = glob.glob(os.path.join(self.image_folder, "*.jpg"))
        self.image_embeddings = self._precompute_embeddings()

    def _precompute_embeddings(self):
        embeddings = []
        for img_path in self.image_paths:
            img = Image.open(img_path)
            embedding = self.model.encode(img, convert_to_tensor=True)
            embeddings.append(embedding)
        return embeddings

    def find_best_meme(self, text):
        text_embedding = self.model.encode(text, convert_to_tensor=True)
        similarities = [
            util.pytorch_cos_sim(text_embedding, img_emb).item()
            for img_emb in self.image_embeddings
        ]
        best_idx = similarities.index(max(similarities))
        return self.image_paths[best_idx]