import type { Recipe } from "./Recipe";
import type { Ingredient } from "./Ingredient";

export interface RecipeItem {
    id?: number;
    recipe: Recipe;
    ingredient: Ingredient;
    quantity_required: number;
}