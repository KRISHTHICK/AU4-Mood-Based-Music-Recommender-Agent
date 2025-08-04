from transformers import pipeline

# Load sentiment/emotion pipeline
emotion_model = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

def detect_mood(text):
    result = emotion_model(text)
    emotion = result[0]['label'].lower()
    
    # Map emotion to mood
    if emotion in ["joy", "love"]:
        return "happy"
    elif emotion in ["sadness"]:
        return "sad"
    elif emotion in ["anger"]:
        return "angry"
    elif emotion in ["calm", "neutral"]:
        return "relaxed"
    else:
        return "relaxed"  # fallback

def get_songs_for_mood(mood, mood_to_songs):
    return mood_to_songs.get(mood, ["No songs found."])
