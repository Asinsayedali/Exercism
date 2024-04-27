list_of_colors=["black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white"]

def label(colors):
        result = (list_of_colors.index(colors[0]) * 10 + list_of_colors.index(colors[1])) * (10 ** list_of_colors.index(colors[2]))
        if result<1000:
            return str(result)+ ' ohms'
        if result < 10**6:
            return str(int(result / 1000)) + ' kiloohms'
        if result < 10**9:
            return  str(int(result/1000000)) + ' megaohms'
        if result >=10**9:
            return str(int(result / 1000000000)) + ' gigaohms'
