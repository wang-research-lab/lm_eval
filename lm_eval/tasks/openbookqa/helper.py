def openbookqa_prompt(input):
    question = input['question_stem']
    choices_text = input['choices']['text']
    choices_label = input['choices']['label']
    choices_formatted = "\n".join([f"{label}: {text}" for label, text in zip(choices_label, choices_text)])

    return f"User: {question} Choose the best option from the choices provided:\n{choices_formatted}\nAssistant: The best answer is\""