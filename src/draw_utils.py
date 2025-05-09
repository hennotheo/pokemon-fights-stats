import matplotlib.pyplot as plt

def draw_pie_chart(values, value_labels, title):
    plt.figure(figsize=(4, 4))
    plt.pie(values, labels=value_labels, autopct='%1.1f%%', startangle=90)
    plt.title(title)

def save_png(filename):
    plt.savefig(F"output/{filename}", format='png', dpi=300)
    plt.close()