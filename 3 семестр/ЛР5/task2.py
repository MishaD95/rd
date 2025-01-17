import matplotlib.pyplot as plt

def calculate_y(U, T, K, T0, n_steps):
    """
    Розрахунок значень y[k] за заданим рівнянням.
    :param U: Вхідний сигнал
    :param T: Постійна часу
    :param K: Коефіцієнт підсилення
    :param T0: Період дискретизації
    :param n_steps: Кількість кроків
    :return: Список значень y[k]
    """
    y = [0]  # Початкове значення y[0]
    for k in range(n_steps):
        next_y = (1 - T0 / T) * y[k] + (T0 / T) * K * U
        y.append(next_y)
    return y


def plot_results(U, T, K, T0, n_steps):
    """
    Побудова графіка залежності y[k].
    """
    y_values = calculate_y(U, T, K, T0, n_steps)
    plt.figure(figsize=(10, 5))
    plt.plot(range(len(y_values)), y_values, marker='o', label='y[k]')
    plt.title("Залежність y[k] від часу")
    plt.xlabel("Крок (k)")
    plt.ylabel("y[k]")
    plt.grid()
    plt.legend()
    plt.savefig("image.png")
    plt.show()
