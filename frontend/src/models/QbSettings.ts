export interface QbSettings {
    id?: number;
    qb_access_token: string;
    qb_refresh_token: string;
    qb_realm_id: string;
    last_sync_time?: string | null; // ISO date-time
}