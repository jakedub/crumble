export interface Supplier {
    id?: number;
    name: string;
    contact_name?: string | null;
    phone_number?: string | null;
    lead_time_days: number;
}