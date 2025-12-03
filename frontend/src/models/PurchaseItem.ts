import type { PurchaseOrder } from "./PurchaseOrder";
import type { Ingredient } from "./Ingredient";

export interface PurchaseItem {
    id?: number;
    purchase_order: PurchaseOrder;
    ingredient: Ingredient;
    quantity_ordered: number;
    unit_cost_at_purchase: number;
}