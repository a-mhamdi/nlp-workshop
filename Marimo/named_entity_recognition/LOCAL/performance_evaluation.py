def evaluate_ner_model(model, test_data):
    """
    Evaluate NER model performance
    """
    true_positives = 0
    false_positives = 0
    false_negatives = 0

    for text, annotations in test_data:
        # Get predicted entities
        doc = model(text)
        predicted_entities = set([
            (ent.text, ent.label_) for ent in doc.ents
        ])

        # Get true entities
        true_entities = set([
            (text[start:end], label)
            for start, end, label in annotations['entities']
        ])

        # Calculate metrics
        true_positives += len(predicted_entities & true_entities)
        false_positives += len(predicted_entities - true_entities)
        false_negatives += len(true_entities - predicted_entities)

    # Calculate precision, recall, F1
    precision = true_positives / (true_positives + false_positives)
    recall = true_positives / (true_positives + false_negatives)
    f1 = 2 * (precision * recall) / (precision + recall)

    return {
        'precision': precision,
        'recall': recall,
        'f1': f1
    }
