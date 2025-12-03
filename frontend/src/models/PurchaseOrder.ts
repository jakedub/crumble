import type { Supplier } from "./Supplier";

export interface PurchaseOrder {
    id?: number;
    supplier: Supplier;
    order_date: string; // ISO date
    total_cost: number;
    qb_expense_id: string;
}