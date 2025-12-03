import type { Supplier } from "./Supplier";

export interface Ingredient {
    id?: number;
    name: string;
    supplier?: Supplier | null;
    us_measure: string;
    standard_measure: string;
    gluten_free: boolean;
    quantity_on_hand: number;
    reorder_point: number;
    avg_unit_cost: number;
}