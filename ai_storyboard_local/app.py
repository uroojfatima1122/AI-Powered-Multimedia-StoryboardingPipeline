import os
import sys
import gradio as gr
from groq import Groq

# Try to get the API key from environment variables
api_key = os.environ.get("GROQ_API_KEY")

if not api_key:
    print("❌ ERROR: GROQ_API_KEY environment variable is not set.")
    print("Please set your GROQ_API_KEY before running this script.")
    print("Check the README.md file for instructions.")
    sys.exit(1)

client = Groq(api_key=api_key)

PROMPT_TEMPLATE = """
You are an AI Storyboard Creator designed for beginner multimedia students.

Your task is to transform a simple idea into a complete storyboard pipeline.

-------------------------
🎯 INPUT:
User Idea: {user_input}
-------------------------

🎬 OUTPUT FORMAT:

🎬 TITLE:
Generate a short, creative, and catchy title.

📝 SCRIPT (Scene-by-Scene Breakdown):
Create 5 to 8 scenes.

For each scene include:
- Scene Number
- Short Description (clear and simple)
- Key Visual Elements (characters, setting, mood)
- Camera Angle (e.g., close-up, wide shot, aerial)

🎨 IMAGE PROMPTS:
For EACH scene, generate a detailed prompt.

Format strictly as:
Scene X Prompt: "Highly detailed cinematic scene of ..."

🎙️ NARRATION:
- One paragraph per scene
- Simple English
- Emotionally engaging

🎵 BACKGROUND MUSIC:
Suggest mood for each scene

-------------------------
⚠️ RULES:
- Keep beginner-friendly
- Maintain consistency
- Clean structured output only
-------------------------
"""

def generate_storyboard(user_input):
    prompt = PROMPT_TEMPLATE.format(user_input=user_input)
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def app_function(user_input):
    if not user_input.strip():
        return "⚠️ Please enter a story idea."
    return generate_storyboard(user_input)

with gr.Blocks() as demo:
    gr.Markdown("# 🎬 AI Storyboard Creator")
    gr.Markdown("Turn your ideas into scripts, visuals, and narration (Beginner Friendly)")
    with gr.Column():
        user_input = gr.Textbox(
            label="💡 Enter Your Story Idea",
            placeholder="Example: A boy discovers a magical book that brings drawings to life...",
            lines=3
        )
        generate_btn = gr.Button("✨ Generate Storyboard")
        output = gr.Textbox(label="📜 Generated Storyboard", lines=25)

    generate_btn.click(fn=app_function, inputs=user_input, outputs=output)

if __name__ == "__main__":
    # Run locally; setting share=False as default for local use
    demo.launch(share=False)
