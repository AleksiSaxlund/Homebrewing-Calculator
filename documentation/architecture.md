# Architecture

## Application Structure

### Code Package Structure

```mermaid

classDiagram
    class ui
    class services
    class repositories
    class entities

    ui --> services
    services --> entities
    services --> repositories
    repositories --> entities

```

The ui directory is responsible for the user interface, services handles the application logic and calculations, repositories communicates with the databases, and entities directory defines classes representing ingredients and recipes.

### Class Structure

```mermaid

classDiagram
    class ui
    class malts_scrollarea
    class hops_scrollarea
    class yeasts_scrollarea
    class calculations_grid
    class manager_services
    class calculations_services
    class recipe
    class all_ingredients
    class ingredients_repository
    class notes_text_box

    ui "1" -- "1" malts_scrollarea
    ui "1" -- "1" hops_scrollarea
    ui "1" -- "1" yeasts_scrollarea
    ui "1" -- "1" calculations_grid
    ui "1" -- "1" notes_text_box
    malts_scrollarea -- manager_services
    hops_scrollarea -- manager_services
    yeasts_scrollarea -- manager_services
    calculations_grid -- manager_services
    manager_services "1" -- "1" recipe
    manager_services -- calculations_services
    manager_services -- ingredients_repository
    recipe "1" -- "1" calculations_services
    ingredients_repository "1" -- "*" all_ingredients
    calculations_services ..> all_ingredients
    manager_services ..> all_ingredients

```
## Databases

The application has three databases, one for each main ingredient (Malts, Hops, and Yeasts). Each database has its own repository class responsible for retrieving data from the databases. In the future, these classes can be expanded to include features for adding and removing data from the databases.

## Functionalities

Basic functionalities of the application described using sequence diagrams.

### Adding an Ingredient (Yeast) to the Recipe via GUI

```mermaid

sequenceDiagram
    actor user
    participant ui
    participant manager_services
    participant calculations_services
    participant recipe

    user ->> ui: Select yeast from combobox
    activate ui
    ui ->> manager_services: ingredient_added(chosen_yeast, "yeasts")
    activate manager_services
    manager_services ->> recipe: ingredients["yeasts"].append(yeast)
    activate recipe
    recipe -->> manager_services: none
    deactivate recipe
    manager_services ->> manager_services: update_calculation()
    manager_services ->> calculations_services: get_all_calculations()
    activate calculations_services
    calculations_services ->> calculations_services: *calls calculation functions for all values
    calculations_services ->> recipe: 
    activate recipe
    recipe -->> calculations_services: *required ingredient data
    deactivate recipe
    calculations_services -->> manager_services: return results
    deactivate calculations_services
    manager_services ->> manager_services: format_calculation_results()
    manager_services ->> ui: return results
    deactivate manager_services
    ui ->> ui: data_grid.update_values(results)
    deactivate ui

```

### Changing the Recipe Size

```mermaid

sequenceDiagram
    actor user
    participant ui
    participant manager_services
    participant calculations_services
    participant recipe

    user ->> ui: Change volume from the line edit
    activate ui
    ui ->> manager_services: volume_changed(new_volume)
    activate manager_services
    manager_services ->> recipe: recipe.volume = new_volume
    activate recipe
    recipe -->> manager_services:  none
    deactivate recipe
    manager_services ->> manager_services: update_calculations()
    manager_services ->> calculations_services: get_all_calculations()
    activate calculations_services
    calculations_services ->> calculations_services: *calls calculation functions for all values
    calculations_services ->> recipe: 
    activate recipe
    recipe -->> calculations_services: *required ingredient data
    deactivate recipe
    calculations_services -->> manager_services: return results
    deactivate calculations_services
    manager_services ->> manager_services: format_calculation_results()
    manager_services ->> ui: return results
    deactivate manager_services
    ui ->> ui: data_grid.update_values(results)
    deactivate ui

```

*Marked with *: the get_all_calculations function executes all other functions defined in calculations_services and returns their results. Each of these functions retrieves the required data from the recipe object.

### Other Functionalities

As evident from the two previous diagrams, several changes made to the recipe in the application follow a similar pattern. An ingredient is selected and added to the recipe, followed by recalculations and updating of the new data for the user to see.
