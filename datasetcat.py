import kagglehub

# Download latest version
path = kagglehub.dataset_download("crawford/cat-dataset")

print("Path to dataset files:", path)