def parse_document(document):
    document["_id"] = str(document["_id"])
    return document


def parse_iterator(iterator):
    return [parse_document(document) for document in iterator]
