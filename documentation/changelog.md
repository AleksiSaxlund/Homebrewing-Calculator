# Changelog

## Week 1

## Week 2

- Project started
- Created classes for recipe, malts, hops, and yeasts
- Established databases
- Created malts_repository class for reading malt database
- Created calculations_services class for handling calculations

## Week 3

- Created index.py, which serves as an initial version of the final application
- Added functionality to calculations_services class
- Created tests for calculations_services class
- Defined invoke tasks

## Week 4

- It is now possible to add hops and yeasts to the recipe
- Final gravity, ABV, and SRM can also be calculated
- Calculations are automatically displayed after changes
- All ingredients can be retrieved from the database and directly added to the recipe
- Fixed an error in the yeast database
- Created management_services for application logic

## Week 5

- Partially implemented graphical user interface (GUI)
- Added IBU calculation
- Added notes feature
- Created manager_services to handle application logic
- Increased test coverage

## Week 6

- Transitioned to the graphical user interface
- Removed unnecessary code related to the text-based user interface
- Added DOCSTRING to almost all classes outside of the user interface

## Week 7

- Fixed bugs
- Added tests
- Updated documentation
- Added DOCSTRINGs

## v0.1.0-alpha

- Created poetry environment
- Defined invoke tasks for running certain commands
- Users can add malts, hops, and yeast from the database to the recipe.
- Users can specify the batch size.
- After each addition, the following default values are calculated and displayed to the user:
  - Original Gravity
  - Final Gravity
  - ABV (Alcohol by Volume)
  - IBU (International Bitterness Units)
  - SRM (Standard Reference Method)
- Users can write separate notes about the recipe.
- No SQL databases for the ingredients currently
- GUI
- Unittesting for the existing classes
- English documentation
