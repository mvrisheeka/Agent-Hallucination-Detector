import spacy
from typing import List, Tuple, Dict

nlp = spacy.load("en_core_web_sm")


# --------------------------------------------------
# ENTITY EXTRACTION (Improved)
# --------------------------------------------------
def extract_entities(text: str) -> List[str]:
    doc = nlp(text)

    # Named entities
    ner_entities = [ent.text.strip() for ent in doc.ents]

    # Proper nouns fallback
    proper_nouns = [token.text for token in doc if token.pos_ == "PROPN"]

    return list(set(ner_entities + proper_nouns))


# --------------------------------------------------
# PREDICATE EXTRACTION (Intent)
# --------------------------------------------------
def extract_predicates(text: str) -> List[str]:
    doc = nlp(text)
    return list(set([token.lemma_ for token in doc if token.pos_ == "VERB"]))


# --------------------------------------------------
# IMPROVED TRIPLE EXTRACTION
# Handles:
# - Direct objects
# - Prepositional objects
# - Copula constructions
# - Passive voice
# --------------------------------------------------
def extract_triples(text: str) -> List[Tuple[str, str, str]]:
    doc = nlp(text)
    triples = []

    for sent in doc.sents:
        for token in sent:

            # Only consider verbs as predicates
            if token.pos_ == "VERB":

                subject = None
                obj = None

                # Find subject
                for child in token.children:
                    if child.dep_ in ["nsubj", "nsubjpass"]:
                        subject = child.text

                # Find direct object
                for child in token.children:
                    if child.dep_ in ["dobj", "attr"]:
                        obj = child.text

                # Find prepositional object
                for child in token.children:
                    if child.dep_ == "prep":
                        for subchild in child.children:
                            if subchild.dep_ == "pobj":
                                obj = subchild.text

                if subject and obj:
                    triples.append((
                        subject.strip(),
                        token.lemma_.strip(),
                        obj.strip()
                    ))

    return triples


# --------------------------------------------------
# MAIN EVALUATION FUNCTION
# --------------------------------------------------
def evaluate_hallucination(context: str,
                           question: str,
                           answer: str) -> Dict:

    report = {
        "entity_level": {},
        "intent_level": {},
        "semantic_level": {},
        "final_decision": None
    }

    # -----------------------------
    # Extraction
    # -----------------------------
    context_entities = set(extract_entities(context))
    answer_entities = set(extract_entities(answer))

    context_predicates = set(extract_predicates(context))
    answer_predicates = set(extract_predicates(answer))

    context_triples = set(extract_triples(context))
    answer_triples = set(extract_triples(answer))

    report["entity_level"]["context_entities"] = list(context_entities)
    report["entity_level"]["answer_entities"] = list(answer_entities)

    report["intent_level"]["context_predicates"] = list(context_predicates)
    report["intent_level"]["answer_predicates"] = list(answer_predicates)

    report["semantic_level"]["context_triples"] = list(context_triples)
    report["semantic_level"]["answer_triples"] = list(answer_triples)

    # --------------------------------------------------
    # 1️⃣ ENTITY LEVEL CHECK
    # --------------------------------------------------
    ooc_entities = answer_entities - context_entities

    if ooc_entities:
        report["entity_level"]["hallucination"] = True
        report["entity_level"]["type"] = "Entity Out-of-Context"
        report["entity_level"]["details"] = list(ooc_entities)
        report["final_decision"] = "Entity Hallucination"
        return report
    else:
        report["entity_level"]["hallucination"] = False

    # --------------------------------------------------
    # 2️⃣ INTENT LEVEL CHECK
    # --------------------------------------------------
    intent_mismatch = answer_predicates - context_predicates

    if intent_mismatch:
        report["intent_level"]["hallucination"] = True
        report["intent_level"]["type"] = "Intent Mismatch"
        report["intent_level"]["details"] = list(intent_mismatch)
        report["final_decision"] = "Intent Hallucination"
        return report
    else:
        report["intent_level"]["hallucination"] = False

    # --------------------------------------------------
    # 3️⃣ SEMANTIC LEVEL CHECK
    # --------------------------------------------------
    semantic_mismatch = answer_triples - context_triples

    if semantic_mismatch:
        report["semantic_level"]["hallucination"] = True
        report["semantic_level"]["type"] = "Semantic Triple Mismatch"
        report["semantic_level"]["details"] = list(semantic_mismatch)
        report["final_decision"] = "Semantic Hallucination"
        return report
    else:
        report["semantic_level"]["hallucination"] = False

    # --------------------------------------------------
    # 4️⃣ NO HALLUCINATION
    # --------------------------------------------------
    report["final_decision"] = "No Hallucination Detected"

    return report