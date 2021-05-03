# Python calculator

This project contains a python calculator that uses [Reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation) as its syntax.
The project currently supports basic binary operations as well as exp and log and has functionality to record user history.


## Documentation

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)

## Install
1. Install dependencies with the command

```bash
poetry install
```

## Commands

### Launching the calculator

Launch the calculator with the command:

```bash
poetry run invoke start
```

### Testing

Tests are done using the command:

```bash
poetry run invoke test
```

### Test Coverage Report

Test coverage report can be generated using the command:

```bash
poetry run invoke coverage-report
```

### Linting

Pylint report can be obtained using the command:

```bash
poetry run invoke lint
```
