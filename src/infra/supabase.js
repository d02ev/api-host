import { createClient } from '@supabase/supabase-js';

export const createSupabase = config => {
    return createClient(config.projectUrl, config.serviceRoleKey);
};