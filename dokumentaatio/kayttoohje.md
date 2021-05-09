# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/nikpaa/ot-harjoitustyo/releases) lähdekoodi valitsemalla alta "Source code".

Sovellus on laskin, joka toimii [käänteisen puolalaisen notaation](https://en.wikipedia.org/wiki/Reverse_Polish_notation) esitysmuodon mukaisesti. Sovellusta käytetään komentoriviltä.

## Ohjelman käynnistäminen

Asenna ensin riippuvuudet komennolla:

```bash
poetry install
```

Nyt ohjelman voi käynnistää komennolla:

```
poetry run invoke start
```

**Suosittelen kuitenkin käynnistämään ohjelman manuaalisesti suorittamalla komennon `python3 src/calculator.py`, koska poetry ei tue askelpalautinta.**
