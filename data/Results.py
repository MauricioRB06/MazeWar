
import matplotlib.pyplot as plt

# Resultados Datos, Primer Avance

fig, ax = plt.subplots()
Celda = ['4', '5', '6', '10', '15', '20', '25', '30', '40', '50', '60', '100']
segundos = {'Arbol Binario': [4.393938779830933, 2.734421491622925, 1.922520637512207, 0.7350101470947266,
                              0.32111358642578125, 0.17792034149169922, 0.1219637393951416, 0.08099222183227539,
                              0.047516584396362305, 0.030001163482666016, 0.023002147674560547, 0.006011009216308594 ],
            'Retroceso Recursivo': [4.540259122848511, 2.9908721446990967, 2.0523548126220703, 0.7112786769866943,
                                    0.32094621658325195, 0.18314695358276367, 0.12615561485290527, 0.08529877662658691,
                                    0.04999804496765137, 0.0309903621673584, 0.017996788024902344, 0.00700235366821289]}
ax.plot(Celda, segundos['Arbol Binario'])
ax.plot(Celda, segundos['Retroceso Recursivo'])
ax.set_xlabel("Tamaño Celdas", fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'green'})
ax.set_ylabel("Segundos", fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'green'})
ax.set_ylim([0, 5])
ax.set_yticks(range(0, 5))
plt.show()
