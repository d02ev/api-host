import { config } from '../config/index.js';
import { createSupabase } from '../infra/supabase.js';
import { createGithub } from '../infra/github.js';
import { createTelegram } from '../infra/telegram.js';

export const initDependencies = () => {
    const supabase = createSupabase(config.supabase);
    const github = createGithub(config.github);
    const telegram = createTelegram(config.telegram);

    return {
        supabase,
        github,
        telegram
    }
};