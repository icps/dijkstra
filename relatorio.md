# Modelagem

A modelagem deste problema se deu da seguinte forma: seja o grafo não-orientado G = (V, E), onde V
representa os institutos da UFMG e (u, v, w) ∈ E as ligações entre os institutos u e v, com distância w.
Uma vez que deseja-se somente caminhos de tamanho ı́mpar, foi necessário obter o grafo G 0 , que é a seguinte
transformação de G: para cada aresta (u, v) em G, adiciona-se duas novas arestas em G 0 , que são (u_par,
v_impar, w) e (u_impar, v_par, w). Para a implementação da modelagem, como o grafo é não-orientado, ou
seja, se pode caminhar nas duas direções de um instituto a outro, adiciona-se mais duas arestas na lista de
adjacência, (v_impar, u_par, w) e (v_par, v_impar, w). Para que cada vértice u tenha nome diferente em
sua versão par e ı́mpar, calcula-se o pares como (u × 10) + 2 e os ı́mpares como (u × 10) + 1. Assim, por
exemplo, para o vértice 1, tem-se o 12 como o 1 par e o vértice 11 como o 1 ı́mpar. A figura 1 mostra um
exemplo de G 0 , obtido após a transformação descrita.
Após obter o novo grafo G 0 , como queremos a menor distância entre o instituto ICEX e o bandejão (e
como são distâncias, nunca serão valores negativos), utilizamos o algoritmo Dijkstra, a partir do vértice 12
(isto é, a partir da versão par do vértice 1, pois não há aresta (1, 1), então o caminho de 1 para 1 é de
tamanho zero, um número par) para a versão ı́mpar do vértice N.

Figure 1: Exemplo de grafo G', obtido a partir de G

![figure](https://github.com/icps/odd_dijkstra/blob/main/PAA%20TP1.png)

# Análise de Complexidade

Para a leitura da entrada de tamanho E, precisa-se ler toda a entrada, logo, temos um custo O(E). A adição
de arestas no grafo G', que consiste em adicionar um novo valor na lista de adjacências, assim como a criação
dos vértices pares e ı́mpares, possuem custo constante. Para o algoritmo de Dijkstra, utilizamos uma fila de
prioridade mı́nima, e supomos que o grafo é esparso (pois é pouco provável que um instituto tenha caminho
para todos os outros): o custo para a leitura da fila (o laço while), que tem no máximo O(E) vértices, é
O(E). O custo para a leitura dos vizinhos na lista de adjacência (o laço for ) é O(E)). As operações da fila
de prioridade (adicionar e retirar vértice) tem custo O(log E) cada. Assim, o nosso custo total é O(E log E).
