from transformers import pipeline

def generate_qa(text, model_name="mistralai/Mistral-7B-Instruct-v0.1", num_questions=5):
    prompt = f"""
Text:
{text}

Generate {num_questions} question-answer pairs based on the text above.
Output must be JSON like:
[
  {{"question": "...", "answer": "..."}},
  ...
]
"""
    pipe = pipeline("text-generation", model=model_name, max_new_tokens=1024)
    output = pipe(prompt)[0]['generated_text']

    import re, json
    try:
        json_str = re.search(r"\[.*\]", output, re.DOTALL).group()
        return json.loads(json_str)
    except:
        return [{"error": "Failed to parse output", "raw_output": output}]
