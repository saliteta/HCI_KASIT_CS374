import gradio as gr
import openai


import openai
import gradio

# Set the API key
openai.api_key = "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"


MODEL = "text-davinci-003"



def generate_text(user_input, mode):

    if mode == "boss":
        question_1 = f"I want to ask my boss some question, could you help me repherase my sentence? {user_input}"
        question_2 = f"I want to ask my boss some question, could you give me some basic principle for how to change it? {user_input}"
    elif mode == "mentor":
        question_1 = f"I want to ask my mentor some question, could you help me repherase my sentence? {user_input}"
        question_2 = f"I want to ask my mentor some question, could you give me some basic principle for how to change it? {user_input}"
    elif mode == "":
        question_1 = f"I want to ask my co-worker some question, could you help me repherase my sentence? {user_input}"
        question_2 = f"I want to ask my co-worker some question, could you give me some basic principle for how to change it? {user_input}"
    rephrased_text = openai.Completion.create(
        engine=MODEL,
        prompt=question_1,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    suggestion = openai.Completion.create(
        engine=MODEL,
        prompt=question_2,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = rephrased_text.choices[0].text
    response += '\n'+ suggestion.choices[0].text
    return response

prompt_input = gr.inputs.Textbox(lines=5, label="Prompt")
mode_input = gr.inputs.Radio(choices=["boss", "mentor", "co-worker"], label="Output Mode")
output_text = gr.outputs.Textbox(label="Generated Text")

gr.Interface(
    fn=generate_text,
    inputs=[prompt_input, mode_input],
    outputs=output_text,
    title="Communication Fedback System",
    description="Give one some feed back when one tries to talk to a group of specific roles",
    theme= gr.themes.Soft(
    primary_hue="zinc",
    secondary_hue="blue",
    neutral_hue="violet",
)
).launch()
