import type { Order } from "./Order";
import type { Product } from "./Product";

export interface OrderItem {
    id?: number;
    order: Order;
    product: Product;
    quantity: number;
    price_at_sale: number;
}