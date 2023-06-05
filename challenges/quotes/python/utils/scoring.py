import copy
from collections import defaultdict
import json

import spacy
from spacy.training import Example
from spacy.training.scorer import PRFScore

# TODO= docs[n]['file_upload'].split('_')[1]

def extract_labelstudio_annotations(labelstudio_doc):
    id2entity = {
        ann["id"]: (int(ann["value"]["start"]), int(ann["value"]["end"]), ann["value"]["labels"][0])
        for ann in labelstudio_doc["annotations"][0]["result"]
        if ann['type'] == 'labels'
    }
    relations = [
        (id2entity[ann['from_id']][:2], id2entity[ann['to_id']][:2])
        for ann in labelstudio_doc["annotations"][0]["result"]
        if ann['type'] == 'relation'
    ]
    spans = {'0': [tuple(val) for val in id2entity.values()]}
    
    doc_copy = copy.deepcopy(labelstudio_doc)
    text = doc_copy['data'].pop('content')
    res = {
        'metadata': labelstudio_doc['data'],
        'text': text,
        #'entities': list(id2entity.values()),
        'spans': spans,
        'relations': relations,
    }
    
    return res


def lbjson2data(fpath, split=True):
    with open(fpath) as dump:
        dataset = json.load(dump)

    if split:
        datasets = defaultdict(list)
        for doc in dataset:
            sub_dataset = doc['file_upload'].split('_')[1]
            if sub_dataset == 'test':
                sub_dataset = 'train'
            elif sub_dataset == 'train':
                sub_dataset = 'test'
            datasets[sub_dataset].append(extract_labelstudio_annotations(doc))

        return datasets

    else:
        annotated_docs = [
            extract_labelstudio_annotations(doc)
            for doc in dataset
        ]

        return annotated_docs


def lbjson2spacyexamples(fpath_or_data, nlp):
    spacy_gold_example = []
    data = fpath_or_data
    if isinstance(fpath_or_data, str):
        data = lbjson2data(fpath_or_data)
    for doc in data:
        spacy_gold_example.append(
            Example.from_dict(
                nlp(doc['text']),
                {
                    'text': doc['text'],
                    #'entities': doc['entities'],
                    #TODO: add relations annotation support
                    'spans': doc['spans'],
                },
            )
        )
    return spacy_gold_example


def get_dataset_stats(data):
    from collections import Counter
    stats = {
        'nb_docs': len(data),
        'entities': Counter([
            ent[2]
            for doc in data
            for spans in doc['spans'].values()
            for ent in spans
        ]),
        'relations': sum([len(doc['relations']) for doc in data]),
    }
    stats['entities']['total'] = sum(list(stats['entities'].values()))

    return stats


def score(predicted, gold_standard, nlp):
    predicted_docs = lbjson2spacyexamples(predicted)
    gold_docs = lbjson2spacyexamples(gold_standard)
    examples = [
        Examples(pred, gold)
        for pred, gold in zip(predicted_docs, gold_docs)
    ]

    score = Scorer.score_spans(
        examples,
        '0',
        getter=lambda d, k: d.spans[k]
    )
    
    return score


def naive_prf_spans_score(predicted, gold_standard):
    pred_spans = [s for spans in predicted['spans'].values() for s in spans]
    gold_spans = [s for spans in gold_standard['spans'].values() for s in spans]
    scorer = PRFScore()
    return scorer.score_set(set(pred_spans), set(gold_spans))


def main():
    import sys
    input_path, output_path = sys.argv[1:]

    datasets = lbjson2data(input_path)
    for dataset_part, dataset in datasets.items():
        print (dataset)
        out_fpath = output_path + "." + dataset_part
        with open(out_fpath, 'w') as dump:
            json.dump(dataset, dump, indent=2, ensure_ascii=False)

    return

    data = lbjson2data(input_path)
    dataset_stats = get_dataset_stats(data)

    nlp = spacy.load("fr_core_news_lg")
    examples = lbjson2spacyexamples(data, nlp)

    dataset_stats['nb_tokens'] = sum([len(eg.reference) for eg in examples])
    print(dataset_stats)

    with open(output_path, 'w') as f_out:
        json.dump(
            data,
            f_out,
            indent=2,
            ensure_ascii=False,
        )


if __name__ == '__main__':
    main()
