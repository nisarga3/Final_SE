import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd


def parse_list(lis):
    sales = []
    dates = []
    for ele in lis:
        sales.append(ele[0])
        dates.append(ele[1])
    res = pd.DataFrame(dict(map(lambda i, j: (j, i), sales, dates)))
    return res


def plot_final(lis):
    res = parse_list(lis)
    fig = px.line(res, x="Dates", y="Sales", title="Sales of the week")
    fig.show()
