# Agent Hallucination Detector

A Python-based project that detects possible hallucinations in AI-generated answers by comparing them with a provided context.

The system checks whether an answer introduces unsupported entities, actions, or factual relationships that are not present in the original context. It uses rule-based Natural Language Processing with spaCy to analyze the context and answer.

## Features

* Detects entity hallucinations
* Detects intent hallucinations
* Detects semantic hallucinations
* Extracts named entities and proper nouns
* Extracts verbs to identify actions and intent
* Extracts subject–predicate–object triples
* Generates a structured JSON report
* Includes multiple sample test cases

## How It Works

The project evaluates an AI-generated answer at three levels.

### 1. Entity-Level Check

The system extracts entities such as people, organizations, locations, and proper nouns from the context and answer.

If the answer contains an entity that is not supported by the context, it is flagged as an **Entity Hallucination**.

**Example:**

* Context: France won the 2018 FIFA World Cup.
* Answer: Brazil won the 2018 FIFA World Cup.
* Result: Entity Hallucination.

### 2. Intent-Level Check

The system extracts verbs from the context and answer.

If the answer introduces an unsupported action or intent, it is flagged as an **Intent Hallucination**.

**Example:**

* Context: Tesla was founded in 2003.
* Answer: Tesla was acquired in 2003.
* Result: Intent Hallucination.

### 3. Semantic-Level Check

The system extracts subject–predicate–object triples from the context and answer.

If the answer changes a factual relationship from the context, it is flagged as a **Semantic Hallucination**.

**Example:**

* Context: Type 1 diabetes requires lifelong insulin therapy.
* Answer: Type 2 diabetes requires lifelong insulin therapy.
* Result: Semantic Hallucination.

## Project Structure

```text
Agent-Hallucination/
│
├── hallucination_detector.py
├── hallucination_detector1.py
├── test_run.py
├── requirements.txt
└── README.md
```

## Requirements

* Python 3.11 or Python 3.12
* spaCy 3.7.2
* `en_core_web_sm` spaCy English language model

> **Note:** The project may run immediately after dependency installation if the `en_core_web_sm` model is already available in your Python environment.

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Agent-Hallucination
```

### 2. Create a Virtual Environment

#### macOS / Linux

```bash
python3 -m venv hallucination_env
source hallucination_env/bin/activate
```

#### Windows

```bash
python -m venv hallucination_env
hallucination_env\Scripts\activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Running the Project

Run the sample test file:

```bash
python test_run.py
```

The program prints a JSON report containing extracted entities, predicates, semantic triples, hallucination details, and a final decision.

## Example Input

```python
context = """
Type 1 diabetes is an autoimmune condition in which the pancreas produces little or no insulin.
It requires lifelong insulin therapy.
"""

question = "Which type of diabetes requires lifelong insulin therapy?"

answer = "Type 2 diabetes requires lifelong insulin therapy."
```

## Example Output

```json
{
    "entity_level": {
        "context_entities": [
            "1",
            "2",
            "Type"
        ],
        "answer_entities": [
            "2"
        ],
        "hallucination": false
    },
    "intent_level": {
        "context_predicates": [
            "require",
            "manage",
            "produce"
        ],
        "answer_predicates": [
            "require"
        ],
        "hallucination": false
    },
    "semantic_level": {
        "context_triples": [
            [
                "diabetes",
                "manage",
                "changes"
            ],
            [
                "It",
                "require",
                "therapy"
            ],
            [
                "pancreas",
                "produce",
                "which"
            ]
        ],
        "answer_triples": [
            [
                "diabetes",
                "require",
                "therapy"
            ]
        ],
        "hallucination": true,
        "type": "Semantic Triple Mismatch",
        "details": [
            [
                "diabetes",
                "require",
                "therapy"
            ]
        ]
    },
    "final_decision": "Semantic Hallucination"
}
```

## Main Function

The main function used to evaluate hallucinations is:

```python
evaluate_hallucination(context, question, answer)
```

### Parameters

| Parameter  | Description                                     |
| ---------- | ----------------------------------------------- |
| `context`  | Original source information or document content |
| `question` | Question asked based on the context             |
| `answer`   | AI-generated answer that needs to be checked    |

### Return Value

The function returns a dictionary containing:

* Context entities
* Answer entities
* Context predicates
* Answer predicates
* Context semantic triples
* Answer semantic triples
* Hallucination details
* Final hallucination decision

## Possible Final Decisions

| Decision                    | Meaning                                                   |
| --------------------------- | --------------------------------------------------------- |
| `No Hallucination Detected` | The answer is supported by the context                    |
| `Entity Hallucination`      | The answer contains unsupported entities                  |
| `Intent Hallucination`      | The answer contains unsupported actions or verbs          |
| `Semantic Hallucination`    | The answer changes factual relationships from the context |

## Customizing Test Cases

Open `test_run.py` and modify the following variables:

```python
context = """
Add your source information here.
"""

question = "Add your question here."

answer = "Add the AI-generated answer to evaluate here."
```

Then run:

```bash
python test_run.py
```

## Troubleshooting

### spaCy Model Not Found

If you see this error:

```text
OSError: [E050] Can't find model 'en_core_web_sm'
```

install the English spaCy model using:

```bash
python -m spacy download en_core_web_sm
```

If the command does not work, install the compatible model package directly:

```bash
python -m pip install --no-cache-dir "https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1-py3-none-any.whl"
```

### spaCy Installation Error on Python 3.14

spaCy 3.7.2 may not work correctly with Python 3.14.

Use Python 3.11 or Python 3.12, create a new virtual environment, and install the dependencies again.

```bash
python3.12 -m venv hallucination_env
source hallucination_env/bin/activate
python -m pip install -r requirements.txt
```

## Limitations

* The project uses rule-based NLP checks.
* It may not correctly understand all complex sentence structures.
* Pronouns, synonyms, indirect references, and multi-step reasoning may not always be detected accurately.
* It works best with short factual contexts and direct answers.
* It does not currently use embeddings, transformer models, or external knowledge bases.

## Future Improvements

* Add sentence similarity scoring using embeddings
* Use transformer-based Natural Language Inference models
* Add confidence scores for hallucination detection
* Support multiple languages
* Add PDF and document input support
* Build a web interface using Streamlit or Flask
* Store hallucination reports in a database
* Add automated unit tests
* Add batch processing for multiple answers

## Technologies Used

* Python
* spaCy
* Natural Language Processing
* Rule-Based Entity Extraction
* Predicate Extraction
* Subject–Predicate–Object Triple Extraction

## Author

Vrisheeka Mulakala

## License

This project is created for educational and research purposes.
