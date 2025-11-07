from transformers import pipeline
from PIL import Image

print("🚀 Loading lightweight model... (this may take a minute the first time)")
captioner = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

# Ask for image input
image_path = input("\n📁 Enter the full path to your image: ")

try:
    image = Image.open(image_path)
except Exception as e:
    print("❌ Could not open image:", e)
    exit()

print("\n✨ Generating caption...")
captions = captioner(image)

print("\n🖼️ Caption Generated:")
print("👉", captions[0]['generated_text'])
