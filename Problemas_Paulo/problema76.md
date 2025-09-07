# [76. Subcadeia de Janela Mínima (Minimum Window Substring)](https://leetcode.com/problems/minimum-window-substring/description/)

**Dificuldade:** Difícil  
**Tópicos:** Hash Table, String, Sliding Window
**Descrição:**

Dadas duas strings `s` e `t`, de comprimentos `m` e `n` respectivamente, retorne a **subcadeia de janela mínima** de `s` de forma que cada caractere em `t` (incluindo duplicatas) esteja incluído na janela. Se não houver tal subcadeia, retorne a string vazia `" "`.

Você deve implementar um algoritmo que execute em tempo `0(n)` e use espaço auxiliar `0(1)`.

Os casos de teste serão gerados de forma que a resposta seja **única**.

---

## Exemplos:

### Exemplo 1:

**Entrada:** `s = "ADOBECODEBANC"`, `t = "ABC"`  

**Saída:** `"BANC"`  

**Explicação:** A subcadeia de janela mínima "BANC" inclui 'A', 'B' e 'C' da string `t`.

---

### Exemplo 2:

**Entrada:** `s = "a"`, `t = "a"`  

**Saída:** `"a"`  

**Explicação:** A string `s` inteira é a janela mínima.

---

### Exemplo 3:

**Entrada:** `s = "a"`, `t = "aa"`  

**Saída:** `""`  

**Explicação:** Os dois 'a's de `t` devem ser incluídos na janela. Como a maior janela de `s` tem apenas um 'a', retorne a string vazia.
---

## Restrições:

- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10^5`
- `s` e `t` consistem em letras do alfabeto inglês, maiúsculas e minúsculas.