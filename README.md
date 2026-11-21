# SpecimenScout

Identify a mystery specimen by asking the most informative available yes/no question.

The agent chooses the available trait that most evenly splits the surviving species. The sample observations simulate answers from a user. Inspect trace to see how each answer narrows the list. Only include traits defined in the catalog.

## Run locally

From this folder with Python 3.8 or newer, run the included synthetic example and tests. Only the standard library is required.

```bash
python3 app.py
python3 -m unittest -v
```

Copy sample.json and edit its values, then run `python3 app.py your-input.json`.

## Sample output

```json
{
  "candidates": [
    "bat"
  ],
  "trace": [
    {
      "question": "feathers",
      "answer": false,
      "remaining": [
        "bat",
        "rabbit"
      ]
    },
    {
      "question": "nocturnal",
      "answer": true,
      "remaining": [
        "bat"
      ]
    }
  ]
}
```
