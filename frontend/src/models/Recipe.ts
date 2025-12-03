import type { Product } from "./Product";

export interface Recipe {
    id?: number;
    product: Product;
    batch_yield_qty: number;
    batch_yield_unit: string;
}