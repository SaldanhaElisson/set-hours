# set-hours

## Descrição do Problema 
**Definição dos Hoário de Cursos em um Evento**

_Um evento vai oferecer *K**minicursos de uma hora de duração cada. Dessa, forma, os organizadores do evento vão definir os horário em **slots** de uma hora de duração,  por exemplo, 8:00-9:00, 9:00-10:00, 10:00-11:00, e assim por diante. Os participantes podem se inscrever em mais de um minicurso, Logo, a organização do evento deseja agendars horários dos minicurssos de forma a atender as incrições dos participantes, ou seja, **minicursos que possuem inscrições de um mesmo participante não podem ser ofertados no mesmo horário**_

### Dados de entrada

- [ ]  **K** -> Conjunto de minicursos
- [ ]  **M** -> Conjunto de horário/slots disponíveis 
- [ ]  **P(1, J)** -> Cursos com matrículas simultâneas


### Exemplo

```Entrada:
# Minicursos:
1 HTML
2 PHP
3 MySQL
4 Swift
# Slots: 3
# Pares de minicursos com inscrições em comum:
1 2
2 3
2 4
3 4
Saída:
1 s1
2 s3
3 s1
4 s2
```

### Variáveis 
Vamos utilizar ```Xc,s``` oara reoresebtar que o minicurso _c_  é ofertado no slot _s_

### Restrições
1 . Cada minicurso deve ser ofertado em pleo menos um slot.
``` 
(x1,1 v X1,2 v X1,3 v .... v X1,s) ^ ..... ^ (Xc, 1 v Xc,2 v Xc,3 ... Xc,s)
```

2. Cada minicurso deve ser ofertado em no máximo um slot
```
~(X,1,1 ^ X1,2) ^ ~(X1,1 ^ X1,3) ^ ~(X1,1 ^ X1,4) ... ^ ~(Xc,s-1 ^ Xc, s)
```

3. 
