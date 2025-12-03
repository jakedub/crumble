import type { Recipe } from "./Recipe";
export interface Batch {
    id?: number;
    recipe: Recipe;
    quantity_produced: number;
    start_time: string; // ISO date-time
    end_time?: string | null; // ISO date-time or null
}