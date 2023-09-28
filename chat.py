//fai in modo che questa classe prenda 2 parametri in ingresso: il primo è il testo della domanda, il secondo è il testo della risposta
//la classe deve restituire il testo della risposta


import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY","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")
completion = openai.ChatCompletion.create(
  model="ft:gpt-3.5-turbo-0613:personal:test-baustore-prod:83gaa8KQ",
  messages=[
    {"role": "system", "content": "Rispondimi con una query SQL"},
    {"role": "user", "content": "Come faccio a sapere qual'è l'importo massimo delle fatture di questo mese?"}
  ]
)
print(completion.choices[0].message)