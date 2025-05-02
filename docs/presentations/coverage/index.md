## Code Coverage - Understand the GCOV Report

---

## Code Example

```c
boolean CheckAbort(
  boolean abort_commanded,
  boolean valid_abort_command,
  boolean off_course
) {
    if ((abort_commanded && valid_abort_command) || off_course)
    {
        return TRUE;
    }
    else
    {
        return FALSE;
    }
}

```

<div class="bottom-aligned-text">
<a href="https://www.youtube.com/watch?v=k0_PF8MtEEo">See full youtube video example from NASA Engineer Dr. Lorraine Prokop</a> <!-- .element: class="highlighted-yellow-transparent-background-small" -->
</div>

---

<div class="raw monospace" style="float: left; width: 55%">

```c

boolean CheckAbort(
  boolean A,
  boolean B,
  boolean C
) {
    if ((A && B) || C)
    {
        return TRUE;
    }
    else
    {
        return FALSE;
    }
}

```

</div>

<div class="raw monospace" style="float: right; width: 45%">

```asm

CheckAbort:
        push    rbp
        mov     rbp, rsp
        mov     ecx, esi
        mov     eax, edx
        mov     edx, edi
        mov     BYTE PTR [rbp-4], dl
        mov     edx, ecx
        mov     BYTE PTR [rbp-8], dl
        mov     BYTE PTR [rbp-12], al
        cmp     BYTE PTR [rbp-4], 0 ; compare A
        je      .L2
        cmp     BYTE PTR [rbp-8], 0 ; compare B
        jne     .L3
.L2:
        cmp     BYTE PTR [rbp-12], 0 ; compare C
        je      .L4
.L3:
        mov     eax, 1
        jmp     .L5
.L4:
        mov     eax, 0
.L5:
        pop     rbp
        ret

```

</div>

--

## [`--coverage`](https://godbolt.org/z/3e8MvjKdP)

---

### Binary Decision Diagram (BDD)

<div class="raw monospace" style="float: left; width: 60%">

```c
boolean CheckAbort(
  boolean A,
  boolean B,
  boolean C
) {
    if ((A && B) || C)
    {
        return TRUE;
    }
    else
    {
        return FALSE;
    }
}

```

</div>

<div class="mermaid" style="float: right; width: 40%">
  <pre>
    %%{init: {'theme': 'dark', 'themeVariables': { 'darkMode': true }}}%%
    graph TD
      A{{A?}} -- "true" --> B{{B?}}
      A -- "false" --> C{{C?}}

      B -- "true" --> E[[return 1]]
      B -- "false" --> C

      C -- "true" --> G[[return 1]]
      C -- "false" --> F[[return 0]]

  </pre>
</div>

---

<div class="mermaid">
  <pre>
    %%{init: {'theme': 'dark', 'themeVariables': { 'darkMode': true }}}%%
    graph TD
      A{{A?
      *cond0*}} -- "true
      *b0*" --> B{{B?
      *cond1*}}
      A -- "false
      *b1*" --> C{{C?
      *cond2*}}
      B -- "true
      *b2*" --> E[[return 1]]
      B -- "false
      *b3*" --> C
      C -- "true
      *b4*" --> G[[return 1]]
      C -- "false
      *b5*" --> F[[return 0]]
  </pre>
</div>

---

<div class="mermaid" style="float: left; width: 40%;">
  <pre>
    %%{init: {'theme': 'dark', 'themeVariables': { 'darkMode': true }}}%%
    graph TD
      A{{A?
      *cond0*}} -- "true
      *b0*" --> B{{B?
      *cond1*}}
      A -- "false
      *b1*" --> C{{C?
      *cond2*}}
      B -- "true
      *b2*" --> E[[return 1]]
      B -- "false
      *b3*" --> C
      C -- "true
      *b4*" --> G[[return 1]]
      C -- "false
      *b5*" --> F[[return 0]]
  </pre>
</div>

<div class="monospacesmall" style="float: right; width: 60%">

|     | `A` <br/> `(cond_0)` | `B` <br/> `(cond_1)` | `C` <br/> `(cond_2)` | `Return Value` |
| :-: | :------------------: | :------------------: | :------------------: | :------------: |
|  1  |     true (`b0`)      |     true (`b2`)      |          X           |      true      |
|  2  |     true (`b0`)      |     false (`b3`)     |     true (`b4`)      |      true      |
|  3  |     true (`b0`)      |     false (`b3`)     |     false (`b5`)     |     false      |
|  4  |     false (`b1`)     |          X           |     true (`b4`)      |      true      |
|  5  |     false (`b1`)     |          X           |     false (`b5`)     |     false      |

</div>

---

## Demo! 📽️

<!-- .slide: data-background-color="green" -->

GCC >=14 MC/DC coverage report.

---

## Tree vs Non-Tree Like BDD

---

<div  class="monospace">
<p> Non tree-like structure BDD: <br> (A && B) || C </p>
<div class="mermaid">
  <pre>
    %%{init: {'theme': 'dark', 'themeVariables': { 'darkMode': true }}}%%
    graph TD
      A{{A?
      *cond0*}} -- "true
      *b0*" --> B{{B?
      *cond1*}}
      A -- "false
      *b1*" --> C{{C?
      *cond2*}}:::drawRed
      B -- "true
      *b2*" --> E[[return 1]]
      B -- "false
      *b3*" --> C
      C -- "true
      *b4*" --> G[[return 1]]
      C -- "false
      *b5*" --> F[[return 0]]
      classDef drawRed stroke:#ff9999
  </pre>
</div>
</div>

---

<div  class="monospace"style="float: left; width: 40%;">
<div class="mermaid">
  <pre>
    %%{init: {'theme': 'dark', 'themeVariables': { 'darkMode': true }}}%%
    graph TD
      A{{A?
      *cond0*}}:::drawGreen -- "true
      *b0*" --> B{{B?
      *cond1*}}:::drawGreen
      A -- "false
      *b1*" --> C{{C?
      *cond2*}}:::drawRed
      B -- "true
      *b2*" --> E[[return 1]]
      B -- "false
      *b3*" --> C
      C -- "true
      *b4*" --> G[[return 1]]
      C -- "false
      *b5*" --> F[[return 0]]
      classDef drawRed stroke:#ff9999
      classDef drawGreen stroke:#99ff99
  </pre>
</div>
<p> Non tree-like structure BDD: <br> (A && B) || C </p>
</div>

<div  class="monospace"style="float: right; width: 40%;">
<div class="mermaid">
  <pre>
    %%{init: {'theme': 'dark', 'themeVariables': { 'darkMode': true }}}%%
    graph TD
      C{{C?
      *cond2*}}:::drawGreen -- "true
      *b4*" --> G[[return 1]]
      C -- "false
      *b5*" --> A{{A?
      *cond0*}}:::drawGreen
      A -- "true
      *b0*" --> B{{B?
      *cond1*}}:::drawGreen
      A -- "false
      *b1*" --> F[[return 0]]
      B -- "true
      *b2*" --> E[[return 1]]
      B -- "false
      *b3*" --> H[[return 0]]
      classDef drawGreen stroke:#99ff99
  </pre>
</div>
<p> 🌳 Tree-like structure BDD: <br> C || (A && B)</p>
</div>

---

## ❔ Questions ❔

<!-- .slide: data-background-color="green" -->

---

## Thank you!

<!-- .slide: data-background-color="pink" -->

Note:

Thank you for your attention!
