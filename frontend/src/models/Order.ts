export interface Order {
    id?: number;
    squarespace_order_id: string;
    order_date: string; // ISO date-time
    total_amount: number;
    customer_email: string;
    is_synced_to_qb: boolean;
    raw_json_data: any;
}