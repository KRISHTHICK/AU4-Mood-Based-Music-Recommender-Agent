import streamlit as st
from mood_agent import detect_mood, get_songs_for_mood
from songs import mood_to_songs

st.set_page_config(page_title="🎶 Mood Music Recommender")

st.title("🎧 Mood-Based Music Recommender Agent")

mood_option = st.selectbox("How are you feeling today?", ["", "happy", "sad", "relaxed", "angry", "Detect from text"])

if mood_option == "Detect from text":
    user_text = st.text_area("Describe your mood or write a journal entry:", height=150)
    if st.button("Analyze Mood"):
        if user_text.strip() == "":
            st.warning("Please enter some text.")
        else:
            detected = detect_mood(user_text)
            st.success(f"Detected Mood: **{detected.capitalize()}**")
            songs = get_songs_for_mood(detected, mood_to_songs)
            st.markdown("### 🎵 Recommended Songs:")
            for s in songs:
                st.write(f"- {s}")
else:
    if mood_option:
        songs = get_songs_for_mood(mood_option, mood_to_songs)
        st.markdown("### 🎵 Recommended Songs:")
        for s in songs:
            st.write(f"- {s}")
