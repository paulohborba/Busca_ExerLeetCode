# [41. Primeiro Positivo Ausente (First Missing Positive)](https://leetcode.com/problems/first-missing-positive/description/)

**Dificuldade:** Difícil  
**Tópicos:** Array, Hash Table
**Descrição:**

Dado um array de inteiros não ordenado chamado  `nums`. Retorne o **menor inteiro positivo** que **não está presente** em `nums`.

Você deve implementar um algoritmo que execute em tempo `0(n)` e use espaço auxiliar `0(1)`.

---

## Exemplos:

### Exemplo 1:

**Entrada:** `nums = [1,2,0]`  

**Saída:** `3`  

**Explicação:** Os números no intervalo `[1,2]` estão todos no array.

---

### Exemplo 2:

**Entrada:** `nums = [3,4,-1,1]` 

**Saída:** `2`

**Explicação:** `1` está no array, mas `2` está ausente.

---

### Exemplo 3:

**Entrada:** `nums = [7,8,9,11,12]`

**Saída:** `1`

**Explicação:** O menor inteiro positivo, `1`, está ausente.

---

## Restrições:

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`