def my_languages(results):
    result = list(dict(i for i in sorted(results.items(), key=lambda item: item[1], reverse=True) if i[1] >= 60).keys())
    return result
