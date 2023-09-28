# Guida al fine tune di ChatGPT

Questo è un semplicissimo script per creare un fine-tuning di ChatGPT. Accompagna questo video:

https://youtu.be/v9KVX_9XySE

## Istruzioni per chi non ha idea di come usare python

Prima di tutto, bisogna installare Python se non lo hai già fatto: https://www.python.org/downloads/

Poi, entrare sul Command Prompt, e installare openai con questo comando: `pip install openai`

E in ogno caso, anche se hai già usato openai, aggiornarlo: `pip install --upgrade openai`

Poi copiare da qualche parte i due script .py, creare il file data.json nel formato descritto nel video.

Infine, per far partire il fine tuning, entrare col Command Prompt dentro alla cartella che contiene tutti i file, e far partire lo script: `python create_ft.py`

Per vedere a che punto è l'addestramento (ci mette pochi minuti in genere), cambiare in `retrieve_job.py` il jobname con il nome che viene dato da create_ft.py quando viene lanciato lo script, e far partire questo script: `python retrieve_job.py`