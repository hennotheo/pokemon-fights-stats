def filter_with_other_category(data, min_percent):
    type_counts = data.value_counts(normalize=True) * 100

    type_counts_filtered = type_counts[type_counts >= min_percent]
    type_counts_filtered["Other"] = type_counts[type_counts < min_percent].sum()
    return type_counts_filtered