# Homebrewing Calculator

The Homebrewing Calculator is a tool designed to assist homebrewing enthusiasts in creating and fine-tuning their beer recipes. With this app, users can easily add malt, hops, and yeast from a pre-defined database to their recipes. The app automatically calculates important values such as: Original Gravity, Final Gravity, ABV and IBU. Additionally, users can write personalized notes to keep track of their recipe details and observations.

## Releases

The latest release can be found [here](https://github.com/AleksiSaxlund/Homebrewing-Calculator/releases).

## Documentation

- [user_guide.md](./documentation/user_guide.md)
- [changelog.md](./documentation/changelog.md)
- [specifications.md](./documentation/specifications.md)
- [architecture.md](./documentation/architecture.md)
- [testing_document.md](./documentation/testing_document.md)

## Command Line Commands

### Starting the Program:

  poetry run invoke start

### Running Tests:

  poetry run invoke test

### Test Coverage:

  poetry run invoke coverage-report

### Pylint Check:

  poetry run invoke lint

## Future Feature Roadmap 
1. Implement a database
2. Implement better calculation for IBU
3. Add save/load feature
4. ??

1.0.0 release when atleast 1-3 points implemented and working.
